import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/PhaseIITDRFall17DR/VBF_BulkGravToWW_narrow_M-2000_14TeV-madgraph/GEN-SIM-RECO/noPU_93X_upgrade2023_realistic_v2-v1/150000/08F9847E-63B3-E711-88F9-782BCB50BA52.root',
'/store/mc/PhaseIITDRFall17DR/VBF_BulkGravToWW_narrow_M-2000_14TeV-madgraph/GEN-SIM-RECO/noPU_93X_upgrade2023_realistic_v2-v1/150000/1207CA83-6FB3-E711-B101-5065F381E271.root',
'/store/mc/PhaseIITDRFall17DR/VBF_BulkGravToWW_narrow_M-2000_14TeV-madgraph/GEN-SIM-RECO/noPU_93X_upgrade2023_realistic_v2-v1/150000/12902692-AEB2-E711-AD66-E0071B742D60.root',
'/store/mc/PhaseIITDRFall17DR/VBF_BulkGravToWW_narrow_M-2000_14TeV-madgraph/GEN-SIM-RECO/noPU_93X_upgrade2023_realistic_v2-v1/150000/1E5D68F3-12B4-E711-A2B3-002590DE6E30.root',
'/store/mc/PhaseIITDRFall17DR/VBF_BulkGravToWW_narrow_M-2000_14TeV-madgraph/GEN-SIM-RECO/noPU_93X_upgrade2023_realistic_v2-v1/150000/4853FAAD-AFB4-E711-A217-A0B3CCE45C2A.root',
'/store/mc/PhaseIITDRFall17DR/VBF_BulkGravToWW_narrow_M-2000_14TeV-madgraph/GEN-SIM-RECO/noPU_93X_upgrade2023_realistic_v2-v1/150000/705A5ACF-13B4-E711-86C0-0CC47AD99176.root',
'/store/mc/PhaseIITDRFall17DR/VBF_BulkGravToWW_narrow_M-2000_14TeV-madgraph/GEN-SIM-RECO/noPU_93X_upgrade2023_realistic_v2-v1/150000/74F861B5-6BB3-E711-8A65-E0071B73B6F0.root',
'/store/mc/PhaseIITDRFall17DR/VBF_BulkGravToWW_narrow_M-2000_14TeV-madgraph/GEN-SIM-RECO/noPU_93X_upgrade2023_realistic_v2-v1/150000/80319B7B-76AF-E711-8E14-90E2BAD1C73C.root',
'/store/mc/PhaseIITDRFall17DR/VBF_BulkGravToWW_narrow_M-2000_14TeV-madgraph/GEN-SIM-RECO/noPU_93X_upgrade2023_realistic_v2-v1/150000/92405DBC-97B5-E711-9197-5065F37D4131.root',
'/store/mc/PhaseIITDRFall17DR/VBF_BulkGravToWW_narrow_M-2000_14TeV-madgraph/GEN-SIM-RECO/noPU_93X_upgrade2023_realistic_v2-v1/150000/9E5384A1-50B3-E711-9EF7-E0071B73B6F0.root',
'/store/mc/PhaseIITDRFall17DR/VBF_BulkGravToWW_narrow_M-2000_14TeV-madgraph/GEN-SIM-RECO/noPU_93X_upgrade2023_realistic_v2-v1/150000/A2667E2D-68B3-E711-9DF3-5065F38142E1.root',
'/store/mc/PhaseIITDRFall17DR/VBF_BulkGravToWW_narrow_M-2000_14TeV-madgraph/GEN-SIM-RECO/noPU_93X_upgrade2023_realistic_v2-v1/150000/C042F8B3-9EB4-E711-B3CA-E0071B7A7860.root',
'/store/mc/PhaseIITDRFall17DR/VBF_BulkGravToWW_narrow_M-2000_14TeV-madgraph/GEN-SIM-RECO/noPU_93X_upgrade2023_realistic_v2-v1/150000/F20A93AF-13B4-E711-95DF-002590785950.root',
'/store/mc/PhaseIITDRFall17DR/VBF_BulkGravToWW_narrow_M-2000_14TeV-madgraph/GEN-SIM-RECO/noPU_93X_upgrade2023_realistic_v2-v1/150000/F826DDA3-76AF-E711-B167-002590FD030A.root',
'/store/mc/PhaseIITDRFall17DR/VBF_BulkGravToWW_narrow_M-2000_14TeV-madgraph/GEN-SIM-RECO/noPU_93X_upgrade2023_realistic_v2-v1/150000/F8CBAF1D-80B4-E711-97A2-C0BFC0E56816.root' ] );


secFiles.extend( [
               ] )
