#include<iostream>
#include<vector>
#include<string>
#include<stdio.h>
#include<cstring>
using namespace std;
int summ(int K){
    int sum=0;
if(K==1){
   sum=1;
}
else{
    for(int m=1; m<=K;m++){
        sum+=m;
    }
}
return sum;
}

int main(){
int N;
cin>>N;
int odd=0;



int gun;
if(N==1){
    cout<<"1/1";
    return 0;
}
for(int i=1;i<10000000;i++){

    if((summ(i)<N)&&(N<=summ(i+1))){
        //printf("%d",i+1);
        gun=i+1;
        //cout<<gun;
        break;
    }
}
if(gun%2==1){
    odd=1;
}
//cout<<"몇 군인지: "<<gun<<endl;
//cout<<"몇 번째인지: "<<N-summ(gun-1)<<endl;

if(odd==0){
    cout<<N-summ(gun-1)<<"/"<<gun-(N-summ(gun-1))+1;
}
else{
    cout<<gun-(N-summ(gun-1))+1<<"/"<<N-summ(gun-1);
}
return 0;
}


