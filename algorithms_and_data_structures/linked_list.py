class node:
    def __init__(self,value):
        self.value = value
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    def prepend(self,value):
        new_node = node(value)
        new_node.next = self.head
        self.head = new_node 


    def append(self,value):
        new_node = node(value)
        if self.head is None:
            self.head = new_node 
            return 
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node 

    def remove(self,value):
        if self.head is None:
            return 
        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(f"[{current.value}]",end="->")
            current = current.next
        print("None")

if __name__ == "__main__":
    my_linked_list = linked_list()
    # append operations o(n)
    my_linked_list.append(10)
    my_linked_list.append(14)
    my_linked_list.append(13)
    my_linked_list.append(22)
    # prepend operations o(1)
    my_linked_list.prepend(5)
    
    my_linked_list.display()
    # remove operations o(n)
    my_linked_list.remove(22)
    my_linked_list.display()



