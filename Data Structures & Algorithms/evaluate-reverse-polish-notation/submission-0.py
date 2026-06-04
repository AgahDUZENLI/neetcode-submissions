class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []

        for i in tokens:
            if(i != '+' and i != '-' and i != '*'and i != '/'):
                nums.append(int(i))
            else:
                b = nums.pop()
                a = nums.pop()

                if i == '+' :
                    nums.append(a+b)
                elif i == '-' :
                    nums.append(a-b)
                elif i == '*' :
                    nums.append(a*b)
                elif i == '/':
                    nums.append(int(a/b))              
        return nums[0]
        
        