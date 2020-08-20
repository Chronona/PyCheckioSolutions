#!/usr/local/bin/checkio --domain=py run caesar-cipher-decryptor


def to_decrypt(cryptotext, delta):
    words = cryptotext.split(" ")
    result = []
    for word in words:
        answer = ""
        for letter in word:
            if letter.isalpha():
                answer += chr(ord("a") + (ord(letter) - ord("a") + delta) % 26)
        result.append(answer)
    return " ".join(result)


if __name__ == "__main__":
    print("Example:")
    print(to_decrypt("abc", 10))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_decrypt("!d! [e] &f*", -3) == "a b c"
    assert to_decrypt("x^$# y&*( (z):-)", 3) == "a b c"
    assert to_decrypt("iycfbu!@# junj%&", -16) == "simple text"
    assert to_decrypt("*$#%swzybdkxd !)(^#%dohd", -10) == "important text"
    assert to_decrypt("fgngr **&&frperg^__^", 13) == "state secret"
    print("Coding complete? Click 'Check' to earn cool rewards!")
