label bed_management:
    call ep01_dialogues2_day1_family_3a()
    if _return == 0:
        return
    if _return == 1:
        call changeDayTime("afternoon")
        call refresh_scene_fade_long()
        return
    if _return == 2:
        call changeDayTime("evening")
        call refresh_scene_fade_long()
        return
    if _return == 3:
        call changeDayTime("night")
        call refresh_scene_fade_long()
        return
    if _return == 4:
        call changeDayTime("morning")
        call refresh_scene_fade_long()
        return
    return
