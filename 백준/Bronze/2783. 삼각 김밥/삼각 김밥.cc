#include<iostream>
using namespace std;
int main() {
double A,B;
cin>>A>>B;
double samgak=A*1000/B;
int N;
cin>>N;
for(int i=0; i<N;i++){
    cin>>A>>B;
    if(samgak>A*1000/B) samgak=A*1000/B;
}

printf("%.2f",samgak);
return 0;
}




