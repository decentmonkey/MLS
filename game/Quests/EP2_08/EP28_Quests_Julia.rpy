default juliaQuestStage1_Progress = 0
default juliaQuestMonicaRefusedFred = False # Моника отказала Фреду в продолжении квестов Юлии

label ep28_quests_julia_fred_catch1: # Фред ловит Монику на входе #1
    music stop
    sound snd_lift
    pause 1.0
    call ep28_dialogues6_julia_1() from _call_ep28_dialogues6_julia_1
    music stop
    img black_screen
    with diss
    pause 1.0
    if _return == False:
        $ remove_objective("find_julia_panties_color")
        $ juliaQuestMonicaRefusedFred = True
        $ remove_hook(label="ep29_quests_julia3_workers")
    else:
        $ juliaQuestStage1_Progress = 1
    $ move_object("Melanie", "empty")
    call change_scene("monica_office_makeup_room") from _call_change_scene_385
    $ add_hook("enter_scene", "ep27_dialogues6_julia10a", scene="monica_office_makeup_room", once=True)
    return

label ep28_quests_julia_panties_menu:
    call ep28_dialogues6_julia_9() from _call_ep28_dialogues6_julia_9
    if _return == 0:
        return
    if _return == 1: # Искать флешку
        call ep28_dialogues6_julia_2() from _call_ep28_dialogues6_julia_2
        $ juliaQuestLastDay = day
        if _return == True:
            $ juliaQuestStage1_Progress = 2
        $ workingOfficeCabinetMonicaSuffix = 2
        call refresh_scene_fade() from _call_refresh_scene_fade_176
        return
    if _return == 2: # Достать с полки документы
        call ep28_dialogues6_julia_3() from _call_ep28_dialogues6_julia_3
        $ juliaQuestLastDay = day
        if _return == True:
            if juliaQuestStage1_Progress <= 2:
                $ add_hook("before_open", "ep28_quests_julia_fred_catch2", scene="monica_office_entrance", recursive=True, label="ep28_quests_julia1_a", priority=1000)
                $ juliaFredCatchFromDay = day
        $ workingOfficeCabinetMonicaSuffix = 2
        call refresh_scene_fade() from _call_refresh_scene_fade_177
        return
    if _return == 3: # Залезть под стол
        call ep28_dialogues6_julia_5() from _call_ep28_dialogues6_julia_5
        $ juliaQuestLastDay = day
        if _return == True:
            if juliaQuestStage1_Progress <= 3:
                $ add_hook("before_open", "ep28_quests_julia_fred_catch3", scene="monica_office_entrance", recursive=True, label="ep28_quests_julia1_b", priority=1000)
                $ juliaFredCatchFromDay = day
        $ workingOfficeCabinetMonicaSuffix = 2
        call refresh_scene_fade() from _call_refresh_scene_fade_178
        return
    if _return == 4: # Показать Юлии трусики Юлии :)
        call ep28_dialogues6_julia_7() from _call_ep28_dialogues6_julia_7
        $ juliaQuestLastDay = day
        if _return == True:
            if juliaQuestStage1_Progress <= 4:
                $ add_hook("before_open", "ep28_quests_julia_fred_catch4", scene="monica_office_entrance", recursive=True, label="ep28_quests_julia1_c", priority=1000)
                $ juliaFredCatchFromDay = day
        $ workingOfficeCabinetMonicaSuffix = 2
        call refresh_scene_fade() from _call_refresh_scene_fade_179
        return
    if _return == 5: #Заставить Юлию включить неработающий компьютер
        call ep29_quests_julia1() from _call_ep29_quests_julia1
        return
    if _return == 6: #Заставить Юлию принести горячий кофе
        call ep29_quests_julia2() from _call_ep29_quests_julia2
        return
    if _return == 7: #Есть же подчиненные. Поручить им выполнить просьбу Фреда
        call ep29_quests_julia3() from _call_ep29_quests_julia3
        return
    return

label ep28_quests_julia_fred_catch2: # Фред ловит Монику на входе #2
    if juliaFredCatchFromDay == day or week_day == 7 or day_time != "day" or scene_name == "monica_office_entrance":
        return
    $ remove_hook(label="ep28_quests_julia1_a")
    music stop
    sound snd_lift
    pause 1.0
    call ep28_dialogues6_julia_4() from _call_ep28_dialogues6_julia_4
    music stop
    img black_screen
    with diss
    pause 1.0
    if _return == False:
        $ juliaQuestMonicaRefusedFred = True
        $ remove_objective("find_julia_panties_color")
        $ remove_hook(label="ep29_quests_julia3_workers")
    else:
        $ juliaQuestStage1_Progress = 3
    $ move_object("Melanie", "empty")
    call change_scene("monica_office_makeup_room") from _call_change_scene_386
    $ add_hook("enter_scene", "ep27_dialogues6_julia11a", scene="monica_office_makeup_room", once=True)
    return

label ep28_quests_julia_fred_catch3: # Фред ловит Монику на входе #3
    if juliaFredCatchFromDay == day or week_day == 7 or day_time != "day" or scene_name == "monica_office_entrance":
        return
    $ remove_hook(label="ep28_quests_julia1_b")
    music stop
    sound snd_lift
    pause 1.0
    call ep28_dialogues6_julia_6() from _call_ep28_dialogues6_julia_6
    music stop
    img black_screen
    with diss
    pause 1.0
    if _return == False:
        $ juliaQuestMonicaRefusedFred = True
        $ remove_objective("find_julia_panties_color")
        $ remove_hook(label="ep29_quests_julia3_workers")
    else:
        $ juliaQuestStage1_Progress = 4
    call change_scene("monica_office_secretary_teatable") from _call_change_scene_387
    $ add_hook("enter_scene", "ep27_dialogues6_julia10a", scene="monica_office_makeup_room", once=True)
    return

label ep28_quests_julia_fred_catch4: # Фред ловит Монику на входе #4
    if juliaFredCatchFromDay == day or week_day == 7 or day_time != "day" or scene_name == "monica_office_entrance":
        return
    $ remove_hook(label="ep28_quests_julia1_c")
    music stop
    sound snd_lift
    pause 1.0
    call ep28_dialogues6_julia_8() from _call_ep28_dialogues6_julia_8
    music stop
    img black_screen
    with diss
    pause 1.0
    if _return == False:
        $ juliaQuestMonicaRefusedFred = True
        $ remove_objective("find_julia_panties_color")
        $ remove_hook(label="ep29_quests_julia3_workers")
    else:
        $ juliaQuestStage1_Progress = 5
    call change_scene("monica_office_photostudio") from _call_change_scene_388
    $ add_hook("enter_scene", "ep27_dialogues6_julia11a", scene="monica_office_photostudio", once=True)
    return


#ep28_dialogues6_julia_1 - фред начало
#ep28_dialogues6_julia_2 - флешка
#ep28_dialogues6_julia_3 - полка
#


#
