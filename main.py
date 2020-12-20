import sys
from queue import Queue
_CHOSUNG = [
      'r', 'R', 's', 'e', 'E',
      'f', 'a', 'q', 'Q', 't',
      'T', 'd', 'w', 'W', 'c',
      'z', 'x', 'v', 'g']

_JUNGSUNG = [
      'k', 'o', 'i', 'O', 'j',
      'p', 'u', 'P', 'h', 'hk',
      'ho', 'hl', 'y', 'n', 'nj',
      'np', 'nl', 'b', 'm', 'ml',
      'l']

_JONGSUNG = [
      '', 'r', 'R', 'rt', 's',
      'sw', 'sg', 'e', 'f', 'fr',
      'fa', 'fq', 'ft', 'fx', 'fb',
      'fg', 'a', 'q', 'qt', 't',
      'T', 'd', 'w', 'c', 'z',
      'x', 'v', 'g']

ZAUM = ['q','w','e','r','t','a','s','d','f','g','z','x','c','v','Q','W','E','R','T']
MOUM = ['y','u','i','o','p','h','j','k','l','n','m','b','O','P']

def printUnicode(decimal):
    hangulNumber = decimal
    hexNumberStr = hex(hangulNumber)
    hexNumber = int(hexNumberStr, 16)
    print(hexNumber, hexNumberStr, chr(hexNumber))

def mapping(target, source):
    count = 0
    for i in source:
        target[i] = count
        count += 1

def printCombinedLetter(chosung,jungsung,jongsung):
    a = CHOSUNG[chosung]
    b = JUNGSUNG[jungsung]
    c = JONGSUNG[jongsung]

    result = (a*21 + b)*28+c
    result = 0xAC00 + result
    printUnicode(result)

if __name__ == '__main__':
    CHOSUNG = dict()
    JUNGSUNG = dict()
    JONGSUNG = dict()
    mapping(CHOSUNG,_CHOSUNG)
    mapping(JUNGSUNG,_JUNGSUNG)
    mapping(JONGSUNG,_JONGSUNG)

    # while(True):
    #     char = sys.read()
    #     if(char!= None):
    #         print(char)

    # while True:
    #     try:
    #         print(input())
    #     except EOFError:
    #         break

    # while True:
    #     c1 = chr(input())
    #     print(c1)

    # while True:
    #     c = sys.stdin.read(1)
    #     print(c)

    printUnicode(ord(u'ㄱ'))
    printUnicode(ord(u'ㅏ'))
    printUnicode(ord(u'각'))

    printCombinedLetter('r','k','rt')

    while True:
        c = input()
        beforeIsMoum = False
        result=""
        character = Queue()
        for i in c:
            if beforeIsMoum is False and i in ZAUM:
                character.put(i)



   # printCombinedLetter('ㅅ','ㅗ','ㅇ')