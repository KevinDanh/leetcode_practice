// Solution 1
// Runtime; 89 ms
// Memory Usage: 41.52 MB
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> result;
        map<map<char, int>, vector<string>> anagramList;
        map<char, int> tempMap;
        for(int i=0; i<strs.size(); i++){
            for(char letter: strs[i]){
                tempMap[letter] += 1;    
            }
            if (anagramList.find(tempMap) == anagramList.end()){
                anagramList[tempMap] = {strs[i]};
            } else {
                anagramList[tempMap].push_back(strs[i]);
            }
            tempMap = {};
        }

        for (const auto& [innerMap, vec] : anagramList) {
            result.push_back(vec);
        }

        // debug
//        for (const auto& [innerMap, vec] : anagramList) {
//            for (const auto& [key, value] : innerMap) {
//               std::cout << "Map: " << key << ": " << value << std::endl;
//            }
//            for (const auto& str : vec) {
//                std::cout << "Vector Element: " << str << std::endl;
//            }
//           cout << "-----" << endl; 
//        }

        return result;
    }
};


// Solution 2
// Runtime; 29 ms
// Memory Usage: 23.79 MB
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> result;
        unordered_map<string, vector<string>> anagramList;

        for(int i=0; i<strs.size(); i++){
            string temp = strs[i];
            sort(strs[i].begin(), strs[i].end());
            if (anagramList.find(strs[i]) == anagramList.end()){
                anagramList[strs[i]] = {temp};
            } else {
                anagramList[strs[i]].push_back(temp);
            }
        }

        for (const auto [k,v] : anagramList) {
            result.push_back(v);
        }

        return result;
    }
};