class Solution {
    vector<vector<int>> output;
    vector<int> curr;

    void findCombinations(int start, int n, int k) {
        if (k == 0) {
            output.push_back(curr);
            return;
        }

        if (start > n) {
            return;
        }

        for (int i = start; i <= n; i++) {
            curr.push_back(i);
            findCombinations(i+1, n, k-1);
            curr.pop_back();
        }
    }

public:
    vector<vector<int>> combine(int n, int k) {
        findCombinations(1, n, k);
        return output;
    }
};