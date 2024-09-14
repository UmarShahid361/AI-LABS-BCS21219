# Implement alpha beta pruning in python. .(pseudocode is given in
# chapter slides as well as in this manual below)

# Code:


def minimax(node, depth, isMaximizingPlayer, alpha, beta):
    if depth == 0 or len(node[1]) == 0:
        return node[0]
    if isMaximizingPlayer:
        bestVal = float("-inf")
        for child in node[1]:
            value = minimax(child, depth - 1, False, alpha, beta)
            bestVal = max(bestVal, value)
            alpha = max(alpha, bestVal)
            if beta <= alpha:
                break
        return bestVal
    else:
        bestVal = float("inf")
        for child in node[1]:
            value = minimax(child, depth - 1, True, alpha, beta)
            bestVal = min(bestVal, value)
            beta = min(beta, bestVal)
            if beta <= alpha:
                break
        return bestVal


tree = [
    3,
    [
        [
            5,
            [[9, [[8, [], []], [6, [], []]]], [6, [], []]],
            [2, [[3, [[1, [], []]], [7, [], []]]]],
        ]
    ],
]

print(minimax(tree, 3, True, float("-inf"), float("inf")))  # 5
