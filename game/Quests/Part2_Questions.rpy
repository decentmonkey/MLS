default ep22_questions_answered_count = 0
default ep2p2_flag1 = False

label part2_questions_start_new_game:

#        $ del(map_objects["Teleport_Slums_Apartments"])
#    $ map_objects["Teleport_Hostel2"]["state"] = "visible"
    call part2_questions_process(True) from _rcall_part2_questions_process
    return

label part2_questions_init_loadgame:
    python:
        for i in range(0, renpy.call_stack_depth()):
            renpy.pop_call()

    $ after_load_ready_to_render = True
    $ refresh_list_files_forced()

    hide screen questhelp_screen
    hide screen achievements_screen
    hide screen questlog_screen
    music2 stop
#    $ episode = 2
#    $ debugMode = True
    if owner != "Monia":
        call change_owner("Monica") from _rcall_change_owner_6

#    $ day = 231
    $ scenes_data = {"objects": {}, "substs" : {}, "autorun": {}, "hooks": {}}
    $ hooks_stack = []
#    if owner != "Monica:"
    $ inventory_objects = {}
    $ inventory = []
    $ owner = "Monica"
    $ questHelpJustUpdated = False
    $ questHelpUpdatedDay = 0
    $ questHelpData = {}
    $ questHelpDataQuests = {}
    $ questHelpDataCategoriesDescriptions = {}
    $ questHelpDataCategoriesDescriptionsData = {}
    $ questHelpDataLastMemory = {}
    $ questHelpDataLastQuestsBold = {}
    $ questHelpDataCategoriesBold = {}
    $ questHelpCurrentCategory = False
    $ questHelpCurrentQuest = False
    $ questHelpCategoriesHistory = []
    $ questHelpCategoriesHistoryStatic = []
    call questHelp_init() from _rcall_questHelp_init_3

#    call game_init()

    $ ep2p2_flag1 = check_hook("ep22_quests_Dick7", scene="global_week_day")

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
    call characters_init() from _rcall_characters_init
    call characters_pub_init() from _rcall_characters_pub_init_1
    call characters_pub_init2() from _rcall_characters_pub_init2_1
    call characters_init_julia() from _rcall_characters_init_julia
    $ char_info["Pub_StripteaseGirl1"]["name"] = t_("Молли")
    $ char_info["Pub_StripteaseGirl2"]["name"] = t_("Клэр")
    $ char_info["Rebecca"]["enabled"] = True
    $ char_info["Stephanie"]["enabled"] = True

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


    call define_hudpresets() from _rcall_define_hudpresets_1
    call questLog_init() from _rcall_questLog_init_1
    $ day_stored = day
    $ day = 0
    # обнуляем квестлог
    python:
        questLogDataEnabled = {}
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
    $ monicaEarnedWeeklyMoneySkip = False

    $ monicaWorkFlashCardReportLastDay = day - 1
    if monicaWorkedDaysTotal == 0:
        $ monicaWorkedDaysTotal = 30
    $ add_office_working_day(True)

    $ monicaWorkFlashCardQuestActive = True # надо собирать отчеты
    if ep27_flash_card_reports_done_count == 0:
        $ ep27_flash_card_reports_done_count = 10
    $ miniMapOfficeActivated = True
    $ ep216_office_blocked_day = 0
    $ biffLevel3Opened = True

    $ monicaWorkingAtBiffOffice = True
    $ ep27_quests_flash_quest1_inited = True

    $ makeupRoomMelanieSuffix = 2
    $ monicaOfficeWhiskeyOnTable = True

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

    #escort
    if ep215_quests_escort_completed_day == 0:
        $ ep215_quests_escort_completed_day = 10
    $ monicaEscortRevengeGirl2 = True
    $ ep212_escort3_completed = True

    #Юлия
#    $ monica_living_at_juliahome = True
    $ juliaQuestStarted = True
    $ ep210_julia_not_at_work = False
    $ juliaHomeLivingRoomJuliaCloth = "JuliaCloth1"
    $ minimapJuliaGenerateEnabled = True
    call ep213_quests_julia2_req_init() from _rcall_ep213_quests_julia2_req_init_2

    # Блок Маркуса
    $ add_hook("Building", "ep213_dialogues_police19", scene="street_police", label="ep2_part2_block_marcus")

    # Fitness
    if fitness_gym_visited_amount == 0:
        $ fitness_gym_visited_amount = 14
    $ fitness_gym_state = 1

    # Ральф
    $ monicaBardieRalphSeducingStage = 6

    # Slums
    $ slumsApartmentsCheckInitialized = True # всегда
    $ monicaRentApartmentsInited = True # всегда
    $ ep214_quests_citizens_stage2 = True
    $ kebabWorkInProgress = False

    #pub

    $ ep29_quests_dancing_with_claire_active = False
    $ monicaDancingWillingly = True
    $ pubMonicaWorkingWaitress = True
    if monicaPubWashingDishesCount == 0:
        $ monicaPubWashingDishesCount = 10
    $ ep29_quests_pub_monica_knows_claire = True
    $ ep29_quests_pub_monica_knows_molly = True
    $ monicaWorkingAsDishwasher = True
    $ stage_Monica_shoots_array = ["1up", "1side", "1down", "2up", "2side", "2down", "3up", "3side", "3down", "4up", "4side", "4down", "5up", "5side", "5down", "6up", "6side", "6down", "7up", "7side", "7down", "8up", "8side", "8down", "9up", "9side", "9down", "18up", "18side", "18down", "19up", "19side", "19down", "20up", "20side", "20down", "21up", "21side", "21down", "22up", "22side", "22down", "23up", "23side", "23down", "24up", "24side", "24down", "25up", "25side", "25down", "26side"]
