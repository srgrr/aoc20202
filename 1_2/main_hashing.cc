#include <unordered_set>
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

const int anti = 0b11101100111100000100010110100;

int main() {
    ios_base::sync_with_stdio(false);
    ifstream ifs("input.txt");
    unordered_set< int > S;
    vector< int > nums;
    int last_num;
    while(ifs >> last_num) {
        nums.push_back(last_num);
        S.insert(nums.back());
    }
    int n = int(nums.size());
    for(int i = 0; i < n; ++i) {
        for(int j = i + 1; j < n; ++j) {
            int need = 2020 - nums[i] - nums[j];
            S.erase(nums[i]);
            S.erase(nums[j]);
            if(S.count(need)) {
                cout << need * nums[i] * nums[j] << endl;
                return 0;
            }
            S.insert(nums[i]);
            S.insert(nums[j]);
        }
    }
}
