# files.py

import ROOT

###############################
# WITH SCALE FACTORS, 25/25   #
###############################

mc_june16 = {

    'DYJets' : {
        'tfile' : ROOT.TFile('data/june16/ana_template_DYJetsToLL.root'),
        'type'  : 'DY',
        'label' : 'DY+Jets',
        'xsec' : 6025.2,
        'sumw' : (75427319225. + 74570134300. + 77086876398. + 76643341637. + 76753312353. + 71020148223.),
    },

    'TTJets' : {
        'tfile' : ROOT.TFile('data/june16/ana_template_TTJets.root'),
        'type'  : 'TT',
        'label' : 'TT+Jets',
        'xsec' : 57.35,
        'sumw' : (3057295. + 3045081.),
    },

    'TTZTo2L2Nu' : {
        'tfile' : ROOT.TFile('data/june16/ana_template_TTZToLLNuNu.root'),
        'type'  : 'TTZ',
        'label' : 'TTZ#rightarrow 2l2#nu',
        'xsec' : 0.2529,
        'sumw' : 394200.,
    },

    'WWTo2L2Nu' : {
        'tfile' : ROOT.TFile('data/june16/ana_template_WWTo2L2Nu.root'),
        'type'  : 'WW',
        'label' : 'WW#rightarrow 2l2#nu',
        'xsec' : 12.178,
        'sumw' : (530896. + 628550. + 583100. + 237442.),
    },

    'WZTo2L2Q' : {
        'tfile' : ROOT.TFile('data/june16/ana_template_WZTo2L2q.root'),
        'type'  : 'WZ',
        'label' : 'WZ#rightarrow 2l2j',
        'xsec' : 5.595,
        'sumw' : (45028859. + 40594470. + 41361814. + 42527668. + 40918226.),
    },

    'WZTo3LNu' : {
        'tfile' : ROOT.TFile('data/june16/ana_template_WZTo3LNu.root'),
        'type'  : 'WZ',
        'label' : 'WZ#rightarrow 3l#nu',
        'xsec' : 4.42965,
        'sumw' : (2000000.),
    },

    'ZZTo2L2Nu' : {
        'tfile' : ROOT.TFile('data/june16/ana_template_ZZTo2L2Nu.root'),
        'type'  : 'ZZ',
        'label' : 'ZZ#rightarrow2l2#nu',
        'xsec' : 0.564,
        'sumw' : (4384725. + 4400325.),
    },

    'ZZTo2L2Q' : {
        'tfile' : ROOT.TFile('data/june16/ana_template_ZZTo2L2q.root'),
        'type'  : 'ZZ',
        'label' : 'ZZ#rightarrow2l2j',
        'xsec' : 3.22,
        'sumw' : (14944513. + 15748854. + 14951603. + 15704273. + 13155400.),
    },

    'ZZTo4L' : {
        'tfile' : ROOT.TFile('data/june16/ana_template_ZZTo4L.root'),
        'type'  : 'ZZ',
        'label' : 'ZZ#rightarrow4l',
        'xsec' : 1.256,
        'sumw' : (3361872. + 3307316.),
    },

}

data_june16 = {

    'SMu15C' : {
        'tfile' : ROOT.TFile('data/june16/ana_template_SingleMuon2015C.root'),
        'type'  : 'data',
        'label' : 'SingleMuon Run2015C',
    },

    'SMu15D' : {
        'tfile' : ROOT.TFile('data/june16/ana_template_SingleMuon2015D.root'),
        'type'  : 'data',
        'label' : 'SingleMuon Run2015D',
    },

}


