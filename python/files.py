# PlotMaker/python/files.py
import ROOT

###############################
# WITH SCALE FACTORS, 25/25   #
###############################

mc_juli16/76X = {

    'DYJets' : {
        'tfile' : ROOT.TFile('data/juli16/76X/ana_template_DYJetsToLL.root'),
        'type'  : 'DY',
        'label' : 'DY+Jets',
        'sumw' : (75427319225. + 74570134300. + 77086876398. + 76643341637. + 76753312353. + 71020148223.),
        'source' : 'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8',
    },

    'TTJets' : {
        'tfile' : ROOT.TFile('data/juli16/76X/ana_template_TTJets.root'),
        'type'  : 'TT',
        'label' : 'TT+Jets',
        'sumw' : (3057295. + 3045081.),
        'source' : 'TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
    },

    'TTZTo2L2Nu' : {
        'tfile' : ROOT.TFile('data/juli16/76X/ana_template_TTZToLLNuNu.root'),
        'type'  : 'TTZ',
        'label' : 'TTZ#rightarrow 2l2#nu',
        'sumw' : 394200.,
        'source' : 'TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8',
    },

    'WWTo2L2Nu' : {
        'tfile' : ROOT.TFile('data/juli16/76X/ana_template_WWTo2L2Nu.root'),
        'type'  : 'WW',
        'label' : 'WW#rightarrow 2l2#nu',
        'sumw' : (530896. + 628550. + 583100. + 237442.),
        'source' : 'WWTo2L2Nu_13TeV-powheg',
    },

    'WZTo2L2Q' : {
        'tfile' : ROOT.TFile('data/juli16/76X/ana_template_WZTo2L2q.root'),
        'type'  : 'WZ',
        'label' : 'WZ#rightarrow 2l2j',
        'sumw' : (45028859. + 40594470. + 41361814. + 42527668. + 40918226.),
        'source' : 'WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8',
    },

    'WZTo3LNu' : {
        'tfile' : ROOT.TFile('data/juli16/76X/ana_template_WZTo3LNu.root'),
        'type'  : 'WZ',
        'label' : 'WZ#rightarrow 3l#nu',
        'sumw' : (2000000.),
        'source' : 'WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8',
    },

    'ZZTo2L2Nu' : {
        'tfile' : ROOT.TFile('data/juli16/76X/ana_template_ZZTo2L2Nu.root'),
        'type'  : 'ZZ',
        'label' : 'ZZ#rightarrow2l2#nu',
        'sumw' : (4384725. + 4400325.),
        'source' : 'ZZTo2L2Nu_13TeV_powheg_pythia8',
    },

    'ZZTo2L2Q' : {
        'tfile' : ROOT.TFile('data/juli16/76X/ana_template_ZZTo2L2q.root'),
        'type'  : 'ZZ',
        'label' : 'ZZ#rightarrow2l2j',
        'sumw' : (14944513. + 15748854. + 14951603. + 15704273. + 13155400.),
        'source' : 'ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8',
    },

    'ZZTo4L' : {
        'tfile' : ROOT.TFile('data/juli16/76X/ana_template_ZZTo4L.root'),
        'type'  : 'ZZ',
        'label' : 'ZZ#rightarrow4l',
        'sumw' : (3361872. + 3307316.),
        'source' : 'ZZTo4L_13TeV_powheg_pythia8',
    },

}

data_juli16/76X = {

    'SMu15C' : {
        'tfile' : ROOT.TFile('data/juli16/76X/ana_template_SingleMuon2015C.root'),
        'type'  : 'data',
        'label' : 'SingleMuon Run2015C',
        'source' : 'SingleMuon_Run2015C_25ns-16Dec2015-v1',
    },

    'SMu15D' : {
        'tfile' : ROOT.TFile('data/juli16/76X/ana_template_SingleMuon2015D.root'),
        'type'  : 'data',
        'label' : 'SingleMuon Run2015D',
        'source' : 'SingleMuon_Run2015D-16Dec2015-v1',
    },

}


################################
# WITHOUT SCALE FACTORS, 25/25 #
################################

mc_juli16 = {

    'DYJets' : {
        'tfile' : ROOT.TFile('data/juli16/80X/ana_2Mu_DYJetsToLL.root'),
        'type'  : 'DY',
        'label' : 'DY+Jets',
        'sumw' : (35435679339. + 39875315578. + 24512314383. + 38827590001. + 39179723008. + 39053178313. + 38775758414. + 39539239787. + 39542732281. + 39653006797. + 38400344972. + 37862896171.),
        'source' : 'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8',
    },
}

data_juli16 = {

    'SMu16B' : {
        'tfile' : ROOT.TFile('data/juli16/80X/ana_2Mu_SingleMuon2016B.root'),
        'type'  : 'data',
        'label' : 'SingleMuon Run2016B',
        'source' : 'SingleMuon_Run2016B-PromptReco-v2',
    },
}


