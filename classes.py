#--------------------------------------------------------------CLASSES---------------------------------------------------------------------------
class Character:
    def __init__(self, race=None, gender=None, name=None, class_name=None, sub_class=None, background=None, personality_traits=None, alignment=None, languages=None, stats=None, level=None):
        self.race = race
        self.gender = gender
        self.name = name
        self.class_name = class_name
        self.sub_class = sub_class
        self.background = background
        self.personality_traits = personality_traits
        self.alignment = alignment
        self.languages = languages
        self.stats = stats
        self.level = level
    
    def __repr__(self):
        returnable = ""
        return returnable.format()

    def add_race():
        pass
    def add_gender():
        pass
    def add_name():
        pass
    def add_class():
        pass
    def add_sub_class():
        pass
    def add_background():
        pass
    def add_alignment():
        pass
    def add_languages():
        pass
    def set_stat(self, stat_type, stat_value):
        if stat_type in "StrDexConWisIntCha":
            