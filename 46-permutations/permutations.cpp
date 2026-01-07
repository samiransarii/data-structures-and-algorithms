class Solution {
    vector<vector<int>> output;
    vector<int> curr;
    std::unordered_set<int> visited;

    void findPermutations(vector<int>& nums) {
        if (curr.size() == nums.size()) {
            output.push_back(curr);
            return;
        }

        for (int i = 0; i < nums.size(); i++) {
            if (visited.find(nums[i]) == visited.end()) {
                curr.push_back(nums[i]);
                visited.insert(nums[i]);
                findPermutations(nums);

                curr.pop_back();
                visited.erase(nums[i]);
            }
        }
    }
    
public:
    vector<vector<int>> permute(vector<int>& nums) {
        findPermutations(nums);
        
        return output;
    }
};