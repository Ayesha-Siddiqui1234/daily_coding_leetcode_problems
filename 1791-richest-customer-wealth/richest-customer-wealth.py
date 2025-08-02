class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        current_wealth=0
        for i in accounts:
            wealth = sum(i)
            current_wealth= max(current_wealth, wealth)
        return current_wealth    

        