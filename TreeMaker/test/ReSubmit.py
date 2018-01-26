import os
import sys


import os, bisect
from optparse import OptionParser
from FWCore.PythonUtilities.LumiList import LumiList

# define options
parser = OptionParser()

parser.add_option("-i", "--inputFile", dest="inputFile", default="",
                                    help="inputfile name (default = %default)")
#parser.add_option("-o", "--outputFile", dest="outputFile", default="",
#                                    help="outputFile  name (default = %default)")


(options, args) = parser.parse_args()

if options.inputFile=="":
   raise Exception, 'No inputfile specified'


#outputDir="/eos/uscms/store/user/bmahakud/ObjectPGENSIMRECO_SDzcut0p15"
outputDir="/eos/uscms/store/user/bmahakud/HGCALLHCCTuples_v1"
outputFile= options.inputFile+"*_.root";#"GENSIM.RSGluonToTT_M-3000_TuneCUETP8M1_14TeV-pythia8GENSIMRECO_NoPU0_.root"


readFiles = getattr(__import__("HLLHCSubstructure.TreeMaker."+options.inputFile+"_cff",fromlist=["readFiles"]),"readFiles")

print "total number of inputFiles on whihc jobs are submitted: ",len(readFiles)

FilesList=[]
FilesList=readFiles
listOfile = "ls -1 %s/%s > Outfile.dat"%(outputDir,outputFile)
os.system(listOfile)

InputROOTfiles="Outfile.dat"

with open(InputROOTfiles) as f:
     content = f.readlines()
content = [x.strip() for x in content]

#print "Num of jobs completed: ",len(content)
successJobs=[]

for line in range(0,len(content)):
    num_=content[line].count('_')
    Jobstr=content[line].split('_')[num_-1]
    jobnum=""
    if "NoPU" in Jobstr:
       jobnum=Jobstr.replace("NoPU","")
    if "PU200" in Jobstr:
       jobnum=Jobstr.replace("PU200","")
    successJobs.append(jobnum)

print "number of successful jobs: ",len(successJobs)

#print "successJobs: ",successJobs
count=0
subFileName="jobExecCondor_"+options.inputFile

for isub in range(0, len(FilesList)):
   #print isub
   jobnum=str(isub)
   resubjobs = "condor_submit "+subFileName+str(isub)+"_"+str(isub)+".jdl"
   if jobnum  not  in successJobs:
         #os.system(resubjobs);
         print "submitting job: ",resubjobs
         #os.system(resubjobs);
         count=count+1


print "number of failed jobs  submitted for "," dataset",": ",count
print "......................................"





