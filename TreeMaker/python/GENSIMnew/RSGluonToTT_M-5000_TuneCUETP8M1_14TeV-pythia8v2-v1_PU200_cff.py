import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/00FAB82F-6FBA-E711-9330-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/020D1131-1FBA-E711-ADE3-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/02896944-2DBA-E711-955A-008CFAE451D8.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/06084940-B0BA-E711-8B14-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/08856E08-E0B9-E711-A0C6-0025905AA9F0.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/08A86882-7ABA-E711-8192-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/0A0D448B-84BA-E711-924C-0CC47A4C8E14.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/0A1525D0-79BA-E711-B492-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/0A776184-1CBB-E711-9A28-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/0C4411DD-3ABB-E711-B4FD-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/0C6B9C63-80BA-E711-B352-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/1433A6F2-FEB9-E711-8775-0CC47A6C1866.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/16006EDB-60BA-E711-927D-0025907254C8.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/1A855017-C3BA-E711-B9B0-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/208BEA1F-6ABA-E711-9B87-1866DAEA6CF0.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/242C035D-D5B8-E711-80A2-F04DA27541CF.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/245ABC43-DEB9-E711-B5AB-0CC47AD98B8E.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/263BA333-BABA-E711-9301-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/26B41146-A7BA-E711-87BB-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/2A0FBFB9-4ABA-E711-BFBE-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/2C881139-5DBA-E711-B672-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/2CE0CB59-DFB9-E711-8033-0CC47AD98D0C.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/2CFE5192-94B9-E711-8644-7845C4FC3BD2.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/2E84BC04-26B9-E711-9C61-7CD30AC0301A.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/3061A769-05BA-E711-92B3-E0071B73B6B0.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/30919710-3EBA-E711-A564-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/30CFCD7F-28BA-E711-8A0C-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/30E0920F-95BA-E711-B45A-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/32AF32C3-25BA-E711-9993-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/32DF2EC9-34BA-E711-A21D-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/38169C78-2BBA-E711-B5A2-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/3AAC1E90-D6B9-E711-AEC8-782BCB21110B.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/3CD29CA4-34BA-E711-963A-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/3E1D754C-8FBA-E711-AECE-0CC47AD9901E.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/42504B2D-BABA-E711-8EFD-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/44C2563B-05BA-E711-9DDF-E0071B740D80.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/4639E544-35BA-E711-B2D3-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/46962E32-BABA-E711-9D2E-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/480D5830-BABA-E711-ADD6-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/4A57608A-34BA-E711-88CE-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/4ABEF416-07BA-E711-8BDF-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/4E95CE24-A8BA-E711-85E3-24BE05C4D8F1.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/56468164-7BB9-E711-86D1-7845C4F93215.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/565C8D5A-85BA-E711-A287-0CC47A4C8E16.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/626CE494-19BA-E711-BD71-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/64B99BE7-6ABA-E711-9376-24BE05CEFB41.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/661C9756-5ABA-E711-A1B6-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/66A1B2CF-E6B9-E711-B496-E0071B73C640.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/681363CC-1FBA-E711-AF60-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/6869D1DD-22B9-E711-AB5D-F04DA27541CF.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/6A2EF0F7-34BB-E711-B222-24BE05CEEB31.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/6AA0DC06-24B9-E711-851D-008CFAF5592A.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/6AA74976-B7BA-E711-B8BE-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/6C78E937-6DBC-E711-B53C-0025905A48C0.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/728ED69F-D4BB-E711-995A-0025900B5648.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/7A179438-E0B9-E711-A8C7-0CC47A4D7640.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/7C5BDA5B-BCBA-E711-9A7C-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/801A434C-3CBA-E711-90D1-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/826D0F7D-26BA-E711-9D24-008CFAF29264.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/864BC598-B8BA-E711-9A1A-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/8E655638-B1BA-E711-B88C-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/8EACFFBD-D8B8-E711-A35E-008CFAF5592A.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/9207A427-BABA-E711-A7B4-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/9291F8FF-2CB9-E711-9B5E-7CD30AC03006.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/962F1E36-BABA-E711-BFB0-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/966678FC-C2B9-E711-A50E-0CC47AD98CFA.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/96C34297-ECB9-E711-98B1-24BE05C49891.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/98D48ED0-26BA-E711-AF34-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/9A11FE0D-81BA-E711-B8A6-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/9C14575F-3ABB-E711-B500-0CC47A7C3424.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/9C91FB36-BABA-E711-A4F8-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/9E7EE5CC-32BA-E711-9F32-0025901D08BE.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/9E908E1D-B3BA-E711-B059-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/9EACBCA7-5ABC-E711-BE52-24BE05C6C741.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/A0512377-11BA-E711-A44A-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/A4017643-7ABA-E711-8BDB-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/A4612944-25BA-E711-9E06-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/A4A6B549-30BA-E711-905C-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/A882D3A6-BBBA-E711-9354-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/A89D2FA3-4DBA-E711-8B15-0CC47AD98CFA.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/A8CF3061-D3BB-E711-B97F-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/AA135A34-BABA-E711-9052-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/AA261D9D-48BB-E711-AAAB-0CC47A13CB18.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/AA801EAD-A6BA-E711-87D6-0CC47A6C115C.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/AAE3CAD9-47BA-E711-BC98-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/AEE78737-19BC-E711-8B7E-24BE05C4D851.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/B286A40C-7DB9-E711-986C-A0369F5BD8D4.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/B2A44334-BABA-E711-A565-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/B6BD34C3-1DBA-E711-B98F-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/B8958334-3CBB-E711-B867-0CC47AD991FA.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/BAF6B5DA-89B9-E711-804A-F04DA2753F56.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/BC75F11F-FBB9-E711-BD71-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/BE239B2F-78BA-E711-ADAA-0CC47AA98A0E.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/CA081E0F-B1BA-E711-A9A7-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/CA79CD09-24B9-E711-8494-A0369F5BD8D4.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/D0326BF0-0BBB-E711-9FD6-E0071B73C610.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/D0378B45-C0B9-E711-B806-90B11C282313.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/D25BE162-D4BB-E711-8954-0CC47A7452D0.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/D4E65F4A-27BC-E711-9E4E-001E675A68C4.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/D62755A7-D3BB-E711-9261-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/E07863DB-05BA-E711-B8C8-0CC47AD9914A.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/E2AE84E9-34BA-E711-8542-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/E2EC9029-C4B9-E711-94CB-0025900E3514.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/E47A5FA3-08BB-E711-8158-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/E6E96373-46BA-E711-9984-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/E8B06E35-BABA-E711-BA22-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/EA7C8EA0-3EBA-E711-A95A-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/EADEBEE9-17BA-E711-B8A7-782BCB1F5E69.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/EC03115D-D4BB-E711-A24F-0CC47A4C8EEA.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/EC781CBD-3ABB-E711-B94F-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/EEC1860F-7FBA-E711-94E6-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/F63C6FF0-69BA-E711-BFBF-24BE05CEECD1.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/F6B38C6A-06BA-E711-BD49-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/F8B91ABA-3EBA-E711-9939-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/FA42B74C-BCB9-E711-AD1F-0025907254C8.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/FA65E2CC-0BBA-E711-A402-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/FAF99B37-E0B9-E711-908B-0CC47A4C8F12.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/FCD332EA-8CBA-E711-A24A-0CC47AD98B8E.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/00000/FEFE2B09-B1BA-E711-9526-0242AC130002.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/1404226F-95B9-E711-BDD4-141877410B85.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/1C1FCD16-ADB8-E711-A23B-0CC47AA992B2.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/1C4099D5-E0BA-E711-A8CA-0CC47AA98A0E.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/2A624BE5-F0B8-E711-B4CB-002590725380.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/304EEF6A-0BBA-E711-A9E1-FA163EFC0D54.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/34C747B6-36B9-E711-A3E9-10983627C3DB.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/3A178F2D-36B9-E711-BBA6-0025900B20E2.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/420CBCA0-34B9-E711-A235-90B11C27E141.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/4A8025ED-0BBA-E711-A849-FA163E546DA9.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/4ED21294-0EB9-E711-A23F-7CD30AC03016.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/5C310BEC-6EB9-E711-A0EA-24BE05CEFB31.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/5E1C289F-ADB8-E711-9750-0CC47A6C138A.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/6888E997-E0B9-E711-B532-0CC47AACFCDE.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/6CB6F2E9-4EB9-E711-9D9D-0CC47AD98D12.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/7450DE03-D4B9-E711-B9B1-0025900B20E2.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/A4E80A26-63B9-E711-853A-E0071B7AC770.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/B093F5D4-D5B9-E711-B11A-0CC47A6C1060.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/B097B3A5-ADB8-E711-97B8-0CC47AD98B8E.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/B2A25B0A-57B9-E711-92EF-0CC47AD98F6E.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/B63E1BFA-0BBA-E711-B5A5-FA163E477EA9.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/BCD8CC58-0BBA-E711-86A6-FA163ED0C1C8.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/C4AF70F3-0BBA-E711-96B2-FA163E4D7022.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/C852542F-E6B9-E711-9176-002590CB0B5A.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/CE7776C9-72B9-E711-8882-7CD30AC0301A.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/D2717489-99B8-E711-94A5-0CC47A13D110.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/D29854F5-0BBA-E711-A380-FA163E5D21A5.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/E23DA533-E6B9-E711-B40F-0CC47A13D052.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/E69356EE-3DBA-E711-BC28-5065F38142E1.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/EA04FC00-0CBA-E711-9419-FA163E523873.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/FE104100-0CBA-E711-9E5A-FA163E2C55BD.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/30000/04175711-92BA-E711-BFF8-FA163E1C5550.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/30000/0423A081-B0B8-E711-B86B-FA163E2B764A.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/30000/0AB6F0AD-02BA-E711-B848-E0071B7A9810.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/30000/0E6D7F93-F1B9-E711-8304-FA163E01971C.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/30000/10000FD3-D4B8-E711-9B61-7845C4FB82F2.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/30000/40321C5F-F1B9-E711-9F25-02163E01492D.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/30000/7AE89251-F2B9-E711-BDAD-02163E014A82.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/30000/8858BF57-F1B9-E711-BB66-FA163E834B97.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/30000/92CC7E02-0AB9-E711-86AD-008CFAFBEEE6.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/30000/9E1E9654-F1B9-E711-A6D8-FA163EBE2454.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/30000/B27B4128-F2B9-E711-A008-FA163EDCCDE1.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/30000/C662B960-F1B9-E711-A0E5-FA163EA8B047.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/30000/C66D3B56-F1B9-E711-A82B-FA163EC3C56B.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/30000/C82F8755-F1B9-E711-9362-FA163E5A9498.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/30000/D0609275-F1B9-E711-A971-02163E0149CA.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/30000/E84E2753-F1B9-E711-BF00-FA163E4F8C68.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/30000/EE182C13-16BA-E711-B042-0CC47AA989BA.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/30000/F099B2F2-D0BB-E711-BA19-0CC47A7C3444.root',
'/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-5000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/30000/F2A50C58-F1B9-E711-AA16-FA163E215219.root' ] );


secFiles.extend( [
               ] )
