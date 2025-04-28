#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
	long long countSubarrays(vector<int>& nums, long long k) {
		long long count = 0, sum = 0;
		int idx = 0;

		for (int i = 0; i < nums.size(); i++) {
			sum += nums[i];

			// 길이 : i + 1
			int length = i + 1 - idx;
			long long score = sum * length;
			
			while (score >= k) {
				sum -= nums[idx];
				idx += 1;
				
				length = i + 1 - idx;
				score = sum * length;
				
			}
			
			count += length;
		}

		return count;
	}
};
