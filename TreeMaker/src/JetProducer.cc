// -*- C++ -*-
//
// Package:    Analysis/JetProducer
// Class:      JetProducer
// 
/**\class JetProducer JetProducer.cc Analysis/JetProducer/plugins/JetProducer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  bibhuprasad mahakud
//         Created:  Sat, 13 May 2017 12:41:37 GMT
//
//


// system include files
#include "DataFormats/JetReco/interface/Jet.h"

#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "PhysicsTools/PatAlgos/plugins/PATJetProducer.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"

#include <memory>
#include <iostream>    
#include <algorithm>   
#include <bitset>   

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/StreamID.h"


// DataFormats
#include "DataFormats/JetReco/interface/GenJet.h"
#include "DataFormats/JetReco/interface/PFJet.h"
#include "DataFormats/JetReco/interface/PFJetCollection.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/Common/interface/ValueMap.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"

// TFileService
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

// Gen particle
#include "DataFormats/PatCandidates/interface/PackedGenParticle.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

// JEC
#include "CondFormats/JetMETObjects/interface/JetCorrectorParameters.h"
#include "CondFormats/JetMETObjects/interface/FactorizedJetCorrector.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectionUncertainty.h"

// JER
#include "JetMETCorrections/Modules/interface/JetResolution.h"

// Electron
#include "DataFormats/EgammaCandidates/interface/GsfElectron.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/EgammaCandidates/interface/ConversionFwd.h"
#include "DataFormats/EgammaCandidates/interface/Conversion.h"
#include "RecoEgamma/EgammaTools/interface/ConversionTools.h"
#include "DataFormats/PatCandidates/interface/VIDCutFlowResult.h"

// Trigger
#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"
#include "DataFormats/PatCandidates/interface/PackedTriggerPrescales.h"

// Vertex
#include "DataFormats/VertexReco/interface/Vertex.h"

// Pileup
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"

// LHE weights
#include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

// Utilities
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/deltaPhi.h"

#include "TLorentzVector.h"
#include "FWCore/ParameterSet/interface/FileInPath.h"

//
// class declaration
//

class JetProducer : public edm::stream::EDProducer<> {
   public:
      explicit JetProducer(const edm::ParameterSet&);
      ~JetProducer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

   private:
      virtual void beginStream(edm::StreamID) override;
      virtual void produce(edm::Event&, const edm::EventSetup&) override;
      virtual void endStream() override;

      //virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
      //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

      // ----------member data ---------------------------
      edm::InputTag AK8PFCHSJetTag_;
      edm::InputTag AK8PFPuppiJetTag_;
      edm::InputTag AK8PFPuppiSubJetTag_;
      edm::InputTag AK8GenJetTag_;
      edm::InputTag prunedGenTag_;
      edm::InputTag vtxTag_;
      edm::InputTag rhoTag_;
      edm::InputTag SDGenTag;

      std::string jetCollection; // name of jet collection
      edm::EDGetTokenT<std::vector<reco::GenJet>> jetCollection_;

      //edm::EDGetTokenT<pat::JetCollection> ak8CHSSoftDropSubjetsToken_;
      //edm::EDGetTokenT<pat::JetCollection> ak8PuppiSoftDropSubjetsToken_; 

      std::vector<std::string>  jecPayloadsAK4chs_;
      std::vector<std::string>  jecPayloadsAK8chs_;
      std::vector<std::string>  jecPayloadsAK4pup_;
      std::vector<std::string> jecPayloadsAK8pup_;

      boost::shared_ptr<FactorizedJetCorrector>   JetCorrectorAK4chs;
      boost::shared_ptr<FactorizedJetCorrector>   JetCorrectorAK8chs;
      boost::shared_ptr<FactorizedJetCorrector>   JetCorrectorAK4pup;
      boost::shared_ptr<FactorizedJetCorrector>   JetCorrectorAK4pupSD;
      boost::shared_ptr<FactorizedJetCorrector>   JetCorrectorAK8pup;
      boost::shared_ptr<JetCorrectionUncertainty> JetCorrUncertAK4chs;
      boost::shared_ptr<JetCorrectionUncertainty> JetCorrUncertAK8chs;
      boost::shared_ptr<JetCorrectionUncertainty> JetCorrUncertAK4pup;
      boost::shared_ptr<JetCorrectionUncertainty> JetCorrUncertAK8pup;



      edm::EDGetTokenT<edm::View<pat::Jet>> AK8PFCHSJetTok_;
      edm::EDGetTokenT<edm::View<pat::Jet>> AK8PFPuppiJetTok_;
      edm::EDGetTokenT<edm::View<pat::Jet>> AK8PFPuppiSubjetTok_;
      edm::EDGetTokenT<std::vector<reco::GenJet>> AK8GenJetTok_;
      edm::EDGetTokenT<edm::View<reco::GenParticle>> prunedGenTok_;
      edm::EDGetTokenT<std::vector<reco::Vertex>> vtxTok_; 
      edm::EDGetTokenT<double> rhoTok_;
      bool TurnOnSoftdrop_,TurnOnTrimming_, TurnOnPruning_, TurnOnNsub_,TurnOnCMSTopTagger_;


     double puppi_pt; 
     double puppi_mass;
     double puppi_eta;
     double puppi_phi; 
     double puppi_area; 
     double puppi_energy;


     double puppi_prunedMass;
     double puppi_trimmedMass;
     double puppi_softDropMass;
     double puppi_tau1;
     double puppi_tau2;
     double puppi_tau3;
     double  puppi_tau4; 
     double puppi_NHF;
     double puppi_NEMF;
     double puppi_CHF;
     double puppi_MUF;
     double puppi_CEMF;
     double puppi_NumConst;
     double puppi_NM;
     double puppi_CM;








      int count_all_subjets;// =0;
      int count_matched_subjets;// =0;
      double closest_DR;// = 99;
      double closest_i;// = -1;
      double second_closest_DR;// = 99;
      double second_closest_i;//  = -1;
      int nsubjets_pup;
      double rho;
      int nvtx;
      double subjet_corr_factor_L23res_full;

        double subjetPt;
        double subjetEta;
        double subjetPhi;
        double subjetMass;
        double subjetBdisc;

        double gensubjetpt;

    int count_pupsubjet;
    double pup0_area;
    double pup0_tau1;
    double pup0_tau2;
    double pup0_tau3;
    double pup0_flav_hadron;
    double pup0_flav_parton;
    double pup0_bdisc;
    double pup0_genpt;
    double pup1_area;
    double pup1_tau1;
    double pup1_tau2;
    double pup1_tau3;
    double puppi_tau21;
    double puppi_tau32;

    double pup1_flav_hadron;
    double pup1_flav_parton;
    double pup1_bdisc;
    double pup1_genpt;
    double mostMassiveSDPUPPIsubjetMass;

    double pup_maxbdisc;
    double pup_maxbdiscflav_hadron;
    double pup_maxbdiscflav_parton;


     //////////////Jet 1 stuff

    double Jet1SDmass_doble; 
    double Jet1SDmassSubjetCorrL23_doble; 
    double Jet1SDmassSubjetCorrL123_doble; 
    double Jet1MassPruned_doble; 
    double Jet1MassTrimmed_doble; 
    double Jet1Tau1_doble; 
    double Jet1Tau2_doble; 
    double Jet1Tau3_doble; 
    double Jet1Tau4_doble; 
    double Jet1Tau32_doble; 
    double Jet1Tau21_doble; 
    double Jet1SDsubjet0bdisc_doble; 
    double Jet1SDsubjet1bdisc_doble; 
    double Jet1SDmaxbdisc_doble;
    double Jet1SDmaxbdiscflavHadron_doble;   
    double Jet1SDmaxbdiscflavParton_doble; 
    double Jet1SDsubjet0area_doble; 
    double Jet1SDsubjet0flavHadron_doble; 
    double Jet1SDsubjet0flavParton_doble; 
    double Jet1SDsubjet0matchedgenjetpt_doble; 
    double Jet1SDsubjet0tau1_doble; 
    double Jet1SDsubjet0tau2_doble; 
    double Jet1SDsubjet0tau3_doble; 
    double Jet1SDsubjet1area_doble; 
    double Jet1SDsubjet1flavHadron_doble; 
    double Jet1SDsubjet1flavParton_doble;
    double Jet1SDsubjet1matchedgenjetpt_doble; 
    double Jet1SDsubjet1tau1_doble; 
    double Jet1SDsubjet1tau2_doble; 
    double Jet1SDsubjet1tau3_doble; 
    double Jet1CHF_doble; 
    double Jet1NHF_doble; 
    double Jet1CM_doble; 
    double Jet1NM_doble; 
    double Jet1NEF_doble; 
    double Jet1CEF_doble; 
    double Jet1MF_doble; 
    double Jet1Mult_doble; 
    int Jet1NsubjetsSD_integer; 
    double Jet1GenMatched_bPt_doble; 
    double Jet1GenMatched_WPt_doble; 
    double Jet1GenMatched_Wd1Pt_doble; 
    double Jet1GenMatched_Wd2Pt_doble; 
    double Jet1GenMatched_Wd1ID_doble; 
    double Jet1GenMatched_Wd2ID_doble; 

   ////Jet 0 stuff

    double Jet0SDmass_doble; 
    double Jet0SDmassSubjetCorrL23_doble; 
    double Jet0SDmassSubjetCorrL123_doble; 
    double Jet0MassPruned_doble; 
    double Jet0MassTrimmed_doble; 
    double Jet0Tau1_doble; 
    double Jet0Tau2_doble; 
    double Jet0Tau3_doble; 
    double Jet0Tau4_doble; 
    double Jet0Tau32_doble; 
    double Jet0Tau21_doble; 
    double Jet0SDsubjet0bdisc_doble; 
    double Jet0SDsubjet1bdisc_doble; 
    double Jet0SDmaxbdisc_doble;
    double Jet0SDmaxbdiscflavHadron_doble;   
    double Jet0SDmaxbdiscflavParton_doble; 
    double Jet0SDsubjet0area_doble; 
    double Jet0SDsubjet0flavHadron_doble; 
    double Jet0SDsubjet0flavParton_doble; 
    double Jet0SDsubjet0matchedgenjetpt_doble; 
    double Jet0SDsubjet0tau1_doble; 
    double Jet0SDsubjet0tau2_doble; 
    double Jet0SDsubjet0tau3_doble; 
    double Jet0SDsubjet1area_doble; 
    double Jet0SDsubjet1flavHadron_doble; 
    double Jet0SDsubjet1flavParton_doble;
    double Jet0SDsubjet1matchedgenjetpt_doble; 
    double Jet0SDsubjet1tau1_doble; 
    double Jet0SDsubjet1tau2_doble; 
    double Jet0SDsubjet1tau3_doble; 
    double Jet0CHF_doble; 
    double Jet0NHF_doble; 
    double Jet0CM_doble; 
    double Jet0NM_doble; 
    double Jet0NEF_doble; 
    double Jet0CEF_doble; 
    double Jet0MF_doble; 
    double Jet0Mult_doble; 
    int Jet0NsubjetsSD_integer; 
    double Jet0GenMatched_bPt_doble; 
    double Jet0GenMatched_WPt_doble; 
    double Jet0GenMatched_Wd1Pt_doble; 
    double Jet0GenMatched_Wd2Pt_doble; 
    double Jet0GenMatched_Wd1ID_doble; 
    double Jet0GenMatched_Wd2ID_doble;

    double Jet0L2Corr;
    double Jet1L2Corr;

   float corr_factorAK4pup_L1;
   float corr_factorAK4pup_L12;

    int numJets;
    // int numJCounter;


};

//
// constants, enums and typedefs
//


//
// static data member definitions
//

//
// constructors and destructor
//
JetProducer::JetProducer(const edm::ParameterSet& iConfig)
{
   //register your products
  jetCollection =iConfig.getUntrackedParameter<std::string>("jetCollection");  
  TurnOnSoftdrop_ = iConfig.getParameter <bool> ("TurnOnSoftdrop");
  TurnOnTrimming_ = iConfig.getParameter <bool> ("TurnOnTrimming");
  TurnOnPruning_ = iConfig.getParameter <bool> ("TurnOnPruning");
  TurnOnNsub_ = iConfig.getParameter <bool> ("TurnOnNsub");
  TurnOnCMSTopTagger_ = iConfig.getParameter <bool> ("TurnOnCMSTopTagger");
  AK8PFCHSJetTag_ = iConfig.getParameter<edm::InputTag >("AK8PFCHSJetTag");
  AK8PFPuppiJetTag_ = iConfig.getParameter<edm::InputTag >("AK8PFPuppiJetTag");

  AK8PFPuppiSubJetTag_ = iConfig.getParameter<edm::InputTag >("AK8PFPuppiSubjetTag");


  AK8GenJetTag_ = iConfig.getParameter<edm::InputTag >("AK8GenJetTag");
  prunedGenTag_ = iConfig.getParameter<edm::InputTag>("prunedGenParticles");
  vtxTag_ = iConfig.getParameter<edm::InputTag>("vertexTag");
  rhoTag_ = iConfig.getParameter<edm::InputTag>("rhoTag");

  //jetCollection_ = consumes<std::vector<reco::GenJet>>(jetCollection);

  AK8PFCHSJetTok_ = consumes<edm::View<pat::Jet>>(AK8PFCHSJetTag_);
  AK8PFPuppiJetTok_ = consumes<edm::View<pat::Jet>>(AK8PFPuppiJetTag_);
  AK8PFPuppiSubjetTok_ = consumes<edm::View<pat::Jet>>(AK8PFPuppiSubJetTag_);

  AK8GenJetTok_ = consumes<std::vector<reco::GenJet>>(AK8GenJetTag_);
  prunedGenTok_ = consumes<edm::View<reco::GenParticle>>(prunedGenTag_);
  vtxTok_ = consumes<std::vector<reco::Vertex>>(vtxTag_);
  rhoTok_= consumes<double>(rhoTag_); 

  jecPayloadsAK4chs_= iConfig.getParameter<std::vector<std::string> >  ("jecPayloadsAK4chs");
  jecPayloadsAK8chs_= iConfig.getParameter<std::vector<std::string> >  ("jecPayloadsAK8chs");
  jecPayloadsAK4pup_ = iConfig.getParameter<std::vector<std::string> >  ("jecPayloadsAK4pup");
  jecPayloadsAK8pup_ = iConfig.getParameter<std::vector<std::string> > ("jecPayloadsAK8pup");


  //produces<std::vector<Jet> >();
  produces<std::vector<TLorentzVector> > ("AK8PFCHSJet");
  produces<std::vector<TLorentzVector> > ("AK8PFPuppiJetUncorr");
  produces<std::vector<TLorentzVector> > ("AK8PFPuppiJet");
  produces<std::vector<TLorentzVector> > ("AK8PFSDPuppiJet");
  produces<std::vector<TLorentzVector> > ("AK8PFPuppiJetGenMatched");
  produces<std::vector<int> > ("AK8PFPuppiJetID");  
  //////////////////////////////////////
  // Jet 0
  //
  ///////////////////////////////////////
  produces<std::vector<TLorentzVector> >("Jet0Raw");
  produces<std::vector<TLorentzVector> >("Jet0");
  produces<std::vector<TLorentzVector> >("Jet0SD");
  produces<std::vector<TLorentzVector>>("Jet0SDRaw");
  produces<std::vector<TLorentzVector>>("Jet0SDsubjet0"); 
  produces<std::vector<TLorentzVector>>("Jet0SDsubjet1");
  produces<std::vector<TLorentzVector>>("Jet0MatchedGenJet");
  produces<std::vector<TLorentzVector>>("Jet0MatchedTopHadronic");
  produces<std::vector<double>>("Jet0Area");

  produces<double>("Jet0L2RelativeCorr");
  produces<double>("Jet1L2RelativeCorr");

  produces<double>("Jet0SDmass");
  produces<double>("Jet0SDmassSubjetCorrL23");
  produces<double>("Jet0SDmassSubjetCorrL123");
  produces<double>("Jet0MassPruned");  
  produces<double>("Jet0MassTrimmed");
  produces<double>("Jet0Tau1"); 
  produces<double>("Jet0Tau2");
  produces<double>("Jet0Tau3");
  produces<double>("Jet0Tau4");
  produces<double>("Jet0Tau32");
  produces<double>("Jet0Tau21");
  produces<double>("Jet0SDsubjet0bdisc");
  produces<double>("Jet0SDsubjet1bdisc");
  produces<double>("Jet0SDmaxbdisc");
  produces<double>("Jet0SDmaxbdiscflavHadron");                  
  produces<double>("Jet0SDmaxbdiscflavParton");                  
  produces<double>("Jet0SDsubjet0area");                         
  produces<double>("Jet0SDsubjet0flavHadron");                   
  produces<double>("Jet0SDsubjet0flavParton");                   
  produces<double>("Jet0SDsubjet0matchedgenjetpt");              
  produces<double>("Jet0SDsubjet0tau1");                         
  produces<double>("Jet0SDsubjet0tau2");                         
  produces<double>("Jet0SDsubjet0tau3");                         
  produces<double>("Jet0SDsubjet1area");                         
  produces<double>("Jet0SDsubjet1flavHadron");                   
  produces<double>("Jet0SDsubjet1flavParton");                   
  produces<double>("Jet0SDsubjet1matchedgenjetpt");              
  produces<double>("Jet0SDsubjet1tau1");                         
  produces<double>("Jet0SDsubjet1tau2");                         
  produces<double>("Jet0SDsubjet1tau3");
  produces<double>("Jet0CHF");                                   
  produces<double>("Jet0NHF");                                   
  produces<double>("Jet0CM");                                    
  produces<double>("Jet0NM");                                    
  produces<double>("Jet0NEF");                                   
  produces<double>("Jet0CEF");                                   
  produces<double>("Jet0MF");                                    
  produces<double>("Jet0Mult"); 
  produces<int>("Jet0NsubjetsSD");
  produces<double>("Jet0GenMatchedbPt");
  produces<double>("Jet0GenMatchedWPt"); 
  produces<double>("Jet0GenMatchedWd1Pt");
  produces<double>("Jet0GenMatchedWd2Pt");
  produces<double>("Jet0GenMatchedWd1ID");
  produces<double>("Jet0GenMatchedWd2ID");

  //////////////////////////////////////
  // Jet 1
  //
  ///////////////////////////////////////



  produces<std::vector<TLorentzVector> >("Jet1Raw");
  produces<std::vector<TLorentzVector> >("Jet1");
  produces<std::vector<TLorentzVector> >("Jet1SD");
  produces<std::vector<double>>("Jet1Area");
  produces<std::vector<TLorentzVector>>("Jet1SDRaw");
  produces<std::vector<TLorentzVector>>("Jet1SDsubjet0");
  produces<std::vector<TLorentzVector>>("Jet1SDsubjet1");
  produces<std::vector<TLorentzVector>>("Jet1MatchedGenJet");
  produces<std::vector<TLorentzVector>>("Jet1MatchedTopHadronic");



  produces<double>("Jet1SDmass");
  produces<double>("Jet1SDmassSubjetCorrL23");
  produces<double>("Jet1SDmassSubjetCorrL123");
  produces<double>("Jet1MassPruned");
  produces<double>("Jet1MassTrimmed");
  produces<double>("Jet1Tau1");
  produces<double>("Jet1Tau2");
  produces<double>("Jet1Tau3");
  produces<double>("Jet1Tau4");
  produces<double>("Jet1Tau32");
  produces<double>("Jet1Tau21");
  produces<double>("Jet1SDsubjet0bdisc");
  produces<double>("Jet1SDsubjet1bdisc");
  produces<double>("Jet1SDmaxbdisc");
  produces<double>("Jet1SDmaxbdiscflavHadron");
  produces<double>("Jet1SDmaxbdiscflavParton");
  produces<double>("Jet1SDsubjet0area");
  produces<double>("Jet1SDsubjet0flavHadron");
  produces<double>("Jet1SDsubjet0flavParton");
  produces<double>("Jet1SDsubjet0matchedgenjetpt");
  produces<double>("Jet1SDsubjet0tau1");
  produces<double>("Jet1SDsubjet0tau2");
  produces<double>("Jet1SDsubjet0tau3");
  produces<double>("Jet1SDsubjet1area");
  produces<double>("Jet1SDsubjet1flavHadron");
  produces<double>("Jet1SDsubjet1flavParton");
  produces<double>("Jet1SDsubjet1matchedgenjetpt");
  produces<double>("Jet1SDsubjet1tau1");
  produces<double>("Jet1SDsubjet1tau2");
  produces<double>("Jet1SDsubjet1tau3");
  produces<double>("Jet1CHF");
  produces<double>("Jet1NHF");
  produces<double>("Jet1CM");
  produces<double>("Jet1NM");
  produces<double>("Jet1NEF");
  produces<double>("Jet1CEF");
  produces<double>("Jet1MF");
  produces<double>("Jet1Mult");
  produces<int>("Jet1NsubjetsSD");
  produces<double>("Jet1GenMatchedbPt");
  produces<double>("Jet1GenMatchedWPt");
  produces<double>("Jet1GenMatchedWd1Pt");
  produces<double>("Jet1GenMatchedWd2Pt");
  produces<double>("Jet1GenMatchedWd1ID");
  produces<double>("Jet1GenMatchedWd2ID");





  ///////////////////////Extra stuff






  produces<std::vector<reco::GenJet> > ("AK8GenJet");
  produces<std::vector<TLorentzVector>>("AK8GenJets");
  produces<std::vector<double> > ("AK8PFPuppiTrimmedMass");
  produces<std::vector<double> > ("AK8PFPuppiPrunedMass");
  produces<std::vector<double> > ("AK8PFPuppiSoftdropMass");
  produces<std::vector<double> > ("AK8PFPuppitau1");
  produces<std::vector<double> > ("AK8PFPuppitau2");
  produces<std::vector<double> > ("AK8PFPuppitau3");

  produces<std::vector<double> > ("AK8puppiNHEF");
  produces<std::vector<double> > ("AK8puppiNEmEF");
  produces<std::vector<double> > ("AK8puppiCHF");
  produces<std::vector<double> > ("AK8puppimuEF");
  produces<std::vector<double> > ("AK8puppiCEmF");
  produces<std::vector<double> > ("AK8puppiNumConst");
  produces<std::vector<double> > ("AK8puppiNMultiplicity");
  produces<std::vector<double> > ("AK8puppiCMultiplicity");  


   produces<int>("numAK8puppiJets");




/* Examples
   produces<ExampleData2>();

   //if do put with a label
   produces<ExampleData2>("label");
 
   //if you want to put into the Run
   produces<ExampleData2,InRun>();
*/
   //now do what ever other initialization is needed
  
}


