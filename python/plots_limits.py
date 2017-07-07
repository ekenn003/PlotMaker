from PlotBase import PlotBase
from tools.CMS_lumi import CMS_lumi
#from array import array
import numpy as np
from ROOT import TCanvas, TPad, TFile, TGraphAsymmErrors
from ROOT import TMarker, TBox, TGaxis
from ROOT import kYellow, kGreen
class CatLimPlotter(PlotBase):
    def __init__(self, args):
        super(CatLimPlotter, self).__init__(args)

        self.legend_width  = 0.16
        self.legend_height = 0.35
        self.canvas_width  = 600
        self.canvas_height = 1200

        self.lumi = 36460.
        self.textra = 'Simulation'

        self.plotsdir = '/Users/ken/Work/PlotMaker/myplots/catlims'

        self.fname_head = '/Users/ken/Work/PlotMaker/data/combine/higgsCombine_'
        self.fname_tail = '.Asymptotic.mH125.root'


        self.sp = ['VBF', 'GluGlu', 'WMinus', 'WPlusH', 'ZH']

        # this list is ordered and ends with the combination
        self.cats = ['cat'+str(i).zfill(2) for i in xrange(1,16)]
        self.cats += ['comb']

        #self.tfiles = {'comb': TFile.Open(self.fname_head+'comb'+self.fname_tail)}
        self.tfiles = {'comb': TFile.Open(self.fname_head+'cat00'+self.fname_tail)}

        self.limits = {}
        for c in self.cats:
            #self.tfiles[c] = TFile.Open(self.fname_head+c+self.fname_tail)
            self.tfiles[c] = TFile.Open(self.fname_head+'cat00'+self.fname_tail)
            self.limits[c] = {}

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
            lt.GetEntry(5)
            self.limits[c]['obs']     = lt.limit
            self.limits[c]['obs_err'] = lt.limitErr


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
            vals_array_x_.insert(0, self.limits[c]['median'])
            vals_array_y_ += [i+1]
            vals_err_x_low_1s_.insert(0, self.limits[c]['1s_down'])
            vals_err_x_high_1s_.insert(0, self.limits[c]['1s_up'])
            vals_err_x_low_2s_.insert(0, self.limits[c]['2s_down'])
            vals_err_x_high_2s_.insert(0, self.limits[c]['2s_up'])
        # dummy
        vals_err_y_  = [0.] * len(self.cats)

        # turn them into arrays
        #vals_array_x = array('f', vals_array_x_)
        #vals_array_y = array('f', vals_array_y_)
        #vals_err_y   = array('f', vals_err_y_)
        #vals_err_x_low_2s  = array('f', vals_err_x_low_2s_)
        #vals_err_x_high_2s = array('f', vals_err_x_high_2s_)
        #vals_err_x_low_1s  = array('f', vals_err_x_low_1s_)
        #vals_err_x_high_1s = array('f', vals_err_x_high_1s_)


        # turn them into arrays
        vals_array_x = np.asarray(vals_array_x_)
        vals_array_y = np.asarray(vals_array_y_)
        vals_err_y   = np.asarray(vals_err_y_)
        vals_err_x_low_2s  = np.asarray(vals_err_x_low_2s_)
        vals_err_x_high_2s = np.asarray(vals_err_x_high_2s_)
        vals_err_x_low_1s  = np.asarray(vals_err_x_low_1s_)
        vals_err_x_high_1s = np.asarray(vals_err_x_high_1s_)
        

        # make canvas
        canvname = 'catlims'
        canv = self.get_canvas(canvname, self.canvas_width, self.canvas_height)
        canv.cd()

        # back layer - 2 sigma bands
        yellow = TGraphAsymmErrors(vals_array_x, vals_array_y, vals_err_x_low_2s, vals_err_x_high_2s, vals_err_y, vals_err_y)
        yellow.SetMarkerSize(0)
        yellow.SetMarkerStyle(20)
        # front layer - 1 sigma bands and median
        green  = TGraphAsymmErrors(vals_array_x, vals_array_y, vals_err_x_low_1s, vals_err_x_high_1s, vals_err_y, vals_err_y)
        green.SetMarkerSize(1)
        green.SetMarkerStyle(5)


        green.SetTitle('')


        yellow.Draw()
        green.Draw('ALP')
        ##            xd   yd    xup   yup   wd   wup   ndiv
        #xax = TGaxis(0.1, 0.75, 0.95, 0.75, 0, 10, 10, 'I+', 5000)

        #xax.SetTitle('95% CL on #sigma/#sigma_{SM (H#rightarrow2#mu)}')
        #xax.CenterTitle(True)
        #xax.SetTitleSize(0.3)
        ##xax.SetTitleOffset(1.)
        #xax.SetLabelSize(0.3)
        #xax.SetTextFont(42)
        #xax.SetTickLength(0.4)
        #xax.SetTickSize(0.4)
        ##xax.SetLabelOffset(0.025)
        #xax.Draw()



















        CMS_lumi(canv, self.iPeriod, self.iPos, self.lumi, self.textra)
        canv.Update()
        savename = '{0}/test.png'.format(self.plotsdir)
        canv.Print(savename)



## ___________________________________________________________
def main(argv=None):
    CatLimPlotter(argv).plot()

## ___________________________________________________________
# checks if this was run from the command line
if __name__ == '__main__':
    status = main()
#    sys.exit(status)



