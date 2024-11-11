class Solution:
    def evalRPN(self, tokens):
        stack = []
        for i in tokens:
            if i not in "+-*/":
                stack.append(int(i))
            else:
                b = stack.pop()
                a = stack.pop()
                if i == '+':
                    stack.append(a + b)
                elif i == '-':
                    stack.append(a - b)
                elif i == '*':
                    stack.append(a * b)
                elif i == '/':
                    stack.append(int(int(a) / float(b)))  # 确保整数除法
                """
                python 的整数除法是向下取整，而不是向零取整。
                python2 的除法 "/" 是整数除法， "-3 / 2 = -2" ；
                python3 的地板除 "//" 是整数除法， "-3 // 2 = -2" ；
                python3 的除法 "/" 是浮点除法， "-3 / 2 = -1.5" ；
                而 C++/Java 中的整数除法是向零取整。

                """
        return stack[0]

# 测试代码
sol = Solution()
print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))  # 输出: 22