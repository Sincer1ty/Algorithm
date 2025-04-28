#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
	long long countSubarrays(vector<int>& nums, long long k) {
		long long count = 0;
		int idx = 0, adjustValue = 0;
		vector<long long> sumVector;

		for (int i = 0; i < nums.size(); i++) {
			// 합이 k 를 넘어가는 건 볼 필요 없음
			if (nums[i] < k) count += 1;
			else {
				// 무조건 커지니까 다음으로 for 문 이동
				sumVector.clear();
				idx = i;
				adjustValue = 0;
				continue;
			}

			for (int j = 0; j < sumVector.size(); j++){
				sumVector[j] += nums[i];
				
				// 길이 : i + 1
				int length = i + 1 - j - adjustValue;
				if (idx != 0) length -= idx + 1;
				long long score = sumVector[j] * length;
				if (score < k) count += 1;
			}

			sumVector.push_back(nums[i]);
			// 0 인덱스가 가장 클 것
			if (sumVector[0] >= k) {
				sumVector.erase(sumVector.begin());
				adjustValue += 1;
			}
		}

		return count;
	}
};
