#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<string> divideString(string s, int k, char fill) {
		int idx = 0;
		vector<string> result;
		while(idx < s.size()) {
			string sample = s.substr(idx, k);
			// 마지막 : k개의 문자가 남아 있지 않으면 fill 문자로 채우기
			if (sample.size() != k) {
				sample += string(k - sample.size(), fill);
			}
			result.push_back(sample);
			idx += k;
		}

		return result;
    }
};