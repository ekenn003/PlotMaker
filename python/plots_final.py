from PlotBase import PlotBase
from tools.CMS_lumi import CMS_lumi
from datasets import *
from variables_2mu import varnames
import ROOT
class Apr17Plotter(PlotBase):
    def __init__(self, args):
        super(Apr17Plotter, self).__init__(args)
        #self.varnames = varnames
        self.iPos = 11
        self.cats = ['cat'+str(i).zfill(2) for i in xrange(16)]
        self.era = 'golden'
        #self.extrainfo = self.era + '_pu'
        self.extrainfo = self.era + '_ctrl'

        self.varnames = {
            #'hVtxN_withpu': {
            #    'title' : 'N_{PV} after PU reweighting',
            #    'xMin' : 0., 'xMax' : 70.,
            #    'xLabel' : 'N_{PV}',
            #    'binSize' : 1.,
            #    'yUnits' : '', # none
            #    'leglinlog' : (0,3),
            #},

            #'hVtxN_withoutpu': {
            #    'title' : 'N_{PV} before PU reweighting',
            #    'xMin' : 0., 'xMax' : 70.,
            #    'xLabel' : 'N_{PV}',
            #    'binSize' : 1.,
            #    'yUnits' : '', # none
            #    'leglinlog' : (0,3),
            #},

            'hDiMuInvMass': {
                'title' : 'dimuon inv mass',
                'xMin' : 60., 'xMax' : 150.,
                'xLabel' : 'M_{#mu^{+}#mu^{-}}',
                'binSize' : 5., # GeV
                'yUnits' : 'GeV/c^{2}',
                'leglinlog' : (3,3),
            },
            'hMuPt' : {
                'title' : 'Muon p_{T}',
                'xMin' : 0., 'xMax' : 100.,
                'xLabel' : 'p_{T #mu}',
                'binSize' : 5., # GeV
                'yUnits' : 'GeV/c',
                'leglinlog' : (3,0),
            },
            'hJetPt' : {
                'title' : 'Jet p_{T}',
                'xMin' : 0., 'xMax' : 100.,
                'xLabel' : 'p_{T jet}',
                'binSize' : 5., # GeV
                'yUnits' : 'GeV/c',
                'leglinlog' : (3,0),
            },
            'hDiMuPt' : {
                'title' : 'Dimuon p_{T}',
                'xMin' : 0., 'xMax' : 100.,
                'xLabel' : 'p_{T #mu#mu}}',
                'binSize' : 5., # GeV
                'yUnits' : 'GeV/c',
                'leglinlog' : (3,0),
            },
            'hNumJets' : {
                'title' : 'N_{jets}',
                'xMin' : 0., 'xMax' : 10.,
                'xLabel' : 'N_{j}',
                'binSize' : 1, # GeV
                'yUnits' : 'GeV/c',
                'leglinlog' : (3,0),
            },
            'hMET' : {
                'title' : 'MET',
                'xMin' : 0., 'xMax' : 100.,
                'xLabel' : 'MET',
                'binSize' : 5., # GeV
                'yUnits' : 'GeV/c',
                'leglinlog' : (3,0),
            },
            'hMuEta' : {
                'title' : 'Muon #eta',
                'xMin' : -7., 'xMax' : 7.,
                'xLabel' : '#eta_{#mu}',
                'binSize' : .2,
                'yUnits' : '',
                'leglinlog' : (3,0),
            },
        }


        self.version = '80X'

        self.textra = 'Preliminary'

        self.analysis = '2Mu'

        self.full_data_title = 'SingleMuon'

        self.signal_scale = 1000.

        #self.draw_sigs = True
        self.draw_sigs = False

        self.draw_big_legend = False
        #self.draw_big_legend = True
        self.draw_tiny_legend = True
        #self.draw_tiny_legend = False

        self.legend_width  = 0.16
        self.legend_height = 0.35
        self.canvas_width  = 1200
        self.canvas_height = 900


        self.plotsdir = ('/Users/ken/Work/PlotMaker/myplots'
            #'/{0}/{1}'.format(self.era, self.analysis))
            '/{0}/ctrl'.format(self.era))


        self.jank = 1.

        self.signals = [
#            'GluGlu_HToMuMu',
#            'VBF_HToMuMu',
#            'WMinusH_HToMuMu',
#            'WPlusH_HToMuMu',
#            'ZH_HToMuMu',
        ]

        # this is also the order in which they will be stacked
        self.backgrounds = [
            'DYJetsToLL',
            'TTJets',
            'ZZTo2L2Nu',
            'ZZTo2L2Q',
            'ZZTo4L',
            'WZTo2L2Q',
            'WZTo3LNu',
            'WWTo2L2Nu',
            'TTZToLLNuNu',
            'TTWJetsToLNu',
#            'WWW',
#            'WWZ',
#            'WZZ',
#            'ZZZ',
#            'TZQ_ll_4f',
#            'WJetsToLNu',
#            'ST_tW_antitop_5f',
#            'ST_tW_top_5f',
        ]

        self.datas = [
            #'SingleMuon_Run2016',
            'SingleMuon_Run2016Bv2',
            'SingleMuon_Run2016C',
            'SingleMuon_Run2016D',
            'SingleMuon_Run2016E',
            'SingleMuon_Run2016F',
            'SingleMuon_Run2016G',
            'SingleMuon_Run2016Hv2',
            'SingleMuon_Run2016Hv3',
        ]


    def load_datasets(self):
        for d in self.signals:
            self.signal_sets += [Dataset(d, self.version,
                self.era, self.analysis)]
        for d in self.backgrounds:
            self.background_sets += [Dataset(d, self.version,
                self.era, self.analysis)]
        for d in self.datas:
            self.data_sets += [Dataset(d, self.version,
                self.era, self.analysis)]








    def plot(self):

        # initialise dataset objects
        self.load_datasets()

        self.lumi = 35920
