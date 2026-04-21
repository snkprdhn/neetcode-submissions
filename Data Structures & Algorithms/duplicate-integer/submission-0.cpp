class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int,int> umap;
        for(int i=0;i<nums.size();i++){
            if (umap[nums[i]]) return true;
            umap[nums[i]]++;
        }
        return false;
    }
};
