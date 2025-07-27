// Runtime: 0ms
// Memory: 62.92 MB
class Solution {
public:
    int maxArea(vector<int>& heights) {
        int* left = heights.data();
        int* right = heights.data() + heights.size() - 1;
        int height = min(*right, *left);
        int width = right-left;
        int maxArea = width * height;

        while(left < right){
            if (*left >= *right) {
                right--;
            } else {
                left ++;
            }
            width = right - left;
            height = min(*left, *right);
            int currentArea = width * height;
            if (maxArea < currentArea){
                maxArea = currentArea;
            }
        }
        return maxArea;
    }
};
