#include<bits/stdc++.h>
using namespace std;

void find(int a[], int n, int x, int y){
    int maxi = a[0], k = 0;
    for(int i = 1; i < n; i++){
        if(a[i] > maxi){
            maxi = a[i];
            x = i;
        }
    }int secm = a[0];
    for (int i = 0; i < n; i++){
        if(a[i] < maxi && a[i] > secm){
            secm = a[i];
            y = i;
        }
    }
    cout << "Largest element "<< maxi << "is at " << x << " and  second " << secm << "is at " << y << endl;
}

int main(){
    int n; cin >> n;
    int a[n];
    for(int i = 0; i < n; i++) cin >> a[i];
    int l1, l2;
    find(a, n, l1, l2);
}