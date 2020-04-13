#
#

default calls_done = []
default calls_available = []

init python:
    choices_menu_text = {
        'intro2': 'Intro house call',
        'a1': 'Case A',
        'b1': 'Case B',
        'c1': 'Case C1',
        'c2': 'Case C2',
        'c3': 'Case C3',
        'd1': 'Case D1',
        'd2': 'Case D2',
        'e1': 'Case E',
        'main3': 'Main 3',
        'main4': 'Main 4',
        'main5': 'Main 5',
    }

    all_choices_intro = [
        'intro2',
    ]
    all_choices_act1 = [
        'a1',
        'b1',
    ]
    all_choices_act2 = [
        'c1',
        'c2',
        'c3',
        'd1',
        'd2',
        'e1',
        'main3',
        'main4',
        'main5',
    ]

    def update_calls_variables(all_choices):
        global calls_available

        calls_available = []
        for c in all_choices:
            if c == 'c2' and not 'c1' in calls_done:
                continue
            if c == 'c3' and not 'c2' in calls_done:
                continue
            if c == 'd2' and not 'd1' in calls_done:
                continue
            if c == 'e1' and not 'c1' in calls_done:
                continue
            if c == 'main3' and (not 'main2' in calls_done or len(calls_done) < 5):
                continue
            if c == 'main4' and (not 'main3' in calls_done or len(calls_done) < 8):
                continue
            if c == 'main5' and (not 'main4' in calls_done or len(calls_done) < 11):
                continue
            if not c in calls_done:
                calls_available.append(c)

    def get_menu_choices(all_choices):
        choices = []
        for c in all_choices:
            choices.append((choices_menu_text[c], c))
        return choices

label choice:
    $ calls_available = None
    if len(calls_done) == 0:
        $ update_calls_variables(all_choices_intro)
    elif len(calls_done) < 3: # intro + ACT 1
        $ update_calls_variables(all_choices_act1)
    elif len(calls_done) == 3: # intro + ACT 1
        $ calls_done.append('main2')
        # jump credits
        jump main2
    elif len(calls_done) < 13: # intro + ACT 1 + main2 + ACT 2
        $ update_calls_variables(all_choices_act2)
    elif len(calls_done) == 13: # intro + ACT 1 + main2 + ACT 2
        $ calls_done.append('main6')
        jump main6

    # Show the organiser UI once available

    # For now, use menu selection
    $ c = renpy.display_menu(get_menu_choices(calls_available))
    $ calls_done.append(c)
    $ renpy.jump(c)
