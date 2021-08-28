default ep217_quests_shinyhole7_ashley_day = 0
default ep217_quests_shinyhole10_molly_day = 0
default ep217_quests_shinyhole9_ashley_day = 0
default ep217_quests_shinyhole16_molly_after_private_flag = False
default ep217_quests_ashley_tips_dialogue_planned = False
default ep217_quests_shinyhole15_claire_after_private_day = 0
default ep217_quests_shinyhole16_molly_after_private_day = 0

label ep217_quests_shinyhole1_init:
    $ add_talk("Pub_StripteaseGirl2", "ep217_quests_shinyhole2_claire", scene="pub_makeuproom", label="shinyhole_quest1", quest="molly_joe_private1")
    return

label ep217_quests_shinyhole2_claire:
    # Клэр говорит о том, что уходит
    if cloth != "Whore":
        sound snd_fabric1
        fadeblack 2.0
        $ cloth = "Whore"
        $ cloth_type = "Whore"
    call ep217_dialogues2_shiny_hole_1() from _rcall_ep217_dialogues2_shiny_hole_1
    if _return == False:
        $ questHelp("shinyhole_50", True)
        $ questHelp("shinyhole_51", False)
        call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_24
        return False

    $ remove_hook(label="shinyhole_quest1")
    call ep217_dialogues2_shiny_hole_2() from _rcall_ep217_dialogues2_shiny_hole_2


    $ questHelp("shinyhole_50", True)
    $ questHelp("shinyhole_51", True)
    $ questHelp("shinyhole_52")

    $ set_active("Tips", False, scene="pub_makeuproom")
    $ set_active("Tips", False, scene="pub_makeuproom_mollytable")

    $ add_talk("Pub_StripteaseGirl2", "ep217_quests_shinyhole3_claire_repeat", scene="pub_makeuproom", label="shinyhole_quest1", quest="molly_joe_private1")
    $ add_talk("Pub_StripteaseGirl1", "ep217_quests_shinyhole4_molly", scene="pub_makeuproom", label="shinyhole_quest1_molly", quest="molly_joe_private1")
    call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_25
    return False

label ep217_quests_shinyhole3_claire_repeat:
    # Повтор с Клэр
    if cloth != "Whore":
        sound snd_fabric1
        fadeblack 2.0
        $ cloth = "Whore"
        $ cloth_type = "Whore"
    call ep217_dialogues2_shiny_hole_3() from _rcall_ep217_dialogues2_shiny_hole_3
    call refresh_scene_fade() from _rcall_refresh_scene_fade_127
    return False

label ep217_quests_shinyhole4_molly:
    # Ругаемся с Молли
    if cloth != "Whore":
        sound snd_fabric1
        fadeblack 2.0
        $ cloth = "Whore"
        $ cloth_type = "Whore"
    call ep217_dialogues2_shiny_hole_4() from _rcall_ep217_dialogues2_shiny_hole_4
    if _return == False:
        $ questHelp("shinyhole_52", False)
        call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_26
        return False
    $ remove_hook(label="shinyhole_quest1_molly")
    $ questHelp("shinyhole_52a")
    $ add_objective("blame_molly", t_("Подбросить деньги Молли в банку чаевых"), c_red, 155)
    $ set_active("Tips", False, scene="pub_makeuproom")
    $ set_active("Tips", False, scene="pub_makeuproom_mollytable")

    $ add_hook("enter_scene", "ep217_quests_shinyhole5_tips", scene="pub_makeuproom_mollytable", label="shinyhole_quest1_tips", quest="molly_joe_private1")

    return False

