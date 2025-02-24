#include<iostream>
#include<cmath>

using namespace std;
int main() {
 int A,B,C,D,P;
 cin>>A>>B>>C>>D>>P;
 int X,Y;
 X=A*P;
 if(P>C){
    Y=B+(P-C)*D;
 }
 else{
    Y=B;
 }
printf("%d",min(X,Y));

    return 0;
}




