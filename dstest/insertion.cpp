#include<bits/stdc++.h>
using namespace std;

void insertion(vector<int>& arr, int n){
    for(int i = 1; i < n; i++){
        int key = arr[i];
        int j = i - 1;

        while(j >= 0 && arr[j] > key){
            arr[j+1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

int main(){
    vector<int> arr = {50, 20, 10, 55, 70, 60};
    int n = arr.size();

    for(int i: arr){
        cout << i << " ";
    } cout << endl;

    insertion(arr, n);

    cout << "Sorted Array!" << endl;
    for(int i: arr){
        cout << i << " ";
    } cout << endl;

    return 0;
}
