#include<iostream>

using namespace std;
int main() {
int A=0;
int B=0;
for(int i=0;i<4;i++){
    int tmp;
    cin>>tmp;
    A+=tmp;
}
for(int i=0;i<4;i++){
    int tmp;
    cin>>tmp;
    B+=tmp;
}
cout<<max(A,B);

return 0;
}




