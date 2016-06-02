#from PlotBase import PlotBase
#ThisPlot = PlotBase()
import ROOT
from tools.CMS_lumi import CMS_lumi
import tools.tdrstyle as tdrstyle
from math import floor as roundDown
from math import ceil as roundUp

def GetWeightedHist(var, sample, samplelist, ismc):
    h = (samplelist[sample]['tfile']).Get(var).Clone()

    # scale MC hists appropriately
    if ismc:
        mctype = samplelist[sample]['type']
        xsec = samplelist[sample]['xsec']
        sumw = samplelist[sample]['sumw']
        h.Scale((lumi * xsec)/(sumw))
    # blind signal region in data
    elif 'InvMass' in varname:
        binWidth = h.GetXaxis().GetBinWidth(1)
        blindBinLow = int(roundDown(blindLow/binWidth))
        blindBinHigh = int(roundUp(blindHigh/binWidth))
        for b in range(blindBinLow, blindBinHigh):
            h.SetBinContent(b, 0.)

    lineColor = ROOT.kBlack;
    lineStyle = 1;
    lineWidth = 1;
    fillColor = 0;
    fillStyle = 0;
    markerSize = 0.6;
    markerStyle = 20;

    if not ismc:
        lineColor = ROOT.kBlack;
        lineStyle = 1;
        lineWidth = 1;
        fillColor = 0;
        fillStyle = 0;
        markerSize = 0.6;
        markerStyle = 20;
    elif mctype=='ZZ':
        lineColor = ROOT.kViolet-5;
        lineStyle = 1;
        lineWidth = 1;
        fillColor = ROOT.kViolet-5;
        fillStyle = 1001;
        markerSize = 0.;
    elif mctype=='WZ':
        lineColor = ROOT.kAzure+5;
        lineStyle = 1;
        lineWidth = 0;
        fillColor = ROOT.kAzure+5;
        fillStyle = 1001;
        markerSize = 0.;
    elif mctype=='TT' or mctype=='TTZ':
        lineColor = ROOT.kRed+2;
        lineStyle = 1;
        lineWidth = 0;
        fillColor = ROOT.kRed+2;
        fillStyle = 1001;
        markerSize = 0.;
    elif mctype=='DY':
        lineColor = ROOT.kOrange-3;
        lineStyle = 1;
        lineWidth = 0;
        fillColor = ROOT.kOrange-3;
        fillStyle = 1001;
        markerSize = 0.;
    elif mctype=='W':
        lineColor = ROOT.kMagenta-6;
        lineStyle = 1;
        lineWidth = 0;
        fillColor = ROOT.kMagenta-6;
        fillStyle = 1001;
        markerSize = 0.;
    elif mctype=='WW':
        lineColor = ROOT.kBlue-2;
        lineStyle = 1;
        lineWidth = 1;
        fillColor = ROOT.kBlue-2;
        fillStyle = 1001;
        markerSize = 0.;

    h.SetLineColor(lineColor);
    h.SetLineStyle(lineStyle);
    h.SetLineWidth(lineWidth);
    h.SetFillColor(fillColor);
    h.SetFillStyle(fillStyle);
    h.SetMarkerSize(markerSize);
    h.SetMarkerStyle(markerStyle);

    h.SetName(sample);







#    'hDiMuInvMass' : {
#        'title' : 'Dimuon invariant mass',
#        'xmin' : 30., 'xmax' : 200.,
#        'xLabel' : 'M_{#mu^{+}#mu^{-}}',
#        'ymax' : 10000.,
#        'yLabel' : 'Events/x GeV',
#    },


    return h














mcSamples = {
    'DYJets' : {
        'tfile' : ROOT.TFile('data/june16/ana_DYJetsToLL.root'),
        'type' : 'DY', 'label' : 'DY+Jets', 'xsec' : 6025.2, 'sumw' : (154088004145. + 155017413713. + 142395714278),
    },
    'TTJets' : {
        'tfile' : ROOT.TFile('data/june16/ana_TTJets.root'),
        'type' : 'TT', 'label' : 'TT+Jets', 'xsec' : 831.76, 'sumw' : 6102376.,
    },
    'TTZTo2L2Nu' : {
        'tfile' : ROOT.TFile('data/june16/ana_TTZToLLNuNu.root'),
        'type' : 'TTZ', 'label' : 'TTZ#rightarrow 2l2#nu', 'xsec' : 0.2529, 'sumw' : 394200.,
    },
    'WWTo2L2Nu' : {
        'tfile' : ROOT.TFile('data/june16/ana_WWTo2L2Nu.root'),
        'type' : 'WW', 'label' : 'WW#rightarrow 2l2#nu', 'xsec' : 12.178, 'sumw' : 1979988.,
    },
    'WZTo2L2Q' : {
        'tfile' : ROOT.TFile('data/june16/ana_WZTo2L2q.root'),
        'type' : 'WZ', 'label' : 'WZ#rightarrow 2l2j', 'xsec' : 5.595, 'sumw' : (103013246. + 107417791.),
    },
    'WZTo3LNu' : {
        'tfile' : ROOT.TFile('data/june16/ana_WZTo3LNu.root'),
        'type' : 'WZ', 'label' : 'WZ#rightarrow 3l#nu', 'xsec' : 4.42965, 'sumw' : 2000000.,
    },
    'ZZTo2L2Nu' : {
        'tfile' : ROOT.TFile('data/june16/ana_ZZTo2L2Nu.root'),
        'type' : 'ZZ', 'label' : 'ZZ#rightarrow2l2#nu', 'xsec' : 0.564, 'sumw' : 8785050.,
    },
    'ZZTo2L2Q' : {
        'tfile' : ROOT.TFile('data/june16/ana_ZZTo2L2q.root'),
        'type' : 'ZZ', 'label' : 'ZZ#rightarrow2l2j', 'xsec' : 3.22, 'sumw' : 74504643.,
    },
    'ZZTo4L' : {
        'tfile' : ROOT.TFile('data/june16/ana_ZZTo4L.root'),
        'type' : 'ZZ', 'label' : 'ZZ#rightarrow4l', 'xsec' : 1.256, 'sumw' : 6669188.,
    },
}
mcStackOrder = [
    'DYJets',
    'TTJets',
    'TTZTo2L2Nu',
    'WWTo2L2Nu',
    'WZTo2L2Q',
    'WZTo3LNu',
    'ZZTo2L2Nu',
    'ZZTo2L2Q',
    'ZZTo4L',
]

