class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) return 0;
       unordered_set<int> numSet;

       for(int x : nums) numSet.insert(x);

       int best = 0;

       for (int x : numSet){
        if(!numSet.contains(x-1)){
            int curr = x;
            int len = 1;

            while(numSet.contains(curr+1)){
                curr++;
                len++;
            }
            best = max(best, len);
        }
       }

       return best;
    }
};
