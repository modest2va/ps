#include<iostream>
#include<algorithm>
#include<string>
using namespace std;
string s[1000000];
int n, m, r;
int main() {
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n + m; i++) cin >> s[i];
    sort(s, s + n + m);
    for (int i = 1; i < n + m; i++) r += s[i] == s[i - 1];
    cout << r << endl;
    for (int i = 1; i < n + m; i++) if (s[i] == s[i - 1]) cout << s[i] << endl;
    return 0;
}
