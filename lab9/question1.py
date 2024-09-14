# Implement Minimax Algo in python.(pseudocode is given in 
# chapter slides as well as in this manual below)

# Code:

def minimax(node, depth, maximizingPlayer):
    if depth == 0 or len(node[1]) == 0:
        return node[0]
    if maximizingPlayer:
        maxEva = float('-inf')
        for child in node[1]:
            eva = minimax(child, depth - 1, False)
            maxEva = max(maxEva, eva)   
        return maxEva
    else:
        minEva = float('inf')
        for child in node[1]:
            eva = minimax(child, depth - 1, True)
            minEva = min(minEva, eva)
        return minEva
    
tree = [3, [[5, [[9, [[8, [], []], [6, [], []]]], [6, [], []]], [2, [[3, [[1, [], []]], [7, [], []]]]]]]]

print(minimax(tree, 3, True)) # 6