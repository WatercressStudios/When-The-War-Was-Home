# The script of the game goes in this file.

# callback=speaker is needed for mouth flaps
define mc = Character("Imani",  what_color="#fff")
define m = Character("Miranda", callback=speaker("m"), who_color="#fff", what_color="#fff")
define ai = Character("Ai", callback=speaker("ai"))
define son = Character("Aarul", callback=speaker("son"), who_color="#fff")
define fly = Character("Jason", callback=speaker("fly"), who_color="#fff")
define p1 = Character("Patient", callback=speaker("p1"), who_color="#fff")
define ric = Character("Richter", callback=speaker("ric"), who_color="#fff")
define RTO = Character("Radio Telephone Operator", who_color="#fff")
define pat = Character("Bar Patron", who_color="#fff")
define bar = Character("Barmaid", callback=speaker("bar"), who_color="fff")
define G1 = Character("Player 1", who_color="#fff")
define G2 = Character("Player 2", who_color="#fff")
define G3 = Character("Player 3", who_color="#fff")
define G4 = Character("Player 4", who_color="#fff")
define GF3 = Character("Player 5", who_color="#fff")
define bui = Character("Winston", callback=speaker("bui"), who_color="#fff")
define fri = Character("Charlotte", callback=speaker("fri"), who_color="#fff")
define Girl = Character("Little Girl", who_color="#fff", what_color="fff")


#transitions
define circlewipe = ImageDissolve("imagedissolve_circlewipe.png", 1.0, 8)



## The script of the game goes in this file.

# son: Aarul [The MC's Adopted Son, Bangladeshi male name for "brilliant"]
# bar: Bartender [Female pronouns]
# pat: Patron [Bar Patron]
# fly: Jason [The Flybot getting the body swap, male pronouns] (TO BE CHANGED)
# ai: Ai [Main Case Patient, female pronouns, Chinese name for "lovely"]
# rto: Radio Telephone Operator [Specific to Case E Scene 2]

label start:
    $ renpy.music.play(config.main_menu_music)
    jump intro
