# BG clinic
# sfx of phone ringing
# sfx phone being picked up
#music carries on from main menu
label intro:
    scene bg clinic with dissolve:
        zoom 2.0 align (0.0, 0.5)
        ease 3.5 zoom 1.3
    play sound "sfx/phone ring.ogg"
    pause 3.5
    play sound "sfx/pick up.ogg"
    mc "Imani speaking."

    p1 "Good afternoon. Is this a clinic?"

    show bg clinic:
        linear 60.0 align (1.0, 0.5)

    mc "Yes. I'm Doctor Ward, the owner. Are you calling to make an appointment?"

    p1 "Indeed. I hear you do house calls?"

    mc "I certainly do. Email us your details and I'll schedule it today. Do you need our email address?"

    p1 "No, I have it. Bless you."

    # sfx of phone hanging up
    play sound "sfx/hang up.ogg"
    "Well, there goes my relaxing summer afternoon."

    "It's been a little quiet this weekend, which is a good thing. It means no one needed medical help."

    show bg clinic:
        ease 1.0 align (0.8, 0.5)
    pause 1.0
    show son neutral with dissolve:
        xalign 0.5

    "Aarul, my son, could probably spend his summer days doing summer-y things with teenagers his age, too."

    # sfx of a new notification
    play sound "sfx/notification.ogg"
    son "I see the patient's email, Imi. I'm entering his details into the new app now."

    show son happy
    son "Do you need me to show you how to use it again?"

    mc "No need, no need, I got this. Sheesh, how different can it be from the previous app?"

    # Sprite & VA: laughs
    son "Well you've got this {i}young man{/i} here to help you if you run into trouble."

    "This little brat. I shouldn't have let him change the booking system."

    "Alright, let's pencil in the appointment into one of my available days on the app."

    "Aarul's gone ahead and marked the days I'm available."

    "Just gotta {b}pick a patient file{/b}, and then {b}pick a day{/b} on the calendar. How hard can it be?"

    stop music fadeout 2.0

    # highlight the CALENDAR button
    jump choice

label intro2:
    # after the player schedules in a day, show the clinic again.

    show son happy2
    son "Hey, I see you've scheduled it correctly. Nice job, Imi!"

    mc "Savor this while you can, Aarul. It won't be long till I'm better at this app than you, too."

    show son surprised with hpunch
    son "It's not my fault the last app was a disaster!"

    show son sigh
    son "Oh, forget it."

    show son happy
    son "From now on, I'll add any new house call requests through this app. So keep an eye on it, okay?"

    mc "Got it."

    hide son with dissolve
    "Looking up the address, it looks like the patient's home is just a few blocks away."

    "Perfect distance for a summer day."

    show bg clinic:
        ease 3.0 zoom 2.0 xalign 0.72
    "I grab my tools bag and walk out the front door."

# BG black snow sky
# SFX of a cold breeze
    play env "sfx/wind.ogg" fadein 1.0
    scene bg_sky night darksnow

    "Brrr. Looks like it's snowing, just like the forecast said it would."

    "I push open the umbrella to protect my head from the black snow."

    "Don't wanna end up bald."

# BG: front door of a house (I think I'm just gonna zoom into Case E's dark BG, flip it, and hope no one notices.)
    scene bg introhouse with dissolve
    "Well, this is the house."

# SFX of doorbell being pushed
    play sound "sfx/doorbell.ogg"
    "I ring the doorbell while reviewing the patient case notes on my tablet once more."

    "Discomfort in the joints, starting from two weeks ago. Coincidentally, it was also snowing heavily that day."

    "This should be a straightforward case."

# SFX of door opening
    play sound "sfx/door open.ogg"
# sprite of a robot (use a variation or one of the unused/thrown away concepts? no need for emotes or anything)

    show p1 with dissolve:
        xalign 0.5
    p1 "Yes?"

    "I smile at my patient. I can tell right away he's a war veteran, too."

    mc "I'm Doctor Ward. We spoke on the phone earlier today."
    stop env fadeout 2.0
    p1 "Oh! You're just on time. Bless you, doctor. My joints really are killing me,"

    "The discoloration around the patient's limbs confirms my initial diagnosis."

    mc "Have you been taking proper precautions from the black snow?"

    p1 "I usually do, doctor. However, how embarrassing, I may have fallen asleep on the porch once when it was snowing."

    "I sigh and shake my head in disappointment. I'm not actually {i}that{/i} disappointed. I'm mostly doing it for effect."

    mc "You know what the chemicals in that snow do, don't you?"

    mc "In fact, it was developed {i}specifically{/i} to melt your chassis during the war."

    mc "Please be more careful."

    p1 "I will. I promise, doctor. Now, will you relieve this old man of his pain already?"

    "I laugh and pull out my tools. A screwdriver and a wrench, for now. Neutralizing agents and a sterile cloth later. Time to get to work."

# fade to black
# fade to flackback BG - zoom in at the sofa at the clinic, flipped, black and white? sepia?

    # "I was in my final year of mechanical engineering, watching TV in my dorm, when my life changed forever."
    #
    # "The usual programming was interrupted, replaced by an emergency breaking news."
    #
    #
    # "They assassinated a diplomat who was at a summit for peace talks."
    #
    # "Each of us knew what that meant."
    #
    # "We were at war."

# END SCENE, FADE TO BLACK
    scene black with dissolve
    jump main1
