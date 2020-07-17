#!/usr/local/bin/checkio --domain=py run sort-by-extension
from typing import List


def sort_by_ext(files: List[str]) -> List[str]:
    file_dict = {}
    no_name = []
    for i in range(len(files)):
        file = files[i].rsplit(".", 1)
        name = file[0]
        extension = file[1]
        if name == "":
            no_name.append("." + extension)
            continue
        file_dict[i] = [name, extension]
    file_dict = sorted(file_dict.items(), key=lambda x: (x[1][1], x[1][0]))
    result = [".".join(j) for i, j in file_dict]
    if len(no_name) != 0:
        no_name.extend(result)
        return no_name
    return result
