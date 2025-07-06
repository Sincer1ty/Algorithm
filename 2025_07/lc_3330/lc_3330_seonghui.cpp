#include <string>

using namespace std;

class Solution {
public:
    int possibleStringCount(string word) {
		int result = 1; // 자기 자신
		for (int i = 1; i < word.size(); ++i) {
			if (word[i - 1] == word[i]) ++result;;
		}
		return result;
    }
};