def print_return_tuple(arg1, *vartuple):
    print("Inside arg1 is : ", arg1)
    for var in vartuple:
        print("Inside vartuple is : ", var)
    return vartuple

print_return_tuple(10)
out_tuple = print_return_tuple(70, 60, 50)
print(out_tuple)
