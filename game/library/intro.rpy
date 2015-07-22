init python:
    """
    init phase is initiation phase that is used to declare constant stuff. At most, you will be defining images in it and using it to create events/quest and their conditions! There will be examples of that in different files.
    This file is the first you should read if you wish to get into written/story development of PyTFall as it contains all the basics.
    play music "path/file.ogg"
    Transform("path/img.png", zoom=-1)
    show image_tag:
    pos (100, 100)
    show image_tag at Transform(pos=(100, 100)) with move
    This is a way to leave a long, multiline comment in Python and Ren'Py.
    show tag:
    yalign 1.0
    xpos 100

    show layer master at damage_shake(0.05, (-10, 10))
    pause 2.0
    show layer master
    There is a very detailed Ren'Py and (far more complicated) Python documentation avalible if you want to learn about something in greater detail.
    Ren'Py comes with a number of script languages. Python is the main one, everything can be done with it but it often requires a long and complicated code.
    That's why other script languages were created as wrappers around it:
    
    **Python:
    Everrything that starts with:
    $
    or
    python:
    
    1) Ren'Py Script: It's evething you see in .rpy files that is not declared as being something else.
    *Examples:
    label
    show
    menu
    image
    define
    and so on.
    
    2) Screen Language (short: SL (Ren'Py in 6.18 was updated to Screen Language 2))
    Screens are used to diplay information to the players and enable any interaction that is not anticipated in default Ren'Py (Anything more than default VN capabilities basically)
    evething that comes after:
    screen my_screen:
        # Screen Language statements
    
    3) ATL (Animation and Transformation Language). 
    Used to move displayable, zoom, crop, rotate and so on.
    Examples:
    transform my_transform:
        # Transformation instructions
    image my_image:
        # Transformation instructions
    
    4) Style Script:
    This is used to create styles and customise the displyable.
    style my_syle:
        # style statements
    
    ===
    init: (initiation phase, it runs every time Ren'Py game is launched from the OS) should be mensioned as well.
    """
    
init:
    image terumi normal = ProportionalScale("content/events/Intro/terumi.png", 1700, 500)
    image terumi reversed = Transform(ProportionalScale("content/events/Intro/terumi.png", 1600, 400), xzoom=-1)
    image sinstar = FilmStrip('content/events/Intro/sinstar.png', (192, 192), (5, 6), 0.1, loop=True)
    image teleport = FilmStrip('content/events/Intro/Teleport.png', (256, 256), (4, 4), 0.1, loop=False)
    image timestop = FilmStrip('content/events/Intro/time_stop.png', (800, 800), (24, 1), 0.1, loop=False)
    image bg slq = im.Scale("content/events/Intro/slq.jpg", config.screen_width, config.screen_height)
    image bg firetome = im.Scale("content/events/Intro/firetome.jpg", config.screen_width, config.screen_height)
    image bg war = im.Scale("content/events/Intro/war.jpg", config.screen_width, config.screen_height)
    image bg ash1 = im.Scale("content/events/Intro/ash1.jpg", config.screen_width, config.screen_height)
    image bg ash2 = im.Scale("content/events/Intro/ash2.jpg", config.screen_width, config.screen_height)
    image bg dun = im.Scale("content/events/Intro/dungeon.jpg", config.screen_width, config.screen_height)
    image bg fcity = im.Scale("content/events/Intro/fire_city.jpg", config.screen_width, config.screen_height)
    image bg wh = im.Scale("content/events/Intro/wh.jpg", config.screen_width, config.screen_height)
    image bg p1 = im.Scale("content/events/Intro/p1.jpg", config.screen_width, config.screen_height)
    image bg p2 = im.Scale("content/events/Intro/p2.jpg", config.screen_width, config.screen_height)
    image bg p3 = im.Scale("content/events/Intro/p3.jpg", config.screen_width, config.screen_height)
    image bg p4 = im.Scale("content/events/Intro/p4.jpg", config.screen_width, config.screen_height)
    image bg sky1 = im.Scale("content/events/Intro/sky1.jpg", config.screen_width, config.screen_height)
    image bg sky2 = im.Scale("content/events/Intro/sky2.jpg", config.screen_width, config.screen_height)
    image bg sky3 = im.Scale("content/events/Intro/sky3.jpg", config.screen_width, config.screen_height)
    image bg ruin1 = im.Scale("content/events/Intro/ruin1.jpg", config.screen_width, config.screen_height)
    image bg ruin2 = im.Scale("content/events/Intro/ruin2.jpg", config.screen_width, config.screen_height)
    image boy = ProportionalScale("content/events/Intro/boy.png", 900, 300)
    image logo = ProportionalScale("content/events/Intro/logo-transperent.png", 600, 300)
    image cat = ProportionalScale("content/events/Intro/cat.png", 1100, 350)
    image girl = ProportionalScale("content/events/Intro/girl.png", 1300, 400)
    image priest = ProportionalScale("content/events/Intro/priest.png", 1300, 400)
    image soldier1 = ProportionalScale("content/events/Intro/soldier.png", 1800, 550)
    image soldier1 kaputt = HitlerKaputt(ProportionalScale("content/events/Intro/soldier.png", 1300, 400), 50)
    image tergr = ProportionalScale("content/events/Intro/tergr.png", 1700, 500)
    image he = ProportionalScale("content/events/Intro/h1.png", 1750, 550)
    image hes = ProportionalScale("content/events/Intro/he1.png", 1750, 550)
    $ flash = Fade(.75, 0.25, .75, color=darkred)
    $ sflash = Fade(.25, 0, .25, color=darkred)
    
    transform star:
        subpixel True
        parallel:
            repeated_rotate(t=0.1)
    
