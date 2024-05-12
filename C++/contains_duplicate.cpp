// Uses sort() and adacent_find() built in methods
// Runtime: 84ms
// Memory: 60.98 MB
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        auto i1 = std::adjacent_find(nums.begin(), nums.end());
    
        if (i1 == nums.end()) {
            return false;
        }
        return true;
    }
};
