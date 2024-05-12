// 242. Valid Anagrams
// Problem: https://leetcode.com/problems/valid-anagram/


// Solution using maps, creates 2 maps that keep track of character count in each string
// Runtime: 11 ms
// Memory Usage: 9.78 MB
class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char, int> mymap1;
        map<char, int> mymap2;

        for (int i=0; i<s.size();i++){
            mymap1[s[i]] += 1;
        }
        for (int i=0; i<t.size();i++){
            mymap2[t[i]] += 1;
        }
        return mymap1 == mymap2;
    }
};
