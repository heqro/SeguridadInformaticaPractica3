def vigenere_e(s, key):
    str_res = ""
    for i in range(len(s)):
        num = ord(s[i])
        n = ord(key[i % len(key)])

        if 97 <= n <= 122:
            n -= 97
        elif 65 <= n <= 90:
            n -= 65
        else:
            n = 0
        if 97 <= num <= 122:
            num -= 97
            res = (num + n) % 26
            str_res += chr(res + 97)
        elif 65 <= num <= 90:
            num -= 65
            res = (num + n) % 26
            str_res += chr(res + 65)
        else:
            str_res += i
    return str_res


def vigenere_d(s, key):
    str_res = ""
    for i in range(len(s)):
        num = ord(s[i])
        n = ord(key[i % len(key)])

        if 97 <= n <= 122:
            n -= 97
        elif 65 <= n <= 90:
            n -= 65
        else:
            n = 0
        if 97 <= num <= 122:
            num -= 97
            res = (num - n) % 26
            str_res += chr(res + 97)
        elif 65 <= num <= 90:
            num -= 65
            res = (num - n) % 26
            str_res += chr(res + 65)
        else:
            str_res += i
    return str_res


if __name__ == '__main__':
    print(vigenere_d("QqmiaiiiYmisqmwmxijs", "Vigenere"))
    print(vigenere_e("VigenereDecodificado", "Vigenere"))
