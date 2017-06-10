from PlotBase import PlotBase
from tools.CMS_lumi import CMS_lumi
from datasets import *
#from variables_2mu import varnames
import ROOT
class CategoryPlotter(PlotBase):
    def __init__(self, args):
        super(CategoryPlotter, self).__init__(args)

        self.lumi = 100.
        self.textra = 'Simulation'
        self.signal_scale = 1.

        self.varnames = {
            #'hNumJets': {
            #    'title' : 'num jets',
            #    'xMin' : 0., 'xMax' : 7.,
            #    'xLabel' : 'N_{j}',
            #    'binSize' : 1.,
            #    'yUnits' : '', # none
            #    'leglinlog' : (0,3),
            #},

            'hDiMuInvMass': {
                'title' : 'dimuon inv mass',
                'xMin' : 60., 'xMax' : 150.,
                'xLabel' : 'M_{#mu^{+}#mu^{-}}',
                'binSize' : 2., # GeV
                'yUnits' : 'GeV/c^{2}',
                'leglinlog' : (0,3),
            },

            'hMuEta' : {
                'title' : 'Muon eta',
                'xMin' : -3., 'xMax' : 3.,
                'xLabel' : '#eta_{#mu}',
                'binSize' : 0.1,
                'yUnits' : '',
                'leglinlog' : (3,0),
            },

            'hDiMuPt' : {
                'title' : 'Dimuon p_{T}',
                'xMin' : 0., 'xMax' : 100.,
                'xLabel' : 'p_{T #mu^{+}#mu^{-}}',
                'binSize' : 5., # GeV
                'yUnits' : 'GeV/c',
                'leglinlog' : (3,0),
            },

            'hLeadJetPt' : {
                'title' : 'Leading jet p_{T}',
                'xMin' : 0., 'xMax' : 500.,
                'xLabel' : 'p_{T j_{lead}}',
                'binSize' : 50., # GeV
                'yUnits' : 'GeV/c',
                'leglinlog' : (0,3),
            },

            'hSubLeadJetPt' : {
                'title' : 'Subleading jet p_{T}',
                'xMin' : 0., 'xMax' : 500.,
                'xLabel' : 'p_{T j_{sublead}}',
                'binSize' : 50., # GeV
                'yUnits' : 'GeV/c',
                'leglinlog' : (0,3),
            },

            'hDiJetInvMass': {
                'title' : 'dijet inv mass',
                'xMin' : 0., 'xMax' : 1000.,
                'xLabel' : 'M_{jj}',
                'binSize' : 25., # GeV
                'yUnits' : 'GeV/c^{2}',
                'leglinlog' : (3,3),
            },

            'hDiJetDeltaEta' : {
                'title' : 'Dijet #Delta#eta',
                'xMin' : 0., 'xMax' : 6.2,
                'xLabel' : '#Delta#eta_{jj}',
                'binSize' : .2,
                'yUnits' : '',
                'leglinlog' : (0,3),
            },

            'hMET' : {
                'title' : 'MET',
                'xMin' : 0., 'xMax' : 100.,
                'xLabel' : 'MET',
                'binSize' : 5., # GeV
                'yUnits' : 'GeV/c',
                'leglinlog' : (3,0),
            },
        }

        self.version = '80X'
        self.era = 'final'

        self.extrainfo = self.era + '_les_chats'

        self.analysis = '2Mu'


        self.draw_sigs = True
        #self.draw_sigs = False

        self.draw_big_legend = False
        #self.draw_big_legend = True

        self.legend_width  = 0.16
        self.legend_height = 0.35
        self.canvas_width  = 1200
        self.canvas_height = 900


        self.plotsdir = ('/Users/ken/Work/PlotMaker/myplots'
            '/{0}/{1}'.format(self.era, self.analysis))



        self.signals = [
            'GluGlu_HToMuMu',
            'VBF_HToMuMu',
            'WMinusH_HToMuMu',
            'WPlusH_HToMuMu',
            'ZH_HToMuMu',
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
            'TTZToLLNuNu',
            'TTWJetsToLNu',
            'WWW',
            'WWZ',
            'WZZ',
            'ZZZ',
            'TZQ_ll_4f',
            'WJetsToLNu',
            'WWTo2L2Nu',
            'ST_tW_antitop_5f',
            'ST_tW_top_5f',
        ]

    def load_datasets(self):
        self.signal_sets = [None] * 5
        self.signal_sets[0] = Dataset('GluGlu_HToMuMu', self.version, self.era, self.analysis)
        self.signal_sets[1] = Dataset('VBF_HToMuMu', self.version, self.era, self.analysis)
        self.signal_sets[2] = Dataset('WMinusH_HToMuMu', self.version, self.era, self.analysis)
        self.signal_sets[3] = Dataset('WPlusH_HToMuMu', self.version, self.era, self.analysis)
        self.signal_sets[4] = Dataset('ZH_HToMuMu', self.version, self.era, self.analysis)
        for d in self.backgrounds:
            self.background_sets += [Dataset(d, self.version, self.era, self.analysis)]


    def plot(self):
        # initialise dataset objects
        self.load_datasets()

        for s in self.signal_sets+self.background_sets+self.data_sets:
            s.print_info()

        # make all the regular plots
        for var in self.varnames:
            canvname = '{0}_{1}'.format(var, 'stack')

            canv = self.get_canvas(canvname, self.canvas_width, self.canvas_height)
            plotpad = self.get_plotpad(canvname, usepull=False)
            canv.cd()

            plotpad.Draw()
            plotpad.cd()
            stack_integral = 0.

            stack = ROOT.THStack()
            for sample in reversed(self.background_sets):
                h_ = self.get_weighted_hist('categories/'+var+'_cat00', sample, self.lumi, newbinsize=self.varnames[var]['binSize'])
                stack.Add(h_)
                stack_integral += h_.Integral()

            stack.Draw('hist')

            stack.GetXaxis().SetTitle(self.varnames[var]['xLabel'])
            stack.GetXaxis().SetRangeUser(self.varnames[var]['xMin'], self.varnames[var]['xMax'])
         #   stack.GetHistogram().GetXaxis().SetLabelSize(0)
         #   stack.SetMinimum(0.)
            # set y axis
            ymax_factor = 4.8 if 'hDiJetInvMass' in var else 1.2
            stack.SetMaximum(stack.GetHistogram().GetMaximum()*ymax_factor)

            stack.GetYaxis().SetTitle('Events/{0} {1}'.format(stack.GetXaxis().GetBinWidth(1), self.varnames[var]['yUnits']))

            stack.GetXaxis().SetLabelFont(42)
 #           stack.GetXaxis().SetLabelSize(0.2)
            stack.GetXaxis().SetLabelOffset(0.01)


            stack.GetXaxis().SetTitleOffset(1.)

            print 'integral =', stack_integral
            #print 'integral =', stack.GetHistogram().Integral(0,10000)


            # draw signals
            signal_hists = []
            if self.draw_sigs:
