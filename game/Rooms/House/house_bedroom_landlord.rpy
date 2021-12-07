default houseBedroomLandlordSophieSuffix = 1
default houseBedroomLandlordHenrySuffix = 1

label house_bedroom_landlord:
    $ miniMapData = []
    call miniMapHouseGenerate() from _rcall_miniMapHouseGenerate_2
    $ scene_image = "scene_House_Bedroom_Landlord[day_suffix]"
    return

label house_bedroom_landlord_init:
    $ default_tint = [1.0, 1.0, 1.0]
    $ add_object_to_scene("Sophie", {"type" : 2, "base" : "House_Bedroom_Landlord[day_suffix]_Mother_[houseBedroomLandlordSophieSuffix]", "click" : "house_bedroom_landlord_environment", "actions" : "l", "zorder":10}, scene="house_bedroom_landlord")
    $ add_object_to_scene("Henry", {"type" : 2, "base" : "House_Bedroom_Landlord[day_suffix]_Henry_[houseBedroomLandlordHenrySuffix]", "click" : "house_bedroom_landlord_environment", "actions" : "l", "zorder":10}, scene="house_bedroom_landlord")

    $ add_object_to_scene("Teleport_Floor2", {"type":3, "text" : t_("НАЗАД"), "larrow" : "arrow_left_2", "base":"House_Bedroom_Landlord_Teleport_Floor2", "click" : "house_bedroom_landlord_environment", "xpos" : 334, "ypos" : 972, "zorder":11, "teleport":True, "group":"teleports"}, scene="house_bedroom_landlord")
    return

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label house_bedroom_landlord_environment:
    if obj_name == "Teleport_Floor2":
        call change_scene("house_floor2", "Fade", "snd_door_close1") from _rcall_change_scene_84
        return
    return
