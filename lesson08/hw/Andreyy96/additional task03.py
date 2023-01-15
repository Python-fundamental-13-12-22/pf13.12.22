class Warrior:

    def __init__(self, level=1, rank='Pushover', experoence=100, achievements=[]):
        self.level = level
        self.rank = rank
        self.experience = experoence
        self.achievements = achievements

    def rank_warrior(self):
        if self.level >= 1 and self.level <= 9 :
            self.rank = 'Pushover'
        elif self.level > 9 and self.level <= 19:
            self.rank = 'Novice'
        elif self.level > 19 and self.level <= 29:
            self.rank = 'Fighter'
        elif self.level > 29 and self.level <= 39:
            self.rank = 'Warrior'
        elif self.level > 39 and self.level <= 49:
            self.rank = 'Veteran'
        elif self.level > 49 and self.level <= 59:
            self.rank = 'Sage'
        elif self.level > 59 and self.level <= 69:
            self.rank = 'Elite'
        elif self.level > 69 and self.level <= 79:
            self.rank = 'Conqueror'
        elif self.level > 79 and self.level <= 89:
            self.rank = 'Champion'
        elif self.level > 89 and self.level <= 99:
            self.rank = 'Master'
        elif self.level > 99 and self.level == 100:
            self.rank = 'Greatest'
        else:
            if self.level < 1:
                self.level = 1
                self.rank = 'Pushover'
                self.experience = 100
                self.achievements = []
            else:
                self.level = 100
                self.rank = 'Greatest'
                self.experience = 10000
                self.achievements = ['Defeated Chuck Norris']

    def battle_rules(self, enemy_level):
        if self.level < 1 or self.level > 100:
            return 'Invalid level'
        elif self.level == enemy_level:
            self.experience += 10
            print('A good fight')
            self.formula_get_level(enemy_level)
            self.rank_warrior()
        elif self.level - enemy_level == 1:
            self.experience += 5
            print('A good fight')
            self.formula_get_level(enemy_level)
            self.rank_warrior()
        elif self.level - enemy_level <= 2 and self.level - enemy_level > 0:
            self.experience += 0
            print('An intense fight')
            self.formula_get_level(enemy_level)
            self.rank_warrior()
        elif self.level - enemy_level >= -2 and self.level - enemy_level > -5:
            self.experience += 0
            print('Easy fight')
            self.formula_get_level(enemy_level)
            self.rank_warrior()
        elif self.level - enemy_level <= -5:
            print("You've been defeated")
            self.formula_get_level(enemy_level)

    def formula_get_level(self, enemy_level):
        diff = enemy_level - self.level
        self.experience += 20 * diff * diff
        self.level = self.experience // 100

    def training(self, trainer):
        if self.level >= trainer[2]:
            self.experience = self.experience + trainer[1]
            self.achievements.append(trainer[0])
            self.level = self.experience // 100
            jet_lee.rank_warrior()
        else:
            return "Not strong enough"


jet_lee = Warrior()
jet_lee.battle_rules(3)
print(f'Опыт битвы с противником 3 уровня: {jet_lee.experience}')
jet_lee.training(["Defeated Chuck Norris", 9000, 1])
print(f'Опыт после тренировки с тренером: {jet_lee.experience}')
print(jet_lee.level)
print(jet_lee.rank)
