class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for op in operations:
            print(op)
            if op != "C" and op != "D" and op != "+":
                res.append(int(op))
            elif op == 'C':
                if len(res) > 0:
                    res.pop()
            elif op == 'D':
                res.append(int(res[-1])*2)
            elif op == '+':
                res.append(int(res[-1]) + int(res[-2]))

        res = map(int, res)
        return sum(res)

            
        