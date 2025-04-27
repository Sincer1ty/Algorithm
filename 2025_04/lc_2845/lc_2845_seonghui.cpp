#include <vector>

using namespace std;

class Solution {
private:
	int countFromIndex(int start, vector<bool> v, int cnt){
		int temp = cnt, result = 0;

		for (int i = start; i < v.size(); i++) {
			if (temp < 0) {
				break;
			}
			if (v[i]) {
				temp -= 1;
			}
			if (temp == 0) result += 1;
		}

		return result;
	}
public:
	long long countInterestingSubarrays(vector<int>& nums, int modulo, int k) {
		int cnt = 0, result = 0;
		vector<int> validCnts;
		vector<bool> numsFlag;

		// 1. cnt 범위 찾기
		if (k == 0) validCnts.push_back(0);

		for (int i = 0; i < nums.size(); i++) {
			if (nums[i] % modulo == k) {
				numsFlag.push_back(true);
				cnt += 1;
				// 2. 가능성있는 cnt 찾기
				if (cnt % modulo == k) validCnts.push_back(cnt);
			}
			else numsFlag.push_back(false);
		}

		// 3. 해당 cnt에 부합하는 범위 개수 구하기
		// 인덱스로 참인 것들 기준으로 경우의 수를 찾기
		for (int i = 0; i < validCnts.size(); i++) {
			cnt = validCnts[i];
			for (int j = 0; j < numsFlag.size(); j++) {
				result += countFromIndex(j, numsFlag, validCnts[i]);
			}
		}

		return result;
	}
};
