#include<bits/stdc++.h>
using namespace std;

// void find(int a[], int n, int x, int y){
//     int maxi = a[0], k = 0;
//     for(int i = 1; i < n; i++){
//         if(a[i] > maxi){
//             maxi = a[i];
//             x = i;
//         }
//     } int secm = a[0];
//     for (int i = 0; i < n; i++){
//         if(a[i] < maxi && a[i] > secm){
//             secm = a[i];
//             y = i;
//         }
//     }
//     cout << "Largest element "<< maxi << "is at " << x << " and  second " << secm << "is at " << y << endl;
// }

void find(int a[], int n, int l1, int l2){
    int f = a[0], s = a[1];
    l1 = 0;
    l2 = 1;
    if(f < s){
        swap(f, s);
        swap(l1, l2);
    }
    for(int i = 2; i < n; i++){
        if(a[i] > f){
            s = f;
            l2 = l1;
            f = a[i];
            l1 = i;
        }else if(a[i] > s){
            s = a[i];
            l2 = i;
        }
    }
    cout << "Largest element " << f << " is at " << l1 << " and second " << s << " is at " << l2 << endl;
}

int main(){
    int n; cin >> n;
    int a[n];
    for(int i = 0; i < n; i++) cin >> a[i];
    int l1, l2;
    find(a, n, l1, l2);
}