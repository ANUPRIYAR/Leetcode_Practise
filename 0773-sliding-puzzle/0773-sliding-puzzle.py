class Solution:
    def slidingPuzzle(self, grid: List[List[int]]) -> int:
        target = "123450"
        # Graph
        neighbours = {
            0:[1,3], 1:[0, 2, 4], 2:[1,5],
            3:[0, 4], 4:[1,3,5], 5:[2,4]
        }

        start = ''.join([str(num) for row in grid for num in row])
        visited = set()
        visited.add(start)

        queue = deque([(start, 0)])

        while queue:
            state, moves = queue.popleft()

            if state == target:
                return moves

            zero_index = state.index('0')

            for neigh in neighbours[zero_index]:
                new_state = list(state)
                new_state[zero_index], new_state[neigh] = new_state[neigh], new_state[zero_index]

                new_state_str = ''.join(new_state)
                
                if new_state_str not in visited:
                    visited.add(new_state_str)
                    queue.append((new_state_str, moves + 1))

        return -1 



        