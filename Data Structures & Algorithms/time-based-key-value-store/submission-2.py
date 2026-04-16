class TimeMap:

    def __init__(self):
        self.current = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.current:
            self.current[key][-1][1] = timestamp - 1
            self.current[key].append([timestamp, math.inf, value])
        else:
            self.current[key] = [[timestamp, math.inf, value]]
            # left, right, value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.current:
            return ""
        m = len(self.current[key]) - 1
        lo = 0
        hi = m

        # print(self.current)

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            # print(timestamp, mid, m, self.current[key][mid])

            if mid == 0 and timestamp < self.current[key][mid][0]:
                return ""
            elif self.current[key][mid][0] <= timestamp and timestamp <= self.current[key][mid][1]:
                return self.current[key][mid][2]
            elif timestamp > self.current[key][mid][1]:
                lo = mid + 1
            else:
                hi = mid - 1

        return ""