#include<iostream>
#include<string>
using namespace std;

int main(){
string tmp;
cin>>tmp;
int cnt=0;
while(tmp!="0"){
        int output=1;
    for(int i=0;i<4;i++){
        if(tmp[i]=='\0') break;
        switch(tmp[i]){
        case '1':
            output+=2;
            break;
        case '0':
            output+=4;
            break;
        default:
            output+=3;
            break;
        }

    }
    cout<<output+tmp.size()<<endl;
    cin>>tmp;
}
return 0;
}




