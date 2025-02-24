#include<iostream>
#include<vector>
#include<string>
using namespace std;
int main() {
int ascii[26]={0};
int N;
cin>>N;
while(N--){
string tmp;
cin>>tmp;
ascii[tmp[0]-97]++;
}
int tmpcnt=0;
    for(int i=0;i<26;i++){
        if(ascii[i]>=5){
        printf("%c",i+97);
        tmpcnt=1;
        }
    }
    if(tmpcnt==0){
        printf("PREDAJA");
    }

    return 0;
}




