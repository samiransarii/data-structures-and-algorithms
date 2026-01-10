class Solution {

    void findValidRequests(int idx, int count, int& output, vector<vector<int>>& requests, vector<int>& balance) {
        // Update the maxRequest if the building are balanced
        if (isBalanced(balance)) {
            output = max(output, count);
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

            findValidRequests(i+1, count, output, requests, balance);

            count -= 1;
            balance[from] += 1;
            balance[to] -= 1;
        }
    }

    bool isBalanced(vector<int>& balance) {
        for (int x: balance) if (x != 0) return false;
        return true;
    }

public:
    int maximumRequests(int n, vector<vector<int>>& requests) {
        vector<int> balance(n, 0);
        int maxRequest = 0;

        findValidRequests(0, 0, maxRequest, requests, balance);
        return maxRequest;
    }
};