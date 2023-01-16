class Warrior:

    def __init__(self, level=1, rank='Pushover', experoence=100, achievements=[]):
        self.level = level
        self.rank = rank
        self.experience = experoence
        self.achievements = achievements

    def rank_warrior(self):
        if 1 <= self.level <= 9:
            self.rank = 'Pushover'
        elif 9 < self.level <= 19:
            self.rank = 'Novice'
        elif 19 < self.level <= 29:
            self.rank = 'Fighter'
        elif 29 < self.level <= 39:
            self.rank = 'Warrior'
        elif 39 < self.level <= 49:
            self.rank = 'Veteran'
        elif 49 < self.level <= 59:
            self.rank = 'Sage'
        elif 59 < self.level <= 69:
            self.rank = 'Elite'
        elif 69 < self.level <= 79:
            self.rank = 'Conqueror'
        elif 79 < self.level <= 89:
            self.rank = 'Champion'
        elif 89 < self.level <= 99:
            self.rank = 'Master'
        elif 99 < self.level == 100:
            self.rank = 'Greatest'
        else:
            if self.level < 1:
                self.level = 1
                self.rank = 'Pushover'
                self.experience = 100
            else:
                self.level = 100
                self.rank = 'Greatest'
                self.experience = 10000

    def battle_rules(self, enemy_level):
        message = ''
        if self.level < 1 or self.level > 100:
            return 'Invalid level'
        elif self.level == enemy_level:
            self.experience += 10
        elif self.level - enemy_level == 1:
            self.experience += 5
        elif self.level - enemy_level == 2:
            self.experience += 0
        elif enemy_level - self.level == 6:
            self.formula_get_level(enemy_level)
        elif 1 <= enemy_level - self.level < 5:
            self.formula_get_level(enemy_level)
        elif self.level - enemy_level <= -5:
            print("You've been defeated")
        self.rank_warrior()

        if self.level - enemy_level >= 2:
            message = "Easy fight"
        elif self.level - enemy_level == 1 or self.level == enemy_level:
            message = "A good fight"
        elif self.level < enemy_level:
            message = "An intense fight"

        return message

    def formula_get_level(self, enemy_level):
        diff = enemy_level - self.level
        self.experience += 20 * diff * diff
        self.level = self.experience // 100

    def training(self, trainer):
        if self.level >= trainer[2]:
            self.experience = self.experience + trainer[1]
            self.achievements.append(trainer[0])
            self.level = self.experience // 100
            self.rank_warrior()
        else:
            return "Not strong enough"
        return trainer[0]

jet_li = Warrior()

print(jet_li.training(["Defeated Chuck Norris", 9000, 1]))
print(jet_li.experience)
print(jet_li.level)
print(jet_li.rank)
print(jet_li.battle_rules(90))
print(jet_li.experience)
print(jet_li.achievements)
