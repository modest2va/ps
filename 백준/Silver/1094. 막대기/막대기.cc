#include<iostream>
#include<stdio.h>
#include<cmath>
#include<vector>

using namespace std;
int convertTwo(int number){
int answer=0;
for(int i=1;number>0;i*=10){
    int bin=number%2;
    answer+=bin*i;
    number/=2;
}
return answer;
}
int main(){
    int N;
    cin>>N;
    int result=0;
    int converted=convertTwo(N);
    for(int i=1; i<=7;i++){
        if(converted==0){
            break;
        }
        if(converted%10==1){
            result++;
        }

        converted/=10;
    }
    printf("%d",result);
return 0;
}
