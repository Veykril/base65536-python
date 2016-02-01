import base65536

for b in range(0, 256):
    buf1 = bytearray([b])
    str1 = base65536.encode(buf1)
    buf2 = base65536.decode(str1)
    if buf1 != buf2:
        raise Exception

firstDefectStr = base65536.encode(bytearray([0, 110]))
firstDefectBuf = base65536.decode(firstDefectStr)
print(ord(firstDefectStr[0]) == 67072)
print(ord(firstDefectStr[0]) == 0x10600)
print(firstDefectBuf == bytearray([0, 110]))

for b1 in range(0, 256):
    for b2 in range(0, 256):
        buf1 = bytearray([b1, b2])
        str1 = base65536.encode(buf1)
        buf2 = base65536.decode(str1)
        if buf1 != buf2:
            raise Exception

buf = bytearray(b"hello world")
enc = base65536.encode(buf)
print(enc == "驨ꍬ啯𒁷ꍲᕤ")
dec = base65536.decode(enc)
print(dec == buf)

print("OK")