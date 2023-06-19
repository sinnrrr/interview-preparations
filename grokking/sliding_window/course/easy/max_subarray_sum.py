import pytest


def max_sub_array_of_size_k(k, arr):
    window_start, window_sum, max_sum = 0, 0, 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        if (window_end >= k - 1):
            max_sum = max(window_sum, max_sum)
            window_sum -= arr[window_start]
            window_start += 1

    return max_sum


@pytest.mark.parametrize(
    "k, arr, expected",
    [(3, [2, 1, 5, 1, 3, 2], 9), (2, [2, 3, 4, 1, 5], 7)],
)
def test_max_sub_array_of_size_k(k, arr, expected):
    assert max_sub_array_of_size_k(k, arr) == expected
