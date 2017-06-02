class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> solution;
    vector<vector<int>> result;
    int sum = 0;
    sort(candidates.begin(),candidates.end());
    getCombineSum(sum,0,target,solution,candidates,result);
    return result;

    }
     void getCombineSum(
                   int &sum,
                   int level,
                   int target,
                   vector<int> &solution,
                   vector<int> &candidates,
                   vector<vector<int>> &result
                   ){
    if(sum > target) return;
    if(sum == target){
        result.push_back(solution);
        return;
    }
    for(int i = level; i<candidates.size(); i++){
        sum += candidates[i];
        solution.push_back(candidates[i]);
        getCombineSum(sum,i,target,solution,candidates,result);
        solution.pop_back();
        sum -= candidates[i];
    }

}
};
