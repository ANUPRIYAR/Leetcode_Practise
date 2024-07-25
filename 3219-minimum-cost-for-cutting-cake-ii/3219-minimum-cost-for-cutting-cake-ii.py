class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        cuts = [[cost, 'H'] for cost in horizontalCut] + [[cost, 'V'] for cost in verticalCut]
        cuts.sort(reverse=True)

        hcuts, vcuts, total = 1, 1, 0


        for cost, cut_type in cuts:
            if cut_type == 'H':
                total += cost*vcuts
                hcuts += 1
            else:
                total += cost*hcuts
                vcuts += 1

        return total




        