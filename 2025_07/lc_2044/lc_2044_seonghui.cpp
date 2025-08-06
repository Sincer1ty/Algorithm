#include <vector>

using namespace std;

int countMaxOrSubsets(vector<int>& nums) {
    int n = nums.size();
    int max_or = 0, count = 0;

	// mask 가 선택되는 조합의 경우
    for (int mask = 1; mask < (1 << n); ++mask) {
        int cur_or = 0;
        for (int i = 0; i < n; ++i) {
            if (mask & (1 << i)) {
                cur_or |= nums[i];
            }
        }
        if (cur_or > max_or) {
            max_or = cur_or;
            count = 1;
        } else if (cur_or == max_or) {
            ++count;
        }
    }
    return count;
}