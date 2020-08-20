#!/usr/local/bin/checkio --domain=py run yaml-simple-dict


def yaml(a):
    new_list = a.split("\n")
    new_list = [i.split(": ") for i in new_list if len(i) != 0]
    yaml_key = [i[0] for i in new_list]
    yaml_value = [i[1] for i in new_list]
    new_yaml_value = []
    for i in yaml_value:
        try:
            new_yaml_value.append(int(i))
        except ValueError:
            new_yaml_value.append(i)
    result = dict(zip(yaml_key, new_yaml_value))
    return result


if __name__ == "__main__":
    print("Example:")
    print(
        yaml(
            """name: Alex
age: 12"""
        )
    )

    # These "asserts" are used for self-checking and not for an auto-testing
    assert (
        yaml(
            """name: Alex
age: 12"""
        )
        == {"age": 12, "name": "Alex"}
    )
    assert (
        yaml(
            """name: Alex Fox
age: 12

class: 12b"""
        )
        == {"age": 12, "class": "12b", "name": "Alex Fox"}
    )
    print("Coding complete? Click 'Check' to earn cool rewards!")
