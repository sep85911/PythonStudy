
import time
import random
import os
import ConfigLoader

# 角色类
class Character:
    def __init__(self, name, hp, speed, attack):
        self.name = name
        self.hp = hp
        self.speed = speed
        self.attack = attack

    def attacking(self, enemy):
        thisattack = random.randint(self.attack-20,self.attack + 20)
        enemy.hp -= thisattack

        if enemy.hp < 0:
            enemy.hp = 0

        print(f'{self.name} 攻击 {enemy.name},造成 {thisattack} 点伤害,{enemy.name}的血量还剩 {enemy.hp}')

# 战斗类    
class Battle:
    def __init__(self):
        # 创建两个角色
        self.c1 = Character('Cloud', 1500, 600, 50)
        self.c2 = Character('Sephiroth', 1000, 100, 175)

        # ATB条,range 0-100
        self.atb1 = 0  
        self.atb2 = 0
        
    def start(self):
        while True:
            # ATB补给,根据速度增加ATB
            self.atb1 += self.c1.speed * 0.1  
            self.atb2 += self.c2.speed * 0.1  

            # 显示ATB和血量
            # print(f'{self.c1.name}的ATB:{int(self.atb1)} 血量:{self.c1.hp}')  
            # print(f'{self.c2.name}的ATB:{int(self.atb2)} 血量:{self.c2.hp}')  

            # 判断是否有人的ATB条满了,满了就攻击
            if self.atb1 >= 100:
                self.atb1 = 0
                self.c1.attacking(self.c2)
            if self.atb2 >= 100:
                self.atb2 = 0 
                self.c2.attacking(self.c1)  

            # 判断是否结束战斗
            if self.c1.hp <= 0: 
                print('战斗结束!克劳德死求了！')
                break
            if self.c2.hp <= 0:
                print('战斗结束!萨菲罗斯死求了！')
                break  

            time.sleep(0.1)  # 暂停0.5秒

if __name__ == '__main__':
    battle = Battle()
    battle.start()
    os.system("pause")
