#include<bits/stdc++.h>
using namespace std;

int fibo(int n){
    if (n == 0 || n == 1) return n;
    return (fibo(n-2) + fibo(n-1));
}

int main(){
    int n, v; cin >> n;

    for(int i = 0; i < n; i++){
        v = fibo(i);
        cout << v << " ";
    }
    cout << endl;

    return 0;
}
