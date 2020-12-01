#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    ifstream ifs("input.txt");
    vector< int > nums;
    int last_num;
    while(ifs >> last_num) nums.push_back(last_num);
    sort(nums.begin(), nums.end());
    int ans = 0;
    for(int i = 0; i < int(nums.size()); ++i) {
        int have = nums[i];
        int need = 2020 - have;
        if(binary_search(nums.begin(), nums.begin() + i, need) || binary_search(nums.begin() + i + 1, nums.end(), need)) {
            cout << have * need << endl;
            return 0;
        }
    }
}
