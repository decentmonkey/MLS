define debugMode = True

default gameStage = 0
default gameSubStage = 0
default afterJail = False
default rain = False
default rainIntencity = 0
default lightning = False
default sceneIsStreet = False
default hudDaySkipToEveningEnabled = True
default objectives_list = []
default currentMusic = False
default currentMusicPriority = 0
default currentMusic2 = False
default currentMusic3 = False
default storedMusic = []
default storedMusicPriority = []
default day_time = "day"
default day = 0
default week_day = 1
default owner = "Monica"
default showObjectsNotOwner = True
default episode = 1
default notifList = []
default lastNotifTime = 0

default menu_corruption = []
default menu_price = []
default menu_bitchiness = []
default menu_required = {}

default hud_preset_current = "default"
default hud_preset_default = "default"
default minimap_coords_preset = 0
default blur_effect = False

default after_load_ready_to_render = False
default nextFriday = -1

default act = ""

default episode2part = 1
default episode2part2_initialized = False
default episode2full = False

default questLogGlobalEnabled = False

label start: #for blink here

    #new game
    $ after_load_ready_to_render = True
    $ refresh_list_files_forced()
    $ episode = 2
#    $ debugMode = True

    $ day = 231
    $ scenes_data = {"objects": {}, "substs" : {}, "autorun": {}, "hooks": {}}
    $ hooks_stack = []
    $ inventory_objects = {}
    $ inventory = []
    $ owner = "Monica"
    call game_init() from _rcall_game_init

    $ episode2part2_initialized = True
    $ scenes_data = json.loads(renpy.file("ep2_part2_init_data.json").read())
    $ objectives_list = []
    $ add_objective("freedom", t_("Избежать наказания"), c_red, 0)
    $ define_inventory_object("flash_card", {"description" : t_("Флеш Карта"), "label_suffix" : "_use_flash_card", "default_label" : False, "default_nolabel" : "cant_use", "icon" : "Inventory/flash_card" + res.suffix + ".png"})
    $ add_inventory("flash_card", 1, False)
    $ define_inventory_object("keys_apartments", {"description" : t_("Ключи от дома в трущобах"), "label_suffix" : "_use_keys_apartments", "default_label" : False, "default_nolabel" : "cant_use", "icon" : "Inventory/keys_apartments" + res.suffix + ".png"})
    $ map_objects = {
            "Teleport_Monica_Office" : {"text" : t_("ОФИС МОНИКИ"), "xpos" : 882, "ypos" : 320, "base" : "map_marker", "state" : "visible"},
            "Teleport_Street_Corner" : {"text" : t_("УГОЛ УЛИЦЫ"), "xpos" : 124, "ypos" : 476, "base" : "map_marker", "state" : "visible"},
            "Teleport_Dick_Office" : {"text" : t_("ОФИС ДИКА"), "xpos" : 1370, "ypos" : 127, "base" : "map_marker", "state" : "visible"},
            "Teleport_Gas_Station" : {"text" : t_("ЗАПРАВКА"), "xpos" : 1125, "ypos" : 910, "base" : "map_marker", "state" : "visible"},
            "Teleport_Police" : {"text" : t_("ПОЛИЦИЯ"), "xpos" : 912, "ypos" : 809, "base" : "map_marker", "state" : "visible"},
            "Teleport_Rich_Hotel" : {"text" : t_("ОТЕЛЬ ЛЯ ГРАНД"), "xpos" : 1782, "ypos" : 593, "base" : "map_marker", "state" : "visible"},
            "Teleport_Fitness" : {"text" : t_("ФИТНЕСС"), "xpos" : 356, "ypos" : 411, "base" : "map_marker", "state" : "visible"},
            "Teleport_Steve_Office" : {"text" : t_("ОФИС СТИВА"), "xpos" : 1333, "ypos" : 724, "base" : "map_marker", "state" : "visible"},
            "Teleport_Bank" : {"text" : t_("БАНК"), "xpos" : 1212, "ypos" : 439, "base" : "map_marker", "state" : "visible"},
            "Teleport_Cloth_Shop" : {"text" : t_("МАГАЗИН ОДЕЖДЫ"), "xpos" : 340, "ypos" : 901, "base" : "map_marker", "state" : "visible"},
            "Teleport_Street_Corner" : {"text" : t_("УГОЛ УЛИЦЫ"), "xpos" : (88+15), "ypos" : 942, "base" : "map_marker", "state" : "visible"},
            "Teleport_Hostel2" : {"text" : t_("ГРЯЗНАЯ УЛИЦА"), "xpos" : 259, "ypos" : 1046, "base" : "map_marker", "state" : "visible"},
            "Teleport_House" : {"text" : t_("ДОМ МОНИКИ"), "xpos" : 105, "ypos" : 798, "base" : "map_marker_house", "state" : "active"},
            "Teleport_Melanie_Home" : {"text" : t_("АПАРТАМЕНТЫ МЕЛАНИ"), "xpos" : 1726, "ypos" : 791, "base" : "map_marker", "state" : "visible"},
            "Teleport_College" : {"text" : t_("КОЛЛЕДЖ"), "xpos" : 174, "ypos" : 579, "base" : "map_marker", "state" : "visible"},
            "Teleport_PhilipHome" : {"text" : t_("ДОМ ФИЛИППА"), "xpos" : 1767, "ypos" : 242, "base" : "map_marker", "state" : "visible"},
            "Teleport_JuliaHome" : {"text" : t_("ДОМ ЮЛИИ"), "xpos" : 521, "ypos" : 1014, "base" : "map_marker", "state" : "visible"},
            "Teleport_Slums_Apartments" : {"text" : t_("ДОМ В ТРУЩОБАХ"), "xpos" : 408, "ypos" : 728, "base" : "map_marker", "state" : "visible"},
            "Teleport_VictoriaHome" : {"text" : t_("АПАРТАМЕНТЫ ВИКТОРИИ"), "xpos" : 1403, "ypos" : 260, "base" : "map_marker", "state" : "visible"}
    }

    call characters_init() from _rcall_characters_init_1
    call characters_pub_init() from _rcall_characters_pub_init_2
    call characters_pub_init2() from _rcall_characters_pub_init2_2
    call characters_init_julia() from _rcall_characters_init_julia_1
    $ char_info["ReceptionGirl"]["enabled"] = True
    $ char_info["ReceptionGirl"]["caption"] = t_("Сутенерша в Le Grand.")
    $ char_info["Pub_StripteaseGirl1"]["name"] = t_("Молли")
    $ char_info["Pub_StripteaseGirl2"]["name"] = t_("Клэр")
    $ char_info["Rebecca"]["enabled"] = True
    $ char_info["Stephanie"]["enabled"] = True

