#!/usr/bin/env python3
# Author ID: ssuresh14

# Global list as required
my_list = [100, 200, 300, 'six hundred']

def give_list():
    # Return the entire global list
    return my_list

def give_first_item():
    # Return first item as string (even if it's an int originally)
    return str(my_list[0])

def give_first_and_last_item():
    # Return a list of first and last elements
    return [my_list[0], my_list[-1]]

def give_second_and_third_item():
    # Return a list containing the second and third elements
    return my_list[1:3]

if __name__ == '__main__':
    print(give_list())
    print(give_first_item())
    print(give_first_and_last_item())
    print(give_second_and_third_item())
