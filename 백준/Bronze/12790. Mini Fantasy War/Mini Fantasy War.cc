#include<iostream>
#include<stdio.h>

using namespace std;

int main(){
int N;
 cin>>N;
for(int i=0; i<N;i++){
    int hp,mp,att,def,fight=0;
    int tmp1,tmp2,tmp3,tmp4,tmp5,tmp6,tmp7,tmp8;
    cin>>tmp1>>tmp2>>tmp3>>tmp4>>tmp5>>tmp6>>tmp7>>tmp8;
    hp=tmp1+tmp5;
    if(hp<1){
        hp=1;
    }
    mp=tmp2+tmp6;
    if(mp<1){
        mp=1;
    }
    att=tmp3+tmp7;
    if(att<0){
        att=0;
    }
    def=tmp4+tmp8;
    cout<<hp+5*mp+2*att+2*def<<endl;

}
return 0;
}
