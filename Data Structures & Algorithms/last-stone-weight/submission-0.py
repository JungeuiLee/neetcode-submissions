class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        sorted_stones = sorted(stones)
        
        while len(sorted_stones) > 1:
            # new_weight = 0

            # if len(sorted_stones) <=1:  break

            # x = sorted_stones[-1]
            # y = sorted_stones[-2]

            # if x == y:
            #     sorted_stones.pop(-1)
            #     sorted_stones.pop(-2)
            # elif x > y:
            #     sorted_stones.pop(-1)
            #     sorted_stones.pop(-2)
            #     new_weight = x - y
            #     sorted_stones.append(new_weight)
            # elif x < y:
            #     sorted_stones.pop(-1)
            #     sorted_stones.pop(-2)
            #     new_weight = y - x
            #     sorted_stones.append(new_weight)

            # print(sorted_stones)
            x = sorted_stones.pop()      # 제일 무거운 돌
            y = sorted_stones.pop()      # 두 번째로 무거운 돌

            if x != y:
                sorted_stones.append(x - y)
                sorted_stones.sort()     # 새 돌 넣었으니 다시 정렬

        return sorted_stones[0] if sorted_stones else 0