#include <vector>
#include <numeric>

using namespace std;

class Solution {
public:
    int maxFreeTime(int eventTime, vector<int>& startTime, vector<int>& endTime) {
        int n = startTime.size();
        vector<int> gaps(n + 1);
        gaps[0] = startTime[0];
        for (int i = 1; i < n; ++i) {
            gaps[i] = startTime[i] - endTime[i - 1];
        }
        gaps[n] = eventTime - endTime[n - 1];

        vector<int> prefixMax(n + 1), suffixMax(n + 1);
        prefixMax[0] = gaps[0];
        for (int i = 1; i <= n; ++i)
            prefixMax[i] = max(prefixMax[i - 1], gaps[i]);

        suffixMax[n] = gaps[n];
        for (int i = n - 1; i >= 0; --i)
            suffixMax[i] = max(suffixMax[i + 1], gaps[i]);

        // sliding window
        int ans = 0;
        int windowSum = gaps[0] + gaps[1];
        int dur = endTime[0] - startTime[0];

        int maxExcept = suffixMax[2];
        ans = windowSum + (maxExcept >= dur ? dur : 0);

        for (int i = 2; i <= n; ++i) {
            windowSum += gaps[i] - gaps[i - 2];
            dur = endTime[i - 1] - startTime[i - 1];

            maxExcept = (i == n) ? prefixMax[n - 2] :
                             max(prefixMax[i - 2], suffixMax[i + 1]);

            int adjusted = windowSum + (maxExcept >= dur ? dur : 0);
            ans = max(ans, adjusted);
        }

        return ans;
    }
};
