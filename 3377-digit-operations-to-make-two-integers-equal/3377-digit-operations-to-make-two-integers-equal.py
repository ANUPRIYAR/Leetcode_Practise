from heapq import heappush as hpush , heappop as hpop
class Solution:
    def minOperations(self, n: int, m: int) -> int:
        def is_prime(num):
            if num < 2:
                return False
            if num == 2:
                return True
            if num % 2 == 0:
                return False

            for i in range(3, int(sqrt(num)) + 1, 2):
                if num % i == 0:
                    return False
            return True

        def find_neighbors(cur):
            string = str(cur)
            neighbors = []
            for i in range(len(string)):
                digit = int(string[i])

                if digit != 9:
                    new_digit = digit + 1
                    next = int(string[:i] + str(new_digit) + string[i+1:])
                    if next != 0 and next not in dist and not is_prime(next):
                        neighbors.append(next)

                if digit != 0:
                    new_digit = digit - 1
                    next = int(string[:i] + str(new_digit) + string[i+1 :])
                    if next != 0 and next not in dist and not is_prime(next):
                        neighbors.append(next)

            return neighbors


        if is_prime(n) or is_prime(m):
            return -1

        print(is_prime(2))

        queue = [(n , n)]
        dist = {}

        while queue:
            cost, cur = hpop(queue)
            if cur == m:
                return cost

            if cur in dist and dist[cur] <= cost:
                continue
            dist[cur] = cost
            neighbors = find_neighbors(cur)
            for neighbor in neighbors:
                if not is_prime(neighbor):
                    hpush(queue, (cost + neighbor, neighbor))

        return -1
