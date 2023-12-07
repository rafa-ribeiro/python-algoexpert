class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def add_child(self, name):
        self.children.append(Node(name))
        return self

    def depth_first_search(self, array):
        """

        Complexity:

        Time: O(v+e)
        Space: O(v)

        Where:
            - v is the number of vertices of the tree
            - e is the number of edges of the tree

        """

        array.append(self.name)
        for child in self.children:
            child.depth_first_search(array)

        return array
