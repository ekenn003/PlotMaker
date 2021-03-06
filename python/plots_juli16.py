from PlotBase import PlotBase
from tools.CMS_lumi import CMS_lumi
from datasets import mc_80X, data_80X
from variables_2mu import varnames
import ROOT
class juli16Plotter(PlotBase):
    def __init__(self, args):
        super(juli16Plotter, self).__init__(args)
        self.varnames = varnames

        self.lumi = 6260 # pb^-1
        #self.drawBigLegend = False
        self.drawBigLegend = True
        self.legendWidth = 0.16
        self.legendHeight = 0.35

        self.plotsdir = 'myplots/juli16'

    def plot(self):

        self.extrainfo = '80X_25_25'
        self.mcsamplelist = mc_80X
        self.fullDataTitle = 'SingleMuon'
        self.datasamplelist = data_80X


        self.mcStackOrder = [
            'DYJets',
            'TTZJets',
            'TTWJets',
            'tZq_ll_4f',
            'TTJets',
        ]


        # make all the regular plots
        for var in self.varnames:
            canvname = '{0}_{1}'.format(var, 'stack')
            canv = ROOT.TCanvas(canvname, canvname, 800, 600)
            canv.SetLeftMargin(0.12)
            canv.SetRightMargin(0.04)
            canv.SetTopMargin(0.08)
            canv.SetBottomMargin(0.12)

            plotpad = ROOT.TPad(canvname+'_plot', canvname+'_plot', 0.0, 0.2, 1.0, 1.0)
            pullpad = ROOT.TPad(canvname+'_pull', canvname+'_pull', 0.0, 0.0, 1.0, 0.2)
            plotpad.SetBottomMargin(0.03)
            plotpad.SetBorderMode(0)
            plotpad.SetBorderSize(0)
            plotpad.SetLeftMargin(0.14)
            plotpad.SetRightMargin(0.04)
            plotpad.SetTopMargin(0.08/0.8)
            pullpad.SetTopMargin(0.01)
            pullpad.SetBorderMode(0)
            pullpad.SetBorderSize(0)
            pullpad.SetLeftMargin(0.14)
            pullpad.SetRightMargin(0.04)
            pullpad.SetBottomMargin(0.12/0.2)
            plotpad.Draw()
            pullpad.Draw()
            plotpad.cd()

            stack = ROOT.THStack()
            for sample in reversed(self.mcStackOrder):
                stack.Add(self.getWeightedHist(var, sample, self.varnames[var]['binSize'], ismc=True))

            stack.Draw('hist')

            stack.GetXaxis().SetTitle(self.varnames[var]['xLabel'])
            stack.GetXaxis().SetRangeUser(self.varnames[var]['xMin'], self.varnames[var]['xMax'])
            stack.GetHistogram().GetXaxis().SetLabelOffset(999)
            stack.GetHistogram().GetXaxis().SetLabelSize(0)
            stack.SetMinimum(0.)
            # set y axis
            stack.SetMaximum(stack.GetHistogram().GetMaximum()*1.2)

            stack.GetYaxis().SetTitle('Events/{0} {1}'.format(stack.GetXaxis().GetBinWidth(1), self.varnames[var]['yUnits']))

            # draw data histogram
            datalist = ROOT.TList()
            for sample in self.datasamplelist:
                datalist.Add(self.getWeightedHist(var, sample, self.varnames[var]['binSize'], ismc=False))
            datahist = ROOT.TH1F(datalist.At(0).Clone('datahist'))
            datahist.Reset()
            datahist.Merge(datalist)

            datahist.Draw('p0 same')

            # draw goodness histogram
            pullpad.cd()
            numhist = datahist.Clone()
            denhist = stack.GetStack().Last().Clone()
            goodnesshist = self.getRatioHist(numhist, denhist, var)
            goodnesshist.Draw()
        
            unity = ROOT.TF1('unity', '1', 0.9*self.varnames[var]['xMin'], 1.1*self.varnames[var]['xMax'])
            unity.SetLineColor(ROOT.kRed)
            unity.Draw('same')
        
            CMS_lumi(plotpad, self.iPeriod, self.iPos, self.lumi);
            stack.SetTitle(self.varnames[var]['title'])
            canv.Update()

            # save canvas
            savename = '{0}/{1}_{2}'.format(self.plotsdir, var, self.extrainfo)
            drawLinear = self.varnames[var]['leglinlog'][0]
            drawLog    = self.varnames[var]['leglinlog'][1]
            plotpad.cd()

            if drawLinear:
                leg = self.getLegend(var, drawLinear, datahist, stack)
                leg.Draw()
                canv.Print('{0}_lin.png'.format(savename))
                leg.Delete()
            if drawLog:
                leg = self.getLegend(var, drawLog, datahist, stack)
                leg.Draw()
                stack.SetMinimum(1.)
                plotpad.SetLogy()
                canv.Print('{0}_log.png'.format(savename))
            canv.Clear()
        




        # make all the control plots
        for var in self.varnames:
            try: # not everything in varnames has a control plot
                canvname = '{0}_{1}'.format(var+'_ctrl', 'stack')
                canv = ROOT.TCanvas(canvname, canvname, 800, 600)
                canv.SetLeftMargin(0.12)
                canv.SetRightMargin(0.04)
                canv.SetTopMargin(0.08)
                canv.SetBottomMargin(0.12)

                plotpad = ROOT.TPad(canvname+'_plot', canvname+'_plot', 0.0, 0.2, 1.0, 1.0)
                pullpad = ROOT.TPad(canvname+'_pull', canvname+'_pull', 0.0, 0.0, 1.0, 0.2)
                plotpad.SetBottomMargin(0.03)
                plotpad.SetBorderMode(0)
                plotpad.SetBorderSize(0)
                plotpad.SetLeftMargin(0.14)
                plotpad.SetRightMargin(0.04)
                plotpad.SetTopMargin(0.08/0.8)
                pullpad.SetTopMargin(0.01)
                pullpad.SetBorderMode(0)
                pullpad.SetBorderSize(0)
                pullpad.SetLeftMargin(0.14)
                pullpad.SetRightMargin(0.04)
                pullpad.SetBottomMargin(0.12/0.2)
                plotpad.Draw()
                pullpad.Draw()
                plotpad.cd()

                stack = ROOT.THStack()
                for sample in reversed(self.mcStackOrder):
                    stack.Add(self.getWeightedHist('control/'+var+'_ctrl', sample, self.varnames[var]['binSize'], ismc=True))

                stack.Draw('hist')

                stack.GetXaxis().SetTitle(self.varnames[var]['xLabel'])
                stack.GetXaxis().SetRangeUser(self.varnames[var]['xMin'], self.varnames[var]['xMax'])
                stack.GetHistogram().GetXaxis().SetLabelOffset(999)
                stack.GetHistogram().GetXaxis().SetLabelSize(0)
                stack.SetMinimum(0.)
                # set y axis
                stack.SetMaximum(stack.GetHistogram().GetMaximum()*1.2)

                stack.GetYaxis().SetTitle('Events/{0} {1}'.format(stack.GetXaxis().GetBinWidth(1), self.varnames[var]['yUnits']))

                # draw data histogram
                datalist = ROOT.TList()
                for sample in self.datasamplelist:
                    datalist.Add(self.getWeightedHist('control/'+var+'_ctrl', sample, self.varnames[var]['binSize'], ismc=False))
                datahist = ROOT.TH1F(datalist.At(0).Clone('datahist'))
                datahist.Reset()
                datahist.Merge(datalist)

                datahist.Draw('p0 same')

                # draw goodness histogram
                pullpad.cd()
                numhist = datahist.Clone()
                denhist = stack.GetStack().Last().Clone()
                goodnesshist = self.getRatioHist(numhist, denhist, var) #var is only used to access varnames, not hists
                goodnesshist.Draw()
        
                unity = ROOT.TF1('unity', '1', 0.9*self.varnames[var]['xMin'], 1.1*self.varnames[var]['xMax'])
                unity.SetLineColor(ROOT.kRed)
                unity.Draw('same')
        
                CMS_lumi(plotpad, self.iPeriod, self.iPos, self.lumi);
                stack.SetTitle(self.varnames[var]['title']+'_ctrl')
                canv.Update()

                # save canvas
                savename = '{0}/{1}_{2}'.format(self.plotsdir, var+'_ctrl', self.extrainfo)
                drawLinear = self.varnames[var]['leglinlog'][0]
                drawLog    = self.varnames[var]['leglinlog'][1]
                plotpad.cd()

                if drawLinear:
                    leg = self.getLegend(var, drawLinear, datahist, stack)
                    leg.Draw()
                    canv.Print('{0}_lin.png'.format(savename))
                    leg.Delete()
                if drawLog:
                    leg = self.getLegend(var, drawLog, datahist, stack)
                    leg.Draw()
                    stack.SetMinimum(1.)
                    plotpad.SetLogy()
                    canv.Print('{0}_log.png'.format(savename))
                canv.Clear()

            except:
                pass


## ___________________________________________________________
def main(argv=None):
    juli16Plotter(argv).plot()

## ___________________________________________________________
# checks if this was run from the command line
if __name__ == '__main__':
    status = main()
#    sys.exit(status)



