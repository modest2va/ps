#include<iostream>
#include<stdio.h>

using namespace std;
int gcd(int a,int b){

    while(1){
        int r;
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
int gcm(int a,int b){
return a*b/gcd(a,b);
}
int main()
{	int N;
cin>>N;
for(int i=0; i<N;i++){
        int a,b;
    cin>>a>>b;
    cout<<gcm(a,b)<<endl;
}
return 0;
}
