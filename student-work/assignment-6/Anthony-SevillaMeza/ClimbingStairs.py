class Solution:
    #fibonacci
    def climbStairs(self, n: int) -> int:
        distinct = []
        
        for i in range(n):
            distinct += [0]
        
        for j in range(n):
            if j == 0:
                distinct[j] = 1
            elif j == 1:
                distinct[j] = 2
            else:
                distinct[j] = distinct[j-1] + distinct[j-2]
        return distinct[-1]


# --- More comprehensive test cases ---
def test_climb_stairs():
    sol = Solution()
    test_cases = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
        (6, 13),
        (10, 89),   # Larger input
    ]

    for i, (n, expected) in enumerate(test_cases):
        result = sol.climbStairs(n)
        print(f"Test {i+1}: n = {n}")
        print(f"  Expected: {expected}")
        print(f"  Got:      {result}")
        print(f"  {'PASS' if result == expected else 'FAIL'}\n")

# Run the tests
test_climb_stairs()