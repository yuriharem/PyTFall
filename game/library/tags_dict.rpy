init python:
    tags_dict = {
    # Main Tags:
    'nn': 'sfw',
    'nd': 'nude', # Nude Main Tag (Used to be subtag)
    'sx': 'sex',
    'bs': 'battle_sprite',
    'po': 'portrait',
    'qs': 'vnsprite', # Used to be quest
    
    # Nude/SFW Subtags:
    'pr': 'profile',
    'pa': 'girlmeets',
    'pb': 'battle',
    'pc': 'rest',
    'pd': 'beauty',    
    'pf': 'etiquette',
    
    # Locations:
    'l1': 'no bg',
    'l2': 'simple bg',
    'l3': 'outdoors', 
    'l4': 'indoors',
    'l5': 'beach',
    'l6': 'onsen',
    'l7': 'pool',
    'l8': 'stage',
    'l9': 'urban',
    'la': 'wildness',
    'lb': 'suburb',
    'lc': 'nature',
    'ld': 'dungeon',
    'le': 'living',
    'lf': 'public',
    
    # Emotions:
    'e1': 'angry',
    'e2': 'confident',
    'e3': 'defiant',
    'e4': 'ecstatic',
    'e5': 'happy',
    'e7': 'in pain',
    'e6': 'indifferent',
    'e9': 'sad',
    'e8': 'insane',    
    'ea': 'scared',
    'ec': 'suggestive',
    'eb': 'shy',
    'ed': 'tired',
    'ee': 'uncertain',
    
    # Clothes:
    'c9': 'lingerie',
    'c8': 'no clothes',
    'c3': 'indoor',
    'c2': 'formal',
    'c1': 'everyday',
    'c7': 'transformed',
    'c6': 'cosplay',
    'c5': 'ripped', 
    'c4': 'revealing',
    'ca': 'armor',
    'ck': 'cow',
    'cj': 'cat',
    'ci': 'bunny',
    'ch': 'yukata',
    'cm': 'ninja',
    'cl': 'dog',
    'cc': 'maid',
    'cb': 'swimsuit',
    'cg': 'sportswear',
    'cf': 'schoolgirl',
    'ce': 'nurse',
    'cd': 'miko',
    
    # Actions:
    'a1': 'stripping', 
    'a3': 'cleaning', 
    'a2': 'bathing',
    'a5': 'dancing', 
    'a4': 'cooking',
    'a7': 'exercising',
    'a6': 'eating',
    'a9': 'gambling',
    'a8': 'fighting',
    'aa': 'healing',
    'ac': 'musician',
    'ab': 'magic',
    'ae': 'sleeping', 
    'ad': 'reading',
    'ag': 'singing',
    'af': 'shopping', 
    'ai': 'studying',
    'ah': 'sport', 
    'aj': 'waitress',
    
    # Sex Actions:
    # Masturbation:
    'ma': 'masturbation',
    'm5': 'hand',
    'm4': 'othertoy',
    'm7': 'titsvibrator',
    'm2': 'analplug',
    'm1': 'analbeads',
    'm3': 'dildo',
    'm6': 'vibrator',
    'm8': 'forced',
    
    # Cumcovered:
    'cu': 'after sex',
    
    # Group:
    'gr': 'group',
    'gg': 'ass',
    'gf': 'group restrained', 
    'ge': 'group rape',
    'gd': 'othersmast',
    'gc': 'notmain',
    'gb': 'bukkake',
    'ga': 'girlhidden',
    'gl': 'tits',
    'gk': 'feet',
    'gj': 'hands',
    'gi': 'mouth',
    'gh': 'pussy',
    'g7': 'threegirls',
    'g6': 'twogirls',
    'g5': 'onegirl',
    'g4': 'moreguys',
    'g3': 'threeguys',
    'g2': 'twoguys',
    'g1': 'oneguy',
    'g9': 'guyhidden',
    'g8': 'moregirls',
    
    # BDSM:
    'bc': 'cumcovered',
    'bd': 'bdsm',
    'b4': 'suspended',
    'b5': 'whipped',
    'b6': 'tortured',
    'b7': 'alone', 
    'b1': 'leashed',
    'b2': 'bdsm restrained',
    'b3': 'spanked', 
    'b8': 'girl',
    'b9': 'hiddengirl',
    'be': 'dominatrix',
    'ba': 'guy', 
    'bb': 'hiddenguy', 
    
    # "Normal" Sex:
    'ns': 'normalsex',
    'p2': 'straight',
    'p3': 'partnerhidden', 
    'p1': 'gay', # Former "les"
    
    # poses:
    's9': 'standing',
    's8': 'spooning',
    's3': 'missionary',
    's2': 'doggy',
    's1': '69',
    's6': 'scissors', 
    's5': 'ontop',
    's4': 'onside',
    's7': 'sitting',
    'sb': 'restrained',
    'sa': 'rape', 
    
    # Sex to character: (startswith 2c *To Character of the image)
    'sl': '2c hug',
    'sc': '2c analfingering',
    'se': '2c lickanus', 
    'sg': '2c analtoy',
    'sf': '2c lickpussy',
    'sh': '2c vaginaltoy',
    'si': '2c anal',
    'sj': '2c vaginal',
    'sk': '2c kiss',
    'sm': '2c caresstits',
    'sd': '2c vaginalfingering',
    
    # Sex done by character: (startswith bc *To Character of the image)
    'sz': 'bc vaginalfootjob',
    'sy': 'bc analfootjob',
    'ss': 'bc hug',
    'sr': 'bc handjob',
    'sp': 'bc footjob',
    'sw': 'bc vaginalhandjob',
    'sv': 'bc analhandjob',
    'su': 'bc titsjob', 
    'st': 'bc kiss',
    'so': 'bc deepthroat', 
    'sn': 'bc blowjob',
    't6': 'bc toypussy',
    't7': 'bc caresstits',
    't4': 'bc vaginal',
    't5': 'bc toyanal',
    't2': 'bc lickpussy',
    't3': 'bc anal',
    't1': 'bc lickanus',

    # Time/Season:
    'z1': 'evening',
    'z4': 'winter',
    'z2': 'night',
    'z3': 'autumn'
    }
