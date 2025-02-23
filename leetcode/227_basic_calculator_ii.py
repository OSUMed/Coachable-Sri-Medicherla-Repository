class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        curr = 0
        prev = 0
        operation = "+"
        i = 0

        while i < len(s):
            curr = s[i]

            if curr.isdigit():
                # Form curr:
                curr = 0
                while i < len(s) and s[i].isdigit():
                    curr = curr * 10 + int(s[i])
                    i += 1
                i -= 1

                if operation == "+":
                    res += curr
                    prev = curr
                

                elif operation == "-":
                    res -= curr
                    prev = -curr
                

                elif operation == "*":
                    res -= prev
                    curr *= prev
                    res += curr
                    prev = curr
                
                elif operation == "/":
                    res -= prev
                    curr = int(prev/curr)
                    res += curr
                    prev = curr
              
            elif curr != " ":
                operation = curr
            i += 1
            
        return res
                