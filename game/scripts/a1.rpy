
label a1:

    # #*ringing sfx*
    # play sound "sfx/phone ring.ogg"
    # pause 3.5
    # play sound "sfx/pick up.ogg"
    # scene clinic onlayer master with dissolve:
    #     subpixel True xpos 0.5 ypos 1.0 xanchor 0.35 yanchor 1.0 rotate None
    #     parallel:
    #         xpos -0.22
    #         ease 1.0 xpos 0.09
    #     parallel:
    #         zoom 1.48
    #         ease 1.0 zoom 1.0
    # mc "You've reached Dr. Ward, how may we help you today?"
    #
    # ric "Heeeeeeey, what's up Doc?"
    # "Ahhh, no mistaking who's that now."
    # mc "How's it going Ric, finally caught some time home from the last tour?"
    #
    # ric "Is it on the news already or you're too cynical to consider I'm calling just to check on a friend?"
    # mc "I assume both are true, but I skim the entertainment section."
    #
    # ric "Hahaha, ouch, real cold-blooded. Read my bluff without a second thought."
    # ric "I need to buff some scrapes up, I got a new item to showcase this Friday and it just so happen it's the one set that I managed to ding up in a press conference."
    # ric "The world demands perfection, y'know?"
    # "Aggh, here I thought {i}he's{/i} the one that's supposed to be blinded by his hubris."
    # mc "Well, you've got good timing. I have an open slot, care to hop on over to the clinic and we'll knock this out today?"
    # #*clap sfx*
    # show ric smile
    # ric "Marvelous! Be there in a flash hon!"
    # #*click sfx*
    # play sound "sfx/hang up.ogg"
    # "Welp, that's today settled for. It's gonna take a while to reach his standards, but I shouldn't complain. An easy job and good pay."
    scene bg clinic with dissolve:
        xalign 0.0
    "Now, where'd did I leave the sander? Still gotta be around here from his last visit."
    #*rummaging folly sfx*
    play sound "sfx/rumage.ogg"
    pause 2.0
    play sound "sfx/doorbell.ogg"
    #*doorbell sfx*
    show bg clinic:
        ease 1.0 xalign 0.9
    "Right on cue."
    #show ric
    play music "music/richter.ogg" fadein 1.0
    show ric shout with dissolve:
        xalign 0.6
    ric "Dooooooc! It's been too long! Come here!" with hpunch
    #*grip sfx*
    play sound "sfx/hug.ogg"
    "Before I can react, he locks me in a powerful hug. The kind that probably isn't safe for my non-metallic skeleton."
    "Richter is both famous and infamous around these parts, living up to his namesake:"
    "Much like the Richter scale, his ego gets exponentially worse."
    "He's a good kid, don't get me wrong, but he sure makes it hard for people to notice."
    mc "It's... good... to see... {i}y-agh…{/i}"
    #*pistons sfx*
    show ric surprised
    ric "Oh, oh god! My bad Doc, it's been nothing but androids around me this past week, kinda forgot to tone it down."
    # VA: heavy panting from nearly being crushed to death at the start of this line
    mc "No need to ask if the hydraulics are in order."
    "Richter gently straightens my coat, laughing nervously."
    mc "How did the show go? Got any buyers for your collection?"
    show ric neutral
    ric "Yeah, I got three labels that want to purchase the rights for this one, and two others looking into a contract for me to design their fall armor collection."
    ric "Honestly I wanted to work on my casual drone-wear lineup, but if I push it back I might get to work on Tactonic’s new plate composites next season."
    mc "Hope your fans can wait that long, the last leak kind of forced your hand with it, no?"
    show ric pleased
    ric "Hahahaha, you’re not wrong! But that’s stardom baby, ain’t nothing easy in this world!"
    show ric neutral
    ric "I’ve got enough sketches laying around to give them a taste of what’s to come. Worst case I’ll just give up a few nights of sleep to crank them all out."
    mc "Careful Icarus, try to have it all and you might end up with none."
    "Richter flaunts his cape magnanimously."
    show ric pleased
    ric "Nonsense! The Richter brand is synonymous with perfection for a reason! Anything else won’t see the light of day!"
    "I have a feeling he has inspirational music in his head I’m not privy to hear."
    mc "That aside, I think we can get down to business.  I need to find the sander, can you bring the polish from the top of the cabinet?"
    show ric sad
    ric "Umm... can I look for the sander instead? My shoulder’s been acting up lately."
    mc "Oh? This is the first time I'm hearing about this."
    ric "Yeah, um, I mean, it ain’t rolling like it used to. I think the weather abroad did it no good."
    mc "Want me to take a look at it? Maybe I can tune it a little bit."
    "Richter mumbles to himself, his grip on his cape tightening."
    ric "Yeah, umm... Yeah, there’s no good reason not to, right? Feel free."
    play sound "sfx/cape.ogg"
    stop music fadeout 3.0
    hide ric sad with dissolve
    show bg clinic:
        ease 1.5 xalign 0.0
    "He sits down on the examination table, fidgeting.  With a click, he unlocks his cape and I set it aside."
    "I take a screwdriver and remove the screws on the upper arm one by one, loosening up the exo-armor."
    "I gently pry it open to protect the wiring, and take off the front piece and reveal the skeleton beneath."
    #*Scarred Skeleton CG\Sprite*
    "It’s way worse than I anticipated. The scrapes and indentations are numerous, not to mention the large scarring deep in the ball joint."
    play music "music/scars.ogg" fadein 2.0
    "I touch the surface around the scar and notice a rough grainy texture. Rust? No, it's not scraping off. It’s seared."
    show ric dm frown with dissolve:
        xalign 0.5
    ric "Mmm-well? Do you see what’s wrong?"
    mc "Clearly, yeah. You should have told me sooner. Honestly it's a surprise it's only starting to act up."
    ric"Yeah, recently... yeah..."
    "He averts his gaze away, tapping the palm of his hand with his fingers."
    mc "I think I have a replacement joint for the MIMRU series, might not be exactly yours bu-"
    "Richter gently grabs my sleeve, with a slight unwieldy shake."
    show ric dm groan
    ric "About that… c-can we leave that in?"
    "I can’t quite figure out what to say. He still doesn’t look at me, or anything in particular."
    "The superstar that walked in the door is gone. I sit next to him, putting my arm around him"
    mc "What was the mission?"
    show ric dm frown
    ric "Western maneuver of Operation Phalanx. Move to defensive positions in a border town and prepare for a possible siege."
    ric "We received intelligence there was going to be attempted raids across the border, but that didn’t matter. Not to the people."
    ric "They attacked us with everything they had. Bats, knives, rakes, molotovs – whatever was left after the last siege."
    ric "They said we were the reason for the raids, and that we took everything from them."
    ric "And you know what? They were right. We made that town important. We made it worthwhile. It was never a strategic concern until we came."
    ric "We eventually got the go-ahead to push forward, but, I… I don’t want to. I don’t want to let it go."
    mc "You don’t have to let go of it. It’s important. "
    mc "Not everyone needs our help, or wants it, but it's important to reach out and at least offer a hand."
    #ric "I- I want... Please, let me, accept m-m..."
    #Wolf's Temp Replacement:
    show ric dm groan
    ric "I-I want... I don't know. I wish things were different."
    # VA: sniffs/cries a little at the start of line
    ric "Please, I need to keep it."
    "I stand up and wedge the screwdriver between ball joint and its socket"
    mc "It's jutting a bit too much to move in your current exo, so I’ll have to sand off a millimeter or two off it to allow the joint to move freely after lubrication."
    mc "It does mean you’ll have to custom shape your other upper arm guards, but I guess a designer like you can work with it."
    show ric dm neutral
    "Richter looks at me, smiling, and hugs me gently."
    ric "Thank you, Doctor."
    mc "Com’on, Ric. Doc doesn’t need formality"
    show ric dm pleased
    ric "Hehe, maybe so, but you at least deserve it."
    stop music fadeout 2.0
    scene black with dissolve
    jump choice
