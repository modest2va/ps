#include<stdio.h>
#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int main(){
int N;

scanf("%d",&N);

        for(int k=1; k<10;k++)
            printf("%d * %d = %d\n",N,k,N*k);

return 0;
}
