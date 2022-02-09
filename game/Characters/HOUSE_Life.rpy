default sister1RoomDoorLocked = False
default sister2RoomDoorLocked = False
default landLordRoomDoorLocked = False
default bathroomDoorLocked = False
default houseLifeStage = 0

# houseLifeStage == 1 - никого нет, все открыто, кроме спальни
# houseLifeStage == 2 - все дома, все закрыто
label house_life:

    if day_time_idx == 0:
        # утро
        python:
            # Синтия
            move_object("Sister2", "house_bathroom")
            houseBathroomSister2Suffix = renpy.random.randint(1, 5)
            sister2RoomDoorLocked = False

            # Оливия
            move_object("Sister1", "house_sister1")
            houseSister1_Sister1Suffix = renpy.random.randint(1, 4)
            sister1RoomDoorLocked = True

            # Софи
            move_object("Sophie", "house_kitchen")
            landLordRoomDoorLocked = False

            # Генри
            move_object("Henry", "empty")

        return

    if day_time_idx == 1:
        # день
        python:
            # Синтия
            move_object("Sister2", "college_coridor1")
            sister2RoomDoorLocked = False

            # Оливия
            rand1 = renpy.random.randint(1, 3)
            if rand1 <= 2: # Оливия в комнате
                move_object("Sister1", "house_sister1")
                houseSister1_Sister1Suffix = renpy.random.randint(1, 4)
                sister1RoomDoorLocked = False
            if rand1 > 2: # Оливия в душе
                move_object("Sister1", "house_bathroom")
                houseBathroomSister1Suffix = renpy.random.randint(1, 4)
                sister1RoomDoorLocked = False

            # Софи
            rand1 = renpy.random.randint(1, 3)
            if rand1 == 1: # Софи в гостиной
                move_object("Sophie", "house_livingroomhall")
                houseLivingRoomSophieSuffix = renpy.random.randint(1, 4)
                landLordRoomDoorLocked = False
            if rand1 == 2: # Софи в спальне
                move_object("Sophie", "house_bedroom_landlord")
                houseBedroomLandlordSophieSuffix = renpy.random.randint(1, 3)
                landLordRoomDoorLocked = False
            if rand1 == 3: # Софи на кухне
                move_object("Sophie", "house_kitchen")
                houseKitchenSophieSuffix = renpy.random.randint(1, 3)
                landLordRoomDoorLocked = False

            # Генри
            move_object("Henry", "empty")


    if day_time_idx == 2:
        # вечер
        python:
            # Синтия
            move_object("Sister2", "house_sister2")
            houseSister2_Sister2Suffix = renpy.random.randint(1, 3)
            sister2RoomDoorLocked = False

            # Оливия
            move_object("Sister1", "house_sister1")
            houseSister1_Sister1Suffix = renpy.random.randint(1, 3)
            sister1RoomDoorLocked = False

            # Софи
            move_object("Sophie", "house_kitchen")
            houseKitchenSophieSuffix = renpy.random.randint(1, 3)
            landLordRoomDoorLocked = False

            # Генри
            move_object("Henry", "house_livingroomhall")
            houseLivingRoomFatherSuffix = renpy.random.randint(1, 3)

    if day_time_idx == 3:
        # ночь
        python:
            # Синтия
            move_object("Sister2", "house_sister2")
            houseSister2_Sister2Suffix = renpy.random.randint(1, 3)
            sister2RoomDoorLocked = True

            # Оливия
            move_object("Sister1", "house_bathroom")
            houseBathroomSister1Suffix = renpy.random.randint(1, 4)
            sister1RoomDoorLocked = False

            # Софи
            move_object("Sophie", "house_bedroom_landlord")
            houseBedroomLandlordSophieSuffix = renpy.random.randint(1, 3)
            landLordRoomDoorLocked = True

            # Генри
            move_object("Henry", "house_bedroom_landlord")
            houseBedroomLandlordHenrySuffix = renpy.random.randint(1, 3)

    if houseLifeStage == 1:
        python:
            move_object("Sister1", "empty")
            move_object("Sister2", "empty")
            move_object("Sophie", "empty")
            sister1RoomDoorLocked = False
            sister2RoomDoorLocked = False
            landLordRoomDoorLocked = True
        return
    if houseLifeStage == 2:
        python:
            move_object("Sister1", "house_sister1")
            move_object("Sister2", "house_sister2")
            move_object("Sophie", "house_bedroom_landlord")
            sister1RoomDoorLocked = True
            sister2RoomDoorLocked = True
            landLordRoomDoorLocked = True
        return

    return
