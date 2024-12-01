#include<bits/stdc++.h>
using namespace std;

int main(){
    int r1, c1; cin >> r1 >> c1;
    int ar1[r1][c1];
    for(int i = 0; i < r1; i++){
        for(int j = 0; j < c1; j++){
            cin >> ar1[i][j];
        }
    }
    int r2, c2; cin >> r2 >> c2;
    int ar2[r2][c2];
    for(int i = 0; i < r2; i++){
        for(int j = 0; j < c2; j++){
            cin >> ar2[i][j];
        }
    }
    int res[r1][c2];
    if(c1 != r2){
        cout << "Multiplication not possible" << endl;
    } else {
        for(int i = 0; i < r1; i++){
            for(int j = 0; j < c2; j++){
                res[i][j] = 0;
                for(int k = 0; k < c1; k++){
                    res[i][j] += ar1[i][k] * ar2[k][j];
                }
            }
        }
        for(int i = 0; i < r1; i++){
            for(int j = 0; j < c2; j++){
                cout << res[i][j] << " ";
            }
            cout << endl;
        }
    }
}