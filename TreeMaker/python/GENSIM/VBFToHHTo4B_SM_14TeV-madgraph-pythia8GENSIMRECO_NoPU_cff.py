import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/PhaseIITDRFall17DR/VBFToHHTo4B_SM_14TeV-madgraph-pythia8/GEN-SIM-RECO/noPU_93X_upgrade2023_realistic_v2-v1/150000/1E8D0821-D4B8-E711-93EF-A4BF01125C60.root',
'/store/mc/PhaseIITDRFall17DR/VBFToHHTo4B_SM_14TeV-madgraph-pythia8/GEN-SIM-RECO/noPU_93X_upgrade2023_realistic_v2-v1/150000/58C537B6-D4B8-E711-9DEA-141877637B68.root',
'/store/mc/PhaseIITDRFall17DR/VBFToHHTo4B_SM_14TeV-madgraph-pythia8/GEN-SIM-RECO/noPU_93X_upgrade2023_realistic_v2-v1/150000/8A518EA6-66B8-E711-BCA8-FA163E45DF18.root',
'/store/mc/PhaseIITDRFall17DR/VBFToHHTo4B_SM_14TeV-madgraph-pythia8/GEN-SIM-RECO/noPU_93X_upgrade2023_realistic_v2-v1/150000/B6955DEF-D3B8-E711-AFC5-02163E0130EA.root',
'/store/mc/PhaseIITDRFall17DR/VBFToHHTo4B_SM_14TeV-madgraph-pythia8/GEN-SIM-RECO/noPU_93X_upgrade2023_realistic_v2-v1/150000/C21BF079-66B8-E711-A715-FA163E9603AB.root',
'/store/mc/PhaseIITDRFall17DR/VBFToHHTo4B_SM_14TeV-madgraph-pythia8/GEN-SIM-RECO/noPU_93X_upgrade2023_realistic_v2-v1/150000/C6A222ED-D5B8-E711-959E-ECB1D7B67E10.root' ] );


secFiles.extend( [
               ] )
