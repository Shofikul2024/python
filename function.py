

# def addTwo (a,b):
#     num1 = a
#     num2 = b
#     print(num1 + num2)


# addTwo(500,1000 )


# def addTwo (a,b):
#     num1 = a
#     num2 = b
    
#     if num1< num2:
        
#         break
#     print(num1 + num2)


# addTwo(500,1000 )












my_list = [2, 3, 4, 5, 6, 7]

def is_even(x):
    if (x % 2) == 0:
        return True
    else:
        return False

new_list = filter(is_even, my_list)
print(new_list)
print(list(new_list))