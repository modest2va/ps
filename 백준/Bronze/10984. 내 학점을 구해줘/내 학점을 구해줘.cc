#include<iostream>
using namespace std;
int main() {
int N;
cin>>N;
while(N--){
    int semN;
    cin>>semN;
    double total=0;
    double gradeNum=0;
    while(semN--){
        double A,B;
    cin>>A>>B;
    gradeNum+=A;
    total+=B*A;

    }
    printf("%.0f %.1f\n",gradeNum,total/gradeNum);
}
    return 0;
}




