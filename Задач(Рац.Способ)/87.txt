#include <iostream>
#include<algorithm>
#include<vector>
#include<climits>
using namespace std;
vector<vector<vector<int>>> v(200, vector <vector<int>>(200,vector<int>(200,INT_MIN)));
//vector<int>v(2000,INT_MIN);
int game(int x,int y,int z){
    if(v[x][y][z] != INT_MIN){
        return v[x][y][z];
    }
    if(x + y + z >= 73){
        return 0;
    }
    //3, 13 или 23 камня
    vector<int>neg,tmp={game(x+3,y,z), game(x+13,y,z),game(x+23,y,z), game(x,y+3,z),game(x,y+13,z), game(x,y+23,z), game(x,y,z+3),game(x,y,z+13),game(x,y,z+23)};
    for(auto x: tmp){
        if(x<=0){
            neg.push_back(x);
        }
    }
    int res;
    if(!neg.empty()){
        res = -*max_element(neg.begin(),neg.end())+1;
    } else {
        res = -*max_element(tmp.begin(),tmp.end());
    }
    return v[x][y][z]= res;
}

int main()
{
    //int c =0;
    for(int i = 1; i < 100; i++){
        if (game(2,i,2 * i) == 2){
        cout << "(" << 6 << " , " << i <<") " << game(2,i,2 * i) << endl;
        }
    }
}
