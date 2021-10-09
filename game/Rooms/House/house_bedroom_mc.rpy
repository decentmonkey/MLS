label house_bedroom_mc:
    $ miniMapData = []
    call miniMapHouseGenerate() from _rcall_miniMapHouseGenerate_3
    $ scene_image = "scene_House_Bedroom_MC[day_suffix]"
    return

label house_bedroom_mc_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Bed", {"type" : 2, "base" : "House_Bedroom_MC_Bed", "click" : "house_bedroom_mc_environment", "actions" : "l", "zorder":10, "b":0.2}, scene="house_bedroom_mc")
#    $ add_object_to_scene("Typewriter", {"type" : 2, "base" : "House_Bedroom_MC_Typewriter", "click" : "house_bedroom_mc_environment", "actions" : "l", "zorder":10}, scene="house_bedroom_mc")
    $ add_object_to_scene("Table", {"type" : 2, "base" : "House_Bedroom_MC_Table", "click" : "house_bedroom_mc_environment", "actions" : "lw", "zorder":10}, scene="house_bedroom_mc")

    $ add_object_to_scene("Teleport_Floor2", {"type":3, "text" : t_("ЛЕСТНИЦА ВНИЗ"), "larrow" : "arrow_down_2_a", "base":"House_Bedroom_MC_Teleport_Floor2", "click" : "house_bedroom_mc_environment", "xpos" : 633, "ypos" : 954, "zorder":11, "teleport":True, "group":"teleports"}, scene="house_bedroom_mc")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label house_bedroom_mc_environment:
    if obj_name == "Teleport_Floor2":
        call change_scene("house_floor2") from _rcall_change_scene_85
        return
    if obj_name == "Bed":
        call bed_management() from _rcall_bed_management
        return

    if obj_name == "Table":
        if act=="l":
            call ep01_dialogues2_day1_family_1_3() from _rcall_ep01_dialogues2_day1_family_1_3
            return
        call change_scene("house_bedroom_mc_tablenear") from _rcall_change_scene_86
        return
    return
