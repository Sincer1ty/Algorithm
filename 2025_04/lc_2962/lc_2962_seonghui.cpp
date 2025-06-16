#include <vector>

using namespace std;

class Solution {
public:
	long long countSubarrays(vector<int>& nums, int k) {
		long long result = 0;
		int max = 0;
		// max 가 들어있는 위치를 알아두기
		vector<int> maxIdxs;

		for (int i = 0; i < nums.size(); i++) {
			if (max < nums[i]) {
				max = nums[i];
				maxIdxs = {i};
				result = 0;
			}
			else if (max == nums[i]){
				maxIdxs.push_back(i);
			}

			if (maxIdxs.size() >= k) {
				result += maxIdxs[maxIdxs.size() - k] + 1;
			} 
		}
		return result;
	}
};
