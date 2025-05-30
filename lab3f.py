#!/usr/bin/env python3

# Define the global list
my_list = [1, 2, 3, 4, 5]

def add_item_to_list(ordered_list):
    # Appends one more than the last item in the list
    if len(ordered_list) > 0:
        last_item = ordered_list[-1]
        ordered_list.append(last_item + 1)

def remove_items_from_list(ordered_list, items_to_remove):
    # Removes items found in items_to_remove from ordered_list
    for item in items_to_remove:
        while item in ordered_list:
            ordered_list.remove(item)

# Main execution block
if __name__ == '__main__':
    print(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    print(my_list)
    remove_items_from_list(my_list, [1, 5, 6])
    print(my_list)