#    $ stage_Monica_shoots_array = ["1up", "1side", "1down", "2up", "2side", "2down", "3up", "3side", "3down", "4up", "4side", "4down", "5up", "5side", "5down", "6up", "6side", "6down", "7up", "7side", "7down", "8up", "8side", "8down", "9up", "9side", "9down", "10up", "10side", "10down", "11up", "11side", "11down", "12up", "12side", "12down", "13up", "13side", "13down", "14up", "14side", "14down", "15up", "15side", "15down", "16up", "16side", "16down", "17up", "17side", "17down", "18up", "18side", "18down", "19up", "19side", "19down", "20up", "20side", "20down", "21up", "21side", "21down", "22up", "22side", "22down", "23up", "23side", "23down", "24up", "24side", "24down", "25up", "25side", "25down", "26up", "26side", "26down"]
    if pubDanceCount < 10:
        $ pubDanceCount = 30
    $ stage_shoots_total_amount_cur = 27 + stage_shoots_total_amount_nude
#    $ stage_shoots_total_amount_cur = 78
    $ monicaDancingStage = 2
    $ stage_low_tips = True
    $ stage_dance_nude_planned = True
    $ monicaDancingJoeAskedAboutPrivate = True
    $ ep210_quests_stage = 5
    if stage_dance_nude_last_day == 0:
        $ stage_dance_nude_last_day = 210
    $ monicaAshleyTalkedAboutSharingTips = True
    $ ep215_quests_ashley_dialogue2_active = True
    $ ep213_quests_stole_tips_count = 3

    # house
    $ bardieBlackmailStage = 5
    $ bardieMonicaNonNudeCount = bardieCleaningNonNudeDuringPunishment - 1
    $ bardieFollowMonicaDuringCleaning = True
    $ monicaMustNotWearPanties = True
    $ bettyMustNotWearPanties = True
    $ monicaMustWearBettyPanties = False
    $ monicaLaundryBettyPantiesSelectMode = 1 #Выбор в прачечной
    $ monicaLaundryBettyPantiesSelectNudeDisabled = False
    $ spotCleaning = True
    $ floor2WashingSport = True
    $ monica_tint = [1.0, 1.0, 1.0]
    $ bettyOffendedBardieKitchen = True

    if monicaEarnedWeeklyMoney == False:
        $ add_objective("money_for_victoria", t_("Заработать $ 5000 для Виктории до Пятницы!"), c_pink, 10)

    $ define_inventory_object("food_package", {"description" : t_("Еда"), "label_suffix" : "_use_food", "default_label" : False, "default_nolabel" : "cant_use", "icon" : "Inventory/food_package" + res.suffix + ".png"})

    call food_basement_room_init() from _rcall_food_basement_room_init

    $ basementBedSkipUntilFridayEnabled = True
    $ monicaCasualDressWearFirstTimeWardrobe = False
    $ gameStage = 0
    $ gameSubStage = 0
    $ afterJail = True
    $ rain = False
    $ sceneIsStreet = False
    $ game_version1_screen_ready_to_render = True
    $ zoom_factor = 1
    $ monicaEatedLastDay = day-1
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

#    $ episode2part2_initialized = True
    img black_screen
#    m "part2 init!"
    call part2_questions_process(False) from _rcall_part2_questions_process_1

    call monica_cheats_init() from _rcall_monica_cheats_init_2
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

    $ hudDaySkipToEveningEnabled = True
    $ map_enabled = True
    $ map_disabled_forced = False

    $ cloth = "CasualDress1"
    $ cloth_type = "CasualDress"
    $ changeDayTime("day")

    call citizens_init_day() from _rcall_citizens_init_day
    call Bardie_Life_day() from _rcall_Bardie_Life_day
    call Betty_Life_day() from _rcall_Betty_Life_day
    call Ralph_Life_day() from _rcall_Ralph_Life_day
    call Fred_Life_day() from _rcall_Fred_Life_day
    call Biff_Life_day() from _rcall_Biff_Life_day
    call Melanie_Life_day() from _rcall_Melanie_Life_day
    call Dick_Life_day() from _rcall_Dick_Life_day
    call Pub_Life_day() from _rcall_Pub_Life_day
    $ set_active(False, group="workers", scene="working_office")
    $ set_active(False, group="workers", scene="working_office2")
    call office_life_day() from _rcall_office_life_day
    call Steve_Life_day() from _rcall_Steve_Life_day

    call change_scene("street_house_outside") from _rcall_change_scene_219
    call process_change_map_location("House") from _rcall_process_change_map_location_9
    call refresh_scene_fade_long() from _rcall_refresh_scene_fade_long_28
    jump start_game_EP22

label part2_questions_process(new_game_started):
    if 1==2:
        help "Продолжение квеста ищите во второй части эпизода!"
    help "Добро пожаловать в Fashion Business: Episode 2 part 2!"
    help "Вторая часть эпизода начинается сразу после завершения первой."
    if new_game_started == False:
        pass
