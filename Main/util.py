from math import sqrt
import heapq as heap
import matplotlib.pyplot as plt
import numpy


def make_empty_grid(size):
    return numpy.zeros((size, size))


def get_element_from_list(input_list, element):
    for i in input_list:
        if i == element:
            return i
    return None


def closer_from_start(old_state, new_state):
    return new_state.gx < old_state.gx

# Here we are replacing the element to be popped with the last element and removing the last element and then re-heapify
# we hope this logic saves more time then shifting all the elements by one positions to delete the given element
def update_with_child(input_list, key, new_key):
    i = 0
    while i < len(input_list):
        element = input_list[i]
        if element == key:
            input_list[i] = input_list[-1]
            input_list.pop()
            heap.heapify(input_list)
            heap.heappush(input_list, new_key)
            break
        i += 1


def find_path(start_state, end_state):
    path = []
    temp_state = end_state
    while temp_state != start_state:
        path.insert(0, temp_state)
        temp_state = temp_state.parent_state
    return path


def add_to_final_path(final_path, start_state, final_state):
    final_path += find_path(start_state, final_state)


def print_path(path):
    print("x  y gx  hx  fx")
    for state in path:
        print(state.x, "  ", state.y, " ", state.gx, "  ", state.hx, "  ", state.get_fx())


def print_list(input_list):
    for element in input_list:
        print(element.x, "   ", element.y)


def generate_graph(x, y, title, x_label, y_label, line_label=""):
    if isinstance(y[0], list):
        i = 0
        while i < len(y):
            plt.plot(x, y[i], label=line_label[i])
            i = i+1

    else:
        plt.plot(x, y, label=line_label)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    leg = plt.legend(loc='upper center')
    plt.show()


'''

[[0. 0. 1. 0. 1. 0. 0. 1. 0. 0.]
 [0. 0. 1. 1. 1. 0. 1. 1. 0. 0.]
 [1. 0. 0. 1. 1. 0. 0. 0. 1. 0.]
 [1. 1. 0. 0. 1. 1. 0. 0. 1. 0.]
 [1. 1. 0. 0. 1. 0. 0. 1. 0. 0.]
 [1. 1. 1. 0. 1. 1. 0. 1. 0. 0.]
 [0. 0. 0. 0. 1. 1. 1. 1. 0. 0.]
 [1. 0. 0. 0. 0. 0. 1. 0. 0. 0.]
 [0. 0. 0. 1. 1. 1. 1. 1. 1. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
'''
