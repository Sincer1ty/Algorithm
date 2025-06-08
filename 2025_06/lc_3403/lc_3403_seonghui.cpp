#include <string>

using namespace std;

class Solution {
public:
    string answerString(string word, int numFriends) {
        if (numFriends == 1) return word;

        // 사전순으로 제일 큰 연속된 부분배열
        int idx_max = 0;
        for (int i = 1; i < word.size(); i++) {
            if (word[idx_max] < word[i]) {
                idx_max = i;
                continue;
            }
            
            if (word[idx_max] != word[i]) continue;

            int offset = 0;
            // 똑같은 것이 있을 경우 고려
            while (word[idx_max + offset] == word[i + offset]) {
                offset++;
            }

            if (word[idx_max + offset] < word[i + offset]) {
                idx_max = i;
            }
        }
        
        // 최대 길이는 내 길이 - (numFriends - 1)
        string result = word.substr(idx_max, word.size() - (numFriends - 1));        
        return result;
    }
};