#        help "Если в вашем сохранении некоторые квесты не завершены, то будут заданы вопросы о принятых решениях в них."
    else:
        help "Будут заданы основные вопросы о решениях, принятых во время игры."
        help "Для сохранения всех сделанных выборов, рекомендуется использовать сохраненную игру из Episode 2 part 1."

    music Groove2_85

    if new_game_started == True:
        call intro_questions() from _rcall_intro_questions
        help "Действия во втором эпизоде."
    imgf 32167
    help "Где закончилась часть 1?"
    menu:
        "Основной сюжет.":
            pass
        "Тренировка у Маркуса (продолжение квеста в следующих апдейтах) (disabled)":
            pass
        "Путь мести (продолжение квеста в следующих апдейтах) (disabled)":
            pass

    if new_game_started == True or ep2p2_flag1 != True:
        call part2_questions_loadgame_comment() from _rcall_part2_questions_loadgame_comment
        imgf 7992
        help "Показывала-ли Моника Виктории грудь для фото?"
        menu:
            "Показывала.":
                $ monicaShowedBoobsToVictoriaCamera = True
            "Обошлась без этого.":
                $ monicaShowedBoobsToVictoriaCamera = False
        $ ep22_questions_answered_count += 1

        imgf 8085
        help "Моника раздевалась перед Диком в его кабинете?"
        menu:
            "Моника разделась.":
                $ monicaShowedAssToDickAndVictoria = True
            "Моника просто ушла":
                $ monicaShowedAssToDickAndVictoria = False
        $ ep22_questions_answered_count += 1

    if new_game_started == True or melanieDisappearedAndReturned == False:
        call part2_questions_loadgame_comment() from _rcall_part2_questions_loadgame_comment_1
        imgf 9195
        help "Моника проходила кастинг с Мелани?"
        menu:
            "Моника прошла унизительный кастинг c Мелани.":
                $ monicaMelanieCastingPlanned = True
                $ monicaMelanieCastingLickedDildo = True
            "Моника была в хороших отношениях с Мелани и попросила помочь ей без кастинга.":
                $ monicaMelanieCastingPlanned = False
                $ monicaMelanieCastingLickedDildo = False
        $ ep22_questions_answered_count += 1

    if new_game_started == True or ep27_melanie_going_to_victoria == False:
        call part2_questions_loadgame_comment() from _rcall_part2_questions_loadgame_comment_2
        imgf 13965
        help "Пошла-ли Мелани на встречу к Виктории? (линия квестов с Викторией)"
        menu:
            "Мелани пошла к Виктории.":
                $ ep27_melanie_going_to_victoria = True
                $ ep27_melanie_visited_victoria = True

            "Мелани не стала общаться с ней.":
                $ ep27_melanie_refused_victoria_friendship = True
        $ ep22_questions_answered_count += 1

    if ep27_melanie_refused_victoria_friendship == True:
        $ ep27_melanie_visited_victoria = False
        $ ep27_melanie_going_to_victoria = False
        if map_objects.has_key("Teleport_VictoriaHome"):
            $ del map_objects["Teleport_VictoriaHome"]
        $ char_info["DickSecretary"]["caption"] = t_("Виктория ждет свои деньги еженедельно.")

    if ep27_melanie_going_to_victoria == True:
        if new_game_started == True or ep216_victoria_visit_day1 == False:
            call part2_questions_loadgame_comment() from _rcall_part2_questions_loadgame_comment_3
            imgf 40604
            help "Моника согласилась с Викторией, что Мелани поступила неправильно, пытаясь показать видео Дику?"
            menu:
                "Моника согласилась с Викторией что Мелани была неправа.":
                    $ melanieVictoriaMonicaTable1 = True
                "Моника попыталась оправдать Мелани.":
                    $ melanieVictoriaMonicaTable1 = False
            $ ep22_questions_answered_count += 1


    if new_game_started == True or (monica_ralph_relationships_type == 0 and ep214_ralph_blowjob_day == 0):
        call part2_questions_loadgame_comment() from _rcall_part2_questions_loadgame_comment_4
        imgf 31561
        help "Моника вступила в отношения с Ральфом с целью вернуть свой дом?"
        menu:
            "Моника вступила в отношения с Ральфом":
                $ ep214_ralph_blowjob_day = 210
                $ monicaBardieRalphSeducingStage = 6
