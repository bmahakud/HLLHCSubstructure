#!/bin/bash

#
# variables from arguments string in jdl
#

echo "Starting job on " `date` #Only to display the starting of production date
echo "Running on " `uname -a` #Only to display the machine where the job is running
echo "System release " `cat /etc/redhat-release` #And the system release
echo "CMSSW on Condor"

CMSSWVER=$1
INPUTFILE=$2
OUTDIR=$3
NSTART=$4
NFILES=$5

echo ""
echo "parameter set:"
echo "CMSSWVER:   $CMSSWVER"
echo "INPUTFILE  $INPUTFILE"
echo "OUTDIR:     $OUTDIR"
echo "NSTART:     $NSTART"
echo "NFILES:     $NFILES"

tar -xzf ${CMSSWVER}.tar.gz
cd ${CMSSWVER}
scram b ProjectRename
source /cvmfs/cms.cern.ch/cmsset_default.sh
# cmsenv
eval `scramv1 runtime -sh`
cd -

# run CMSSW
SAMPLE="QCD_Flat_Pt-15to7000_TuneCUETP8M1_14TeV_pythia8_NoPU_AODSIM"
ARGS="inputFilesConfig=${INPUTFILE} nstart=${NSTART} nfiles=${NFILES}"
echo "ARGS $ARGS"
cmsRun runMakeTreeTest932_cfg.py ${ARGS} 2>&1

CMSEXIT=$?

if [[ $CMSEXIT -ne 0 ]]; then
  rm *.root
  echo "exit code $CMSEXIT, skipping xrdcp"
  exit $CMSEXIT
fi

# copy output to eos
echo "xrdcp output for condor"
for FILE in *.root
do
  echo "xrdcp -f ${FILE} ${OUTDIR}/${FILE}"
  xrdcp -f ${FILE} ${OUTDIR}/${FILE} 2>&1
  XRDEXIT=$?
  if [[ $XRDEXIT -ne 0 ]]; then
    rm *.root
    echo "exit code $XRDEXIT, failure in xrdcp"
    exit $XRDEXIT
  fi
  rm ${FILE}
done

