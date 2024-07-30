class Brawler:
    def __init__(self,name,health,dmg,ammo,reloadSpeed,super,x,y):
        self.health=health
        self.name=name
        self.dmg=dmg
        self.ammo=ammo
        self.reloadSpeed=reloadSpeed
        self.super=super
        self.x=None
        self.y=None
    def move(self,IntendedXPos,IntendedYPos,IsHidden):
        self.x=IntendedXPos
        self.y=IntendedYPos
        self.IsHidden=IsHidden
        print(f'{self.name} moved to {self.x}, {self.y}')
    def reset(self,SpawnX,SpawnY):
        self.x=SpawnX
        self.y=SpawnY
    def DamageTaken(self,IncomingDamage):
        self.health-=IncomingDamage
        if self.health<=0:
            self.died()
    def died(self):
        print(f'{self.name} died\n')
        self.health=100
        self.move(0,0,True)
    def damage(self,IsDead):
        self.IsDead

player1=Brawler('angelo',6000,4000,3,0.5,'acid',0,0)

player1.move(40,-30,False)
player1.DamageTaken(7000)


#reset Pos
#You died
#Deal Damage
#Etc