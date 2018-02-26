# password = ''
# while password != 'password123':
#     password = input('\nEnter the password: ')
#     if password == 'password123':
#         print('You are logged in!!!\n')
#     else:
#         print('try again!!!')

# a = ['1','2', '3', '4', '5','6','7']
# b = ['mon', 'tue', 'wed', 'thur', 'fri', 'sat', 'sun']
# c = ['','','','','','Holiday', 'holiday']
#
# for i,j,z in zip(a,b,c):
#     print(i,j,z)

def c_to_f(c):
    if c< -273.15:
        return "That temperature doesn't make sense!"
    else:
        f=c*9/5+32
        return f
    
temperatures=[10,-20,-289,100]

for i in temperatures:
    print(c_to_f(i))

