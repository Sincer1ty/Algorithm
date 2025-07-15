#include <string>
#include <unordered_set>

using namespace std;

class Solution {
public:
    bool isValid(string word) {        
        // 최소 3 글자
        if (word.size() < 3) return false;

        bool isVowel = false, isConsonant = false;
        unordered_set<char> vowel = {'a','e','i','o','u','A','E','I','O','U'};
        for (char w : word) {
           if ('0' <= w && w <= '9') continue;
           else if (('a' <= w && w <= 'z') || 
                    ('A' <= w && w <= 'Z')) {
            if (vowel.count(w)) isVowel = true;
            else isConsonant = true;
           }
           else return false;
        }

        if (!(isVowel && isConsonant)) return false;

        return true; 
    }  
};