class Solution:
    def countCollisions(self, directions: str) -> int:
        res = 0
        flag = -1  # 标记碰撞区间，-1代表没有碰撞

        for c in directions:
            if c == 'L':  # 左行车
                if flag >= 0:  # 碰撞区间存在
                    res += flag + 1  # 增加碰撞次数
                    flag = 0  # 碰撞后该车停止
            elif c == 'S':  # 静止车
                if flag > 0:  # 有车正在行驶
                    res += flag  # 增加碰撞次数
                flag = 0  # 静止车停止
            else:  # 右行车
                if flag >= 0:  # 继续增加碰撞区间长度
                    flag += 1
                else:
                    flag = 1  # 启动碰撞区间

        return res
