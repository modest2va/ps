#include<iostream>
#include<vector>
#include<math.h>
using namespace std;
int main() {
int A,B,C;
cin>>A>>B>>C;

while(A!=0&&B!=0&&C!=0){
    vector <int>v1;
    v1.push_back(A);
    v1.push_back(B);
    v1.push_back(C);
    for(int i=0;i<9;i++){
        for(int k=0;k<2;k++){
            if(v1[k]>v1[k+1]){
                    int tmp;
                    tmp=v1[k];
                    v1[k]=v1[k+1];
                    v1[k+1]=tmp;
            }
        }
    }
    if(v1[0]*v1[0]+v1[1]*v1[1]==v1[2]*v1[2]) cout<<"right"<<endl;
    else    cout<<"wrong"<<endl;
    cin>>A>>B>>C;
}

return 0;
}




