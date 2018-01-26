import sys
import FWCore.ParameterSet.Config as cms
# Read parameters
from HLLHCSubstructure.TreeMaker.CommandLineParams import CommandLineParams
parameters = CommandLineParams()
inputFilesConfig=parameters.value("inputFilesConfig","")
dataset=parameters.value("dataset",[])
nstart = parameters.value("nstart",0)
nfiles = parameters.value("nfiles",-1)
numevents=parameters.value("numevents",-1)
reportfreq=parameters.value("reportfreq",100)





from Configuration.StandardSequences.Eras import eras
process = cms.Process("HLLHCTreeMaker",eras.Phase2_timing)
# configure geometry & conditions
#process.load("Configuration.Geometry.GeometryExtended2023D4Reco_cff")
#process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
process.load("Configuration.Geometry.GeometryExtended2023D20Reco_cff")
#process.load("Configuration.StandardSequences.GeometryExtended_cff")
process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load('Configuration.StandardSequences.Services_cff')
process.GlobalTag.globaltag ="90X_upgrade2023_realistic_v1"# "80X_mcRun2_asymptotic_2016_TrancheIV_v8"
process.load('JetMETCorrections.Configuration.DefaultJEC_cff')
process.load("PhysicsTools.PatAlgos.patSequences_cff")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.options = cms.untracked.PSet(
        allowUnscheduled = cms.untracked.bool(True),
#        wantSummary = cms.untracked.bool(True) # off by default
)

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(100)
)

redir=parameters.value("redir", "root://cms-xrd-global.cern.ch/")# if fastsim and signal else "root://cms-xrd-global.cern.ch/")
readFiles = cms.untracked.vstring()

if inputFilesConfig!="" :
    if nfiles==-1:
        process.load("HLLHCSubstructure.TreeMaker."+inputFilesConfig+"_cff")
        readFiles.extend( process.source.fileNames )
    else:
        readFilesImport = getattr(__import__("HLLHCSubstructure.TreeMaker."+inputFilesConfig+"_cff",fromlist=["readFiles"]),"readFiles")
        readFiles.extend( readFilesImport[nstart:(nstart+nfiles)] )

if dataset!=[] :
    readFiles.extend( [dataset] )

for f,val in enumerate(readFiles):
    if readFiles[f][0:6]=="/store":
        readFiles[f] = redir+readFiles[f]




process.source = cms.Source("PoolSource",
        #fileNames = cms.untracked.vstring("/store/mc/PhaseIITDRSpring17MiniAOD/RSGluonToTT_M-3000_TuneCUETP8M1_14TeV-pythia8/MINIAODSIM/noPU_91X_upgrade2023_realistic_v3-v1/90000/10E3DB34-DA56-E711-AF9F-D8D385AF8A88.root"),
        #fileNames = cms.untracked.vstring("/store/mc/PhaseIITDRFall17MiniAOD/RSGluonToTT_M-3000_TuneCUETP8M1_14TeV-pythia8/MINIAODSIM/noPU_93X_upgrade2023_realistic_v2-v1/00000/0479CE11-46AF-E711-BE92-FA163E519C7A.root"),
        #fileNames =cms.untracked.vstring("/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-3000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/PU200_93X_upgrade2023_realistic_v2-v1/150000/007AD037-A4B8-E711-A642-24BE05CECBE1.root"),
        #fileNames =cms.untracked.vstring("/store/mc/PhaseIITDRFall17DR/RSGluonToTT_M-3000_TuneCUETP8M1_14TeV-pythia8/GEN-SIM-RECO/noPU_93X_upgrade2023_realistic_v2-v1/00000/74EABFA9-68AE-E711-BF6E-6CC2173DA930.root"),
         fileNames=cms.untracked.vstring(readFiles),
#fileNames = cms.untracked.vstring("file:6C325DFE-5EBE-E611-9E4D-0025904C6620.root"),
)

process.TFileService = cms.Service("TFileService",
        fileName = cms.string("Test_.root")
)

#process.AK8Jets = cms.EDProducer("JetProducer",
#    AK8PFJetTag = cms.InputTag("slimmedJetsAK8")
#    )
#VectorRecoCand.extend(['AK8Jets:AK8PFJet(AK8PFJets)'])

#VectorRecoCand       = cms.vstring()
#VarsDouble           = cms.vstring()
#VarsInt              = cms.vstring()
#VarsBool             = cms.vstring()
#VectorTLorentzVector = cms.vstring()
#VarsTLorentzVector = cms.vstring()
#VectorDouble         = cms.vstring()
#VectorString         = cms.vstring()
#VectorInt            = cms.vstring()
#vectorBool           = cms.vstring()



