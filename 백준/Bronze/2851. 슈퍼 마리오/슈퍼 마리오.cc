#include<iostream>
#include<vector>
#include<math.h>
using namespace std;
int main() {
vector<int>v1;
    int tmp=0;
    int that=0;
for(int i=0;i<10;i++){
    int A;
    cin>>A;
    tmp+=A;
    v1.push_back(A);
    if(tmp>=100){
        that=i;

        break;
    }
}
    if(abs(100-tmp)==abs(100-tmp+v1[that])){
       cout<<tmp;
       }
    else if(abs(100-tmp)<abs(100-tmp+v1[that])){
            cout<<tmp;
            }
    else if(abs(100-tmp)>abs(100-tmp+v1[that])){
            cout<<tmp-v1[that];}
    return 0;
}