label ep217_quests_shinyhole5_tips:
    # Подбрасываем чаевые
    call ep217_dialogues2_shiny_hole_5() from _rcall_ep217_dialogues2_shiny_hole_5
    if _return == False:
        call change_scene("pub_makeuproom", "Fade_long") from _rcall_change_scene_216
        return False

    $ remove_hook(label="shinyhole_quest1_tips")

    $ set_active("Tips", True, scene="pub_makeuproom")
    $ set_active("Tips", True, scene="pub_makeuproom_mollytable")
    $ remove_objective("blame_molly")
    $ add_objective("talk_ashley", t_("Сказать Эшли, что Молли украла у Моники чаевые."), c_orange, 155)
    $ questHelp("shinyhole_52a", True)
    $ questHelp("shinyhole_52b")
    $ add_talk("Bartender", "ep217_quests_shinyhole7_ashley", scene="pub", label=["shinyhole_quest1_tips2", "shinyhole_quest1_ashley"], quest="molly_joe_private1")
    $ add_talk("Bartender_Waitress", "ep217_quests_shinyhole7_ashley", scene="pub", label=["shinyhole_quest1_tips2", "shinyhole_quest1_ashley"], quest="molly_joe_private1")
    $ add_hook("Tips", "ep217_quests_shinyhole6_tips_back", scene="pub_makeuproom_mollytable", label="shinyhole_quest1_tips2", quest="molly_joe_private1")
    $ add_hook("Teleport_Hostel_Street", "ep217_dialogues2_shiny_hole_5a2", scene="pub", label=["shinyhole_quest1_tips2", "shinyhole_quest1_ashley"], quest="molly_joe_private1", priority=100000)
    call refresh_scene_fade() from _rcall_refresh_scene_fade_128
    return False

label ep217_quests_shinyhole6_tips_back:
    # Забираем чаевые назад, если передумали
    call ep217_dialogues2_shiny_hole_5a() from _rcall_ep217_dialogues2_shiny_hole_5a
    if _return == False:
        call refresh_scene_fade() from _rcall_refresh_scene_fade_129
        return False
    $ set_active("Tips", False, scene="pub_makeuproom")
    $ set_active("Tips", False, scene="pub_makeuproom_mollytable")
    $ questHelp("shinyhole_52a", False)
    $ questHelp("shinyhole_52b", False)
    $ questHelp("shinyhole_52c", False, skipIfNonExists=True)
    $ add_money(100.0)
    $ remove_objective("talk_ashley")
    $ remove_hook(label="shinyhole_quest1_tips2")
    $ add_hook("enter_scene", "ep217_quests_shinyhole5_tips", scene="pub_makeuproom_mollytable", label="shinyhole_quest1_tips", quest="molly_joe_private1")
    call refresh_scene_fade() from _rcall_refresh_scene_fade_130

    return False

label ep217_quests_shinyhole7_ashley:
    # Говорим Эшли что Молли украла чаевые
    call ep217_dialogues2_shiny_hole_6() from _rcall_ep217_dialogues2_shiny_hole_6
    $ questHelp("shinyhole_52b", True)
    $ questHelp("shinyhole_52c")
    $ remove_hook(label="shinyhole_quest1_ashley")
    $ remove_objective("talk_ashley")
    $ ep217_quests_shinyhole7_ashley_day = day
    $ add_hook("before_open", "ep217_quests_shinyhole8_molly_ashley", scene="pub_makeuproom", label="shinyhole_quest1_tips2", priority = 99, quest="molly_joe_private1")
    call refresh_scene_fade() from _rcall_refresh_scene_fade_131
    return False

label ep217_quests_shinyhole8_molly_ashley:
    # Эшли с Молли ругаются в гримерке
    if ep217_quests_shinyhole7_ashley_day == day or get_active_objects("Pub_StripteaseGirl1", scene="pub_makeuproom") == False:
        return
    call ep217_dialogues2_shiny_hole_7() from _rcall_ep217_dialogues2_shiny_hole_7
    $ questHelp("shinyhole_52", True)
    $ questHelp("shinyhole_52c", True)
    $ questHelp("shinyhole_53")
    $ set_active("Tips", False, scene="pub_makeuproom")
    $ set_active("Tips", False, scene="pub_makeuproom_mollytable")

    $ add_talk("Bartender", "ep217_quests_shinyhole9_ashley", scene="pub", label=["shinyhole_quest1_tips3", "shinyhole_quest1_ashley2"], quest="molly_joe_private1")
    $ add_talk("Bartender_Waitress", "ep217_quests_shinyhole9_ashley", scene="pub", label=["shinyhole_quest1_tips3", "shinyhole_quest1_ashley2"], quest="molly_joe_private1")

    $ add_hook("Cloth2", "ep217_dialogues2_shiny_hole_7a", scene="pub_makeuproom", label="shinyhole_quest1_tips3", quest="molly_joe_private1")
    $ add_hook("Teleport_Hostel_Street", "ep217_dialogues2_shiny_hole_7a", scene="pub", label="shinyhole_quest1_tips3", quest="molly_joe_private1", priority=100000)

    $ pub_makeuproom_monica_suffix = 2

    $ remove_hook(label="shinyhole_quest1_tips2")
    $ add_objective("blame_molly", t_("Сказать Эшли, что Молли напала на Монику."), c_red, 155)
    call refresh_scene_fade() from _rcall_refresh_scene_fade_132
    return

