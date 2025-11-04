def count_unbalanced(bt):
  if (bt.right == None and bt.left == None) or (bt.right and bt.left) :
    return 0
  if bt.right and bt.left == None:
    return 1 + count_unbalanced(bt.right)
  if bt.left and bt.right == None:
    return 1 + count_unbalanced(bt.left)
print("image run successfully.")

