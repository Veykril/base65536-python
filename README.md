# base65536

A Base65536 implementation written in Python 3 based on this [javascript version](https://github.com/ferno/base65536/).

## Usage

```
import base65536

buf = new bytearray(b"hello world"); // 11 bytes

string = base65536.encode(buf); 
print(string); // 6 code points, "驨ꍬ啯𒁷ꍲᕤ"

buf2 = base65536.decode(string);
print(buf.equals(buf2)); // true
```

## API

### base65536.encode(buf)

Encodes a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) and returns a Base65536 `String`, suitable for passing safely through almost any "Unicode-clean" text-handling API. This string contains no special characters and is immune to Unicode normalization. The string encodes two bytes per code point.

### base65536.decode(str)

Decodes a Base65536 `String` and returns a `bytes-like object` containing the original binary data.

This function is currently very strict, with no tolerance for whitespace or other unexpected characters. An `Error` is thrown if the supplied string is not a valid Base65536 text, or if there is a "final byte" code point in the middle of the string.

## More examples

```
uuid = "8eb44f6c-2505-4446-aa57-22d6897c9922";   // 32 hex digits
buf = bytearray(uuid.replace('-', ''));          // <Buffer 8e b4 ... 22>
print(base65546.encode(buf));                    // "𣪎ꍏ㤥筄貪𥰢𠊉垙", 8 chars
```

## License

MIT