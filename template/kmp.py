#!/usr/bin/python3
# -*- coding: utf-8 -*-
# __author__ = '__Yunzhe__'

# https://blog.csdn.net/weixin_52622200/article/details/110563434


def generate_next(pattern_text: str):

    #  a   a   b   a   a
    # -1   0
    if len(pattern_text) == 1:
        return [-1]
    k = -1

    n = len(pattern_text)
    j = 0
    next_array = [0] * n
    next_array[0] = -1
    # print(next_array)
    while j < n - 1:
        if k == -1 or pattern_text[k] == pattern_text[j]:

            j += 1
            k += 1
            if pattern_text[j] == pattern_text[k]:
                next_array[j] = next_array[k]

            else:
                next_array[j] = k
        else:
            k = next_array[k]

        print(f"next array: {next_array}, k: {k}, j: {j}")

    return next_array


def kmp(source_text, target_text):

    if target_text == '':
        return 0

    next_array = generate_next(target_text)
    i = 0
    j = 0
    while i < len(source_text):
        if j == -1 or source_text[i] == target_text[j]:
            i += 1
            j += 1
        else:
            j = next_array[j]

        if j == len(target_text):
            return i - len(target_text)

    return -1






if __name__ == '__main__':

    source = 'acbaabaaf'
    target = 'aabaaf'
    generate_next('aabaa')
    # print(kmp(source, target))