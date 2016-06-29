import ROOT
def main():
    ROOT.gROOT.SetBatch(ROOT.kTRUE)


    filelist = {
        'SingleMuC' : ROOT.TFile('data/june16/withSF/ana_template_SingleMuon2015C.root'),
        'SingleMuD' : ROOT.TFile('data/june16/withSF/ana_template_SingleMuon2015D.root'),
        'DYJets'    : ROOT.TFile('data/june16/withSF/ana_template_DYJetsToLL.root'),
    }

    plotsdir = 'myplots/june16_SF_compare'

    varlist = {
        'Pt' : {
            'xMin' : 0.,
            'xMax' : 100,
        },
        'Eta' : {
            'xMin' : -2.5,
            'xMax' : 2.5,
        },
        'Phi' : {
            'xMin' : -3.5,
            'xMax' : 3.5,
        },
        'Energy' : {
            'xMin' : 0.,
            'xMax' : 200.,
        },
        'Mass' : {
            'xMin' : 0.,
            'xMax' : 10.,
        },
    }

    for var in varlist:
        var1 = 'hMu' + var
        var2 = 'hCorrMu' + var
        for sample in filelist:
            hist1 = filelist[sample].Get(var1).Clone()
            hist2 = filelist[sample].Get(var2).Clone()
            canvname = '{0}_{1}'.format(var, sample)
            canv = ROOT.TCanvas(canvname, canvname, 800, 600)
            canv.cd()
            hist1.SetLineColor(ROOT.kBlack)
            hist1.SetLineStyle(7)
            hist1.SetLineWidth(2)
            hist2.SetLineColor(ROOT.kRed)
            hist2.SetLineStyle(2)
            hist2.SetLineWidth(2)
            hist1.Draw('hist')
            hist2.Draw('hist same')

            hist1.GetXaxis().SetRangeUser(varlist[var]['xMin'], varlist[var]['xMax'])
            hist2.GetXaxis().SetRangeUser(varlist[var]['xMin'], varlist[var]['xMax'])

            canv.cd()
            leg = ROOT.TLegend()
            leg.SetHeader(sample)
            leg.AddEntry(hist1, 'uncorrected', 'F2')
            leg.AddEntry(hist2, 'corrected', 'F2')
            leg.Draw()

            hist1.SetTitle('Mu '+var+': '+sample)
            hist2.SetTitle('Mu '+var+': '+sample)
            canv.Update()
            canv.Print('{0}/{1}.png'.format(plotsdir, canvname))
            hist1.Delete()
            hist2.Delete()
            leg.Delete()

        canv.Clear()
        

## ___________________________________________________________
# checks if this was run from the command line
if __name__ == '__main__':
    status = main()
