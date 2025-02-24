#include<iostream>
#include<stdio.h>
#include<vector>
using namespace std;
int main(){
int totalnum;
cin>>totalnum;


for(int i=0; i<9;i++){
    int N;
    cin>>N;

    totalnum-=N;
}


cout<<totalnum;

return 0;
}
