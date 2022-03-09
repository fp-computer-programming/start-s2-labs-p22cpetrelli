#author CJP 03/07/2022
#defines function
def smash(lst):
#empty string
    x = ""
#enumerate to seperate index and value
    for i, v in enumerate(lst):
        if i == 0:
            x = x + v
        else:
            x = x + " " + v
#returns function
    return x
print(smash(["My", "name", "is", "cam."]))