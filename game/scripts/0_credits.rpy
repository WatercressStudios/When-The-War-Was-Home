init python:
    credits_duration = 30.0
    credits_height = 3500
    credits_content = [
        ( "Developed for Nanoreno 2020.",
            [
            ]
        ),
        ( "Directing",
            [
                "Tristan 'Wolf' Barber",
            ]
        ),
        ( "Story",
            [
                (
                    "Writing",
                    "Tristan 'Wolf' Barber",
                    "Zodai",
                    "Merritt Barber",
                    "Sagittaeri",
                    "Happiness",
                ),
            ]
        ),
        ( "Editing Directing",
            [
                "TheAlchemyst",
            ]
        ),
        ( "Editing",
            [
                "Tristan 'Wolf' Barber",
            ]
        ),
        ( "Audio",
            [
                (
                    "Music Directing",
                    "Paul Robins",
                ),
                (
                    "Music",
                    "Kierious",
                    "Noah 'Speedy' Aman",
                    "Jae",
                ),
                (
                    "Sound Design",
                    "Paul Robins",
                ),
                (
                    "Sound Editing",
                    "Paul Robins",
                ),
            ]
        ),

        ( "Art",
            [
                (
                    "Sprite",
                    "Kenta",
                ),
                (
                    "Concept Art",
                    "Voiderling",
                ),
                (
                    "BG Art",
                    "Alison 'Draz' Huang",
                ),
                (
                    "UI Design and Art",
                    "TheAlchemyst",
                ),
                (
                    "Logo Design",
                    "TheAlchemyst",
                    "Voiderling",
                ),
            ]
        ),

        ( "Code",
            [
                (
                    "Development Director",
                    "Happiness",
                ),
                (
                    "Tools and UI",
                    "Sagittaeri",
                ),
            ]
        ),

        ( "Ren'py Scripting",
            [
                (
                    "General",
                    "Sagittaeri",
                    "Happiness",
                    "Wei Yuan Lee",
                    "Zodai",
                ),
                (
                    "Audio",
                    "Paul Robins",
                ),
            ]
        ),

        ( "Marketing Directing",
            [
                "TheAlchemyst",
            ]
        ),
        ( "Marketing",
            [
                "Bodo",
            ]
        ),
        ( "Cinematics Directing",
            [
                "TheAlchemyst",
            ]
        ),

        ( "Special thanks to",
            [
                "Ren'py Tom",
                "The Lemmasoft Forum",
                "Our Fans",
            ]
        ),
        ( "A thank you to all of our Patrons, including",
            [
                "Merritt Barber",
                "Jonas Lee",
                "TheAlchemyst",
            ]
        ),
    ]

transform credits_roll(duration, dest):
    on show:
        alpha 0 pos (0, 0)
        parallel:
            linear duration ypos -dest
        parallel:
            linear 1 alpha 1
    on hide:
        linear 1 alpha 0

screen credits():
    if not main_menu:
        timer (credits_duration-2) action Return()
        key "dismiss" action Return()
    else:
        timer (credits_duration-2) action Hide("credits")
        key "dismiss" action Hide("credits")
    frame at credits_roll(credits_duration, credits_height):
        background "#000"
        xsize 2560
        vbox:
            xalign 0.5
            null height 500
            for title, names in credits_content:
                null height 50
                text title:
                    text_align 0.5
                    xalign 0.5
                    size 50
                    color "#7ECBDD"
                for name in names:
                    if type(name) == type(()):
                        hbox:
                            xalign 0.5
                            frame:
                                background None
                                padding (0,0,0,0)
                                margin (0,0,0,0)
                                xsize 900
                                text name[0]:
                                    text_align 1.0
                                    xalign 1.0
                                    size 30
                                    color "#fff"
                            null width 50
                            frame:
                                background None
                                padding (0,0,0,0)
                                margin (0,0,0,0)
                                xsize 900
                                vbox:
                                    for n in name[1:]:
                                        text n:
                                            text_align 0.0
                                            xalign 0.0
                                            size 30
                                            color "#fff"
                    else:
                        text name:
                            text_align 0.5
                            xalign 0.5
                            size 30
                            color "#fff"
            null height 5000
