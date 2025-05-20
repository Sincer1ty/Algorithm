#include <vector>

using namespace std;

class Solution {
public:
    bool isZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
        vector<int> diff(nums.size(), 0);
        
        for (int i = 0; i < queries.size(); i++) {
            int r = queries[i][1];
            diff[queries[i][0]] -= 1;

            if (r + 1 < nums.size()) diff[r + 1] += 1;
        }

        int apply = 0;
        for (int i = 0; i < nums.size(); i++) {
            apply += diff[i];
            if (nums[i] + apply > 0) return false;
        }

        return true;
    }
};