#                for sample in reversed(self.signal_sets):
#                    h_ = self.get_weighted_hist(var, sample, self.lumi, newbinsize=self.varnames[var]['binSize'])
#                    signal_hists += [h_]
#                    h_.Draw('hist same')


                h_VBF = self.get_weighted_hist('categories/'+var+'_cat00', self.signal_sets[1], self.lumi, newbinsize=self.varnames[var]['binSize'])
                h_VBF.Scale(stack_integral/h_VBF.Integral())

                h_GGF = self.get_weighted_hist('categories/'+var+'_cat00', self.signal_sets[0], self.lumi, newbinsize=self.varnames[var]['binSize'])
                h_GGF.Scale(stack_integral/h_GGF.Integral())

                h_VH_list = ROOT.TList()
                h_VH_list.Add(self.get_weighted_hist('categories/'+var+'_cat00', self.signal_sets[2], self.lumi, newbinsize=self.varnames[var]['binSize']))
                h_VH_list.Add(self.get_weighted_hist('categories/'+var+'_cat00', self.signal_sets[3], self.lumi, newbinsize=self.varnames[var]['binSize']))
                h_VH_list.Add(self.get_weighted_hist('categories/'+var+'_cat00', self.signal_sets[4], self.lumi, newbinsize=self.varnames[var]['binSize']))
                h_VH = ROOT.TH1F(h_VH_list.At(0).Clone('VH_HToMuMu'))
                h_VH.Reset()
                h_VH.Merge(h_VH_list)
                h_VH.Scale(stack_integral/h_VH.Integral())


                signal_hists += [h_VBF]
                signal_hists += [h_GGF]
                signal_hists += [h_VH]


                for h_ in signal_hists:
                    h_.Draw('hist same')






            CMS_lumi(plotpad, self.iPeriod, self.iPos, self.lumi, self.textra);
#            stack.SetTitle(self.varnames[var]['title'])
            canv.Update()

            # save canvas
            savename = '{0}/{1}_{2}'.format(self.plotsdir, var, self.extrainfo)
            drawLinear = self.varnames[var]['leglinlog'][0] # int
            drawLog    = self.varnames[var]['leglinlog'][1] # int
            plotpad.cd()


            if drawLinear:
                #leg = self.get_legend(var, drawLinear, datahist, stack, self.signal_sets, self.signalscale)
                leg = self.get_legend(var, drawLinear, stackhist=stack, sighists=signal_hists)
                leg.Draw()
                canv.Print('{0}_lin.png'.format(savename))
                leg.Delete()
            if drawLog:
                #leg = self.get_legend(var, drawLog, datahist, stack, self.signal_sets, self.signalscale)
                leg = self.get_legend(var, drawLog, stackhist=stack, sighists=signal_hists)
                leg.Draw()
                stack.SetMinimum(1.)
                plotpad.SetLogy()
                canv.Print('{0}_log.png'.format(savename))
            canv.Clear()




## ___________________________________________________________
def main(argv=None):
    CategoryPlotter(argv).plot()

## ___________________________________________________________
# checks if this was run from the command line
if __name__ == '__main__':
    status = main()
#    sys.exit(status)



