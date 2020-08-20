#!/usr/local/bin/checkio --domain=py run caesar-cipher-encryptor


def to_encrypt(text, delta):
    answer = ""
    for letter in text:
        if letter == " ":
            answer += letter
        else:
            answer += chr(ord("a") + (ord(letter) - ord("a") + delta) % 26)
    return answer


if __name__ == "__main__":
    print("Example:")
    print(to_encrypt("abc", 10))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")
