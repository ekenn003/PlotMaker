from PlotBase import PlotBase
from tools.CMS_lumi import CMS_lumi
from datasets import *
#from variables_2mu import varnames
import ROOT
class SignificancePlotter(PlotBase):
    def __init__(self, args):
        super(SignificancePlotter, self).__init__(args)

        self.textra = '       Simulation'
        self.iPos = 0

        self.lumi = 1.
        self.version = '80X'
        self.era = 'final'

        self.extrainfo = self.era
        self.analysis = '2MuSig'

        self.plotsdir = ('/Users/ken/Work/PlotMaker/myplots'
            '/{0}/{1}'.format(self.era, self.analysis))


    def plot(self):
        d_sig_vbf = Dataset('VBF_HToMuMu', self.version, self.era, self.analysis)
#        d_sig_ggf = Dataset('GluGlu_HToMuMu', self.version, self.era, self.analysis)
#        d_sig_wm  = Dataset('WMinusH_HToMuMu', self.version, self.era, self.analysis)
#        d_sig_wp  = Dataset('WPlusH_HToMuMu', self.version, self.era, self.analysis)
#        d_sig_zh  = Dataset('ZH_HToMuMu', self.version, self.era, self.analysis)

        d_bkg_dy   = Dataset('DYJetsToLL', self.version, self.era, self.analysis)
        d_bkg_tt   = Dataset('TTJets', self.version, self.era, self.analysis)
#        d_bkg_zz_a = Dataset('ZZTo2L2Nu', self.version, self.era, self.analysis)
#        d_bkg_zz_b = Dataset('ZZTo2L2Q', self.version, self.era, self.analysis)
#        d_bkg_zz_c = Dataset('ZZTo4L', self.version, self.era, self.analysis)
#        d_bkg_wz_a = Dataset('WZTo2L2Q', self.version, self.era, self.analysis)
#        d_bkg_wz_b = Dataset('WZTo3LNu', self.version, self.era, self.analysis)
#        d_bkg_ww   = Dataset('WWTo2L2Nu', self.version, self.era, self.analysis)


        canv = self.get_canvas('vbf_cuts_sig', 1200, 900)
        canv.SetRightMargin(0.1)
        canv.SetLeftMargin(0.14)
        canv.cd()


        vbf_cuts = ROOT.TH2D('vbf_cuts_sig', 'vbf_cuts_sig', 50, 200., 700., 6, 1.5, 4.5)
        n=0
        for i in xrange(200,701,10):
            n+=1

            # eta = 1p5: ybin=1
            tot_sig_1p5 = self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta1p5', d_sig_vbf, 1.)
            S_1p5 = float(tot_sig_1p5.Integral())
            print 'S_1p5 =', S_1p5
            tot_bkg_1p5_list = ROOT.TList()
            tot_bkg_1p5_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta1p5', d_bkg_dy, 1.))
            tot_bkg_1p5_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta1p5', d_bkg_tt, 1.))
#            tot_bkg_1p5_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta1p5', d_bkg_zz_a, 1.))
#            tot_bkg_1p5_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta1p5', d_bkg_zz_b, 1.))
#            tot_bkg_1p5_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta1p5', d_bkg_zz_c, 1.))
#            tot_bkg_1p5_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta1p5', d_bkg_wz_a, 1.))
#            tot_bkg_1p5_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta1p5', d_bkg_wz_b, 1.))
#            tot_bkg_1p5_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta1p5', d_bkg_ww, 1.))
            tot_bkg_1p5 = ROOT.TH2D(tot_bkg_1p5_list.At(0).Clone())
            tot_bkg_1p5.Reset()
            tot_bkg_1p5.Merge(tot_bkg_1p5_list)
            B_1p5 = float(tot_bkg_1p5.Integral())
            print 'B_1p5 =', B_1p5
            bincontent_1p5 = (S_1p5 * S_1p5) / (S_1p5 + B_1p5)
            vbf_cuts.SetBinContent(n, 1, bincontent_1p5)
            print 'bincontent_1p5 = ', bincontent_1p5

            # eta = 2p0: ybin=2
            tot_sig_2p0 = self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta2p0', d_sig_vbf, 1.)
            S_2p0 = float(tot_sig_2p0.Integral())
            print 'S_2p0 =', S_2p0
            tot_bkg_2p0_list = ROOT.TList()
            tot_bkg_2p0_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta2p0', d_bkg_dy, 1.))
            tot_bkg_2p0_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta2p0', d_bkg_tt, 1.))
