default bed_sleep_time = 2 # время, когда можно ложиться спать (2-вечер, 3-ночь)

label bed_management:
    call ep01_dialogues2_day1_family_3a() from _rcall_ep01_dialogues2_day1_family_3a
    if _return == 0:
        return
    if _return == 1:
        call changeDayTime("afternoon") from _rcall_changeDayTime
        call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long
        return
    if _return == 2:
        call changeDayTime("evening") from _rcall_changeDayTime_1
        call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_1
        return
    if _return == 3:
        call changeDayTime("night") from _rcall_changeDayTime_2
        call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_2
        return
    if _return == 4:
        call changeDayTime("morning") from _rcall_changeDayTime_3
        call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_3
        return
    return

label bed_sleep1:
    if day_time_idx < bed_sleep_time:
        call ep01_dialogues2_day1_family_1_1() from _rcall_ep01_dialogues2_day1_family_1_1
        return False
    $ house_bedroom_mc_onbed_suffix = 1
    $ add_hook("enter_scene", "bed_sleep1_bed", scene="house_bedroom_mc_onbed", label="get_sleep", once=True)
    call change_scene("house_bedroom_mc_onbed", "Fade_long", "put_dress") from _rcall_change_scene_149

    return False

label bed_sleep1_bed:
    call process_hooks("before_sleep", "global") from _rcall_process_hooks_55
    if _return == False:
        return
    call ep01_dialogues2_day1_family_3b() from _rcall_ep01_dialogues2_day1_family_3b
    if _return == False:
        return
    call process_hooks("before_sleep_actions", "global") from _rcall_process_hooks_56
    if _return != False:
        call process_hooks("sleep", "global") from _rcall_process_hooks_57
    return

label bed_sleep1_bedsleep1:
    call process_hooks("sleep", "global") from _rcall_process_hooks_58
    return

label bed_sleep1_bedsleep2:
    fadeblack 1.5
    call changeDayTime("morning") from _rcall_changeDayTime_35
    $ house_bedroom_mc_onbed_suffix = 2
    call process_hooks("after_sleep", "global") from _rcall_process_hooks_59
    if _return == False:
        return
    call refresh_scene_fade() from _rcall_refresh_scene_fade_39
    return

