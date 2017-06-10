# PlotMaker/python/variables_2mu.py
'''
leglinlog: 
    legend position for (linear plot, log plot)
    if it is 0, it will not make that plot
'''

varnames = {
    ###########################
    # event variables         #
    ###########################

    'hVtxN': {
        'title' : 'nPV after reweighting',
        'xMin' : 0., 'xMax' : 40.,
        'xLabel' : 'N_{PV}',
        'binSize' : 2,
        'yUnits' : '', # none
        'leglinlog' : (3,3),
    },

#    'hVtxN_nopu': {
#        'title' : 'nPV',
#        'xMin' : 0., 'xMax' : 40.,
#        'xLabel' : 'N_{PV}',
#        'binSize' : 2,
#        'yUnits' : '', # none
#        'leglinlog' : (3,3),
#    },

    'hNumMu': {
        'title' : 'num muons',
        'xMin' : 0., 'xMax' : 7.,
        'xLabel' : 'N_{#mu}',
        'binSize' : 1.,
        'yUnits' : '', # none
        'leglinlog' : (0,3),
    },

    'hNumJets': {
        'title' : 'num jets',
        'xMin' : 0., 'xMax' : 7.,
        'xLabel' : 'N_{j}',
        'binSize' : 1.,
        'yUnits' : '', # none
        'leglinlog' : (0,3),
    },


    ###########################
    # muon variables          #
    ###########################

    'hMuPhi' : {
        'title' : 'Muon phi',
        'xMin' : -3.6, 'xMax' : 3.6,
        'xLabel' : '#phi_{#mu}',
        'binSize' : 0.4, # rad
        'yUnits' : 'rad',
        'leglinlog' : (6,0),
    },

    'hMuEta' : {
        'title' : 'Muon eta',
        'xMin' : -3., 'xMax' : 3.,
        'xLabel' : '#eta_{#mu}',
        'binSize' : 0.1,
        'yUnits' : '',
        'leglinlog' : (3,0),
    },

    'hMuPt' : {
        'title' : 'Muon p_{T} (yes RC yes SF)',
#        'xMin' : 0., 'xMax' : 100.,
        'xMin' : 20., 'xMax' : 100.,
        'xLabel' : 'p_{T #mu}',
        'binSize' : 2., # GeV
        'yUnits' : 'GeV/c',
        'leglinlog' : (3,0),
    },

#    'hMuPt_u' : {
#        'title' : 'Muon p_{T} (yes RC no SF)',
##        'xMin' : 0., 'xMax' : 100.,
#        'xMin' : 20., 'xMax' : 100.,
#        'xLabel' : 'p_{T #mu}',
#        'binSize' : 5., # GeV
#        'yUnits' : 'GeV/c',
#        'leglinlog' : (3,6),
#    },

    #'hMuPt_nrc' : {
    #    'title' : 'Muon p_{T} (no RC yes SF)',
    #    #'xMin' : 0., 'xMax' : 100.,
    #    'xLabel' : 'p_{T #mu}',
    #    'binSize' : 5., # GeV
    #    'yUnits' : 'GeV/c',
    #    'leglinlog' : (3,6),
    #},

#    'hMuPt_nrc_u' : {
#        'title' : 'Muon p_{T} (no RC no SF)',
##        'xMin' : 0., 'xMax' : 100.,
#        'xMin' : 20., 'xMax' : 100.,
#        'xLabel' : 'p_{T #mu}',
#        'binSize' : 5., # GeV
#        'yUnits' : 'GeV/c',
#        'leglinlog' : (3,6),
#    },
#
#    'hMuEnergy' : {
#        'title' : 'Muon E',
#        'xMin' : 0., 'xMax' : 100.,
#        'xLabel' : 'E_{#mu}',
#        'binSize' : 5., # GeV
#        'yUnits' : 'GeV',
#        'leglinlog' : (3,6),
#    },
#
#    'hMuMass' : {
#        'title' : 'Muon mass',
#        'xMin' : 0., 'xMax' : 1.,
#        'xLabel' : 'M_{#mu}',
#        'binSize' : 0.1, # GeV
#        'yUnits' : 'GeV/c^{2}',
#        'leglinlog' : (0,6),
#    },


    'hLeadMuPt' : {
        'title' : 'Leading muon p_{T}',
        'xMin' : 0., 'xMax' : 100.,
        'xLabel' : 'p_{T #mu_{lead}}',
        'binSize' : 2., # GeV
        'yUnits' : 'GeV/c',
        'leglinlog' : (3,0),
    },

    'hSubLeadMuPt' : {
        'title' : 'Subleading muon p_{T}',
        'xMin' : 0., 'xMax' : 100.,
        'xLabel' : 'p_{T #mu_{sublead}}',
        'binSize' : 2., # GeV
        'yUnits' : 'GeV/c',
        'leglinlog' : (3,0),
    },
###
###
###    ###########################
###    # dimuon variables        #
###    ###########################
###
####    'hNumDiMu': {
####        'title' : 'num dimuon pairs',
####        'xMin' : 0., 'xMax' : 6.,
####        'xLabel' : 'N_{#mu}',
####        'binSize' : 1.,
####        'yUnits' : '', # none
####        'leglinlog' : (0,3),
####    },
###
    'hDiMuInvMass' : {
        'title' : 'Dimuon invariant mass (yes RC yes SF)',
        'xMin' : 60., 'xMax' : 150.,
#        'xMin' : 80., 'xMax' : 100.,
        'xLabel' : 'M_{#mu^{+}#mu^{-}}',
        'binSize' : 2., # GeV
        'yUnits' : 'GeV/c^{2}',
        'leglinlog' : (3,6),
    },
###
###    'hDiMuInvMass_Category1_V_mu_h' : {
###        'title' : 'Dimuon invariant mass (Category1, V_mu_h)',
###        'xMin' : 60., 'xMax' : 150.,
####        'xMin' : 80., 'xMax' : 100.,
###        'xLabel' : 'M_{#mu^{+}#mu^{-}}',
###        'binSize' : 2., # GeV
###        'yUnits' : 'GeV/c^{2}',
###        'leglinlog' : (3,0),
###    },
###
###    'hDiMuInvMass_Category2_V_e_h' : {
###        'title' : 'Dimuon invariant mass (Category2, V_e_h)',
###        'xMin' : 60., 'xMax' : 150.,
###        'xLabel' : 'M_{#mu^{+}#mu^{-}}',
###        'binSize' : 2., # GeV
###        'yUnits' : 'GeV/c^{2}',
###        'leglinlog' : (3,0),
###    },
###
###    'hDiMuInvMass_Category3_Z_tau_h' : {
###        'title' : 'Dimuon invariant mass (Category3, Z_tau_h)',
###        'xMin' : 60., 'xMax' : 150.,
###        'xLabel' : 'M_{#mu^{+}#mu^{-}}',
###        'binSize' : 2., # GeV
###        'yUnits' : 'GeV/c^{2}',
###        'leglinlog' : (3,0),
###    },
###
###    'hDiMuInvMass_Category4_Z_mu_h' : {
###        'title' : 'Dimuon invariant mass (Category4, Z_mu_h)',
###        'xMin' : 60., 'xMax' : 150.,
###        'xLabel' : 'M_{#mu^{+}#mu^{-}}',
###        'binSize' : 2., # GeV
###        'yUnits' : 'GeV/c^{2}',
###        'leglinlog' : (3,0),
###    },
###
###    'hDiMuInvMass_Category5_Z_e_h' : {
###        'title' : 'Dimuon invariant mass (Category4, Z_e_h)',
###        'xMin' : 60., 'xMax' : 150.,
###        'xLabel' : 'M_{#mu^{+}#mu^{-}}',
###        'binSize' : 2., # GeV
###        'yUnits' : 'GeV/c^{2}',
###        'leglinlog' : (3,0),
###    },
###
####    'hDiMuInvMass_u' : {
####        'title' : 'Dimuon invariant mass (yes RC no SF)',
####        'xMin' : 60., 'xMax' : 150.,
#####        'xMin' : 80., 'xMax' : 100.,
####        'xLabel' : 'M_{#mu^{+}#mu^{-}}',
####        'binSize' : 2., # GeV
####        'yUnits' : 'GeV/c^{2}',
####        'leglinlog' : (1,4),
####    },
###
###    #'hDiMuInvMass_nrc' : {
###    #    'title' : 'Dimuon invariant mass (no RC yes SF)',
###    #    #'xMin' : 60., 'xMax' : 150.,
###    #    'xMin' : 80., 'xMax' : 110.,
###    #    'xLabel' : 'M_{#mu^{+}#mu^{-}}',
###    #    'binSize' : 2., # GeV
###    #    'yUnits' : 'GeV/c^{2}',
###    #    'leglinlog' : (3,3),
###    #},
###
####    'hDiMuInvMass_nrc_u' : {
####        'title' : 'Dimuon invariant mass (no RC no SF)',
#####        'xMin' : 60., 'xMax' : 150.,
####        'xMin' : 80., 'xMax' : 100.,
####        'xLabel' : 'M_{#mu^{+}#mu^{-}}',
####        'binSize' : 2., # GeV
####        'yUnits' : 'GeV/c^{2}',
####        'leglinlog' : (1,4),
####    },
###
###    'hDiMuEta' : {
###        'title' : 'Dimuon eta',
###        'xMin' : -3., 'xMax' : 3.,
###        'xLabel' : '#eta_{#mu^{+}#mu^{-}}',
###        'binSize' : .1,
###        'yUnits' : 'GeV/c',
###        'leglinlog' : (3,0),
###    },
###
###    'hDiMuPt' : {
###        'title' : 'Dimuon p_{T}',
###        'xMin' : 0., 'xMax' : 100.,
###        'xLabel' : 'p_{T #mu^{+}#mu^{-}}',
###        'binSize' : 5., # GeV
###        'yUnits' : 'GeV/c',
###        'leglinlog' : (1,1),
###    },
###
###    'hDiMuDeltaPhi' : {
###        'title' : 'Dimuon #Delta#phi',
###        'xMin' : -4., 'xMax' : 4.,
###        'xLabel' : '#Delta#phi_{#mu^{+}#mu^{-}}',
###        'binSize' : 0.4,
###        'yUnits' : 'rad',
###        'leglinlog' : (2,0),
###    },
#
#
#    ###########################
#    # misc                    #
#    ###########################
#
#    'hDiJetInvMass' : {
#        'title' : 'Dijet invariant mass',
#        'xMin' : 0., 'xMax' : 250.,
#        'xLabel' : 'M_{j^{+}j^{-}}',
#        'binSize' : 5., # GeV
#        'yUnits' : 'GeV/c^{2}',
#        'legendPos' : 6,
#        'leglinlog' : (3,6),
#    },

    'hEPt' : {
        'title' : 'Electron p_{T}',
#        'xMin' : 0., 'xMax' : 100.,
        'xMin' : 20., 'xMax' : 100.,
        'xLabel' : 'p_{T e}',
        'binSize' : 1., # GeV
        'yUnits' : 'GeV/c',
        'leglinlog' : (3,0),
    },


    'hNumE': {
        'title' : 'num electrons',
        'xMin' : 0., 'xMax' : 8.,
        'xLabel' : 'N_{e}',
        'binSize' : 1.,
        'yUnits' : '', # none
        'leglinlog' : (3,0),
    },


}

for step in [1,2,3,4]:
    varnames['hVtxN_step{0}'.format(step)]  = varnames['hVtxN']
    varnames['hNumMu_step{0}'.format(step)] = varnames['hNumMu']
    varnames['hMuPt_step{0}'.format(step)]  = varnames['hMuPt']
    varnames['hNumE_step{0}'.format(step)]  = varnames['hNumE']
    varnames['hEPt_step{0}'.format(step)]   = varnames['hEPt']
    varnames['hDiMuInvMass_step{0}'.format(step)] = varnames['hDiMuInvMass']

