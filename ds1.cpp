#include <bits/stdc++.h>
using namespace std;

int main(){
    int a, b, c; cin >> a >> b >> c;
    int  d = b*b - 4*a*c;
    int x, y;
    if(d > 0){
        x = (-b + sqrt(d))/(2*a);
        y = (-b - sqrt(d))/(2*a);
        cout << "Two Real Roots: " << x << " " << y << endl;
    }else if(d == 0){
        x = -b/(2*a);
        cout << "One Real Root: " << x << endl;
    }else{
        cout << "No Real Roots" << endl;
    }
}