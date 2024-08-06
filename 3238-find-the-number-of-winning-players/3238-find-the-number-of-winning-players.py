class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        hashmap = {}
        for player, color in pick:
            hashmap[(player, color)] = hashmap.get((player, color), 0) + 1

        winning_players = set()
        for key, value in hashmap.items():
            player, color = key[0], key[1]
            if value > player:
                winning_players.add(player)

        return len(winning_players)



    
        