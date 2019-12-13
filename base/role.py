# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: role.py
    @time: 2019/12/12 11:43
    @desc:
'''
# ********************************************************


class Role_Attribute:

    # 创建一个通用角色模板
    def __init__(self):
        self.STR = 10       # 力量
        self.CON = 10       # 体质
        self.INT = 10       # 智力
        self.SPR = 10       # 精神
        self.SPD = 10       # 速度
        self.LUK = 0        # 幸运
        self.CHA = 0        # 魅力
        self.level = 1      # 等级
        self.levelMax = 10  # 满级
        self.EXP = 0        # 经验
        self.EXPMax = 100   # 当前满级经验值
        self.Monkey = 0     # 金钱



    def RoleLevel(self):
        if self.EXP >= self.EXPMax and self.level < self.levelMax:
            self.EXP = self.EXP - self.EXPMax
            self.EXPMax += self.EXPMax
            self.level += 1

        elif self.EXP >= self.EXPMax and self.level == self.levelMax:
            self.EXP = self.EXPMax

        else:
            pass



    def RoleValue(self):
        # 展示角色属性
        self.HP  = (self.CON//2 + self.SPD//5) * self.level * 100     # 生命值，计算公式为：（体质//2 + 速度//5） * 100
        self.ATK = self.STR  * self.level * 10                        # 物攻值，计算公式为：力量 * 10
        self.DEF = self.CON  * self.level * 10                        # 物防值，计算公式为：体质 * 10
        self.SAT = self.INT  * self.level * 10                        # 特攻值，计算公式为：智力 * 10
        self.SDF = self.SPR  * self.level * 10                        # 特防值，计算公式为：精神 * 10
        self.SPE = self.SPD  * self.level * 10                        # 速度值，计算公式为：速度 * 10

        global playerdict
        playerdict = {"血量" : self.HP ,
                      "物攻" : self.ATK,
                      "物防" : self.DEF,
                      "特攻" : self.SAT,
                      "特防" : self.SDF,
                      "速度" : self.SPE,
                      "等级" : self.level,
                      "当前经验" : self.EXP,
                      "升级所需经验" : self.EXPMax - self.EXP,
                      "金钱" : self.Monkey}

