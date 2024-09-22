#!/bin/python3

import os


def binary_search(arr, val):
    lp, rp = 0, len(arr) - 1
    while lp <= rp:
        mp = (lp + rp) // 2
        if arr[mp] == val:
            return mp

        if arr[mp] < val:
            lp = mp
        elif arr[mp] > val:
            rp = mp
    return rp


def numberOfItems(s, startIndices, endIndices):
    wall_indices = [idx for idx, char in enumerate(s) if char == "|"]
    i, n = 0, len(startIndices)
    res = []

    while i < n:
        start, end = startIndices[i], endIndices[i]

        start_wall_idx = binary_search(wall_indices, start)
        end_wall_idx = binary_search(wall_indices, end)

        total = (wall_indices[end_wall_idx] - wall_indices[start_wall_idx]) - (
            end_wall_idx - start_wall_idx
        )
        res.append(total)

        i += 1

    return res


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    startIndices_count = int(input().strip())

    startIndices = []

    for _ in range(startIndices_count):
        startIndices_item = int(input().strip())
        startIndices.append(startIndices_item)

    endIndices_count = int(input().strip())

    endIndices = []

    for _ in range(endIndices_count):
        endIndices_item = int(input().strip())
        endIndices.append(endIndices_item)

    result = numberOfItems(s, startIndices, endIndices)

    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
