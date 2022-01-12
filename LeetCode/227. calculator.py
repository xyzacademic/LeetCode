class Solution:
    def calculate(self, s):

        n = len(s)

        stack = []

        pre_sign = '+'

        num = 0

        for i in range(n):
            if s[i] != ' ' and s[i].isdigit():
                num = num*10 + int(s[i])
            if i == n-1 or s[i] in '+-*/':
                if pre_sign == '+':
                    stack.append(num)
                elif pre_sign == '-':
                    stack.append(-num)
                elif pre_sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))

                pre_sign = s[i]
                num = 0

        return sum(stack)






if __name__ == '__main__':
    # cal = Solution()

    s = '-1+2*3-6/4'
    print(calculate(s))


