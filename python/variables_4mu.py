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
        'yMax' : 20.,
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
        'yMax' : 15.,
        'yUnits' : 'GeV/c',
        'leglinlog' : (6,0),
    },

    'hMuEta' : {
        'title' : 'Muon eta',
        'xMin' : -3., 'xMax' : 3.,
        'xLabel' : '#eta_{#mu}',
        'yMax' : 20.,
        'yUnits' : 'GeV/c',
        'leglinlog' : (3,0),
    },

    'hMuPt' : {
        'title' : 'Muon p_{T}',
        'xMin' : 0., 'xMax' : 100.,
        'xLabel' : 'p_{T #mu}',
        'yMax' : 20.,
        'yUnits' : 'GeV/c',
        'leglinlog' : (3,3),
    },

    'hLeadMuPt' : {
        'title' : 'Leading muon p_{T}',
        'xMin' : 0., 'xMax' : 100.,
        'xLabel' : 'p_{T #mu_{lead}}',
        'yMax' : 20.,
        'yUnits' : 'GeV/c',
        'leglinlog' : (3,3),
    },

    'hSubLeadMuPt' : {
        'title' : 'Subleading muon p_{T}',
        'xMin' : 0., 'xMax' : 100.,
        'xLabel' : 'p_{T #mu_{sublead}}',
        'yMax' : 20.,
        'yUnits' : 'GeV/c',
        'leglinlog' : (3,3),
    },

    ###########################
    # dimuon variables        #
    ###########################

    'hDiMuInvMass' : {
        'title' : 'Dimuon invariant mass',
        'xMin' : 60., 'xMax' : 150.,
        'xLabel' : 'M_{#mu^{+}#mu^{-}}',
        'yMax' : 10.,
        'yUnits' : 'GeV/c^{2}',
        'leglinlog' : (3,3),
    },

    'hDiMuEta' : {
        'title' : 'Dimuon eta',
        'xMin' : -3., 'xMax' : 3.,
        'xLabel' : '#eta_{#mu^{+}#mu^{-}}',
        'yMax' : 20.,
        'yUnits' : 'GeV/c',
        'leglinlog' : (3,0),
    },

    'hDiMuPt' : {
        'title' : 'Dimuon p_{T}',
        'xMin' : 0., 'xMax' : 100.,
        'xLabel' : 'p_{T #mu^{+}#mu^{-}}',
        'yMax' : 50.,
        'yUnits' : 'GeV/c',
        'leglinlog' : (1,1),
    },

    'hDiMuDeltaPhi' : {
        'title' : 'Dimuon #Delta#phi',
        'xMin' : -4., 'xMax' : 4.,
        'xLabel' : '#Delta#phi_{#mu^{+}#mu^{-}}',
        'yMax' : 15.,
        'yUnits' : 'rad',
        'leglinlog' : (2,0),
    },


    ###########################
    # misc                    #
    ###########################



}
