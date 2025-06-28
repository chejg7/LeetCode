class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # for i in range(len(gas)):
        #     tank = 0
        #     for j in range(len(gas)):
        #         cur = i + j if i + j < len(gas) else i + j - len(gas)
        #         tank += gas[cur]
        #         tank -= cost[cur]
        #         if tank < 0:
        #             break

        #     if tank >= 0:
        #         return i
        
        # return -1

        total_tank = 0
        curr_tank = 0
        start_index = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total_tank += diff
            curr_tank += diff

            # 현재까지 도중에 연료 부족 → 다음 지점부터 다시 시작
            if curr_tank < 0:
                curr_tank = 0
                start_index = i + 1

        return start_index if total_tank >= 0 else -1