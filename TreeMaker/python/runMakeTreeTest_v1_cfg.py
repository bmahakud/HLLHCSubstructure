import sys
import FWCore.ParameterSet.Config as cms
# Read parameters
from Configuration.StandardSequences.Eras import eras
process = cms.Process("HLLHCTreeMaker")
# configure geometry & conditions
#process.load("Configuration.Geometry.GeometryExtended2023D4Reco_cff")
process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
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
        input = cms.untracked.int32(10)
)
process.source = cms.Source("PoolSource",
        #fileNames = cms.untracked.vstring("/store/mc/PhaseIITDRSpring17MiniAOD/RSGluonToTT_M-3000_TuneCUETP8M1_14TeV-pythia8/MINIAODSIM/noPU_91X_upgrade2023_realistic_v3-v1/90000/10E3DB34-DA56-E711-AF9F-D8D385AF8A88.root"),
fileNames = cms.untracked.vstring("file:6C325DFE-5EBE-E611-9E4D-0025904C6620.root"),
)

process.TFileService = cms.Service("TFileService",
        fileName = cms.string("Test_.root")
)

#process.AK8Jets = cms.EDProducer("JetProducer",
#    AK8PFJetTag = cms.InputTag("slimmedJetsAK8")
#    )
#VectorRecoCand.extend(['AK8Jets:AK8PFJet(AK8PFJets)'])


process.TreeMaker = cms.EDProducer(
'TreeMaker',
# Name of the output tree
TreeName = cms.string('RA2Tree'),
## might help if something isn't working, will produce couts
debug = cms.bool(False),
#default: output RecoCands as vector<TLorentzVector>
#switches to vector<double> pt, eta, phi, energy if false
doLorentz = cms.bool(True),
#branches are sorted alphabetically by default
sortBranches = cms.bool(True),
# list of reco candidate objects: for each reco cand collection, the TLorentzVector will be stored in a vector.
VarsBool = cms.vstring(),
VarsInt = cms.vstring(),
VarsFloat = cms.vstring(),
VarsDouble = cms.vstring(),
VarsString = cms.vstring(),
VarsTLorentzVector = cms.vstring(),
VectorBool = cms.vstring(),
VectorInt = cms.vstring(),
VectorFloat = cms.vstring(),
VectorDouble=cms.vstring("AK8Jets:AK8PFMass(AK8PFJetMass)"),
VectorString = cms.vstring(),
VectorTLorentzVector = cms.vstring(),
VectorRecoCand = cms.vstring("AK8Jets:AK8PFJet(AK8PFJets)"),
)

from JMEAnalysis.JetToolbox.jetToolbox_cffGen import jetToolbox
#jetToolbox( process, 'ak8', 'jetSequence', 'out', PUMethod='Puppi',JETCorrLevels = [ 'None' ],
#subJETCorrLevels = [ 'None' ], miniAOD=True,runOnMC=True)
ak8Cut    = 'pt > 30 && abs(eta) < 2.5'
ak8pupCut = 'pt > 140 && abs(eta) < 2.5'

listBTagInfos = [
     'pfInclusiveSecondaryVertexFinderTagInfos',
]



listBtagDiscriminatorsAK8 = [ 
    # 'pfJetProbabilityBJetTags',
    'pfCombinedInclusiveSecondaryVertexV2BJetTags',
    # 'pfCombinedMVAV2BJetTags',
    # 'pfCombinedCvsLJetTags',
    # 'pfCombinedCvsBJetTags',
    # 'pfBoostedDoubleSecondaryVertexAK8BJetTags',
    # 'pfBoostedDoubleSecondaryVertexCA15BJetTags',
]


jetToolbox( process, 'ak8', 'ak8JetSubs', 'out', 
  runOnMC = True, 
  PUMethod='Plain',
  JETCorrPayload='None', 
  JETCorrLevels = [ 'None' ],
  subJETCorrLevels = [ 'None' ],
  addSoftDropSubjets = True, 
  addTrimming = True,  rFiltTrim=0.2, ptFrac=0.05,
  addPruning = True, 
  addFiltering = True, 
  addSoftDrop = True, 
  addNsub = True, 
  bTagInfos = listBTagInfos, 
  bTagDiscriminators = listBtagDiscriminatorsAK8, 
  addCMSTopTagger = False, 
  Cut = ak8pupCut , 
  addNsubSubjets = True, 
  subjetMaxTau = 3 )




process.AK8Jets = cms.EDProducer("JetProducer",
    AK8PFJetTag = cms.InputTag("selectedPatJetsAK8PF")#slimmedJetsAK8")#collection by jetToolBox selectedPatJetsAK8PFCHS
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
       # process.Baseline *
        process.AK8Jets
    )

process.WriteTree.associate(process.myTask)

process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )
process.options.allowUnscheduled = cms.untracked.bool(True)

# final tweaks to process
process.options.SkipEvent = cms.untracked.vstring('ProductNotFound')
process.TFileService.closeFileFast = cms.untracked.bool(True)
