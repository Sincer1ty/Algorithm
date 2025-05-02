#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    void pushLeft(string dominoes, int idx, vector<int>& secs) {
        int time = 0;

        while (idx != 0 && dominoes[--idx] == '.') {
            time -= 1;

            if (abs(time) == abs(secs[idx])) {
                secs[idx] = 0;
                break;
            }
            // 절댓값이 작아야지만 이김
            else if (!secs[idx] || abs(time) < abs(secs[idx])) secs[idx] = time;
        }
    }

    void pushRight(string dominoes, int idx, vector<int>& secs) {
        int time = 0;

        while (idx != dominoes.size() - 1 && dominoes[++idx] == '.') {
            time += 1;

            if (abs(time) == abs(secs[idx])) {
                secs[idx] = 0;
                break;
            }
            else if (!secs[idx] || abs(time) < abs(secs[idx])) secs[idx] = time;
        }
    }

    string pushDominoes(string dominoes) {
        vector<int> secs(dominoes.size(), 0);
        string result;
        
        for (int i = 0; i < dominoes.size(); i++) {
            if (i != 0 && dominoes[i] == 'L') {
                pushLeft(dominoes, i, secs);
            }
            else if (dominoes[i] == 'R') {
                pushRight(dominoes, i, secs);
            }
        }

        for (int i = 0; i < secs.size(); i++) {
            if (secs[i] > 0) dominoes[i] = 'R';
            else if (secs[i] < 0) dominoes[i] = 'L';
        }

        return dominoes;
    }
};
