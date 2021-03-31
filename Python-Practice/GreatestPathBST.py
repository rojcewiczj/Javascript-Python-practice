def maxPathSum(tree):
    _, maxSum = findMaxSum(tree)
	print(_)
	print(maxSum)
    return maxSum

def findMaxSum(tree):
	if tree is None:
		return(0, float("-inf"))
	
	leftMaxSumAsBranch, leftMaxPathSum = findMaxSum(tree.left)
	print("leftMaxSumAsBranch, leftMaxPathSum: ",leftMaxSumAsBranch, leftMaxPathSum)
	rightMaxSumAsBranch, rightMaxPathSum = findMaxSum(tree.right)
    print("rightMaxSumAsBranch, rightMaxPathSum: ", rightMaxSumAsBranch, rightMaxPathSum)
	maxChildSumAsBranch = max(leftMaxSumAsBranch, rightMaxSumAsBranch)
	print("MaxChildSumAsBranch: ", maxChildSumAsBranch)
	value = tree.value
    print("value: ", value)
	maxSumAsBranch = max(maxChildSumAsBranch + value, value)
	print("maxSumAsBranch: ", maxSumAsBranch)
	maxSumAsRootNode = max(leftMaxSumAsBranch + value + rightMaxSumAsBranch, maxSumAsBranch)
	print("maxSumAsRootNode: ", maxSumAsRootNode)
	maxPathSum = max(leftMaxPathSum, rightMaxPathSum, maxSumAsRootNode)
	print("maxPathSum: ", maxPathSum)
	
	return(maxSumAsBranch, maxPathSum)
	