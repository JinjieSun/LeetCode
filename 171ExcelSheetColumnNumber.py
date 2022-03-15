class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        string_lst = list(string.ascii_uppercase)
        size = len(columnTitle)
        num = 0
        for i in range(size):
            cur_letter = columnTitle[i]
            exp = size - i - 1
            const = string_lst.index(cur_letter) + 1
            num += const * (26 ** exp)
        return num