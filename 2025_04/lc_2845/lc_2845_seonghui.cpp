#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
	long long countInterestingSubarrays(vector<int>& nums, int modulo, int k) {
		int result = 0, temp;
		vector<int> validCnts;
		unordered_map<int, int> dict;
		
		if (k == 0) validCnts.push_back(0);
		
		for (int i = 1; i <= nums.size(); i++) {
			temp = 0;
			for (int j = i; j <= nums.size(); j++) {
				if (nums[j-1] % modulo == k) {
					temp += 1;
					if (temp % modulo == k) {
						validCnts.push_back(temp);
					}
				}
				if (dict.find(temp) == dict.end()) {
					dict[temp] = 1;
				}
				else dict[temp] += 1;
			}
		}

		for (int i = 0; i < validCnts.size(); i++) {
			result += dict[validCnts[i]];
		}

		return result;
	}
};
