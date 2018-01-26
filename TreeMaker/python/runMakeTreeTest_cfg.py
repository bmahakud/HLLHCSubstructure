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
        input = cms.untracked.int32(100)
)
process.source = cms.Source("PoolSource",
        #fileNames = cms.untracked.vstring("/store/mc/PhaseIITDRSpring17MiniAOD/RSGluonToTT_M-3000_TuneCUETP8M1_14TeV-pythia8/MINIAODSIM/noPU_91X_upgrade2023_realistic_v3-v1/90000/10E3DB34-DA56-E711-AF9F-D8D385AF8A88.root"),
        fileNames = cms.untracked.vstring("/store/mc/PhaseIITDRFall17MiniAOD/RSGluonToTT_M-3000_TuneCUETP8M1_14TeV-pythia8/MINIAODSIM/noPU_93X_upgrade2023_realistic_v2-v1/00000/0479CE11-46AF-E711-BE92-FA163E519C7A.root"),
#fileNames = cms.untracked.vstring("file:6C325DFE-5EBE-E611-9E4D-0025904C6620.root"),
)

process.TFileService = cms.Service("TFileService",
        fileName = cms.string("Test_.root")
)

#process.AK8Jets = cms.EDProducer("JetProducer",
#    AK8PFJetTag = cms.InputTag("slimmedJetsAK8")
#    )
#VectorRecoCand.extend(['AK8Jets:AK8PFJet(AK8PFJets)'])

'''
process.TreeMaker = cms.EDProducer(
'TreeMaker',
# Name of the output tree
TreeName          = cms.string('RA2Tree'),
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
VectorRecoCand = cms.vstring()#"AK8Jets:AK8PFJet(AK8PFJets)"),
)


from JMEAnalysis.JetToolbox.jetToolboxShort_cff import jetToolbox
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
  PUMethod='Puppi',
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



from RecoJets.Configuration.RecoPFJets_cff import ak4PFJets, ak8PFJetsCHSSoftDrop, ak8PFJetsCHSSoftDropMass, ak8PFJetsCHSPruned, ak8PFJetsCHSPrunedMass, ak8PFJetsCHSTrimmed, ak8PFJetsCHSTrimmedMass, ak8PFJetsCHSFiltered, ak8PFJetsCHSFilteredMass, ak4PFJetsCHS, ca15PFJetsCHSMassDropFiltered, hepTopTagPFJetsCHS, ak8PFJetsCHSConstituents, puppi
from RecoJets.Configuration.RecoGenJets_cff import ak4GenJets
from RecoJets.JetProducers.SubJetParameters_cfi import SubJetParameters
from RecoJets.JetProducers.PFJetParameters_cfi import *
from RecoJets.JetProducers.GenJetParameters_cfi import *
from RecoJets.JetProducers.AnomalousCellParameters_cfi import *
from RecoJets.JetProducers.CATopJetParameters_cfi import *
from PhysicsTools.PatAlgos.producersLayer1.patCandidates_cff import *
from PhysicsTools.PatAlgos.selectionLayer1.jetSelector_cfi import selectedPatJets
from PhysicsTools.PatAlgos.tools.jetTools import addJetCollection, updateJetCollection

genParticlesLabel = 'prunedGenParticles'
pvLabel = 'offlineSlimmedPrimaryVertices'
svLabel = 'slimmedSecondaryVertices'
tvLabel = 'unpackedTracksAndVertices'
muLabel = 'slimmedMuons'
elLabel = 'slimmedElectrons'
pfCand =  'packedPFCandidates'


#jetSeq = cms.Sequence()


setattr( process, 'packedGenParticlesForJetsNoNu',          cms.EDFilter("CandPtrSelector",
                                                        src = cms.InputTag("packedGenParticles"),
                                                        cut = cms.string("abs(pdgId) != 12 && abs(pdgId) != 14 && abs(pdgId) != 16")
                                                        ))
#jetSeq += getattr(process, 'packedGenParticlesForJetsNoNu' )

setattr( process, 'ak8GenJetsNoNu',                   ak4PFJets.clone( src = 'packedGenParticles',
                                                        rParam = 0.8,
                                                        jetAlgorithm = 'AntiKt' ) )
#jetSeq += getattr(process, 'ak8GenJetsNoNu' )


process.load('PhysicsTools.PatAlgos.slimming.unpackedTracksAndVertices_cfi')
process.load('CommonTools.PileupAlgos.Puppi_cff')
puppi.candName = cms.InputTag( pfCand )
puppi.vertexName = cms.InputTag('offlineSlimmedPrimaryVertices')
puppi.clonePackedCands = cms.bool(True)
jetSeq += getattr(process, 'puppi' )
srcForPFJets = 'puppi'
from RecoJets.JetProducers.ak4PFJetsPuppi_cfi import ak4PFJetsPuppi
setattr( process, 'ak8PFJetsPuppi', ak4PFJetsPuppi.clone( src = cms.InputTag( srcForPFJets ),
                                                doAreaFastjet = True,
                                                rParam = 0.8,
                                                jetAlgorithm = 'AntiKt' ) )
jetSeq += getattr(process, 'ak8PFJetsPuppi' )
JEC = None
setattr( process, 'ak8PFJetsPuppiConstituents', cms.EDProducer("MiniAODJetConstituentSelector", src = cms.InputTag( 'ak8PFJetsPuppi' ), cut = cms.string( '' ) ))



setattr( process, 'ak8PFJets',                   ak4PFJets.clone( src = 'packedPFCandidates',
                                                        rParam = 0.8,
                                                        jetAlgorithm = 'AntiKt' ) )


addJetCollection(               process,
                                labelName = 'AK8Gen',
                                jetSource = cms.InputTag('ak8GenJetsNoNu'),#ak8PFJetsPuppi'),
                                #jetSource = cms.InputTag('ak8PFJetsPuppi'),
                                postfix = '',
                                algo = 'ak8',
                                rParam = 0.8,
                                jetCorrections =  None,
                                pfCandidates = cms.InputTag( pfCand ),
                                svSource = cms.InputTag( svLabel ),
                                genJetCollection = cms.InputTag('ak8GenJetsNoNu'),
                                pvSource = cms.InputTag( pvLabel ),
                                muSource = cms.InputTag( muLabel ),
                                elSource = cms.InputTag( elLabel ),
                                btagDiscriminators = listBtagDiscriminatorsAK8,
                                btagInfos = None,
                                getJetMCFlavour = True,
                                genParticles = cms.InputTag(genParticlesLabel),
                                outputModules = ['outputFile']
                                )






setattr( process, 'ak8GenJetConstituents', cms.EDProducer("PFJetConstituentSelector", src = cms.InputTag('ak8GenJetsNoNu' ), cut = cms.string( '' ) ))

setattr( process, 'ak8GenJetsSoftDrop',
                        ak8PFJetsCHSSoftDrop.clone(
                                src = cms.InputTag('ak8GenJetConstituents:constituents'),
                                rParam = 0.8,
                                jetAlgorithm = 'AntiKt',
                                useExplicitGhosts=True,
                                R0= cms.double(0.8),
                                zcut=0.1,
                                beta=0.0,
                                doAreaFastjet = cms.bool(True),
                                writeCompound = cms.bool(True),
                                jetCollInstanceName=cms.string('SubJets') ) )


setattr( process, 'ak8GenJetsSoftDropMass',
                        ak8PFJetsCHSSoftDropMass.clone( src = cms.InputTag( 'ak8GenJetsNoNu' ),
                                matched = cms.InputTag( 'ak8GenJetsSoftDrop'),
                                distMax = cms.double( 0.8 ) ) )


#getattr(process,'patJetsAK8Gen').addTagInfos = cms.bool(True)

#getattr( process, 'patJetsAK8Gen').userData.userFloats.src += ['ak8GenJetsSoftDropMass']
#                toolsUsed.append( jetalgo+'PFJets'+PUMethod+postFix+'SoftDropMass' )

'''

