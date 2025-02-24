#include<iostream>
#include<vector>
#include<string>
#include<stdio.h>
#include<cstring>
using namespace std;

int main(){
string N;
cin>>N;
int cnt=0;
for(int i=0;i<100;i++){
    if(N[i]=='\0'){
        break;
    }
    if(N[i]=='='){
        switch (N[i-1]){
    default:
        break;
            case 'c':
            case 's':

                cnt--;
                break;
            case 'z':
                if(N[i-2]=='d'){
                    cnt-=2;
                }
                else{
                    cnt--;
                }

                        }
    }
    if(N[i]=='-'){
        switch(N[i-1]){
        default:
            break;
        case 'c':
        case 'd':
            cnt--;
            break;
        }
    }
    if(N[i]=='j'){
        switch(N[i-1]){
        default:
            break;
        case 'l':
        case 'n':
            cnt--;
            break;
        }
    }
    cnt++;
}
printf("%d",cnt);
return 0;
}


