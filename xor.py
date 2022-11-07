def cod_xor(str_x, k):
    str_res = ""
    for i in range(len(str_x)):
        a = ord(str_x[i])
        b = ord(k[(i % len(k))])
        str_res += chr(a ^ b)
    return str_res


if __name__ == '__main__':
    print(cod_xor("+*5-=;¡.61!47=?9;;;.", "XOR"))
    print(cod_xor("seguriùadinformatica", "XOR"))