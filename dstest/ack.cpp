#include<bits/stdc++.h>
using namespace std;

int ack(int m, int n){
    if (m == 0) return n + 1;
    else if (m != 0 && n == 0) return ack(m - 1, 1);
    else return ack(m - 1, ack(m, n - 1));
}

int main(){
    int m, n, v;

    cout << "Input for m: "; cin >> m;
    cout << "Input for n: "; cin >> n;

    v = ack(m, n); cout << v;
    cout << "Value of A(" << m << ", " << n << ") is: " << v << endl;

    return 0;
}

