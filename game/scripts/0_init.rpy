# The script of the game goes in this file.

# callback=speaker is needed for mouth flaps
define mc = Character("Imani",  what_color="#f4d6a7")
define m = Character("Miranda", callback=speaker("m"),  what_color="#A4FBFE")
define ai = Character("Ai", callback=speaker("ai"))
define son = Character("Aarul", callback=speaker("son"), who_color="#FFA500")
define fly = Character("Jason", callback=speaker("fly"), who_color="#FF8000")
define p1 = Character("Patient", callback=speaker("p1"), who_color="#0000FF")
define ric = Character("Richter", callback=speaker("ric"), who_color="#FF0000")
define RTO = Character("Radio Telephone Operator", who_color="#ffffff")
define pat = Character("Bar Patron", who_color="#FFFF00")
define bar = Character("Barmaid", callback=speaker("bar"), who_color="80FF00")
define G1 = Character("Player 1", who_color="#ffffff")
define G2 = Character("Player 2", who_color="#ffffff")
define G3 = Character("Player 3", who_color="#ffffff")
define G4 = Character("Player 4", who_color="#ffffff")
define GF3 = Character("Player 5", who_color="#ffffff")
define bui = Character("Winston", callback=speaker("bui"), who_color="#FFC0CB")
define fri = Character("Charlotte", callback=speaker("fri"), who_color="#D2691E")
define Girl = Character("Little Girl", who_color="#6082b6", what_color="FADFAE")



## The script of the game goes in this file.

# son: Aarul [The MC's Adopted Son, Bangladeshi male name for "brilliant"]
# bar: Bartender [Female pronouns]
# pat: Patron [Bar Patron]
# fly: Jason [The Flybot getting the body swap, male pronouns] (TO BE CHANGED)
# ai: Ai [Main Case Patient, female pronouns, Chinese name for "lovely"]
# rto: Radio Telephone Operator [Specific to Case E Scene 2]

label start:
    scene bg clinic
    show ai neutral:
        xalign 0.5
    "TEST BEGIN"
    ai "Test speech but very long?"

    hide ai
    show bar neutral:
        xalign 0.5
    bar "Test speech but very long?"
    "TEST END"
    jump intro
