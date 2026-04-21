class TimeMap:

    def __init__(self):
        self.time_list = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_list:
            self.time_list[key] = []
        self.time_list[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = self.time_list.get(key, [])
        l, r = 0 , len(res)-1
        cur_val = ""
        while l<=r:
            mid = l + ((r-l)//2)
            mid_ele = res[mid]

            if mid_ele[1] <= timestamp:
                cur_val = mid_ele[0]
                l = mid + 1
            else:
                r = mid - 1
        
        return cur_val
