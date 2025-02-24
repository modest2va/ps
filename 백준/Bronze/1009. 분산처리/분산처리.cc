#include<iostream>
#include<stdio.h>
#include<math.h>
using namespace std;

int main(){
int N;
cin>>N;

for(int i=0; i<N;i++){
    int A,B;
    cin>>A>>B;
    int test=1;
    for(int k=0; k<B;k++){
        test=test*A%10;
    }

    if(test%10==0) printf("10\n");
    else printf("%d\n",test%10);
}

return 0;
}