#            "Моника вступила в отношения с Ральфом.":
#                $ questLog(80, True)
#                $ ep214_ralph_blowjob_day = 210
#                $ monicaBardieRalphSeducingStage = 6
#                $ monica_ralph_relationships_type = 1
#                $ monicaBettyRalphSeduction8 = True
#            "Моника вступила в отношения с Ральфом и сказала что любит его.":
#                $ questLog(81, True)
#                $ ep214_ralph_blowjob_day = 210
#                $ monicaBardieRalphSeducingStage = 6
#                $ monica_ralph_relationships_type = 2
#                $ monicaBettyRalphSeduction9 = True
            "Моника не стала вступать в отношения с Ральфом (отказ от линии квестов в доме).":
                $ questLog(81, False)
                $ remove_hook(label="Monica_Ralph_Quest_regular")
                $ remove_hook(label="Monica_Ralph_Quest")
                $ monicaBardieRalphSeducingStage = 0
                $ char_info["Ralph"]["level"] = 1
                $ char_info["Ralph"]["current_progress"] = 0
                $ char_info["Ralph"]["caption"] = t_("Ральф примерный семьянин.")
        $ ep22_questions_answered_count += 1

    if new_game_started == True or bardieHeardAboutMarcus != True:
        call part2_questions_loadgame_comment() from _rcall_part2_questions_loadgame_comment_5
        imgf 7249
        help "Был-ли у Бетти секс со Фредом?"
        menu:
            "Бетти имела секс со Фредом.":
                $ bettyTouchedFredDick = True
                $ bettyFredLandrySexPlanned = True
                $ bettyFredLaundryHasSex = True
            "Бетти не стала изменять Ральфу со Фредом.":
                $ bettyTouchedFredDick = False
                $ bettyFredLandrySexPlanned = False
                $ bettyFredLaundryHasSex = False
        $ ep22_questions_answered_count += 1

    if bettyFredLaundryHasSex == True and (new_game_started == True or ep215_quests_betty_stage == 0 or ep215_quests_betty_visit2_completed_day == 0):
        call part2_questions_loadgame_comment() from _rcall_part2_questions_loadgame_comment_6
        $ ep215_quests_betty_stage = 1
        imgf 19262
        help "Согласилась-ли Бетти помочь своему соседу в решении его проблемы?"
        menu:
            "Бетти помогла соседу.":
                $ ep215_quests_betty_visit2_completed_day = 210
                $ ep215_quests_betty_refused = False
            "Бетти отказала соседу и ушла.":
                $ ep215_quests_betty_visit2_completed_day = 0
                $ ep215_quests_betty_refused = True
        $ ep22_questions_answered_count += 1

    if new_game_started == True or (monicaAgreedToSellDress == False and monicaBoughtCasualDress1 == False and monicaKickedVivianForDress == False):
        call part2_questions_loadgame_comment() from _rcall_part2_questions_loadgame_comment_7
        imgf 10646
        help "Как Моника получила красивое платье?"
        $ remove_hook(label="cloth_shop_enter_refuse")
        $ remove_hook(label="cloth_shop_quests")
        $ remove_hook(label="steal_dress")
        menu:
            "Моника работала манекеном.":
                $ monicaLickedVivianNipple = True
                $ monicaBoughtCasualDress1 = False
                $ monicaKickedVivianForDress = False
                $ monicaAgreedToSellDress = True
                $ shopVisitorStage10 = 3
                $ add_hook("Teleport_Cloth_Shop_Entrance", "ep25_quests_shop4c", scene="street_cloth_shop", label="cloth_shop_enter_refuse")
                imgf 11219
                help "Моника заставила покупатели купить платье силой или сделала что он требовал?"
                menu:
                    "Моника обслужила покупателя за покупку платья.":
                        $ monicaOffendedCit3 = False
                    "Моника угрожала покупателю и заставила купить его платье так.":
                        $ monicaOffendedCit3 = True
                $ ep22_questions_answered_count += 1

            "Моника купила платье за деньги.":
                $ monicaLickedVivianNipple = False
                $ monicaBoughtCasualDress1 = True
                $ monicaKickedVivianForDress = False
                $ monicaAgreedToSellDress = False
                $ shopVisitorStage10 = 0
                $ add_hook("Teleport_Cloth_Shop_Entrance", "ep25_quests_shop4", scene="street_cloth_shop", label="cloth_shop_enter_refuse")

            "Моника ударила продавщицу и убежала.":
                $ monicaLickedVivianNipple = False
                $ monicaBoughtCasualDress1 = False
                $ monicaKickedVivianForDress = True
                $ monicaAgreedToSellDress = False
                $ shopVisitorStage10 = 0
                $ add_hook("Teleport_Cloth_Shop_Entrance", "ep25_quests_shop4", scene="street_cloth_shop", label="cloth_shop_enter_refuse")
        $ ep22_questions_answered_count += 1

    if (new_game_started == True or monicaHasSchoolOutfit1Day == 0) and monicaKickedVivianForDress == False:
        call part2_questions_loadgame_comment() from _rcall_part2_questions_loadgame_comment_8
        imgf 22254
        help "Получила-ли Моника скидку на одежду для колледжа?"
        $ monicaHasSchoolOutfit1Day = 210
        menu:
            "Моника согласилась получить скидку.":
                $ monicaBoughtSchoolOutfitByLicking = True
            "Моника решила заплатить полную сумму.":
                $ monicaBoughtSchoolOutfitByLicking = False
        $ ep22_questions_answered_count += 1

    if new_game_started == True or (juliaQuestMonicaRefusedFred == False and juliaQuestRefused == False and monica_living_at_juliahome == False):
        call part2_questions_loadgame_comment() from _rcall_part2_questions_loadgame_comment_9
        imgf 23099
        help "Состоит-ли Моника в отношениях с Юлией и живет вместе с ней?"
        menu:
            "Моника живет с Юлией и претворяется что любит ее.":
                $ monica_living_at_juliahome = True
                $ workingOfficeCabinetJuliaSuffix = 3
                $ ep210_julia_kissed_day_day = 210
                $ monicaJuliaLoveStory7 = True
                $ ep210_julia_evening_at_work = True
                if ep210_monica_julia_massage_count == 0:
                    $ ep210_monica_julia_massage_count = 1
            "Моника поставила Юлию на место и Юлия боится Монику.":
#                $ juliaQuestMonicaRefusedFred = True
                $ juliaQuestRefused = True

        $ ep22_questions_answered_count += 1

    if juliaQuestMonicaRefusedFred == True or juliaQuestRefused == True:
        $ char_info["Julia"]["level"] = 1
        $ char_info["Julia"]["current_progress"] = 0
        $ char_info["Julia"]["caption"] = t_("Юлия боится Монику")
        $ minimapJuliaGenerateEnabled = False
        $ clear_hooks("Julia", scene="working_office_cabinet")
        $ add_hook("Julia", "ep26_quests_office7", scene="working_office_cabinet")
        $ monica_living_at_juliahome = False
        $ questLog(64, False)
        $ questLog(73, False)
        $ questLog(74, False)
        if map_objects.has_key("Teleport_JuliaHome"):
            $ del map_objects["Teleport_JuliaHome"]
            $ set_active("Teleport_JuliaHome", False, scene="street_corner")
    else:
        call ep218_quests_julia_init() from _rcall_ep218_quests_julia_init_1


    if new_game_started == True or marcus_visit1_completed == False:
        call part2_questions_loadgame_comment() from _rcall_part2_questions_loadgame_comment_10
        imgf 18418
        help "Была-ли Моника у Маркуса?"
        menu:
            "Моника была у Маркуса и вернулась.":
                $ marcus_visit1_completed = True
                imgf 21279
                help "Ставила ли Моника заключенных на место или исполняла их требования?"
                menu:
                    "Моника поддалась на шантаж заключенных.":
                        $ ep28_quests_monica_offended_day1 = True
                        $ ep28_quests_monica_offended_day2 = True
                        $ ep28_quests_monica_offended_day3 = True
                    "Моника поставила заключенных на место.":
                        $ ep28_quests_monica_offended_prisoners = True
                $ ep22_questions_answered_count += 1
            "Моника не стала посещать Маркуса.":
                pass
        $ ep22_questions_answered_count += 1

    if new_game_started == True or monica_pub_name == False:
        call part2_questions_loadgame_comment() from _rcall_part2_questions_loadgame_comment_11
        imgf 9600
        help "Как Моника назвалась в Shiny Hole?"
        $ monica_pub_name = t__("Мэрилин")
        if renpy.android == True:
            call screen input_softkeyboard
            $ monica_pub_name = _return
        else:
            $ monica_pub_name = renpy.input(t__("Меня зовут... (enter для ввода)"), monica_pub_name)
