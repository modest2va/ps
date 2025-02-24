#include<iostream>
using namespace std;

int main(){
    int A,B,C;
    cin>>A>>B>>C;
   if((B-A)<(C-B)){
       cout<< C-(B+1);
   }
   else cout<< (B-1)-A;
    return 0;
}
