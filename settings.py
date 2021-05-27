class Settings():
    """存储所有游戏设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width = 1200       #定义宽
        self.screen_height = 600       #定义高
        self.bg_color = (245,245,245)  #定义背景色
        self.ship_speed_factor = 1.5   #定义移动速度
        #子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
