# PlotMaker/python/datasets.py
from ROOT import TFile

datadir = '/Users/ken/Work/PlotMaker/data'

class Dataset(object):
    def __init__(self, name, version, era, analysis):
        self.name = name
        self.tfilename = '{0}/{1}/{2}/ana_{3}_{4}.root'.format(datadir, version, era, analysis, name)
        self.tfile = TFile.Open(self.tfilename)
        try:
            # get xsec and sumw/nevents
            tsummary = self.tfile.Get('Summary')
            tsummary.GetEntry(0)
            self.xsec = tsummary.tCrossSec
            self.sumw = 0.
            self.nevt = 0
            for entry in range(tsummary.GetEntries()):
                tsummary.GetEntry(entry)
                self.sumw += tsummary.tSumWts
                self.nevt += tsummary.tNumEvts
        except:
            print 'ERROR opening file ' + self.tfilename
            self.tfile = None
            self.xsec = -1.
            self.sumw = -1.
            self.nevt = -1

    # look up dset

        # sig, bkg, or data
        self.kind = dsetdb[name]['kind']
        # for the stack
        self.group = dsetdb[name]['group']
        # for the legend
        self.label = dsetdb[name]['label']
        # if data
        self.lumi = dsetdb[name]['lumi'] if self.group=='data' else -1.

    def set_xsec(self, xsec):
        self.xsec = xsec
    def set_sumwts(self, sumw):
        self.sumw = sumw


    def print_info(self):
        print
        print 'self.name  = ' + self.name
        print 'self.tfile = ' + self.tfilename
        print 'self.kind  = ' + self.kind
        print 'self.group = ' + self.group
        print 'self.label = ' + self.label
        print 'self.lumi  = ' + str(self.lumi)
        print 'self.xsec  = ' + str(self.xsec)
        print 'self.sumw  = ' + str(self.sumw)
        print 'self.nevt  = ' + str(self.nevt)
        print




    def __del__(self):
        try:
            self.tfile.Close()
        except:
            pass






dsetdb = {

##### signal

    'GluGlu_HToMuMu' : {
        'kind'  : 'sig',
        'group' : 'GGF',
        'label' : 'GGF H',
    },
    'VBF_HToMuMu' : {
        'kind'  : 'sig',
        'group' : 'VBF',
        'label' : 'VBF H',
    },
    'WMinusH_HToMuMu' : {
        'kind'  : 'sig',
        'group' : 'VH',
        'label' : 'W^{-}H',
    },
    'WPlusH_HToMuMu' : {
        'kind'  : 'sig',
        'group' : 'VH',
        'label' : 'W^{+}H',
    },
    'ZH_HToMuMu' : {
        'kind'  : 'sig',
        'group' : 'VH',
        'label' : 'ZH',
    },

##### background

    'DYJetsToLL' : {
        'kind'  : 'bkg',
        'group' : 'DY',
        'label' : 'DY+Jets',
    },

    'TTJets' : {
        'kind'  : 'bkg',
        'group' : 'TT',
        'label' : 'TT+Jets',
    },

    'TTZTo2L2Nu' : {
        'kind'  : 'bkg',
        'group' : 'TTZ',
        'label' : 'TTZ#rightarrow 2l2#nu',
    },

    'WWTo2L2Nu' : {
        'kind'  : 'bkg',
        'group' : 'WW',
        'label' : 'WW#rightarrow 2l2#nu',
    },

    'WZTo2L2Q' : {
        'kind'  : 'bkg',
        'group' : 'WZ',
        'label' : 'WZ#rightarrow 2l2j',
    },

    'WZTo3LNu' : {
        'kind'  : 'bkg',
        'group' : 'WZ',
        'label' : 'WZ#rightarrow 3l#nu',
    },

    'ZZTo2L2Nu' : {
        'kind'  : 'bkg',
        'group' : 'ZZ',
        'label' : 'ZZ#rightarrow2l2#nu',
    },

    'ZZTo2L2Q' : {
        'kind'  : 'bkg',
        'group' : 'ZZ',
        'label' : 'ZZ#rightarrow2l2j',
    },

    'ZZTo4L' : {
        'kind'  : 'bkg',
        'group' : 'ZZ',
        'label' : 'ZZ#rightarrow4l',
    },

    'WWW' : {
        'kind'  : 'bkg',
        'group' : 'VVV',
        'label' : 'WWW',
    },

    'WWZ' : {
        'kind'  : 'bkg',
        'group' : 'VVV',
        'label' : 'WWZ',
    },

    'WZZ' : {
        'kind'  : 'bkg',
        'group' : 'VVV',
        'label' : 'WZZ',
    },

    'ZZZ' : {
        'kind'  : 'bkg',
        'group' : 'VVV',
        'label' : 'ZZZ',
    },

##### data

    'SingleMuon_Run2015C' : {
        'kind'  : 'data',
        'group' : 'data',
        'label' : 'SingleMuon_Run 15C',
        'lumi'  : 0.,
    },
    'SingleMuon_Run2015D' : {
        'kind'  : 'data',
        'group' : 'data',
        'label' : 'SingleMuon_Run 15D',
        'lumi'  : 0.,
    },

    'SingleMuon_Run2016B' : {
        'kind'  : 'data',
        'group' : 'data',
        'label' : 'SingleMuon Run2016Bv1',
        'lumi'  : 5887.799,
    },

    'SingleMuon_Run2016Bv3' : {
        'kind'  : 'data',
        'group' : 'data',
        'label' : 'SingleMuon Run2016Bv3',
        'lumi'  : 5855.410,
    },

    'SingleMuon_Run2016C' : {
        'kind'  : 'data',
        'group' : 'data',
        'label' : 'SingleMuon Run2016C',
        'lumi'  : 2645.968,
    },

    'SingleMuon_Run2016D' : {
        'kind'  : 'data',
        'group' : 'data',
        'label' : 'SingleMuon Run2016D',
        'lumi'  : 4353.449,
    },

    'SingleMuon_Run2016E' : {
        'kind'  : 'data',
        'group' : 'data',
        'label' : 'SingleMuon 2016E',
        'lumi'  : 4049.732, # /pb
    },

    'SingleMuon_Run2016F' : {
        'kind'  : 'data',
        'group' : 'data',
        'label' : 'SingleMuon 2016F',
        'lumi'  : 3157.021, # /pb
    },

    'SingleMuon_Run2016G' : {
        'kind'  : 'data',
        'group' : 'data',
        'label' : 'SingleMuon 2016G',
        'lumi'  : 7260.835, # /pb
    },

    'SingleMuon_Run2016Hv2' : {
        'kind'  : 'data',
        'group' : 'data',
        'label' : 'SingleMuon 2016Hv2',
        'lumi'  : 8284.592, # /pb
    },

    'SingleMuon_Run2016Hv3' : {
        'kind'  : 'data',
        'group' : 'data',
        'label' : 'SingleMuon 2016Hv3',
        'lumi'  : 216.783, # /pb
    },


}

# brilcalc lumi --normtag /afs/cern.ch/user/l/lumipro/public/normtag_file/normtag_DATACERT.json -u /pb -i processedLumis_SingleMuon_Run2016?.json
