"""
Problem Challenge 3

Cycle in a Circular Array (hard)

We are given an array containing positive and negative numbers. Suppose the
array contains a number ‘M’ at a particular index.

Now, if ‘M’ is positive we will move forward ‘M’ indices and if ‘M’
is negative move backwards ‘M’ indices. You should assume that the array is
circular which means two things:
- If, while moving forward, we reach the end of the array, we will jump to the
  first element to continue the movement.
- If, while moving backward, we reach the beginning of the array, we will jump
  to the last element to continue the movement.

Write a method to determine if the array has a cycle. The cycle should have
more than one element and should follow one direction which means the cycle
should not contain both forward and backward movements.

Example 1
Input: [1, 2, -1, 2, 2]
Output: true
Explanation: The array has a cycle among indices: 0 -> 1 -> 3 -> 0

Example 2
Input: [2, 2, -1, 2]
Output: true
Explanation: The array has a cycle among indices: 1 -> 3 -> 1

Example 3
Input: [2, 1, -1, -2]
Output: false
Explanation: The array does not have any cycle.

My Example
Input: [1, 2, -1, 2, 1, 4]
Output: true
Explanation: The array has a cycle among indices: 3 -> 5 -> 3
"""


def circular_array_loop_exists(nums: list[int]) -> bool:
    def _next(from_idx):
        return (from_idx + nums[from_idx]) % len(nums)

    for idx in range(len(nums) - 1):
        if nums[idx] == 0:
            continue

        slow = fast = idx
        while (
            nums[slow] * nums[_next(slow)] > 0
            and nums[_next(slow)] * nums[_next(_next(slow))] > 0
        ):
            slow = _next(slow)
            fast = _next(_next(fast))
            if slow == fast:
                if fast == _next(fast):
                    break

                return True

        slow = idx
        while nums[slow] * nums[_next(slow)] > 0:
            slow = _next(slow)
            nums[slow] = 0

    return False


def circular_array_loop_exists_custom(nums):
    # if num is negative, it will go from end
    head = nums[0] % len(nums)
    if nums[0] > 0:
        head -= 1
    slow = fast = head

    while True:
        slow = make_move(nums, slow, nums[slow])

        fast = make_move(nums, fast, nums[fast])
        fast = make_move(nums, fast, nums[fast])
        fast = make_move(nums, fast, nums[fast])

        if slow == fast:
            break

    cycle_has_one_direction, cycle_len = cycle_stats(nums, slow)

    if not cycle_has_one_direction:
        return False

    if cycle_len == 1:
        return False

    return True


def make_move(arr, from_idx, steps):
    return (from_idx + steps) % len(arr)


def cycle_stats(arr, slow):
    curr = slow
    cycle_len = 0
    cycle_direction = arr[slow] > 0  # true for forward, false for backward
    cycle_has_one_direction = True

    while True:
        curr = make_move(arr, curr, arr[curr])
        cycle_len += 1
        if arr[curr] > 0 == cycle_direction:
            cycle_has_one_direction = False
        if curr == slow:
            break

    return (cycle_has_one_direction, cycle_len)


def calc_cycle_len(arr, slow):
    curr = slow
    cycle_len = 0
    while True:
        curr = make_move(arr, curr, arr[curr])
        cycle_len += 1
        if curr == slow:
            break

    return cycle_len


def test_grokking():
    assert circular_array_loop_exists([1, 2, -1, 2, 2])
    assert circular_array_loop_exists([2, 2, -1, 2])
    assert not circular_array_loop_exists([2, 1, -1, -2])


def test_custom():
    assert circular_array_loop_exists([1, 2, -1, 2, 1, 4])


def test_leetcode():
    assert circular_array_loop_exists([2, -1, 1, 2, 2])
    assert not circular_array_loop_exists([-1, -2, -3, -4, -5, 6])
    assert circular_array_loop_exists([1, -1, 5, 1, 4])

    # submit tests
    assert not circular_array_loop_exists([-2, 1, -1, -2, -2])
