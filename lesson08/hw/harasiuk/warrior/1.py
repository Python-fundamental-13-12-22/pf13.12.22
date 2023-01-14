class Warrior():
    def __init__(self, level=1, experience=100, rank="Pushover", achivments=[]):
        self.level = level
        self.experience = experience
        self.rank = rank
        self.achivments = achivments

    def  battle(self, other):
        if (other.level < 1 and other.level > 100):
            print("Invalid level")
        elif self.level == other.level:
            self.experience = self.experience + 10
        elif self.level - other.level == 1:
            self.experience = self.experience + 5
        elif self.level - other.level == 2:
            pass
        elif other.level - self.level >= 5:
            print("You've been defeated")
        else:
            diff = other.level - self.level
            self.level = self.level + 20*diff*diff
        rank_list = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion",
                     "Master", "Greatest"]
        self.rank = rank_list[level // 10]
        self.level = self.experience // 100

    def training(self, l):
        if self.level >= l[2]:
            self.experience = self.experience + l[1]
            self.achivments.append(l[0])
        else:
            print("Not strong enough")
        if self.level > 100:
            self.level = 100
            self.experience = 10000
        rank_list = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"]
        self.rank = rank_list[self.level // 10]
        self.level = self.experience // 100

    def printed(self):
        print(f" ({self.level}, {self.rank}, {self.experience})")

tom = Warrior()
bruce_lee = Warrior()
bruce_lee.training(["Defeated Chuck Norris", 9000, 1])
bruce_lee.printed()