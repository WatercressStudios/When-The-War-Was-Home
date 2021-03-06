label b1:
    #Case B
    #Wolf's Territory
    #Scene 1: "Save 'Em, Too."


    scene bg clinic with Dissolve(2.0)
    play music "music/Other Side.ogg" fadein 2.0
    show fly:
        align (0.5, 0.5)
        block:
            ease 1.5 yoffset -20
            ease 1.5 yoffset +20
            repeat

    mc "You know, a body swap procedure like this is a pretty rare one. Normally I only do it for the severely injured, but-"

    fly "C'mon, man..."

    mc "-But, I know how those of your particular model are treated. Having any non-humanoid chassis is social suicide. That's just the way people outside of our community are, I suppose."

    fly "Hey, whatever ya have ta tell yourself. I just want this done sooner than later, ya know?"

    mc "What, is that not the case here?"

    fly "Bro, I don't give a shit what anyone has ta think'r say about me. People will say whatever bullshit they wanna say, and there ain't nothin' I can do about it."

    fly "They haven't done nothin' ta deserve my attention anyways."

    mc "Then what is the {i}real{/i} reason, then? I can't go through with this in good faith without knowing what's up."

    fly "I..."
    "I look him right in the eye, crossing my arms. He cracks under the pressure."

    fly "Aah... I... Okay, okay, okay — so. You served. We all know ya served. Fixin' up all us bots. Were ya ever in the fight, like, guns to motherfuckers' heads combat?"

    "I shake my head."

    mc "I was on the field plenty of times, but they only risked me being there if the front had moved on."

    fly "Yeah, yeah, yeah. So, in your case, wouldjya say you... I dunno, ever felt sorta helpless?"

    fly "Like, you never picked up a gun and pointed it at the enemy. You never {i}fought{/i}, ya know?"

    fly "Doesn't that ever bother you?"

    mc "Well, if I had to admit it, yes. Sometimes it does bother me. Sometimes I get called a POG, but other times people thank me for all the work I did."

    mc "I may not have fired a gun outside of training, but I kept all you boys in the fight. I helped you get back home."

    fly "Yeah, but, but, but — ya only were ever able ta send everyone back ta fight and die again. Ya couldn't change the outcome."

    mc "You were reconnaissance, right? Sure, you weren't “Recon”, but you were the first out. That's why you were built. No matter who you are on the inside, the military molded you."

    mc "They gave you your core and your body and your flight mechanisms, and all of that shit - just to serve a singular purpose."

    mc "Sure, it's fucked up that we often had very little say in what we did, but we still did it."

    mc "In fact, we did it {b}well{/b}. Very well. Supremely fucking well. We were the best motherfuckers at that job, bar none. That's how we won the war, no matter what shape that victory ended up taking."

    mc "We — biological and mechanical — were all well-oiled machines. If we fucked up, if we didn't do our job to the utmost of our ability, {i}people fucking died{/i}."

    mc "If I weren't there, all of those people would have died. They needed me more than anyone could ever know."

    mc "And you were recon. Without your intelligence, your eye in the sky, many others would die as well. We can't fight a war blind."

    mc "Just like we can't fight a war with broken bones, and we can't fight a war without weapons, food, ammunition, water, transportation, logistics — war isn't a singular thing. We all did our part."

    mc "In one way or another, we were all cogs in a machine. War is complex, simplified only by compartmentalization and task organization."

    fly "Shit, doc. You and your big fuckin' words."

    mc "But you're picking up what I'm laying down, yeah?"

    fly "Don't worry, I'm trackin', I'm trackin'."

    fly "Fuck, man. If we didn't do our job, {i}people fuckin' died{/i}."

    fly "Ain't that the truth."

    mc "So, you still want to go through with it?"

    fly "Hell yeah doc, you crazy? Ya helped me out a lot in the head, but that doesn't change what I want to do. I can always switch back, right?"

    mc "I mean, yes-"

    fly "Exaaaactlyyyy! With this new body, imagine the cool shit I could do."

    mc "It is a nice chassis, yeah, but-"

    fly "Bro, I wanna get into rescue. Liftin' up heavy buildings 'n shit, making sure people are safe. I watched enough people die, it's time I got ta save 'em too."

    mc "I... am not going to lie, I didn't expect that. It's good work."

    fly "Right? Nobody thinks that I'm thinkin', but I'm thinkin' more than any thinkin' man's gonna think about me."

    mc "I-Uh, sure. I believe you."

    fly "Alrighty, let's get this shit going, doc, we don't have all day!"

    hide fly with dissolve
    show bg clinic:
        ease 2.0 xalign 0.0

    "He reclines back in the operating chair, and I get to work."

    stop music fadeout 2.0

    hide fly at right with dissolve
    scene black with dissolve
    jump choice
