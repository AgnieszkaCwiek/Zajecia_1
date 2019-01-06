import os
import os.path

import hashlib


def przegladanie(root, starting_dict=None):
    file_list = os.listdir(root)
    filesizes = starting_dict or {}
    dir_list = []
    for item in file_list:
        if os.path.isfile(os.path.join(root, item)):
            full_name = os.path.join(root, item)
            file_size = os.path.getsize(full_name)
            print(full_name, file_size)

            if file_size in filesizes:
                filesizes[file_size].append(item)
            else:
                filesizes[file_size] = [item]

        if os.path.isdir(os.path.join(root, item)):
            dir_list.append(item)
    for dirname in dir_list:
        przegladanie(os.path.join(root, dirname), filesizes)

    return filesizes

print(przegladanie('.'))


def przegladanie_md5(root, starting_dict=None):
    file_list = os.listdir(root)
    hashes = starting_dict or {}
    dir_list = []
    for item in file_list:
        if os.path.isfile(os.path.join(root, item)):
            full_name = os.path.join(root, item)
            file_size = os.path.getsize(full_name)

            with open(full_name) as file:
                checksum = hashlib.md5(file.read().encode(encoding='utf-8')).hexdigest()

            print(full_name, file_size)

            if checksum in hashes:
                hashes[checksum].append(item)
            else:
                hashes[checksum] = [item]

        if os.path.isdir(os.path.join(root, item)):
            dir_list.append(item)
    for dirname in dir_list:
        przegladanie_md5(os.path.join(root, dirname), hashes)

    return hashes

print(przegladanie_md5('.'))