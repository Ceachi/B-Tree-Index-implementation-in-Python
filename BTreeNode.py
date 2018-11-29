from BTreeKeyValue import BTreeKeyValue

class BTreeNode(object):
    MIN_DEGREE = 5
    LOWER_BOUND_KEY_NUM = MIN_DEGREE - 1
    UPPER_BOUND_KEY_NUM = (MIN_DEGREE * 2) - 1

    def __init__(self):
        self.mIsLeaf = True
        self.mCurrentKeyNum = 0
        self.mKeys = [None] * self.UPPER_BOUND_KEY_NUM
        self.mChildren = [None] * (self.UPPER_BOUND_KEY_NUM + 1)

    @staticmethod
    def getChildNodeAtIndex(btNode, keyIdx, nDirection):
        if(btNode.mIsLeaf):
            return None

        keyIdx += nDirection
        if (keyIdx < 0 or keyIdx > btNode.mCurrentKeyNum):
            return None

        return btNode.mChildren[keyIdx]

    @staticmethod
    def getLeftChildAtIndex(btNode, keyIdx):
        return BTreeNode.getChildNodeAtIndex(btNode, keyIdx, 0)

    @staticmethod
    def getRightChildAtIndex(btNode, keyIdx):
        return BTreeNode.getChildNodeAtIndex(btNode, keyIdx, 1)

    @staticmethod
    def getLeftSiblingAtIndex(parentNode, keyIdx):
        return BTreeNode.getChildNodeAtIndex(parentNode, keyIdx, -1)

    @staticmethod
    def getRightSiblingAtIndex(parentNode, keyIdx):
        return BTreeNode.getChildNodeAtIndex(parentNode, keyIdx, 1)

    def showBTreeNode(self):
        print(self.mIsLeaf, self.mCurrentKeyNum, self.mKeys, self.mChildren)