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
        'group' : 'WH',
        'label' : 'W^{-}H',
    },
    'WPlusH_HToMuMu' : {
        'kind'  : 'sig',
        'group' : 'WH',
        'label' : 'W^{+}H',
    },
    'ZH_HToMuMu' : {
        'kind'  : 'sig',
        'group' : 'ZH',
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

    'TTWJetsToLNu' : {
        'kind'  : 'bkg',
        'group' : 'TTV',
        'label' : 'TTW#rightarrowl#nu',
    },

    'TTZToLLNuNu' : {
        'kind'  : 'bkg',
        'group' : 'TTV',
        'label' : 'TTZ#rightarrow2l2#nu',
    },

    'WJetsToLNu' : {
        'kind'  : 'bkg',
        'group' : 'W',
        'label' : 'W+Jets#rightarrowl#nu',
    },

    'WWTo2L2Nu' : {
        'kind'  : 'bkg',
        'group' : 'WW',
        'label' : 'WW#rightarrow2l2#nu',
    },

    'WZTo2L2Q' : {
        'kind'  : 'bkg',
        'group' : 'WZ',
        'label' : 'WZ#rightarrow2l2j',
    },

    'WZTo3LNu' : {
        'kind'  : 'bkg',
        'group' : 'WZ',
        'label' : 'WZ#rightarrow3l#nu',
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

    'TZQ_ll_4f' : {
        'kind'  : 'bkg',
        'group' : 'T',
        'label' : 'TZQ_ll_4f',
    },

    'ST_tW_antitop_5f' : {
        'kind'  : 'bkg',
        'group' : 'extra3',
        'label' : 'ST_tW_antitop_5f',
    },

    'ST_tW_top_5f' : {
        'kind'  : 'bkg',
        'group' : 'extra4',
        'label' : 'ST_tW_top_5f',
    },

##### data

    'SingleMuon_Run2016Bv2' : {
        'kind'  : 'data',
        'group' : 'data',
        'label' : 'SingleMuon Run2016Bv2',
        'lumi'  : 5788.1,
    },

    'SingleMuon_Run2016C' : {
        'kind'  : 'data',
        'group' : 'data',
        'label' : 'SingleMuon Run2016C',
        'lumi'  : 2573.1,
    },

    'SingleMuon_Run2016D' : {
        'kind'  : 'data',
        'group' : 'data',
        'label' : 'SingleMuon Run2016D',
        'lumi'  : 4248.1,
    },

    'SingleMuon_Run2016E' : {
        'kind'  : 'data',
        'group' : 'data',
        'label' : 'SingleMuon 2016E',
        'lumi'  : 4009.1, # /pb
    },

    'SingleMuon_Run2016F' : {
        'kind'  : 'data',
        'group' : 'data',
        'label' : 'SingleMuon 2016F',
        'lumi'  : 3102.1, # /pb
    },

    'SingleMuon_Run2016G' : {
        'kind'  : 'data',
        'group' : 'data',
        'label' : 'SingleMuon 2016G',
        'lumi'  : 7540.1, # /pb
    },

    'SingleMuon_Run2016Hv2' : {
        'kind'  : 'data',
        'group' : 'data',
        'label' : 'SingleMuon 2016Hv2',
        'lumi'  : 8391.1, # /pb
    },

    'SingleMuon_Run2016Hv3' : {
        'kind'  : 'data',
        'group' : 'data',
        'label' : 'SingleMuon 2016Hv3',
        'lumi'  : 215.1, # /pb
    },


}

# brilcalc lumi --normtag /afs/cern.ch/user/l/lumipro/public/normtag_file/normtag_DATACERT.json -u /pb -i processedLumis_SingleMuon_Run2016?.json
