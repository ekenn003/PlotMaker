import os, sys
import array
import ROOT
from tools.CMS_lumi import CMS_lumi
import tools.tdrstyle as tdrstyle
from tools.tools import getXsec
import logging
import math
from collections import OrderedDict
from variables import varnames


## ___________________________________________________________
class PlotBase(object):
    '''Plot base'''
    def __init__(self, args):
        # set batch mode
        ROOT.gROOT.SetBatch(ROOT.kTRUE)
        # empty sample lists
        self.mcsamplelist = {}
        self.datasamplelist = {}
        self.varnames = varnames
        # set tdr style
        tdrstyle.setTDRStyle()
        # CMS_lumi parameters
        self.iPeriod = 4
        self.iPos = 0
        # blinding region
        self.blindLow = 122.
        self.blindHigh = 128.



    ## _______________________________________________________
    def plot(self):
        '''Dummy function overridden in the derived class'''
        pass

    ## _______________________________________________________
    def getLegendCoordinates(self, pos, w, h):
        '''
        Legend pos. for each var:
         -------------
         | 1 | 2 | 3 |
         -------------
         | 4 | 5 | 6 |
         -------------
        '''
        if pos not in [1,2,3,4,5,6]:
            pos=3
            print 'Legend position must be one of 1-6. Will use 3'

        # vertical positioning
        if pos in [1,2,3]:
            yhigh = 0.87
            ylow = yhigh - h
        elif pos in [4,5,6]:
            ylow = 0.066
            yhigh = ylow + h
        # horizontal positioning
        if pos in [1,4]:
            xlow = 0.17
            xhigh = xlow + w
        elif pos in [2,5]:
            xlow = 0.575 - w/2.
            xhigh = 0.575 + w/2.
        elif pos in [3,6]:
            xhigh = 0.93
            xlow = xhigh - w

        return xlow, ylow, xhigh, yhigh



    ## _______________________________________________________
    def getLegend(self, var, pos, datahist, stackhist):
        ## get legend coordinates
        legXlow_, legYlow_, legXhigh_, legYhigh_ = self.getLegendCoordinates(pos, self.legendWidth, self.legendHeight)
        leg = ROOT.TLegend(legXlow_, legYlow_, legXhigh_, legYhigh_)
        # add data
        leg.AddEntry(datahist, self.fullDataTitle, 'lep')
        # add mc
        if self.drawBigLegend:
            for hist in reversed(stackhist.GetHists()):
                leg.AddEntry(hist, hist.GetName(), 'F2')
        else:
            mcHistList_ = []
            for hist in reversed(stackhist.GetHists()):
                if hist.GetName()[:2] not in mcHistList_:
                    leg.AddEntry(hist, hist.GetName()[:2], 'F2')
                    mcHistList_ += [hist.GetName()[:2]]
        # set style
        leg.SetFillColor(0)
        leg.SetBorderSize(1)
        leg.SetLineColor(ROOT.kWhite)
        leg.SetHeader(var)
        return leg


    ## _______________________________________________________
    def getWeightedHist(self, var, sample, newbinsize, ismc):
        '''
        Returns weighted histogram (weight=1 if data).
        Rebinning: if newBinSize = 0, rebinning is not performed.
        '''
        samplelist = self.mcsamplelist if ismc else self.datasamplelist

        h = (samplelist[sample]['tfile']).Get(var).Clone()
    
        htype = samplelist[sample]['type']
        # scale MC hists appropriately
        if 'hWeight' in var:
            h.Scale(1./h.Integral())
        if ismc:
            xsec = getXsec(samplelist[sample]['source'])
            sumw = samplelist[sample]['sumw']
            h.Scale((self.lumi * xsec)/(sumw))
        # rebin
        

        # blind signal region in data
        if not ismc and 'DiMuInvMass' in var:
            binWidth = h.GetXaxis().GetBinWidth(1)
            blindBinLow = int(math.floor(self.blindLow/binWidth))
            blindBinHigh = int(math.ceil(self.blindHigh/binWidth))
            for b in range(blindBinLow, blindBinHigh):
                h.SetBinContent(b, 0.)

        h.SetName(sample)

        # default = data
        lineColor = ROOT.kBlack
        lineStyle = 1
        lineWidth = 1
        fillColor = 0
        fillStyle = 0
        markerSize = 0.6
        markerStyle = 20

        # set MC style    
        if htype=='ZZ':
            lineColor = ROOT.kViolet-5
            lineStyle = 1
            lineWidth = 1
            fillColor = ROOT.kViolet-5
            fillStyle = 1001
            markerSize = 0.
        elif htype=='WZ':
            lineColor = ROOT.kAzure+5
            lineStyle = 1
            lineWidth = 0
            fillColor = ROOT.kAzure+5
            fillStyle = 1001
            markerSize = 0.
        elif htype=='TT' or htype=='TTZ':
            lineColor = ROOT.kRed+2
            lineStyle = 1
            lineWidth = 0
            fillColor = ROOT.kRed+2
            fillStyle = 1001
            markerSize = 0.
        elif htype=='DY':
            lineColor = ROOT.kOrange-3
            lineStyle = 1
            lineWidth = 0
            fillColor = ROOT.kOrange-3
            fillStyle = 1001
            markerSize = 0.
        elif htype=='W':
            lineColor = ROOT.kMagenta-6
            lineStyle = 1
            lineWidth = 0
            fillColor = ROOT.kMagenta-6
            fillStyle = 1001
            markerSize = 0.
        elif htype=='WW':
            lineColor = ROOT.kBlue-2
            lineStyle = 1
            lineWidth = 1
            fillColor = ROOT.kBlue-2
            fillStyle = 1001
            markerSize = 0.
        h.SetLineColor(lineColor)
        h.SetLineStyle(lineStyle)
        h.SetLineWidth(lineWidth)
        h.SetFillColor(fillColor)
        h.SetFillStyle(fillStyle)
        h.SetMarkerSize(markerSize)
        h.SetMarkerStyle(markerStyle)
        return h



    ## _______________________________________________________
    def getRatioHist(self, top, bottom, var):
        '''Returns histogram whose bin contents are those of top divided by those of bottom.'''
        rh = top.Clone()
        rh.Divide(top, bottom, 1., 1., '') # option "B" means the hists are correlated
        rh.SetMarkerSize(0.7)
        rh.SetMarkerStyle(20)
        rh.SetStats(ROOT.kFALSE)
        rh.GetYaxis().SetRangeUser(0.5,1.5)
        rh.GetYaxis().SetTitle('data/mc')
        rh.GetYaxis().SetTitleOffset(0.32)
        rh.SetLineColor(ROOT.kAzure-6)
        rh.SetFillColor(ROOT.kAzure-4)
        rh.GetXaxis().SetTitle(self.varnames[var]['xLabel'])
        rh.GetXaxis().SetLabelFont(42)
        rh.GetXaxis().SetLabelSize(0.2)
        rh.GetXaxis().SetLabelOffset(-0.01)
        rh.GetXaxis().SetTickLength(0.1)
        rh.GetXaxis().SetRangeUser(self.varnames[var]['xMin'], self.varnames[var]['xMax'])
        rh.GetYaxis().SetLabelFont(42)
        rh.GetYaxis().SetLabelSize(.12)
        rh.GetYaxis().SetNdivisions(2)
        rh.SetTitleSize(.2, 'XY')
        rh.SetTitle('')

        return rh




