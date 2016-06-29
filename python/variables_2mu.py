# variables.py
'''
leglinlog: 
    legend position for (linear plot, log plot)
    if either is 0, it will not make that plot
'''

varnames = {

    ###########################
    # event variables         #
    ###########################

    'hVtxN': {
        'title' : 'nPV after reweighting',
        'xMin' : 0., 'xMax' : 40.,
        'xLabel' : 'N_{PV}',
        'binSize' : 1.,
        'yUnits' : '', # none
        'leglinlog' : (3,3),
    },

    'hVtxN_u': {
        'title' : 'nPV with PU weight but no event weight',
        'xMin' : 0., 'xMax' : 40.,
        'xLabel' : 'N_{PV}',
        'binSize' : 1.,
        'yUnits' : '', # none
        'leglinlog' : (3,3),
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
        'xMin' : 0., 'xMax' : 100.,
        'xLabel' : 'p_{T #mu}',
        'binSize' : 5., # GeV
        'yUnits' : 'GeV/c',
        'leglinlog' : (3,6),
    },

    'hMuPt_u' : {
        'title' : 'Muon p_{T} (yes RC no SF)',
        'xMin' : 0., 'xMax' : 100.,
        'xLabel' : 'p_{T #mu}',
        'binSize' : 5., # GeV
        'yUnits' : 'GeV/c',
        'leglinlog' : (3,6),
    },

    'hMuPt_nrc' : {
        'title' : 'Muon p_{T} (no RC yes SF)',
        'xMin' : 0., 'xMax' : 100.,
        'xLabel' : 'p_{T #mu}',
        'binSize' : 5., # GeV
        'yUnits' : 'GeV/c',
        'leglinlog' : (3,6),
    },

    'hMuPt_nrc_u' : {
        'title' : 'Muon p_{T} (no RC no SF)',
        'xMin' : 0., 'xMax' : 100.,
        'xLabel' : 'p_{T #mu}',
        'binSize' : 5., # GeV
        'yUnits' : 'GeV/c',
        'leglinlog' : (3,6),
    },

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
        'binSize' : 5., # GeV
        'yUnits' : 'GeV/c',
        'leglinlog' : (3,6),
    },

    'hSubLeadMuPt' : {
        'title' : 'Subleading muon p_{T}',
        'xMin' : 0., 'xMax' : 100.,
        'xLabel' : 'p_{T #mu_{sublead}}',
        'binSize' : 5., # GeV
        'yUnits' : 'GeV/c',
        'leglinlog' : (3,6),
    },


    ###########################
    # dimuon variables        #
    ###########################

    'hDiMuInvMass' : {
        'title' : 'Dimuon invariant mass (yes RC yes SF)',
        'xMin' : 60., 'xMax' : 150.,
        'xLabel' : 'M_{#mu^{+}#mu^{-}}',
        'binSize' : 2., # GeV
        'yUnits' : 'GeV/c^{2}',
        'leglinlog' : (3,3),
    },

    'hDiMuInvMass_u' : {
        'title' : 'Dimuon invariant mass (yes RC no SF)',
        'xMin' : 60., 'xMax' : 150.,
        'xLabel' : 'M_{#mu^{+}#mu^{-}}',
        'binSize' : 2., # GeV
        'yUnits' : 'GeV/c^{2}',
        'leglinlog' : (3,3),
    },

    'hDiMuInvMass_nrc' : {
        'title' : 'Dimuon invariant mass (no RC yes SF)',
        'xMin' : 60., 'xMax' : 150.,
        'xLabel' : 'M_{#mu^{+}#mu^{-}}',
        'binSize' : 2., # GeV
        'yUnits' : 'GeV/c^{2}',
        'leglinlog' : (3,3),
    },

    'hDiMuInvMass_nrc_u' : {
        'title' : 'Dimuon invariant mass (no RC no SF)',
        'xMin' : 60., 'xMax' : 150.,
        'xLabel' : 'M_{#mu^{+}#mu^{-}}',
        'binSize' : 2., # GeV
        'yUnits' : 'GeV/c^{2}',
        'leglinlog' : (3,3),
    },

    'hDiMuEta' : {
        'title' : 'Dimuon eta',
        'xMin' : -3., 'xMax' : 3.,
        'xLabel' : '#eta_{#mu^{+}#mu^{-}}',
        'binSize' : .1,
        'yUnits' : 'GeV/c',
        'leglinlog' : (3,0),
    },

    'hDiMuPt' : {
        'title' : 'Dimuon p_{T}',
        'xMin' : 0., 'xMax' : 100.,
        'xLabel' : 'p_{T #mu^{+}#mu^{-}}',
        'binSize' : 5., # GeV
        'yUnits' : 'GeV/c',
        'leglinlog' : (1,1),
    },

    'hDiMuDeltaPhi' : {
        'title' : 'Dimuon #Delta#phi',
        'xMin' : -4., 'xMax' : 4.,
        'xLabel' : '#Delta#phi_{#mu^{+}#mu^{-}}',
        'binSize' : 0.4,
        'yUnits' : 'rad',
        'leglinlog' : (2,0),
    },


    ###########################
    # misc                    #
    ###########################

    'hDiJetInvMass' : {
        'title' : 'Dijet invariant mass',
        'xMin' : 0., 'xMax' : 250.,
        'xLabel' : 'M_{j^{+}j^{-}}',
        'binSize' : 5., # GeV
        'yUnits' : 'GeV/c^{2}',
        'legendPos' : 6,
        'leglinlog' : (3,6),
    },


}
