# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def print_hello2theworld(name1):
    print(f'YES, {name1}')


# Press the green button in the gutter to runs the script.
if __name__ == '__main__':

    _HELLO_WORLD = str("I don't know what a regular expression is")
    print(_HELLO_WORLD)
    # print_hi('PyCharm')
    # print_hello2theworld('Hello World !')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Taking input from the user
    name2 = input("Enter your name: ")
    if name2 != "YZS":
        print('You got the wrong name !')
    else :
        # Output
        print(f"Hello, " + name2)
        print(type(name2))