#            tot_bkg_2p0_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta2p0', d_bkg_zz_a, 1.))
#            tot_bkg_2p0_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta2p0', d_bkg_zz_b, 1.))
#            tot_bkg_2p0_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta2p0', d_bkg_zz_c, 1.))
#            tot_bkg_2p0_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta2p0', d_bkg_wz_a, 1.))
#            tot_bkg_2p0_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta2p0', d_bkg_wz_b, 1.))
#            tot_bkg_2p0_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta2p0', d_bkg_ww, 1.))
            tot_bkg_2p0 = ROOT.TH2D(tot_bkg_2p0_list.At(0).Clone())
            tot_bkg_2p0.Reset()
            tot_bkg_2p0.Merge(tot_bkg_2p0_list)
            B_2p0 = float(tot_bkg_2p0.Integral())
            print 'B_2p0 =', B_2p0
            bincontent_2p0 = (S_2p0 * S_2p0) / (S_2p0 + B_2p0)
            vbf_cuts.SetBinContent(n, 2, bincontent_2p0)
            print 'bincontent_2p0 = ', bincontent_2p0

            # eta = 2p5: ybin=3
            tot_sig_2p5 = self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta2p5', d_sig_vbf, 1.)
            S_2p5 = float(tot_sig_2p5.Integral())
            print 'S_2p5 =', S_2p5
            tot_bkg_2p5_list = ROOT.TList()
            tot_bkg_2p5_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta2p5', d_bkg_dy, 1.))
            tot_bkg_2p5_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta2p5', d_bkg_tt, 1.))
#            tot_bkg_2p5_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta2p5', d_bkg_zz_a, 1.))
#            tot_bkg_2p5_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta2p5', d_bkg_zz_b, 1.))
#            tot_bkg_2p5_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta2p5', d_bkg_zz_c, 1.))
#            tot_bkg_2p5_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta2p5', d_bkg_wz_a, 1.))
#            tot_bkg_2p5_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta2p5', d_bkg_wz_b, 1.))
#            tot_bkg_2p5_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta2p5', d_bkg_ww, 1.))
            tot_bkg_2p5 = ROOT.TH2D(tot_bkg_2p5_list.At(0).Clone())
            tot_bkg_2p5.Reset()
            tot_bkg_2p5.Merge(tot_bkg_2p5_list)
            B_2p5 = float(tot_bkg_2p5.Integral())
            print 'B_2p5 =', B_2p5
            bincontent_2p5 = (S_2p5 * S_2p5) / (S_2p5 + B_2p5)
            vbf_cuts.SetBinContent(n, 3, bincontent_2p5)
            print 'bincontent_2p5 = ', bincontent_2p5


            # eta = 3p0: ybin=4
            tot_sig_3p0 = self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta3p0', d_sig_vbf, 1.)
            S_3p0 = float(tot_sig_3p0.Integral())
            print 'S_3p0 =', S_3p0
            tot_bkg_3p0_list = ROOT.TList()
            tot_bkg_3p0_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta3p0', d_bkg_dy, 1.))
            tot_bkg_3p0_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta3p0', d_bkg_tt, 1.))
#            tot_bkg_3p0_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta3p0', d_bkg_zz_a, 1.))
#            tot_bkg_3p0_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta3p0', d_bkg_zz_b, 1.))
#            tot_bkg_3p0_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta3p0', d_bkg_zz_c, 1.))
#            tot_bkg_3p0_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta3p0', d_bkg_wz_a, 1.))
#            tot_bkg_3p0_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta3p0', d_bkg_wz_b, 1.))
#            tot_bkg_3p0_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta3p0', d_bkg_ww, 1.))
            tot_bkg_3p0 = ROOT.TH2D(tot_bkg_3p0_list.At(0).Clone())
            tot_bkg_3p0.Reset()
            tot_bkg_3p0.Merge(tot_bkg_3p0_list)
            B_3p0 = float(tot_bkg_3p0.Integral())
            print 'B_3p0 =', B_3p0
            bincontent_3p0 = (S_3p0 * S_3p0) / (S_3p0 + B_3p0)
            vbf_cuts.SetBinContent(n, 4, bincontent_3p0)
            print 'bincontent_3p0 = ', bincontent_3p0


            # eta = 3p5: ybin=5
            tot_sig_3p5 = self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta3p5', d_sig_vbf, 1.)
            S_3p5 = float(tot_sig_3p5.Integral())
            print 'S_3p5 =', S_3p5
            tot_bkg_3p5_list = ROOT.TList()
            tot_bkg_3p5_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta3p5', d_bkg_dy, 1.))
            tot_bkg_3p5_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta3p5', d_bkg_tt, 1.))
