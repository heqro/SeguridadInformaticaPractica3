import base64

def encode(str_b):
    s = str_b.encode("ascii")
    base_64_by = base64.b64encode(s)
    base_64_by = base_64_by.decode("ascii")
    return base_64_by
def decode(str_b):
    s = str_b.encode("ascii")
    res = base64.b64decode(s)
    res = res.decode("ascii")
    return res


if __name__ == '__main__':
    print(decode("RWplcmNpY2lvQmFzZTY0UmVzdWVsdG8="))
    print(encode(decode("RWplcmNpY2lvQmFzZTY0UmVzdWVsdG8=")))