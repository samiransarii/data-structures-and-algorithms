class Solution {

    void findMinimumFairness(int idx, int k, int& unfairness, vector<int>& cookies, vector<int>& kids) {
        unordered_set<int> seen;
        
        if (idx >= cookies.size()) {
            int currMax = *max_element(kids.begin(), kids.end());
            unfairness = min(unfairness, currMax);
            return;
        }

        for (int i = 0; i < k; i++) {
            // Removes hopless redundant branches;
            if (seen.count(kids[i])) continue;
            seen.insert(kids[i]);

            kids[i] += cookies[idx];
            
            if (kids[i] < unfairness) {
                findMinimumFairness(idx+1, k, unfairness, cookies, kids);
            }
            
            kids[i] -= cookies[idx];
        }
    }

public:
    int distributeCookies(vector<int>& cookies, int k) {
        sort(cookies.begin(), cookies.end());
        int unfairness = INT_MAX;
        vector<int> kids(k, 0);

        findMinimumFairness(0, k, unfairness, cookies, kids);
        return unfairness;

    }
};