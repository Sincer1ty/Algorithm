#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
    public:
    int maxRemoval(vector<int>& nums, vector<vector<int>>& queries) {
        priority_queue<int> available;
        priority_queue<int, vector<int>, greater<int>> used;
        int count = 0, query_idx = 0;
        
        sort(queries.begin(), queries.end());
        
        for (int i = 0; i < nums.size(); i++) {
            // 가능하지 않아지면 pop
            while (!used.empty() && used.top() < i) {
                used.pop();
            }
            
            // 새로 포함되는 쿼리 push
            while (query_idx < queries.size() && queries[query_idx][0] == i) {
                available.push(queries[query_idx][1]);
                query_idx++;
            }

            while (nums[i] > used.size()) {
                if (available.empty() || available.top() < i) return -1;
                
                used.push(available.top());
                available.pop();
                count++;
            }
        }

        return queries.size() - count;
    }
};
