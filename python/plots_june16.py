from PlotBase import PlotBase
from tools.CMS_lumi import CMS_lumi
import ROOT
class june16Plotter(PlotBase):
    def __init__(self, args):
        super(june16Plotter, self).__init__(args)

        self.lumi = 2318 # pb^-1
        self.drawBigLegend = False
        self.legendWidth = 0.16
        self.legendHeight = 0.35

        self.plotsdir = 'myplots/june16'

    def plot(self):

        # WITHOUT SF
        withoutSFs, withSFs = True, False

        # WITH SF
        #withoutSFs, withSFs = False, True

        if withoutSFs:
            self.extrainfo = 'withoutSFs'
            self.mcsamplelist = {
                'DYJets' : {
                    'tfile' : ROOT.TFile('data/june16/ana_DYJetsToLL.root'),
                    'type' : 'DY', 'label' : 'DY+Jets', 'xsec' : 6025.2, 'sumw' : (75427319225.+74570134300+77086876398+76643341637+76753312353+71020148223),
                },
                'TTJets' : {
                    'tfile' : ROOT.TFile('data/june16/ana_TTJets.root'),
                    'type' : 'TT', 'label' : 'TT+Jets', 'xsec' : 57.35, 'sumw' : (3057295.+3045081),
                },
                'TTZTo2L2Nu' : {
                    'tfile' : ROOT.TFile('data/june16/ana_TTZToLLNuNu.root'),
                    'type' : 'TTZ', 'label' : 'TTZ#rightarrow 2l2#nu', 'xsec' : 0.2529, 'sumw' : 394200.,
                },
                'WWTo2L2Nu' : {
                    'tfile' : ROOT.TFile('data/june16/ana_WWTo2L2Nu.root'),
                    'type' : 'WW', 'label' : 'WW#rightarrow 2l2#nu', 'xsec' : 12.178, 'sumw' : (530896.+628550+583100+237442),
                },
                'WZTo2L2Q' : {
                    'tfile' : ROOT.TFile('data/june16/ana_WZTo2L2q.root'),
                    'type' : 'WZ', 'label' : 'WZ#rightarrow 2l2j', 'xsec' : 5.595, 'sumw' : (45028859.+40594470+41361814+42527668+40918226),
                },
                'WZTo3LNu' : {
                    'tfile' : ROOT.TFile('data/june16/ana_WZTo3LNu.root'),
                    'type' : 'WZ', 'label' : 'WZ#rightarrow 3l#nu', 'xsec' : 4.42965, 'sumw' : (2000000.),
                },
                'ZZTo2L2Nu' : {
                    'tfile' : ROOT.TFile('data/june16/ana_ZZTo2L2Nu.root'),
                    'type' : 'ZZ', 'label' : 'ZZ#rightarrow2l2#nu', 'xsec' : 0.564, 'sumw' : (4384725.+4400325),
                },
                'ZZTo2L2Q' : {
                    'tfile' : ROOT.TFile('data/june16/ana_ZZTo2L2q.root'),
                    'type' : 'ZZ', 'label' : 'ZZ#rightarrow2l2j', 'xsec' : 3.22, 'sumw' : (14944513.+15748854+14951603+15704273+13155400),
                },
                'ZZTo4L' : {
                    'tfile' : ROOT.TFile('data/june16/ana_ZZTo4L.root'),
                    'type' : 'ZZ', 'label' : 'ZZ#rightarrow4l', 'xsec' : 1.256, 'sumw' : (3361872.+3307316),
                },
            }
            self.fullDataTitle = 'SingleMuon'
            self.datasamplelist = {
                'SMu15C' : {
                    'tfile' : ROOT.TFile('data/june16/ana_SingleMuon2015C.root'),
                    'type' : 'data',
                    'label' : 'SingleMuon Run2015C',
                },
                'SMu15D' : {
                    'tfile' : ROOT.TFile('data/june16/ana_SingleMuon2015D.root'),
                    'type' : 'data',
                    'label' : 'SingleMuon Run2015D',
                },
            }

        elif withSFs:
            self.extrainfo = 'withSFs'
            self.mcsamplelist = {
                'DYJets' : {
                    'tfile' : ROOT.TFile('data/june16_scale/ana_template_DYJetsToLL.root'),
                    'type' : 'DY', 'label' : 'DY+Jets', 'xsec' : 6025.2, 'sumw' : (154088004145. + 155017413713. + 142395714278),
                },
                'TTJets' : {
                    'tfile' : ROOT.TFile('data/june16_scale/ana_template_TTJets.root'),
                    'type' : 'TT', 'label' : 'TT+Jets', 'xsec' : 57.35, 'sumw' : 6102376.,
                },
                'TTZTo2L2Nu' : {
                    'tfile' : ROOT.TFile('data/june16_scale/ana_template_TTZToLLNuNu.root'),
                    'type' : 'TTZ', 'label' : 'TTZ#rightarrow 2l2#nu', 'xsec' : 0.2529, 'sumw' : 394200.,
                },
                'WWTo2L2Nu' : {
                    'tfile' : ROOT.TFile('data/june16_scale/ana_template_WWTo2L2Nu.root'),
                    'type' : 'WW', 'label' : 'WW#rightarrow 2l2#nu', 'xsec' : 12.178, 'sumw' : 1979988.,
                },
                'WZTo2L2Q' : {
                    'tfile' : ROOT.TFile('data/june16_scale/ana_template_WZTo2L2q.root'),
                    'type' : 'WZ', 'label' : 'WZ#rightarrow 2l2j', 'xsec' : 5.595, 'sumw' : (103013246. + 107417791.),
                },
                'WZTo3LNu' : {
                    'tfile' : ROOT.TFile('data/june16_scale/ana_template_WZTo3LNu.root'),
                    'type' : 'WZ', 'label' : 'WZ#rightarrow 3l#nu', 'xsec' : 4.42965, 'sumw' : 2000000.,
                },
                'ZZTo2L2Nu' : {
                    'tfile' : ROOT.TFile('data/june16_scale/ana_template_ZZTo2L2Nu.root'),
                    'type' : 'ZZ', 'label' : 'ZZ#rightarrow2l2#nu', 'xsec' : 0.564, 'sumw' : 8785050.,
                },
                'ZZTo2L2Q' : {
                    'tfile' : ROOT.TFile('data/june16_scale/ana_template_ZZTo2L2q.root'),
                    'type' : 'ZZ', 'label' : 'ZZ#rightarrow2l2j', 'xsec' : 3.22, 'sumw' : 74504643.,
                },
                'ZZTo4L' : {
                    'tfile' : ROOT.TFile('data/june16_scale/ana_template_ZZTo4L.root'),
                    'type' : 'ZZ', 'label' : 'ZZ#rightarrow4l', 'xsec' : 1.256, 'sumw' : 6669188.,
                },
            }
    
            self.fullDataTitle = 'SingleMuon'
            self.datasamplelist = {
                'SMu15C' : {
                    'tfile' : ROOT.TFile('data/june16_scale/ana_template_SingleMuon2015C.root'),
                    'type' : 'data', 'label' : 'SingleMuon Run2015C',
                },
                'SMu15D' : {
                    'tfile' : ROOT.TFile('data/june16_scale/ana_template_SingleMuon2015D.root'),
                    'type' : 'data', 'label' : 'SingleMuon Run2015D',
                },
            }
    

        self.extrainfo += '_23'


        self.mcStackOrder = [
            'DYJets',
            'ZZTo2L2Nu',
            'ZZTo2L2Q',
            'ZZTo4L',
            'WZTo2L2Q',
            'WZTo3LNu',
            'WWTo2L2Nu',
            'TTZTo2L2Nu',
            'TTJets',
        ]


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
                stack.Add(self.getWeightedHist(var, sample, ismc=True))

            stack.Draw('hist')

            stack.GetXaxis().SetTitle(self.varnames[var]['xLabel'])
            stack.GetXaxis().SetRangeUser(self.varnames[var]['xMin'], self.varnames[var]['xMax'])
            stack.GetHistogram().GetXaxis().SetLabelOffset(999)
            stack.GetHistogram().GetXaxis().SetLabelSize(0)
            stack.SetMinimum(0.)
            stack.SetMaximum(self.varnames[var]['yMax'])

            stack.GetYaxis().SetTitle('Events/{0} {1}'.format(stack.GetXaxis().GetBinWidth(1), self.varnames[var]['yUnits']))

            # draw data histogram
            datalist = ROOT.TList()
            for sample in self.datasamplelist:
                datalist.Add(self.getWeightedHist(var, sample, ismc=False))
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
        

## ___________________________________________________________
def main(argv=None):
    june16Plotter(argv).plot()

## ___________________________________________________________
# checks if this was run from the command line
if __name__ == '__main__':
    status = main()
#    sys.exit(status)



