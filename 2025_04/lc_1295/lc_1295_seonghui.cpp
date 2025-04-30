#include <vector>

using namespace std;

class Solution {
public:
	int findNumbers(vector<int>& nums) {
		int count = 0;

		for (int i = 0; i < nums.size(); i++) {
			int digits = 1;
			while (nums[i] >= 10){
				nums[i] /= 10;
				digits += 1;
			}
			if (digits % 2 == 0) count += 1;
		}

		return count;
	}
};
