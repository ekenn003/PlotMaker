# PlotMaker

Each era of plots gets its own class, derived from PlotBase. This runs on
histogram files produced with RootMaker+AnalysisToolLight. The histogram files are 
assumed to contain:
* `tSumWts` in the Summary tree
* `tNumEvts` in the Summary tree
* `tCrossSec` in the Summary tree

