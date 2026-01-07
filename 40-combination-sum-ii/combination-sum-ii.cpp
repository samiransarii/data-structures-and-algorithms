class Solution {
    vector<vector<int>> output;
    vector<int> curr;

    void findCombinations(vector<int>& candidates, int target, int currSum, int idx) {
        std::unordered_set<int> used;

        if (currSum == target) {
            output.push_back(curr);
            return;
        }

        if (currSum > target || idx >= candidates.size()) {
            return;
        }

        for (int i = idx; i < candidates.size(); i++) {
            if (used.find(candidates[i]) == used.end()) {
                used.insert(candidates[i]);

                curr.push_back(candidates[i]);
                currSum += candidates[i];
                findCombinations(candidates, target, currSum, i+1);

                curr.pop_back();
                currSum -= candidates[i];
            }
        }
    }
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        findCombinations(candidates, target, 0, 0);
        
        return output;
    }
};