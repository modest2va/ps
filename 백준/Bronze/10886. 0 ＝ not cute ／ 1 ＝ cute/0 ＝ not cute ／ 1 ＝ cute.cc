#include<iostream>
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;

int main(){
int N;
 cin>>N;
 int cute=0;
 int noncute=0;
 for(int i=0;i<N;i++){
    int iscute;
    cin>>iscute;
    if(iscute==1){
        cute++;
    }
    else noncute++;
 }

 if(cute<noncute){
    cout<<"Junhee is not cute!";
 }
 else cout<<"Junhee is cute!";
return 0;
}
