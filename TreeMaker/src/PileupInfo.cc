// -*- C++ -*-
//
// Package:    PileupInfo
// Class:      PileupInfo
// 
/**\class PileupInfo PileupInfo.cc RA2Classic/PileupInfo/src/PileupInfo.cc
 * 
 * Description: [one line class summary]
 * 
 * Implementation:
 *     [Notes on implementation]
 */ 
//Author ; Bibhuprasad Mahakud
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include <DataFormats/Math/interface/deltaR.h>
#include "DataFormats/PatCandidates/interface/PackedGenParticle.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"
#include "DataFormats/VertexReco/interface/Vertex.h"

#include<iostream>
//
// class declaration
//

class PileupInfo : public edm::EDProducer {
public:
	explicit PileupInfo(const edm::ParameterSet&);
	~PileupInfo();
	
	static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
	
private:
	virtual void beginJob() ;
	virtual void produce(edm::Event&, const edm::EventSetup&);
	virtual void endJob() ;
	
	virtual void beginRun(edm::Run&, edm::EventSetup const&);
	virtual void endRun(edm::Run&, edm::EventSetup const&);
	virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
	virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
	edm::InputTag puTag_;
	edm::EDGetTokenT<std::vector<PileupSummaryInfo>> puTagTok_;
	
	
	// ----------member data ---------------------------
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
PileupInfo::PileupInfo(const edm::ParameterSet& iConfig)
{
	//register your produc
	puTag_ = iConfig.getParameter<edm::InputTag>("puCollection");
	puTagTok_ = consumes<std::vector<PileupSummaryInfo>>(puTag_);
	
	produces<int>("");
	/* Examples
	 *   produces<ExampleData2>();
	 * 
	 *   //if do put with a label
	 *   produces<ExampleData2>("label");
	 * 
	 *   //if you want to put into the Run
	 *   produces<ExampleData2,InRun>();
	 */
	//now do what ever other initialization is needed
	
}


PileupInfo::~PileupInfo()
{
	
	// do anything here that needs to be done at desctruction time
	// (e.g. close files, deallocate resources etc.)
	
}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
PileupInfo::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
	using namespace edm;

        edm::Handle<std::vector< PileupSummaryInfo > >  PupInfo;
        //iEvent.getByLabel(edm::InputTag("addPileupInfo"), PupInfo);
        iEvent.getByToken(puTagTok_, PupInfo);
        std::vector<PileupSummaryInfo>::const_iterator PVI;
        int npuNum=0;        
        //float npT=-1.;
        //float npIT=-1.;

       for(PVI = PupInfo->begin(); PVI != PupInfo->end(); ++PVI) {
        int BX = PVI->getBunchCrossing();
          if(BX == 0) {
           //npT = PVI->getTrueNumInteractions();
           npuNum = PVI->getPU_NumInteractions();

             }
         }

      // std::cout<<"true Num: "<<npT<<std::endl;
      // std::cout<<"pu Num: "<<npIT<<std::endl;




	//edm::Handle<reco::VertexCollection> vertices;
	//iEvent.getByToken(vertexCollectionTok_,vertices);
	//if( vertices.isValid() ) {
	//	nVertices = vertices->size();
//	}
//	else std::cout<<"Warning VertexCollection Tag not valid: "<<vertexCollectionTag_.label()<<std::endl;
	auto punum = std::make_unique<int>(npuNum);
	iEvent.put(std::move(punum));
	
}

// ------------ method called once each job just before starting event loop  ------------
void 
PileupInfo::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
PileupInfo::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
PileupInfo::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
PileupInfo::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
PileupInfo::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
PileupInfo::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
PileupInfo::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
	//The following says we do not know what parameters are allowed so do no validation
	// Please change this to state exactly what you do use, even if it is no parameters
	edm::ParameterSetDescription desc;
	desc.setUnknown();
	descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(PileupInfo);
