default introHUDBlocked = False

label ep1_intro_quests1:
    call ep01_dialogues1_start_1a() # пляж, показываем геймплей
    call refresh_scene_fade()
    $ introHUDBlocked = True
    return

label ep1_intro_quests1_block:
    hide screen hud_block
    call ep01_dialogues1_start_1a5()
    call refresh_scene_fade()
    return

label ep1_intro_quests2:
    hide screen hud_block
    $ introHUDBlocked = False
    call ep01_dialogues1_start_1a2()
    hide screen hud_screen
    $ add_hook("enter_scene", "ep1_intro_quests3", scene="map")
    call map_show()
    return

label ep1_intro_quests3:
    $ remove_hook()
    show screen sprites_hover_dummy_screen()
    call ep01_dialogues1_start_1ab3()
    call ep01_dialogues1_start_1b() # подглядывание за Оливией и Марком
    call ep01_dialogues1_start_2() # поезд
    call ep01_dialogues1_start_3() # вокзал

    $ autorun_to_object("ep01_dialogues2_day1_family_1_2", scene="house_bedroom_mc")
    $ add_hook("Bed", "ep01_dialogues2_day1_family_1_1", scene="house_bedroom_mc", label="bed_block")
    $ autorun_to_object("ep01_dialogues2_day1_family_1_11", scene="house_livingroomhall")
    $ autorun_to_object("ep01_dialogues2_day1_family_1_15", scene="house_kitchen")

    call ep01_dialogues2_day1_family_1() # комната Барди перед ужином
    call ep01_dialogues2_day1_family_2() # кухня, ужин с семьей
    return
