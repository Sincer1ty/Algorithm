#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
	long long countInterestingSubarrays(vector<int>& nums, int modulo, int k) {
		long long result = 0, cnt = 0;
		unordered_map<int, long long> dict;

		dict[0] = 1;
		
		for (int i = 0; i < nums.size(); i++) {
			if (nums[i] % modulo == k) cnt += 1;

			int mod = cnt % modulo;
			int target = (mod - k + modulo) % modulo;
			result += dict[target];
			dict[mod] += 1;
		}

		return result;
	}
};