#########

    call ep01_dialogues1_start_1a() # пляж, показываем геймплей
    call ep01_dialogues1_start_1b() # подглядывание за Оливией и Марком
    call ep01_dialogues1_start_2() # поезд
    call ep01_dialogues1_start_3() # вокзал

    call ep01_dialogues2_day1_family_1() # комната Барди перед ужином
    call ep01_dialogues2_day1_family_2() # кухня, ужин с семьей
    call ep01_dialogues2_day1_family_3() # комната Барди, вечер, клик на кровать (меню)
    call ep01_dialogues2_day1_family_4() # вечером на кухне, клик на Софи
    call ep01_dialogues2_day1_family_4_1() # повторный клик на Софи после разговора с ней
    call ep01_dialogues2_day1_family_5() # вечером в гостиной, клик на Генри
    call ep01_dialogues2_day1_family_6() # попытка зайти в комнату старшей Оливии вечером
    call ep01_dialogues2_day1_family_7() # попытка зайти в комнату младшей Синтии
    call ep01_dialogues2_day1_family_8() # комната Барди, при выборе пункта меню "Лечь спать"

    call ep01_dialogues3_day2_family_1() # комната Барди, утро, перед колледжем
    call ep01_dialogues3_day2_family_2() # клик на душ утром, в душе младшая сестра Синтия
    call ep01_dialogues3_day2_family_4() # до колледжа, Софи на кухне, разговор с ней
    call ep01_dialogues3_day2_family_5() # при повторном клике на Софи утром, если уже разговаривали

    call ep01_dialogues3_day2_college_1() # Барди пришел в колледж
    call ep01_dialogues3_day2_college_5() # приемная директора
    call ep01_dialogues3_day2_college_8() # второй этаж, в поисках кабинета инглиша, встреча с информатичкой
    call ep01_dialogues3_day2_college_9() # урок английского, начало
    call ep01_dialogues3_day2_college_10() # урок английского, конец
    call ep01_dialogues3_day2_college_11() # мысли возле колледжа
    call ep01_dialogues3_day2_college_14() # пришел к Шону
    call ep01_dialogues3_day2_college_15() # после того, как вышел от Шона
    call ep01_dialogues3_day2_college_15a() # телефон Барди, клик на строку контакта "sophie"
    call ep01_dialogues3_day2_college_16() # телефон Барди, клик на строку контакта "cynthia"
    call ep01_dialogues3_day2_college_17() # телефон Барди, клик на строку контакта "sean"

    call ep01_dialogues3_day2_family_6() # Барди приходит после колледжа, ужин с Софи и Генри
    call ep01_dialogues3_day2_family_7() # ночь, Барди ложится спать (подглядывание за Оливией + мечты)

#########


    python:
        # Betty
        char_info["Betty"]["level"] = 6
        char_info["Betty"]["current_progress"] = 0
        char_info["Betty"]["caption"] = t_("Бетти привыкла к гувернантке и не так строго следит за ней.")
        char_info["Betty"]["enabled"] = True

        char_info["Ralph"]["level"] = 2
        char_info["Ralph"]["current_progress"] = 0
        char_info["Ralph"]["caption"] = t_("Ральф привык к регулярному сексу с гувернанткой...")
        char_info["Ralph"]["enabled"] = True

        #char_info["Ralph"]["level"] = 1
        #char_info["Ralph"]["current_progress"] = 0
        #char_info["Ralph"]["caption"] = t_("Ральф примерный семьянин.")

        char_info["Bardie"]["level"] = 6
        char_info["Bardie"]["current_progress"] = 0
        char_info["Bardie"]["caption"] = t_("Барди считает Монику своей игрушкой.")
        char_info["Bardie"]["enabled"] = True

        char_info["Biff"]["level"] = 2
        char_info["Biff"]["current_progress"] = 0
        char_info["Biff"]["caption"] = t_("Цыпочке надо развлекать папочку, чтобы он продолжал давать ей работу.")
        char_info["Biff"]["enabled"] = True

        char_info["AlexPhotograph"]["level"] = 2
        char_info["AlexPhotograph"]["current_progress"] = 93
        char_info["AlexPhotograph"]["enabled"] = True

        char_info["Melanie"]["level"] = 1
        char_info["Melanie"]["current_progress"] = 10

        char_info["DickSecretary"]["level"] = 2
        char_info["DickSecretary"]["current_progress"] = 0
        char_info["DickSecretary"]["caption"] = t_("Виктория любит играть с подружками.")
        char_info["DickSecretary"]["enabled"] = True

#        char_info["DickSecretary"]["caption"] = t_("Виктория ждет свои деньги еженедельно.")


        char_info["Driver"]["level"] = 1
        char_info["Driver"]["current_progress"] = 0
        char_info["Driver"]["caption"] = t_("Бывший водитель Моники.")
        char_info["Driver"]["enabled"] = True

        char_info["ReceptionGirl"]["level"] = 1
        char_info["ReceptionGirl"]["current_progress"] = 50
        char_info["ReceptionGirl"]["caption"] = t_("Сутенерша в Le Grand.")
        char_info["ReceptionGirl"]["enabled"] = True
