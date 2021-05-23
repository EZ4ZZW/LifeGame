import pygame
from LifeGame import LifeGame

class LifeGameUI:
    def __init__(self, row, column):
        pygame.init()
        self.screen = pygame.display.set_mode((600,700))
        self.frame = LifeGame(row, column)
        self.position = [[0 for i in range(column)] for j in range(row)]
        self.Count = self.frame.get_count()
        self.CountEvent = pygame.USEREVENT
        self.Event = pygame.USEREVENT + 1
        self.Texts = ["start", "pause", "reset", "random"]
        # 设置事件计时器
        pygame.time.set_timer(self.CountEvent, 500)
        pygame.time.set_timer(self.Event, 500)
        pygame.display.set_caption("LifeGame")
        # 设置背景颜色
        self.screen.fill((200,200,200))

        for i in range(self.frame.Row):
            for j in range(self.frame.Column):
                x = i*600/self.frame.Row
                y = j*600/self.frame.Column
                # 设置细胞在UI中的位置
                self.position[i][j] = (x,y+100)
        # 绘制菜单栏
        # RGB  Point Length Width
        for i in range(4):
            pygame.draw.rect(self.screen, (255,255,255), ((5 + 150*i,5), (140, 50)))    

        self.draw_Count_Text(self)

        for i in range(4):
            self.screen.blit(self.draw_text(self.Texts[i], pygame.Color(255, 255, 255)), (50 + 150*i, 20))

    @staticmethod
    def draw_text(content, color):
        try:
            # 设置为系统默认字体
            pygame.font.init()
            DefaultFont = pygame.font.get_default_font()
            font = pygame.font.Font(DefaultFont, 30)
            text_sf = font.render(content, True, pygame.Color(0, 0, 0), color)
            return text_sf
        except Exception as err:
            print(err)
            return 0

    @staticmethod
    def draw_Count_Text(self):
        self.Count = self.frame.get_count()
        CountStr = str(self.Count)
        self.screen.blit(self.draw_text("Count: " + CountStr + "        ", pygame.Color(200, 200, 200)), (270, 70))

    # 绘制细胞格子
    def show(self):
        for i in range(self.frame.Row):
            for j in range(self.frame.Column):
                if self.frame.GameMap[i][j] == 1:
                    pygame.draw.rect(self.screen, (0, 0, 0), (self.position[i][j], (600//self.frame.Row - 5, 600//self.frame.Column - 5)))
                elif self.frame.GameMap[i][j] == 0:
                    pygame.draw.rect(self.screen, (255, 255, 255), (self.position[i][j], (600//self.frame.Row - 5, 600//self.frame.Column - 5)))
        pygame.display.update()


    def random_init(self):
        self.frame.random_init()
        self.show()

    def start(self):
        self.frame.GameStatus = 1
        return self.frame.GameStatus

    def pause(self):
        self.frame.GameStatus = 0
        return self.frame.GameStatus

    def reset(self):
        self.frame.reset()
        self.show()

    def GameStarting(self):
        pygame.display.flip()
        self.show()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.frame.GameStatus == 0:
                        # 如果按下的是菜单键
                        if event.pos[1] <= 55:
                            whichButton = event.pos[0] // 150
                            if whichButton == 0:
                                self.start()
                            elif whichButton == 2:
                                self.reset()
                            elif whichButton == 3:
                                self.random_init()
                            continue
                        
                        # 按下的为细胞
                        for i in range(len(self.position)):
                            for j in range(len(self.position[i])):
                                point = self.position[i][j]
                                if point[0] <= event.pos[0] <= (point[0] + 600//self.frame.Row - 5) and point[1] <= event.pos[1] <= (point[1] + 600//self.frame.Column - 5):
                                    self.frame.GameMap[i][j] = 1^self.frame.GameMap[i][j]
                                    self.show()
                                    break
                    else:
                        if event.pos[1] <= 55:
                            whichButton = event.pos[0] // 150
                            if whichButton == 1:
                                self.pause()

                elif event.type == self.Event:
                    if self.frame.GameStatus == 1:
                        self.frame.game_update()
                        self.show()
                elif event.type == self.CountEvent:
                    self.draw_Count_Text(self)
                    self.show()

if __name__ == '__main__':
    lifegame = LifeGameUI(30, 30)
    lifegame.random_init()
    lifegame.GameStarting()