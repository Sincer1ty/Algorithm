#include <vector>

using namespace std;

class Solution {
public:
    int maximumDifference(vector<int>& nums) {
		// 없으면 -1
		int max = -1;

		for (int i = 0; i < nums.size(); i++) {
			for (int j = i+1; j < nums.size(); j++) {
				int cmp = nums[j] - nums[i];
				if (cmp != 0 && max < cmp) max = cmp;
			}
		}

		return max;
    }
};