#        with fadelong
        if bool(monica_pub_name) == False or str(monica_pub_name) == "False":
            $ monica_pub_name = t__("Мэрилин")
        $ ep22_questions_answered_count += 1

    if new_game_started == True or (monicaPubFiredTips1 == False and monica_shiny_hole_queen_day == 0):
        call part2_questions_loadgame_comment() from _rcall_part2_questions_loadgame_comment_12
        imgf 31928
        help "Стала-ли Моника королевой Shiny Hole или уволилась?"
        menu:
            "Моника стала королевой Shiny Hole!":
                $ monica_shiny_hole_queen_day = 210
            "Моника уволилась из паба.":
                $ monica_shiny_hole_queen_day = 0
                $ monicaPubFiredTips1 = True
        $ ep22_questions_answered_count += 1
    if monicaPubFiredTips1 == True:
        $ add_hook("Teleport_Hostel_Pub", "ep211_dialogues5_shiny_hole_7", scene="hostel_street", label="monica_pub_fired_block", priority = 10001)
        $ questLog(69, True)
        $ questLog(66, False)
        $ questLog(52, False)
        $ questLog(48, False)
        $ questLog(49, False)
        $ questLog(50, False)
        $ questLog(51, False)
        $ questLog(53, False)
        $ questLog(57, False)
        $ questLog(60, False)
        $ questLog(58, False)
        $ questLog(59, False)
        $ questLog(75, False)
        $ questLog(84, False)
        $ clear_hooks("exit_scene", scene="pub")
        $ clear_hooks("exit_scene", scene="pub_makeuproom")

    if new_game_started == True or (fallingPathServedCustomersTotal == 0 and fallingPathStarted == False):
        call part2_questions_loadgame_comment() from _rcall_part2_questions_loadgame_comment_13
        imgf 13195
        help "Моника обслуживает клиентов в трущобах?"
        menu:
            "Моника время от времени зарабатывает на клиентах на улице.":
                $ fallingPathStarted = True
                pass
            "Моника не стала связываться с улицей вовсе.":
                $ fallingPathStarted = False
                $ fallingPathServedCustomersTotal = 0
                $ questLog(17, False)
                $ questLog(22, False)
                $ questLog(83, False)
                $ questLog(82, False)
                $ questLog(22, False)
                $ questLog(22, False)
                $ questLog(22, False)
                $ remove_hook(label="Mommy_Whore_Quest_dialogue")
                $ remove_hook(label="Mommy_Whore_Quest")
                $ remove_hook(label="Perry_Debt")
                $ remove_hook(label="Perry_Debt_talk")
                $ remove_hook(label="Perry_Debt_beforesleep")
        $ ep22_questions_answered_count += 1

    if slumsApartmentsMonicaKnow == True:
        if slumsApartmentsRentActive == False:
            $ slumsApartmentsStatus = 1
            $ del(map_objects["Teleport_Slums_Apartments"])
            $ slumsDirtyStreetMiniMapActive = True
            $ slumsApartmentsMiniMapActive = False
            $ set_active("Teleport_Slums_Apartments", False, scene="hostel_street")
            $ questLog(71, False)
    else:
        if new_game_started == True or slumsApartmentsMonicaKnow == False:
            call part2_questions_loadgame_comment() from _rcall_part2_questions_loadgame_comment_14
            $ slumsApartmentsMonicaKnow = True
            $ slumsApartmentsRentStarted = True
            $ slumsApartmentsShawarmaTraderDialogue1Active = True
            imgf 16995
            help "Моника арендует апаратаменты в трущобах?"
            menu:
                "Моника снимает апартаменты.":
                    $ slumsApartmentsMiniMapActive = True
                    $ slumsDirtyStreetMiniMapActive = False
    #                $ slumsApartmentsShawarmaTraderDialogue1Active = True
                    $ slumsApartmentsStatus = 2
                    $ monicaHomeMiniMapEnabled = True
                    $ slumsApartmentsRentActive = True
                    $ slumsApartmentsRentActiveDay = int(day/7)-2
                    $ add_objective("earn_money_rent_apartments", t_("Заработать $ 300 за аренду апартаментов до субботы."), c_green, 30)
                    if check_inventory("keys_apartments",1) != True:
                        $ add_inventory("keys_apartments", 1, True)

                "Моника не снимает апартаменты.":
                    $ slumsApartmentsStatus = 1
                    $ del(map_objects["Teleport_Slums_Apartments"])
                    $ slumsDirtyStreetMiniMapActive = True
                    $ slumsApartmentsMiniMapActive = False
                    $ set_active("Teleport_Slums_Apartments", False, scene="hostel_street")
                    $ questLog(71, False)
            $ ep22_questions_answered_count += 1

    if new_game_started == True or charityEventCompleted == False:
        call part2_questions_loadgame_comment() from _rcall_part2_questions_loadgame_comment_15
        $ charityEventCompleted = True
        imgf 6757
        help "Согласилась Моника на предложение Филиппа или пообещала Бифу быть хорошей цыпочкой?"
        menu:
            "Моника согласилась сделать минет Филиппу в туалете отеля.":
                $ monicaSaidBiffSheIsWillBeAGoodChick = False
                $ monicaMadeBlowjobToHotelStaff = True
                $ monicaMadeBlowjobToPhilip = True
            "Моника пообещала Бифу быть хорошей цыпочкой.":
                $ monicaSaidBiffSheIsWillBeAGoodChick = True
                $ monicaMadeBlowjobToHotelStaff = False
                $ monicaMadeBlowjobToPhilip = False
        $ ep22_questions_answered_count += 1

    if monicaPhillipHotelKick == False:
        if new_game_started == True or monica_philip_visits == 0:
            call part2_questions_loadgame_comment() from _rcall_part2_questions_loadgame_comment_16
            imgf 16381
            help "Работает-ли Моника субботней шлюхой номер 2 у Филиппа?"
            menu:
                "Моника посещает Филиппа.":
                    $ monica_philip_visits = 5
                    $ monica_philip_visited_last_day = 210
                    $ monica_philip_visits_blowjobs = 5
                    $ monica_philip_visits_sex = 5
                    $ monica_philip_visits_swallowed = 3
                    $ monica_philip_visits_double_blowjobs = 3
                    $ monica_philip_visits_threesomes = 5
                "Моника не ходит к Филиппу.":
                    pass
            $ ep22_questions_answered_count += 1
    else:
        # если ударила Филиппа
        $ del map_objects["Teleport_PhilipHome"]

    $ char_info["ReceptionGirl"]["enabled"] = True
    if new_game_started == True or (monica_escort_service_started == False and ep212_escort_monica_fired == False and ep212_escort3_monica_fired == False and ep212_escort5_monica_fired == False):
        call part2_questions_loadgame_comment() from _rcall_part2_questions_loadgame_comment_17
        imgf 16339
        help "Работает-ли Моника в ВИП-Эскорте?"
        menu:
            "Моника работает в эскорте.":
                $ monicaHotelAdminAgreement3 = True
                $ monica_escort_service_started = True
                $ monica_escort_service_started_day = 210
                $ monicaEscortLindaTable1 = True
                $ char_info["ReceptionGirl"]["caption"] = t_("Сутенерша в Le Grand.")
            "Моника работала в эскорте, но уволилась.":
                $ monicaEscortLindaTable1 = True
                $ monicaHotelAdminAgreement3 = True
                $ monica_escort_service_started = True
                $ monica_escort_service_started_day = 210
                $ ep212_escort_monica_fired = True
                $ ep212_escort3_monica_fired = True
                $ ep212_escort5_monica_fired = True
                $ add_hook("Teleport_Rich_Hotel_Reception", "ep212_dialogues3_escort_hotel_7_2", scene="street_rich_hotel", priority = 500) # Блокируем вход в отель
                $ questLog(62, False)
                $ char_info["ReceptionGirl"]["caption"] = t_("Сутенерша в Le Grand.")
            "Моника никогда не работала в эскорте.":
                $ monicaHotelAdminAgreement3 = False
                $ monica_escort_service_started = False
                $ monica_escort_service_started_day = 0
                $ clear_hooks("ReceptionGirl", scene="rich_hotel_reception")
                $ clear_hooks("Teleport_Restaurant", scene="rich_hotel_reception")
                $ add_hook("Teleport_Restaurant", "ep26_quests_restaurant2", scene="rich_hotel_reception", label="reception_capturing_monica")
                $ set_active("Teleport_Lift", False, scene="rich_hotel_reception")
                $ char_info["ReceptionGirl"]["caption"] = t_("Администратор отеля.")
                $ char_info["ReceptionGirl"]["level"] = 1
                $ char_info["ReceptionGirl"]["current_progress"] = 0
                $ remove_hook(label="rich_hotel_door_block")
                $ questLog(62, False)
        $ ep22_questions_answered_count += 1

    if (new_game_started == True and monica_escort_service_started == True) or (monica_escort_service_started == True and monica_hotel_name == False):
        call part2_questions_loadgame_comment() from _rcall_part2_questions_loadgame_comment_18
        # если работает или работала
        imgf 16328
        help "Какой Моника выбрала творческий псевдоним для работы в эскорте?"
        $ monica_hotel_name = t__("Снежанна")
        if renpy.android == True:
            call screen input_softkeyboard
            $ monica_hotel_name = _return
        else:
            $ monica_hotel_name = renpy.input(t__("Меня зовут... (enter для ввода)"), monica_hotel_name)
        if monica_hotel_name == False:
            $ monica_hotel_name = t__("Снежанна")

    if (new_game_started == True and monica_escort_service_started == True and ep212_escort_monica_fired == False) or (monica_escort_service_started == True and monicaEscortScene6Day == 0 and ep212_escort_monica_fired == False):
        call part2_questions_loadgame_comment() from _rcall_part2_questions_loadgame_comment_19
        imgf 18798
        help "Стала-ли Моника мстить Миранде в присутствии постоянного клиента в номере отеля?"
        menu:
            "Моника унизила Миранду при клиенте.":
                $ monicaEscortRevengeGirl2 = True
                $ monicaEscortScene6Day = 210
                $ monicaEscortRevengeGirl4 = True
                $ ep214_dialogues3_escort_10_flag1 = True
                $ ep214_dialogues3_escort_10_flag2 = True
                $ ep212_escort3_completed = True
            "Моника не стала унижать Миранду.":
                $ monicaEscortRevengeGirl2 = False
                $ monicaEscortScene6Day = 210
                $ ep212_escort3_completed = True
        $ ep22_questions_answered_count += 1


    if (new_game_started == True and monica_escort_service_started == True and ep212_escort_monica_fired == False) or (monica_escort_service_started == True and monicaBiffInvestorDate1 == False and ep212_escort_monica_fired == False):
        call part2_questions_loadgame_comment() from _rcall_part2_questions_loadgame_comment_20
        $ monicaBiffInvestorDate1 = True
        imgf 40128
        help "Стала-ли Моника мстить Линде?"
        menu:
            "Моника унизила Линду в номере отеля перед инвестором.":
                $ monicaBiffInvestorDate2 = False
                $ monicaBiffInvestorDate5 = False
                $ monicaBiffInvestorDate8 = True
                $ monicaBiffInvestorDate4 = True
                $ ep215_quests_linda_restaurant_dialogue_planned = True
            "Моника конфликтует с Линдой, но не унижала ее.":
                $ monicaBiffInvestorDate2 = False
                $ monicaBiffInvestorDate5 = True
                $ monicaBiffInvestorDate8 = False
                $ monicaBiffInvestorDate4 = True
            "Моника не ездила в номер с инвестором, заставив пообещать инвестировать при его жене.":
                $ monicaBiffInvestorDate2 = True
                $ monicaBiffInvestorDate5 = False
                $ monicaBiffInvestorDate8 = False
        $ ep22_questions_answered_count += 1

    if new_game_started == True or steveVisit2Day == 0:
        call part2_questions_loadgame_comment() from _rcall_part2_questions_loadgame_comment_21
        imgf 9953
        help "Моника угрожала Стиву вилкой?"
        menu:
            "Моника угрожала Стиву вилкой.":
                $ monicaSteveLivingRoomOffended = True
            "Моника не стала рисковать.":
                $ monicaSteveLivingRoomOffended = False
        $ ep22_questions_answered_count += 1


    if new_game_started == True or (monicaMadeBlowjobForSteveChair == False and monicaSteveCumDealRejected == False and monicaSteveCumDealCompleted == False):
        call part2_questions_loadgame_comment() from _rcall_part2_questions_loadgame_comment_22
        imgf 11430
        help "Моника заключала контракты со Стивом?"
        menu:
            "Моника заключила со Стивом контракт.":
                imgf 11526
                help "При заключении контрактов, Моника занималась сексом или делала минет?"
                menu:
                    "Моника занималась сексом.":
                        $ monicaHasSexWithSteveBasement = True
                        $ monicaSteveCumDealCompleted = True
                        imgf 10127
                        help "Толкнула-ли Моника Стива в бассейн?"
                        menu:
                            "Моника толкнула Стива в бассейн.":
                                $ monicaSteveBasementOffended = True
                                sound snd_water_splash
                            "Моника не стала толкать Стива.":
                                $ monicaSteveBasementOffended = False
                        $ ep22_questions_answered_count += 1
                    "Моника делала минет.":
                        $ monicaHasSexWithSteveBasement = False
                        $ monicaSteveCumDealCompleted = False
                        $ monicaSteveBlowjobDealCount = 1
                $ ep22_questions_answered_count += 1

                if new_game_started == True or bettyVisitedSteve == False:
                    imgf 12716
                    help "Моника видела секс Бетти со Стивом в его офисе?"
                    menu:
                        "Моника видела как Бетти изменяет со Стивом.":
                            $ bettySteveOfficeTouchedSteveDick = True
                            $ bettySteveOfficeSteveSex = True
                        "Моника не знает про это.":
                            $ bettyVisitedSteve = False
                            $ bettySteveOfficeTouchedSteveDick = False
                            $ bettySteveOfficeSteveSex = False
                    $ ep22_questions_answered_count += 1

            "Моника не стала связываться со Стивом.":
                $ monicaSteveBlowjobDealCount = 0
                $ monicaSteveCumDealRejected = True
                $ monicaSteveCumDealActive = False
        $ ep22_questions_answered_count += 1

    if new_game_started == True or (fredKickedByMonicaToBalls == False and fredKickedByMonicaToFace == False):
        call part2_questions_loadgame_comment() from _rcall_part2_questions_loadgame_comment_23
        imgf 8643
        help "Моника ударила Фреда в раздевалке?"
        menu:
            "Моника ударила Фреда.":
                $ fredKickedByMonicaToBalls = True
                $ fredKickedByMonicaToFace = False
            "Моника дала пощечину.":
                $ fredKickedByMonicaToBalls = False
                $ fredKickedByMonicaToFace = True
        $ ep22_questions_answered_count += 1

    if new_game_started == True:
        imgf 32436
        help "Пожалуйста, укажите развращенность Моники."
        menu:
            "Монике это не нравится, но тело - это самый главный инструмент для решения ее проблем.":
                $ corruption = 950
                $ biffCastingStage = 7
            "Моника периодически позволяла использовать свое тело для достижения целей.":
                $ corruption = 600
                $ biffCastingStage = 5
            "Моника лишь иногда соглашалась на небольшие вольности в отношении себя.":
                $ corruption = 300
                $ biffCastingStage = 3
            "Моника избегала любых пикантных ситуаций":
                $ corruption = 100
                $ biffCastingStage = 0
        help "Сколько денег Монике удалось скопить?"
        menu:
            "$ 50":
                $ money = 50
            "$ 100":
                $ money = 100
            "$ 200":
                $ money = 200

    imgf black_screen
    help "Спасибо за ответы!"
    help "Приключения Моники продолжаются!"
    fadeblack 2.0

    return

