import os, bisect
from optparse import OptionParser
from FWCore.PythonUtilities.LumiList import LumiList

# define options
parser = OptionParser()
parser.add_option("-n", "--nFiles", dest="nFiles", default=1,
                                    help="number of files to process per job (default = %default)")

parser.add_option("-i", "--inputFile", dest="inputFile", default="",
                                    help="inputfile name (default = %default)")


parser.add_option("-o","--outputDir",dest="outputDir", default="",
                                       help="path to ouput directory in which root files will be stored  (default = %default)")

parser.add_option("-s","--submit",dest="submit", default=False,action="store_true",
                                       help="submit jobs to condor once they are configured  (default = %default)")

                                       
parser.add_option("-j","--firstJob",dest="firstJob", default=0,
                                       help="first job to submit  (default = %default)")
                                       


(options, args) = parser.parse_args()

if options.inputFile=="":
   raise Exception, 'No inputfile specified'

if options.outputDir=="":
    raise Exception, 'No ouput directory (-o) specified'
    

# fix malformed options
    
# verify specified options
print "inputFile: ", options.inputFile
print "nFiles: ",options.nFiles
print "submit: ",options.submit
print "firstJob: ",options.firstJob

# for data, get the (sorted) list of good runs from the json

# grab full file list from config files


readFiles = getattr(__import__("HLLHCSubstructure.TreeMaker."+options.inputFile+"_cff",fromlist=["readFiles"]),"readFiles")



# to keep track of how many data files have been divied up
fileListLen = len(readFiles)

print "There are "+str(fileListLen)+" files in your sample"

# calculate the number of jobs necessary

nJobs = fileListLen / int( options.nFiles )
if ( fileListLen % int( options.nFiles ) != 0 ) :
     nJobs += 1

netJobs = nJobs - int(options.firstJob)
print "I will create "+str(netJobs)+" jobs for you!"
if options.firstJob>0: print "(starting from job "+str(options.firstJob)+")"

# start loop over N jobs
nActualJobs = 0
for iJob in range( int(options.firstJob), nJobs ) :
    # get starting file number
    nstart = iJob*int(options.nFiles)

    # skipping data files with bad runs only works with nFiles==1 right now
    #if int(options.nFiles)==1:
        # check if this file's run is in the list of good runs
       # readFileSplit = readFiles[iJob].split('/')
        # some filenames don't have the run in them
        #if len(readFileSplit)==12:
         #   readFileRun = readFileSplit[8]+readFileSplit[9]
          #  i = bisect.bisect_left(runlist,readFileRun)
    
    # replace placeholders in template files
    print "Printing the file number: ",iJob
    jobname = options.inputFile+str(iJob)
    if nJobs>1: jobname = jobname+"_"+str(iJob)
    os.system("sed -e 's|CMSSWVER|'${CMSSW_VERSION}'|g' "\
                 +"-e 's~OUTDIR~"+options.outputDir+"~g' "\
                 +"-e 's|JOBNAME|"+jobname+"|g' "\
                 +"-e 's~INPUTFILE~"+options.inputFile+"~g' "\
                 +"-e 's|NSTART|"+str(nstart)+"|g' "\
                 +"-e 's|NFILES|"+str(options.nFiles)+"|g' "\
                 +"< jobExecCondor.jdl > jobExecCondor_"+jobname+".jdl")

    # submit jobs to condor, if -s was specified
    if ( options.submit ) :
        print " job submission"
        os.system("condor_submit jobExecCondor_"+jobname+".jdl")
        
    nActualJobs += 1
print "("+str(nActualJobs)+" actual jobs)"
