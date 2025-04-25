#include <vector>

using namespace std;

class Solution {
private:
	vector<int> makeSet(vector<int> v){
		vector<int> result;

		for (int i = 0; i < v.size(); i++){
			if(find(result.begin(), result.end(), v[i]) == result.end()){
				result.push_back(v[i]);
			}
		}

		return result;
	}

	bool isExistSet(int idx, vector<int> v, vector<int> set){
		for (int i = 0; i < set.size(); i++){
			if (find(v.begin()+idx, v.end(), set[i]) == v.end()){
				return false;
			}
		}

		return true;
	}

	bool isExist(int start, int idx, vector<int> v){
		for (int i = start; i < idx; i++){
			if (v[i] == v[idx]) return true;
		}
		return false;
	}
public:
	int countCompleteSubarrays(vector<int>& nums) {
		int count = 0;
		vector<int> set;
		
		// 다양한 조합을 구한 후
		set = makeSet(nums);

		for (int i = 0; i < nums.size(); i++){
			// 조합이 다 들어 있는지 확인
			if (!isExistSet(i, nums, set)) return count;

			for (int j = nums.size() - 1; j >= i; j--){
				count += 1;
				// nums[j] 가 앞쪽 부분배열에 존재하면
				if (!isExist(i, j, nums)){
					break;
				}
			}
		}

		return count;
	}
};
