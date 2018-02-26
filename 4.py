# with open('/Users/Kumaran/Downloads/fruits.txt', 'r') as fb:
#     data = fb.readlines()
#     print([len(e.rstrip('\n')) for e in data])


# with open('/Users/Kumaran/Desktop/delete.txt', 'w') as tb:
#     with open('/Users/Kumaran/Downloads/fruits.txt', 'r') as fb:
#         data = fb.readlines()
#         data1 = [e.rstrip('\n') for e in data]
#         for i in data1:
#             tb.write(i +'\n')

# with open('/Users/Kumaran/Desktop/delete.txt', 'w+') as file:
#     data = file.read()
#     data = [e.rstrip('\n') for e in data]
#     [e for e in data if e == 'apple']
#     file.write('This is good for health')

temperatures=[10,-20,-289,100]


def c_to_f(c):
    if c < -273.15:
        return "That temperature doesn't make sense!"
    else:
        f = c * 9 / 5 + 32
        return f

with open('/Users/Kumaran/Desktop/delete1.txt', 'w+') as file:
    for t in temperatures:
        f = c_to_f(t)
        print(f, file=file)

""" This is tessting the docstring in python
lets check it out
"""