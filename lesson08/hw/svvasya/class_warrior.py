class Warrior():
    def __init__(self, level=1, experience=100, rank="Pushover", achievements=[]):
        self._level = level
        self._experience = experience
        self._rank = rank
        self._achievements = achievements

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        self._level = level

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, experience):
        self._experience = experience

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, rank):
        self._rank = rank

    @property
    def achievements(self):
        return self._achievements

    @achievements.setter
    def achievements(self, achievements):
        self._achievements = achievements

    def battle(self, other_player_level):
        rank_list = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion",
                     "Master", "Greatest"]
        result = None
        diff = self.level - other_player_level
        if other_player_level < 1 or other_player_level > 100:
            return 'Invalid level'

        elif self.level == other_player_level:
            self.experience += 10
        elif self.level - other_player_level == 1:
            self.experience += 5
        elif abs(self.level - other_player_level) == 2:
            self.experience += 0
        elif other_player_level - self.level >= 1 and other_player_level - self.level < 5:
            self.experience += 20 * diff * diff
        elif other_player_level - self.level >= 5: #and rank_list.index(self.rank)<rank_list.index():
            return f'''You've been defeated'''
        if diff >= 2:
            result = "Easy fight"
        elif diff == 0 or diff == 1:
            result = "A good fight"
        elif diff < 0:
            result = "An intense fight"
        self.experience<=1000
        experience_r = self.experience // 100
        self.level = experience_r
        if self.level >= 100:
            self.level = 100
            self.experience = 10000

        rank_r = self.level // 10
        self.rank = rank_list[rank_r]
        return result
    def training(self, training_list):
        if self._level >= training_list[2]:
            self.experience += training_list[1]
            self.level += training_list[2]
            desc_training = f'''{training_list[0]}'''
        else:
            desc_training = "Not strong enough"
        experience_r = self.experience // 100
        self.level = experience_r
        if self.level >= 100:
            self.level = 100
            self.experience = 10000
        self.achievements.append(desc_training)
        rank_r = self.level // 10
        rank_list = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion",
                     "Master", "Greatest"]
        self.rank = rank_list[rank_r]
        return desc_training


bruce_lee = Warrior()
print(bruce_lee.training(["Defeated Chuck Norris", 9000, 1]))
print(bruce_lee.battle(90))    # => "A good fight"
print(bruce_lee.level)
