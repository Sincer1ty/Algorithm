#include <vector>
#include <unordered_set>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxSum(vector<int>& nums) {
        int result = 0;
        unordered_set<int> s;
        for (int n : nums) {
            // 유일한 요소로만
            if (s.insert(n).second && n > 0) {
                result += n;
            }
        }

        if (result == 0) {
            result = *max_element(nums.begin(), nums.end());
        }

        return result;
    }
};