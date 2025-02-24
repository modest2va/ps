#include<iostream>
using namespace std;
int main(){
int N;
cin>>N;
for(int i=0; i<N; i++){
    int tmp1,tmp2;
    cin>>tmp1>>tmp2;
    cout<<"You get "<<tmp1/tmp2<<" piece(s) and your dad gets "<<tmp1%tmp2<<" piece(s).\n";
}
return 0;
}




