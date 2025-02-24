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
    int N,R;
    cin>>N>>R;
    for(int i=0;i<N-1;i++){
        int A;
    cin>>A;
        cout<<R/gcd(R,A)<<"/"<<A/gcd(R,A)<<endl;
    }

return 0;
}
