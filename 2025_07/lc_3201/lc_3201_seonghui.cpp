#include <vector>

using namespace std;

class Solution {
public:
    int maximumLength(vector<int>& nums) {
		bool isPrevOdd = nums[0] % 2;
		int odd = isPrevOdd, even = !isPrevOdd, alternating = 0;
		for (int i = 1; i < nums.size(); ++i) {
			// 홀수
			if (nums[i] % 2) {
				++odd;
				if (!isPrevOdd) ++alternating;

				isPrevOdd = true;
			}
			else {
				if (isPrevOdd) {
					++alternating;
				}
				++even;
				isPrevOdd = false;
			}
		}

		return max(max(odd, even), alternating + 1);
    }
};
