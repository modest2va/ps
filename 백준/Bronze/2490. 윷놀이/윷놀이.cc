#include<iostream>
using namespace std;

int main(){

  for(int i=0; i<3;i++){
        int sum=0;
        int A,B,C,D;
    cin>>A>>B>>C>>D;
    sum=A+B+C+D;
  switch(sum){
case 3:
    cout<<"A";
    break;
case 2:
    cout<<"B";
    break;
case 1:
    cout<<"C";
    break;
case 0:
    cout<<"D";
    break;
case 4:
    cout<<"E";
    break;
  }
    printf("\n");
  }
    return 0;
}
