class KVNode(object):
    def __init__(self, key=None, val=None, size_of_subtree=1):
        self.key = key
        self.val = val
        self.size_of_subtree = size_of_subtree
        self.left = None
        self.right = None

class LNode(object):
    def __init__(self, key=None, size_of_subtree=1):
        self.key = key
        self.size_of_subtree = size_of_subtree
        self.left = None
        self.right = None

class KVBST(object):
    def __init__(self):
        self.root = None

    def height(self,node):
        if node is None:
            return 0 ; 
        else :
            lDepth = self.height(node.left)
            rDepth = self.height(node.right)
            if (lDepth > rDepth):
                return lDepth+1
            else:
                return rDepth+1

    def _size(self, node):
        if node is None:
            return 0
        else:
            return node.size_of_subtree

    def size(self):
        return self._size(self.root)

    def is_empty(self):
        return self.Tree_size() == 0

    def _get(self, key, node):
        if node is None:
            return None
        if key < node.key:
            return self._get(key, node.left)
        elif key > node.key:
            return self._get(key, node.right)
        else:
            return node.val

    def get(self, key):
        return self._get(key, self.root)

    def contains(self, key):
        return self.get(key) is not None

    def _insert(self, key, val, node):
        
        if node is None:
            return KVNode(key, val)

        print("node key =  " + str(node.key))
        if key > node.key:
            node.right = self._insert(key, val, node.right)
        elif key < node.key:
            node.left = self._insert(key, val, node.left)
        else:
            node.val = val

        node.size_of_subtree = self._size(node.left) + self._size(node.right)+1
        return node

    def insert(self, key, val):
        self.root = self._insert(key, val, self.root)

    def _min_node(self):
        min_node = self.root
        if min_node is None:
            return None

        while min_node.left is not None:
            min_node = min_node.left

        return min_node

    def min_key(self):
        min_node = self._min_node()
        if min_node is None:
            return None
        else:
            return min_node.key

    def _max_node(self):
        max_node = self.root
        if max_node is None:
            return None

        while max_node.right is not None:
            max_node = max_node.right

        return max_node

    def max_key(self):
        max_node = self._max_node()
        if max_node is None:
            return None
        else:
            return max_node.key

    def _delete(self, key, node):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(key, node.left)
        elif key > node.key:
            node.right = self._delete(key, node.right)

        else:
            if node.right is None:
                return node.left
            elif node.left is None:
                return node.right
            else:
                old_node = node
                node = self._ceiling_node(key, node.right)
                node.right = self._delete_min(old_node.right)
                node.left = old_node.left
        node.size_of_subtree = self._size(node.left) + self._size(node.right)+1
        return node

    def delete(self, key):
        self.root = self._delete(key, self.root)

    def _delete_min(self, node):
        if node.left is None:
            return node.right

        node.left = self._delete_min(node.left)
        node.size_of_subtree = self._size(node.left) + self._size(node.right)+1
        return node

    def delete_min(self):
        self.root = self._delete_min(self.root)

    def _delete_max(self, node):
        if node.right is None:
            return node.left

        node.right = self._delete_max(node.right)
        node.size_of_subtree = self._size(node.left) + self._size(node.right)+1
        return node

    def delete_max(self):
        self.root = self._delete_max(self.root)

    def _disp(self, node, keys):
        if node is None:
            return keys
        if node.left is not None:
            keys = self._disp(node.left, keys)
        keys.append(node.key)
        if node.right is not None:
            keys = self._disp(node.right, keys)
        return keys

    def _preorder(self,node,int_lst):
        if node is not None:
            int_lst.append(node.key)    
            int_lst.append(node.val)        
            self._preorder(node.left,int_lst)
            self._preorder(node.right,int_lst)

    def preorder(self):
        int_lst=[]
        self._preorder(self.root,int_lst)
        return int_lst


    def _postorder(self,node,int_lst):
        if node is not None:
            self._postorder(node.left,int_lst)
            self._postorder(node.right,int_lst)
            int_lst.append(node.key)            
            int_lst.append(node.val)        


    def postorder(self):
        int_lst=[]
        self._postorder(self.root,int_lst)
        return int_lst


    def _inorder(self,node,int_lst):
        if node is not None:
            self._inorder(node.left,int_lst)
            int_lst.append(node.key)
            int_lst.append(node.val)        
            self._inorder(node.right,int_lst)

    def inorder(self):
        int_lst=[]
        # print(str(self.root.key))
        # print(str(self.root.left.key))
        # print(str(self.root.left.left.key))
        # print(str(self.root.left.left.left.key))
        
        self._inorder(self.root,int_lst)
        return int_lst


    def disp(self):
        keys = []
        print (self._disp(self.root, keys))

        
