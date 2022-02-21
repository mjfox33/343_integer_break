from code_343_integer_break import Solution

def test_example_1():
    s = Solution()
    n = 2
    output = 1
    assert s.integerBreak(n) == output

def test_example_2():
    s = Solution()
    n = 10
    output = 36
    assert s.integerBreak(n) == output
