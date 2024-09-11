class Solution:
    """
    I couldn't understand NeetCode's solution and had to rewatch 4 times until I got it. In case you don't get my writing, please see NeetCode's explanation first.
    https://www.youtube.com/watch?v=fFVZt-6sgyo

    Essentially this problem is like two sum, but the hashmap is more complicated. To understand this problem you must understand how to form this hashmap.

    In two sum, the hasmap key was `target - curr_val`, and hashmap value is `index_of(curr_val)`.
    Here, the hashmap behaves the same way, but because the problem is about **summing up the subarrays**, we sum up the current subarray and write the `k - sum_of_subarray` into the hashmap.

    That is exactly the same logic we had in two sum. We want to know the remainder, so that we would use that reminder to add up to target.
    In our solution to this problem, every time we iterate over the new subarrays we look up the hashmap if it has `sum_of_subarray - k` value (remainder).
    What that essentially means is that we want to know if there are any other subarrays we saw in the past that we can combine to our current subarray.

    If there were some subarrays in the past with remainder -- we add those values up to `answer`. Remember, if `sum_of_subarray - k != 0` , that means we did not reach the `sum_of_subarray` to be `k`, this is why we look up our hashmap to find if there is any subarrays that can complement to our total.
    We return the number of subarrays found in the hashmap because again, our current `sum_of_subarray` is not enough (not equal to `k`), and to reach `k` you need to query hashmap.

    Think about this imaginary problem, which is a modified two sum:
        - imagine we have this array: `[1, 2, 3, 4, 5, 6, 3]`, and `target` or `k` is 9
        - we want to return the amount of pairs of numbers (a pair consist of 2 numbers) that add up to `target` or `k`
        - for each of the value in array (`curr_val`) we compute `k - curr_val` and save the count of such values in our hashmap
        - so for this example our hashmap is {8: 1, 7: 1, 6: 2, 5: 1, 6: 1, 4: 1, 3: 1}

    That's exactly how the hashmap works in this example as well. Now knowing how the hashmap works, look at the code.
    """

    def subarraySum(self, nums: list[int], k: int) -> int:
        res = 0
        cur_sum = 0
        prefix_sums = {0: 1}

        for n in nums:
            cur_sum += n
            diff = cur_sum - k

            res += prefix_sums.get(diff, 0)
            prefix_sums[cur_sum] = 1 + prefix_sums.get(cur_sum, 0)

        return res
