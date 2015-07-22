init python:
    renpy.image("jumping_frog", animate("/library/events/frog_event/img/frog_jump"))
    renpy.image("jumping_frog_2", animate("/library/events/frog_event/img/frog_jump_2"))
    renpy.image("frog", "library/events/frog_event/img/frog.png")
    renpy.image("boyakki", "library/events/frog_event/img/boyakki.png")
    register_quest("Frog Princess!")
    if config.developer:
        register_event("show_frog", screen=True, quest="Frog Princess!", locations=["forest_entrance"], trigger_type="auto", restore_priority=1, priority=300, start_day=1, jump=True, dice=100, max_runs=20)
    else:
        register_event("show_frog", screen=True, quest="Frog Princess!", locations=["forest_entrance"], trigger_type="auto", restore_priority=1, priority=300, start_day=choice([15, 25, 35]), jump=True, dice=65, max_runs=20)
    
    # Dev Note: I've added screen attribute to WorldEvent class so the useless labels below are no longer required.
    # This doesn't change much for this event but in other places it will mean a much smoother gameplay.
label show_frog_abby_part2:
    show screen show_frog_abby_2
    jump witches_hut_shopping
    
label show_frog_arena_eye:
    show screen show_frog_arena
    jump arena_outside
    
label show_frog_deathfight:
    show screen show_frog_deathfight
    jump arena_outside
    
label show_frog_gotgoods:
    show screen show_frog_abby_3
    jump witches_hut_shopping
    
label show_frog_final:
    show screen show_frog_final
    jump forest_entrance
    
screen show_frog:
    zorder 10
    if renpy.get_screen("pyt_forest_entrance"):
        $ img = Transform("jumping_frog", zoom=0.2)
        imagebutton:
            pos (237, 586)
            idle Transform("jumping_frog", zoom=0.2) 
            hover Transform("jumping_frog", zoom=0.2)
            action Jump("start_frog_event")
    else:
        timer 0.01 action Hide("show_frog")
        
screen show_frog_abby:
    zorder 10
    if renpy.get_screen("pyt_witches_hut_shopping"):
        button:
            style_group "basic"
            align (0.5, 0.9)
            action Jump("frog1_event_abby")
            text "Ask about the frog" align (0.5, 0.5)
    else:
        timer 0.01 action Hide("show_frog_abby")
        
screen show_frog_abby_2:
    zorder 10
    if renpy.get_screen("pyt_witches_hut_shopping"):
        button:
            style_group "basic"
            align (0.5, 0.9)
            action Jump("frog1_event_abby_2")
            text "Ask about the frog (again)" align (0.5, 0.5)
    else:
        timer 0.01 action Hide("show_frog_abby_2")
        
screen show_frog_arena:
    zorder 10
    if last_label == "arena_outside":
        button:
            style_group "basic"
            align (0.9, 0.4)
            action Jump("frog_event_arena")
            text "Enquire about the eye!" align (0.5, 0.5)
    else:
        timer 0.01 action Hide("show_frog_arena")
        
screen show_frog_deathfight:
    zorder 10
    if last_label == "arena_outside":
        button:
            style_group "basic"
            align (0.9, 0.4)
            action Jump("frog_deathfight")
            text "Deathfight!" align (0.5, 0.5)
    else:
        timer 0.01 action Hide("show_frog_deathfight")
        
screen show_frog_abby_3:
    zorder 10
    if renpy.get_screen("pyt_witches_hut_shopping"):
        button:
            style_group "basic"
            align (0.5, 0.9)
            action Jump("frog1_event_abby_3")
            text "Ask about the frog (again)" align (0.5, 0.5)
    else:
        timer 0.01 action Hide("show_frog_abby_3")
        
screen show_frog_final:
    zorder 10
    if renpy.get_screen("pyt_forest_entrance"):
        $ img = im.Scale("library/events/frog_event/img/frog.png", 70, 70)
        imagebutton:
            pos (237, 586)
            idle img
            hover im.MatrixColor(img, im.matrix.brightness(0.15))
            action Jump("final_frog_event")
    else:
        timer 0.01 action Hide("show_frog_final")
        
