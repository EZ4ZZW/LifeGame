import unittest
from LifeGameUI import LifeGameUI
from LifeGame import LifeGame

class GameTest(unittest.TestCase):

    # 开始测试标志
    def setUp(self):
        print("start test")

    # 测试游戏开始
    def test_start(self):
        lifeGameUI = LifeGameUI(10, 10)
        self.assertEqual(lifeGameUI.start(), 1, "error")

    # 测试游戏暂停
    def test_pause(self):
        lifeGameUI = LifeGameUI(10, 10)
        self.assertEqual(lifeGameUI.pause(), 0, "error")

    # 测试LifeGameUI界面重置
    def test_reset_LifeGameUI(self):
        lifeGameUI = LifeGameUI(10, 10)
        for i in range(10):
            for j in range(10):
                lifeGameUI.frame.GameMap[i][j] = 1
        lifeGameUI.reset()
        for i in range(10):
            for j in range(10):
                self.assertEqual(lifeGameUI.frame.GameMap[i][j], 0, "error")

    # 测试获取单个细胞周围存活细胞数
    def test_get_neighbor(self):
        lifeGame = LifeGame(100, 100)
        lifeGame.GameMap[0][0] = 1
        lifeGame.GameMap[0][1] = 1
        lifeGame.GameMap[0][2] = 1
        lifeGame.GameMap[1][0] = 1
        lifeGame.GameMap[1][1] = 1
        lifeGame.GameMap[1][2] = 1
        lifeGame.GameMap[2][0] = 1
        lifeGame.GameMap[2][1] = 1
        lifeGame.GameMap[2][2] = 1
        # 本格子以及周围格子设置为1
        self.assertEqual(lifeGame.get_neighbor(1, 1), 8, "error")
        # 检测周围或者数量是否为8

        lifeGame.GameMap[0][0] = 0
        self.assertEqual(lifeGame.get_neighbor(1, 1), 7, "error")
        # 逐渐递减
        lifeGame.GameMap[0][1] = 0
        self.assertEqual(lifeGame.get_neighbor(1, 1), 6, "error")
        lifeGame.GameMap[0][2] = 0
        self.assertEqual(lifeGame.get_neighbor(1, 1), 5, "error")
        lifeGame.GameMap[1][0] = 0
        self.assertEqual(lifeGame.get_neighbor(1, 1), 4, "error")
        lifeGame.GameMap[1][1] = 0
        self.assertEqual(lifeGame.get_neighbor(1, 1), 4, "error")  # 本格子设置为0.没有影响
        lifeGame.GameMap[1][2] = 0
        self.assertEqual(lifeGame.get_neighbor(1, 1), 3, "error")
        lifeGame.GameMap[2][0] = 0
        self.assertEqual(lifeGame.get_neighbor(1, 1), 2, "error")
        lifeGame.GameMap[2][1] = 0
        self.assertEqual(lifeGame.get_neighbor(1, 1), 1, "error")
        lifeGame.GameMap[2][2] = 0
        self.assertEqual(lifeGame.get_neighbor(1, 1), 0, "error")

    # 测试改变单个细胞状态
    def test_change_status(self):
        lifeGame = LifeGame(100, 100)
        lifeGame.GameMap[0][0] = 1
        lifeGame.GameMap[0][1] = 1
        lifeGame.GameMap[0][2] = 1
        lifeGame.GameMap[1][0] = 1
        lifeGame.GameMap[1][2] = 1
        lifeGame.GameMap[2][0] = 1
        lifeGame.GameMap[2][1] = 1
        lifeGame.GameMap[2][2] = 1
        lifeGame.change_status(1, 1)
        self.assertEqual(lifeGame.NextMap[1][1], 0, "error")  # 死亡

        lifeGame.GameMap[0][0] = 1
        lifeGame.GameMap[0][1] = 1
        lifeGame.GameMap[0][2] = 0
        lifeGame.GameMap[1][0] = 1
        lifeGame.GameMap[1][2] = 0
        lifeGame.GameMap[2][0] = 0
        lifeGame.GameMap[2][1] = 0
        lifeGame.GameMap[2][2] = 0
        lifeGame.change_status(1, 1)
        self.assertEqual(lifeGame.NextMap[1][1], 1, "error")  # 一定活

        lifeGame.GameMap[0][0] = 1
        lifeGame.GameMap[0][1] = 0
        lifeGame.GameMap[0][2] = 0
        lifeGame.GameMap[1][0] = 1
        lifeGame.GameMap[1][2] = 0
        lifeGame.GameMap[2][0] = 0
        lifeGame.GameMap[2][1] = 0
        lifeGame.GameMap[2][2] = 0
        lifeGame.GameMap[1][1] = 1
        lifeGame.change_status(1, 1)
        self.assertEqual(lifeGame.NextMap[1][1], 1, "error")  # 不变

        lifeGame.GameMap[0][0] = 1
        lifeGame.GameMap[0][1] = 0
        lifeGame.GameMap[0][2] = 0
        lifeGame.GameMap[1][0] = 1
        lifeGame.GameMap[1][2] = 0
        lifeGame.GameMap[2][0] = 0
        lifeGame.GameMap[2][1] = 0
        lifeGame.GameMap[2][2] = 0
        lifeGame.GameMap[1][1] = 0
        lifeGame.change_status(1, 1)
        self.assertEqual(lifeGame.NextMap[1][1], 0, "error")  # 不变

        # 边界测试
        lifeGame.GameMap[99][99] = 1
        lifeGame.GameMap[0][99] = 0
        lifeGame.GameMap[1][99] = 0
        lifeGame.GameMap[99][0] = 1
        lifeGame.GameMap[1][0] = 0
        lifeGame.GameMap[99][1] = 0
        lifeGame.GameMap[0][1] = 1
        lifeGame.GameMap[1][1] = 0
        lifeGame.change_status(0, 0)
        self.assertEqual(lifeGame.NextMap[0][0], 1, "error")  # 不变l
    # 测试全部细胞状态更新
    def test_next_phrase(self):
        lifeGame = LifeGame(100, 100)
        lifeGame.GameMap[0][0] = 1
        lifeGame.GameMap[0][1] = 1
        lifeGame.GameMap[0][2] = 1
        lifeGame.GameMap[1][0] = 1
        lifeGame.GameMap[1][2] = 1
        lifeGame.GameMap[2][0] = 1
        lifeGame.GameMap[2][1] = 1
        lifeGame.GameMap[2][2] = 1
        lifeGame.game_update()
        self.assertEqual(lifeGame.GameMap[0][0], 1, "error")
        self.assertEqual(lifeGame.GameMap[1][1], 0, "error")
        self.assertEqual(lifeGame.GameMap[99][1], 1, "error")
        lifeGame.GameMap[97][97] = 1
        lifeGame.GameMap[97][98] = 1
        lifeGame.GameMap[97][99] = 1
        lifeGame.GameMap[98][97] = 0
        lifeGame.GameMap[98][98] = 1
        lifeGame.GameMap[98][99] = 0
        lifeGame.GameMap[99][97] = 0
        lifeGame.GameMap[99][98] = 1
        lifeGame.game_update()
        self.assertEqual(lifeGame.GameMap[98][98], 0, "error")

    # 将所有单元格置为1l检测清空函数是否正常进行。如果正常运行，则应该数组全为0
    def test_reset(self):
        lifeGame = LifeGame(100, 100)
        for i in range(100):
            for j in range(100):
                lifeGame.GameMap[0][0] = 1
        lifeGame.reset()
        for i in range(100):
            for j in range(100):
                self.assertEqual(lifeGame.GameMap[i][j], 0, "error")

    def tearDown(self):
        print("tear down")


if __name__ == '__main__':
    suite = unittest.TestSuite()

    suite.addTest(GameTest("test_start"))  # 测试游戏开始
    suite.addTest(GameTest("test_pause"))  # 测试游戏暂停
    suite.addTest(GameTest("test_get_neighbor"))  # 测试 获取该方格周边存活数量
    suite.addTest(GameTest("test_change_status"))  # 测试 改变该方格存活状态
    suite.addTest(GameTest("test_next_phrase"))  # 测试 改变全部方格状态
    suite.addTest(GameTest("test_reset"))  # 测试 重置内部数组
    suite.addTest(GameTest("test_reset_LifeGameUI"))  # 测试 重置棋盘

    runner = unittest.TextTestRunner()   
    runner.run(suite)