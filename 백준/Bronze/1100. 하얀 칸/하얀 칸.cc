#include<iostream>
#include<vector>
#include<string>
using namespace std;

int main(){
string arr[8][8];
int cnt=0;
for(int i=0;i<8;i++){
    for(int k=0;k<8;k++){
        char tmp;
        cin>>tmp;
        if(i%2==0&&k%2==0&&tmp=='F')cnt++;
        if(i%2==1&&k%2==1&&tmp=='F') cnt++;
    }
}

cout<<cnt;
return 0;
}




