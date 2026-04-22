class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, root, key, val):
        if not root:
            return TreeNode(key, val)
        if key < root.key:
            root.left = self.insert(root.left, key, val)
        elif key > root.key:
            root.right = self.insert(root.right, key, val)
        else:
            root.val = val
        return root
    
    def search(self, root, key):
        # should return val for the key else -1
        if not root:
            return -1
        if key == root.key:
            return root.val
        if key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)
    
    def delete(self, root, key):
        if not root:
            return None
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            temp = self.minValueNode(root.right)
            root.key = temp.key
            root.val = temp.val
            root.right = self.delete(root.right, temp.key)
        return root
    
    def minValueNode(self, root):
        while root.left:
            root = root.left
        return root
    
    def put(self, key, val):
        self.root = self.insert(self.root, key, val)
    
    def remove(self, key):
        self.root = self.delete(self.root, key)
    
    def get(self, key):
        return self.search(self.root, key)
    
    

class MyHashMap:

    def __init__(self):
        self.size = 10000
        self.buckets = [BST() for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        idx = self._hash(key)
        self.buckets[idx].put(key, value)

    def get(self, key: int) -> int:
        idx = self._hash(key)
        return self.buckets[idx].get(key)
        
    def remove(self, key: int) -> None:
        idx = self._hash(key)
        self.buckets[idx].remove(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)