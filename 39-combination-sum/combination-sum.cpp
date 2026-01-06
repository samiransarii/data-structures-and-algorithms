class Solution {

    void findCombinations(vector<int>& candidates, int target, int sum, int index, vector<int>& curr, vector<vector<int>>& output) {
        if (sum == target) {
            output.push_back(curr);
            return;
        }

        if (index >= candidates.size() || sum > target) {
            return;
        }

        for (int i = index; i < candidates.size(); i++) {
            curr.push_back(candidates[i]);
            sum += candidates[i];
            findCombinations(candidates, target, sum, i, curr, output);
            curr.pop_back();
            sum -= candidates[i];
        }
    }

public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> output;
        vector<int> curr;

        findCombinations(candidates, target, 0, 0, curr, output);
        return output;

    }
};