// 1. Two Sum
// Problem: https://leetcode.com/problems/two-sum/

// Runtime: 10 ms
// Memory Usage: 13.69 MB
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> mymap;
        mymap[nums[0]] = 0;
        for(int i=1;i<nums.size();i++){
            if (mymap.find(target-nums[i]) != mymap.end()) {
                return {mymap[target-nums[i]], i};
            } else {
                mymap[nums[i]] = i;   
            }
        }
        return {};
    }
};
