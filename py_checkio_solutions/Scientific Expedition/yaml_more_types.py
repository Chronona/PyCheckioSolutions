#!/usr/local/bin/checkio --domain=py run yaml-more-types


import re


def yaml(a):
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


if __name__ == "__main__":
    print("Example:")
    print(yaml("name: Alex\nage: 12"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml("name: Alex\nage: 12") == {"age": 12, "name": "Alex"}
    assert yaml("name: Alex Fox\n" "age: 12\n" "\n" "class: 12b") == {
        "age": 12,
        "class": "12b",
        "name": "Alex Fox",
    }, "two"
    assert yaml('name: "Alex Fox"\n' "age: 12\n" "\n" "class: 12b") == {
        "age": 12,
        "class": "12b",
        "name": "Alex Fox",
    }, "three"
    assert yaml('name: "Alex \\"Fox\\""\n' "age: 12\n" "\n" "class: 12b") == {
        "age": 12,
        "class": "12b",
        "name": 'Alex "Fox"',
    }, "four"
    assert yaml('name: "Bob Dylan"\n' "children: 6\n" "alive: false") == {
        "alive": False,
        "children": 6,
        "name": "Bob Dylan",
    }, "five"
    assert yaml('name: "Bob Dylan"\n' "children: 6\n" "coding:") == {
        "children": 6,
        "coding": None,
        "name": "Bob Dylan",
    }, "six"
    assert yaml('name: "Bob Dylan"\n' "children: 6\n" "coding: null") == {
        "children": 6,
        "coding": None,
        "name": "Bob Dylan",
    }, "seven"
    assert yaml('name: "Bob Dylan"\n' "children: 6\n" 'coding: "null" ') == {
        "children": 6,
        "coding": "null",
        "name": "Bob Dylan",
    }, "eight"
    print("Coding complete? Click 'Check' to earn cool rewards!")
