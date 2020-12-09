def differenceVars(*var_args01, **var_args02):
    print(var_args01, type(var_args01))
    print(var_args02, type(var_args02))

differenceVars(1,2,3,4,5,6,a=2,b=3,c=5)

args_list=[1,2,3,4]
args_dict={'a':10, 'b':20}
differenceVars(*args_list, **args_dict)
