#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxTaskAssign(vector<int>& tasks, vector<int>& workers, int pills, int strength) {
        int count = 0, assigned = 0;

        sort(workers.begin(), workers.end());
        sort(tasks.begin(), tasks.end());
        
        for (int i = 0; i < workers.size(); i++) {
            assigned = 0;
            while (assigned < tasks.size() && workers[i] >= tasks[assigned]) {
                assigned += 1;
            }
            
            if (assigned == 0 || workers[i] < tasks[assigned - 1]) {
                workers[i] += strength;
            }
            else {
                count += 1;
                // 불가능한 수로 만들기
                workers[i] = -1 -strength;
                tasks[assigned - 1] = 2000000001;
            }
        }
        assigned = -1;
        for (int i = 0; i < workers.size(); i++) {
            for (int j = assigned + 1; j < tasks.size(); j++) {
                // 있으면 할당 가능
                if (workers[i] >= tasks[j]) {
                    if (pills == 0) return count;
                    count += 1;
                    assigned = j;
                    pills -= 1;       
                    break;
                }
            }
        }

        return count;
    }
};
