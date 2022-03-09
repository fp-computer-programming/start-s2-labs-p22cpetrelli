#author CJP 03/09/2022

#define function
def double_every_other(l):
#returns the value of x times 2 when i % 2
#else enumerate 
    return [x * 2 if i % 2 else x for i, x in enumerate(l)]
