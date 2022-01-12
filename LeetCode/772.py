def calculate(s):
    def cal(x, y, opt):
        if opt == '+':
            return x + y
        elif opt == '-':
            return x - y
        elif opt == '*':
            return x * y
        else:
            return x // y
    n = len(s)
    priority = {
        '(': 0,
        ')': 0,
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
    }

    opt_stack = []
    num_stack = []
    opt = set(list('+-*/()'))
    num = 0
    i = 0
    while i < n:
        if s[i] == ' ':
            i += 1
            continue

        elif s[i].isdigit():
            num = int(s[i])
            while i+1<n and s[i+1].isdigit():
                num = num * 10 + int(s[i+1])
                i += 1
            num_stack.append(num)

        elif s[i] == '(':
            opt_stack.append(s[i])
        elif s[i] == ')':
            while opt_stack and opt_stack[-1] != '(':
                opt_ = opt_stack.pop()
                y = num_stack.pop()
                x = num_stack.pop()
                z = cal(x, y, opt_)
                num_stack.append(z)
            opt_stack.pop()
        else:
            while opt_stack and priority[opt_stack[-1]] >= priority[s[i]]:
                opt_ = opt_stack.pop()
                y = num_stack.pop()
                x = num_stack.pop()
                z = cal(x, y, opt_)
                num_stack.append(z)
            opt_stack.append(s[i])
        i += 1

    while opt_stack:
        opt_ = opt_stack.pop()
        y = num_stack.pop()
        x = num_stack.pop()
        z = cal(x, y, opt_)
        num_stack.append(z)

    return num_stack[-1]


