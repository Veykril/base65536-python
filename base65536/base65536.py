import json

with open('get-block-start.json') as data:
    get_block_start = json.load(data)
with open('get-b2.json') as data:
    get_b2 = json.load(data)

NO_BYTE = -1


def encode(buf):
    strings = []
    i = 0
    for i in range(0, len(buf), 2):
        b1 = buf[i]
        b2 = buf[i + 1] if i + 1 < len(buf) else NO_BYTE
        code_point = get_block_start[str(b2)] + b1
        string = chr(code_point)
        strings.append(string)
    return ''.join(strings)


def decode(string):
    bufs = []
    done = False
    for i in range(0, len(string)):
        code_point = ord(string[i])
        b1 = code_point & ((1 << 8) - 1)
        try:
            b2 = get_b2[str(code_point - b1)]
        except KeyError as e:
            print("Not a valid Base65536 code point: {0}".format(str(code_point)))
        buf = bytearray([b1]) if b2 == NO_BYTE else bytearray([b1, b2])
        if len(buf) == 1:
            if done:
                print("Base65536 sequence continued after final byte")
                raise Exception
            done = True
        bufs.append(buf)
        if code_point >= (1 << 16):
            i += 1
    return b''.join(bufs)
