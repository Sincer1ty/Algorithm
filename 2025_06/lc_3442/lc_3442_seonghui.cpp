#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int maxDifference(string s) {
        unordered_map<char, int> dict;

        for (char c : s) {
            dict[c] += 1;
        }
        
        // 제일 큰 홀수
        // 제일 작은 짝수
        int max = 1, min = 100;
        for (auto d : dict) {
            int value = d.second;

            if (value % 2 == 0 && min > value) min = value;
            else if (value % 2 != 0 && max < value) max = value;
        }

        return max - min;
    }
};
