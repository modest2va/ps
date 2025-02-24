#include<iostream>
#include<stdio.h>

using namespace std;
int main(){
int N;
cin>>N;
int cnt=0;
for(int i=0; i<5;i++){
    int carNum;
    cin>>carNum;
    if(N==carNum){
        cnt++;
    }
}

printf("%d",cnt);

return 0;
}