#        char_info["ReceptionGirl"]["caption"] = ""

        char_info["Julia"]["level"] = 9
        char_info["Julia"]["current_progress"] = 25
        char_info["Julia"]["caption"] = t_("Юлия любит Монику и хочет с ней пробовать все виды развлечений.")
        char_info["Julia"]["enabled"] = True

#        char_info["Julia"]["level"] = 1
#        char_info["Julia"]["current_progress"] = 0
#        char_info["Julia"]["caption"] = t_("Юлия боится Монику")

        char_info["Jane"]["level"] = 1
        char_info["Jane"]["current_progress"] = 0
        char_info["Jane"]["caption"] = t_("Собирается замуж за Стива.")
        char_info["Jane"]["enabled"] = True

        char_info["Stephanie"]["level"] = 1
        char_info["Stephanie"]["current_progress"] = 10
        char_info["Stephanie"]["caption"] = t_("Монике удается скрывать от бывших подружек ее положение.")
        char_info["Stephanie"]["enabled"] = True

        char_info["Rebecca"]["level"] = 1
        char_info["Rebecca"]["current_progress"] = 10
        char_info["Rebecca"]["caption"] = t_("Монике удается скрывать от бывших подружек ее положение.")
        char_info["Rebecca"]["enabled"] = True

        char_info["Bartender"]["level"] = 3
        char_info["Bartender"]["current_progress"] = 0
        char_info["Bartender"]["enabled"] = True

        char_info["Bartender_Waitress"]["level"] = 3
        char_info["Bartender_Waitress"]["current_progress"] = 0
        char_info["Bartender_Waitress"]["enabled"] = True

        char_info["Pub_StripteaseGirl1"]["level"] = 2
        char_info["Pub_StripteaseGirl1"]["current_progress"] = 50
        char_info["Pub_StripteaseGirl1"]["caption"] = t_("Молли ненавидит Монику и пакостит ей. Моника тоже...")
        char_info["Pub_StripteaseGirl1"]["enabled"] = True

        char_info["Pub_StripteaseGirl2"]["level"] = 3
        char_info["Pub_StripteaseGirl2"]["current_progress"] = 0
        char_info["Pub_StripteaseGirl2"]["caption"] = t_("Клэр знает имя Моники и помогает ей. Она ее друг.")
        char_info["Pub_StripteaseGirl2"]["enabled"] = True

        char_info["Shawarma_Trader"]["level"] = 1
        char_info["Shawarma_Trader"]["current_progress"] = 0
        char_info["Shawarma_Trader"]["caption"] = t_("Сдает жилье постояльцам без документов. Недорого.")
        char_info["Shawarma_Trader"]["enabled"] = True

        char_info["Mommy"]["level"] = 1
        char_info["Mommy"]["current_progress"] = 0
        char_info["Mommy"]["caption"] = t_("Следит за тем, чтобы все проститутки работали у нее под присмотром.")
        char_info["Mommy"]["enabled"] = True


    call define_hudpresets() from _rcall_define_hudpresets_2
    call questLog_init() from _rcall_questLog_init_2
    $ day_stored = day
    $ day = 0
    # обнуляем квестлог
    python:
        for i in range(0, len(questLogData)):
            questLogData[i][2] = False

        # включаем максимум квестлога
        questLog(55, True) #Барди совсем обнаглел и заставляет меня быть мамой для своего одноклассника. Такого же неудачника как он сам!
        questLog(45, True) #Я могу питаться в доме. Если буду соблюдать условие..."
        questLog(38, True) #Я теперь должна ходить без трусиков в доме. Иначе Барди накажет меня. Мерзавец!
        questLog(4, True) #Бетти ждет от меня, что я буду регулярно убираться в доме и тереть это проклятое пятно.
        questLog(23, True) #Кажется, Бетти не так строго следит за тем, чтобы я убиралась все время.
        questLog(39, True) #Бетти теперь должна ходить без трусиков в доме. Она сказала что я могу проверять это. Это все проделки Барди!
        questLog(43, True) #Теперь я могу работать в офисе. Денег это не добавило, но я могу чувствовать себя Боссом снова...
        questLog(46, True) #Биф требует, чтобы я собирала отчеты у своих сотрудников и приносила ему. За кого он меня держит?!
        questLog(8, True) #Похоже я нашла возможность зарабатывать деньги, делая фотосессии у Бифа. Но эти фотосессии все более развратные. Долго-ли я смогу себе это позволять?
        questLog(67, True) #Биф требует, чтобы я убедила этих глупых инвесторов инвестировать деньги в мой журнал. Как он предполагает я смогу это сделать?
        questLog(64, True) #Мне нужно каждый день целовать Юлию и говорить ей комплименты.
        questLog(73, True) #У меня появилась возможность сбежать из страны. Для этого мне всего лишь нужно притворяться влюбленной дурочкой перед никчемной Юлией.
        questLog(74, True) #Теперь я могу жить у этой дурацкой гувернантки. И мне не нужно платить за жилье и еду. Но на что мне придется идти взамен?
        questLog(12, True) #Теперь я должна приносить Виктории раз в неделю $ 5000 до пятницы. Я даже не представляла насколько она опасна.
        questLog(81, True) #Я притворяюсь перед Ральфом что люблю его. Уверена, что я смогу занять место Бетти и вернуть себе свой дом!
        questLog(71, True) #У меня теперь есть место, где я могу жить. Апартаменты в трущобах... Но это лучше, чем подвал в доме, где живет семейка идиотов.
        questLog(62, True) #Мне предложили работу в эскорте! Неужели я решусь на такое?! Хотя... Там можно неплохо заработать.
        questLog(61, True) #У меня появилась возможность дополнительного заработка по субботам. У Филиппа. Но смогу ли я?
        questLog(42, True) #Стив слизняк и негодяй! Но, может быть, через него можно найти какую-то работу или просто деньги?
        questLog(22, True) #Вместо разноски флаеров я нашла более быстрый способ заработать. Он немного... неудобный, но ведь это ненадолго...
        questLog(83, True) #Старая карга застукала меня! Она сказала что заниматься проституцией в этом районе нельзя без ее разрешения! Какого черта?! Ложь! Я бы никогда не стала заниматься этим! Но что мне теперь делать? Если я хочу хоть что-то заработать, мне придется найти укромное место, где старая карга не найдет меня...
        questLog(82, True) #Теперь мне нужно каждую неделю приносить гребаной Перри деньги в счет оплаты долга. Черт!
        questLog(30, True) #Я нашла способ зарабатывать на еду, моя посуду в Баре. Я не в восторге, но ведь это временно?
        questLog(18, True) #Мне надо как-то вернуть мою прошлую жизнь. Я не смогу долго прожить в этом кошмаре!
        questLog(84, True) #Теперь корона Shiny Hole принадлежит МНЕ! Я буду пользоваться королевскими привилегиями! А эта сучка Молли теперь никто!
        questLog(77, True) #Мерзавец Биф! Он при Клэр сказал, что я работаю заменой Моники Бакфетт! Теперь единственный адекватный человек будет считать меня лгуньей!
        questLog(52, True) #Я устроилась работать официанткой в Shiny Hole. У меня нет зарплаты и почти все чаевые надо отдавать хозяевам, но это шанс заработать хоть какие-то деньги. Я не могу выносить этих жутких клиентов, но у меня нет выбора. Тем более, это ненадолго...
        questLog(48, True) #Кажется, Джо пытается меня лапать, когда я мою посуду... Ненавижу эту работу!
        questLog(49, True) #Кажется, Эшли пытается меня лапать. Я не понимаю с какой целью. Ведь у нее есть муж!
        questLog(60, True) #Эшли простила мне долг. Теперь я могу зарабатывать, выступая на сцене в пабе Shiny Hole. Неужели для меня это теперь нормально?
        questLog(75, True) #Я полностью разделать на сцене перед толпой пьяных посетителей. Мне не верится, что это случилось наяву, а не в кошмарном сне! Но, с другой стороны, я делала это в маске и меня никто не знает здесь...
        questLog(58, True) #Эта рыжая стриптизерша слишком многое себе позволяет. Как она смеет так общаться со мной?!
        questLog(59, True) #Похоже, Клэр единственная в этой дыре, с кем можно нормально общаться.
        questLog(56, True) #Маркус ждет меня снова... Смогу-ли я решиться снова навестить его?
        questLog(14, True) #В фитнес-зале я встретила Стефани и Ребекку. Я, кажется, убедила их что все это игра. Но долго-ли они будут в это верить?

    $ day = day_stored
    $ set_active("Teleport_House_Outside_Neighbour", False, scene="street_house_outside")

    $ monicaHasCasualDress1 = True