label intro:
    stop world
    stop music

    scene black
    
    #show sinstar:
    #    pos (100, 100)
    #    alpha 0
    #    linear 1.0 alpha 1.0
    #    star
    #show sinstar at Transform(pos=(500, 500)) with move:
    #    alpha 0
    #    linear 1.0 alpha 1.0
    #    star
    # play music "content/sfx/music/intro-1.mp3"
    
    show expression Text("Mundiga continent", style="tisa_otm", align=(0.5, 0.33), size=40) as txt1:
        alpha 0
        linear 3.5 alpha 1.0
    show expression Text("3596 AD", style="tisa_otm", align=(0.5, 0.66), size=35) as txt2:
        alpha 0
        1
        linear 3.5 alpha 1.0
    pause 4
    hide txt1
    hide txt2
    with dissolve
    
    play music "content/sfx/music/intro-1.mp3" fadein 2.0 fadeout 2.0
    "Through trade and seemingly endless supply of slaves from the City of Crossgate, which grew from a small provincial city into the SlaveTrade capital of the world in a matter of years, many new city states arose."
    
    show bg humans with dissolve
    "One of them is PyTFall, a relatevely small town in neutral lands on the border of the Median Empire."
    
    show bg city_jail with dissolve
    "It was a time when slaves had less rights than pets..."
    extend " They were severely punished and could executed on spot by their masters without reprecussions for the slightest infraction."
    
    show bg slq with dissolve
    "Cruelty and lust for power of the Masters knew no bounds and they carelessly kept breeding and buying more and more slaves..."
    extend " and soon found themselves outnumbered ten to one."
    
    "They say there were those who sympathized with the oppressed. Those who gave them weapons and magic to fight back. "
    show bg firetome with ImageDissolve("content/gfx/masks/m21.jpg", 2)
    extend "To resist!"

    show bg war with dissolve
    "Riots happened one after the other. It is easy to take up arms when you have nothing to lose."
    "First few incedents were violently suppresed by the Masters..."
    extend " but it was too late."
    "The conflict quickly turned into a full scale warfare."
    
    show bg p2 with dissolve:
        subpixel True
        size (config.screen_width, config.screen_height)
        crop (0, 0, config.screen_width, config.screen_height)
        linear 30 crop (config.screen_width/2, config.screen_height/2, config.screen_width/8, 100)
    show he with dissolve:
        yalign 1.0 xpos 400
    "Out of nowhere a stranger appeared, claiming to be a historian."
    "He told the Master of underground sanctuary not too far from the city, where an antient star sleept."
    show bg ruin1 with dissolve:
        subpixel True
        size (config.screen_width, config.screen_height)
        crop (0, 0, config.screen_width, config.screen_height)
        linear 30 crop (config.screen_width/2, config.screen_height/2, config.screen_width/8, 100)
    show hes with dissolve:
        xpos 400 yalign 1.0
    "A dreadful weapon, capable of unimaginable destruction"
    show bg ruin2 with dissolve:
        subpixel True
        size (config.screen_width, config.screen_height)
        crop (0, 0, config.screen_width, config.screen_height)
        linear 30 crop (config.screen_width/2, config.screen_height/2, config.screen_width/32, 100)
    extend " and of crushing the rebels once and for all..."
    "Yelding magic powerful enough to build a new empire and maybe, even to surpass Crossgates weath and fame!"
    
    show bg ruin2:
        linear 3 alpha 0
    show hes:
        linear 3 alpha 0
    $ renpy.pause (3.0, hard=True)
    play music "content/events/Intro/tremor.mp3" fadein 2.0 fadeout 2.0
    scene black with dissolve
    show bg humans with dissolve
    pause 1.0
    show layer master at damage_shake(0.05, (-10, 10))
    pause 2.0
    show layer master
    $ renpy.pause (1.0, hard=True)
    show bg sky1 with wipedown:
        alpha 0
        linear 2.0 alpha 1.0
    $ renpy.pause (1.0, hard=True)
    play music "content/sfx/music/intro-2.mp3" fadeout 2.0
    show bg sky2 with flash
    show layer master at damage_shake(0.05, (-10, 10))
    pause 2.0
    show layer master
    show bg sky2 with sflash
    pause 1.0
    show bg sky2 with sflash
    pause 1.0
    show bg sky3 with flash
    pause 1.0
    show bg sky3 with sflash
    pause 1.0
    show bg ash2 with wipeup:
        alpha 0
        linear 2.0 alpha 1.0
    pause 2.0
    show bg ash2:
        subpixel True
        size (config.screen_width, config.screen_height)
        crop (0, 0, config.screen_width, config.screen_height)
        linear 10 crop (config.screen_width/2, config.screen_height/2, config.screen_width/16, config.screen_height/16)
    pause 5.0
    scene bg ash1 with dissolve:
        subpixel True
        size (config.screen_width, config.screen_height)
        crop (0, 0, config.screen_width, config.screen_height)
        linear 10 crop (config.screen_width/2, config.screen_height/2, config.screen_width/16, config.screen_height/16)
    pause 0.5
    $ renpy.show("logo", at_list=[szoom(0.5, 2, 8), Transform(pos=(0.5, 0.75), subpixel=True)])
    $ renpy.with_statement(dissolve)
    pause 4.5
    return
    
    
    