label start_frog_event:
    hide screen pyt_forest_entrance
    with dissolve
    "In your hunt for attractive women, you picked the forest as your hunting ground for today. Walking for couple of hours, you had found a rather large frog jumping around."
    
    menu:
        "Approach with curiosity to have a closer look.":
            jump frog1_event_look
        "Leave the frog alone.":
            "Not interested in green slime bags, you continue your quest looking for some fun bags."
            $ pytfall.world_quests.get("Frog Princess!").finish_in_label("You've rejected the Frog Princess Quest! It's further fate is unknown.")
            $ pytfall.world_events.kill_event("show_frog")
            jump forest_entrance

label frog1_event_look:
    
    menu:
        "You approach the frog! Upon further inspection, it appears to be wearing a crown."
        
        "Poke the frog with a stick.":
            jump frog1_event_poke
        # "Try to snatch the crown":
            # jump frog1_event_snatch # @Klaus you forgot this choice...
        "Leave the frog alone":
            "Not interested in green slime bags, you continue your quest looking for some fun bags."
            $ pytfall.world_quests.get("Frog Princess!").finish_in_label("You've rejected the Frog Princess Quest! It's further fate is unknown.")
            $ pytfall.world_events.kill_event("show_frog")
            jump forest_entrance # note to Xela, I want it to jump to the previous end quest option, but i don't know if it will or should I copy it from above, paste it belowe and rename.
            # I don't understand what is required here, for now it will terminate the event.


label frog1_event_poke:
    define f1 = Character("Frog", color=green, what_color=lawngreen, show_two_window=True)
    
    hero.say "How do you like that?."
    show frog
    "It easiely dodges your stick and..."
    f1 "Another one came to laugh at my misfortune. Come on. Let's be done with it."
    "The animal's ability to use human language totally surprised you. You are just standing there not knowing what to do."
    f1 "Hey boy, you look like had never seen a talking frog before? Maybe you could help me out? What do you say?"

    menu:
        "Listen.":
            jump frog1_event_listen
        "Run!":
            "You turned around and run towards the city, screaming like a little bitch."
            $ pytfall.world_quests.get("Frog Princess!").finish_in_label("You've rejected the Frog Princess Quest! It's further fate is unknown.")
            $ pytfall.world_events.kill_event("show_frog")
            jump forest_entrance
            
label frog1_event_listen:
    f1 "Once I was a beautiful princess. Few years ago I was travelling thru this woods to wed my beloved in PyTFall. On my travel I met and older women that turned me into this creature. Please could you help a maiden in distress? "
    $ loop = True
    while loop:
        menu:
            "Ask about groom": # note to Xela, all 3 ask options, after reading, should go back to this choice menu but without the frogs text and i don't know how to do this. 
                f1 "We met shortly after the event. He wanted to see his bride as soon as possible, so he came to meet me halfway."
                f1 "Not knowing what happened to me I spoke first. He thought that I was hiding behind the frog, trying to trick him. But when he realized the truth, he broke on his knees crying."
                f1 "Then I realized what have happened to me. We sworn to each other that we would be strong and find a solution."
                f1 "Because of this curse I am enable to leave the forest, so for the first few weeks he came to see me every day."
                f1 "But weeks grew into months and he started to come less frequently. After five months he stopped visiting me and I didn’t saw him ever since…"
            "Ask about older women":
                f1 "I can’t tell you much about her. Only thing that I remember about her, was that she approached me on the road mumbling something and blown some sparkly dust in my face."
            "Ask about Frog Princess":
                f1 "So you would like to know more about me. Sure I will tell you. Once I was a maiden of incomparable beauty."
                f1 "Being  the first daughter of Eastern Yatta Clan I had many admirers. But I fell in love with a merchants son."
                f1 "I planned my escape carefully. On a starless I slipped out my father castle to be with my beloved. On the way I met that older woman."
            "Promise her that you will find a way to break this spell.":
                "You promised her that you would try to find a solution. But do you know someone that use magic and brew potions that would be able to help you?"
                $ global_flags.set_flag("agreed_to_help_frog")
                $ pytfall.world_events.kill_event("show_frog")
                $ loop = False
                $ hero.take_ap(1)
                $ pytfall.world_quests.get("Frog Princess!").next_in_label("You've met a talking frog who claims to be a princess! She asked you to help restore her original form.", manual=True)
                $ register_event_in_label("show_frog_abby", screen=True, locations=["witches_hut_shopping"], trigger_type="auto", restore_priority=1, priority=300, start_day=day, jump=True, dice=100, max_runs=100)
                # Using the new method to add the button to abbies hut on the same day!:
                $ pytfall.world_events.force_event("show_frog_abby")
                jump forest_entrance
            "Fuck this, I'm going home.":
                "Not being interested in a talking frog tale you had left the forest."
                $ pytfall.world_quests.get("Frog Princess!").finish_in_label("You've rejected the Frog Princess Quest! It's further fate is unknown.")
                $ pytfall.world_events.kill_event("show_frog")
                $ loop = False
                jump forest_entrance