#    $ monicaAgreedToSellDress = True
#    $ monicaBoughtCasualDress1 = False
#    $ monicaStealCasualDress1 = False
#    $ monicaKickedVivianForDress = False
#    $ monicaOffendedCit3 = False # Моника заставила покупателя купить платье силой

#    $ monicaHasSchoolOutfit1Day = 5
    $ monicaHasSchoolOutfit1 = True

    $ monicaPussyShaved = True
    $ monicaMustNotWearPanties = True

    # Office
#    $ monicaEarnedWeeklyMoney = True
    $ monicaAskBiffGiftCertificateFirstTime = False
    $ monicaOfficeBiffMelanie = False
    $ monicaOutfitsEnabled[7] = True
    $ monicaOutfitsEnabled[8] = True
    $ monicaOutfitsEnabled[9] = True
    $ photoshoot8_melanie_forced = True
    $ ep22_quests_biff_init_flag = True
    $ ep211_quests_photoshoot_stage = 3
    $ ep2_part2_alex_old_photoshoots_progress_blocked = True # только в new game!

    $ monicaWorkFlashCardReportLastDay = day - 1
    $ monicaWorkedDaysTotal = 30
    $ add_office_working_day(True)

    $ monicaWorkFlashCardQuestActive = True # надо собирать отчеты
    $ ep27_flash_card_reports_done_count = 10
    $ miniMapOfficeActivated = True
    $ ep216_office_blocked_day = 0
    $ biffLevel3Opened = True

    $ monicaWorkingAtBiffOffice = True
    $ ep27_quests_flash_quest1_inited = True

    $ makeupRoomMelanieSuffix = 2
    $ monicaOfficeWhiskeyOnTable = True

    $ monicaEarnedWeeklyMoneySkip = False

    $ ep211_quests_publicevent2_completed = True
    $ ep213_quests_biff1_inited = True
    $ ep213_presentation2_completed_day = 210
    $ ep211_quests_photoshot8_opened_day = 210
    $ ep215_quests_escort_initialized = True
    $ monicaNeedToAskMelanieForHelp = False

    $ biffLevel3Opened = True

    $ ep29_quests_melanie_started = True
    $ ep212_quests_melanie_inited = True
    $ ep213_quests_victoria1_init_flag = True
    $ ep27_melanie_visited_victoria = True
    $ ep27_melanie_refused_victoria_friendship = False

    #escort
    $ ep215_quests_escort_completed_day = 10
    $ monicaEscortRevengeGirl2 = True
    $ ep212_escort3_completed = True

    #Юлия
    $ juliaQuestStarted = True
    $ ep210_julia_not_at_work = False
    #    $ monica_living_at_juliahome = True
    $ juliaHomeLivingRoomJuliaCloth = "JuliaCloth1"
    $ minimapJuliaGenerateEnabled = True
    call ep213_quests_julia2_req_init() from _rcall_ep213_quests_julia2_req_init_3

    # Блок Маркуса
    $ add_hook("Building", "ep213_dialogues_police19", scene="street_police", label="ep2_part2_block_marcus")

    # Fitness
    $ fitness_gym_visited_amount = 14
    $ fitness_gym_state = 1

    # Ральф
    $ monicaBardieRalphSeducingStage = 6

    # Slums
    $ slumsApartmentsCheckInitialized = True # всегда
    $ monicaRentApartmentsInited = True # всегда

    $ ep214_quests_citizens_stage2 = True

    # pub
    $ ep29_quests_dancing_with_claire_active = False
    $ monicaDancingWillingly = True
    $ pubMonicaWorkingWaitress = True
    if monicaPubWashingDishesCount == 0:
        $ monicaPubWashingDishesCount = 10
    if monica_shiny_hole_queen_day == 0:
        $ monica_shiny_hole_queen_day = 210
    $ monicaWorkingAsDishwasher = True
    $ ep29_quests_pub_monica_knows_claire = True
    $ ep29_quests_pub_monica_knows_molly = True
    $ stage_Monica_shoots_array = ["1up", "1side", "1down", "2up", "2side", "2down", "3up", "3side", "3down", "4up", "4side", "4down", "5up", "5side", "5down", "6up", "6side", "6down", "7up", "7side", "7down", "8up", "8side", "8down", "9up", "9side", "9down", "18up", "18side", "18down", "19up", "19side", "19down", "20up", "20side", "20down", "21up", "21side", "21down", "22up", "22side", "22down", "23up", "23side", "23down", "24up", "24side", "24down", "25up", "25side", "25down", "26side"]
