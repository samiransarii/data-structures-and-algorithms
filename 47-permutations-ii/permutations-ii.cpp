class Solution {
    void findPermutations(vector<int>& nums, vector<vector<int>>& output, vector<int>& curr, vector<bool>& used) {
        if (curr.size() == nums.size()) {
            output.push_back(curr);
            return;
        }

        for (int i = 0; i < nums.size(); i++) {
            if (i > 0 && nums[i] == nums[i-1] && used[i-1]) {
                continue;
            }

            if (used[i] == false) {
                curr.push_back(nums[i]);
                used[i] = true;

                findPermutations(nums, output, curr, used);

                curr.pop_back();
                used[i] = false;
            }
        }
    }

public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        vector<vector<int>> output;
        vector<int> curr;
        vector<bool> used(nums.size(), false);

        findPermutations(nums, output, curr, used);
        
        return output;
    }
};