label frog1_event_abby:
    # note to Xela, this should be an option when talking to Abby inside the witch hut. the text is: "Ask about finding a way to lift a spell from a talking frog."
    $ w = Character("Abby", color=orange, what_color=yellow, show_two_window=True)
    hide screen pyt_shopping
    hide screen pyt_witches_hut_shopping
    with dissolve
    
    if not global_flags.flag("frog_spoke_abby"):
        w "Frog transmutation, heh? I could look into it, but it will cost ya!"
        extend " Let me see..."
        w "{color=[gold]}5000 Gold{/color} for my research!"

    menu:
        w "How about it?"
        "Pay her." if hero.gold >= 5000:
            w "I should have the answer soon. Come see me in few days." # not to Xela, MC -5000 gold, quest goes to next phase, kicked out the hut or just to the talk menu.
            $ pytfall.world_quests.get("Frog Princess!").next_in_label("For a hefty sum of 5000 Gold Abby the witch promised to look into the frog matter. You should visit her again in a few days.")
            $ hero.take_money(5000, reason="Other")
            $ register_event_in_label("show_frog_abby_part2", locations=["witches_hut_shopping"], trigger_type="auto", restore_priority=1, priority=300, start_day=day+4, jump=True, dice=100, max_runs=100)
            $ pytfall.world_events.kill_event("show_frog_abby")
            jump forest_entrance
             
        "I don't have that kind of money right now.":
            w "That's too bad. Come back when you have the money."
            $ global_flags.set_flag("frog_spoke_abby")
            jump forest_entrance
        "5000??? I'm not paying!": #note at Xela, drop quest option.
            "Being the last ray of hope for a princess turned into a talking frog  to regain her humanity, you decided that spending 5000 gold was too much."
            extend "{color=[red]} Way to go cheapskate!"
            $ pytfall.world_quests.get("Frog Princess!").finish_in_label("You've rejected the Frog Princess Quest! It's further fate is unknown.")
            $ pytfall.world_events.kill_event("show_frog_abby")
            jump forest_entrance


label frog1_event_abby_2:
    $ w = Character("Abby", color=orange, what_color=yellow, show_two_window=True)
    hide screen pyt_shopping
    hide screen pyt_witches_hut_shopping
    with dissolve
    
    hero.say "Did you found anything?" # note to Xela, this should be an option when talking to Abby inside the witch hut. 
    if dice(50 + day/3):
        w "Still going thru my books and scrolls. Come back later." # note to Xela, option able for first 3 days, when asking Abby did she finished. <-- Too much hussle :(
        jump forest_entrance
    else:    
        w "I found a solution. A rare magic potion should do the trick but that's not the hard part..."
        extend " I need another 10 000 gold to buy the necessary ingredients but the really hard part will be getting a goblin champion eye." # note to Xela, option avaible from day 4 after Abbys line go to menu.

    menu:
        "I will get you the money and the eye...":
            $ pytfall.world_events.kill_event("show_frog_abby_part2")
            $ pytfall.world_quests.get("Frog Princess!").next_in_label("Abby asked you to aquire another 10000 Gold for ingridients and an eye of a Goblin Champion.")
            $ register_event_in_label("show_frog_arena_eye", locations=["arena_outside"], trigger_type="auto", restore_priority=1, priority=300, start_day=day, jump=True, dice=100, max_runs=100)
            jump forest_entrance
        "Oh my weak heart! 10 000 not a chance.":
            "You gave up :("
            $ pytfall.world_quests.get("Frog Princess!").finish_in_label("You've rejected the Frog Princess Quest! It's further fate is unknown.")
            $ pytfall.world_events.kill_event("show_frog_abby_part2")
            jump forest_entrance

