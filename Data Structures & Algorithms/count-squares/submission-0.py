class CountSquares:

    def __init__(self):
        self.points_map = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points_map[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0

        for cur_point, point_count in self.points_map.items():
            px, py = cur_point
            x, y = point

            if (abs(px-x) != abs(py-y)) or (px==x or py==y):
                continue
            
            res += (
                (
                    self.points_map.get((px, y), 0)
                    * self.points_map.get((x, py), 0)
                ) 
                * point_count
            )

        return res
