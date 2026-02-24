class GreekGod():
    def __init__(self, name, power, weapon):
        self.name = name
        self.power = power
        self.weapon = weapon

    def power_line(self):
        print(f"Feel the wrath of {self.power}")

    def name_callout(self):
        print(f"Hello my name is {self.name}")

class GreekChild(GreekGod):
    def __init__(self, name, power, weapon, lineage, children):
        super().__init__(name, power, weapon)
        self.GodlyParent = lineage
        self.childrenAmount = children

    def introduction(self):
        print(f"Greetings my name is {self.name}, a descendant of {self.GodlyParent}")



x = GreekChild("Odysseus", "Wit", "Hands", "Hermes", 9)
x.introduction()
