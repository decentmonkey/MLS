init python:
    def changeDayTime(dayTime):
        global day_time, day_suffix, day, week_day, scene_name
        if dayTime == day_time:
            return
        if dayTime == "evening":
            day_time = "evening"
            day_suffix = "_Evening"
            renpy.call("changeDayTime_evening_hooks")
            return
        if dayTime == "day":
            day_time = "day"
            day_suffix = ""
            day = day + 1
            week_day = (day)%7
            if week_day == 0:
                week_day = 7
            if week_day == 6:
                renpy.free_memory()

            renpy.call("changeDayTime_day_hooks")
            return
        return

    def getNextDayByWeekDay(target_week_day): #найти дату для следующего дня недели
        if target_week_day == week_day:
            return day + 7
        if target_week_day < week_day:
            return day + 7 - week_day + target_week_day
        if target_week_day > week_day:
            return day + target_week_day - week_day
        return

    def get_scene_label(scene_label):
        global sceneStages
        for idx in reversed(range(0, len(sceneStages))):
            if renpy.has_label(scene_label + sceneStages[idx]):
                return scene_label + sceneStages[idx]
        return scene_label

    def checkTimeDay():
        return day_time == "day"

    def setDayTimeVars():
        global day_time, day_time_idx, day_suffix
        if day_time_idx == 0:
            day_time = "morning"
            day_suffix = ""
        if day_time_idx == 1:
            day_time = "day"
            day_suffix = ""
        if day_time_idx == 2:
            day_time = "evening"
            day_suffix = "_Evening"
        if day_time_idx == 3:
            day_time = "night"
            day_suffix = "_Evening"
        return

label changeDayTime(new_day_time):
    if new_day_time == day_time:
        return
    $ day_time_idx += 1
    if day_time_idx > 3:
        $ day_time_idx = 0
        $ day += 1
        $ week_day = (day)%7
        if week_day == 0:
            $ week_day = 7
        if week_day == 6:
            $ renpy.free_memory()
    $ setDayTimeVars()
    call expression "changeDayTime_" + day_time + "_hooks"
    if day_time == new_day_time:
        return
    if _return == False:
        return False

    $ day_time_idx += 1
    if day_time_idx > 3:
        $ day_time_idx = 0
        $ day += 1
        if week_day == 0:
            $ week_day = 7
        if week_day == 6:
            $ renpy.free_memory()
    $ setDayTimeVars()
    call expression "changeDayTime_" + day_time + "_hooks"
    if day_time == new_day_time:
        return
    if _return == False:
        return False

    $ day_time_idx += 1
    if day_time_idx > 3:
        $ day_time_idx = 0
        $ day += 1
        if week_day == 0:
            $ week_day = 7
        if week_day == 6:
            $ renpy.free_memory()
    $ setDayTimeVars()
    call expression "changeDayTime_" + day_time + "_hooks"
    if day_time == new_day_time:
        return
    if _return == False:
        return False

    $ day_time_idx += 1
    if day_time_idx > 3:
        $ day_time_idx = 0
        $ day += 1
        if week_day == 0:
            $ week_day = 7
        if week_day == 6:
            $ renpy.free_memory()
    $ setDayTimeVars()
    call expression "changeDayTime_" + day_time + "_hooks"
    if day_time == new_day_time:
        return
    if _return == False:
        return False
    return

label changeDayTime_morning_hooks:
    $ remove_hook(label="evening_time_temp")
    call process_hooks("change_day_time", "global") from _rcall_process_hooks
    call process_hooks("morning_" + str(day), "global_day") from _rcall_process_hooks_1
    if _return == False:
        return False
    call process_hooks("week_morning_" + str(week_day), "global_week_day") from _rcall_process_hooks_2
    if _return == False:
        return False
    call process_hooks("change_time_morning_global", "global") from _rcall_process_hooks_3
    if _return == False:
        return False
    call process_hooks("change_time_morning", "global") from _rcall_process_hooks_4
    if _return == False:
        return False
    return

label changeDayTime_day_hooks:
    $ remove_hook(label="morning_time_temp")
    call process_hooks("change_day_time", "global") from _rcall_process_hooks_5
    call process_hooks("day_" + str(day), "global_day") from _rcall_process_hooks_6
    if _return == False:
        return False
    call process_hooks("week_day_" + str(week_day), "global_week_day") from _rcall_process_hooks_7
    if _return == False:
        return False
    call process_hooks("change_time_day_global", "global") from _rcall_process_hooks_8
    if _return == False:
        return False
    call process_hooks("change_time_day", "global") from _rcall_process_hooks_9
    if _return == False:
        return False
    return
label changeDayTime_evening_hooks:
    $ remove_hook(label="day_time_temp")
    call process_hooks("change_day_time", "global") from _rcall_process_hooks_10
    call process_hooks("evening_" + str(day), "global_day") from _rcall_process_hooks_11
    if _return == False:
        return False
    call process_hooks("week_evening_" + str(week_day), "global_week_day") from _rcall_process_hooks_12
    if _return == False:
        return False
    call process_hooks("change_time_evening_global", "global") from _rcall_process_hooks_13
    if _return == False:
        return False
    call process_hooks("change_time_evening", "global") from _rcall_process_hooks_14
    if _return == False:
        return False
    return

label changeDayTime_night_hooks:
    $ remove_hook(label="evening_time_temp")
    call process_hooks("change_day_time", "global") from _rcall_process_hooks_15
    call process_hooks("night_" + str(day), "global_day") from _rcall_process_hooks_16
    if _return == False:
        return False
    call process_hooks("week_night_" + str(week_day), "global_week_day") from _rcall_process_hooks_17
    if _return == False:
        return False
    call process_hooks("change_time_night_global", "global") from _rcall_process_hooks_18
    if _return == False:
        return False
    call process_hooks("change_time_night", "global") from _rcall_process_hooks_19
    if _return == False:
        return False
    return
