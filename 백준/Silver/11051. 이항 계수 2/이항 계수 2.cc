#include<iostream>
using namespace std;

int B[1001][1001];
int main(){
    int N,K;
    cin >>N>>K;
    for(int i=0; i<=N;i++){
        for(int j=0; j<=min(i,K); j++){
            if(j==0||j==i) B[i][j]=1;
            else B[i][j]= (B[i-1][j-1]+B[i-1][j])%10007;
        }
    }
printf("%d",B[N][K]);

}