#            tot_bkg_3p5_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta3p5', d_bkg_zz_a, 1.))
#            tot_bkg_3p5_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta3p5', d_bkg_zz_b, 1.))
#            tot_bkg_3p5_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta3p5', d_bkg_zz_c, 1.))
#            tot_bkg_3p5_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta3p5', d_bkg_wz_a, 1.))
#            tot_bkg_3p5_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta3p5', d_bkg_wz_b, 1.))
#            tot_bkg_3p5_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta3p5', d_bkg_ww, 1.))
            tot_bkg_3p5 = ROOT.TH2D(tot_bkg_3p5_list.At(0).Clone())
            tot_bkg_3p5.Reset()
            tot_bkg_3p5.Merge(tot_bkg_3p5_list)
            B_3p5 = float(tot_bkg_3p5.Integral())
            print 'B_3p5 =', B_3p5
            bincontent_3p5 = (S_3p5 * S_3p5) / (S_3p5 + B_3p5)
            vbf_cuts.SetBinContent(n, 5, bincontent_3p5)
            print 'bincontent_3p5 = ', bincontent_3p5


            # eta = 4p0: ybin=6
            tot_sig_4p0 = self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta4p0', d_sig_vbf, 1.)
            S_4p0 = float(tot_sig_4p0.Integral())
            print 'S_4p0 =', S_4p0
            tot_bkg_4p0_list = ROOT.TList()
            tot_bkg_4p0_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta4p0', d_bkg_dy, 1.))
            tot_bkg_4p0_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta4p0', d_bkg_tt, 1.))
#            tot_bkg_4p0_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta4p0', d_bkg_zz_a, 1.))
#            tot_bkg_4p0_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta4p0', d_bkg_zz_b, 1.))
#            tot_bkg_4p0_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta4p0', d_bkg_zz_c, 1.))
#            tot_bkg_4p0_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta4p0', d_bkg_wz_a, 1.))
#            tot_bkg_4p0_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta4p0', d_bkg_wz_b, 1.))
#            tot_bkg_4p0_list.Add(self.get_weighted_hist('scan/hDiMuInvMass_dijetmassAbove'+str(i)+'_deta4p0', d_bkg_ww, 1.))
            tot_bkg_4p0 = ROOT.TH2D(tot_bkg_4p0_list.At(0).Clone())
            tot_bkg_4p0.Reset()
            tot_bkg_4p0.Merge(tot_bkg_4p0_list)
            B_4p0 = float(tot_bkg_4p0.Integral())
            print 'B_4p0 =', B_4p0
            bincontent_4p0 = (S_4p0 * S_4p0) / (S_4p0 + B_4p0)
            vbf_cuts.SetBinContent(n, 6, bincontent_4p0)
            print 'bincontent_4p0 = ', bincontent_4p0




        canv.cd()
        vbf_cuts.Draw('colz')
        vbf_cuts.GetZaxis().SetLabelSize(0.02)
        vbf_cuts.GetXaxis().SetTitle('min cut on M_{jj}')
        vbf_cuts.GetXaxis().SetLabelSize(0.04)
        vbf_cuts.GetXaxis().SetTitleSize(0.05)
        vbf_cuts.GetXaxis().SetTitleOffset(1.0)
        vbf_cuts.GetYaxis().SetTitle('min cut on #Delta#eta(jj)')
        vbf_cuts.GetYaxis().SetLabelSize(0.04)
        vbf_cuts.GetYaxis().SetTitleSize(0.05)
        vbf_cuts.GetYaxis().SetTitleOffset(1.0)
        CMS_lumi(canv, self.iPeriod, self.iPos, 1., self.textra);
        canv.Update()

        # save canvas
        savename = '{0}/{1}_{2}'.format(self.plotsdir, 'significance', self.extrainfo)
        canv.Print('{0}.png'.format(savename))
        #canv.Clear()




## ___________________________________________________________
def main(argv=None):
    SignificancePlotter(argv).plot()

## ___________________________________________________________
# checks if this was run from the command line
if __name__ == '__main__':
    status = main()
#    sys.exit(status)