label frog_event_arena:
    hide screen pyt_arena_outside
    "You find Xeona to ask about the eye."
    define ax = Character('Xeona', color=ivory, show_two_window=True)
    show npc xeona
    with dissolve
    
    ax "An eye of the goblin champion you say?"
    ax "I sure hope it's not some weird fetish you're into..."
    ax "It can be arranged I suppose, as you may know, damnpening field prevents fatal blows in the Arena, often even to Monsters but a proper DeathMatch can be arranged."
    ax "Come back in three days and make certain you are well equiped, you may even consider bringing a couple of friends along with you."
    ax "A real G-Champ will be bloody hard to kill and in deathmatch you'll die as well if your party is wiped out."
    ax "Also don't expect him to be along even if you are, people will expect a vicious fight, deathmatches are rare enough so it's best to make it look good!"
    $ hero.take_ap(1)
    $ pytfall.world_quests.get("Frog Princess!").next_in_label("Xeona agreed to set up a match per your request but you've been warned that it is a {color=[red]}very{/color} dangerous endevour and it would be a good idea to bring some backup!")
    $ register_event_in_label("show_frog_deathfight", locations=["arena_outside"], trigger_type="auto", restore_priority=1, priority=300, start_day=day+3, jump=True, dice=100, max_runs=100)
    $ pytfall.world_events.kill_event("show_frog_arena_eye")
    jump arena_outside
    
label frog_deathfight:
    hide screen pyt_arena_outside
    define ax = Character('Xeona', color=ivory, show_two_window=True)
    show npc xeona
    with dissolve
    $ renpy.music.stop(channel="world")
    ax "Well, I hope that you're ready! "
    extend "{color=[red]}Best of luck!"
    $ hero.take_ap(2)
    python:
        # Prepear the teams:
        enemy_team = Team(name="Enemy Team", max_size=3)
        mob = copy.deepcopy(pytfall.mobs["Goblin Warrior"])
        for stat in ilists.battlestats:
            stat_value = int(getattr(mob, stat) * 16)
            setattr(mob, stat, stat_value)
        enemy_team.add(mob)
        mob = copy.deepcopy(pytfall.mobs["Goblin Archer"])
        for stat in ilists.battlestats:
            stat_value = int(getattr(mob, stat) * 8)
            setattr(mob, stat, stat_value)
        enemy_team.add(mob)
        enemy_team.add(mob)
        
        result = start_battle(hero.team, enemy_team, music=choice(ilists.battle_tracks), background="bg battle_arena_1")
        
        if result[0]:
            renpy.play("content/sfx/sound/events/go_for_it.mp3")
            for member in hero.team:
                if member not in result[1]:
                    member.attack += 2
                    member.luck += 2
                    member.defence += 2
                    member.magic += 2
                    member.vitality -= 100
                    member.exp += adjust_exp(member, 500)
        else:
            jump("game_over")
            
    ax "Great Fight!!! I was rooting for you!"
    ax "Knock yourself out playing with it's corpse ;) I am sure getting to the eye will be no problem."
    $ pytfall.world_quests.get("Frog Princess!").next_in_label("You got the eye! You should visit Abby yet again!")
    $ register_event_in_label("show_frog_gotgoods", locations=["witches_hut_shopping"], trigger_type="auto", restore_priority=1, priority=300, start_day=day, jump=True, dice=100, max_runs=100)
    $ pytfall.world_events.force_event("show_frog_gotgoods")
    $ pytfall.world_events.kill_event("show_frog_arena_eye")
    jump arena_outside
            
            
# note to Xela, option in the talk menu inside the witch hut should be able for selection: 
label frog1_event_abby_3:
    $ w = Character("Abby", color=orange, what_color=yellow, show_two_window=True)
    hide screen pyt_shopping
    hide screen pyt_witches_hut_shopping
    with dissolve
    
    w "I heard you got the base ingredient. " # note to xela, the same talk menu: 
    extend "I heard it was one hell of a fight in the Arena!"
    extend " ... too bad I've missed it."
    w "Anyway, I took liberties to prepear the potion so I only need the eye from you (takes the eye)."
    w "And don't worry about the 10000 Gold, I was only joking, most of these ingriedients grow right outside my hut :)"
    "Three minutes have passed..."
    w "Here is the potion. Now listen. To undo the spell, have the frog to drink the potion and after that you have to kiss."
    extend " She should transform right away. It's that simple. If a normal kiss won't work try a more passionate one. Good luck!"
    "You get a little corked vial, filled with a glowing green liquid called the potion of unfroging. You rushed in a hurry form the Withes Hut."
    $ pytfall.world_quests.get("Frog Princess!").next_in_label("Finally you have the potion! Talk to the frog again!")
    $ renpy.music.stop(channel="world", fadeout=1)
    scene bg forest_entrance at truecenter
    hero.say "Damn, that blasted frog isn't around... Maybe I should comeback tomorrow."
    $ pytfall.world_events.kill_event("show_frog_gotgoods")
    $ register_event_in_label("show_frog_final", locations=["forest_entrance"], trigger_type="auto", restore_priority=1, priority=300, start_day=day, jump=True, dice=100, max_runs=100)
    jump forest_entrance

