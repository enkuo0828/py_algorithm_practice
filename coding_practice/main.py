# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def binary_search_tree(order_list: list) -> list:
    # Use a breakpoint in the code line below to debug your script.

    return order_list


class Node:
    def __init__(self, val, left_node=None, right_node=None):
        self.val = val
        self.left_node = left_node
        self.right_node = right_node

    def __str__(self):
        return f'''{self.val}'''

    def in_order(self):



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = [5, 3, 2, 6, 8, 9, 1, 7, 4]
    n = Node(a)
    print(n)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
