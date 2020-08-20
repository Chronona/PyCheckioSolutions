#!/usr/local/bin/checkio --domain=py run yaml-list-and-comments


import re


def yaml_more_types(a):
    new_list = a.split("\n")
    new_list = [re.sub(":$", ": null", i) for i in new_list if len(i) != 0]
    new_list = [i.split(": ") for i in new_list]
    yaml_key = [i[0] for i in new_list]
    yaml_value = [i[1] for i in new_list]
    yaml_value = [re.sub(" *$", "", i) for i in yaml_value]
    new_yaml_value = []
    for i in yaml_value:
        if i == "false":
            new_yaml_value.append(False)
        elif i == "null":
            new_yaml_value.append(None)
        i = re.sub('"', "", i)
        i = i.replace(chr(92), '"')
        try:
            new_yaml_value.append(int(i))
        except ValueError:
            new_yaml_value.append(i)

    result = dict(zip(yaml_key, new_yaml_value))
    return dict(sorted(result.items()))


def yaml(a):
    if ": " in a:
        return yaml_more_types(a)

    new_list = a.split("\n")
    new_list = [i.replace("-", "") for i in new_list if i.startswith("-")]
    result = []
    for i in new_list:
        if "#" in i:
            if '"' in i:
                i = i.replace('"', "")
                result.append(i[1:])
            else:
                result.append(i[1 : i.index("#", 2) - 1])
        elif i == "":
            result.append(None)
        else:
            if '"' in i:
                i = i.replace('"', "")
            result.append(i[1:])

    result = [int(i) if i is not None and i.isnumeric() else i for i in result]
    return result


if __name__ == "__main__":
    print("Example:")
    print(yaml('- write some\n- "Alex Chii"\n- 89'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml('- write some\n- "Alex Chii"\n- 89') == ["write some", "Alex Chii", 89]
    assert yaml(
        "# comment\n"
        "- write some # after\n"
        "# one mor\n"
        '- "Alex Chii #sir "\n'
        "- 89 #bl"
    ) == ["write some", "Alex Chii #sir ", 89]
    assert yaml("- 1\n- 2\n- 3\n\n- 4\n\n\n\n- 5") == [1, 2, 3, 4, 5]
    assert yaml("-\n-\n-\n- 7") == [None, None, None, 7]
    print("Coding complete? Click 'Check' to earn cool rewards!")
