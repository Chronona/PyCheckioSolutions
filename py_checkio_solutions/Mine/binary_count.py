#!/usr/local/bin/checkio --domain=py run binary-count

# 
# END_DESC

def checkio(number: int) -> int:
    return str(bin(number)).count("1")