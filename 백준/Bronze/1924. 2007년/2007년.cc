#include<stdio.h>
#include<iostream>
#include<fstream>
#include<string>

using namespace std;

int zelle(int y, int m, int d)
{
    int k, j, h;

    if(m <= 2)
    {
        m += 12;
        y--;
    }

    k = y % 100;
    j = y / 100;
    h = 21*j/4 + 5*k/4 + 13*(m+1)/5 + d - 1;

    if(h < 0) h += 7;

    return h % 7;
}
//Zeller's congruence 첼러의 공식


int main(){
int M,D;
cin>>M;
cin>>D;

switch(zelle(2007,M,D)){
case 1:
    printf("MON");
    break;
case 2:
    printf("TUE");
    break;
case 3:
    printf("WED");
    break;
case 4:
    printf("THU");
    break;
case 5:
    printf("FRI");
    break;
case 6:
    printf("SAT");
    break;
case 0:
    printf("SUN");
    break;
}


return 0;
}

