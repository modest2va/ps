#include<iostream>
#include<vector>
#include<string>
#include<math.h>
using namespace std;
int main() {
int N;
double A,B;
cin>>N>>A>>B;
while(N--){
    int tmp;
    cin>>tmp;

    if(tmp<=max(max(A,B),sqrt(A*A+B*B))){
        printf("DA\n");
    }
    else printf("NE\n");
}
    return 0;
}