class LBST(object):
    def __init__(self):
        self.root = None


    def height(self,node):
        if node is None:
            return 0 ; 
        else :
            lDepth = self.height(node.left)
            rDepth = self.height(node.right)
            if (lDepth > rDepth):
                return lDepth+1
            else:
                return rDepth+1

    def _size(self, node):
        if node is None:
            return 0
        else:
            return node.size_of_subtree

    def size(self):
        return self._size(self.root)

    def is_empty(self):
        return self.Tree_size() == 0

    def _get(self, key, node):
        if node is None:
            return None
        if key < node.key:
            return self._get(key, node.left)
        elif key > node.key:
            return self._get(key, node.right)
        else:
            return node.key

    def get(self, key):
        return self._get(key, self.root)

    def contains(self, key):
        return self.get(key) is not None

    def _insert(self, key, node):
        if node is None:
            return LNode(key)
        if key < node.key:
            node.left = self._insert(key, node.left)
        elif key > node.key:
            node.right = self._insert(key, node.right)
        else:
            node.key = key
        node.size_of_subtree = self._size(node.left) + self._size(node.right)+1
        return node

    def insert(self, key):
        self.root = self._insert(key, self.root)

    def _min_node(self):
        min_node = self.root
        if min_node is None:
            return None

        while min_node.left is not None:
            min_node = min_node.left

        return min_node

    def min_key(self):
        min_node = self._min_node()
        if min_node is None:
            return None
        else:
            return min_node.key

    def _max_node(self):
        max_node = self.root
        if max_node is None:
            return None

        while max_node.right is not None:
            max_node = max_node.right

        return max_node

    def max_key(self):
        max_node = self._max_node()
        if max_node is None:
            return None
        else:
            return max_node.key

    def _delete(self, key, node):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(key, node.left)
        elif key > node.key:
            node.right = self._delete(key, node.right)

        else:
            if node.right is None:
                return node.left
            elif node.left is None:
                return node.right
            else:
                old_node = node
                node = self._ceiling_node(key, node.right)
                node.right = self._delete_min(old_node.right)
                node.left = old_node.left
        node.size_of_subtree = self._size(node.left) + self._size(node.right)+1
        return node

    def delete(self, key):
        self.root = self._delete(key, self.root)

    def _delete_min(self, node):
        if node.left is None:
            return node.right

        node.left = self._delete_min(node.left)
        node.size_of_subtree = self._size(node.left) + self._size(node.right)+1
        return node

    def delete_min(self):
        self.root = self._delete_min(self.root)

    def _delete_max(self, node):
        if node.right is None:
            return node.left

        node.right = self._delete_max(node.right)
        node.size_of_subtree = self._size(node.left) + self._size(node.right)+1
        return node

    def delete_max(self):
        self.root = self._delete_max(self.root)

    def _disp(self, node, keys):
        if node is None:
            return keys
        if node.left is not None:
            keys = self._disp(node.left, keys)
        keys.append(node.key)
        if node.right is not None:
            keys = self._disp(node.right, keys)
        return keys

    def disp(self):
        keys = []
        print (self._disp(self.root, keys))
    
    def _preorder(self,node,int_lst):
        if node is not None:
            int_lst.append(node.key)            
            self._preorder(node.left,int_lst)
            self._preorder(node.right,int_lst)

    def preorder(self,int_lst):
        self._preorder(self.root,int_lst)
        return int_lst


    def _postorder(self,node,int_lst):
        if node is not None:
            self._postorder(node.left,int_lst)
            self._postorder(node.right,int_lst)
            int_lst.append(node.key)            


    def postorder(self,int_lst):
        self._postorder(self.root,int_lst)
        return int_lst

    def _inorder(self,node,int_lst):
        if node is not None:
            self._inorder(node.left,int_lst)
            int_lst.append(node.key)
            self._inorder(node.right,int_lst)

    def inorder(self,int_lst):
        self._inorder(self.root,int_lst)
        return int_lst



# b=LBST()
# b.insert(5)
# b.insert(10)
# b.insert(53)
# b.insert(101)
# b.inorder()

# import json
# import time
# from memory_profiler import profile
# def func(str):
#     print(str)

# def sum(a, b):
#     print(a+b)

# def sub(a, b):
#     print(a-b)
# @profile
# def main():
#     printf = func
#     sumf = sum
#     subf = sub
#     dic = {"print": printf, "sum": sumf, "sub": subf}
#     prevFunc = None
#     file = open("filing.txt", "r")
#     string = file.read()
#     string = string.split('\n')
#     count = 0
#     jsonS = ""
#     for str in string:
#         try:
#             function = dic[str]
#             continue
#         except:
#             funtion = prevFunc
#         try:
#             function()
#             continue
#         except:
#             pass
#         prevFunc = function
#         if (str.find(":") != -1 or str.find("{") != -1 or str.find("}") != -1):
#             if (str.find("{") != -1):
#                 count = count + 1
#             if (str.find("}") != -1):
#                 count = count - 1
#             jsonS = jsonS + str
#             if (count == 0):
#                 dictionary = json.loads(jsonS)
#                 for i in dictionary:
#                     print(dictionary[i])
#         else:
#             function(str)
# if _name_ == '_main_':
#     start_time = time.time()
#     main()
#     print("--- %s seconds ---" % (time.time() - start_time))
