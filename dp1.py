# #A DP is an algorithmic technique which is usually based on a recurrent formula and one (or some) starting states. A sub-solution of the problem is constructed from previously found ones. DP solutions have a polynomial complexity which assures a much faster running time than other techniques like backtracking, brute-force etc.
# 
# Now let's see the base of DP with the help of an example:
# 
# Given a list of N coins, their values (V1, V2, , VN), and the total sum S. Find the minimum number of coins the sum of which is S (we can use as many coins of one type as we want), or report that it's not possible to select coins in such a way that they sum up to S.
# 
# Now let's start constructing a DP solution:
# 
# First of all we need to find a state for which an optimal solution is found and with the help of which we can find the optimal solution for the next state.
# 
# What does a "state" stand for?
# 
# It's a way to describe a situation, a sub-solution for the problem. For example a state would be the solution for sum i, where i<=S. A smaller state than state i would be the solution for any sum j, where j<i. For finding a state i, we need to first find all smaller states j (j<i) . Having found the minimum number of coins which sum up to i, we can easily find the next state - the solution for i+1.
# 
# How can we find it?
# 
# It is simple - for each coin j, Vj<=i, look at the minimum number of coins found for the i-Vjsum (we have already found it previously). Let this number be m. If m+1 is less than the minimum number of coins already found for current sum i, then we write the new result for it.
# 
# For a better understanding let's take this example:
# Given coins with values 1, 3, and 5.
# And the sum S is set to be 11.
# 
# First of all we mark that for state 0 (sum 0) we have found a solution with a minimum number of 0 coins. We then go to sum 1. First, we mark that we haven't yet found a solution for this one (a value of Infinity would be fine). Then we see that only coin 1 is less than or equal to the current sum. Analyzing it, we see that for sum 1-V1= 0 we have a solution with 0 coins. Because we add one coin to this solution, we'll have a solution with 1 coin for sum 1. It's the only solution yet found for this sum. We write (save) it. Then we proceed to the next state - sum 2. We again see that the only coin which is less or equal to this sum is the first coin, having a value of 1. The optimal solution found for sum (2-1) = 1 is coin 1. This coin 1 plus the first coin will sum up to 2, and thus make a sum of 2 with the help of only 2 coins. This is the best and only solution for sum 2. Now we proceed to sum 3. We now have 2 coins which are to be analyzed - first and second one, having values of 1 and 3. Let's see the first one. There exists a solution for sum 2 (3 - 1) and therefore we can construct from it a solution for sum 3 by adding the first coin to it. Because the best solution for sum 2 that we found has 2 coins, the new solution for sum 3 will have 3 coins. Now let's take the second coin with value equal to 3. The sum for which this coin needs to be added to make 3 , is 0. We know that sum 0 is made up of 0 coins. Thus we can make a sum of 3 with only one coin - 3. We see that it's better than the previous found solution for sum 3 , which was composed of 3 coins. We update it and mark it as having only 1 coin. The same we do for sum 4, and get a solution of 2 coins - 1+3. And so on.
import sys

sumS = 11
coins = [1,3,5]

minNumCoins = [0]
coinVal = [0]
lastSum = [0]

for s in range(1,sumS+1):
    minNumCoins.append(sys.maxint)
    coinVal.append(0)
    lastSum.append(0)
    for vj in coins:
        #print s, vj        
        if (vj <= s and minNumCoins[s-vj]+1 < minNumCoins[s]): 
            minNumCoins[s] = minNumCoins[s-vj]+1
            coinVal[s] = vj
            lastSum[s] = s-vj
    
            
for i in range(sumS+1):
    print i, minNumCoins[i], coinVal[i], lastSum[i]
