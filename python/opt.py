from PlotBase import PlotBase
from tools.CMS_lumi import CMS_lumi
from datasets import *
import ROOT
class SignificancePlotter(PlotBase):
    def __init__(self, args):
        super(SignificancePlotter, self).__init__(args)

        self.textra = '       Simulation'
        self.iPos = 0

        self.lumi = 35920. # pb
        self.version = '80X'
        self.era = 'final'

        self.sigf = 50

        self.legend_width  = 0.16
        self.legend_height = 0.35

        self.draw_sigs = True
        self.draw_big_legend = False
        self.draw_tiny_legend = True

        self.analysis = 'test'


        self.extrainfo = self.era
        self.plotsdir = ('/Users/ken/Work/PlotMaker/myplots'
            '/{0}/{1}'.format(self.era, self.analysis))

    def get_poisson_significance(self, sig, bkg):
        s, se = abs(sig[0]), abs(sig[1])
        b, be = abs(bkg[0]), abs(bkg[1])
        return (s * s)/(b+be**2) if b or be else 0.


    def plot(self):

        d_sig_vbf = Dataset('VBF_HToMuMu', self.version, self.era, self.analysis)
        d_sig_ggf = Dataset('GluGlu_HToMuMu', self.version, self.era, self.analysis)
        d_sig_wm  = Dataset('WMinusH_HToMuMu', self.version, self.era, self.analysis)
        d_sig_wp  = Dataset('WPlusH_HToMuMu', self.version, self.era, self.analysis)
        d_sig_zh  = Dataset('ZH_HToMuMu', self.version, self.era, self.analysis)

        d_bkg_dy   = Dataset('DYJetsToLL', self.version, self.era, self.analysis)
        d_bkg_tt   = Dataset('TTJets', self.version, self.era, self.analysis)
        d_bkg_zz_a = Dataset('ZZTo2L2Nu', self.version, self.era, self.analysis)
        d_bkg_zz_b = Dataset('ZZTo2L2Q', self.version, self.era, self.analysis)
        d_bkg_zz_c = Dataset('ZZTo4L', self.version, self.era, self.analysis)
        d_bkg_wz_a = Dataset('WZTo2L2Q', self.version, self.era, self.analysis)
        d_bkg_wz_b = Dataset('WZTo3LNu', self.version, self.era, self.analysis)
        d_bkg_ww   = Dataset('WWTo2L2Nu', self.version, self.era, self.analysis)


        metcutlist = [str(i) for i in xrange(20, 91, 10)]
        etacutlist = ['1p5', '2p0', '2p5', '3p0', '3p5', '4p0', '4p5', '5p0']




        for met in metcutlist:
            hname = 'hNumJets_'+met
            print hname
            #newbinsize = 10. # GeV

            canv = self.get_canvas(hname, 1200, 900)
            canv.SetRightMargin(0.05)
            canv.SetLeftMargin(0.14)
            canv.cd()

            stack = ROOT.THStack()
            
            bkg_dy_hist = self.get_weighted_hist('opt/'+hname, d_bkg_dy, self.lumi)
            bkg_tt_hist = self.get_weighted_hist('opt/'+hname, d_bkg_tt, self.lumi)
            bkg_vv_list = ROOT.TList()
            bkg_vv_list.Add(self.get_weighted_hist('opt/'+hname, d_bkg_zz_a, self.lumi, newhgroup='VV'))
            bkg_vv_list.Add(self.get_weighted_hist('opt/'+hname, d_bkg_zz_b, self.lumi, newhgroup='VV'))
            bkg_vv_list.Add(self.get_weighted_hist('opt/'+hname, d_bkg_zz_c, self.lumi, newhgroup='VV'))
            bkg_vv_list.Add(self.get_weighted_hist('opt/'+hname, d_bkg_wz_a, self.lumi, newhgroup='VV'))
            bkg_vv_list.Add(self.get_weighted_hist('opt/'+hname, d_bkg_wz_b, self.lumi, newhgroup='VV'))
            bkg_vv_list.Add(self.get_weighted_hist('opt/'+hname, d_bkg_ww, self.lumi, newhgroup='VV'))
            bkg_vv_hist = bkg_vv_list.At(0).Clone('VV')
            bkg_vv_hist.Reset()
            bkg_vv_hist.Merge(bkg_vv_list)

            stack.Add(bkg_vv_hist)
            stack.Add(bkg_tt_hist)
            stack.Add(bkg_dy_hist)

            stack.Draw('hist')
    
            stack.GetXaxis().SetTitle('num jets')
            stack.GetXaxis().SetRangeUser(0, 8)
            ymax_factor = 1.2
            stack.SetMaximum(stack.GetHistogram().GetMaximum()*ymax_factor)
            stack.GetYaxis().SetTitle('Events')
            stack.GetXaxis().SetLabelFont(42)
            stack.GetXaxis().SetLabelOffset(0.01)
            stack.GetXaxis().SetTitleOffset(0.85)
            #stack.GetYaxis().SetTitleOffset(0.85)
            #stack.GetXaxis().SetTitleSize(1.)

            sig_vbf_hist = self.get_weighted_hist('opt/'+hname, d_sig_vbf, self.lumi)
            sig_ggf_hist = self.get_weighted_hist('opt/'+hname, d_sig_ggf, self.lumi)
            sig_vh_list = ROOT.TList()
            sig_vh_list.Add(self.get_weighted_hist('opt/'+hname, d_sig_wm, self.lumi))
            sig_vh_list.Add(self.get_weighted_hist('opt/'+hname, d_sig_wp, self.lumi))
            sig_vh_list.Add(self.get_weighted_hist('opt/'+hname, d_sig_zh, self.lumi))
            sig_vh_hist = sig_vh_list.At(0).Clone()
            sig_vh_hist.Reset()
            sig_vh_list.Merge(sig_vh_list)

            sig_vbf_hist.Draw('hist same')
            sig_ggf_hist.Draw('hist same')
            sig_vh_hist.Draw('hist same')

            signal_hists = []
            signal_hists += [sig_vbf_hist]
            signal_hists += [sig_ggf_hist]
            signal_hists += [sig_vh_hist]

            CMS_lumi(canv, self.iPeriod, self.iPos, 0, self.textra)
            canv.Update()
            savename = '{0}/{1}_{2}'.format(self.plotsdir, hname, self.extrainfo)
            legXlow_, legYlow_, legXhigh_, legYhigh_ = self.get_legend_coordinates(3, self.legend_width, self.legend_height)
            leg = ROOT.TLegend(legXlow_, legYlow_, legXhigh_, legYhigh_)
            leg.AddEntry(sig_vbf_hist, 'VBF signal x'+str(self.sigf), 'l')
            leg.AddEntry(sig_ggf_hist, 'ggF signal x'+str(self.sigf), 'l')
            leg.AddEntry(sig_vh_hist, 'VBF signal x'+str(self.sigf), 'l')
            leg.AddEntry(bkg_dy_hist, 'Drell-Yan', 'F2')
            leg.AddEntry(bkg_tt_hist, 'TTbar', 'F2')
            leg.AddEntry(bkg_vv_hist, 'VV', 'F2')
            leg.SetFillColor(0)
            leg.SetBorderSize(1)
            leg.SetLineColor(ROOT.kWhite)
            leg.SetHeader('MET < '+met+' GeV')

            leg.Draw()
            canv.Print('{0}.png'.format(savename))
            leg.Delete()



        for eta in etacutlist:
            hname = 'hhDiJetInvMass_'+eta
            print hname


        for met in metcutlist:
            for eta in etacutlist: 
                hname = 'hDiMuInvMass_eta'+eta+'_met'+met
                print hname








## ___________________________________________________________
def main(argv=None):
    SignificancePlotter(argv).plot()

## ___________________________________________________________
# checks if this was run from the command line
if __name__ == '__main__':
    status = main()
#    sys.exit(status)



