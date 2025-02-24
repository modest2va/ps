#include<iostream>
using namespace std;


int main() {

int N;
cin>>N;
while(N--){
    int A,B,C;
    cin>>A>>B>>C;
    if(B-C>A) printf("advertise\n");
    else if(B-C==A) printf("does not matter\n");
    else printf("do not advertise\n");
}

    return 0;
}




