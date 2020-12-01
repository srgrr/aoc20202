#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <set>
using namespace std;

vector< int > solve_for_two(multiset< int >& input, int already) {
    int sum_need = 2020 - already;
    auto input_it = input.begin();

    while(input_it != input.end()) {
        int x = *input_it;
        int need = sum_need - x;
        input_it = input.erase(input_it);
        if(input.count(need)) {
            return {already, x, need};
        }
        input_it = input.insert(x);
        ++input_it;
    }

    return vector< int >();
}

int main() {
    ios_base::sync_with_stdio(0);
    ifstream ifs("input.txt");
    multiset< int > nums;
    int last_num;
    while(ifs >> last_num) nums.insert(last_num);
    auto nums_it = nums.begin();
    while(nums_it != nums.end()) {
        int x = *nums_it;    
        nums_it = nums.erase(nums_it);

        auto solution = solve_for_two(nums, x);

        if(!solution.empty()) {
            cout << solution[0] * solution[1] * solution[2] << endl;
            return 0;
        }

        nums_it = nums.insert(x);
        ++nums_it;
    }
}
