#include <iostream>
#include <fstream>

using namespace std;

void PrintWeight(){
ifstream inFile;
inFile.open("EventInfo.dat");

string pName;
double EvNum;
double xsec;
for(int i=0;i<7;i++){
inFile>>pName>>EvNum>>xsec;
//cout<<"Sample Name: "<<pName<<"  "<<EvNum<<"  "<<xsec<<endl;

double Weight=0;
Weight=(xsec*300000)/EvNum;

cout<<pName<<"   "<<Weight<<endl;


}











}
