#include <vector>
#include <math.h>

using namespace std;

class Solution {
public:
    int maxAdjacentDistance(vector<int>& nums) {
        int max = 0;

        for (int i = 0; i < nums.size(); i++) {
            int cmp = (i + 1) % nums.size();
            int diff = abs(nums[i] - nums[cmp]);
            if (max < diff) max = diff;
        }

        return max;
    }
};