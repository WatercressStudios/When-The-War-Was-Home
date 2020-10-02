
screen tobecontinued:
    button:
        background "#000"
        xysize (1.0, 1.0)
        padding (0, 0)
        margin (0, 0)
        text "To be continued...":
            size 100
            align (0.5, 0.5)
        action Return()

label main2:
    scene bg_sky day with dissolve

    "Looking back to my tablet, I remind myself of the case I'm on for the day."

    "Thankfully, like most of my cases, this is a boring one."

    "I like boring. Boring is good. Boring means no one is dying."

    "Looks like I'm replacing a new patient's primary care physician. Their file shows... alcoholism."

    "Simple as simple gets. And common, too."

    "All too common."

    scene bg introhouse with dissolve

    "Preparing myself for a routine visit, I knock on the door lightly."

    show ai with dissolve:
        xalign 0.5
    "The door opens a few seconds later, the occupant clearly having been waiting for me. This sort of readiness is to be expected from most veterans."

    "..."

    "But this one is familiar."

    
    jump choice
