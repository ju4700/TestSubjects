#include<bits/stdc++.h>
using namespace std;

int main(){
    int adj[10][10];
    int n, i, j;
    cout << "Enter the number of vertices: "; cin >> n;

    for(i = 1; i <= n; i++){
        for(j = 1; j <= n; j++){
            cout << "Enter 1 if Verteci " << i << " has an edge with Verteci " << j << " else 0 : ";
            cin >> adj[i][j];
        }
    }
    cout << endl << "The Adjacency Matrix of The Graph: " << endl;
    for ( i = 1; i <= n; i++ ) {
        for ( j = 1; j <= n; j++ ) {
            cout << adj[i][j];
        }
        cout << endl;
    }
}
