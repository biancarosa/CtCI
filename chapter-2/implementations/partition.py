class LinkedList():

    def __init__(self, node=None):
        self.head = node


class Node():

    def __init__(self, data):
        self.next = None
        self.data = data


def partition(linked_list, n=0):
    node = linked_list.head
    left_list = LinkedList()
    right_list = LinkedList()
    last_left_node = None
    last_right_node = None
    while node != None:
        if node.data < n:
            if not left_list.head:
                left_list.head = Node(node.data)
                last_left_node = left_list.head
            else:
                last_left_node.next = Node(node.data)
                last_left_node = last_left_node.next
        else:
            if not right_list.head:
                right_list.head = Node(node.data)
                last_right_node = right_list.head
            else:
                last_right_node.next = Node(node.data)
                last_right_node = last_right_node.next
        node = node.next
    last_left_node.next = right_list.head
    linked_list.head = left_list.head


def main():
    node = Node(3)
    ll = LinkedList(node)
    node.next = Node(5)
    node = node.next
    node.next = Node(5)
    node = node.next
    node.next = Node(8)
    node = node.next
    node.next = Node(5)
    node = node.next
    node.next = Node(10)
    node = node.next
    node.next = Node(2)
    node = node.next
    node.next = Node(1)
    node = node.next
    partition(ll, 5)

    node = ll.head
    while (node):
        print(node.data, ' - ', end='')
        node = node.next


if __name__ == '__main__':
    main()