label final_frog_event:
    hide screen pyt_forest_entrance
    "Having a solution to the frog princess problem you enter the forest with confidence."
    "Finding her wasn't really a problem, she was sitting on the same rock when you met for the first time."
    
    define f1 = Character("Frog", color=green, what_color=lawngreen, show_two_window=True)
    
    show frog
    f1 "So why did you came today?"
    
    menu:
        "I have found a method to break the spell.": 
            jump frog1_event_potkiss
        "I know how to break the spell but it will cost you.": 
            jump frog1_event_potkissgold

label frog1_event_potkissgold:
    f1 "I will do anything just help me. My father is a very rich and powerful man. He surely will pay you any sum when I safely return home."
    menu:
        "Give potion + Kiss":
            jump frog1_event_potkiss
        "Don't give her anything":
            jump frog1_event_potspit 

label frog1_event_potspit:
    hero.say "I need some proof first!"
    f1 "Come here I will show you a proof."
    play sound "library/events/frog_event/sfx/spit.mp3"
    "Irritated frog spit in your face. It was highly poisonous (Almost Zerg-like). Your death was instant..." # note to Xela, game over here.
    jump game_over

label frog1_event_potkiss:
    play sound "library/events/frog_event/sfx/kiss_short.mp3"
    "Frog drunk the potion and you gave it a quick kiss. Nothing happened. You need to be more passionate."
    menu:
        "French kiss":
            jump frog1_event_french
        "It's to disgusting":
            jump frog1_event_disq

label frog1_event_disq:
    "First kiss was disgusting enough, this is just too much for you. After dropping the frog you head back home thinking about what a crappy ordial this was." # note to Xela, end quest.
    $ pytfall.world_quests.get("Frog Princess!").finish_in_label("You could not bring yourself to kiss the frog properly...")
    $ pytfall.world_events.kill_event("show_frog_final")
    jump forest_entrance

label frog1_event_french:
    
    "You had French kissed a frog! (Side note: Large Frogs eats: flies, mosquitoes, moths, dragonflies, small snakes, mice, baby turtles and sometime other smaller frogs)."
    play sound "library/events/frog_event/sfx/kiss_long.mp3"
    show frog:
        size (389, 400)
        crop (0, 0, 389, 400)
        easein 1.0 crop (100, 100, 100, 100)
    "..."
    scene black
    $ flash = Fade(.25, 0, .75, color="#fff")
    scene bg forest_entrance
    with flash
    
    play sound "content/sfx/sound/events/good_night.mp3"
    "It worked. A bright flash and the frog was gone. In her place was…"

    show boyakki
    define b = Character("Boyakki", color=red, what_color=green, show_two_window=True)
    b "Thanks dude. You really saved me. About that princess and gold..."
    $ pytfall.world_quests.get("Frog Princess!").finish_in_label("{color=[blue]}You've completed the Quest... but the whole thing was Boyakkis scam...{/color}")
    show boyakki:
        parallel:
            zoom 1.0
            linear 1.0 zoom 0.1
        parallel:
            align (0.5, 1.0)
            linear 1.0 align (0.28, 0.67)
    extend " {color=[red]} It was all crap! Sorry, gotta go!"
    hide boyakki
    with fade
    "You had lost a lot of time, 5 000 Gold and French kissing frog. But look at the bright side. Now you know that you shouldn't trust a talking frog."
    "On your way back you meet another talking frog with a cape on its back."

    show jumping_frog_2
    define f2 = Character("Frog x2", color=green, what_color=lawngreen, show_two_window=True)
    f2 "Excuse me kind sir. Could you help a damsel in distress?"
    menu:
        "Not falling for it twice!": # note to xela, this will be the only option for times being. If we want to continue with event for the second frog we have a foothold in here.": 
            jump frog1_event_frog2not

label frog1_event_frog2not:
    "Without stopping you ignored the frog getting away from it as fast as possible."
    $ pytfall.world_events.kill_event("show_frog_final")
    jump forest_entrance

