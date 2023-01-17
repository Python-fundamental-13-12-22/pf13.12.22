class Warrior():
    def __init__(self, level=1, experience=100, rank="Pushover", achievements=[]):
        self.level = level
        self.experience = experience
        self.rank = rank
        self.achievements = achievements

    def battle(self, other_level):
        if (other_level < 1 or other_level > 100):
            return "Invalid level"
        elif self.level == other_level:
            self.experience = self.experience + 10
        elif self.level - other_level == 1:
            self.experience = self.experience + 5
        elif other_level - self.level >= 5:
            return "You've been defeated"
        else:
            diff = other_level - self.level
            self.level = self.level + 20*diff*diff
        rank_list = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"]
        self.level = self.experience // 100
        self.rank = rank_list[self.level // 10]
        if self.level - other_level >= 2:
            return "Easy fight"
        elif self.level - other_level == 1 or self.level == other_level:
            return "A good fight"
        elif self.level < other_level:
            return "An intense fight"

    def training(self, l):
        if self.level >= l[2]:
            self.experience = self.experience + l[1]
            self.achievements.append(l[0])
        else:
            return "Not strong enough"
        if self.level > 100:
            self.level = 100
            self.experience = 10000
        rank_list = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"]
        self.level = self.experience // 100
        self.rank = rank_list[self.level // 10]
        return l[0]


    def printed(self):
        print(f" ({self.level}, {self.rank}, {self.experience})")

