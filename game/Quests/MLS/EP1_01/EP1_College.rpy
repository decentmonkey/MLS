label ep1_college_sean: # встреча с Шоном
    $ remove_hook(label="college_sean")
    $ remove_hook(label="day1_morning")
    if ep1_intro_quests6_cynthia_bathroom_Flag == False:
        $ questHelp("college_4", False)
    $ clear_object_follow_all()
    call ep01_dialogues3_day2_college_1()
    return False
