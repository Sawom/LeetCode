class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        n = len(s)

        for i in range(n-1):
            if roman_values[s[i]] < roman_values[s[i+1]]:
                total = total - roman_values[s[i]]
            else:
                total = total + roman_values[s[i]]

        total = total + roman_values[s[n-1]]

        return total

# ide sample input
if __name__ == "__main__":
    obj = Solution()
    print(obj.romanToInt("III"))
    print(obj.romanToInt("LVIII"))
    print(obj.romanToInt("MCMXCIV"))