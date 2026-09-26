class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        values = {}

        for key, value in knowledge:
            values[key] = value

        result = []
        i = 0

        while i < len(s):

            if s[i] == '(':
                i += 1
                key = ""

                while s[i] != ')':
                    key += s[i]
                    i += 1

                if key in values:
                    result.append(values[key])
                else:
                    result.append("?")

                i += 1

            else:
                result.append(s[i])
                i += 1

        return "".join(result)
