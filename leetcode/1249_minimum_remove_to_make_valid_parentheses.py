class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_parens = []
        parens = list(s)

        for index, char in enumerate(parens):
            
            if char == "(":
                open_parens.append(index)
            
            elif char == ")" and open_parens:
                open_parens.pop()

            elif char == ")" and not open_parens:
                parens[index] = ""

        for i in open_parens:
            parens[i] = ""

        return "".join(parens)
        
        
