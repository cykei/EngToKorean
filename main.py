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
    'np', 'nl', 'b', 'm', 'ml', 'l']

_JONGSUNG = [
    '', 'r', 'R', 'rt', 's',
    'sw', 'sg', 'e', 'f', 'fr',
    'fa', 'fq', 'ft', 'fx', 'fb',
    'fg', 'a', 'q', 'qt', 't',
    'T', 'd', 'w', 'c', 'z',
    'x', 'v', 'g']

_LETTER = [
    'r', 'R', 'rt', 's', 'sw', 'sg', 'e', 'E', 'f', 'fr',
    'fa', 'fq', 'ft', 'fx', 'fv', 'fg', 'a', 'q', 'Q', 'qt',
    't', 'T', 'd', 'w', 'W', 'c', 'z', 'x', 'v', 'g',
    'k', 'o', 'i', 'O', 'j', 'p', 'u', 'P', 'h', 'hk',
    'ho', 'hl', 'y', 'n', 'nj', 'np', 'nl', 'b', 'm', 'ml', 'l'
]

ZAUM = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'Q', 'W', 'E', 'R', 'T']
MOUM = ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm', 'b', 'O', 'P']


def convertToKorean(decimal):
    hangulNumber = decimal
    hexNumberStr = hex(hangulNumber)
    hexNumber = int(hexNumberStr, 16)
    return (chr(hexNumber))


def mapping(target, source):
    count = 0
    for i in source:
        target[i] = count
        count += 1


def getCombinedLetter(chosung, jungsung, jongsung):
    a = CHOSUNG[chosung]
    b = JUNGSUNG[jungsung]
    c = JONGSUNG[jongsung]

    result = (a * 21 + b) * 28 + c
    result = 0xAC00 + result
    return convertToKorean(result)


def getLetter(char):
    result = 0x3131 + LETTER[char]
    return chr(result)


def isZAUM(char):
    if char in ZAUM:
        return True
    return False


def isMOUM(char):
    if char in MOUM:
        return True
    return False


def isChosung(char):
    if char in CHOSUNG:
        return True
    return False


def isJungsung(char):
    if char in JUNGSUNG:
        return True
    return False


def isJongsung(char):
    if char in JONGSUNG:
        return True
    return False


def getKoreanString(englishString):
    korean_str = ""
    one_letter = Queue()

    queue = list()
    for i in englishString:
        queue.append(i)

    cnt = 0
    while cnt < len(queue):
        front = queue[cnt]
        qsize = one_letter.qsize()
        if not isZAUM(front) and not isMOUM(front):
            temp = list()
            for i in range(qsize):
                temp.append(one_letter.get())

            if qsize is 1 and isChosung(temp[0]):
                korean_str += getLetter(temp[0])
            elif qsize is 2 and isChosung(temp[0]) and isJungsung(temp[1]):
                korean_str += getCombinedLetter(temp[0], temp[1], '')
            elif qsize is 3 and isChosung(temp[0]) and isJungsung(temp[1]) and isJongsung(temp[2]):
                korean_str += getCombinedLetter(temp[0], temp[1], temp[2])
            elif qsize is 4 and isChosung(temp[0]) and isJungsung(temp[1]) and isJongsung(temp[2] + temp[3]):
                korean_str += getCombinedLetter(temp[0], temp[1], temp[2]+temp[3])
            else:
                for i in range(qsize):
                    korean_str += getLetter(temp[0])
            korean_str += front
        elif qsize is 0 and isChosung(front):
            one_letter.put(front)
        elif qsize is 1 and isJungsung(front):
            one_letter.put(front)
        elif qsize is 2 and isChosung(front):
            one_letter.put(front)
        elif qsize is 2 and isJungsung(front):
            chosung = one_letter.get()
            jungsung = one_letter.get()
            combinedJungsung = jungsung + front
            if isJungsung(combinedJungsung):
                one_letter.put(chosung)
                one_letter.put(combinedJungsung)
            else:
                korean_str += getCombinedLetter(chosung, jungsung, '')
                korean_str += getLetter(front)
        elif qsize is 3 and isJungsung(front):
            korean_str += getCombinedLetter(one_letter.get(), one_letter.get(), '')
            one_letter.put(front)
        elif qsize is 3 and isChosung(front):
            if cnt + 1 < len(queue) and isJungsung(queue[cnt + 1]):
                korean_str += getCombinedLetter(one_letter.get(), one_letter.get(), one_letter.get())
                one_letter.put(front)
            elif cnt + 1 < len(queue) and isChosung(queue[cnt + 1]):
                chosung = one_letter.get()
                jungsung = one_letter.get()
                jongsung = one_letter.get()
                combinedJongsung = jongsung + front
                if (isJongsung(combinedJongsung)):
                    korean_str += getCombinedLetter(chosung, jungsung, combinedJongsung)
                else:
                    korean_str += getCombinedLetter(chosung, jungsung, jongsung)
                    one_letter.put(front)
            else:
                one_letter.put(front)
        else:
            if qsize is 1:
                korean_str += getLetter(one_letter.get())
                one_letter.put(front)
        cnt += 1
    if one_letter.qsize() is 1:
        korean_str += getLetter(one_letter.get())
    elif one_letter.qsize() is 2:
        korean_str += getCombinedLetter(one_letter.get(), one_letter.get(), '')
    elif one_letter.qsize() is 3:
        korean_str += getCombinedLetter(one_letter.get(), one_letter.get(), one_letter.get())
    elif one_letter.qsize() is 4:
        korean_str += getCombinedLetter(one_letter.get(), one_letter.get(), (one_letter.get() + one_letter.get()))
    return korean_str


if __name__ == '__main__':
    CHOSUNG = dict()
    JUNGSUNG = dict()
    JONGSUNG = dict()
    LETTER = dict()
    mapping(CHOSUNG, _CHOSUNG)
    mapping(JUNGSUNG, _JUNGSUNG)
    mapping(JONGSUNG, _JONGSUNG)
    mapping(LETTER, _LETTER)

    while True:
        ss = input()
        if ss is '':
            break
        print(getKoreanString(ss))