#        self.lumi = 0.
#        for d in self.data_sets:
#            self.lumi += d.lumi

        for s in self.signal_sets+self.background_sets+self.data_sets:
            s.print_info()

        #cat = 'cat00'
        for cat in self.cats:


            # make all the regular plots
            for var in self.varnames:
                if 'hVtxN' in var and cat != 'cat00': continue


                # only do the ones with this in the name
                #if not any(x in var for x in ['Vtx','MuPt','InvMass','Num']): continue
                #if any(x in var for x in ['Eff','step']): continue

                canvname = '{0}_{1}'.format(var, 'stack')

                canv = self.get_canvas(canvname, self.canvas_width, self.canvas_height)
                plotpad = self.get_plotpad(canvname)
                pullpad = self.get_pullpad(canvname)
                canv.cd()

                plotpad.Draw()
                pullpad.Draw()
                plotpad.cd()

                stack = ROOT.THStack()
                for sample in reversed(self.background_sets):
                    hname_ = 'control/'+var+'_'+cat+'_ctrl'
                    #hname_ = 'categories/'+var+'_'+cat
                    h_ = self.get_weighted_hist(hname_, sample, self.lumi, 
                        newbinsize=self.varnames[var]['binSize'])
                    h_.Scale(self.jank)
                    stack.Add(h_)

                stack.Draw('hist')

                stack.GetXaxis().SetTitle(self.varnames[var]['xLabel'])
                stack.GetXaxis().SetRangeUser(self.varnames[var]['xMin'],
                    self.varnames[var]['xMax'])
                stack.GetHistogram().GetXaxis().SetLabelOffset(999)
                stack.GetHistogram().GetXaxis().SetLabelSize(0)
                stack.SetMinimum(0.)
                # set y axis
                stack.SetMaximum(stack.GetHistogram().GetMaximum()*1.4)

                stack.GetYaxis().SetTitle('Events/{0} {1}'.format(stack.GetXaxis().GetBinWidth(1),
                    self.varnames[var]['yUnits']))

                # draw MC statistical unc
                stackerr = stack.GetStack().Last().Clone()
                stackerr.SetLineColor(ROOT.kGray+3)
                stackerr.SetFillColor(ROOT.kGray+3)
                stackerr.SetFillStyle(3013)
                stackerr.SetMarkerSize(0)
                stackerr.SetLineWidth(0)
                stackerr.Draw('e2 same')


                ## draw signals
                signal_hists = []
                #if self.draw_sigs:
                #    for sample in reversed(self.signal_sets):
                #        h_ = self.get_weighted_hist(var, sample, self.lumi, newbinsize=self.varnames[var]['binSize'])
                #        h_.Scale(self.hltf)
                #        signal_hists += [h_]
                #        h_.Draw('hist same')




                # draw data histogram
                datalist = ROOT.TList()
                for sample in self.data_sets:
                    datalist.Add(self.get_weighted_hist(hname_, sample, self.lumi,
                        newbinsize=self.varnames[var]['binSize']))
                datahist = ROOT.TH1F(datalist.At(0).Clone('datahist'))
                datahist.Reset()
                datahist.Merge(datalist)

                #datahist.Draw('p0 same')
                datahist.Draw('p same')

                # draw goodness histogram
                pullpad.cd()
                numhist = datahist.Clone()
                denhist = stack.GetStack().Last().Clone()
                goodnesshist = self.get_ratio_hist(numhist, denhist, var)
                goodnesshist.Draw()
            
                unity = ROOT.TF1('unity', '1', 0.9*self.varnames[var]['xMin'],
                    1.1*self.varnames[var]['xMax'])
                unity.SetLineColor(ROOT.kRed)
                unity.SetLineStyle(2)
                unity.Draw('same')
            
                CMS_lumi(plotpad, self.iPeriod, self.iPos, self.lumi, self.textra);
#                stack.SetTitle(self.varnames[var]['title'])
                canv.Update()

                # save canvas
                savename = '{0}/{1}_{3}_{2}'.format(self.plotsdir, var, self.extrainfo, cat)
                drawLinear = self.varnames[var]['leglinlog'][0] # int
                drawLog    = self.varnames[var]['leglinlog'][1] # int
                plotpad.cd()

                if drawLinear:
                    #leg = self.get_legend(var, drawLinear, datahist, stack, self.signal_sets, self.signalscale)
                    leg = self.get_legend(var, drawLinear, datahist=datahist, stackhist=stack, sighists=signal_hists)
                    leg.SetHeader(cat)
                    leg.Draw()
                    canv.Print('{0}_lin.png'.format(savename))
                    leg.Delete()
                if drawLog:
                    #leg = self.get_legend(var, drawLog, datahist, stack, self.signal_sets, self.signalscale)
                    stack.SetMaximum(stack.GetHistogram().GetMaximum()*10)
                    datahist.SetMaximum(stack.GetHistogram().GetMaximum()*10)
                    leg = self.get_legend(var, drawLog, datahist=datahist, stackhist=stack, sighists=signal_hists)
                    leg.SetHeader(cat)
                    leg.Draw()
                    stack.SetMinimum(1.)
                    plotpad.SetLogy()
                    canv.Print('{0}_log.png'.format(savename))
                canv.Clear()







## ___________________________________________________________
def main(argv=None):
    Apr17Plotter(argv).plot()

## ___________________________________________________________
# checks if this was run from the command line
if __name__ == '__main__':
    status = main()
#    sys.exit(status)