process.MET = cms.EDProducer("METProducer",
    METTag = cms.InputTag("pfMet")
    )
#        VarsDouble.extend(['MET:Pt(MET)'])
process.goodVertices = cms.EDFilter("VertexSelector",
    src = cms.InputTag("offlinePrimaryVertices"),
    cut = cms.string("!isFake && ndof > 4 && abs(z) < 24 && position.Rho < 2"),
    filter = cms.bool(False)
    )
#        from HLLHCSubstructure.Utils.primaryvertices_cfi import primaryvertices
process.NVtx = cms.EDProducer("PrimaryVerticesInt",
    VertexCollection  = cms.InputTag('goodVertices'),
    )
#        VarsInt.extend(['NVtx:nPV(NVtx)'])
    # also store total number of vertices without quality checks
process.nAllVertices = cms.EDProducer("PrimaryVerticesInt",
    VertexCollection  = cms.InputTag('offlinePrimaryVertices'),
    )
#        VarsInt.extend(['nAllVertices:nPV(nAllVertices)'])
#        from HLLHCSubstructure.Utils.pileup_cfi import pileup
process.npu = cms.EDProducer("PileupInfo",
   puCollection  = cms.InputTag('addPileupInfo'),
  )
#        VarsInt.extend(['npu'])







from JMEAnalysis.JetToolbox.jetToolbox_cffBackUp import jetToolbox



SoftDrop_=True
Trimming_=True
Pruning_=True
Nsub_=True
CMSTopTagger_=False;
puMethod_='Puppi'
runOnminiAOD_=False



jetToolbox( process, 'ak8', 'jetSequence', 'out', PUMethod='CHS', miniAOD=runOnminiAOD_,runOnMC=True,addSoftDrop=SoftDrop_, addSoftDropSubjets=SoftDrop_,addTrimming=Trimming_,addPruning=Pruning_,addPrunedSubjets=Pruning_,addNsub=Nsub_,addCMSTopTagger=False)
jetToolbox( process, 'ak8', 'jetSequence', 'out', PUMethod='Puppi',JETCorrLevels = [  'None' ],subJETCorrLevels = [ 'None' ],JETCorrPayload='None',subJETCorrPayload='None', miniAOD=runOnminiAOD_,runOnMC=True,addSoftDrop=SoftDrop_, addSoftDropSubjets=SoftDrop_,addTrimming=Trimming_,addPruning=Pruning_,addPrunedSubjets=Pruning_,addNsub=Nsub_,addNsubSubjets = True,
  subjetMaxTau = 3)


import os
cwd = os.getcwd()
print "current working directory: ",cwd

copy1="xrdcp  root://cmseos.fnal.gov//store/user/bmahakud/JECFiles/PhaseIISummer16_25nsV3_MC_L1FastJet_AK8PFPuppi.txt ."
copy2="xrdcp  root://cmseos.fnal.gov//store/user/bmahakud/JECFiles/PhaseIISummer16_25nsV3_MC_L2Relative_AK8PFPuppi.txt ."
copy3="xrdcp  root://cmseos.fnal.gov//store/user/bmahakud/JECFiles/PhaseIISummer16_25nsV3_MC_L3Absolute_AK8PFPuppi.txt ."
copy4="xrdcp  root://cmseos.fnal.gov//store/user/bmahakud/JECFiles/Summer16_23Sep2016V3_MC_L2L3Residual_AK8PFPuppi.txt ."
copy5="xrdcp  root://cmseos.fnal.gov//store/user/bmahakud/JECFiles/Summer16_23Sep2016V3_MC_Uncertainty_AK8PFPuppi.txt ."
copy6="xrdcp  root://cmseos.fnal.gov//store/user/bmahakud/JECFiles/PhaseIISummer16_25nsV3_MC_L1FastJet_AK4PFPuppi.txt ."
copy7="xrdcp  root://cmseos.fnal.gov//store/user/bmahakud/JECFiles/PhaseIISummer16_25nsV3_MC_L2Relative_AK4PFPuppi.txt ."
copy8="xrdcp  root://cmseos.fnal.gov//store/user/bmahakud/JECFiles/PhaseIISummer16_25nsV3_MC_L3Absolute_AK4PFPuppi.txt ."
copy9="xrdcp  root://cmseos.fnal.gov//store/user/bmahakud/JECFiles/Summer16_23Sep2016V3_MC_L2L3Residual_AK4PFPuppi.txt ."
copy10="xrdcp  root://cmseos.fnal.gov//store/user/bmahakud/JECFiles/Summer16_23Sep2016V3_MC_Uncertainty_AK4PFPuppi.txt ."


