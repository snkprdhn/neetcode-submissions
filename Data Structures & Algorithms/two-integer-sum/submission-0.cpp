class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> umap;
        for(int i=0;i<nums.size();i++){
            cout<<"umap[target-nums[i]]= "<<umap[target-nums[i]]<<endl;
            if(umap[target-nums[i]]) return {umap[target-nums[i]]-1, i};
            if(!umap[nums[i]])umap[nums[i]] = i+1;
            cout<<"umap[nums[i]]= "<<umap[nums[i]]<<endl;
        }
        cout<<"not found";
        return {0,0};
    }
};
