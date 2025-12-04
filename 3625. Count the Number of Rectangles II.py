class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        groups = defaultdict(list)  # 斜率 -> [截距]
        groups2 = defaultdict(list)  # 中点 -> [斜率]

        # Step 1: 计算所有两点之间的斜率和截距
        for i, (x, y) in enumerate(points):
            for x2, y2 in points[:i]:
                dy = y - y2
                dx = x - x2
                k = dy / dx if dx else inf  # 计算斜率，避免除零错误
                b = (y * dx - x * dy) / dx if dx else x  # 计算截距
                groups[k].append(b)  # 将截距加入到对应斜率的组
                groups2[(x + x2, y + y2)].append(k)  # 将斜率加入到对应中点的组

        ans = 0
        # Step 2: 计算具有相同斜率的线段组成的梯形数量
        for g in groups.values():
            if len(g) == 1:
                continue
            s = 0
            for c in Counter(g).values():  # 计算每个截距出现的次数
                ans += s * c  # 通过组合公式计算梯形数量
                s += c  # 更新累计的数量

        # Step 3: 计算去除平行四边形的重复计算
        for g in groups2.values():
            if len(g) == 1:
                continue
            s = 0
            for c in Counter(g).values():
                ans -= s * c  # 去除重复计算的平行四边形
                s += c  # 更新累计的数量

        return ans
