from BTreeNode import *
from BTreeKeyValue import *

class Btree:
    mRoot = None
    mSize = 0
    mIntermediateInternalNode = None
    mNodeIdx = 0

    def getRootNode(self):
        return self.mRoot

    def size(self):
        return self.mSize

    def clear(self):
        self.mSize = 0
        self.mRoot = None


    def createNode(self):
        btNode = BTreeNode()
        btNode.mIsLeaf = True
        btNode.mCurrentKeyNum = 0
        return btNode

    def insert(self, key, value):
        if(self.mRoot == None):
            self.mRoot = self.createNode()

        self.mSize+=1
        if(self.mRoot.mCurrentKeyNum == BTreeNode.UPPER_BOUND_KEY_NUM):
            btNode = self.createNode()
            btNode.mIsLeaf = False
            btNode.mChildren[0] = self.mRoot
            self.mRoot = btNode
            self.splitNode(self.mRoot, 0, btNode.mChildren[0])

        self.insertKeyAtNode(self.mRoot, key, value)

    def search(self, key):
        global currentNode, currentKey
        global i, numberOfKeys
        currentNode = self.mRoot #currentProcessedNode = rootNode
        currentKey = None
        while(currentNode != None): # while currentProcessedNode is not null
            numberOfKeys = currentNode.mCurrentKeyNum
            i = 0
            currentKey = currentNode.mKeys[i]
            while(i<numberOfKeys and key>currentKey.mKey): # while(currentIndex < key number of currentProcessedNode
                                                           # and searchedKey > currentProcessedNode.Keys[currentIndex]
                i+=1 # we increment the currentIndex
                if(i<numberOfKeys):
                    currentKey = currentNode.mKeys[i]
                else:
                    i-=1
                    break

            if(i<numberOfKeys and key == currentKey.mKey): # if currentIndex < key number of currentProcessedNode AND
                                                           # searchedKey ==  currentProcessedNode.Keys[currentIndex]
                return currentKey.mValue # we return searchedKey is found

            # currentProcessedNode  = Left/Right Child of the currentProcessedNode
            if(key>currentKey.mKey):
                currentNode = BTreeNode.getRightChildAtIndex(currentNode, i)
            else:
                currentNode = BTreeNode.getLeftChildAtIndex(currentNode, i)


    def insertKeyAtNode(self, rootNode, key, value):
        global i
        currentKeyNum = rootNode.mCurrentKeyNum
        if(rootNode.mIsLeaf):
            # Empty root
            if(rootNode.mCurrentKeyNum == 0):
                rootNode.mKeys[0] = BTreeKeyValue(key, value)
                rootNode.mCurrentKeyNum += 1
                return
            for i in range(rootNode.mCurrentKeyNum):
                # Find existing key, overwrite its value only
                if(key == rootNode.mKeys[i].mKey):
                    rootNode.mKeys[i].mValue = value
                    self.mSize -= 1
                    return

            i=currentKeyNum-1
            existingKeyVal = rootNode.mKeys[i]
            while(i>-1 and key<existingKeyVal.mKey):
                rootNode.mKeys[i+1] = existingKeyVal
                i-=1
                if(i>-1):
                    existingKeyVal = rootNode.mKeys[i]

            i+=1
            rootNode.mKeys[i] = BTreeKeyValue(key, value)
            rootNode.mCurrentKeyNum += 1
            return

        # This is an internal node, not a leaf node
        # So lets find the child node where the key is supposed to be long
        i=0
        numberOfKeys = rootNode.mCurrentKeyNum
        currentKey = rootNode.mKeys[i]
        while(i<numberOfKeys and key>currentKey.mKey):
            i+=1
            if(i<numberOfKeys):
                currentKey = rootNode.mKeys[i]
            else:
                i-=1
                break

        if(i<numberOfKeys and key==currentKey.mKey):
            # The key already existed so replace it's value and done with it
            currentKey.mValue = value
            self.mSize-=1
            return

        btNode = None
        if(key>currentKey.mKey):
            btNode = BTreeNode.getRightChildAtIndex(rootNode, i)
            i+=1
        else:
            if(i-1>=0 and key>rootNode.mKeys[i-1].mKey):
                btNode = BTreeNode.getRightChildAtIndex(rootNode, i-1)
            else:
                btNode = BTreeNode.getLeftChildAtIndex(rootNode, i)

        if(btNode.mCurrentKeyNum == BTreeNode.UPPER_BOUND_KEY_NUM):
            # If the child node is full node then handle it by splitting out
            # then insert key starting at the root node after splitting node
            self.splitNode(rootNode, i, btNode)
            self.insertKeyAtNode(rootNode, key, value)
            return

        self.insertKeyAtNode(btNode, key, value)

    def splitNode(self, parentNode, nodeIdx, btNode):
        global i
        newNode = self.createNode()
        newNode.mIsLeaf = btNode.mIsLeaf

        # Since the node is full, new node must share LOWER_BOUND_KEYNUM (t-1) keys from the node
        newNode.mCurrentKeyNum = BTreeNode.LOWER_BOUND_KEY_NUM
        # Copy right half of the keys from the node to the new node
        i=0
        for i in range(BTreeNode.LOWER_BOUND_KEY_NUM):
            newNode.mKeys[i] = btNode.mKeys[i + BTreeNode.MIN_DEGREE]
            btNode.mKeys[i + BTreeNode.MIN_DEGREE] = None

        # If the node is an internal node (not a leaf)
        # copy it's child pointers at the half right as well
        if(not btNode.mIsLeaf):
            i=0
            for i in range(BTreeNode.MIN_DEGREE):
                newNode.mChildren[i] = btNode.mChildren[i + BTreeNode.MIN_DEGREE]
                btNode.mChildren[i+BTreeNode.MIN_DEGREE] = None

        # The node at this point should have LOWER_BOUND_KEYNUM ...
        btNode.mCurrentKeyNum = BTreeNode.LOWER_BOUND_KEY_NUM

        for i in range(parentNode.mCurrentKeyNum, nodeIdx, -1):
            parentNode.mChildren[i+1] = parentNode.mChildren[i]
            parentNode.mChildren[i] = None

        parentNode.mChildren[nodeIdx + 1] = newNode
        for i in range(parentNode.mCurrentKeyNum-1, nodeIdx+1, -1):
            parentNode.mKeys[i+1] = parentNode.mKeys[i]
            parentNode.mKeys[i] = None

        parentNode.mKeys[nodeIdx] = btNode.mKeys[BTreeNode.LOWER_BOUND_KEY_NUM]
        btNode.mKeys[BTreeNode.LOWER_BOUND_KEY_NUM] = None
        parentNode.mCurrentKeyNum+=1




