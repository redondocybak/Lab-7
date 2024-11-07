#LAB7ARC

class Node():
    #constructor
    def __init__(self, value=None, next=None, previous=None):
        self.__value = value 
        self.__next = next  
        self.__previous = previous  
    
    #method to set the value of the node
    def set(self, value):
        self.__value = value
        return self

    #method to get the value of the node
    def get_value(self):
        return self.__value

    #method to get the next node
    def get_next(self):
        return self.__next

    #method to get the previous node
    def get_previous(self):
        return self.__previous

    #method to set the next node
    def set_next(self, next_node):
        self.__next = next_node
        return self

    #method to set the previous node
    def set_previous(self, previous_node):
        self.__previous = previous_node
        return self

#main function for the creation of nodes, links and the displays
def main():
    #nodes
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    
    #linking the nodes
    node1.set_next(node2)
    node2.set_previous(node1).set_next(node3)
    node3.set_previous(node2)
    
    #displays
    print("Node 1 value - ", node1.get_value())
    print("Node 1 next -", node1.get_next().get_value())
    print("----------------------------")

    print("Node 2 value -", node2.get_value())
    print("Node 2 next -", node2.get_next().get_value())
    print("Node 2 previous -", node2.get_previous().get_value())
    print("----------------------------")

    print("Node 3 value -", node3.get_value())
    print("Node 3 previous -", node3.get_previous().get_value())
    print("----------------------------")

main()
