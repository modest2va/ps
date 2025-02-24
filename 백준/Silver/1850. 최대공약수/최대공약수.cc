#include<iostream>
#include<stdio.h>
#include<cmath>

using namespace std;
long long int gcd(long long int a,long long int b){

    while(1){
        long long int r;
        r=b%a;
        if(r==0){
            return a;
        }
        else{
            b=a;
            a=r;
        }
    }
}
long long int gcm(long long int a,long long int b){
return a*b/gcd(a,b);
}
int main()
{
    long long N,M;
    cin>>N>>M;
    for(int i=0; i<gcd(N,M); i++){
        cout<<1;
    }


return 0;
}
