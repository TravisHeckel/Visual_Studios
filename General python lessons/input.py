mySentence = 'I love the color: '

color_List = ['red','blue','green','pink','teal','black']

def color_Function(name):
    lst = []
    for i in color_List:
        msg = "{0} {1} {2}".format(name,mySentence,i)
        lst.append(msg)
    return lst
        


def get_name():
    go = True
    while go:
            name = input ('What is your name?')
            if name == '':
                print ("you need to provide your name")
            elif name == 'Sally':
                print ("Sally, you may not use this software.")
            else:
                go = False
    lst = color_Function(name)
    for i in lst:
        print(i)


get_name()
