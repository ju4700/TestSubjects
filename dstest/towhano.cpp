#include<bits/stdc++.h>
using namespace std;

int i = 0;

int thanoi(int n, char a, char b, char c){
    if (n != 0){
        thanoi(n-1, a, c, b);
        i += 1;
        cout << "Move disk " << n << " from " << a << " to " << c << endl;
        thanoi(n-1, b, a, c);
    }
}

int main(){
    int n;
    cout << "Amount of disks: "; cin >> n;

    char a = 'A', b = 'B', c = 'C';
    thanoi(n, a, b, c);
    cout << endl;
    cout << "Total number of moves: " << i << endl;
}
