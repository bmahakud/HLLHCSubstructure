import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/PhaseIITDRFall17DR/VBFToHHTo4B_SM_14TeV-madgraph-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/0215E56C-E5B8-E711-BCB5-FA163E40A8F5.root',
'/store/mc/PhaseIITDRFall17DR/VBFToHHTo4B_SM_14TeV-madgraph-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/0A02B793-ACB8-E711-BD0E-FA163EECA31F.root',
'/store/mc/PhaseIITDRFall17DR/VBFToHHTo4B_SM_14TeV-madgraph-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/10A579AC-91B8-E711-A30E-FA163E7724E1.root',
'/store/mc/PhaseIITDRFall17DR/VBFToHHTo4B_SM_14TeV-madgraph-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/28BD4ED4-F0B8-E711-AE8C-FA163E72D76A.root',
'/store/mc/PhaseIITDRFall17DR/VBFToHHTo4B_SM_14TeV-madgraph-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/2A648BD0-F0B8-E711-9E5E-FA163E7EAE9E.root',
'/store/mc/PhaseIITDRFall17DR/VBFToHHTo4B_SM_14TeV-madgraph-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/30CFA8BF-D4BB-E711-97A1-44A8422411EB.root',
'/store/mc/PhaseIITDRFall17DR/VBFToHHTo4B_SM_14TeV-madgraph-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/34AAC5FE-3CB9-E711-9637-FA163E07303A.root',
'/store/mc/PhaseIITDRFall17DR/VBFToHHTo4B_SM_14TeV-madgraph-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/40B3A64B-09B9-E711-889D-FA163E5B1C53.root',
'/store/mc/PhaseIITDRFall17DR/VBFToHHTo4B_SM_14TeV-madgraph-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/544BD3B8-08BA-E711-8FD5-001E67D5D89A.root',
'/store/mc/PhaseIITDRFall17DR/VBFToHHTo4B_SM_14TeV-madgraph-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/60F96A40-E5B8-E711-BED7-FA163E081C75.root',
'/store/mc/PhaseIITDRFall17DR/VBFToHHTo4B_SM_14TeV-madgraph-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/66703DB4-D0B9-E711-85A0-02163E01C549.root',
'/store/mc/PhaseIITDRFall17DR/VBFToHHTo4B_SM_14TeV-madgraph-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/7C00191E-E1B8-E711-818E-002590A88812.root',
'/store/mc/PhaseIITDRFall17DR/VBFToHHTo4B_SM_14TeV-madgraph-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/84773AF1-9FB8-E711-969B-02163E01A8FC.root',
'/store/mc/PhaseIITDRFall17DR/VBFToHHTo4B_SM_14TeV-madgraph-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/94A6F2CE-57B8-E711-A41C-FA163EF8655C.root',
'/store/mc/PhaseIITDRFall17DR/VBFToHHTo4B_SM_14TeV-madgraph-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/94BE2E87-2ABB-E711-9D63-44A842CFC9D9.root',
'/store/mc/PhaseIITDRFall17DR/VBFToHHTo4B_SM_14TeV-madgraph-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/960C8BD1-49B9-E711-B59E-FA163E5A38C2.root',
'/store/mc/PhaseIITDRFall17DR/VBFToHHTo4B_SM_14TeV-madgraph-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/A2412949-51BA-E711-AA9C-FA163EF607E3.root',
'/store/mc/PhaseIITDRFall17DR/VBFToHHTo4B_SM_14TeV-madgraph-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/A46F1746-D3B8-E711-9708-FA163E9BFA0C.root',
'/store/mc/PhaseIITDRFall17DR/VBFToHHTo4B_SM_14TeV-madgraph-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/AA1AA797-30BA-E711-A3CB-A4BF0112E0A0.root',
'/store/mc/PhaseIITDRFall17DR/VBFToHHTo4B_SM_14TeV-madgraph-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/B07634E3-DDB8-E711-8DF7-44A84225C911.root',
'/store/mc/PhaseIITDRFall17DR/VBFToHHTo4B_SM_14TeV-madgraph-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/B20D1878-D0B9-E711-8E74-FA163E9A2713.root',
'/store/mc/PhaseIITDRFall17DR/VBFToHHTo4B_SM_14TeV-madgraph-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/BC1B3737-D3BB-E711-B6F5-14187764197C.root',
'/store/mc/PhaseIITDRFall17DR/VBFToHHTo4B_SM_14TeV-madgraph-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/C0838F8F-BEB8-E711-AE90-FA163EDE6201.root',
'/store/mc/PhaseIITDRFall17DR/VBFToHHTo4B_SM_14TeV-madgraph-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/C86329BF-99B8-E711-A322-FA163E7A8359.root',
'/store/mc/PhaseIITDRFall17DR/VBFToHHTo4B_SM_14TeV-madgraph-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/CAED8792-D0B9-E711-88D0-02163E014FB3.root',
'/store/mc/PhaseIITDRFall17DR/VBFToHHTo4B_SM_14TeV-madgraph-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/D0321193-D4B8-E711-8945-A4BF0112BC72.root',
'/store/mc/PhaseIITDRFall17DR/VBFToHHTo4B_SM_14TeV-madgraph-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/D6389BC0-3ABC-E711-ACB5-FA163E160BB8.root',
'/store/mc/PhaseIITDRFall17DR/VBFToHHTo4B_SM_14TeV-madgraph-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/E64560CE-5BBA-E711-BB90-44A842CFD60C.root',
'/store/mc/PhaseIITDRFall17DR/VBFToHHTo4B_SM_14TeV-madgraph-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/F26CB3FA-5EB9-E711-99AD-44A84225C851.root',
'/store/mc/PhaseIITDRFall17DR/VBFToHHTo4B_SM_14TeV-madgraph-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/F4CEE57C-D3B8-E711-BC1F-02163E017620.root',
'/store/mc/PhaseIITDRFall17DR/VBFToHHTo4B_SM_14TeV-madgraph-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/F84CC272-57B8-E711-9670-FA163E7B2A6B.root',
'/store/mc/PhaseIITDRFall17DR/VBFToHHTo4B_SM_14TeV-madgraph-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/F885EE87-F0B8-E711-A7C0-FA163E4C7713.root',
'/store/mc/PhaseIITDRFall17DR/VBFToHHTo4B_SM_14TeV-madgraph-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/FEC1E623-D4B8-E711-91AE-002481DE485A.root' ] );


secFiles.extend( [
               ] )