#    $ stage_Monica_shoots_array = ["1up", "1side", "1down", "2up", "2side", "2down", "3up", "3side", "3down", "4up", "4side", "4down", "5up", "5side", "5down", "6up", "6side", "6down", "7up", "7side", "7down", "8up", "8side", "8down", "9up", "9side", "9down", "10up", "10side", "10down", "11up", "11side", "11down", "12up", "12side", "12down", "13up", "13side", "13down", "14up", "14side", "14down", "15up", "15side", "15down", "16up", "16side", "16down", "17up", "17side", "17down", "18up", "18side", "18down", "19up", "19side", "19down", "20up", "20side", "20down", "21up", "21side", "21down", "22up", "22side", "22down", "23up", "23side", "23down", "24up", "24side", "24down", "25up", "25side", "25down", "26up", "26side", "26down"]
    $ pubDanceCount = 30
    $ stage_shoots_total_amount_cur = 27 + stage_shoots_total_amount_nude
#    $ stage_shoots_total_amount_cur = 78
    $ monicaDancingStage = 2
    $ stage_low_tips = True
    $ stage_dance_nude_planned = True
    $ monicaDancingJoeAskedAboutPrivate = True
    $ ep210_quests_stage = 5
    $ stage_dance_nude_last_day = 210
    $ monicaAshleyTalkedAboutSharingTips = True
    $ ep215_quests_ashley_dialogue2_active = True
    $ ep213_quests_stole_tips_count = 3

    # house
    $ bardieBlackmailStage = 5
    $ bardieMonicaNonNudeCount = bardieCleaningNonNudeDuringPunishment - 1
    $ monicaMustNotWearPanties = True
    $ bettyMustNotWearPanties = True
    $ bettyOffendedBardieKitchen = True
    $ monicaMustWearBettyPanties = False
    $ monicaLaundryBettyPantiesSelectMode = 1 #Выбор в прачечной
    $ monicaLaundryBettyPantiesSelectNudeDisabled = False
    $ spotCleaning = True
    $ floor2WashingSport = True
    $ monica_tint = [1.0, 1.0, 1.0]

    $ add_objective("money_for_victoria", t_("Заработать $ 5000 для Виктории до Пятницы!"), c_pink, 10)

    $ define_inventory_object("food_package", {"description" : t_("Еда"), "label_suffix" : "_use_food", "default_label" : False, "default_nolabel" : "cant_use", "icon" : "Inventory/food_package" + res.suffix + ".png"})

    $ basementBedSkipUntilFridayEnabled = True

    $ cloth = "CasualDress1"
    $ cloth_type = "CasualDress"
    $ monicaCasualDressWearFirstTimeWardrobe = False
    $ bitchmeterValue = 280

    $ gameStage = 0
    $ gameSubStage = 0
    $ afterJail = True
    $ rain = False
    $ sceneIsStreet = False

    $ game_version1_screen_ready_to_render = True
    $ zoom_factor = 1

    $ monicaEatedLastDay = day-1
    $ week_day = (day)%7
    if week_day == 0:
        $ week_day = 7

    $ day_time = "evening"
    $ day_suffix = ""
    $ money = 0.0

    $ showObjectsNotOwner = True
    $ faceHudImage = False
    $ hud_preset_current = "default"
    $ hud_preset_default = "default"
    $ minimap_coords_preset = 0
    $ miniMapEnabledOnly = []
    $ miniMapDisabled = {}
    $ miniMapDisabled2 = {}
    $ miniMapOfficeActivated = True
    $ miniMapTurnedOff2 = False
    $ miniMapHousePreset = "laundry"

    $ bFredFollowingMonica = False

    $ set_active(False, group="workers", scene="working_office")
    $ set_active(False, group="workers", scene="working_office2")
    call office_life_day() from _rcall_office_life_day_1



    $ scene_refresh_flag = True
    $ map_scene = "House"
    $ map_enabled = True
    $ map_disabled_forced = False
    $ scene_name = "none"
    $ api_scene_name = "none"

    $ scene_sound = False
    $ scene_transition = "Fade_long"

    call food_basement_room_init() from _rcall_food_basement_room_init_1

    call questHelp_init() from _rcall_questHelp_init_4
    call part2_questions_start_new_game() from _rcall_part2_questions_start_new_game

    $ changeDayTime("day")

    call change_scene("street_house_outside") from _rcall_change_scene_220
    call process_change_map_location("House") from _rcall_process_change_map_location_10
