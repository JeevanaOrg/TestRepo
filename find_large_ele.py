

def input_list():
    lst = []
    n = int(input("Enter number elements you want to add to list: "))
    for i in range(0, n):
        num = int(input(f"Enter num {i+1}: "))
        lst.append(num)
    return lst


def find_large_element(list_of_num):
    max = list_of_num[0]
    for i in range(1, len(list_of_num)):
        if list_of_num[i] > max:
            max = list_of_num[i]

    return max


def main():
    list_of_num = input_list()
    large_ele = find_large_element(list_of_num)
    print(f"Large number in the list : {large_ele}")


main()
