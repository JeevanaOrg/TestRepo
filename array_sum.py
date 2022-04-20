


def input_list():
    lst=[]
    n= int(input("Enter number elements you want to add to list: "))
    for i in range(0,n):
        num = int(input(f"Enter num {i+1}: "))
        lst.append(num)
    return lst

def add_list_ele(list_of_num):
    sum = 0
    for i in list_of_num:
        sum = sum + i
    return sum


def main():
    list_of_num = input_list()
    sum_of_ele = add_list_ele(list_of_num)
    print(f"Sum of elements in list : {sum_of_ele}")

main()