label story:
    
    $ b = Character("Boy", color=white, what_color=white, show_two_window=True, show_side_image="content/events/Intro/boyp.png", window_left_padding=230)
    $ c = Character("Cat person", color=white, what_color=white, show_two_window=True, show_side_image="content/events/Intro/catp.png", window_left_padding=230)
    $ g = Character("Girl", color=pink, what_color=pink, show_two_window=True, show_side_image="content/events/Intro/girlp.png", window_left_padding=230)
    $ t = Character("Terumi", color=green, what_color=green, show_two_window=True, show_side_image="content\events\Intro\pnterumi.png", window_left_padding=230)
    $ s1 = Character("Captain", color=white, what_color=white, show_two_window=True, show_side_image="content\events\Intro\soldierp.png", window_left_padding=230)
    $ pr = Character("Man in cloak", color=white, what_color=white, show_two_window=True, show_side_image="content\events\Intro\priestp.png", window_left_padding=230)
    
    hide screen pyt_mainscreen
    scene black
    stop world
    stop music
    
    play music "content/sfx/music/fire-2.mp3" fadein 2.0 fadeout 2.0
    scene bg fcity with dissolve
    show terumi normal at left with dissolve
    t "Ah, what a view! It certainly brings back memories."
    t "They totally wrecked the shopping district! Marvelous!"
    t "That's some impressive demonstration of power."
    t "Will be even more pleasant to trample into the ground all that rebel scum."
    show terumi normal:
        linear 2.0 xpos 300
    show priest:
        xpos 1500
        yalign 1.0
        linear 2.0 xpos 900
    pr "You late, Terumi! We expected you three days ago! Where the hell have you been?"
    t "Well hello there, good sir! What can I help you with?"
    pr "Silence! Since you are finally here, you ought to join our forces and crush rebels army once and for all!"
    t "I feel like you have anger control problem. May I suggest you to go drink some juice maybe? I have urgent business."
    show priest:
        linear 0.1 yoffset 4
        linear 0.1 yoffset 0
        repeat 2
    pr "How dare you! I command you! I..."
    t "Oh, but no worries. It is easy to fix."
    show terumi normal:
        linear 0.1 xpos 900
    play sound "content/sfx/sound/be/scythe_attack.mp3"
    pr "..!"
    show priest:
      linear 1.1 yoffset 300
      linear 1.0 alpha 0
    play sound "content/sfx/sound/be/body_fall.mp3"
    t "See? You are not angry now. And you command nothing either."
    t "Ah, the day keeps getting better and better!"
    show terumi normal:
        linear 2.0 xpos 1800
    stop music fadeout 2.0
    scene black with dissolve
    stop music
    play music "content/sfx/music/Explosions.mp3" fadein 2.0 fadeout 2.0
    scene bg wh with dissolve
    show girl:
        xpos 300
        yalign 1.0
    show boy at left
    pause 0.3
    play sound "content/events/Intro/tel.wav"
    show cat:
        alpha 0
        xpos 800
        yalign 1.0
        linear 1.0 alpha 1
    show teleport:
        alpha 1
        xpos 720
        zoom 1.5
        yalign 1.0
        linear 2.0 alpha 0
    g "Master!"
    c "Yo. What's up with that kiddo?"
    b "I'm not a kiddo!"
    g "Oh, I'm sorry. I picked up him on my way here. He lost his parants, and..."
    c "I see, I see. Well, finders keepers. Did ya get the package?"
    g "Yes. Here."
    show girl:
        linear 1.5 xpos 500
    c "Good, good. Now I want ya to remember how to make it work. See, ya move this part there, and there, and then stick it here."
    g "I see. What should I do now?"
    c "Ya take this little brat and go to the temple. I have some stuff to check."
    g "You can't possibly mean..."
    c "I still might have a chance to affect his time. And even if I don't... "
    c "I have to make sure that ya guys have enough time. I'll meet ya in the temple."
    show girl:
        linear 0.1 yoffset 4
        linear 0.1 yoffset 0
    g "...I understand. Just be careful, Master."
    c "Ya heard me, brat? You should go with this miss and protect her along the road. She can't do it without ya help."
    b "*blush* I-I will p-protect her. And stop calling me brat, you strange suspicious cat person!"
    c "Can't hear ya, kiddo!"
    play sound "content/events/Intro/tel.wav"
    show teleport:
        alpha 1
        xpos 720
        zoom 1.5
        yalign 1.0
        linear 2.0 alpha 0
    show cat:
        linear 1.0 alpha 0
    pause 1
    scene black with dissolve
    play music "content/sfx/music/intro-1.mp3" fadein 2.0 fadeout 2.0

    play music "content/sfx/music/Explosions.mp3" fadein 2.0 fadeout 2.0
    scene black with dissolve
    show bg p1 with dissolve
    show soldier1 at right
    show terumi normal:
        xpos -600 yalign 1.0
        linear 2.1 xpos 50
    s1 "Yuki Terumi. Who would have thought."
    t "Yes sir master sir! Ready to report, captain sir master chief sir!"
    s1 "If you looking for Council, they were evacuated this morning. There is nothing for you here."
    t "I beg to differ. I heard they also evacuated all valuable staff and stuff. I came to look at the collection of the biggest losers in the city."
    s1 "..."
    t "*sigh* No fun, as usual."
    play sound "content/events/Intro/exp.mp3"
    show layer master:
        linear 0.1 yoffset 5
        linear 0.1 yoffset 0
        repeat 5
    show terumi normal:
        linear 0.1 yoffset 4
        linear 0.1 yoffset 0
    t "Holy shit! Did you heard that? Sounds like they aim at the Palace Tower now. What a crazy idea!"
    s1 "Then perhaps you should leave."
    t "Oh, I will. I just want to take a stroll, real quick. May I?"
    s1 "I don't have an authority to stop a captain of Intelligence Department. Even I want to."
    t "Congratulations! You will live another day! If rebels don't kill you, of course."
    show terumi normal:
        linear 1.0 xpos 300
        linear 1.0 alpha 0
    s1 "..."
    scene black with dissolve
    show bg p2 with dissolve
    show terumi normal with dissolve:
        xpos 300
        yalign 1.0
    play music "content/sfx/music/intro-1.mp3" fadein 2.0 fadeout 2.0
    play sound "content/events/Intro/tel.wav"
    show cat:
        alpha 0
        xpos 800
        yalign 1.0
        linear 1.0 alpha 1
    show teleport:
        alpha 1
        xpos 720
        zoom 1.5
        yalign 1.0
        linear 2.0 alpha 0
    t "Ugh. I was expecting you, but the stench of cat hair still took me by surprise."
    c "Terumi. I'll tell this only once..."
    t "They say you can see the future. Not you personally, I actually doubt it. But some of you people, who live in the Temple of Time."
    c "..."
    t "But I, as the captain of Intelligence Department, can see the present and the past. I know everything about you."
    t "I know about your excavations in Crossgate. I know about your little cute helper. Damn, I even know the color of your underwear today, though I wish I didn't."
    t "I know that you supported slaves rebelion all this time. I even know that the device will take the life of the one who activated it."
    c "..."
    t "Ah, you are not surprised. Such a good master you are for your slave. Not so different from me, eh?"
    t "I know that you afraid Sinister Star. I know..."
    show cat:
        linear 0.1 yoffset 4
        linear 0.1 yoffset 0
        repeat 2
    c "Itakebackallyourtimebythenameofeternity!"
    play sound "content/events/Intro/clock.mp3"
    show timestop:
        linear 1.5 alpha 0
        xpos 400
        yalign 1.0
    show tergr with dissolve:
        xpos 300
        yalign 1.0 
    c "Wow. Ya big mouth really made it easy, mate. I had all time in the world to make the spell."
    stop music
    c "Told ya. You don't follow orders, I take your time back."
    play music "content/events/Intro/tremor.mp3" fadein 2.0 fadeout 2.0
    show sinstar:
        pos (100, 100)
        anchor (0.5, 0.5)
        alpha 0
        subpixel True
        
        parallel:
            linear 2.0 alpha 1.0
        parallel:
            linear 4.0 pos (800, 600)
        parallel:
            1.0
            block:
                rotate 0
                linear 0.1 rotate 360
            repeat
        parallel:
            block:
                linear 1.0 zoom 3.0
                linear 1.0 zoom 1.0
            repeat
                
                
    pause    


    show terumi normal at left
    with dissolve
    "Now the reversed version..."
    
    show terumi reversed at right with move
    
    "HOWEVER, Do note that it was never require to declare a reverced character at all!"
    hide terumi
    show terumi normal at left with dissolve
    
    "Now... we do not show the reversed image we've declared, it's useless if we use ATL:"
    
    show terumi normal at right with move:
        xzoom -1
        # This is one of the ways to use ATL, you can have the image rotating, changing shape and size, flying around the screen, changing alpha and anything like that.
    $ npc1 = Character("Terumi", color=green, what_color=green, show_two_window=True, show_side_image="content\events\Intro\pnterumi.png", window_left_padding=230)
    npc1 "Meow!"
    t "Or not?"
    "Note that all the good stuff is written as comments in examples.rpy file and you will not be able to see it from the game!"
    "There is also a very good tutorial availible if you download Ren'Py SDK kit (less than 30 MB and does not require instalation)!"
    "You should get SDK if you want to develop content for PyTFall. It's not really a 'MUST HAVE' but it's most definetly a should have :)'"
    "There will be a great demonstration tutorial there of what the engine is capable of! This shows similar things but those that are more relevant to {color=[red]}PyTFall{/color}!"
    # {color=[red]}Text{/color} changes something about text styling! You can use a lot here... like {b}Text{/b} will write text in bold!
    # You can check all properties by googling RenPy + Text + Style + Properties
    
    return
