# 主程式：攝氏轉華氏的函數
def c_to_f(c: float) -> float:
    return c * 9 / 5 + 32

# 簡單的測試函數，使用 assert 進行測試
def test_c_to_f():
    test_cases = [
        (0, 32),
        (100, 212),
        (-40, -40),
        (37, 98.6)
    ]
    for celsius, expected in test_cases:
        assert c_to_f(celsius) == expected
    print("簡單測試：All passed")

# 使用 unittest 模組進行進一步的單元測試
import unittest

class TestTemperatureConversion(unittest.TestCase):
    def test_cases(self):
        test_cases = [
            (100, 212), (0, 32), (37, 98.6),
            (-40, -40), (-20, -4),
            (1, 33.8), (-1, 30.2)
        ]
        for celsius, expected in test_cases:
            self.assertAlmostEqual(c_to_f(celsius), expected)

# 主程序：執行簡單測試和單元測試
if __name__ == '__main__':
    test_c_to_f()
    unittest.main()

