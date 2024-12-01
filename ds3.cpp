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
    int f = a[0], s = a[1]; // Initialize f and s with the first two elements
    l1 = 0; // Index of the largest element
    l2 = 1; // Index of the second largest element

    // Swap if the first element is smaller than the second
    if(f < s){
        swap(f, s);
        swap(l1, l2);
    }

    // Iterate through the rest of the array
    for(int i = 2; i < n; i++){
        if(a[i] > f){ // If current element is greater than the largest so far
            s = f; // Update second largest
            l2 = l1; // Update index of second largest
            f = a[i]; // Update largest
            l1 = i; // Update index of largest
        }else if(a[i] > s){ // If current element is greater than the second largest so far
            s = a[i]; // Update second largest
            l2 = i; // Update index of second largest
        }
    }

    // Print the results
    cout << "Largest element " << f << " is at " << l1 << " and second " << s << " is at " << l2 << endl;
}

int main(){
    int n; cin >> n;
    int a[n];
    for(int i = 0; i < n; i++) cin >> a[i];
    int l1, l2;
    find(a, n, l1, l2);
}