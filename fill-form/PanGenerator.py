import random
import string


def generator(name):
    letters=string.ascii_uppercase
    numbers="01234568789"
    final_pan=random.sample(letters,4)
    name=name.split()
    final_pan.append(name[1][0])
    final_pan.append(random.sample(numbers,4))
    final_pan.append(random.sample(letters,1))
    new_pan=''
    for element in final_pan:
        if type(element) is list:
            for item in element:
                new_pan=new_pan+item
        else:
            new_pan=new_pan+element

    return new_pan