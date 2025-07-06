#include <string>

using namespace std;

class Solution {
public:
    char kthCharacter(int k) {
        string word = "a";
        
        while (word.size() < k) {
            string newWord = "";
            for (char w : word) {
                newWord += w+1;
            }
            
            word += newWord;
        }

        return word[k-1];
    }
};
