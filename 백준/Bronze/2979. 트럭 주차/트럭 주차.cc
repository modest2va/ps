#include<iostream>
#include<vector>
using namespace std;
int main(){
int A,B,C;
int v1[3][101]={0};
cin>>A>>B>>C;
int cnt=0;
for(int i=0;i<3;i++){
    int a,b;
    cin>>a>>b;
    for(int k=a;k<b;k++){
        v1[i][k]=1;
    }
}
for(int i=0; i<101;i++){
    switch(v1[0][i]+v1[1][i]+v1[2][i]){
    default:
        cnt+=0;
        break;
    case 1:
        cnt+=A ;
        break;
    case 2:
        cnt+=2*B;
        break;
    case 3:
        cnt+=3*C;
        break;
    }
}
cout<<cnt;
return 0;
}




