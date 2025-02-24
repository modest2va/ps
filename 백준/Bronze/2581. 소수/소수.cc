#include<iostream>
#include<vector>
#include<string>
#include<stdio.h>
#include<cstring>
#include<math.h>
using namespace std;
int isPrime(int N){
int cnt=0;
    for(int i=1;i<=N;i++){
        if(N%i==0){
            cnt++;
        }
    }
    if(cnt==2){
        return 1;
    }
    else{
        return 0;
    }

}
int main(){
  int N,M;
  cin>>N;
  cin>>M;
  vector <int>prime;
  int cnt2=0;
  for(int i=N;i<=M;i++){
    if(isPrime(i)==1){
            cnt2+=i;
            prime.push_back(i);
    }
  }
  if(cnt2==0){
    cout<<-1;
  }
    else{
  cout<<cnt2<<endl;
  cout<<prime[0];
        }
return 0;
}





