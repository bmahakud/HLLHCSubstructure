# HLLHCSubstructure
all instructions here

`
cmsrel CMSSW_9_3_2

cd src

cmsenv
git clone https://github.com/bmahakud/HLLHCSubstructure
git clone https://github.com/bmahakud/JetToolbox JMEAnalysis/JetToolbox
scram b -j 9
cd HLLHCSubstructure/TreeMaker/test/
cmsRun runMakeTreeTest932_cfg.py inputFilesConfig=GENSIM.RSGluonToTT_M-3000_TuneCUETP8M1_14TeV-pythia8GENSIMRECO_PU200 nstart=0 nfiles=1
`

