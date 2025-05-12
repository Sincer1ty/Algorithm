#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
	vector<int> findEvenNumbers(vector<int>& digits) {
		vector<int> integers;
		
		// 중복 허용
		// unique 정수 찾기
		
		for (int i = 0; i < digits.size(); i++) {
			// 끝에가 짝수여야 함
			if (digits[i] % 2 == 0) {
				int integer = digits[i];
				for (int k = 0; k < digits.size(); k++) {
					// 현재 인덱스를 제외한 애들 사이에서
					if (k == i) continue;
					integer += digits[k] * 10;

					for (int l = 0; l < digits.size(); l++) {
						if (l == i) continue;
						else if (l == k) continue;
						// 단 0이 처음에 올 수 없음
						if (digits[l] == 0) continue;
						if (find(integers.begin(), integers.end(), integer + digits[l] * 100) == integers.end()){
							integers.push_back(integer + digits[l] * 100);
						}
					}
					integer -= digits[k] * 10;
				}
			}
		}

		// 정렬
		sort(integers.begin(), integers.end());

		return integers;
	}
};
