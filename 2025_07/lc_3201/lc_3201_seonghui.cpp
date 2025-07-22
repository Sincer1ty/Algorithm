#include <vector>

using namespace std;

// 홀 + 홀 = 짝
// 짝 + 짝 = 짝
// 홀 + 짝 = 짝
class Solution {
public:
    int maximumLength(vector<int>& nums) {
        // (sub[0] + sub[1]) % 2 == 
		// (sub[1] + sub[2]) % 2 == ... 
		// == (sub[x - 2] + sub[x - 1]) % 2.
		// 합이 다 홀수 이거나 다 짝수면 되는 거 아닌가?

		// 처음에 하나를 기준으로 쭉 진행하다가
		// 끊기면 끊기는 것을 기존으로 따로 세놓고
		// 어차피 다른 경우일 거니까?
		// 비교?

		// 6 14 13 6
		int odd = 0, even = 0;
		for (int i = 1; i < nums.size(); ++i) {
			// 홀수
			if ((nums[i - 1] + nums[i]) % 2) {
				++odd;
			}
			else ++even;
		}

		// 요소 수는 간격 수 + 1 이니까?
		return max(odd, even) + 1;
    }
};