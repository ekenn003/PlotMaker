from PlotBase import PlotBase
from tools.CMS_lumi import CMS_lumi
import numpy as np
from ROOT import TCanvas, TPad, TFile
from ROOT import TGraphAsymmErrors, TH2D, TLegend
from ROOT import TMarker, TBox, TGaxis
from ROOT import kYellow, kGreen, kWhite, kBlack, kOrange
class CatLimPlotter(PlotBase):
    def __init__(self, args):
        super(CatLimPlotter, self).__init__(args)



        self.xmax = 5.

        #self.setlog = True
        self.setlog = False



        #self.blind = True
        self.blind = False

        self.leg_x1, self.leg_y1 = 0.25, 0.25
        self.leg_x2, self.leg_y2 = 0.6, 0.35


        self.canvas_width  = 1700
        self.canvas_height = 1100

        self.leftmargin = 0.3
        self.bottommargin = 0.15


        self.lumi = 35920.
        self.textra = '      Simulation' if self.blind else '        Preliminary'
        self.iPos = 0

        self.plotsdir = '/Users/ken/Work/PlotMaker/myplots/catlims'

        self.fname_head = '/Users/ken/Work/PlotMaker/data/combine/higgsCombine_'
        self.fname_tail = '.Asymptotic.mH125.root'


        # this list is ordered and ends with the combination
        self.cats = []
        self.cats = ['cat'+str(i).zfill(2) for i in xrange(1,16)]
        self.cats += ['comb_2jet']
        self.cats += ['comb_01jet']
        self.cats += ['comb_01jet_tight']
        self.cats += ['comb_01jet_loose']
        self.cats += ['comb_tot']

        self.cat_names = [
            'VBF Tight (cat01)',
            '2-jet Tight (cat02)',
            '2-jet Loose (cat03)',
            '01-jet Tight BB (cat04)',
            '01-jet Tight BO (cat05)',
            '01-jet Tight BE (cat06)',
            '01-jet Tight OO (cat07)',
            '01-jet Tight OE (cat08)',
            '01-jet Tight EE (cat09)',
            '01-jet Loose BB (cat10)',
            '01-jet Loose BO (cat11)',
            '01-jet Loose BE (cat12)',
            '01-jet Loose OO (cat13)',
            '01-jet Loose OE (cat14)',
            '01-jet Loose EE (cat15)',
            '2-jet Comb.',
            '01-jet Comb.',
            '01-jet Tight Comb.',
            '01-jet Loose Comb.',
            'Total Combination',
        ]

        self.num_bins = len(self.cats)
        self.ymax = self.num_bins+0.5

        self.tfiles = {'comb_tot': TFile.Open(self.fname_head+'comb_tot'+self.fname_tail)}
        #self.tfiles = {'comb': TFile.Open(self.fname_head+'cat00'+self.fname_tail)}

        self.limits = {}
        for c in self.cats:
            self.tfiles[c] = TFile.Open(self.fname_head+c+self.fname_tail)
            #self.tfiles[c] = TFile.Open(self.fname_head+'cat00'+self.fname_tail)
            self.limits[c] = {}

        assert len(self.cat_names) == len(self.cats), 'Category list/size mismatch'



    ## ________________________________________________________________________
    def plot(self):

        # make sigma map
        for c in self.cats:
            lt = self.tfiles[c].Get('limit')
            lt.GetEntry(0)
            self.limits[c]['2s_down'] = lt.limit
            lt.GetEntry(1)
            self.limits[c]['1s_down'] = lt.limit
            lt.GetEntry(2)
            self.limits[c]['median']  = lt.limit
            lt.GetEntry(3)
            self.limits[c]['1s_up']   = lt.limit
            lt.GetEntry(4)
            self.limits[c]['2s_up']   = lt.limit
            if not self.blind:
                lt.GetEntry(5)
                self.limits[c]['obs']     = lt.limit
                self.limits[c]['obs_err'] = lt.limitErr
            else:
                self.limits[c]['obs']     = -1
                self.limits[c]['obs_err'] = -1




        # observed
        vals_array_x_obs_ = []
        vals_err_x_obs_   = []
        # median expected
        vals_array_x_ = []
        # y coord, essentially the inverted cat num
        vals_array_y_ = []
        # green
        vals_err_x_low_1s_  = []
        vals_err_x_high_1s_ = []
        # yellow
        vals_err_x_low_2s_  = []
        vals_err_x_high_2s_ = []

        # fill arrays which will be given to TGraph constr
        for i, c in enumerate(self.cats):
            med = self.limits[c]['median']
            vals_array_x_.insert(0, med)
            vals_array_y_ += [float(i+0.5)]
            vals_err_x_low_1s_.insert(0,  abs(self.limits[c]['1s_down'] - med))
            vals_err_x_high_1s_.insert(0, abs(self.limits[c]['1s_up']   - med))
            vals_err_x_low_2s_.insert(0,  abs(self.limits[c]['2s_down'] - med))
            vals_err_x_high_2s_.insert(0, abs(self.limits[c]['2s_up']   - med))
            vals_array_x_obs_.insert(0, self.limits[c]['obs'])
            vals_err_x_obs_.insert(0,   self.limits[c]['obs_err'])

        # dummies
        vals_err_y_     = [0.21] * len(self.cats)
        vals_err_y_obs_ = [0.] * len(self.cats)

        # turn them into arrays
        vals_array_x = np.asarray(vals_array_x_)
        vals_array_y = np.asarray(vals_array_y_)
        vals_err_y   = np.asarray(vals_err_y_)
        vals_err_y_obs     = np.asarray(vals_err_y_obs_)
        vals_err_x_low_2s  = np.asarray(vals_err_x_low_2s_)
        vals_err_x_high_2s = np.asarray(vals_err_x_high_2s_)
        vals_err_x_low_1s  = np.asarray(vals_err_x_low_1s_)
        vals_err_x_high_1s = np.asarray(vals_err_x_high_1s_)
        vals_array_x_obs   = np.asarray(vals_array_x_obs_)
        vals_err_x_obs     = np.asarray(vals_err_x_obs_)

        # make canvas
        canvname = 'catlims'
        canv = self.get_canvas(canvname, self.canvas_width, self.canvas_height)
        canv.SetLeftMargin(self.leftmargin)
        canv.cd()
        #canv.SetGridy()
        canv.SetGrid()

        # back layer - 2 sigma bands
        yellow = TGraphAsymmErrors(len(self.cats), vals_array_x, vals_array_y, 
            vals_err_x_low_2s, vals_err_x_high_2s, vals_err_y, vals_err_y)
        yellow.SetMarkerSize(2)
        yellow.SetMarkerStyle(20)
        yellow.SetFillColor(kOrange)
        yellow.SetLineColor(kOrange)
        yellow.SetFillStyle(1001)
        # front layer - 1 sigma bands and median
        green = TGraphAsymmErrors(len(self.cats), vals_array_x, vals_array_y,
            vals_err_x_low_1s, vals_err_x_high_1s, vals_err_y, vals_err_y)
        green.SetMarkerSize(2)
        green.SetMarkerStyle(5)
        green.SetFillColor(kGreen+1)
        green.SetLineColor(kGreen+1)
        green.SetFillStyle(1001)

        # observed
        money = TGraphAsymmErrors(len(self.cats), vals_array_x_obs, vals_array_y,
            vals_err_x_obs, vals_err_x_obs, vals_err_y_obs, vals_err_y_obs)
        money.SetMarkerSize(1)
        money.SetMarkerStyle(20)

        # dummy hist
        frame = TH2D('catlims', 'catlims', int(self.xmax), 0., self.xmax, 
            self.num_bins, 0, self.num_bins)
        frame.Draw()

        frame.GetXaxis().SetTitle('95% CL upper limit on '
            '#sigma/#sigma_{SM (H#rightarrow2#mu)}')
        frame.GetXaxis().SetTitleSize(.04)
        frame.GetXaxis().SetTitleOffset(1.1)
        frame.GetXaxis().CenterTitle(True)
        frame.GetXaxis().SetLabelOffset(0.001)
        frame.GetXaxis().SetRangeUser(0.,self.xmax)
        frame.GetYaxis().SetRangeUser(-0.5,self.ymax)
        frame.GetYaxis().SetNdivisions(self.num_bins)
        frame.GetXaxis().SetLabelSize(0.04)
        frame.GetYaxis().SetLabelSize(0.03)

        frame.GetYaxis().CenterLabels(True)

        for i, n in enumerate(reversed(self.cat_names)):
            frame.GetYaxis().SetBinLabel(i+1, n)

        yellow.Draw('2')
        green.Draw('2')
        green.Draw('PX')
        if not self.blind: money.Draw('P')


        green.GetXaxis().SetRangeUser(0., self.xmax)


        leg = TLegend(self.leg_x1, self.leg_y1, self.leg_x2, self.leg_y2)
        if not self.blind:
            leg.AddEntry(money, 'Observed', 'p')
        leg.AddEntry(green, 'Expected', 'p')
        leg.AddEntry(green, 'Expected #pm 1 std. deviation', 'F')
        leg.AddEntry(yellow, 'Expected #pm 2 std. deviation', 'F')
        leg.SetLineColor(kBlack)
        leg.SetBorderSize(1)
        #leg.Draw()

        canv.Update()
        if self.setlog:
            canv.SetLogx()

        CMS_lumi(canv, self.iPeriod, self.iPos, self.lumi, self.textra)
        canv.Update()
        savename = '{0}/catlims_xmax_{1}.png'.format(self.plotsdir, str(int(self.xmax)))
        canv.Print(savename)

        for c in self.cats:
            print 
            print ' -- Asymptotic --', c
            print 'Observed Limit: r <', self.limits[c]['obs'], '+/-', self.limits[c]['obs_err']
            print 'Expected  2.5%: r <', self.limits[c]['2s_down']
            print 'Expected 16.0%: r <', self.limits[c]['1s_down']
            print 'Expected 50.0%: r <', self.limits[c]['median']
            print 'Expected 84.0%: r <', self.limits[c]['1s_up']
            print 'Expected 97.5%: r <', self.limits[c]['2s_up']


## ___________________________________________________________
def main(argv=None):
    CatLimPlotter(argv).plot()

## ___________________________________________________________
# checks if this was run from the command line
if __name__ == '__main__':
    status = main()
#    sys.exit(status)