label ep217_quests_shinyhole9_ashley:
    # Жалуемся Эшли, что Молли ударила Монику
    call ep217_dialogues2_shiny_hole_8() from _rcall_ep217_dialogues2_shiny_hole_8
    $ remove_hook(label="shinyhole_quest1_tips3")
    $ remove_objective("blame_molly")
    $ questHelp("shinyhole_53", True)
    $ questHelp("shinyhole_54")
    $ ep217_quests_shinyhole9_ashley_day = day
    $ add_talk("Pub_StripteaseGirl1", "ep217_quests_shinyhole10_molly", scene="pub_makeuproom", label="shinyhole_quest1_tips4", quest="molly_joe_private1")
    call change_scene("pub_makeuproom", "Fade_long") from _rcall_change_scene_217
    call refresh_scene_fade() from _rcall_refresh_scene_fade_133
    return False

label ep217_quests_shinyhole10_molly:
    # Заставляем Молли просить прощение
    if ep217_quests_shinyhole9_ashley_day == day:
        return
    if cloth != "StripOutfit1":
        sound snd_fabric1
        fadeblack 2.0
        $ cloth = "StripOutfit1"
        $ cloth_type = "StripOutfit"
    call ep217_dialogues2_shiny_hole_9() from _rcall_ep217_dialogues2_shiny_hole_9
    $ questHelp("shinyhole_54", True)
    $ questHelp("shinyhole_55")
    $ remove_hook(label="shinyhole_quest1_tips4")
    $ add_talk("Pub_StripteaseGirl1", "ep217_quests_shinyhole11_molly", scene="pub_makeuproom", label="shinyhole_quest1_tips5", quest="molly_joe_private1")
    $ ep217_quests_shinyhole10_molly_day = day
    $ move_object("Pub_StripteaseGirl1", "empty")
    $ pub_makeuproom_monica_suffix = 2
    call refresh_scene_fade() from _rcall_refresh_scene_fade_134
    return False

label ep217_quests_shinyhole11_molly:
    # Заставляем ее согласиться на приват с Джо
    if ep217_quests_shinyhole10_molly_day == day:
        return
    if cloth != "StripOutfit1":
        sound snd_fabric1
        fadeblack 2.0
        $ cloth = "StripOutfit1"
        $ cloth_type = "StripOutfit"
    $ remove_hook()
    call ep217_dialogues2_shiny_hole_10() from _rcall_ep217_dialogues2_shiny_hole_10

    $ questHelp("shinyhole_55", True)
    $ questHelp("shinyhole_55a")

    $ set_active("Bartender", True, scene="pub_stage1")
    $ set_active("Stage", False, scene="pub_stage1")
    $ add_talk("Bartender", "ep217_quests_shinyhole11_joe", scene="pub_stage1", label="shinyhole_quest1_tips6", quest="molly_joe_private1")
    $ add_hook("Teleport_Hostel_Street", "ep217_dialogues2_shiny_hole_10a", scene="pub", label="shinyhole_quest1_tips6_block", quest="molly_joe_private1", priority=100000)

    call refresh_scene_fade() from _rcall_refresh_scene_fade_135
    return False

label ep217_quests_shinyhole11_joe:
    # Говорим с Джо около сцены
    $ remove_hook(label="shinyhole_quest1_tips6")
    $ questHelp("shinyhole_55a", True)
    $ questHelp("shinyhole_55a2")
    call ep217_dialogues2_shiny_hole_11() from _rcall_ep217_dialogues2_shiny_hole_11
    $ set_active("Bartender", False, scene="pub_stage1")
    $ set_active("Stage", True, scene="pub_stage1")
    $ add_hook("before_open", "ep217_quests_shinyhole12_ashley_init_after_dance", scene="pub_makeuproom", label="shinyhole_quest1_tips7", quest="molly_joe_private1")
    call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_27
    return False

label ep217_quests_shinyhole12_ashley_init_after_dance:
    # инициализируем разговор с Эшли после танцев
    if monicaDancedLastDay != day: # Если не танцевали, ждем
        return
    $ remove_hook()
    $ remove_hook(label="dialogue_5_dance_strip_18")
    $ questHelp("shinyhole_55a2", True)
    $ questHelp("shinyhole_55b")
    $ autorun_to_object("ep217_dialogues2_shiny_hole_12b", scene="pub_makeuproom")

    $ move_object("Bartender", "empty")
    $ add_hook("Bartender_Waitress", "ep217_quests_shinyhole13_ashley", scene="pub", label=["shinyhole_quest1_tips8"], quest="molly_joe_private1")
    $ add_hook("Teleport_Hostel_Street", "ep217_dialogues2_shiny_hole_12a", scene="pub", label="shinyhole_quest1_tips8", quest="molly_joe_private1")
    return False

