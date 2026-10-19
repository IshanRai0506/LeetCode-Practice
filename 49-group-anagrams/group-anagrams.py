
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))

            if sorted_word not in result:
                result[sorted_word] = []

            result[sorted_word].append(word)

        return list(result.values())
