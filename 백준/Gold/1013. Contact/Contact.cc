#include<iostream>
#include<stdio.h>
#include<regex>
#include<string>
using namespace std;
int main(){

regex myRegex("(100+1+|01)+");
int testCase;
cin>>testCase;
for(int i=0; i<testCase;i++){
        string myString;
        smatch m;
cin>>myString;
    if(regex_match(myString,m,myRegex)){
        cout<<"YES"<<endl;

    }
    else cout<<"NO"<<endl;
}

return 0;
}
