class Solution:

    # @param s, a string
    # @return an integer

    def longestValidParentheses(self, s):
        
        # 返回括号串中合法括号串的长度。使用栈。这个解法比较巧妙，开辟一个栈，压栈的不是括号，而是未匹配左括号的索引！

        maxlen = 0
        stack = []
        last = -1

        for i in range(len(s)):

            if s[i]=='(':
                stack.append(i)     # push the INDEX into the stack!!!!

            else:
                if stack == []:
                    last = i

                else:
                    stack.pop()
                    if stack == []:
                        maxlen = max(maxlen, i-last)

                    else:
                        maxlen = max(maxlen, i-stack[len(stack)-1])

        return maxlen