from JMEAnalysis.JetToolbox.jetToolbox_cffBackUp import jetToolbox
#jetToolbox( process, 'ak8', 'jetSequence', 'out', PUMethod='CHS',JETCorrLevels = [ 'None' ],
#subJETCorrLevels = [ 'None' ], miniAOD=True,runOnMC=True)
#jetToolbox( process, 'ak8', 'jetSequence', 'out', PUMethod='Puppi', miniAOD=True,runOnMC=True, JETCorrPayload= 'None')



SoftDrop_=True
Trimming_=True
Pruning_=True
Nsub_=True
CMSTopTagger_=False;
puMethod_='Puppi'
runOnminiAOD_=True



jetToolbox( process, 'ak8', 'jetSequence', 'out', PUMethod='CHS', miniAOD=runOnminiAOD_,runOnMC=True,addSoftDrop=SoftDrop_, addSoftDropSubjets=SoftDrop_,addTrimming=Trimming_,addPruning=Pruning_,addPrunedSubjets=Pruning_,addNsub=Nsub_,addCMSTopTagger=False)
jetToolbox( process, 'ak8', 'jetSequence', 'out', PUMethod='Puppi',JETCorrLevels = [  'None' ],subJETCorrLevels = [ 'None' ],JETCorrPayload='None',subJETCorrPayload='None', miniAOD=runOnminiAOD_,runOnMC=True,addSoftDrop=SoftDrop_, addSoftDropSubjets=SoftDrop_,addTrimming=Trimming_,addPruning=Pruning_,addPrunedSubjets=Pruning_,addNsub=Nsub_,addNsubSubjets = True,
  subjetMaxTau = 3)





process.AK8Jets = cms.EDProducer("JetProducer",
    #AK8PFJetTag = cms.InputTag("slimmedJetsAK8")#collection by jetToolBox selectedPatJetsAK8PFCHS
    #AK8PFJetTag = cms.InputTag("selectedPatJetsAK8PFCHS")
    AK8PFJetTag =cms.InputTag("selectedPatJetsAK8PFPuppi")
    )


process.TreeMaker = cms.EDProducer(
'TreeMaker',
# Name of the output tree
TreeName          = cms.string('RA2Tree'),
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
VectorRecoCand = cms.vstring()#"AK8Jets:AK8PFJet(AK8PFJets)"),
)



#VectorDouble.extend(['AK8Jets:AK8PFMass(AK8PFJetMass)'])

#VectorDouble=cms.vstring(),#"AK8Jets:AK8PFMass(AK8PFJetMass)"),

process.TestProd = cms.EDProducer("GoodJetProducer",
JMTag = cms.InputTag("AK8Jets:AK8PFMass")

)

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
