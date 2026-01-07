class Solution {
    vector<vector<int>> output;
    vector<int> curr;

    void findCombinations(vector<int>& candidates, int target, int currSum, int idx) {
        if (currSum == target) {
            output.push_back(curr);
            return;
        }

        if (currSum > target || idx >= candidates.size()) {
            return;
        }

        // Take the candidate at current index
        curr.push_back(candidates[idx]);
        currSum += candidates[idx];

        findCombinations(candidates, target, currSum, idx);

        // Skip the candidate at current index
        curr.pop_back();
        currSum -= candidates[idx];

        findCombinations(candidates, target, currSum, idx+1);
    }
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {

        findCombinations(candidates, target, 0, 0);
        
        return output;
    }
};