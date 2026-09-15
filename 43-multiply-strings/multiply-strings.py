class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        result = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                product = int(num1[i]) * int(num2[j])

                pos = i + j + 1
                result[pos] += product

                result[pos - 1] += result[pos] // 10
                result[pos] %= 10

        return ''.join(map(str, result)).lstrip('0')