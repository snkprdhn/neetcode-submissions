class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> umap;
        for (auto it:s){
            umap[it]++;
        }

        for (auto it:t){
            umap[it]--;
        }

        for (auto it:umap){
            if(it.second != 0) return false;
        }
        return true;
    }
    
};
