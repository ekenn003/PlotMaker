import os, sys
import array
import logging
import math
from collections import OrderedDict
import ROOT
from tools.CMS_lumi import CMS_lumi
from tools.tools import getXsec
import tools.tdrstyle as tdrstyle
from datasets import *
import argparse


## ___________________________________________________________
class PlotBase(object):
    '''Plot base'''
    def __init__(self, args):
        # set batch mode
        ROOT.gROOT.SetBatch(ROOT.kTRUE)
        # empty sample lists
        self.signal_sets = []
        self.signal_scale = 1.
        self.background_sets = []
        self.data_sets = []
        # set tdr style
        tdrstyle.setTDRStyle()
        # CMS_lumi parameters
        self.iPeriod = 4
        self.iPos = 10
        # blinding region
        self.blindlow = 122.
        self.blindhigh = 128.



    ## _______________________________________________________
    def plot(self):
        '''Dummy function overridden in the derived class'''
        pass

    ## _______________________________________________________
    def get_canvas(self, canvname, w, h, ):
        tcanv = ROOT.TCanvas(canvname, canvname, w, h)
        tcanv.SetLeftMargin(0.12)
        tcanv.SetRightMargin(0.04)
        tcanv.SetTopMargin(0.08)
        tcanv.SetBottomMargin(0.12)
        return tcanv



    ## _______________________________________________________
    def get_plotpad(self, canvname, usepull=True):
        ylow = 0.2 if usepull else 0.1
        plotpad = ROOT.TPad(canvname+'_plot', canvname+'_plot', 0.0, ylow, 1.0, 1.0)
        plotpad.SetBottomMargin(0.03)
        plotpad.SetBorderMode(0)
        plotpad.SetBorderSize(0)
        plotpad.SetLeftMargin(0.14)
        plotpad.SetRightMargin(0.04)
        plotpad.SetTopMargin(0.08/0.8)
        return plotpad


    ## _______________________________________________________
    def get_pullpad(self, canvname):
        pullpad = ROOT.TPad(canvname+'_pull', canvname+'_pull', 0.0, 0.0, 1.0, 0.2)
        pullpad.SetTopMargin(0.01)
        pullpad.SetBorderMode(0)
        pullpad.SetBorderSize(0)
        pullpad.SetLeftMargin(0.14)
        pullpad.SetRightMargin(0.04)
        pullpad.SetBottomMargin(0.12/0.2)
        return pullpad


    ## _______________________________________________________
    def get_legend_coordinates(self, pos, w, h):
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
    def get_legend(self, var, pos, datahist=None, stackhist=None, sighists=None):
        # get legend coordinates
        legXlow_, legYlow_, legXhigh_, legYhigh_ = self.get_legend_coordinates(pos, self.legend_width, self.legend_height)
        leg = ROOT.TLegend(legXlow_, legYlow_, legXhigh_, legYhigh_)

        # add data
        if datahist:
            leg.AddEntry(datahist, self.full_data_title, 'lep')

        # add mc
        if stackhist:
            if self.draw_big_legend:
                for hist in reversed(stackhist.GetHists()):
                    leg.AddEntry(hist, hist.GetName(), 'F2')
            else:
                mc_hists = []
                for hist in reversed(stackhist.GetHists()):
                    hname_ = hist.GetName()
                    if hname_ in ['WWW', 'WWZ', 'WZZ', 'ZZZ']:
                        hgroup_ = 'VVV'
                    else:
                        hgroup_ = hist.GetName()[:2]
                    if hgroup_ not in mc_hists:
                        leg.AddEntry(hist, hgroup_, 'F2')
                        mc_hists += [hgroup_]

        # add signals
        if sighists:
            for hist in sighists:
                #leg.AddEntry(hist, hist.GetName().split('_')[0] + ' signal x{0}'.format(int(self.signal_scale)), 'l')
                leg.AddEntry(hist, hist.GetName().split('_')[0] + ' signal', 'l')

        # set style
        leg.SetFillColor(0)
        leg.SetBorderSize(1)
        leg.SetLineColor(ROOT.kWhite)
        leg.SetHeader(var)
        return leg


    ## _______________________________________________________
    def get_weighted_hist(self, var, sample, lumi, newbinsize=0):
        '''
        Returns weighted histogram (weight=1 if data).
        Rebinning: if newBinSize = 0, rebinning is not performed.
        '''

        ismc = True if sample.kind in ['sig','bkg'] else False

        try:
            h = sample.tfile.Get(('categories/' if 'Category' in var else '') + var).Clone()
        except:
            h = ROOT.TH1F()
            print 'failed in getting hist "{0}" from sample "{1}"'.format(var, sample.name)

        hgroup = sample.group

        # scale MC hists appropriately
        if 'hWeight' in var:
            h.Scale(1./h.Integral())
        if ismc:
            xsec = sample.xsec
            sumw = sample.sumw
            scale_number = (self.lumi * xsec) / sumw



            if sample.kind=='sig': scale_number *= self.signal_scale
            h.Scale(scale_number)
            #print
            #print 'scaling hist from {0} by '.format(sample.name)
            #print '    ( {0} * {1} {2}) / ( {3} ) = {4}'.format(self.lumi, xsec, '* {0} '.format(self.signal_scale) if sample.kind=='sig' else '', sumw, scale_number)
            #print

        # rebin?
        curbinsize = h.GetBinWidth(1)
        if (newbinsize != 0 and newbinsize >= curbinsize):
            rebinnum = newbinsize/curbinsize
            h.Rebin(int(rebinnum))

        # blind signal region in data
        if not ismc and 'DiMuInvMass' in var:
            binwidth = h.GetXaxis().GetBinWidth(1)
            blindbin_low = int(math.floor(self.blindlow/binwidth))
            blindbin_high = int(math.ceil(self.blindhigh/binwidth))
            for b in range(blindbin_low, blindbin_high):
                h.SetBinContent(b, 0.)

        h.SetName(sample.name)

        # default = data
        lineColor = ROOT.kBlack
        lineStyle = 1
        lineWidth = 1
        fillColor = 0
        fillStyle = 0
        markerSize = 0.6
        markerStyle = 20

        # set MC style    
        if hgroup=='ZZ':
            lineColor = ROOT.kViolet-5
            lineStyle = 1
            lineWidth = 1
            fillColor = ROOT.kViolet-5
            fillStyle = 1001
            markerSize = 0.
        elif hgroup=='WZ':
            lineColor = ROOT.kAzure+5
            lineStyle = 1
            lineWidth = 0
            fillColor = ROOT.kAzure+5
            fillStyle = 1001
            markerSize = 0.
        elif hgroup=='TT' or hgroup=='TTZ':
            lineColor = ROOT.kRed+2
            lineStyle = 1
            lineWidth = 0
            fillColor = ROOT.kRed+2
            fillStyle = 1001
            markerSize = 0.
        elif hgroup=='DY':
            lineColor = ROOT.kOrange-3
            lineStyle = 1
            lineWidth = 0
            fillColor = ROOT.kOrange-3
            fillStyle = 1001
            markerSize = 0.
        elif hgroup=='W':
            lineColor = ROOT.kMagenta-6
            lineStyle = 1
            lineWidth = 0
            fillColor = ROOT.kMagenta-6
            fillStyle = 1001
            markerSize = 0.
        elif hgroup=='WW':
            lineColor = ROOT.kBlue-2
            lineStyle = 1
            lineWidth = 1
            fillColor = ROOT.kBlue-2
            fillStyle = 1001
            markerSize = 0.
        elif hgroup=='VVV':
            lineColor = ROOT.kGreen-2
            lineStyle = 1
            lineWidth = 1
            fillColor = ROOT.kGreen-2
            fillStyle = 1001
            markerSize = 0.

        elif hgroup=='GGF':
            lineColor = ROOT.kViolet
            lineStyle = 1
            lineWidth = 2
            fillColor = 0
            fillStyle = 0
            markerSize = 0.

        elif hgroup=='VBF':
            lineColor = ROOT.kGreen
            lineStyle = 1
            lineWidth = 2
            fillColor = 0
            fillStyle = 0
            markerSize = 0.

        elif hgroup=='ZH':
            lineColor = ROOT.kBlue
            lineStyle = 1
            lineWidth = 2
            fillColor = 0
            fillStyle = 0
            markerSize = 0.

        elif hgroup=='WH':
            lineColor = ROOT.kRed
            lineStyle = 1
            lineWidth = 2
            fillColor = 0
            fillStyle = 0
            markerSize = 0.

        elif hgroup=='TTV':
            lineColor = ROOT.kCyan
            lineStyle = 1
            lineWidth = 1
            fillColor = ROOT.kCyan
            fillStyle = 1001
            markerSize = 0.
        elif hgroup=='T':
            lineColor = 6
            lineStyle = 1
            lineWidth = 1
            fillColor = 6
            fillStyle = 1001
            markerSize = 0.
        elif hgroup=='extra3':
            lineColor = 7
            lineStyle = 1
            lineWidth = 1
            fillColor = 7
            fillStyle = 1001
            markerSize = 0.
        elif hgroup=='extra4':
            lineColor = 8
            lineStyle = 1
            lineWidth = 1
            fillColor = 8
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
    def get_ratio_hist(self, top, bottom, var, **kwargs):
        '''Returns histogram whose bin contents are those of top divided by those of bottom.'''
        xmin = kwargs.pop('xmin', 0.)
        xmax = kwargs.pop('xmax', 50.)
        # override
        if var in self.varnames:
            xmin = self.varnames[var]['xMin']
            xmax = self.varnames[var]['xMax']

        rh = top.Clone()
        rh.Divide(top, bottom, 1., 1., '') # option "B" means the hists are correlated
        rh.SetMarkerSize(0.7)
        rh.SetMarkerStyle(20)
        rh.SetStats(ROOT.kFALSE)
        rh.GetYaxis().SetRangeUser(0.8, 1.2)
        rh.GetYaxis().SetTitle('data/mc')
        rh.GetYaxis().SetTitleOffset(0.32)
        rh.SetLineColor(ROOT.kAzure-6)
        rh.SetFillColor(ROOT.kAzure-4)
        rh.GetXaxis().SetLabelFont(42)
        rh.GetXaxis().SetLabelSize(0.2)
        rh.GetXaxis().SetLabelOffset(-0.01)
        rh.GetXaxis().SetTickLength(0.1)
        rh.GetXaxis().SetRangeUser(xmin, xmax)
        rh.GetYaxis().SetLabelFont(42)
        rh.GetYaxis().SetLabelSize(.12)
        rh.GetYaxis().SetNdivisions(2)
        rh.SetTitleSize(.2, 'XY')
        rh.SetTitle('')

        return rh


