#include<iostream>
using namespace std;
int main() {
    int A,B,C,A2,B2,C2;
for(int i=0; i<3;i++){
    cin>>A>>B>>C>>A2>>B2>>C2;
        int h,m,s;
    if(C>C2){
        B2=B2-1;
        s=C2-C+60;
    }
    else s=C2-C;

    if(B>B2){
        A2=A2-1;
        m=B2-B+60;
    }
    else m=B2-B;
    h=A2-A;

    cout<<h<<" "<<m<<" "<<s<<endl;
}

return 0;
}