os.system(copy1)
os.system(copy2)
os.system(copy3)
os.system(copy4)
os.system(copy5)
os.system(copy6)
os.system(copy7)
os.system(copy8)
os.system(copy9)
os.system(copy10)

jecfile=cwd+"/"












process.AK8Jets = cms.EDProducer("JetProducer",
    #AK8PFJetTag = cms.InputTag("slimmedJetsAK8")#collection by jetToolBox selectedPatJetsAK8PFCHS
    AK8PFJetTag = cms.InputTag("selectedPatJetsAK8PFCHS"),
    jetCollection =cms.untracked.string("ak4GenJetsNoNu"),
    AK8PFCHSJetTag = cms.InputTag("selectedPatJetsAK8PFCHS"),
    AK8PFPuppiJetTag = cms.InputTag("selectedPatJetsAK8PFPuppi"),
    AK8PFPuppiSubjetTag = cms.InputTag("selectedPatJetsAK8PFPuppiSoftDropPacked","SubJets"),
    AK8GenJetTag = cms.InputTag("ak4GenJetsNoNu"),
    prunedGenParticles = cms.InputTag("genParticles"),
    vertexTag =cms.InputTag("offlinePrimaryVertices"),
    rhoTag =cms.InputTag("fixedGridRhoFastjetAll"),
    TurnOnCMSTopTagger=cms.bool(CMSTopTagger_),
    TurnOnSoftdrop =cms.bool(SoftDrop_),
    TurnOnTrimming =cms.bool(Trimming_),
    TurnOnPruning =cms.bool(Pruning_),
    TurnOnNsub =cms.bool(Nsub_),
    jecPayloadsAK8chs = cms.vstring([
                                    jecfile+'PhaseIISummer16_25nsV3_MC_L1FastJet_AK8PFchs.txt',
                                    jecfile+'PhaseIISummer16_25nsV3_MC_L2Relative_AK8PFchs.txt',
                                    jecfile+'PhaseIISummer16_25nsV3_MC_L3Absolute_AK8PFchs.txt',
                                    jecfile+'Summer16_23Sep2016V3_MC_L2L3Residual_AK8PFchs.txt',
                                    jecfile+'Summer16_23Sep2016V3_MC_Uncertainty_AK8PFchs.txt'
                                    ]),
    jecPayloadsAK4chs = cms.vstring([
                                    jecfile+'PhaseIISummer16_25nsV3_MC_L1FastJet_AK4PFchs.txt',
                                    jecfile+'PhaseIISummer16_25nsV3_MC_L2Relative_AK4PFchs.txt',
                                    jecfile+'PhaseIISummer16_25nsV3_MC_L3Absolute_AK4PFchs.txt',
                                    jecfile+'Summer16_23Sep2016V3_MC_L2L3Residual_AK4PFchs.txt',
                                    jecfile+'Summer16_23Sep2016V3_MC_Uncertainty_AK4PFchs.txt'
                                    ]),
    jecPayloadsAK8pup = cms.vstring([
                                    jecfile+'PhaseIISummer16_25nsV3_MC_L1FastJet_AK8PFPuppi.txt',
                                    jecfile+'PhaseIISummer16_25nsV3_MC_L2Relative_AK8PFPuppi.txt',
                                    jecfile+'PhaseIISummer16_25nsV3_MC_L3Absolute_AK8PFPuppi.txt',
                                    jecfile+'Summer16_23Sep2016V3_MC_L2L3Residual_AK8PFPuppi.txt',
                                    jecfile+'Summer16_23Sep2016V3_MC_Uncertainty_AK8PFPuppi.txt'
                                    ]),
    jecPayloadsAK4pup = cms.vstring([
                                    jecfile+'PhaseIISummer16_25nsV3_MC_L1FastJet_AK4PFPuppi.txt',
                                    jecfile+'PhaseIISummer16_25nsV3_MC_L2Relative_AK4PFPuppi.txt',
                                    jecfile+'PhaseIISummer16_25nsV3_MC_L3Absolute_AK4PFPuppi.txt',
                                    jecfile+'Summer16_23Sep2016V3_MC_L2L3Residual_AK4PFPuppi.txt',
                                    jecfile+'Summer16_23Sep2016V3_MC_Uncertainty_AK4PFPuppi.txt'
    ]),
    )

    