label start_game_EP22:
    $ ep213_quests_pub1_inited = True
    $ ep214_quests_pub1_check_inited_flag = True
    $ ep215_quests_pub1_inited = True

    $ ep217_quests_bugfix1_initialized = True
    $ ep218_quests_load_init_flag = True
    $ ep219_quests_load_init_flag = True
    $ ep224_quests_load_init_flag = True
    $ ep225_quests_load_init_flag = True
    $ questHelpActivated = True
    call questHelp_init() from _rcall_questHelp_init_2
    $ questHelp("other1")
    $ questHelp("other2")
    $ questHelp("office_58")
    #remove bardie
    $ remove_hook(label="menu_betty_panties_show_to_monica")
    $ set_active("Panties_Box", False, scene="basement_laundry")

#    call refresh_scene_fade_long()
    call ep217_quests() from _rcall_ep217_quests
    call ep218_quests_victoria_init() from _rcall_ep218_quests_victoria_init_1
    jump show_scene




    call intro_questions() from _call_intro_questions

    $ ralphAskedAboutPayment = False
    $ add_objective("ask_ralph", t_("Узнать у Ральфа по поводу оплаты"), c_orange, 13)
    $ add_objective("freedom", t_("Избежать наказания"), c_red, 0)

    call monica_cheats_init() from _rcall_monica_cheats_init_3
    $ ep24_quests_initialized = True
    $ ep26_quests_initialized = True
    $ ep27_quests_initialized = True
    $ ep29_quests_initialized = True
    $ ep210_quests_load_init_flag = True
    $ ep211_quests_load_init_flag = True
    $ ep212_quests_load_init_flag = True
    $ ep213_quests_load_init_flag = True
    $ ep214_quests_load_init_flag = True
    $ ep215_quests_load_init_flag = True
    $ ep216_quests_load_init_flag = True
    call start_game() from _call_start_game
    return

label start_saved_game:
    if scene_name != "basement_bedroom1" and scene_name != "basement_bedroom2":
        img black_screen
        help "Пожалуйста, используйте сохранение из финальной локации в подвале дома."
        scene black_screen
        with Dissolve(1)
        $ renpy.full_restart(transition=Fade(1.0, 1.0, 1.0))
        return

    $ refresh_list_files_forced()
    $ scenes_data = {"objects": {}, "substs" : {}, "autorun": {}, "hooks": {}}
    $ hooks_stack = []
    $ inventory_objects = {}
    $ inventory = []
    call intro_questions_save() from _call_intro_questions_save
    $ objectives_list = []
    if ralphAskedAboutPayment == False:
        $ add_objective("ask_ralph", t_("Узнать у Ральфа по поводу оплаты"), c_orange, 13)
    $ add_objective("freedom", t_("Избежать наказания"), c_red, 0)
    $ teleportHomeFredBlowjobFlag = False
    call start_game() from _call_start_game_1
    return

label start_game:

    $ gameStage = 0
    $ gameSubStage = 0
    $ afterJail = True
    $ rain = False
    $ sceneIsStreet = False

    $ game_version1_screen_ready_to_render = True
    $ zoom_factor = 1

    $ day = 5
    $ monicaEatedLastDay = day
    $ week_day = (day)%7
    if week_day == 0:
        $ week_day = 7

    $ day_time = "evening"
    $ day_suffix = ""
    $ money = 0.0

    $ hud_preset_current = "default"

    call questLog_init() from _call_questLog_init
    $ questLog(19, True)
    $ questLog(18, True)
    $ questLog(15, True)
    $ questLog(6, True)
    $ questLog(3, True)

    call game_init() from _call_game_init
#    python:
#        for i in renpy.exports.get_image_load_log():
#            print i

    $ map_objects = {
            "Teleport_Monica_Office" : {"text" : t_("ОФИС МОНИКИ"), "xpos" : 882, "ypos" : 320, "base" : "map_marker", "state" : "visible"},
            "Teleport_Street_Corner" : {"text" : t_("УГОЛ УЛИЦЫ"), "xpos" : 124, "ypos" : 476, "base" : "map_marker", "state" : "visible"},
            "Teleport_Dick_Office" : {"text" : t_("ОФИС ДИКА"), "xpos" : 1370, "ypos" : 127, "base" : "map_marker", "state" : "visible"},
            "Teleport_Gas_Station" : {"text" : t_("ЗАПРАВКА"), "xpos" : 1125, "ypos" : 910, "base" : "map_marker", "state" : "visible"},
            "Teleport_Police" : {"text" : t_("ПОЛИЦИЯ"), "xpos" : 912, "ypos" : 809, "base" : "map_marker", "state" : "visible"},
            "Teleport_Rich_Hotel" : {"text" : t_("ОТЕЛЬ ЛЯ ГРАНД"), "xpos" : 1782, "ypos" : 593, "base" : "map_marker", "state" : "visible"},
            "Teleport_Fitness" : {"text" : t_("ФИТНЕСС"), "xpos" : 356, "ypos" : 411, "base" : "map_marker", "state" : "visible"},
            "Teleport_Steve_Office" : {"text" : t_("ОФИС СТИВА"), "xpos" : 1333, "ypos" : 724, "base" : "map_marker", "state" : "visible"},
            "Teleport_Bank" : {"text" : t_("БАНК"), "xpos" : 1212, "ypos" : 439, "base" : "map_marker", "state" : "visible"},
            "Teleport_Cloth_Shop" : {"text" : t_("МАГАЗИН ОДЕЖДЫ"), "xpos" : 340, "ypos" : 901, "base" : "map_marker", "state" : "visible"},
            "Teleport_Street_Corner" : {"text" : t_("УГОЛ УЛИЦЫ"), "xpos" : (88+15), "ypos" : 942, "base" : "map_marker", "state" : "visible"},
            "Teleport_Hostel2" : {"text" : t_("ГРЯЗНАЯ УЛИЦА"), "xpos" : 259, "ypos" : 1046, "base" : "map_marker", "state" : "invisible"},
            "Teleport_House" : {"text" : t_("ДОМ МОНИКИ"), "xpos" : 105, "ypos" : 798, "base" : "map_marker_house", "state" : "active"}
    }
