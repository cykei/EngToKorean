
_CHOSUNG = [
      'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ',
      'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ',
      'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ',
      'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

_JUNGSUNG = [
      'ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ',
      'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ',
      'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ',
      'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ',
      'ㅣ']

_JONGSUNG = [
      '', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ',
      'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ',
      'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ',
      'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ',
      'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ',
      'ㅌ', 'ㅍ', 'ㅎ']

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
    print(CHOSUNG['ㄷ'])

    printUnicode(ord(u'ㄱ'))
    printUnicode(ord(u'ㅏ'))
    printUnicode(ord(u'각'))

    printCombinedLetter('ㅅ','ㅗ','ㅇ')