


def input_list():
    lst=[]
    n= int(input("Enter number elements you want to add to list: "))
    for i in range(0,n):
        try:
             num = int(input("Enter num : "))
        # if num is string, raise error. Add only numbers to list
        # if not isinstance(num, (int, float)):
        # if num.is_
            # raise TypeError("Pls enter a valid integer or float")
        except ValueError:
            pass

        lst.append(int(num))

    return lst

def add_list_ele(list_of_num):
    if  len(list_of_num) == 0:
        raise ValueError("Negative list of numbers value error")
    
    sum = 0
    for i in list_of_num:
        sum = sum + i
    return sum


def main():
    list_of_num = input_list()
    sum_of_ele = add_list_ele(list_of_num)
    print(f"Sum of elements in list : {sum_of_ele}")

main()