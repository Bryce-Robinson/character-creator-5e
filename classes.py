#--------------------------------------------------------------CLASSES---------------------------------------------------------------------------
class Character:
    def __init__(self, race=None, gender=None, name=None, class_name=None, sub_class=None, background=None, personality_traits=None, alignment=None, languages=None, stat_dict={"Str":0, "Dex":0, "Con":0, "Wis":0, "Int":0, "Cha":0}, level=None):
        self.race = race
        self.gender = gender
        self.name = name
        self.class_name = class_name
        self.sub_class = sub_class
        self.background = background
        self.personality_traits = personality_traits
        self.alignment = alignment
        self.languages = languages
        self.stat_dict = stat_dict
        self.level = level
    
    def __repr__(self):
        returnable = ""
        return returnable.format()

    
    def add_race(self, race):
        self.race = race
    
    def add_gender(self, gender):
        if gender is "M" or "m":
            gender = "Male"
        elif gender is "F" or "f":
            gender = "Female"
        self.gender = gender
    
    def add_name(self, first_name, last_name=None):
        name = "{} {}"
        self.name = name.format(first_name, last_name)
    
    def add_class(self, class_name):
        pass
    
    def add_sub_class(self, class_name):
        pass
    
    def add_background(self, background):
        self.background = background
        
    def add_alignment(self, word1, word2):
        if word1 is "Lawful" or "Neutral" or "Chaotic":
            if word2 is "Good" or "Neutral" or "Evil":
                self.alignment= word1+" "+word2 
    
    def add_languages(self, languages_list):
        for language in languages_list:
            self.languages.append(language)
    
    def set_stat(self, stat_type, stat_value):
        if stat_type is ("Str" or "Dex" or "Con" or "Wis" or "Int" or "Cha"):
            if (stat_value > 0) and (stat_value <= 18):
                self.stat_dict.update(stat_type= stat_value)

        else: print("Error, invalid stat type detected.")
