#include<iostream>
#include<algorithm>
#include<string>
using namespace std;
int myarr[100][100];

int main() {
  int a,c,d;
  int cnt=0;
  cin>>a;
  while(a--){
    cin>>c>>d;
    for(int i=c;i<c+10;i++)
        for(int j=d;j<d+10;j++)
           myarr[i][j]=1;
  }
for(int i=0;i<100;i++){
        for(int k=0;k<100;k++){
            if(myarr[i][k]==1){
                cnt++;
                                }
                }
            }
    cout<<cnt;
    return 0;
}