label part2_questions_loadgame_comment:
    if new_game_started == False and ep22_questions_answered_count == 0:
        imgf 32436
        help "Кажется в вашем сохранении некоторые квесты не завершены, сейчас будут заданы вопросы о принятых решениях в них."

    return


#Опросник для начала 2-ой части

# Где закончилась часть 1?
# Основной сюжет
# xxxТренировка у Маркуса
# Путь мести

#[Revenge Path]
#01. Был ли начат квест Путь мести? НО что под этим подразумевается? Непосредственно начало "Мести" или сначала квест на "Поиски ключа"?

#[Dick and Victoria storyline]
#xxx02. Собиралась ли Моника закатить иск своему соседу Лиаму?
# Моника показывала грудь Виктории для фото
# Моника проходила кастинг с Мелани?
# Пошла-ли Мелани на встречу к Виктории? (линия Виктории)
#xxx-- Когда Дик (в начале Эп2), у себя в кабинете, просит у Виктории разрешения "поцеловать попку", Виктория может ответить: "Можно, Мистер Дик..."; "Вы уже опоздали, Мистер Дик..." или "Я бы хотела чтобы Миссис Бакфетт первая сделала это... (отказать).
#20. Моника согласилась с Викторией, что Мелани была неправа, предложив поехать к Дику с ее телефоном, или попыталась оправдать Мелани?

