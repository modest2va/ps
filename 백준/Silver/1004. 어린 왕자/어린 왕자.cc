#include<iostream>
#include<stdio.h>
#include<math.h>
using namespace std;
int isInCircle(int X, int Y, int cirX, int cirY, int cirR){
if((X-cirX)*(X-cirX)+(Y-cirY)*(Y-cirY)<cirR*cirR){
    return 1;
}
if((X-cirX)*(X-cirX)+(Y-cirY)*(Y-cirY)>cirR*cirR){
    return -1;
}
}
int main(){
int N;
cin>>N;

for(int i=0; i<N;i++){
    int myX, myY,myX2,myY2;
    cin>>myX>>myY>>myX2>>myY2;
    int circnt;
    cin>>circnt;
    int inCnt=0;
    for(int k=0; k<circnt;k++){
            int cirX,cirY,cirR;
            cin>>cirX>>cirY>>cirR;
       if(isInCircle(myX,myY,cirX,cirY,cirR)*(isInCircle(myX2,myY2,cirX,cirY,cirR))==-1) inCnt++;

    }

    cout<<inCnt<<endl;

}
return 0;
}
