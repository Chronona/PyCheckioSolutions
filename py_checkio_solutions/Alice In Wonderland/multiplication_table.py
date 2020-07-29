#!/usr/local/bin/checkio --domain=py run multiplication-table


def checkio(first, second):
    first = [int(i) for i in format(first, "b")]
    second = [int(i) for i in format(second, "b")]

    def calculation(first, second, operation):
        output = []
        for i in first:
            a = []
            for j in second:
                if operation == "and":
                    a.append(str(i & j))
                elif operation == "or":
                    a.append(str(i | j))
                elif operation == "xor":
                    a.append(str(i ^ j))
            a = "".join(a)
            output.append(int(a, 2))
        return sum(output)

    result = (
        calculation(first, second, "and")
        + calculation(first, second, "or")
        + calculation(first, second, "xor")
    )
    return result


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert checkio(4, 6) == 38
    assert checkio(2, 7) == 28
    assert checkio(7, 2) == 18
