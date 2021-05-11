import random
import copy

class LifeGame:
    def __init__(self, row, column):
        # 生成游戏状态表格
        self.GameMap = [[0 for i in range(column)] for j in range(row)]
        # 当前状态的下一个状态表格
        self.NextMap = [[0 for i in range(column)] for j in range(row)]
        # 游戏状态 0-游戏暂停，1-游戏开始
        self.GameStatus = 0
        # 游戏的行列数
        self.Row = row
        self.Column = column
        # 随机初始化状态表
    def random_init(self):
        for i in range(self.Row):
            for j in range(self.Column):
                self.GameMap[i][j] = random.randint(0, 3)%2

    #统计当前位置相邻的细胞数量
    def get_neighbor(self,x,y):
        num = 0
        for i in range(3):
            for j in range(3):
                if i == j and i == 1:
                    continue
                else:
                    num += self.GameMap[(x - 1 + i)%self.Row][(y - 1 + j)%self.Column]
        return num
    #更新单个细胞状态
    def change_status(self,x,y):
        num = self.get_neighbor(x,y)
        if num == 3:
            self.NextMap[x][y] = 1
        elif num!=2:
            self.NextMap[x][y] = 0
        else:
            self.NextMap[x][y] = self.GameMap[x][y]
    #更新游戏状态
    def game_update(self):
        for i in range(self.Row):
            for j in range(self.Column):
                self.change_status(i, j)
        self.GameMap = copy.deepcopy(self.NextMap)
    #重置游戏
    def reset(self):
        for i in range(self.Row):
            for j in range(self.Column):
                self.GameMap[i][j] = 0

    def get_count(self):
        num = 0
        for i in range(self.Row):
            for j in range(self.Column):
                num += self.GameMap[i][j]
        return num

