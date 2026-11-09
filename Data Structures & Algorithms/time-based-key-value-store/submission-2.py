class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store or not self.store[key]:
            return ""
        
        left = 0
        right = len(self.store[key]) - 1
        res = ""

        while left <= right:
            middle = (left+right) // 2

            # 만약 원하는 시간 타겟이 왼쪽에 있을 경우의 수
            if self.store[key][middle][1] <= timestamp:
                res = self.store[key][middle][0]
                left = middle + 1
            
            # 반대의 경우 (원하는 시간 타겟이 오른쪽에 있을 경우의 수)
            else:
                right = middle -1
        
        return res