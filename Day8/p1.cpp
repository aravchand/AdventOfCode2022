#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main() {
    // freopen("sample.in", "r", stdin);
    freopen("input.in", "r", stdin);
    
    string line;
    vector<string> forest;
    while(cin >> line) {
        forest.push_back(line);
    }
    int n = forest.size(); // its a square, nxn
    cout << n << "\n";
    vector<vector<bool>> visible(n, vector<bool>(n));
    /*tried to think about generalizing 
    but we require to have gotten all the trees in resp.
    direction to do this way.. cannot really do in 1 set of loop
    */
    // int dx[4] = {1, 0, -1, 0};
    // int dy[4] = {0, 1, 0, -1};
    // vector<vector<bool>> fromdir[4];
    // for(int i = 0; i < 4; i++) {
    //     fromdir[i] = vector<vector<bool>>(n, vector<bool>(n));
    // }
    
    // for(int i : {0, n-1})
    //     for(int j = 0; j < n; j++) {
    //         visible[i][j] = 1;
    //         visible[j][i] = 1;
    //     }
    
    // vertically
    for(int j = 0; j < n; j++) {
        char mx = '0'-1;
        for(int i = 0; i < n; i++) {
            if (forest[i][j] > mx) {
                visible[i][j] = 1;
                mx = forest[i][j];
            }
            // for time complexity if we wanted to:
            if (mx == '9') break; // since when equal heights, further is not visible 
        }
        mx = '0' - 1;
        for(int i = n-1; i >= 0; i--) 
            if (forest[i][j] > mx) {
                visible[i][j] = 1;
                mx = forest[i][j];
            }
    }
    

    for(int i = 0; i < n; i++) {
        char mx = '0'-1;
        for(int j = 0; j < n; j++) 
            if(forest[i][j] > mx) {
                visible[i][j] = 1;
                mx = forest[i][j];
            }
        
        mx = '0' - 1;
        for(int j = n-1; j >= 0; j--) 
            if(forest[i][j] > mx) {
                visible[i][j] = 1;
                mx = forest[i][j];
            }
            
    }
    
    // print visible
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            cout << visible[i][j];
        }
        cout << "\n";
    }
    
    int ans = 0; // edges
    for(int i = 0; i < n; i++)
        for(int j = 0; j < n; j++)
            ans += visible[i][j];

    
    cout << ans << "\n";
}