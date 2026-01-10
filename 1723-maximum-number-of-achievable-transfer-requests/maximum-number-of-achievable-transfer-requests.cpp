class Solution {
public:
    int maxRequest;

    void findValidRequests(int idx, int count, vector<vector<int>>& requests, vector<int>& balance) {
        // Update the maxRequest if the building are balanced
        if (isBalanced(balance)) {
            maxRequest = max(maxRequest, count);
        }
        
        // All requests validated
        if (idx == requests.size()) {
            return;
        }
        
        for (int i = idx; i < requests.size(); i++) {
            int from = requests[i][0];
            int to = requests[i][1];

            balance[from] -= 1;
            balance[to] += 1;
            count += 1;

            findValidRequests(i+1, count, requests, balance);

            count -= 1;
            balance[from] += 1;
            balance[to] -= 1;
        }
    }

    bool isBalanced(vector<int>& balance) {
        for (int x: balance) if (x != 0) return false;
        return true;
    }

    int maximumRequests(int n, vector<vector<int>>& requests) {
        vector<int> balance(n, 0);
        maxRequest = 0;

        findValidRequests(0, 0, requests, balance);

        return maxRequest;
    }
};