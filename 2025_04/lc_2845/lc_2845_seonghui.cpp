#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
	long long countInterestingSubarrays(vector<int>& nums, int modulo, int k) {
		int result = 0;
		vector<int> validCnts;
		vector<vector<int>> matrix(nums.size()+1, vector<int>(nums.size()+1, 0));
		unordered_map<int, int> dict;
		
		if (k == 0) validCnts.push_back(0);
		
		for (int i = 1; i <= nums.size(); i++) {
			for (int j = i; j <= nums.size(); j++) {
				if (nums[j-1] % modulo == k) {
					matrix[i][j] = matrix[i][j-1] + 1;
					if (matrix[i][j] % modulo == k) {
						validCnts.push_back(matrix[i][j]);
					}
				}
				else matrix[i][j] = matrix[i][j-1];
				if (dict.find(matrix[i][j]) == dict.end()) {
					dict[matrix[i][j]] = 1;
				}
				else dict[matrix[i][j]] += 1;
			}
		}

		for (int i = 0; i < validCnts.size(); i++) {
			result += dict[validCnts[i]];
		}

		return result;
	}
};
