#include<bits/stdc++.h>
using namespace std;

void selection(vector<int>& arr, int n){
    for (int i = 0; i < n - 1; i++){
        int mini = i;
        for(int j = i + 1; j < n; j++){
            if(arr[j] < arr[mini]){
                mini = j;
            }
        }
        swap(arr[i], arr[mini]);
    }

}

int main(){
    vector<int> arr = {50, 20, 10, 55, 70, 60};
    int n = arr.size();

    for(int i: arr){
        cout << i << " ";
    } cout << endl;

    selection(arr, n);

    cout << "Sorted Array!" << endl;
    for(int i: arr){
        cout << i << " ";
    } cout << endl;

    return 0;
}
