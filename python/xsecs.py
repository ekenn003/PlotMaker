xsecs = {
    'DoubleMuon'                                                       : 1.,
    'SingleMuon'                                                       : 1.,

    'DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8'       :   7160        * PB * 1.216,
    'DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8'      :  18610.       * PB, # already NNLO
    'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8'          :   6025.2      * PB,
    'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8'           :   4895        * PB * 1.216, # 1.216 LO -> NNLO

    'TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8'             :     57.35     * PB,
    'TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8'    :    114.5      * PB,
    'TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8' :    114.6      * PB,
    'TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8'                    :    502.2      * PB,

    'TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8'          :      3.697    * PB,
    'ttZJets_13TeV_madgraphMLM'                                        :      0.259    * PB,
    'ttWJets_13TeV_madgraphMLM'                                        :      0.243    * PB,
    'ttH_M125_13TeV_powheg_pythia8'                                    :      0.5085   * PB,

    'tZq_ll_4f_13TeV-amcatnlo-pythia8_TuneCUETP8M1'                    :      0.0758   * PB,

    'WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8'               :  61526.7      * PB,
    'WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8'                :  61526.7      * PB,

    'ZGTo2LG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8'                  :    117.864    * PB,    
    'WGToLNuG_TuneCUETP8M1_13TeV-madgraphMLM-pythia8'                  :    405.271    * PB,

    'ZH_HToBB_ZToLL_M125_13TeV_amcatnloFXFX_madspin_pythia8'           :      0.8696 * 0.5824 * (0.033658*3) * PB, # ZH * H->bb * Z->ll
    'ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8'         :      0.8696 * 0.5824 * 0.2          * PB, # ZH * H->bb * Z->inv
    'ZH_HToBB_ZToQQ_M125_13TeV_powheg_pythia8'                         :      0.8696 * 0.5824 * 0.6991       * PB, # ZH * H->bb * Z->had
    'ZH_HToGG_ZToAll_M125_13TeV_powheg_pythia8'                        :      0.8696 * 0.00227               * PB, # ZH * H->gamgam
    'ZH_HToZG_ZToAll_M-125_13TeV_powheg_pythia8'                       :      0.8696 * 0.001533              * PB, # ZH * H->Zgam
    'ZHToTauTau_M125_13TeV_powheg_pythia8'                             :      0.8696 * 0.006272              * PB, # ZH * H->tautau
    'ZH_HToZZ_4LFilter_M125_13TeV_powheg2-minlo-HZJ_JHUgenV6_pythia8'  :      0.147 * PB, # MCM , 0.8696 * 0.02619 * (0.033658*3)**2 # ZH * H->ZZ * Z->ll^2 
    'ZH_HToBB_ZToLL_M125_13TeV_powheg_herwigpp'                        :      0.07495  * PB,

    'WWTo2L2Nu_13TeV-powheg'                                           :     10.481    * PB,
    'WWToLNuQQ_13TeV-powheg'                                           :     43.53     * PB,
    'GluGluWWTo2L2Nu_MCFM_13TeV'                                       :      0.39     * PB,

    'WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8'                   :     10.71     * PB,
    'WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8'                     :      3.05     * PB,
    'WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8'                      :      5.60     * PB,
    'WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8'                       :      4.42965  * PB,

    'ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8'                      :      3.28     * PB,
    'ZZTo2L2Nu_13TeV_powheg_pythia8'                                   :      0.564    * PB,
    'ZZTo4L_13TeV_powheg_pythia8'                                      :      1.256    * PB * 1.1,

    'GluGluToZZTo2e2mu_BackgroundOnly_13TeV_MCFM'                      :      0.003194 * PB * 1.7,
    'GluGluToZZTo2e2tau_BackgroundOnly_13TeV_MCFM'                     :      0.003194 * PB * 1.7,
    'GluGluToZZTo2mu2tau_BackgroundOnly_13TeV_MCFM'                    :      0.003194 * PB * 1.7,
    'GluGluToZZTo4e_BackgroundOnly_13TeV_MCFM'                         :      0.001586 * PB * 1.7,
    'GluGluToZZTo4mu_BackgroundOnly_13TeV_MCFM'                        :      0.001586 * PB * 1.7,
    'GluGluToZZTo4tau_BackgroundOnly_13TeV_MCFM'                       :      0.001586 * PB * 1.7,
    'GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8'                  :      0.003194 * PB * 1.7,
    'GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8'                 :      0.003194 * PB * 1.7,
    'GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8'                :      0.003194 * PB * 1.7,
    'GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8'                     :      0.001586 * PB * 1.7,
    'GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8'                    :      0.001586 * PB * 1.7,
    'GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8'                   :      0.001586 * PB * 1.7,


    'WWW_TuneCUETP8M1_13TeV-amcatnlo-pythia8'                          :      0.1651   * PB,
    'WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8'                       :      0.2086   * PB,
    'WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8'                          :      0.1651   * PB,
    'WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8'                          :      0.05565  * PB,
    'ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8'                          :      0.01398  * PB,
    'WWG_TuneCUETP8M1_13TeV-amcatnlo-pythia8'                          :      0.2147   * PB,
    'WZG_TuneCUETP8M1_13TeV-amcatnlo-pythia8'                          :      0.04123  * PB,
}