#mousedown_3, hide_windows
#    $ print(config.keymap["game_menu"])
#    $ config.keymap["hide_windows"] = []
#    $ print(config.keymap)
#    pause

    $ bFredFollowingMonica = False

    $ scene_refresh_flag = True
    $ map_scene = "House"
    $ map_enabled = True
    $ map_disabled_forced = False
    $ scene_name = "none"
    $ api_scene_name = "none"
    call locations_init() from _call_locations_init
    call citizens_init() from _call_citizens_init
    call characters_init() from _call_characters_init
    call basement_shower_init() from _call_basement_shower_init
    call kebab_work_init() from _call_kebab_work_init

    $ add_hook("exit_scene", "hook_basement_bedroom2_change_view_to_suffix3", scene="basement_bedroom2")
    # Запрет Бетти ходить по дому
    $ add_hook("enter_scene", "afterJailHouse_dialogue10", scene="bathroom_bath", label="betty_forbidden")
    $ add_hook("enter_scene", "afterJailHouse_dialogue15", scene="kitchen", label="betty_forbidden")
    $ add_hook("enter_scene", "afterJailHouse_dialogue15b", scene="kitchen2", label="betty_forbidden")
    $ add_hook("enter_scene", "afterJailHouse_dialogue16a", scene="bedroom2", label="betty_forbidden")

    # Проверка одежды при хождении по дому и покидании его
    $ add_hook("exit_scene", "hook_basement_bedroom_check_exit_cloth", scene="basement_bedroom1")
    $ add_hook("exit_scene", "hook_basement_bedroom_check_exit_cloth", scene="basement_bedroom2")
    $ add_hook("exit_scene", "hook_basement_bedroom_check_exit_cloth", scene="basement_bedroom_cupboard")
    $ add_hook("exit_scene", "hook_basement_bedroom_check_exit_cloth", scene="basement_bedroom_table")
    $ add_hook("map_teleport", "hook_basement_bedroom_check_exit_cloth_map", scene="global", priority=1000)
    $ add_hook("Gates", "hook_basement_bedroom_check_exit_cloth_gates", scene="street_house_gate")

    # Жизнь персонажей
    $ add_hook("change_time_day", "citizens_init_day", scene="global")
    $ add_hook("change_time_evening", "citizens_init_evening", scene="global")

    call Bardie_Life_init() from _call_Bardie_Life_init
    call Betty_Life_init() from _call_Betty_Life_init
    call Ralph_Life_init() from _call_Ralph_Life_init
    call Fred_Life_init() from _call_Fred_Life_init
    call Biff_Life_init() from _call_Biff_Life_init

    # Постель в подвале
    $ add_hook("BasementBed", "basement_bed_hook", scene="basement_bedroom2")
    $ add_hook("basement_monica_after_sleep", "basement_monica_after_sleep", scene="global")
    $ add_hook("basement_monica_after_nap", "basement_monica_after_nap", scene="global")
    $ add_hook("basement_monica_after_sleep_dialogue", "basement_monica_after_sleep_dialogue1", scene="global")
    $ add_hook("basement_monica_after_nap_dialogue", "basement_monica_after_nap_dialogue1", scene="global")
    # Уборка в доме
    $ add_hook("enter_scene", "house_cleaning", scene="floor1")
    $ add_hook("enter_scene", "house_cleaning", scene="floor2")
    $ add_hook("enter_scene", "house_cleaning", scene="bedroom_bardie")
    $ add_hook("enter_scene", "house_cleaning", scene="bedroom_second")
    $ add_hook("enter_scene", "house_cleaning", scene="living_room")
    $ add_hook("enter_scene", "house_cleaning", scene="bedroom1")
    $ add_hook("enter_scene", "house_cleaning", scene="bedroom2")
    $ add_hook("monica_cleaning_start", "Bardie_Life_Monica_Cleaning_Start", scene="global")
    $ add_hook("monica_cleaning_end", "Bardie_Life_Monica_Cleaning_End", scene="global")
    $ add_hook("monica_cleaning_start", "Betty_Life_Monica_Cleaning_Start", scene="global")
    $ add_hook("monica_cleaning_end", "Betty_Life_Monica_Cleaning_End", scene="global")
    $ add_hook("monica_cleaning_start", "Ralph_Life_Monica_Cleaning_Start", scene="global")
    $ add_hook("monica_cleaning_end", "Ralph_Life_Monica_Cleaning_End", scene="global")
    $ add_hook("monica_cleaning_start", "Fred_Life_Monica_Cleaning_Start", scene="global")
    $ add_hook("monica_cleaning_end", "Fred_Life_Monica_Cleaning_End", scene="global")
    # Офис Моники
    $ add_hook("Teleport_Monica_Office_Cabinet", "monica_office_secretary_dialogue4a", scene="monica_office_secretary")


    # Узнать про оплату у Ральфа
    $ add_hook("enter_scene", "Ralph_Life_Ask_About_Payment", scene="living_room")

    # Офис Дика вначале закрыт
    $ add_hook("Teleport_Inside", "monica_dick_office_dialogue1a", scene="dick_office_entrance")
    $ move_object("DickTheLawyer", "empty")

    # Офис Моники
    $ add_hook("Teleport_Monica_Office_Secretary", "monica_office_entrance_biff_dialogue1", scene="monica_office_entrance")
    $ move_object("Secretary", "monica_office_secretary")
    $ add_hook("Secretary", "monica_office_secretary_dialogue2", scene="monica_office_secretary") # Регулярный разговор попросить деньги
    $ add_hook("Secretary", "monica_office_secretary_dialogue1", scene="monica_office_secretary", label="secretary1")
    $ add_hook("Teleport_Monica_Office_Photostudio", "monica_office_secretary_dialogue1", scene="monica_office_secretary", label="secretary1")

    $ add_hook("Teleport_Monica_Office_Cabinet", "monica_office_secretary_dialogue4a", scene="monica_office_secretary", label="check_bill_at_place", priority=150)
    $ add_hook("Table", "monica_office_cabinet_biff_dialogue1", scene="monica_office_cabinet", label="biff1")
    $ add_hook("Biff", "monica_office_cabinet_biff_dialogue1", scene="monica_office_cabinet", label="biff1")

    $ add_hook("Teleport_Monica_Office_Cabinet", "monica_office_secretary_dialogue1", scene="monica_office_secretary", label="secretary1")

    $ move_object("Melanie", "monica_office_cabinet")
    $ add_hook("Melanie", "monica_office_photostudio_melanie_dialogue1", scene="monica_office_secretary")
    $ move_object("AlexPhotograph", "monica_office_photostudio")
    $ add_hook("AlexPhotograph", "monica_office_photostudio_alex_dialogue1", scene="monica_office_photostudio") # Приветствие Алекса

    # Заправка
    $ add_hook("enter_scene", "monica_gas_station_thief_dialogue1", scene="gas_station_view1")

