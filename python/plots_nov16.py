from PlotBase import PlotBase
from tools.CMS_lumi import CMS_lumi
from datasets import *
from variables_2mu import varnames
import ROOT
class Nov16Plotter(PlotBase):
    def __init__(self, args):
        super(Nov16Plotter, self).__init__(args)
        self.varnames = varnames

        self.version = '80X'
        self.era = 'nov16'
        self.analysis = 'VH2Mu'

        self.extrainfo = 'run'
        self.full_data_title = 'SingleMuon'


        self.signal_scale = 10.

        #self.draw_big_legend = False
        self.draw_big_legend = True
        self.legend_width  = 0.16
        self.legend_height = 0.35
        self.canvas_width  = 12000
        self.canvas_height = 9000


        self.plotsdir = '/Users/ken/Work/PlotMaker/myplots/{0}'.format(self.era)



        self.signals = [
        #    'GluGlu_HToMuMu',
        #    'VBF_HToMuMu',
            'WMinusH_HToMuMu',
            'WPlusH_HToMuMu',
            'ZH_HToMuMu',
        ]

        self.backgrounds = [
            'DYJetsToLL',
            'TTJets',
        #    'WWTo2L2Nu',
            'WWW',
            'WWZ',
            'WZTo2L2Q',
            'WZTo3LNu',
            'WZZ',
        #    'ZZTo2L2Nu',
        #    'ZZTo2L2Q',
            'ZZTo4L',
            'ZZZ',
        ]

        self.datas = [
            'SingleMuon_Run2016B',
            'SingleMuon_Run2016Bv3',
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
            self.signal_sets += [Dataset(d, self.version, self.era, self.analysis)]
        for d in self.backgrounds:
            self.background_sets += [Dataset(d, self.version, self.era, self.analysis)]
        for d in self.datas:
            self.data_sets += [Dataset(d, self.version, self.era, self.analysis)]





    def plot(self):

        # initialise dataset objects
        self.load_datasets()

        self.lumi = 0.
        for d in self.data_sets:
            self.lumi += d.lumi
        print 'total lumi = ' + str(self.lumi)



        for s in self.signal_sets+self.background_sets+self.data_sets:
            s.print_info()

        # make all the regular plots
        for var in self.varnames:

            if not any(x in var for x in ['step','Eff']): continue

            if 'Category' not in var: continue
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
                h_ = self.get_weighted_hist(var, sample, self.lumi, newbinsize=self.varnames[var]['binSize'])
                stack.Add(h_)

            stack.Draw('hist')

            stack.GetXaxis().SetTitle(self.varnames[var]['xLabel'])
            stack.GetXaxis().SetRangeUser(self.varnames[var]['xMin'], self.varnames[var]['xMax'])
            stack.GetHistogram().GetXaxis().SetLabelOffset(999)
            stack.GetHistogram().GetXaxis().SetLabelSize(0)
            stack.SetMinimum(0.)
            # set y axis
            stack.SetMaximum(stack.GetHistogram().GetMaximum()*1.2)

            stack.GetYaxis().SetTitle('Events/{0} {1}'.format(stack.GetXaxis().GetBinWidth(1), self.varnames[var]['yUnits']))

            # draw MC statistical unc
            stackerr = stack.GetStack().Last().Clone()
            stackerr.SetLineColor(ROOT.kGray+3)
            stackerr.SetFillColor(ROOT.kGray+3)
            stackerr.SetFillStyle(3013)
            stackerr.SetMarkerSize(0)
            stackerr.SetLineWidth(0)
            stackerr.Draw('e2 same')


            # draw signals

            for sample in reversed(self.signal_sets):
                h_ = self.get_weighted_hist(var, sample, self.lumi, newbinsize=self.varnames[var]['binSize'])
                self.signal_hists += [h_]
                h_.Draw('same')




            # draw data histogram
            datalist = ROOT.TList()
            for sample in self.data_sets:
                datalist.Add(self.get_weighted_hist(var, sample, self.lumi, newbinsize=self.varnames[var]['binSize']))
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
        
            unity = ROOT.TF1('unity', '1', 0.9*self.varnames[var]['xMin'], 1.1*self.varnames[var]['xMax'])
            unity.SetLineColor(ROOT.kRed)
            unity.Draw('same')
        
            CMS_lumi(plotpad, self.iPeriod, self.iPos, self.lumi);
            stack.SetTitle(self.varnames[var]['title'])
            canv.Update()

            # save canvas
            savename = '{0}/{1}_{2}'.format(self.plotsdir, var, self.extrainfo)
            drawLinear = self.varnames[var]['leglinlog'][0] # int
            drawLog    = self.varnames[var]['leglinlog'][1] # int
            plotpad.cd()

            if drawLinear:
                #leg = self.get_legend(var, drawLinear, datahist, stack, self.signal_sets, self.signalscale)
                leg = self.get_legend(var, drawLinear, datahist, stack)
                leg.Draw()
                canv.Print('{0}_lin.png'.format(savename))
                leg.Delete()
            if drawLog:
                #leg = self.get_legend(var, drawLog, datahist, stack, self.signal_sets, self.signalscale)
                leg = self.get_legend(var, drawLog, datahist, stack)
                leg.Draw()
                stack.SetMinimum(1.)
                plotpad.SetLogy()
                canv.Print('{0}_log.png'.format(savename))
            canv.Clear()
        

#
#
#
#        # make all the control plots
#        for var in self.varnames:
#            try: # not everything in varnames has a control plot
#                canvname = '{0}_{1}'.format(var+'_ctrl', 'stack')
#                canv = ROOT.TCanvas(canvname, canvname, 800, 600)
#                canv.SetLeftMargin(0.12)
#                canv.SetRightMargin(0.04)
#                canv.SetTopMargin(0.08)
#                canv.SetBottomMargin(0.12)
#
#                plotpad = ROOT.TPad(canvname+'_plot', canvname+'_plot', 0.0, 0.2, 1.0, 1.0)
#                pullpad = ROOT.TPad(canvname+'_pull', canvname+'_pull', 0.0, 0.0, 1.0, 0.2)
#                plotpad.SetBottomMargin(0.03)
#                plotpad.SetBorderMode(0)
#                plotpad.SetBorderSize(0)
#                plotpad.SetLeftMargin(0.14)
#                plotpad.SetRightMargin(0.04)
#                plotpad.SetTopMargin(0.08/0.8)
#                pullpad.SetTopMargin(0.01)
#                pullpad.SetBorderMode(0)
#                pullpad.SetBorderSize(0)
#                pullpad.SetLeftMargin(0.14)
#                pullpad.SetRightMargin(0.04)
#                pullpad.SetBottomMargin(0.12/0.2)
#                plotpad.Draw()
#                pullpad.Draw()
#                plotpad.cd()
#
#                stack = ROOT.THStack()
#                for sample in reversed(self.mcStackOrder):
#                    stack.Add(self.getWeightedHist('control/'+var+'_ctrl', sample, self.varnames[var]['binSize'], ismc=True))
#
#                stack.Draw('hist')
#
#                stack.GetXaxis().SetTitle(self.varnames[var]['xLabel'])
#                stack.GetXaxis().SetRangeUser(self.varnames[var]['xMin'], self.varnames[var]['xMax'])
#                stack.GetHistogram().GetXaxis().SetLabelOffset(999)
#                stack.GetHistogram().GetXaxis().SetLabelSize(0)
#                stack.SetMinimum(0.)
#                # set y axis
#                stack.SetMaximum(stack.GetHistogram().GetMaximum()*1.2)
#
#                stack.GetYaxis().SetTitle('Events/{0} {1}'.format(stack.GetXaxis().GetBinWidth(1), self.varnames[var]['yUnits']))
#
#                # draw data histogram
#                datalist = ROOT.TList()
#                for sample in self.datasamplelist:
#                    datalist.Add(self.getWeightedHist('control/'+var+'_ctrl', sample, self.varnames[var]['binSize'], ismc=False))
#                datahist = ROOT.TH1F(datalist.At(0).Clone('datahist'))
#                datahist.Reset()
#                datahist.Merge(datalist)
#
#                datahist.Draw('p0 same')
#
#                # draw goodness histogram
#                pullpad.cd()
#                numhist = datahist.Clone()
#                denhist = stack.GetStack().Last().Clone()
#                goodnesshist = self.get_ratio_hist(numhist, denhist, var) #var is only used to access varnames, not hists
#                goodnesshist.Draw()
#        
#                unity = ROOT.TF1('unity', '1', 0.9*self.varnames[var]['xMin'], 1.1*self.varnames[var]['xMax'])
#                unity.SetLineColor(ROOT.kRed)
#                unity.Draw('same')
#        
#                CMS_lumi(plotpad, self.iPeriod, self.iPos, self.lumi);
#                stack.SetTitle(self.varnames[var]['title']+'_ctrl')
#                canv.Update()
#
#                # save canvas
#                savename = '{0}/{1}_{2}'.format(self.plotsdir, var+'_ctrl', self.extrainfo)
#                drawLinear = self.varnames[var]['leglinlog'][0]
#                drawLog    = self.varnames[var]['leglinlog'][1]
#                plotpad.cd()
#
#                if drawLinear:
#                    leg = self.get_legend(var, drawLinear, datahist, stack)
#                    leg.Draw()
#                    canv.Print('{0}_lin.png'.format(savename))
#                    leg.Delete()
#                if drawLog:
#                    leg = self.get_legend(var, drawLog, datahist, stack)
#                    leg.Draw()
#                    stack.SetMinimum(1.)
#                    plotpad.SetLogy()
#                    canv.Print('{0}_log.png'.format(savename))
#                canv.Clear()
#
#            except:
#                pass


## ___________________________________________________________
def main(argv=None):
    Nov16Plotter(argv).plot()

## ___________________________________________________________
# checks if this was run from the command line
if __name__ == '__main__':
    status = main()
#    sys.exit(status)



