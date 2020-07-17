#!/usr/local/bin/checkio --domain=py run morse-decoder

# Your task is to decrypt the secret message using theMorse code.
# The message will consist of words with 3 spaces between them and 1 space between each letter of each word.
# If the decrypted text starts with a letter then you'll have to print this letter in uppercase.
# 
# 
# 
# Input:The secret message.
# 
# Output:The decrypted text.
# 
# Precondition:
# 0<len(message)<100
# The message will consists of numbers and English letters only.
# 
# 
# END_DESC

MORSE = {'.-':    'a', '-...':  'b', '-.-.':  'c',
         '-..':   'd', '.':     'e', '..-.':  'f',
         '--.':   'g', '....':  'h', '..':    'i',
         '.---':  'j', '-.-':   'k', '.-..':  'l',
         '--':    'm', '-.':    'n', '---':   'o',
         '.--.':  'p', '--.-':  'q', '.-.':   'r',
         '...':   's', '-':     't', '..-':   'u',
         '...-':  'v', '.--':   'w', '-..-':  'x',
         '-.--':  'y', '--..':  'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
        }


def morse_decoder(code):
    result = ""
    code = code.replace("   ", " _ ")
    code = code.split(" ")
    for i in code:
        if i == "_":
            result += " "
            continue
        for j in MORSE:
            if i == j:
                result += MORSE[j]
                break
    if result[0].isalpha():
        result = result[:1].upper() + result[1:]
    return result