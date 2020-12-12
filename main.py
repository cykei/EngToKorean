# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
def print_unicode(hexa):
    print(chr(hexa))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hangulNumber = (ord(u"ㄱ")*21+ord(u"ㅏ"))*28
    hexNumberStr = hex(hangulNumber)
    hexNumber = int(hexNumberStr, 16)
    print(hexNumberStr)
    print(chr(hexNumber))
    # print_unicode(0x1100)
    # print_unicode(0x11FF)
    # print_unicode(0x3131)
    # print_unicode(0x318E)
    # print_unicode(0xAC00)
    # print_unicode(0xD7AF)
    # while True:
    #     x = input()
    #     if x == "Q":
    #         break;
    #     else :
    #         print_unicode(int(x,16))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
