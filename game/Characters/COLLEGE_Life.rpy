# жизнь в колледже
default college_life_last_init_daytime = -1

label college_life_change_daytime:
    if scene_name == "college_street" or scene_name == "college_streetyard":
        call college_life() from _rcall_college_life
        return
    return

label college_life:
    if day_time_idx == 0 and week_day != 7:
        $ move_object("Sister2", "college_empty")

    if college_life_last_init_daytime == day_time_idx:
        return
label college_life_forced:
    python:
        college_life_last_init_daytime = day_time_idx
        set_active(False, group="students", scene="college_street", recursive=True)

        # улица
        if day_time_idx == 0 or day_time_idx == 1:
            # день
            set_active("Crowd1", True, scene="college_street")
            set_active("Crowd2", True, scene="college_street")
            set_active("Crowd3", True, scene="college_street")
            rand1 = renpy.random.randint(1, 2)
            collegeStreetCrowd3_Suffix = rand1
            set_active("Crowd4", True, scene="college_street")
            rand1 = renpy.random.randint(1, 2)
            collegeStreetCrowd4_Suffix = rand1
            set_active("Crowd5", True, scene="college_street")
            rand1 = renpy.random.randint(1, 2)
            collegeStreetCrowd5_Suffix = rand1
            set_active("Crowd6", True, scene="college_street")
            rand1 = renpy.random.randint(1, 2)
            collegeStreetCrowd6_Suffix = rand1
            set_active("Crowd7", True, scene="college_street")
            set_active("Crowd8", True, scene="college_street")
            set_active("Crowd9", True, scene="college_street")
            set_active("Classmate1", True, scene="college_street")
            rand1 = renpy.random.randint(1, 2)
            collegeStreetClassmate1_Suffix = rand1

        if day_time_idx == 2:
            # вечер
            set_active("Crowd1", True, scene="college_street")
            set_active("Crowd3", True, scene="college_street")
            set_active("Crowd7", True, scene="college_street")
            set_active("Crowd9", True, scene="college_street")
            set_active("Crowd10", True, scene="college_street")

            set_active("Friend_Bardie", False, scene="college_street")


        # внутри колледжа
        set_active("Student1", True, scene="college_coridor1")
        rand1 = renpy.random.randint(1, 2)
        collegeStudent1_Suffix = rand1
        set_active("Student2", True, scene="college_coridor1")
        set_active("Student3", True, scene="college_coridor1")

        set_active("Student4", True, scene="college_coridor2")
        rand1 = renpy.random.randint(1, 2)
        collegeStudent4_Suffix = rand1
        set_active("Student6", True, scene="college_coridor2")

        set_active("Student7", True, scene="college_coridor3")
        set_active("Student8", True, scene="college_coridor3")
        set_active("Student9", True, scene="college_coridor3")

        set_active("Student10", True, scene="college_coridor4")

        set_active("Student11", True, scene="college_coridor5")
        rand1 = renpy.random.randint(1, 2)
        collegeStudent11_Suffix = rand1
        if collegeStudent11_Suffix == 2:
            set_active("Student12", True, scene="college_coridor5")

        set_active("Student13", True, scene="college_coridor6")
        set_active("Student14", True, scene="college_coridor6")
        set_active("Student20", True, scene="college_coridor6")

        set_active("Student15", True, scene="college_coridor7")
        rand1 = renpy.random.randint(1, 2)
        collegeStudent15_Suffix = rand1
        set_active("Student16", True, scene="college_coridor7")
        set_active("Student17", True, scene="college_coridor7")

        set_active("Student18", True, scene="college_coridor8")

        set_active("Student19", True, scene="college_coridor9")

        # класс английского
        set_active("Visitor1", True, scene="college_english")
        set_active("Visitor2", True, scene="college_english")
        set_active("Visitor3", True, scene="college_english")
        set_active("Visitor4", True, scene="college_english")
        set_active("Visitor5", True, scene="college_english")
        set_active("Visitor6", True, scene="college_english")
        set_active("Visitor7", True, scene="college_english")
        set_active("Visitor8", True, scene="college_english")
        set_active("Visitor9", True, scene="college_english")

    return
