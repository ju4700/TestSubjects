#include <bits/stdc++.h>
using namespace std;

int main() 
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    
    string s; cin >> s;
    string p; cin >> s;

    int k = 0; int maxi = s.length() - p.length();
    while(k <= maxi){
        int i;
        for(i = 0; i < p.length(); i++){
            if(s[k + i] != p[i]){
                break;
            }
        } if (i == p.length()){
            cout << "Pattern found at index " << k << endl;
        }
    }


    return 0; 
}