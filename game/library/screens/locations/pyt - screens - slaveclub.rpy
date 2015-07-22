label slave_market_club: 
    
    python:
        # Build the actions
        if pytfall.world_actions.location("slave_market_club"):
            pytfall.world_actions.look_around()
            pytfall.world_actions.finish()
    
    scene bg slave_market_club
    show screen pyt_slavemarket_club
    with fade
    
    $ pytfall.world_quests.run_quests("auto")
    $ pytfall.world_events.run_events("auto")
    
    python:
        while 1:
            result = ui.interact()
            
            if result[0] == 'control':
                if result[1] == 'return': 
                    break
    
    $ global_flags.set_flag("came_from_sc")
    hide screen pyt_slavemarket_club
    jump slave_market
    

screen pyt_slavemarket_club:
    
    use pyt_top_stripe(True)
    
    use location_actions("slave_market_club")
    
