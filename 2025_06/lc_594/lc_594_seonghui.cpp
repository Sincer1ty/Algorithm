#include <vector>

using namespace std;

class Solution {
public:
    int findLHS(vector<int>& nums) {
		// 정렬
		sort(nums.begin(), nums.end());

		int prev = nums[0], prev_dup = 0, dup = 1, result = 0;
		for (int i = 1; i < nums.size(); i++) {
			// 중복 개수 세기
			if (prev == nums[i]) {
				dup += 1;
				continue;
			}

			if (prev_dup && prev_dup + dup > result) {
				result = prev_dup + dup;
			}
			
			if (nums[i] - prev == 1) prev_dup = dup;
			else prev_dup = 0;

			dup = 1;			
			prev = nums[i];
		}

		if (prev_dup && prev_dup + dup > result) result = prev_dup + dup;

		return result;
    }
};
