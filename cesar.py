def rot_n(str_c, n):
    str_res = ""
    for i in str_c:
        num = ord(i)
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


if __name__ == '__main__':
    for i in range(0, 27):
        cesar = rot_n("KqnzilwKmaizKwzzmkbw", i)
        print("Rot {}: {}".format(i, cesar))