JetProducer::~JetProducer()
{
 
   // do anything here that needs to be done at destruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
JetProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   using namespace std;
   using namespace reco;
   using namespace pat;

 

  //std::cout<<"Event "<<std::endl;

   /*
   Handle< View<reco::GenJet> > jetCands;
   iEvent.getByToken(jetCollection_,jetCands);

   for(View<reco::GenJet>::const_iterator iJet = jetCands->begin();
      iJet != jetCands->end();
      ++iJet){

   std::cout << "std jet pt: " << iJet->pt() << std::endl;

     }
    */

   auto AK8PFCHSJet_vec = std::make_unique<std::vector<TLorentzVector>>();
   auto AK8PFPuppiJetsUncorr_vec = std::make_unique<std::vector<TLorentzVector>>();
   auto AK8PFPuppiJets_vec = std::make_unique<std::vector<TLorentzVector>>();
   auto AK8PFSDPuppiJets_vec = std::make_unique<std::vector<TLorentzVector>>();
   auto AK8PFPuppiJetID_vec = std::make_unique<std::vector<int>>();
   auto AK8PFPuppiGenMatched_vec = std::make_unique<std::vector<TLorentzVector>>();
   auto AK8GenJets_vec = std::make_unique<std::vector<reco::GenJet>>();
   auto AK8GenJetss_vec = std::make_unique<std::vector<TLorentzVector>>();
   auto AK8PFPuppiTrimMass_vec = std::make_unique<std::vector<double>>();
   auto AK8PFPuppiPrunMass_vec = std::make_unique<std::vector<double>>();
   auto AK8PFPuppiSoftdropMass_vec = std::make_unique<std::vector<double>>();
   auto AK8PFPuppitau1_vec = std::make_unique<std::vector<double>>();
   auto AK8PFPuppitau2_vec = std::make_unique<std::vector<double>>();
   auto AK8PFPuppitau3_vec = std::make_unique<std::vector<double>>();
   auto AK8PFPuppiNHEF_vec = std::make_unique<std::vector<double>>();  
   auto AK8PFPuppiNEmEF_vec = std::make_unique<std::vector<double>>();
   auto AK8PFPuppiCHF_vec = std::make_unique<std::vector<double>>();
   auto AK8PFPuppimuEF_vec = std::make_unique<std::vector<double>>();
   auto AK8PFPuppiCEmF_vec = std::make_unique<std::vector<double>>();
   auto AK8PFPuppiNumConst_vec = std::make_unique<std::vector<double>>();
   auto AK8PFPuppiNMulti_vec = std::make_unique<std::vector<double>>();
   auto AK8PFPuppiCMulti_vec = std::make_unique<std::vector<double>>();

   ///////////////////Jet1 stuff

   auto Jet1Raw_vec = std::make_unique<std::vector<TLorentzVector>>();
   auto Jet1_vec = std::make_unique<std::vector<TLorentzVector>>();
   auto Jet1SD_vec = std::make_unique<std::vector<TLorentzVector>>();
   auto Jet1Area_dob = std::make_unique<std::vector<double>>();
   auto Jet1SDRaw_vec = std::make_unique<std::vector<TLorentzVector>>();
   auto Jet1SDsubjet0_vec = std::make_unique<std::vector<TLorentzVector>>();
   auto Jet1SDsubjet1_vec = std::make_unique<std::vector<TLorentzVector>>();
   auto Jet1MatchedGenJet_vec = std::make_unique<std::vector<TLorentzVector>>();
   auto Jet1MatchedTopHadronic_vec = std::make_unique<std::vector<TLorentzVector>>();

     numJets=0;
     Jet1SDmass_doble=-99; 
     Jet1SDmassSubjetCorrL23_doble=-99; 
     Jet1SDmassSubjetCorrL123_doble=-99; 
     Jet1MassPruned_doble=-99; 
     Jet1MassTrimmed_doble=-99; 
     Jet1Tau1_doble=-99; 
     Jet1Tau2_doble=-99; 
     Jet1Tau3_doble=-99; 
     Jet1Tau4_doble=-99; 
     Jet1Tau32_doble=-99; 
     Jet1Tau21_doble=-99; 
     Jet1SDsubjet0bdisc_doble=-99; 
     Jet1SDsubjet1bdisc_doble=-99; 
     Jet1SDmaxbdisc_doble=-99;
     Jet1SDmaxbdiscflavHadron_doble=-99;   
     Jet1SDmaxbdiscflavParton_doble=-99; 
     Jet1SDsubjet0area_doble=-99; 
     Jet1SDsubjet0flavHadron_doble=-99; 
     Jet1SDsubjet0flavParton_doble=-99; 
     Jet1SDsubjet0matchedgenjetpt_doble=-99; 
     Jet1SDsubjet0tau1_doble=-99; 
     Jet1SDsubjet0tau2_doble=-99; 
     Jet1SDsubjet0tau3_doble=-99; 
     Jet1SDsubjet1area_doble=-99; 
     Jet1SDsubjet1flavHadron_doble=-99; 
     Jet1SDsubjet1flavParton_doble=-99;
     Jet1SDsubjet1matchedgenjetpt_doble=-99; 
     Jet1SDsubjet1tau1_doble=-99; 
     Jet1SDsubjet1tau2_doble=-99; 
     Jet1SDsubjet1tau3_doble=-99; 
     Jet1CHF_doble=-99; 
     Jet1NHF_doble=-99; 
     Jet1CM_doble=-99; 
     Jet1NM_doble=-99; 
     Jet1NEF_doble=-99; 
     Jet1CEF_doble=-99; 
     Jet1MF_doble=-99; 
     Jet1Mult_doble=-99; 
     Jet1NsubjetsSD_integer=-99; 
     Jet1GenMatched_bPt_doble=-99; 
     Jet1GenMatched_WPt_doble=-99; 
     Jet1GenMatched_Wd1Pt_doble=-99; 
     Jet1GenMatched_Wd2Pt_doble=-99; 
     Jet1GenMatched_Wd1ID_doble=-9999; 
     Jet1GenMatched_Wd2ID_doble=-9999;






   //Jet 0 stuff



   auto Jet0Raw_vec = std::make_unique<std::vector<TLorentzVector>>();
   auto Jet0_vec = std::make_unique<std::vector<TLorentzVector>>();
   auto Jet0SD_vec = std::make_unique<std::vector<TLorentzVector>>();
   auto Jet0Area_dob = std::make_unique<std::vector<double>>();
   auto Jet0SDRaw_vec = std::make_unique<std::vector<TLorentzVector>>();
   auto Jet0SDsubjet0_vec = std::make_unique<std::vector<TLorentzVector>>();
   auto Jet0SDsubjet1_vec = std::make_unique<std::vector<TLorentzVector>>();
   auto Jet0MatchedGenJet_vec = std::make_unique<std::vector<TLorentzVector>>();
   auto Jet0MatchedTopHadronic_vec = std::make_unique<std::vector<TLorentzVector>>();

     Jet0SDmass_doble=-99; 
     Jet0SDmassSubjetCorrL23_doble=-99; 
     Jet0SDmassSubjetCorrL123_doble=-99; 
     Jet0MassPruned_doble=-99; 
     Jet0MassTrimmed_doble=-99; 
     Jet0Tau1_doble=-99; 
     Jet0Tau2_doble=-99; 
     Jet0Tau3_doble=-99; 
     Jet0Tau4_doble=-99; 
     Jet0Tau32_doble=-99; 
     Jet0Tau21_doble=-99; 
     Jet0SDsubjet0bdisc_doble=-99; 
     Jet0SDsubjet1bdisc_doble=-99; 
     Jet0SDmaxbdisc_doble=-99;
     Jet0SDmaxbdiscflavHadron_doble=-99;   
     Jet0SDmaxbdiscflavParton_doble=-99; 
     Jet0SDsubjet0area_doble=-99; 
     Jet0SDsubjet0flavHadron_doble=-99; 
     Jet0SDsubjet0flavParton_doble=-99; 
     Jet0SDsubjet0matchedgenjetpt_doble=-99; 
     Jet0SDsubjet0tau1_doble=-99; 
     Jet0SDsubjet0tau2_doble=-99; 
     Jet0SDsubjet0tau3_doble=-99; 
     Jet0SDsubjet1area_doble=-99; 
     Jet0SDsubjet1flavHadron_doble=-99; 
     Jet0SDsubjet1flavParton_doble=-99;
     Jet0SDsubjet1matchedgenjetpt_doble=-99; 
     Jet0SDsubjet1tau1_doble=-99; 
     Jet0SDsubjet1tau2_doble=-99; 
     Jet0SDsubjet1tau3_doble=-99; 
     Jet0CHF_doble=-99; 
     Jet0NHF_doble=-99; 
     Jet0CM_doble=-99; 
     Jet0NM_doble=-99; 
     Jet0NEF_doble=-99; 
     Jet0CEF_doble=-99; 
     Jet0MF_doble=-99; 
     Jet0Mult_doble=-99; 
     Jet0NsubjetsSD_integer=-99; 
     Jet0GenMatched_bPt_doble=-99; 
     Jet0GenMatched_WPt_doble=-99; 
     Jet0GenMatched_Wd1Pt_doble=-99; 
     Jet0GenMatched_Wd2Pt_doble=-99; 
     Jet0GenMatched_Wd1ID_doble=-9999; 
     Jet0GenMatched_Wd2ID_doble=-9999;

 










 
   bool top1hadronic=false;
   bool top2hadronic=false;
   bool top1leptonic=false;
   bool top2leptonic=false;

   TLorentzVector t1_p4;
   TLorentzVector t2_p4;
   TLorentzVector finalt1_p4;
   TLorentzVector finalt2_p4;
   TLorentzVector b1_p4;
   TLorentzVector b2_p4;
   TLorentzVector W1_p4;
   TLorentzVector W2_p4;
   TLorentzVector W1d1_p4;
   TLorentzVector W1d2_p4;
   TLorentzVector W2d1_p4;
   TLorentzVector W2d2_p4;
   TLorentzVector resonantW1_p4;
   TLorentzVector resonantW2_p4;
   TLorentzVector Resonance_p4;
   TLorentzVector hardest_parton_hardScatterOutgoing_p4;
   TLorentzVector second_hardest_parton_hardScatterOutgoing_p4;

   double hardestpartonhardScatterOutgoingpt = 0;
   double secondhardestpartonhardScatterOutgoingpt = 0;

   int parton1id = 0;
   int parton2id = 0;

   int W1d1_id = 0 ;
   int W1d2_id = 0 ;
   int W2d1_id = 0 ;
   int W2d2_id = 0 ;

   bool GenTruth_allhadronic = false;
   bool GenTruth_semileptonic = false;
   int count_gen_truth_hadronic_top = 0;

   double deltaR_t1_t2       = 99 ;
   double deltaR_t1_b1       = 99 ;
   double deltaR_t1_W1       = 99 ;
   double deltaR_t1_W1d1     = 99 ;
   double deltaR_t1_W1d2     = 99 ;
   double deltaR_W1_b1       = 99 ;
   double deltaR_W1_W1d1     = 99 ;
   double deltaR_W1_W1d2     = 99 ;
   double deltaR_W1d1_W1d2   = 99 ;
   double deltaR_W1d1_b1     = 99 ;
   double deltaR_W1d2_b1     = 99 ;
   double deltaR_t2_b2       = 99 ;
   double deltaR_t2_W2       = 99 ;
   double deltaR_t2_W2d1     = 99 ;
   double deltaR_t2_W2d2     = 99 ;
   double deltaR_W2_b2       = 99 ;
   double deltaR_W2_W2d1     = 99 ;
   double deltaR_W2_W2d2     = 99 ;
   double deltaR_W2d1_W2d2   = 99 ;
   double deltaR_W2d1_b2     = 99 ;
   double deltaR_W2d2_b2     = 99 ;

   double max_deltaR_parton_t1  = -1;
   double max_deltaR_parton_t2  = -1;
   double max_deltaR_Wparton_t1 = -1;
   double max_deltaR_Wparton_t2 = -1;
   double max_deltaR_Wparton_W1 = -1;
   double max_deltaR_Wparton_W2 = -1;

   double counttop = 0;
   Jet0L2Corr=0;  
   Jet1L2Corr=0;

 
   Handle<edm::View<reco::GenParticle> > genpart;
   iEvent.getByToken(prunedGenTok_,genpart);
     
    for(size_t i=0; i<genpart->size();i++){
      if (fabs((*genpart)[i].pdgId())==6 && (*genpart)[i].status()<30 && (*genpart)[i].status()>=20) counttop++;  // Z' events: status 22 = top from Z', status 52 with 2 daughters = the top that decays (after radiating a bunch of times)
    }

    double countW = 0;
    double countb = 0;
    for(size_t i=0; i<genpart->size();i++){//gen particle loop start
      int id        = (*genpart)[i].pdgId();
      int status    = (*genpart)[i].status();
      int ndau      = (*genpart)[i].numberOfDaughters();
      double px     = (*genpart)[i].px();
      double py     = (*genpart)[i].py();
      double pz     = (*genpart)[i].pz();
      double e      = (*genpart)[i].energy();
      double m      = (*genpart)[i].mass();
      double pt     = (*genpart)[i].pt();
      double eta    = (*genpart)[i].eta();
      double phi    = (*genpart)[i].phi();
      // Find the particles from the hard scatter (for QCD samples)

       if(id>1000000 && status == 22){
        Resonance_p4.SetPxPyPzE( px, py, pz, e ); 
        //cout<<"RSG mass: "<<Resonance_p4.M()<<endl;

       }

   }//gen particle loop end






   //AK4puppi JEC
   std::vector<JetCorrectorParameters> vParAK4pup;
   for ( std::vector<std::string>::const_iterator ipayload = jecPayloadsAK4pup_.begin(),
     ipayloadEnd = jecPayloadsAK4pup_.end(); ipayload != ipayloadEnd - 1; ++ipayload ) {

     
     JetCorrectorParameters pars(*ipayload);
     vParAK4pup.push_back(pars);
   }
   JetCorrectorAK4pup   = boost::shared_ptr<FactorizedJetCorrector>  ( new FactorizedJetCorrector(vParAK4pup) );
   JetCorrectorAK4pupSD   = boost::shared_ptr<FactorizedJetCorrector>  ( new FactorizedJetCorrector(vParAK4pup) );

   JetCorrUncertAK4pup = boost::shared_ptr<JetCorrectionUncertainty>( new JetCorrectionUncertainty(jecPayloadsAK4pup_.back()));

   //AK8Puppi JEC
   std::vector<JetCorrectorParameters> vParAK8pup;
   for ( std::vector<std::string>::const_iterator ipayload = jecPayloadsAK8pup_.begin(),
     ipayloadEnd = jecPayloadsAK8pup_.end(); ipayload != ipayloadEnd - 1; ++ipayload ) {

    //std::cout<<"file payload: "<<*ipayload<<std::endl;


     JetCorrectorParameters pars(*ipayload);
     vParAK8pup.push_back(pars);
    }
   JetCorrectorAK8pup   = boost::shared_ptr<FactorizedJetCorrector>  ( new FactorizedJetCorrector(vParAK8pup) );
   JetCorrUncertAK8pup = boost::shared_ptr<JetCorrectionUncertainty>( new JetCorrectionUncertainty(jecPayloadsAK8pup_.back()));

   //double corr = JetCorrectorAK8pup->getCorrection();
   //std::cout<<"correction: "<<corr<<std::endl;

   edm::Handle<edm::View<pat::Jet> > hAK8PFCHS;
   iEvent.getByToken(AK8PFCHSJetTok_, hAK8PFCHS);

   for(const pat::Jet &iak8 : *hAK8PFCHS){

      TLorentzVector tmCHSJet;
      tmCHSJet.SetPtEtaPhiE(iak8.pt(),iak8.eta(),iak8.phi(),iak8.energy());
      if(iak8.pt()>500.0){
       AK8PFCHSJet_vec->push_back(tmCHSJet);

        }


//    std::cout<<"AK8 PFCHS Jet Area: "<<iak8.jetArea()<<std::endl;



    }



   edm::Handle<edm::View<pat::Jet> > AK8PuppiH;
   iEvent.getByToken(AK8PFPuppiJetTok_, AK8PuppiH);

   edm::Handle<edm::View<pat::Jet> > AK8PUPPIsub;
   iEvent.getByToken( AK8PFPuppiSubjetTok_ , AK8PUPPIsub);


   edm::Handle<std::vector<reco::Vertex> > vertices;
   iEvent.getByToken(vtxTok_, vertices);
    nvtx = vertices->size();
   if (vertices->empty()) return; // skip the event if no PV found

   Handle<double> rhoH;
   iEvent.getByToken(rhoTok_, rhoH);
   rho = *rhoH;






   edm::Handle<std::vector<reco::GenJet> > genJetHandle;
   iEvent.getByToken(AK8GenJetTok_, genJetHandle);




   int count_AK8PUPPI = 0;
   TLorentzVector PUPPIjet0_P4;
   TLorentzVector PUPPIjet1_P4;
   TLorentzVector PUPPIjet0_P4corr;
   TLorentzVector PUPPIjet1_P4corr;
   TLorentzVector GenJetMatchedPuppi0;
   TLorentzVector GenJetMatchedPuppi1;
 
   double closestAK8_to_Jet0_dR=99;
   double closestAK8_to_Jet1_dR=99;
   TLorentzVector closestAK8_to_Jet0_P4;
   TLorentzVector closestAK8_to_Jet1_P4;
   double closestAK8_to_Jet0_bdisc=-10;
   double closestAK8_to_Jet1_bdisc=-10;

  // Jet0Raw_vec->SetPxPyPzE(1,2,3,4);

 
   
  
   //int numAK8PFPUPPIJets=0; 
   for(const pat::Jet &ijet : *AK8PuppiH){

     
     puppi_pt             = -99;     
     puppi_mass           = -99;     
     puppi_eta            = -99;  
     puppi_energy         = -99;   
     puppi_phi            = -99;     
     puppi_area           = -99;     
    puppi_tau1           = -99;     
    puppi_tau2           = -99;     
    puppi_tau3           = -99;     
    puppi_tau4           = -99;     
    puppi_prunedMass     = -1;     
    puppi_trimmedMass    = -1;     
    puppi_softDropMass   = -1;     

    TLorentzVector AK8PUPPI_P4uncorr;
    TLorentzVector GenJetMatchedPuppi; 

    puppi_NHF=-99;
    puppi_NEMF=-99;
    puppi_CHF=-99;
    puppi_MUF=-99;
    puppi_CEMF=-99;
    puppi_NumConst=-99;
    puppi_NM=-99;
    puppi_CM=-99;


    



   //comment start
    
    puppi_NHF       = ijet.neutralHadronEnergyFraction();
    puppi_NEMF      = ijet.neutralEmEnergyFraction();
    puppi_CHF       = ijet.chargedHadronEnergyFraction();
    puppi_MUF       = ijet.muonEnergyFraction();
    puppi_CEMF      = ijet.chargedEmEnergyFraction();
    puppi_NumConst  = ijet.chargedMultiplicity()+ijet.neutralMultiplicity();
    puppi_NM        = ijet.neutralMultiplicity();
    puppi_CM        = ijet.chargedMultiplicity(); 
    AK8PFPuppiNHEF_vec->push_back(puppi_NHF);
    AK8PFPuppiNEmEF_vec->push_back(puppi_NEMF);
    AK8PFPuppiCHF_vec->push_back(puppi_CHF);
    AK8PFPuppimuEF_vec->push_back(puppi_MUF);
    AK8PFPuppiCEmF_vec->push_back(puppi_CEMF);    
    AK8PFPuppiNumConst_vec->push_back(puppi_NumConst);
    AK8PFPuppiNMulti_vec->push_back(puppi_NM);
    AK8PFPuppiCMulti_vec->push_back(puppi_CM);

   //std::cout<<"AK8PFPUPPI Area: "<<ijet.jetArea()<<std::endl;


     //double puppi_area         = ijet.jetArea();
     puppi_prunedMass   = ijet.userFloat("ak8PFJetsPuppiPrunedMass");
     puppi_trimmedMass  = ijet.userFloat("ak8PFJetsPuppiTrimmedMass");
     puppi_softDropMass = ijet.userFloat("ak8PFJetsPuppiSoftDropMass");
     puppi_tau1         = ijet.userFloat("NjettinessAK8Puppi:tau1");
     puppi_tau2         = ijet.userFloat("NjettinessAK8Puppi:tau2");
     puppi_tau3         = ijet.userFloat("NjettinessAK8Puppi:tau3");
     puppi_tau4         = ijet.userFloat("NjettinessAK8Puppi:tau4");
   
    double eta = ijet.eta();
    puppi_pt           = ijet.pt();
    puppi_mass         = ijet.mass();
    puppi_eta          = ijet.eta();
    puppi_phi          = ijet.phi();
    puppi_energy  =ijet.energy();
   
   if(puppi_pt<400.0)continue;

   //numJCounter=numJCounter+1; 
   numJets++;

   //bool goodJet_looseJetID=false;

    bool goodJet_looseJetID = ( fabs(eta) <= 2.4 && puppi_NHF < 0.99 && puppi_NEMF < 0.99 && puppi_NumConst >1 && puppi_CHF > 0.0  && puppi_CM > 0 && puppi_CEMF < 0.99   ); 

    const reco::GenJet* genJet = ijet.genJet();
    if(genJet){
      GenJetMatchedPuppi.SetPtEtaPhiM( genJet->pt(), genJet->eta(), genJet->phi(), genJet->mass() );
      AK8PFPuppiGenMatched_vec->push_back(GenJetMatchedPuppi);

       }

      
    AK8PUPPI_P4uncorr.SetPtEtaPhiM(puppi_pt, puppi_eta, puppi_phi, puppi_mass );
    AK8PFPuppiJetsUncorr_vec->push_back(AK8PUPPI_P4uncorr);
    
    if( count_AK8PUPPI==0 ){ 
     Jet0Raw_vec->push_back(AK8PUPPI_P4uncorr);
     GenJetMatchedPuppi0 = GenJetMatchedPuppi;
     Jet0Area_dob->push_back(ijet.jetArea());
     Jet0SDmass_doble=puppi_softDropMass;
     Jet0MassPruned_doble=puppi_prunedMass;
     Jet0MassTrimmed_doble=puppi_trimmedMass;
     Jet0Tau1_doble=puppi_tau1;
     Jet0Tau2_doble=puppi_tau2;
     Jet0Tau3_doble=puppi_tau3;
     Jet0Tau4_doble=puppi_tau4;
     if(puppi_tau2 >0.)Jet0Tau32_doble=puppi_tau3/puppi_tau2;
     if(puppi_tau1 >0.)Jet0Tau21_doble=puppi_tau2/puppi_tau1;
     Jet0CHF_doble=puppi_CHF;
     Jet0NHF_doble=puppi_NHF;
     Jet0CM_doble=puppi_CM;
     Jet0NM_doble=puppi_NM;
     Jet0NEF_doble=puppi_NEMF;
     Jet0CEF_doble=puppi_CEMF;
     Jet0MF_doble=puppi_MUF;
     Jet0Mult_doble=puppi_NumConst;


                           }
    if( count_AK8PUPPI==1 ){
     GenJetMatchedPuppi1 = GenJetMatchedPuppi;
     Jet1Raw_vec->push_back(AK8PUPPI_P4uncorr);
     Jet1Area_dob->push_back(ijet.jetArea());
     Jet1SDmass_doble=puppi_softDropMass;
     Jet1MassPruned_doble =puppi_prunedMass;
     Jet1MassTrimmed_doble=puppi_trimmedMass;
     Jet1Tau1_doble=puppi_tau1;
     Jet1Tau2_doble=puppi_tau2;
     Jet1Tau3_doble=puppi_tau3;
     Jet1Tau4_doble=puppi_tau4;
     if(puppi_tau2 >0.)Jet1Tau32_doble=puppi_tau3/puppi_tau2;
     if(puppi_tau1 >0.)Jet1Tau21_doble=puppi_tau2/puppi_tau1;
     Jet1CHF_doble=puppi_CHF;
     Jet1NHF_doble=puppi_NHF;
     Jet1CM_doble=puppi_CM;
     Jet1NM_doble=puppi_NM;
     Jet1NEF_doble=puppi_NEMF;
     Jet1CEF_doble=puppi_CEMF;
     Jet1MF_doble=puppi_MUF;
     Jet1Mult_doble=puppi_NumConst;



                           }
    
    
    
    puppi_tau21        = 99;
    puppi_tau32        = 99;
    if(puppi_tau1!=0) puppi_tau21 = puppi_tau2/puppi_tau1;
    if(puppi_tau2!=0) puppi_tau32 = puppi_tau3/puppi_tau2;







    //cout<<"goodJetPt: "<<ijet.pt()<<endl;

    
     //reco::Candidate::LorentzVector uncorrJet = ijet.correctedP4(0);
     JetCorrectorAK8pup->setJetEta( puppi_eta);  //uncorrJet.eta() );
     JetCorrectorAK8pup->setJetPt(puppi_pt );// uncorrJet.pt() );
     JetCorrectorAK8pup->setJetE(puppi_energy);// uncorrJet.energy() );
     JetCorrectorAK8pup->setJetA( ijet.jetArea() );
     JetCorrectorAK8pup->setRho( rho );
     JetCorrectorAK8pup->setNPV( nvtx );

     JetCorrectorAK4pupSD->setJetEta( puppi_eta);  //uncorrJet.eta() );
     JetCorrectorAK4pupSD->setJetPt(puppi_pt );// uncorrJet.pt() );
     JetCorrectorAK4pupSD->setJetE(puppi_energy);// uncorrJet.energy() );
     JetCorrectorAK4pupSD->setJetA( ijet.jetArea() );
     JetCorrectorAK4pupSD->setRho( rho );
     JetCorrectorAK4pupSD->setNPV( nvtx );




     //double corr = JetCorrectorAK8pup->getCorrection();
    //cout<<"correction: "<<corr<<endl; 
     //reco::Candidate::LorentzVector corrJet = corr * uncorrJet;
     std::vector<float> factorsAK8pup = JetCorrectorAK8pup->getSubCorrections();
     std::vector<float> factorsAK4pup = JetCorrectorAK4pupSD->getSubCorrections();


     float corr_factorAK8pup_L1      = 1.0;
     float corr_factorAK8pup_L12     = 1.0;
     float corr_factorAK8pup_L123    = 1.0;
     float corr_factorAK8pup_L123res = 1.0;
      corr_factorAK4pup_L1      = 1.0;
      corr_factorAK4pup_L12     = 1.0;
     float corr_factorAK4pup_L123    = 1.0;
     float corr_factorAK4pup_L123res = 1.0;


     if (factorsAK8pup.size() > 0) corr_factorAK8pup_L1       = factorsAK8pup[0];
     if (factorsAK8pup.size() > 1) corr_factorAK8pup_L12      = factorsAK8pup[1];
     if (factorsAK8pup.size() > 2) corr_factorAK8pup_L123     = factorsAK8pup[2];
     if (factorsAK8pup.size() > 3) corr_factorAK8pup_L123res  = factorsAK8pup[3];

     if (factorsAK4pup.size() > 0) corr_factorAK4pup_L1       = factorsAK4pup[0];
     if (factorsAK4pup.size() > 1) corr_factorAK4pup_L12      = factorsAK4pup[1];
     //if (factorsAK4pup.size() > 2) corr_factorAK4pup_L123     = factorsAK4pup[2];
     //if (factorsAK4pup.size() > 3) corr_factorAK4pup_L123res  = factorsAK4pup[3];





     //std::cout<<"L1Puppi Corr: "<<corr_factorAK8pup_L1<<std::endl;
     double corr_factorAK8pup_L2 = corr_factorAK8pup_L12/corr_factorAK8pup_L1;
     double corr_factorAK8pup_L3 = corr_factorAK8pup_L123/corr_factorAK8pup_L12;
     double corr_factorAK8pup_res = corr_factorAK8pup_L123res/corr_factorAK8pup_L123;	

     double corr_factorAK4pup_L2 = corr_factorAK4pup_L12/corr_factorAK4pup_L1;




     double corr_factorAK8pup_L23res = corr_factorAK8pup_L2*corr_factorAK8pup_L3;//corr_factorAK8pup_res;

     TLorentzVector AK8PUPPI_P4corr;
     AK8PUPPI_P4corr = corr_factorAK8pup_L23res *  AK8PUPPI_P4uncorr;




    if(count_AK8PUPPI==0){
     Jet0L2Corr=corr_factorAK4pup_L2;
     PUPPIjet0_P4corr = AK8PUPPI_P4corr;
     Jet0_vec->push_back(AK8PUPPI_P4corr);
     }
    if(count_AK8PUPPI==1){ 
     Jet1L2Corr=corr_factorAK4pup_L2;
     Jet1_vec->push_back(AK8PUPPI_P4corr);
     PUPPIjet1_P4corr = AK8PUPPI_P4corr;
     }


       TLorentzVector sub0_P4_uncorr;
       TLorentzVector sub0_P4_L23res;
       TLorentzVector sub0_P4_L123res;
       TLorentzVector sub1_P4_uncorr;
       TLorentzVector sub1_P4_L23res;
       TLorentzVector sub1_P4_L123res;



       count_all_subjets =0;
       count_matched_subjets =0;
       closest_DR = 99;
       closest_i = -1;
       second_closest_DR = 99;
       second_closest_i  = -1;
   
      
    for (const pat::Jet &isub : *AK8PUPPIsub) { //first subject loop starts
         subjetPt       = isub.pt();//correctedP4(0).pt();
         subjetEta      = isub.eta();//correctedP4(0).eta();
         subjetPhi      = isub.phi();//correctedP4(0).phi();
         subjetMass     = isub.mass();//correctedP4(0).mass();
         subjetBdisc    = isub.bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags"); 
        //cout<<"subjet pt : "<<subjetPt<<endl;
        double deltaRsubjetJet = deltaR(ijet.eta(), ijet.phi(), subjetEta, subjetPhi);

        if (deltaRsubjetJet<closest_DR){
          second_closest_DR = closest_DR;
          closest_DR        = deltaRsubjetJet;
          second_closest_i  = closest_i;
          closest_i         = count_all_subjets;
        }
        else if (deltaRsubjetJet<second_closest_DR){
          second_closest_DR = deltaRsubjetJet ;
          second_closest_i  = count_all_subjets;
        }
        count_all_subjets++;


      }//first Subject loop ends
      
      nsubjets_pup = 0;
      count_all_subjets =0;
      count_pupsubjet=0;

     
     pup0_area  = 0;
     pup0_tau1  = 0;
     pup0_tau2  = 0;
     pup0_tau3  = 0;
     pup0_flav_hadron  = 0;
     pup0_flav_parton  = 0;
     pup0_bdisc = 0;
     pup0_genpt = 0;
     pup1_area  = 0;
     pup1_tau1  = 0;
     pup1_tau2  = 0;
     pup1_tau3  = 0;
     pup1_flav_hadron  = 0;
     pup1_flav_parton  = 0;
     pup1_bdisc = 0;
     pup1_genpt = 0;
     mostMassiveSDPUPPIsubjetMass = 0;
     TLorentzVector pup0_P4_uncorr;
     TLorentzVector pup1_P4_uncorr;
     TLorentzVector pup0_P4_L23res; 
     TLorentzVector pup1_P4_L23res;
     
  //    if(count_AK8PUPPI==0){//for lead jet    
       int numsubjet=0;
       int nummatchsubjet=0; 
      for (const pat::Jet &isub : *AK8PUPPIsub) {  //second subjet loop
  
       // std::cout<<"uncorr subjet pt: "<<isub.pt()<<std::endl;
        //std::cout<<"corr subjet pt :"<<isub.correctedP4(0).pt()<<std::endl;   
        numsubjet=numsubjet+1;
  
         subjetPt       = isub.pt();// correctedP4(0).pt();
         subjetEta      = isub.eta();//correctedP4(0).eta();
         subjetPhi      = isub.phi();//correctedP4(0).phi();
         subjetMass     = isub.mass();//correctedP4(0).mass();
         subjetBdisc    = isub.bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags"); 

        double deltaRsubjetJet = deltaR(puppi_eta, puppi_phi, subjetEta, subjetPhi);
       //  std::cout<<"deltaR(jet, subjet): "<<deltaRsubjetJet<<std::endl;

       //  std::cout<<"b disc value: "<<subjetBdisc<<std::endl;

       //  std::cout<<"count all subjet: "<<count_all_subjets<<std::endl;


      //   std::cout<<"closest_i: "<<closest_i<<std::endl;

      //   std::cout<<"second_closest_i: "<<second_closest_i<<std::endl;

        if ( count_all_subjets==closest_i || count_all_subjets==second_closest_i ){//first and second closest subjet

          if (deltaRsubjetJet<0.8){
             nsubjets_pup++;
             count_matched_subjets++;
             nummatchsubjet=nummatchsubjet+1;
            //reco::Candidate::LorentzVector uncorrSubjet = isub.correctedP4(0);
            JetCorrectorAK4pup -> setJetEta(subjetEta);// uncorrSubjet.eta()    );
            JetCorrectorAK4pup -> setJetPt (subjetPt);// uncorrSubjet.pt()     );
            JetCorrectorAK4pup -> setJetE  (isub.energy());// uncorrSubjet.energy() );
            JetCorrectorAK4pup -> setJetA  ( isub.jetArea()         );
            JetCorrectorAK4pup -> setRho   ( rho                   );
            JetCorrectorAK4pup -> setNPV   ( nvtx                  );
            subjet_corr_factor_L23res_full = JetCorrectorAK4pup->getCorrection();
            //reco::Candidate::LorentzVector corrSubjetL23res = subjet_corr_factor_L23res_full * uncorrSubjet;

            TLorentzVector AK8subjetUncorr;
            TLorentzVector AK8subjetCorr;
            AK8subjetUncorr.SetPtEtaPhiM(subjetPt, subjetEta, subjetPhi ,subjetMass );            
            AK8subjetCorr=subjet_corr_factor_L23res_full*AK8subjetUncorr;

            TLorentzVector corrSubjetL23res=AK8subjetCorr;
            


            gensubjetpt = 0;
            const reco::GenJet* genJet = isub.genJet();
            if(genJet)gensubjetpt = genJet->pt();


            if (count_pupsubjet==0){//count_pup==0
              pup0_P4_uncorr            .SetPtEtaPhiM( subjetPt, subjetEta, subjetPhi, subjetMass);
              pup0_P4_L23res            .SetPtEtaPhiM( corrSubjetL23res          .Pt() , corrSubjetL23res          .Eta() , corrSubjetL23res          .Phi() , corrSubjetL23res          .M() );
              pup0_tau1   = isub.userFloat("NsubjettinessAK8PFPuppiSoftDropSubjets:tau1");
              pup0_tau2   = isub.userFloat("NsubjettinessAK8PFPuppiSoftDropSubjets:tau2");
              pup0_tau3   = isub.userFloat("NsubjettinessAK8PFPuppiSoftDropSubjets:tau3");
            
              pup0_flav_parton   = isub.partonFlavour();
              pup0_flav_hadron   = isub.hadronFlavour();
              pup0_area          = isub.jetArea() ;

           //   std::cout<<"pup0bdisc: "<<subjetBdisc<<std::endl;

              pup0_bdisc         = subjetBdisc;
              pup0_genpt         = gensubjetpt;
            }//count_pup==0
            if (count_pupsubjet==1) {//count_pup==1
              pup1_P4_uncorr            .SetPtEtaPhiM( subjetPt, subjetEta, subjetPhi, subjetMass);
              pup1_P4_L23res            .SetPtEtaPhiM( corrSubjetL23res          .Pt() , corrSubjetL23res          .Eta() , corrSubjetL23res          .Phi() , corrSubjetL23res          .M() );
              pup1_tau1   = isub.userFloat("NsubjettinessAK8PFPuppiSoftDropSubjets:tau1");
              pup1_tau2   = isub.userFloat("NsubjettinessAK8PFPuppiSoftDropSubjets:tau2");
              pup1_tau3   = isub.userFloat("NsubjettinessAK8PFPuppiSoftDropSubjets:tau3");
            
              pup1_flav_parton   = isub.partonFlavour();
              pup1_flav_hadron   = isub.hadronFlavour();
              pup1_area          = isub.jetArea() ;
              pup1_bdisc         = subjetBdisc;
          //    std::cout<<"pup1bdisc: "<<subjetBdisc<<std::endl;

              pup1_genpt         = gensubjetpt;
            }//count_pup==1

         if(subjetMass > mostMassiveSDPUPPIsubjetMass)mostMassiveSDPUPPIsubjetMass = subjetMass;


         count_pupsubjet++;
         }

       }//first and second closest subjet


     count_all_subjets++;

      }//second subjet loop
    
    // std::cout<<"numsubjet: "<<numsubjet<<std::endl;
   ///  std::cout<<"num matched subjet: "<<nummatchsubjet<<std::endl;
//     }//for lead jet


    
    TLorentzVector sumPUPsubjets_P4_uncorr;
    TLorentzVector sumPUPsubjets_P4_L23res;
    if(count_pupsubjet>1){

      sumPUPsubjets_P4_uncorr            = pup0_P4_uncorr + pup1_P4_uncorr ; 
      sumPUPsubjets_P4_L23res            = pup0_P4_L23res + pup1_P4_L23res ; 



     }   

     if(count_AK8PUPPI==0){
      Jet0SDRaw_vec->push_back(sumPUPsubjets_P4_uncorr);
      Jet0SD_vec->push_back(sumPUPsubjets_P4_L23res);     
       }
     if(count_AK8PUPPI==1){
      Jet1SDRaw_vec->push_back(sumPUPsubjets_P4_uncorr);
      Jet1SD_vec->push_back(sumPUPsubjets_P4_L23res);
       }



   


    pup_maxbdisc = 0 ;
    pup_maxbdiscflav_hadron = 0 ;
    pup_maxbdiscflav_parton = 0 ;

    if(pup0_bdisc>=pup1_bdisc){
      pup_maxbdisc = pup0_bdisc;
      pup_maxbdiscflav_hadron = pup0_flav_hadron;
      pup_maxbdiscflav_parton = pup0_flav_parton;
    } 
    else if(pup1_bdisc>pup0_bdisc){
      pup_maxbdisc = pup1_bdisc;
      pup_maxbdiscflav_hadron = pup1_flav_hadron;
      pup_maxbdiscflav_parton = pup1_flav_parton;
    } 
   

     if(count_AK8PUPPI==0){
     Jet0SDsubjet0_vec->push_back(pup0_P4_uncorr);
     Jet0SDsubjet1_vec->push_back(pup1_P4_uncorr);
     Jet0SDsubjet0bdisc_doble=pup0_bdisc;
     Jet0SDsubjet1bdisc_doble=pup1_bdisc;
     Jet0SDmaxbdisc_doble=pup_maxbdisc;
    // std::cout<<"Max subjet b disc> lead jet: "<<Jet0SDmaxbdisc_doble<<std::endl;

     Jet0SDmaxbdiscflavHadron_doble=pup_maxbdiscflav_hadron;
     Jet0SDmaxbdiscflavParton_doble=pup_maxbdiscflav_parton;
     Jet0SDsubjet0area_doble=pup0_area;
     Jet0SDsubjet0flavHadron_doble=pup0_flav_hadron;
     Jet0SDsubjet0flavParton_doble=pup0_flav_parton;
     Jet0SDsubjet0matchedgenjetpt_doble=pup0_genpt;
     Jet0SDsubjet0tau1_doble=pup0_tau1;
     Jet0SDsubjet0tau2_doble=pup0_tau2;
     Jet0SDsubjet0tau3_doble=pup0_tau3;
     Jet0SDsubjet1area_doble=pup1_area;
     Jet0SDsubjet1flavHadron_doble=pup1_flav_hadron;
     Jet0SDsubjet1flavParton_doble=pup1_flav_parton;
     Jet0SDsubjet1matchedgenjetpt_doble=pup1_genpt;
     Jet0SDsubjet1tau1_doble=pup1_tau1;
     Jet0SDsubjet1tau2_doble=pup1_tau2;
     Jet0SDsubjet1tau3_doble=pup1_tau3;     


     }

     if(count_AK8PUPPI==1){
     Jet1SDsubjet0_vec->push_back(pup0_P4_uncorr);
     Jet1SDsubjet1_vec->push_back(pup1_P4_uncorr);
     Jet1SDsubjet0bdisc_doble=pup0_bdisc;
     Jet1SDsubjet1bdisc_doble=pup1_bdisc;
     Jet1SDmaxbdisc_doble=pup_maxbdisc;
     Jet1SDmaxbdiscflavHadron_doble=pup_maxbdiscflav_hadron;
     Jet1SDmaxbdiscflavParton_doble=pup_maxbdiscflav_parton;
     Jet1SDsubjet0area_doble=pup0_area;
     Jet1SDsubjet0flavHadron_doble=pup0_flav_hadron;
     Jet1SDsubjet0flavParton_doble=pup0_flav_parton;
     Jet1SDsubjet0matchedgenjetpt_doble=pup0_genpt;
     Jet1SDsubjet0tau1_doble=pup0_tau1;
     Jet1SDsubjet0tau2_doble=pup0_tau2;
     Jet1SDsubjet0tau3_doble=pup0_tau3;
     Jet1SDsubjet1area_doble=pup1_area;
     Jet1SDsubjet1flavHadron_doble=pup1_flav_hadron;
     Jet1SDsubjet1flavParton_doble=pup1_flav_parton;
     Jet1SDsubjet1matchedgenjetpt_doble=pup1_genpt;
     Jet1SDsubjet1tau1_doble=pup1_tau1;
     Jet1SDsubjet1tau2_doble=pup1_tau2;
     Jet1SDsubjet1tau3_doble=pup1_tau3;     

     }


   
  
  
   count_AK8PUPPI++;
   }//AK8puppi Loop ends



  // numJets=numJCounter;



   	






    /*
    int numPFPuppiJets=0;
    for(View<pat::Jet>::const_iterator iPFpuppi = JetHandlepfpuppi->begin(); iPFpuppi != JetHandlepfpuppi->end(); ++iPFpuppi){//PFCHS Jet loop
             if(iPFpuppi->pt()>30.0 && fabs(iPFpuppi->eta()) < 2.4){
             numPFPuppiJets++;

               //std::cout<<"JetPt: "<<iPFpuppi->pt()<<std::endl;  

               TLorentzVector tmpPJ;
               tmpPJ.SetPxPyPzE(iPFpuppi->px(),iPFpuppi->py(),iPFpuppi->pz(),iPFpuppi->energy());

             
               AK8PFPuppiJets_vec->push_back(tmpPJ);
               if(TurnOnTrimming_){AK8PFPuppiTrimMass_vec->push_back(iPFpuppi->userFloat("ak8PFJetsPuppiTrimmedMass"));}
               if(TurnOnPruning_){AK8PFPuppiPrunMass_vec->push_back(iPFpuppi->userFloat("ak8PFJetsPuppiPrunedMass"));}
               if(TurnOnSoftdrop_){AK8PFPuppiSoftdropMass_vec->push_back(iPFpuppi->userFloat("ak8PFJetsPuppiSoftDropMass"));}
               if(TurnOnNsub_){AK8PFPuppitau1_vec->push_back(iPFpuppi->userFloat("NjettinessAK8Puppi:tau1"));}
               if(TurnOnNsub_){AK8PFPuppitau2_vec->push_back(iPFpuppi->userFloat("NjettinessAK8Puppi:tau2"));}
               if(TurnOnNsub_){AK8PFPuppitau3_vec->push_back(iPFpuppi->userFloat("NjettinessAK8Puppi:tau3"));}
               //if(TurnOnCMSTopTagger_){AK8PFPuppiCMSTopTaggedMass_vec->push_back(iPFpuppi->userFloat("cmsTopTagPFJetsPuppiMassAK8"));}




                                  }
       }//PFCHS Jet loop
      //  std::cout<<"num PFPuppiJets: "<<numPFPuppiJets<<std::endl;

      */


















    for(unsigned int igj=0;igj<genJetHandle->size();igj++){
       if(genJetHandle->at(igj).pt() > 100.0){//jet pt cut
       AK8GenJets_vec->push_back(genJetHandle->at(igj));
       TLorentzVector tmpGJ;
       tmpGJ.SetPxPyPzE(genJetHandle->at(igj).px(),genJetHandle->at(igj).py(),genJetHandle->at(igj).pz(),genJetHandle->at(igj).energy());
       AK8GenJetss_vec->push_back(tmpGJ);

           }//jet pt cut
        }










   //std::vector<fastjet::PseudoJet> fatJets;


   iEvent.put(std::move(AK8PFCHSJet_vec),"AK8PFCHSJet");
   iEvent.put(std::move(AK8GenJetss_vec),"AK8GenJets");
   iEvent.put(std::move(AK8PFPuppiJetsUncorr_vec),"AK8PFPuppiJetUncorr");
   iEvent.put(std::move(AK8PFPuppiNHEF_vec),"AK8puppiNHEF");
   iEvent.put(std::move(AK8PFPuppiNEmEF_vec),"AK8puppiNEmEF");
   iEvent.put(std::move(AK8PFPuppiCHF_vec),"AK8puppiCHF");
   iEvent.put(std::move(AK8PFPuppimuEF_vec),"AK8puppimuEF");
   iEvent.put(std::move(AK8PFPuppiCEmF_vec),"AK8puppiCEmF");
   iEvent.put(std::move(AK8PFPuppiNumConst_vec),"AK8puppiNumConst");
   iEvent.put(std::move(AK8PFPuppiNMulti_vec),"AK8puppiNMultiplicity");
   iEvent.put(std::move(AK8PFPuppiCMulti_vec),"AK8puppiCMultiplicity");
   iEvent.put(std::move(AK8PFPuppiJets_vec),"AK8PFPuppiJet");
   iEvent.put(std::move(AK8PFPuppiGenMatched_vec),"AK8PFPuppiJetGenMatched");
   iEvent.put(std::move(AK8GenJets_vec),"AK8GenJet");
   iEvent.put(std::move(AK8PFPuppiTrimMass_vec),"AK8PFPuppiTrimmedMass");
   iEvent.put(std::move(AK8PFPuppiPrunMass_vec),"AK8PFPuppiPrunedMass");
   iEvent.put(std::move(AK8PFPuppiSoftdropMass_vec),"AK8PFPuppiSoftdropMass");
   iEvent.put(std::move(AK8PFPuppitau1_vec),"AK8PFPuppitau1");
   iEvent.put(std::move(AK8PFPuppitau2_vec),"AK8PFPuppitau2");
   iEvent.put(std::move(AK8PFPuppitau3_vec),"AK8PFPuppitau3");  

   ///////////////////////////Important Analysis variables

   iEvent.put(std::move(Jet0Raw_vec),"Jet0Raw");
   iEvent.put(std::move(Jet0_vec),"Jet0");  
   iEvent.put(std::move(Jet0Area_dob),"Jet0Area");
   iEvent.put(std::move(Jet0SD_vec),"Jet0SD");
   iEvent.put(std::move(Jet0SDRaw_vec),"Jet0SDRaw");
   iEvent.put(std::move(Jet0SDsubjet0_vec),"Jet0SDsubjet0");
   iEvent.put(std::move(Jet0SDsubjet1_vec),"Jet0SDsubjet1");

   auto Jet0L2Corr_dob = std::make_unique<double>(Jet0L2Corr);
   auto Jet1L2Corr_dob = std::make_unique<double>(Jet1L2Corr);   


   auto Jet0SDmass_dob = std::make_unique<double>(Jet0SDmass_doble);
   auto Jet0SDmassSubjetCorrL23_dob = std::make_unique<double>(Jet0SDmassSubjetCorrL23_doble);
   auto Jet0SDmassSubjetCorrL123_dob = std::make_unique<double>(Jet0SDmassSubjetCorrL123_doble);
   auto Jet0MassPruned_dob = std::make_unique<double>(Jet0MassPruned_doble);
   auto Jet0MassTrimmed_dob = std::make_unique<double>(Jet0MassTrimmed_doble);
   auto Jet0Tau1_dob = std::make_unique<double>(Jet0Tau1_doble);
   auto Jet0Tau2_dob = std::make_unique<double>(Jet0Tau2_doble);
   auto Jet0Tau3_dob = std::make_unique<double>(Jet0Tau3_doble);
   auto Jet0Tau4_dob = std::make_unique<double>(Jet0Tau4_doble);
   auto Jet0Tau32_dob = std::make_unique<double>(Jet0Tau32_doble);
   auto Jet0Tau21_dob = std::make_unique<double>(Jet0Tau21_doble);
   auto Jet0SDsubjet0bdisc_dob = std::make_unique<double>(Jet0SDsubjet0bdisc_doble);
   auto Jet0SDsubjet1bdisc_dob = std::make_unique<double>(Jet0SDsubjet1bdisc_doble);
   auto Jet0SDmaxbdisc_dob = std::make_unique<double>(Jet0SDmaxbdisc_doble);
   auto Jet0SDmaxbdiscflavHadron_dob = std::make_unique<double>(Jet0SDmaxbdiscflavHadron_doble);  
   auto Jet0SDmaxbdiscflavParton_dob = std::make_unique<double>(Jet0SDmaxbdiscflavParton_doble);
   auto Jet0SDsubjet0area_dob = std::make_unique<double>(Jet0SDsubjet0area_doble);
   auto Jet0SDsubjet0flavHadron_dob = std::make_unique<double>(Jet0SDsubjet0flavHadron_doble);
   auto Jet0SDsubjet0flavParton_dob = std::make_unique<double>(Jet0SDsubjet0flavParton_doble);
   auto Jet0SDsubjet0matchedgenjetpt_dob = std::make_unique<double>(Jet0SDsubjet0matchedgenjetpt_doble);
   auto Jet0SDsubjet0tau1_dob = std::make_unique<double>(Jet0SDsubjet0tau1_doble);
   auto Jet0SDsubjet0tau2_dob = std::make_unique<double>(Jet0SDsubjet0tau2_doble);
   auto Jet0SDsubjet0tau3_dob = std::make_unique<double>(Jet0SDsubjet0tau3_doble);
   auto Jet0SDsubjet1area_dob = std::make_unique<double>(Jet0SDsubjet1area_doble);
   auto Jet0SDsubjet1flavHadron_dob = std::make_unique<double>(Jet0SDsubjet1flavHadron_doble);
   auto Jet0SDsubjet1flavParton_dob = std::make_unique<double>(Jet0SDsubjet1flavParton_doble);
   auto Jet0SDsubjet1matchedgenjetpt_dob = std::make_unique<double>(Jet0SDsubjet1matchedgenjetpt_doble);
   auto Jet0SDsubjet1tau1_dob = std::make_unique<double>(Jet0SDsubjet1tau1_doble);
   auto Jet0SDsubjet1tau2_dob = std::make_unique<double>(Jet0SDsubjet1tau2_doble);
   auto Jet0SDsubjet1tau3_dob = std::make_unique<double>(Jet0SDsubjet1tau3_doble);
   auto Jet0CHF_dob  = std::make_unique<double>(Jet0CHF_doble);
   auto Jet0NHF_dob = std::make_unique<double>(Jet0NHF_doble);
   auto Jet0CM_dob = std::make_unique<double>(Jet0CM_doble);
   auto Jet0NM_dob  = std::make_unique<double>(Jet0NM_doble);
   auto Jet0NEF_dob  = std::make_unique<double>(Jet0NEF_doble);
   auto Jet0CEF_dob = std::make_unique<double>(Jet0CEF_doble);
   auto Jet0MF_dob = std::make_unique<double>(Jet0MF_doble);
   auto Jet0Mult_dob = std::make_unique<double>(Jet0Mult_doble);
   auto Jet0NsubjetsSD_int = std::make_unique<int>(Jet0NsubjetsSD_integer);
   auto Jet0GenMatched_bPt_dob = std::make_unique<double>(Jet0GenMatched_bPt_doble);
   auto Jet0GenMatched_WPt_dob = std::make_unique<double>(Jet0GenMatched_WPt_doble);
   auto Jet0GenMatched_Wd1Pt_dob = std::make_unique<double>(Jet0GenMatched_Wd1Pt_doble);
   auto Jet0GenMatched_Wd2Pt_dob = std::make_unique<double>(Jet0GenMatched_Wd2Pt_doble);
   auto Jet0GenMatched_Wd1ID_dob = std::make_unique<double>(Jet0GenMatched_Wd1ID_doble);
   auto Jet0GenMatched_Wd2ID_dob = std::make_unique<double>(Jet0GenMatched_Wd2ID_doble);

   iEvent.put(std::move( Jet0L2Corr_dob ), "Jet0L2RelativeCorr");
   iEvent.put(std::move( Jet1L2Corr_dob ), "Jet1L2RelativeCorr");


   iEvent.put(std::move( Jet0SDmass_dob ), "Jet0SDmass");
   iEvent.put(std::move( Jet0SDmassSubjetCorrL23_dob ), "Jet0SDmassSubjetCorrL23");
   iEvent.put(std::move( Jet0SDmassSubjetCorrL123_dob ), "Jet0SDmassSubjetCorrL123");
   iEvent.put(std::move( Jet0MassPruned_dob ), "Jet0MassPruned");
   iEvent.put(std::move( Jet0MassTrimmed_dob ), "Jet0MassTrimmed");
   iEvent.put(std::move( Jet0Tau1_dob ), "Jet0Tau1");
   iEvent.put(std::move( Jet0Tau2_dob ), "Jet0Tau2");
   iEvent.put(std::move( Jet0Tau3_dob ), "Jet0Tau3");
   iEvent.put(std::move( Jet0Tau4_dob ), "Jet0Tau4");
   iEvent.put(std::move( Jet0Tau32_dob ), "Jet0Tau32");
   iEvent.put(std::move( Jet0Tau21_dob ), "Jet0Tau21");
   iEvent.put(std::move( Jet0SDsubjet0bdisc_dob ), "Jet0SDsubjet0bdisc");
   iEvent.put(std::move( Jet0SDsubjet1bdisc_dob ), "Jet0SDsubjet1bdisc");
   iEvent.put(std::move( Jet0SDmaxbdisc_dob ), "Jet0SDmaxbdisc");
   iEvent.put(std::move( Jet0SDmaxbdiscflavHadron_dob ), "Jet0SDmaxbdiscflavHadron");
   iEvent.put(std::move( Jet0SDmaxbdiscflavParton_dob ), "Jet0SDmaxbdiscflavParton");
   iEvent.put(std::move( Jet0SDsubjet0area_dob ), "Jet0SDsubjet0area");
   iEvent.put(std::move( Jet0SDsubjet0flavHadron_dob ), "Jet0SDsubjet0flavHadron");
   iEvent.put(std::move( Jet0SDsubjet0flavParton_dob ), "Jet0SDsubjet0flavParton");
   iEvent.put(std::move( Jet0SDsubjet0matchedgenjetpt_dob ), "Jet0SDsubjet0matchedgenjetpt");
   iEvent.put(std::move( Jet0SDsubjet0tau1_dob ), "Jet0SDsubjet0tau1");
   iEvent.put(std::move( Jet0SDsubjet0tau2_dob ), "Jet0SDsubjet0tau2");
   iEvent.put(std::move( Jet0SDsubjet0tau3_dob ), "Jet0SDsubjet0tau3");
   iEvent.put(std::move( Jet0SDsubjet1area_dob ), "Jet0SDsubjet1area");
   iEvent.put(std::move( Jet0SDsubjet1flavHadron_dob ), "Jet0SDsubjet1flavHadron");
   iEvent.put(std::move( Jet0SDsubjet1flavParton_dob ), "Jet0SDsubjet1flavParton");
   iEvent.put(std::move( Jet0SDsubjet1matchedgenjetpt_dob ), "Jet0SDsubjet1matchedgenjetpt");
   iEvent.put(std::move( Jet0SDsubjet1tau1_dob ), "Jet0SDsubjet1tau1");
   iEvent.put(std::move( Jet0SDsubjet1tau2_dob ), "Jet0SDsubjet1tau2");
   iEvent.put(std::move( Jet0SDsubjet1tau3_dob ), "Jet0SDsubjet1tau3");
   iEvent.put(std::move( Jet0CHF_dob  ), "Jet0CHF");
   iEvent.put(std::move( Jet0NHF_dob ), "Jet0NHF");
   iEvent.put(std::move( Jet0CM_dob ), "Jet0CM");
   iEvent.put(std::move( Jet0NM_dob  ), "Jet0NM");
   iEvent.put(std::move( Jet0NEF_dob  ), "Jet0NEF");
   iEvent.put(std::move( Jet0CEF_dob ), "Jet0CEF");
   iEvent.put(std::move( Jet0MF_dob ), "Jet0MF");
   iEvent.put(std::move( Jet0Mult_dob ), "Jet0Mult");
   iEvent.put(std::move( Jet0NsubjetsSD_int),"Jet0NsubjetsSD");
   iEvent.put(std::move( Jet0GenMatched_bPt_dob ), "Jet0GenMatchedbPt");
   iEvent.put(std::move( Jet0GenMatched_WPt_dob ), "Jet0GenMatchedWPt");
   iEvent.put(std::move( Jet0GenMatched_Wd1Pt_dob ), "Jet0GenMatchedWd1Pt");
   iEvent.put(std::move( Jet0GenMatched_Wd2Pt_dob ), "Jet0GenMatchedWd2Pt");
   iEvent.put(std::move( Jet0GenMatched_Wd1ID_dob ), "Jet0GenMatchedWd1ID");
   iEvent.put(std::move( Jet0GenMatched_Wd2ID_dob ), "Jet0GenMatchedWd2ID"); 








   iEvent.put(std::move(Jet1Raw_vec),"Jet1Raw");
   iEvent.put(std::move(Jet1_vec),"Jet1");
   iEvent.put(std::move(Jet1Area_dob),"Jet1Area");
   iEvent.put(std::move(Jet1SD_vec),"Jet1SD");
   iEvent.put(std::move(Jet1SDRaw_vec),"Jet1SDRaw");
   iEvent.put(std::move(Jet1SDsubjet0_vec),"Jet1SDsubjet0");
   iEvent.put(std::move(Jet1SDsubjet1_vec),"Jet1SDsubjet1");
   
   auto Jet1SDmass_dob = std::make_unique<double>(Jet1SDmass_doble);
   auto Jet1SDmassSubjetCorrL23_dob = std::make_unique<double>(Jet1SDmassSubjetCorrL23_doble);
   auto Jet1SDmassSubjetCorrL123_dob = std::make_unique<double>(Jet1SDmassSubjetCorrL123_doble);
   auto Jet1MassPruned_dob = std::make_unique<double>(Jet1MassPruned_doble);
   auto Jet1MassTrimmed_dob = std::make_unique<double>(Jet1MassTrimmed_doble);
   auto Jet1Tau1_dob = std::make_unique<double>(Jet1Tau1_doble);
   auto Jet1Tau2_dob = std::make_unique<double>(Jet1Tau2_doble);
   auto Jet1Tau3_dob = std::make_unique<double>(Jet1Tau3_doble);
   auto Jet1Tau4_dob = std::make_unique<double>(Jet1Tau4_doble);
   auto Jet1Tau32_dob = std::make_unique<double>(Jet1Tau32_doble);
   auto Jet1Tau21_dob = std::make_unique<double>(Jet1Tau21_doble);
   auto Jet1SDsubjet0bdisc_dob = std::make_unique<double>(Jet1SDsubjet0bdisc_doble);
   auto Jet1SDsubjet1bdisc_dob = std::make_unique<double>(Jet1SDsubjet1bdisc_doble);
   auto Jet1SDmaxbdisc_dob = std::make_unique<double>(Jet1SDmaxbdisc_doble);
   auto Jet1SDmaxbdiscflavHadron_dob = std::make_unique<double>(Jet1SDmaxbdiscflavHadron_doble);  
   auto Jet1SDmaxbdiscflavParton_dob = std::make_unique<double>(Jet1SDmaxbdiscflavParton_doble);
   auto Jet1SDsubjet0area_dob = std::make_unique<double>(Jet1SDsubjet0area_doble);
   auto Jet1SDsubjet0flavHadron_dob = std::make_unique<double>(Jet1SDsubjet0flavHadron_doble);
   auto Jet1SDsubjet0flavParton_dob = std::make_unique<double>(Jet1SDsubjet0flavParton_doble);
   auto Jet1SDsubjet0matchedgenjetpt_dob = std::make_unique<double>(Jet1SDsubjet0matchedgenjetpt_doble);
   auto Jet1SDsubjet0tau1_dob = std::make_unique<double>(Jet1SDsubjet0tau1_doble);
   auto Jet1SDsubjet0tau2_dob = std::make_unique<double>(Jet1SDsubjet0tau2_doble);
   auto Jet1SDsubjet0tau3_dob = std::make_unique<double>(Jet1SDsubjet0tau3_doble);
   auto Jet1SDsubjet1area_dob = std::make_unique<double>(Jet1SDsubjet1area_doble);
   auto Jet1SDsubjet1flavHadron_dob = std::make_unique<double>(Jet1SDsubjet1flavHadron_doble);
   auto Jet1SDsubjet1flavParton_dob = std::make_unique<double>(Jet1SDsubjet1flavParton_doble);
   auto Jet1SDsubjet1matchedgenjetpt_dob = std::make_unique<double>(Jet1SDsubjet1matchedgenjetpt_doble);
   auto Jet1SDsubjet1tau1_dob = std::make_unique<double>(Jet1SDsubjet1tau1_doble);
   auto Jet1SDsubjet1tau2_dob = std::make_unique<double>(Jet1SDsubjet1tau2_doble);
   auto Jet1SDsubjet1tau3_dob = std::make_unique<double>(Jet1SDsubjet1tau3_doble);
   auto Jet1CHF_dob  = std::make_unique<double>(Jet1CHF_doble);
   auto Jet1NHF_dob = std::make_unique<double>(Jet1NHF_doble);
   auto Jet1CM_dob = std::make_unique<double>(Jet1CM_doble);
   auto Jet1NM_dob  = std::make_unique<double>(Jet1NM_doble);
   auto Jet1NEF_dob  = std::make_unique<double>(Jet1NEF_doble);
   auto Jet1CEF_dob = std::make_unique<double>(Jet1CEF_doble);
   auto Jet1MF_dob = std::make_unique<double>(Jet1MF_doble);
   auto Jet1Mult_dob = std::make_unique<double>(Jet1Mult_doble);
   auto Jet1NsubjetsSD_int = std::make_unique<int>(Jet1NsubjetsSD_integer);
   auto Jet1GenMatched_bPt_dob = std::make_unique<double>(Jet1GenMatched_bPt_doble);
   auto Jet1GenMatched_WPt_dob = std::make_unique<double>(Jet1GenMatched_WPt_doble);
   auto Jet1GenMatched_Wd1Pt_dob = std::make_unique<double>(Jet1GenMatched_Wd1Pt_doble);
   auto Jet1GenMatched_Wd2Pt_dob = std::make_unique<double>(Jet1GenMatched_Wd2Pt_doble);
   auto Jet1GenMatched_Wd1ID_dob = std::make_unique<double>(Jet1GenMatched_Wd1ID_doble);
   auto Jet1GenMatched_Wd2ID_dob = std::make_unique<double>(Jet1GenMatched_Wd2ID_doble);

   iEvent.put(std::move( Jet1SDmass_dob ), "Jet1SDmass");
   iEvent.put(std::move( Jet1SDmassSubjetCorrL23_dob ), "Jet1SDmassSubjetCorrL23");
   iEvent.put(std::move( Jet1SDmassSubjetCorrL123_dob ), "Jet1SDmassSubjetCorrL123");
   iEvent.put(std::move( Jet1MassPruned_dob ), "Jet1MassPruned");
   iEvent.put(std::move( Jet1MassTrimmed_dob ), "Jet1MassTrimmed");
   iEvent.put(std::move( Jet1Tau1_dob ), "Jet1Tau1");
   iEvent.put(std::move( Jet1Tau2_dob ), "Jet1Tau2");
   iEvent.put(std::move( Jet1Tau3_dob ), "Jet1Tau3");
   iEvent.put(std::move( Jet1Tau4_dob ), "Jet1Tau4");
   iEvent.put(std::move( Jet1Tau32_dob ), "Jet1Tau32");
   iEvent.put(std::move( Jet1Tau21_dob ), "Jet1Tau21");
   iEvent.put(std::move( Jet1SDsubjet0bdisc_dob ), "Jet1SDsubjet0bdisc");
   iEvent.put(std::move( Jet1SDsubjet1bdisc_dob ), "Jet1SDsubjet1bdisc");
   iEvent.put(std::move( Jet1SDmaxbdisc_dob ), "Jet1SDmaxbdisc");
   iEvent.put(std::move( Jet1SDmaxbdiscflavHadron_dob ), "Jet1SDmaxbdiscflavHadron");
   iEvent.put(std::move( Jet1SDmaxbdiscflavParton_dob ), "Jet1SDmaxbdiscflavParton");
   iEvent.put(std::move( Jet1SDsubjet0area_dob ), "Jet1SDsubjet0area");
   iEvent.put(std::move( Jet1SDsubjet0flavHadron_dob ), "Jet1SDsubjet0flavHadron");
   iEvent.put(std::move( Jet1SDsubjet0flavParton_dob ), "Jet1SDsubjet0flavParton");
   iEvent.put(std::move( Jet1SDsubjet0matchedgenjetpt_dob ), "Jet1SDsubjet0matchedgenjetpt");
   iEvent.put(std::move( Jet1SDsubjet0tau1_dob ), "Jet1SDsubjet0tau1");
   iEvent.put(std::move( Jet1SDsubjet0tau2_dob ), "Jet1SDsubjet0tau2");
   iEvent.put(std::move( Jet1SDsubjet0tau3_dob ), "Jet1SDsubjet0tau3");
   iEvent.put(std::move( Jet1SDsubjet1area_dob ), "Jet1SDsubjet1area");
   iEvent.put(std::move( Jet1SDsubjet1flavHadron_dob ), "Jet1SDsubjet1flavHadron");
   iEvent.put(std::move( Jet1SDsubjet1flavParton_dob ), "Jet1SDsubjet1flavParton");
   iEvent.put(std::move( Jet1SDsubjet1matchedgenjetpt_dob ), "Jet1SDsubjet1matchedgenjetpt");
   iEvent.put(std::move( Jet1SDsubjet1tau1_dob ), "Jet1SDsubjet1tau1");
   iEvent.put(std::move( Jet1SDsubjet1tau2_dob ), "Jet1SDsubjet1tau2");
   iEvent.put(std::move( Jet1SDsubjet1tau3_dob ), "Jet1SDsubjet1tau3");
   iEvent.put(std::move( Jet1CHF_dob  ), "Jet1CHF");
   iEvent.put(std::move( Jet1NHF_dob ), "Jet1NHF");
   iEvent.put(std::move( Jet1CM_dob ), "Jet1CM");
   iEvent.put(std::move( Jet1NM_dob  ), "Jet1NM");
   iEvent.put(std::move( Jet1NEF_dob  ), "Jet1NEF");
   iEvent.put(std::move( Jet1CEF_dob ), "Jet1CEF");
   iEvent.put(std::move( Jet1MF_dob ), "Jet1MF");
   iEvent.put(std::move( Jet1Mult_dob ), "Jet1Mult");
   iEvent.put(std::move( Jet1NsubjetsSD_int),"Jet1NsubjetsSD");
   iEvent.put(std::move( Jet1GenMatched_bPt_dob ), "Jet1GenMatchedbPt");
   iEvent.put(std::move( Jet1GenMatched_WPt_dob ), "Jet1GenMatchedWPt");
   iEvent.put(std::move( Jet1GenMatched_Wd1Pt_dob ), "Jet1GenMatchedWd1Pt");
   iEvent.put(std::move( Jet1GenMatched_Wd2Pt_dob ), "Jet1GenMatchedWd2Pt");
   iEvent.put(std::move( Jet1GenMatched_Wd1ID_dob ), "Jet1GenMatchedWd1ID");
  

        auto NumJ = std::make_unique<int>(numJets);
        iEvent.put(std::move(NumJ),"numAK8puppiJets");


/* This is an event example
   //Read 'ExampleData' from the Event
   Handle<ExampleData> pIn;
   iEvent.getByLabel("example",pIn);

   //Use the ExampleData to create an ExampleData2 which 
   // is put into the Event
   std::unique_ptr<ExampleData2> pOut(new ExampleData2(*pIn));
   iEvent.put(std::move(pOut));
*/

/* this is an EventSetup example
   //Read SetupData from the SetupRecord in the EventSetup
   ESHandle<SetupData> pSetup;
   iSetup.get<SetupRecord>().get(pSetup);
*/
 
}

// ------------ method called once each stream before processing any runs, lumis or events  ------------
void
JetProducer::beginStream(edm::StreamID)
{
}

// ------------ method called once each stream after processing all runs, lumis and events  ------------
void
JetProducer::endStream() {
}

// ------------ method called when starting to processes a run  ------------
/*
void
JetProducer::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method called when ending the processing of a run  ------------
/*
void
JetProducer::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method called when starting to processes a luminosity block  ------------
/*
void
JetProducer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method called when ending the processing of a luminosity block  ------------
/*
void
JetProducer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
JetProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(JetProducer);
