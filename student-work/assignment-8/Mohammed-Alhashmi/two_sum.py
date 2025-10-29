from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in seen:
            return [seen[diff], i]
        seen[n] = i
    return []

if __name__ == "__main__":
    tests = [
        ([2,7,11,15], 9),
        ([3,2,4], 6),
        ([3,3], 6),
    ]
    for nums, target in tests:
        print(f"two_sum({nums}, {target}) -> {two_sum(nums, target)}")
