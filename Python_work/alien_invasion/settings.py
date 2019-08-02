class Settings():
    '''存储外星人入侵所有设置的类'''

    def __init__(self):
        '''初始化游戏的设置'''

        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #设置飞船的速度
        self.ship_speed_factor = 2.5

        # 子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 10
        self.bullet_height = 30
        self.bullet_color = 230,0,0
        self.bullets_allowed = 3

