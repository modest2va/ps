#include<iostream>
#include<cmath>
using namespace std;
int main() {
int ans=0;
int N;
cin>>N;
for(int i=0; i<N;i++){
    int tmp;
    cin>>tmp;

    ans+=pow(tmp/10,tmp%10);
    //cout<<"Current : "<<pow(tmp/10,tmp%10);
}
cout<<ans;
return 0;
}




