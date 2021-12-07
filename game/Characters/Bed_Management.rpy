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
