#include <vector>

using namespace std;

class Solution {
public:
    int countHillValley(vector<int>& nums) {
        int prev = nums[0], count = 0;
        for (int i = 1; i < nums.size() - 1 ; ++i) {
            int cur = nums[i];
            int next = nums[i + 1];
            if (next < cur) {
                // hill
                if (prev < cur) ++count;
            }
            else if (next > cur) {
                // valley
                if (prev > cur) ++count;
            }
            // 같으면 넘기기
            else {
                continue;
            }
            prev = cur;
        }

        return count;
    }
};
