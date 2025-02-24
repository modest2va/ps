#include<iostream>
#include<stdio.h>

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
        long long int a,b;
    cin>>a>>b;
    cout<<gcm(a,b)<<endl;

return 0;
}
