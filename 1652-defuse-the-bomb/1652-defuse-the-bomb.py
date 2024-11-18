class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        new_code = [0]*len(code)
        n = len(code)

        for i in range(2*len(code)):
            if k < 0:
                x = -k 
            else:
                x = k
            for j in range(1, x + 1):
                print(j)
                if k > 0:
                    new_code[i] += code[(i + j)%n]
                elif k == 0:
                    new_code[i] = 0
                else:
                    new_code[i] += code[(i - j)%n] 

            if i == len(code) - 1:
                break


        return new_code
        