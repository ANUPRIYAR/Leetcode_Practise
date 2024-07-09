class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # if len(moves) == 9:
        #     return "Draw"
        player1 = [0]* 8
        player2 = [0]* 8
        for idx, move in enumerate(moves):
            x,y = move
            if idx % 2 == 0:
                player1[x] += 1
                player1[3 + y] += 1 
                if x == y:
                    player1[6] += 1
                if y == (2 - x):
                    player1[7] += 1               
            else:
                player2[x] += 1
                player2[3 + y] += 1 
                if x == y:
                    player2[6] += 1
                if y == (2 - x):
                    player2[7] += 1  

            if 3 in player1:
                return "A"
            if 3 in player2:
                return "B"

        if len(moves) != 9:
            return "Pending"
        else:
            return "Draw"
                


       