#[Bardie storyline]
#xxx-- Было бы ОЧЕНЬ здорово дать возможность игроку "отвязать Барди" от событий с Ральфом. Тем более в "опроснике" он нигде "напрямую" не упоминается. Знаю, что многие "без ума" от ветки Барди. Но что делать тем, кому его ветка (и он сам) не нравится, но многие классные события в доме (без него) завязаны на нем. :confused:
#xxx-- Согласилась ли Моника притворяться Бетти? На данный момент это не обязательно.

#03. Согласилась ли Моника брать деньги у Ральфа или сказала, что любит его?

#[Betty storyline]
#-- У Бетти с Фредом был секс?
#xxx-- Бетти согласилась отнести соседу утюг? На данный момент это не обязательно.
#04. Бетти согласилась помочь своему соседу в решении его проблемы?
#--
#[Clothing Store storyline]
# Как Моника получила красивое платье?
#- Работала манекеном
#- Купила платье
#- Ударила продавщицу и убежала

# # Моника заставила покупателя купить платье силой
# Получила-ли Моника скидку на одежду для колледжа? (если работала манекеном)

#[Relationship with Julia]
#xxxx-- Моника согласилась выяснить цвет трусиков Юлии для Фреда? На данный момент это не обязательно.
#06. Состоит ли Моника в отношениях с Юлией и живет вместе с ней?

