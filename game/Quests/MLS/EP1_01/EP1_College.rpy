label ep1_college_sean: # встреча с Шоном
    $ remove_hook(label="college_sean")
    $ remove_hook(label="day1_morning")
    $ clear_object_follow_all()
    call ep01_dialogues3_day2_college_1()
    return False