process.TreeMaker = cms.EDProducer(
'TreeMaker',
TreeName          = cms.string('Phase2Tree'),
debug = cms.bool(False),
doLorentz = cms.bool(True),
sortBranches = cms.bool(True),
VarsBool = cms.vstring(),
VarsInt = cms.vstring('NVtx:nPV(NVtx)','npu(npu)'),
VarsFloat = cms.vstring(),
VarsDouble = cms.vstring('MET:Pt(MET)','AK8Jets:Jet0SDmass(Jet0SDmass)','AK8Jets:Jet0MassPruned(Jet0MassPruned)','AK8Jets:Jet0MassTrimmed(Jet0MassTrimmed)','AK8Jets:Jet0Tau1(Jet0Tau1)','AK8Jets:Jet0Tau2(Jet0Tau2)','AK8Jets:Jet0Tau3(Jet0Tau3)','AK8Jets:Jet0Tau4(Jet0Tau4)','AK8Jets:Jet0Tau32(Jet0Tau32)','AK8Jets:Jet0SDsubjet0bdisc(Jet0SDsubjet0bdisc)','AK8Jets:Jet0SDsubjet1bdisc(Jet0SDsubjet1bdisc)','AK8Jets:Jet0SDmaxbdisc(Jet0SDmaxbdisc)','AK8Jets:Jet0SDmaxbdiscflavHadron(Jet0SDmaxbdiscflavHadron)','AK8Jets:Jet0SDmaxbdiscflavParton(Jet0SDmaxbdiscflavParton)','AK8Jets:Jet0SDsubjet0area(Jet0SDsubjet0area)','AK8Jets:Jet0SDsubjet0flavHadron(Jet0SDsubjet0flavHadron)','AK8Jets:Jet0SDsubjet0flavParton(Jet0SDsubjet0flavParton)','AK8Jets:Jet0SDsubjet0matchedgenjetpt(Jet0SDsubjet0matchedgenjetpt)','AK8Jets:Jet0SDsubjet0tau1(Jet0SDsubjet0tau1)','AK8Jets:Jet0SDsubjet0tau2(Jet0SDsubjet0tau2)','AK8Jets:Jet0SDsubjet0tau3(Jet0SDsubjet0tau3)','AK8Jets:Jet0SDsubjet1area(Jet0SDsubjet1area)','AK8Jets:Jet0SDsubjet1flavHadron(Jet0SDsubjet1flavHadron)','AK8Jets:Jet0SDsubjet1flavParton(Jet0SDsubjet1flavParton)','AK8Jets:Jet0SDsubjet1matchedgenjetpt(Jet0SDsubjet1matchedgenjetpt)','AK8Jets:Jet0SDsubjet1tau1(Jet0SDsubjet1tau1)','AK8Jets:Jet0SDsubjet1tau2(Jet0SDsubjet1tau2)','AK8Jets:Jet0SDsubjet1tau3(Jet0SDsubjet1tau3)','AK8Jets:Jet0CHF(Jet0CHF)','AK8Jets:Jet0NHF(Jet0NHF)','AK8Jets:Jet0CM(Jet0CM)','AK8Jets:Jet0NM(Jet0NM)','AK8Jets:Jet0NEF(Jet0NEF)','AK8Jets:Jet0CEF(Jet0CEF)','AK8Jets:Jet0MF(Jet0MF)','AK8Jets:Jet0Mult(Jet0Mult)','AK8Jets:Jet1SDmass(Jet1SDmass)','AK8Jets:Jet1MassPruned(Jet1MassPruned)','AK8Jets:Jet1MassTrimmed(Jet1MassTrimmed)','AK8Jets:Jet1Tau1(Jet1Tau1)','AK8Jets:Jet1Tau2(Jet1Tau2)','AK8Jets:Jet1Tau3(Jet1Tau3)','AK8Jets:Jet1Tau4(Jet1Tau4)','AK8Jets:Jet1Tau32(Jet1Tau32)','AK8Jets:Jet1SDsubjet0bdisc(Jet1SDsubjet0bdisc)','AK8Jets:Jet1SDsubjet1bdisc(Jet1SDsubjet1bdisc)','AK8Jets:Jet1SDmaxbdisc(Jet1SDmaxbdisc)','AK8Jets:Jet1SDmaxbdiscflavHadron(Jet1SDmaxbdiscflavHadron)','AK8Jets:Jet1SDmaxbdiscflavParton(Jet1SDmaxbdiscflavParton)','AK8Jets:Jet1SDsubjet0area(Jet1SDsubjet0area)','AK8Jets:Jet1SDsubjet0flavHadron(Jet1SDsubjet0flavHadron)','AK8Jets:Jet1SDsubjet0flavParton(Jet1SDsubjet0flavParton)','AK8Jets:Jet1SDsubjet0matchedgenjetpt(Jet1SDsubjet0matchedgenjetpt)','AK8Jets:Jet1SDsubjet0tau1(Jet1SDsubjet0tau1)','AK8Jets:Jet1SDsubjet0tau2(Jet1SDsubjet0tau2)','AK8Jets:Jet1SDsubjet0tau3(Jet1SDsubjet0tau3)','AK8Jets:Jet1SDsubjet1area(Jet1SDsubjet1area)','AK8Jets:Jet1SDsubjet1flavHadron(Jet1SDsubjet1flavHadron)','AK8Jets:Jet1SDsubjet1flavParton(Jet1SDsubjet1flavParton)','AK8Jets:Jet1SDsubjet1matchedgenjetpt(Jet1SDsubjet1matchedgenjetpt)','AK8Jets:Jet1SDsubjet1tau1(Jet1SDsubjet1tau1)','AK8Jets:Jet1SDsubjet1tau2(Jet1SDsubjet1tau2)','AK8Jets:Jet1SDsubjet1tau3(Jet1SDsubjet1tau3)','AK8Jets:Jet1CHF(Jet1CHF)','AK8Jets:Jet1NHF(Jet1NHF)','AK8Jets:Jet1CM(Jet1CM)','AK8Jets:Jet1NM(Jet1NM)','AK8Jets:Jet1NEF(Jet1NEF)','AK8Jets:Jet1CEF(Jet1CEF)','AK8Jets:Jet1MF(Jet1MF)','AK8Jets:Jet1Mult(Jet1Mult)'),
VarsString = cms.vstring(),
VarsTLorentzVector = cms.vstring(),
VectorBool = cms.vstring(),
VectorInt = cms.vstring(),
VectorFloat = cms.vstring(),
VectorDouble=cms.vstring("AK8Jets:Jet0Area(Jet0Area)","AK8Jets:Jet1Area(Jet1Area)"),#"AK8Jets:AK8PFMass(AK8PFJetMass)"),#,"'AK8Jets:Jet0SDmass(Jet0SDmass)'"),
VectorString = cms.vstring(),
VectorTLorentzVector = cms.vstring("AK8Jets:AK8GenJets(AK8GenJet)","AK8Jets:Jet0Raw(Jet0Raw)","AK8Jets:Jet0(Jet0)","AK8Jets:Jet0SD(Jet0SD)","AK8Jets:Jet0SDRaw(Jet0SDRaw)","AK8Jets:Jet0SDsubjet0(Jet0SDsubjet0)","AK8Jets:Jet0SDsubjet1(Jet0SDsubjet1)","AK8Jets:Jet1Raw(Jet1Raw)","AK8Jets:Jet1(Jet1)","AK8Jets:Jet1SD(Jet1SD)","AK8Jets:Jet1SDRaw(Jet1SDRaw)","AK8Jets:Jet1SDsubjet0(Jet1SDsubjet0)","AK8Jets:Jet1SDsubjet1(Jet1SDsubjet1)"),
VectorRecoCand = cms.vstring()#"AK8Jets:AK8PFJet(AK8PFJets)"),
)




#process.TestProd = cms.EDProducer("GoodJetProducer",
#JMTag = cms.InputTag("AK8Jets:AK8PFMass")
#)

process.myTask = cms.Task()
process.myTask.add(*[getattr(process,prod) for prod in process.producers_()])
process.myTask.add(*[getattr(process,filt) for filt in process.filters_()])




#process.Baseline = cms.Sequence()
    # create the process path
    #process.dump = cms.EDAnalyzer("EventContentAnalyzer")
process.WriteTree = cms.Path(
        process.TreeMaker 
        #process.AK8Jets
    )

process.WriteTree.associate(process.myTask)

process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )
process.options.allowUnscheduled = cms.untracked.bool(True)

# final tweaks to process
process.options.SkipEvent = cms.untracked.vstring('ProductNotFound')
process.TFileService.closeFileFast = cms.untracked.bool(True)