label ep217_quests_shinyhole13_ashley:
    # Отвлекаем Эшли
    $ remove_hook(label="shinyhole_quest1_tips8")
    call ep217_dialogues2_shiny_hole_12() from _rcall_ep217_dialogues2_shiny_hole_12
    $ questHelp("shinyhole_55b", True)
    if cloth != "StripOutfit1":
        sound snd_fabric1
        fadeblack 2.0
        $ cloth = "StripOutfit1"
        $ cloth_type = "StripOutfit"
    $ questHelp("shinyhole_56")

    call ep217_dialogues2_shiny_hole_13() from _rcall_ep217_dialogues2_shiny_hole_13 # Приват Молли для Джо
    $ remove_hook(quest="molly_joe_private1")
    $ questHelp("shinyhole_56", True)
    $ questHelp("shinyhole_57")
    $ questHelp("shinyhole_57a")

    $ move_object("Bartender", "pub")
    $ add_hook("Teleport_Pub", "ep217_quests_shinyhole14_joe_after_private", scene="pub_makeuproom", label="molly_joe_private1_after")
    $ add_talk("Pub_StripteaseGirl2", "ep217_quests_shinyhole15_claire_after_private", scene="pub_makeuproom", label="molly_joe_private1_after")
    $ add_talk("Pub_StripteaseGirl1", "ep217_quests_shinyhole16_molly_after_private", scene="pub_makeuproom", label="molly_joe_private1_after")
    $ ep217_quests_ashley_tips_dialogue_planned = True
    $ remove_hook(label="shinyhole_quest1_tips6_block")

    call change_scene("pub_makeuproom", "Fade_long") from _rcall_change_scene_218

    return False

label ep217_quests_shinyhole14_joe_after_private:
    # разговор с Джо после привата Молли
    if monicaDancedLastDay != day or cloth != "Whore":
        return
    $ remove_hook()
    call ep217_dialogues2_shiny_hole_15() from _rcall_ep217_dialogues2_shiny_hole_15
    return


label ep217_quests_shinyhole15_claire_after_private:
    $ remove_hook()
    if cloth != "StripOutfit1":
        sound snd_fabric1
        fadeblack 2.0
        $ cloth = "StripOutfit1"
        $ cloth_type = "StripOutfit"
    call ep217_dialogues2_shiny_hole_16() from _rcall_ep217_dialogues2_shiny_hole_16
    $ pub_makeuproom_monica_suffix = 2
    $ ep217_quests_shinyhole15_claire_after_private_day = day
    $ questHelp("shinyhole_57", True)
    $ add_char_progress("Pub_StripteaseGirl2", 50, "ep217_quests_shinyhole15_claire_after_private")
    $ add_talk("Pub_StripteaseGirl2", "ep217_dialogues2_shiny_hole_18", scene="pub_makeuproom", label="molly_joe_private1_after")
    call ep218_quests_shinyhole_check() from _rcall_ep218_quests_shinyhole_check
    call refresh_scene_fade() from _rcall_refresh_scene_fade_136
    return False

label ep217_quests_shinyhole16_molly_after_private:
    if cloth != "Whore" and ep217_quests_shinyhole16_molly_after_private_flag == False:
        sound snd_fabric1
        fadeblack 2.0
        $ cloth = "Whore"
        $ cloth_type = "Whore"
    if cloth != "Whore":
        return
    $ ep217_quests_shinyhole16_molly_after_private_flag = True
    $ ep217_quests_shinyhole16_molly_after_private_day = day
    call ep217_dialogues2_shiny_hole_17() from _rcall_ep217_dialogues2_shiny_hole_17
    $ add_char_progress("Pub_StripteaseGirl1", 50, "ep217_quests_shinyhole16_molly_after_private")
    $ questHelp("shinyhole_57a", True)
    call ep218_quests_shinyhole_check() from _rcall_ep218_quests_shinyhole_check_1
    call refresh_scene_fade() from _rcall_refresh_scene_fade_137
    return False




#