#[Office storyline]
#xx--  Продолжает ли Моника работать в офисе или сбежала? На данный момент (в поздних версиях) есть возможность "потерять" доверие Бифа и доступ в офис.
#07. Проводила ли Моника презентацию и фотосессию перед инвесторами? ???????? Она по-любому ее проводила?

#[Marcus storyline]
#08. Ставила ли Моника заключенных на место или исполняла их требования?
#09. Проходила ли Моника тренировки у Маркуса?

#[Falling Path]
#xxxx-- Работает ли Моника в Shiny Hole или уволилась? На данный момент есть возможность бросить работу в пабе.
#10. Стала ли Моника королевой Shiny Hole или уволилась?
#11. Сказала ли Моника правду о себе Клэр?
# Моника обслуживает клиентов в трущобах?

#x12. Разговаривала ли Моника с Перри и мамочкой в трущобах о ее долге перед Перри и работе у пилона?
#x13. Моника отрабатывает свой долг у Перри в хостеле?

#[Slum's apartment]
#x14. Моника арендует, либо арендовала ранее, апартаменты в трущобах у продавца кебабов Джека?
# Моника арендует апартаменты в трущобах? (Моника знает про апартаменты)

#[Escort Service]
#-- Было бы здорово (да-да, еще одна моя "хотелка" :innocent: ) дать возможность игроку "отвязать Филиппа" от событий эскорта. Филипп отдельно, эскорт отдельно (эх мечты-мечты).
#15. Работает ли Моника субботней шлюхой номер 2 у Филиппа?
# ВИП-эскорт
#- Моника работает в эскорте
#- Моника уволилась из эскорта
#- Моника не работала в эскорте

#17. Моника стала мстить Линде в присутствии инвестора в номере отеля Ле Гранд?
#18. Моника стала мстить брюнетке с эскорта в присутствии своего постоянного клиента в номере отеля Ле Гранд?

#[Steve storyline]
# Моника угрожала Стиву вилкой
#-- Послала ли Моника Стива сразу со всеми его контрактами (у бассейна) или согласилась на первый "контракт". (был секс или нет?)
# Скинула-ли Моника Стива в бассейн?
#19. При заключении контрактов со Стивом Моника занималась с ним сексом или делала минет?
# Моника видела секс Бетти со Стивом в его офисе?

# Моника ударила Фреда в раздевалке?



#--
#А еще, возникают вопросы про отношения между Моникой и НПС. Это выборы из Эп1-Эп2 и решения основанные на "сучности".
#Была ли добра Моника к Мелани и Алексу, к Кристине, к официантке в Ле Гранд и т.д.
#Ударила ли Моника Фреда в пах (в раздевалке) или ударила по лицу? Угрожала ли Моника Стиву вилкой или промолчала? Скинула его в бассейн или нет?
#Будет очень жалко все это потерять. Оно конечно практически не влияет на сюжет, но добавляет интерактивности, немного разнообразия и делает НПС более живыми. Мне кажется это важно.


# Вход в полицию продолжение сюжета
# Оставляем танцы у пилона (кроме Клэр)
# Эскорт оставляем последнюю сцену конфликта с девочками
# С Ральфом оставляем все
# С Барди оставляем вебку и подглядывание во время уборки, а также наказание
# Офис все открываем и оставляем 3 последние фотосессии (как повтор),
# Биф оставляем все кастинги, сбрасываем их на начало (если новая игра)
# Филип все убираем. Делаем что Филип прогоняет Монику
# Стив оставляем только blowjob без приходов секретарш
# Фитнесс убираем все, вариант только жать в раздевалке (Моника говорит что не хочет смотреть на этих дур)
# Трущобы флаеры убираем. Оставляем последние сцены с ситизенами (новые)
# Перри оставляем.
# Юлия оставляем все (под вопросом, надо смотреть на итоговый размер)


# апартаменты Мелани скрывать, если заблокирована ветка

# проверить, чтобы не начислялся долг Перри, если заблокированы трущобы

#

# эскорт если не работала
# если не снимает апартаменты, то нет выбора их возобновить
# трущобы клиенты не блокируются
