#include<stdio.h>
#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#define MAXSIZE 10000
using namespace std;
int selfNumber(int N){
    int newN=N;
    for(int i=0; i<5; i++){
        newN=newN+N%10;
        N/=10;
        if(N==0){
            break;
        }
    }
    return newN;
}

int main(){
vector <int>myVec;
for(int i=0; i<MAXSIZE;i++){
    myVec.push_back(0);
}

for(int i=0;i<MAXSIZE;i++){
if(selfNumber(i)<=MAXSIZE){
    myVec[selfNumber(i)]=selfNumber(i);

        }
}
myVec[0]=1;
for(int i=0; i<MAXSIZE;i++){
    if(myVec[i]==0){
        printf("%d\n",i);
    }
}

return 0;
}