dataSamples = {
    'SMu15C' : {
        'tfile' : ROOT.TFile('data/june16/ana_SingleMuon2015C.root'),
        'type' : 'data',
        'label' : 'SingleMuon Run2015C',
    },
    'SMu15D' : {
        'tfile' : ROOT.TFile('data/june16/ana_SingleMuon2015D.root'),
        'type' : 'data',
        'label' : 'SingleMuon Run2015D',
    },
}

lumi = 2318 # pb^-1
blindLow = 122.
blindHigh = 128.
iPeriod = 4
iPos = 11

varnames = {
    'hDiMuInvMass' : {
        'title' : 'Dimuon invariant mass',
        'xmin' : 40., 'xmax' : 160.,
        'xLabel' : 'M_{#mu^{+}#mu^{-}}',
        'ymax' : 10000.,
        'yLabel' : 'Events/x GeV',
    },
    'hVtxN': {
        'title' : 'nPV after reweighting',
        'xmin' : 0., 'xmax' : 50.,
        'xLabel' : 'N_{PV}',
        'ymax' : 1000000.,
        'yLabel' : 'Events',
    },


}


for var in varnames:
    #set the tdr style
    tdrstyle.setTDRStyle()

    canvname = '{0}_{1}'.format(var, 'stack')
    canv = ROOT.TCanvas(canvname, canvname, 800, 600)
    canv.SetLeftMargin(0.12)
    canv.SetRightMargin(0.04)
    canv.SetTopMargin(0.08)
    canv.SetBottomMargin(0.12)

    plotpad = ROOT.TPad(canvname+'_plot', canvname+'_plot', 0.0, 0.2, 1.0, 1.0)
    pullpad = ROOT.TPad(canvname+'_pull', canvname+'_pull', 0.0, 0.0, 1.0, 0.2)
    plotpad.SetBottomMargin(0.03)
    plotpad.SetBorderMode(0)
    plotpad.SetBorderSize(0)
    plotpad.SetLeftMargin(0.12)
    plotpad.SetRightMargin(0.04)
    plotpad.SetTopMargin(0.08/0.8)
    pullpad.SetTopMargin(0.01)
    pullpad.SetBorderMode(0)
    pullpad.SetBorderSize(0)
    pullpad.SetLeftMargin(0.12)
    pullpad.SetRightMargin(0.04)
    pullpad.SetBottomMargin(0.12/0.2)
    plotpad.Draw()
    pullpad.Draw()
    plotpad.cd()

    stack = ROOT.THStack()

    for sample in mcSamples:
        #print 'looking for {0} in {1} file (of type {2})...'.format(var, sample, mcSamples[sample]['type'])
        #print 'sample {0} has xsec = {1} (pb) and sumweights = {2}.'.format(sample, mcSamples[sample]['xsec'], mcSamples[sample]['sumw'])

        hist = GetWeightedHist(var, sample, mcSamples, True)
        stack.Add(hist)

    stack.Draw('hist')

    stack.GetXaxis().SetTitle(varnames[var]['xLabel'])
    stack.GetXaxis().SetRangeUser(varnames[var]['xmin'], varnames[var]['xmax'])
    stack.GetYaxis().SetTitle(varnames[var]['yLabel'])
    stack.GetHistogram().GetXaxis().SetLabelOffset(999)
    stack.GetHistogram().GetXaxis().SetLabelSize(0)

    stack.SetMinimum(0.)
    stack.SetMaximum(varnames[var]['ymax'])

    CMS_lumi(plotpad, iPeriod, iPos);
    stack.SetTitle(varnames[var]['title'])

    canv.Print('myplots/june16/test_{0}_{1}.png'.format(var, 'stack'))

    canv.Clear()


