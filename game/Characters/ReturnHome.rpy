default returnHomeInProcess = False
default returnHomeTick = 0

label returnHomeButton:
    call process_hooks("return_home", "global") from _rcall_process_hooks_20
    if _return == False:
        sound click_denied
        return

    if map_objects.has_key("Teleport_HOUSE") and map_objects["Teleport_HOUSE"]["state"] != "visible" and map_objects["Teleport_HOUSE"]["state"] != "active":
        sound click_denied
        return
    $ returnHomeInProcess = True
    $ returnHomeTick = pause_enter
    $ scene_refresh_flag = True
    $ show_scene_loop_flag = True
    imgd black_screen
    call process_change_map_location("HOUSE") from _rcall_process_change_map_location
    $ add_hook("before_open", "returnHomeButton_step1", scene="house_street", label="return_home_process", priority = -1)
    call change_scene("house_street", "Fade", False) from _rcall_change_scene
    return

label returnHomeButton_step1:
    if returnHomeTick != pause_enter:
        $ remove_hook(label="return_home_process")
        return
    $ add_hook("before_open", "returnHomeButton_step2", scene="house_floor1", label="return_home_process", priority = -1)
    call change_scene("house_floor1", "Fade", False) from _rcall_change_scene_1
    return

label returnHomeButton_step2:
    if returnHomeTick != pause_enter:
        $ remove_hook(label="return_home_process")
        return
    $ add_hook("before_open", "returnHomeButton_step3", scene="house_floor2", label="return_home_process", priority = -1)
    call change_scene("house_floor2", "Fade", False) from _rcall_change_scene_2
    return

label returnHomeButton_step3:
    if returnHomeTick != pause_enter:
        $ remove_hook(label="return_home_process")
        return
    call change_scene("house_bedroom_mc", "Fade_long") from _rcall_change_scene_3
    return
