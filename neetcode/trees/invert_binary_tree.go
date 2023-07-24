package trees

type TreeNode struct {
	Left  *TreeNode
	Right *TreeNode
	Val   int
}

func invertTree(root *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}
	root.Left, root.Right = root.Right, root.Left
	invertTree(root.Left)
	invertTree(root.Right)
	return root
}