#    $ remove_hook(label="betty_forbidden", scene="House", recursive=True)
    call change_scene("basement_bedroom2", "Fade_long", False) from _call_change_scene_51
    $ changeDayTime("day")

    $ miniMapDisabled = {"House":[], "Street_Corner":["Hostel_Street", "Hostel_Street2", "Hostel_Street3", "Hostel_Edge_1_c"]}
    $ miniMapEnabledOnly = []

    # Закрываем вначале доп. локации в Street_Corner (бедный квартал)
    $ add_hook("Teleport_Street_Hostel", "kebab_work_block_teleports", scene="whores_place_shawarma", label="kebab_work_block_teleports")
    $ add_hook("Teleport_Hostel_Street3", "kebab_work_block_teleports", scene="street_corner", label="kebab_work_block_teleports")

    $ scene_transition = "Fade_long"

    $ add_hook("before_open", "food_basement_room_init", scene="basement_bedroom2", label="food_basement_room_init", priority = 200)
    $ add_hook("before_open", "food_basement_room_init2", scene="basement_bedroom_table", label="food_basement_room_init", priority = 200)
    $ define_inventory_object("food_package", {"description" : t_("Еда"), "label_suffix" : "_use_food", "default_label" : False, "default_nolabel" : "cant_use", "icon" : "Inventory/food_package" + res.suffix + ".png"})
    $ ep23_quests_initialized = True

    call floor2_init_addition1() from _call_floor2_init_addition1_1 #Барди floor2
    call bedroom1_init_addition1() from _call_bedroom1_init_addition1_1 # Барди bedroom1
    call monica_cheats_init() from _rcall_monica_cheats_init_1
    $ ep24_quests_initialized = True
    $ ep26_quests_initialized = True
    $ ep27_quests_initialized = True
    $ ep29_quests_initialized = True
    $ ep210_quests_load_init_flag = True
    $ ep211_quests_load_init_flag = True
    $ ep212_quests_load_init_flag = True
    $ ep213_quests_load_init_flag = True
    $ ep214_quests_load_init_flag = True
    $ ep215_quests_load_init_flag = True
    $ ep216_quests_load_init_flag = True
#    $ changeDayTime("evening")
#    $ scene_data = process_scene_objects_list(scene_name) #парсим содержимое свойств объектов перед выводом
#    $ print scene_data

#    $ cloth = "CasualDress1"
#    $ cloth_type = "CasualDress"
#    $ day_time = "evening"
#    $ day_suffix = "_Evening"
#    call locations_init_monicahome()
#    call locations_init_juliahome()
#    call locations_init_public_event2()
#    call locations_init_rich_hotel_restaurant2()
#    call locations_init_rich_hotel_restaurant()
#    call rich_hotel_reception_init2()
#    call rich_hotel_reception_init3()
#    call change_scene("rich_hotel_reception") #debug !!!!!
#    jump show_scene
#    $ renpy.pause(100, hard=True)

#    $ autorun_to_object("intro_scene", "intro_scene_start")
    music stop
#    $ _dismiss_pause = False
    scene black_screen
    with Dissolve(1)
    call textonblack_long("FASHION BUSINESS") from _call_textonblack_long
    scene black_screen
    with Dissolve(1)
    call textonblack_long("EPISODE 2") from _call_textonblack_long_1
    scene black_screen
    with Dissolve(1)
#    $ _dismiss_pause = True
    call sleep_scene1() from _call_sleep_scene1

    $ episode = 2
    jump show_scene

label start_new_game:
    music casualMusic
#    $ map_enabled = True
#    $ add_objective("dress_homecloth", t_("Одеть домашнюю одежду"), c_blue, 0)

#    $ miniMapDisabled = ["Basement"]


#    $ add_inventory("phone", 1, True)
    return

label empty_label:
    return









#
