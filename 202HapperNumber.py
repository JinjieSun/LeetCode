class Solution:
    def isHappy(self, n: int) -> bool:
        exists = []
        str_lst = str(n).replace("0","")
        end = False
        while not end:
            if str_lst == "1":
                return True
            else:
                num = 0
                for i in str_lst:
                    num += int(i) ** 2
                if num in exists:
                    return False
                str_lst = str(num).replace("0","")
                exists.append(num)
        return 