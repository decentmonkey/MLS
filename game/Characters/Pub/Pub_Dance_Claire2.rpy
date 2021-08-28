label pub_dance2_claire_dance2: # Танец с Клэр
    fadeblack 2.0

    $ stageMusicControlEnabled = True
    if stage_low_tips == True:
        $ pub_dance_dialogues_tips_list = 1
    else:
        $ pub_dance_dialogues_tips_list = 0
    music2 stop
    music Road_Trip
    sound2 highheels_short_walk
    imgfl 34194
    call dialogue_5_dance_strip_scene_menu() from _rcall_dialogue_5_dance_strip_scene_menu_1 # выбор музыки
    sound2 highheels_short_walk
    w
    imgf 34192
    w

    python:
        musicList = [
            {"intro":"track1_intro", "loop":"track1"},
            {"intro":"track2_intro", "loop":"track2"},
            {"intro":"track7_intro", "loop":"track7"},
            {"intro":"track3_intro", "loop":"track3"},
            {"intro":"track4_intro", "loop":"track4"},
            {"intro":"track5_intro", "loop":"track5"},
            {"intro":"track8_intro", "loop":"track8"},
            {"intro":"track6_intro", "loop":"track6"},
        ]
        if stageMusicMode == 0:
            stageLastMusic += 1
            if stageLastMusic >= len(musicList):
                stageLastMusic = 0
        if stageMusicMode == 1:
            stageLastMusic = rand(1,len(musicList)) - 1
        if stageMusicMode == 2:
            stageLastMusic = stageCustomMusic
        stageCurrentMusicIntro = musicList[stageLastMusic]["intro"]
        stageCurrentMusicLoop = musicList[stageLastMusic]["loop"]

    music stop
    img black_screen
    with diss
    pause 2.0
    music stageCurrentMusicIntro
    imgd 34193


    $ stage_Claire_Excitement_Last = 0
    $ stage_Claire_Excitement_Current = 0
    $ tmpMoney = money

    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = False
    $ loopCnt = 0

    $ pose = "claire_dance1"
label pub_dance2_claire_dance2_move1:
    $ loopCnt += 1
    $ notif_clean()
    show screen poledance()
    show screen love_bar_screen(stage_Claire_Excitement_Last, stage_Claire_Excitement_Current)
    $ result = ui.interact()
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    hide screen poledance_shoot
    hide screen poledance_coins
    if loopCnt == 1: # первый цикл
        img black_screen
        with fade
        pause 1.0
#        fadeblack 1.5
#        music stageCurrentMusicIntro
#        pause 0.5
    if result == "up":
        scene black
        image videov_Claire_Strip_1A = Movie(play="video/v_Claire_Strip_1A.mkv", fps=25, loop=False, image="/images/Slides/v_Claire_Strip_1A_end.jpg")
        show videov_Claire_Strip_1A
        pause 1.8
        hide videov_Claire_Strip_1A
        show screen poledance_shoot("/images/Slides/v_Claire_Strip_1A_end.jpg")
        wclean
        call pub_dance_claire2_dialogues_react(5) from _rcall_pub_dance_claire2_dialogues_react
        call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_48
        customers1 "Еееее, какая горячая штучка!"
        customers3 "Вау!"
    if result == "side":
        scene black
        image videov_Claire_Strip_1B = Movie(play="video/v_Claire_Strip_1B.mkv", fps=25, loop=False, image="/images/Slides/v_Claire_Strip_1B_end.jpg")
        show videov_Claire_Strip_1B
        pause 1.8
        hide videov_Claire_Strip_1B
        show screen poledance_shoot("/images/Slides/v_Claire_Strip_1B_end.jpg")
        wclean
        call pub_dance_claire2_dialogues_react(5) from _rcall_pub_dance_claire2_dialogues_react_1
        call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_49
        customers3 "Посмотрите на ее движения!"
        customers3 "Я хочу увидеть их без одежды!"
        customers2 "Твою мать! Когда же я доберусь до ее сисек?!"

    if result == "down":
        scene black
        image videov_Claire_Strip_1C = Movie(play="video/v_Claire_Strip_1C.mkv", fps=25, loop=False, image="/images/Slides/v_Claire_Strip_1C_end.jpg")
        show videov_Claire_Strip_1C
        pause 1.8
        hide videov_Claire_Strip_1C
        show screen poledance_shoot("/images/Slides/v_Claire_Strip_1C_end.jpg")
        wclean
        call pub_dance_claire2_dialogues_react(5) from _rcall_pub_dance_claire2_dialogues_react_2
        call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_50
        customers4 "Иди сюда, детка!"
        customers1 "Снимай трусики!"
        customers1 "Разденься для нас!"
        if monicaStripNudeClare1 == 0:
            customers5 "Я ее знаю, это Клэр! Она не раздевается!"

    if arrowUp == True or arrowSide == True or arrowDown == True:
        jump pub_dance2_claire_dance2_move1


    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = False
    $ loopCnt = 0

    $ pose = "claire_dance2"
label pub_dance2_claire_dance2_move2:
    $ loopCnt += 1
    $ notif_clean()
    show screen poledance()
    show screen love_bar_screen(stage_Claire_Excitement_Last, stage_Claire_Excitement_Current)
    $ result = ui.interact()
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    hide screen poledance_shoot
    hide screen poledance_coins
    if loopCnt == 1: # первый цикл
        fadeblack 1.5
        music stageCurrentMusicLoop
        pause 0.5
    if result == "up":
        scene black
        image videov_Claire_Strip_2A = Movie(play="video/v_Claire_Strip_2A.mkv", fps=25, loop=False, image="/images/Slides/v_Claire_Strip_2A_end.jpg")
        show videov_Claire_Strip_2A
        pause 1.8
        hide videov_Claire_Strip_2A
        show screen poledance_shoot("/images/Slides/v_Claire_Strip_2A_end.jpg")
        wclean
        call pub_dance_claire2_dialogues_react(10) from _rcall_pub_dance_claire2_dialogues_react_3
        call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_51
        customers1 "ОГО!! ВОТ ЭТО ДА!!!"
        customers5 "Снимай с себя все скорее!"
    if result == "side":
        scene black
        image videov_Claire_Strip_2B = Movie(play="video/v_Claire_Strip_2B.mkv", fps=25, loop=False, image="/images/Slides/v_Claire_Strip_2B_end.jpg")
        show videov_Claire_Strip_2B
        pause 1.8
        hide videov_Claire_Strip_2B
        show screen poledance_shoot("/images/Slides/v_Claire_Strip_2B_end.jpg")
        wclean
        call pub_dance_claire2_dialogues_react(10) from _rcall_pub_dance_claire2_dialogues_react_4
        call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_52
        customers1 "ОНА ИХ СНИМАЕТ, ОНА СНИМАЕТ ИХ!!!"
        customers3 "Дааа! Давай раздевайся!"
        customers2 "Хочу увидеть твою киску!"
    if result == "down":
        scene black
        image videov_Claire_Strip_2C = Movie(play="video/v_Claire_Strip_2C.mkv", fps=25, loop=False, image="/images/Slides/v_Claire_Strip_2C_end.jpg")
        show videov_Claire_Strip_2C
        pause 1.8
        hide videov_Claire_Strip_2C
        show screen poledance_shoot("/images/Slides/v_Claire_Strip_2C_end.jpg")
        wclean
        call pub_dance_claire2_dialogues_react(10) from _rcall_pub_dance_claire2_dialogues_react_5
        call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_53
        customers4 "Снимай их скорее и дай рассмотреть свою задницу!"

    if arrowUp == True or arrowSide == True or arrowDown == True:
        jump pub_dance2_claire_dance2_move2

    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    hide screen poledance_shoot
    hide screen poledance_coins

    img black_screen
    with diss
    pause 1.5
    sound Jump2
    img 34180 vpunch
    sound2 wow
    customers3 "ООООО! ОХРЕНЕТЬ!"
    customers4 "ДА, КЛЭР! ДАВАЙ, ДЕТКА!"

    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = False
    $ loopCnt = 0

    $ pose = "claire_dance3"
label pub_dance2_claire_dance2_move3:
    $ loopCnt += 1
    $ notif_clean()
    show screen poledance()
    show screen love_bar_screen(stage_Claire_Excitement_Last, stage_Claire_Excitement_Current)
    $ result = ui.interact()
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    hide screen poledance_shoot
    hide screen poledance_coins
    if loopCnt == 1: # первый цикл
        img black_screen
        with diss
        pause 1.0
#        fadeblack 1.5
#        music stageCurrentMusicLoop
#        pause 0.5
    if result == "up":
        scene black
        image videov_Claire_Strip_3A = Movie(play="video/v_Claire_Strip_3A.mkv", fps=25, loop=False, image="/images/Slides/v_Claire_Strip_3A_end.jpg")
        show videov_Claire_Strip_3A
        pause 1.8
        hide videov_Claire_Strip_3A
        show screen poledance_shoot("/images/Slides/v_Claire_Strip_3A_end.jpg")
        wclean
        call pub_dance_claire2_dialogues_react(10) from _rcall_pub_dance_claire2_dialogues_react_6
        sound3 men_scream5

        call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_54
        customers1 "Вот это да! Она разделась, разделась!"
    if result == "side":
        scene black
        image videov_Claire_Strip_3B = Movie(play="video/v_Claire_Strip_3B.mkv", fps=25, loop=False, image="/images/Slides/v_Claire_Strip_3B_end.jpg")
        show videov_Claire_Strip_3B
        pause 1.8
        hide videov_Claire_Strip_3B
        show screen poledance_shoot("/images/Slides/v_Claire_Strip_3B_end.jpg")
        wclean
        call pub_dance_claire2_dialogues_react(10) from _rcall_pub_dance_claire2_dialogues_react_7
#        call pub_dance_battle_dialogues_applause("std")
        sound3 men_scream2
        customers2 "Задери ножку повыше! Мне плохо видно!"
    if result == "down":
        scene black
        image videov_Claire_Strip_3C = Movie(play="video/v_Claire_Strip_3C.mkv", fps=25, loop=False, image="/images/Slides/v_Claire_Strip_3C_end.jpg")
        show videov_Claire_Strip_3C
        pause 1.8
        hide videov_Claire_Strip_3C
        show screen poledance_shoot("/images/Slides/v_Claire_Strip_3C_end.jpg")
        wclean
        call pub_dance_claire2_dialogues_react(10) from _rcall_pub_dance_claire2_dialogues_react_8
#        call pub_dance_battle_dialogues_applause("std")
        sound3 men_scream4
        customers5 "Эта красотка дает разглядеть себя хорошенько!"
        customers3 "Я бы засадил ей прямо на сцене, ААААА!"

    if arrowUp == True or arrowSide == True or arrowDown == True:
        jump pub_dance2_claire_dance2_move3

    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = False
    $ loopCnt = 0

    $ pose = "claire_dance4"
label pub_dance2_claire_dance2_move4:
    $ loopCnt += 1
    $ notif_clean()
    show screen poledance()
    show screen love_bar_screen(stage_Claire_Excitement_Last, stage_Claire_Excitement_Current)
    $ result = ui.interact()
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    hide screen poledance_shoot
    hide screen poledance_coins
#    if loopCnt == 1: # первый цикл
#        fadeblack 0.5
#        music stageCurrentMusicLoop
#        pause 0.5
    if result == "up":
        scene black
        image videov_Claire_Strip_4A = Movie(play="video/v_Claire_Strip_4A.mkv", fps=25, loop=False, image="/images/Slides/v_Claire_Strip_4A_end.jpg")
        show videov_Claire_Strip_4A
        pause 1.8
        hide videov_Claire_Strip_4A
        show screen poledance_shoot("/images/Slides/v_Claire_Strip_4A_end.jpg")
        wclean
        call pub_dance_claire2_dialogues_react(10) from _rcall_pub_dance_claire2_dialogues_react_9
        call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_55
        customers2 "Какая задница! Я ее такой себе и представлял!"
        customers5 "Раздвинь ножки шире, красотка! Хочу разглядеть твою киску!"
    if result == "side":
        scene black
        image videov_Claire_Strip_4B = Movie(play="video/v_Claire_Strip_4B.mkv", fps=25, loop=False, image="/images/Slides/v_Claire_Strip_4B_end.jpg")
        show videov_Claire_Strip_4B
        pause 1.8
        hide videov_Claire_Strip_4B
        show screen poledance_shoot("/images/Slides/v_Claire_Strip_4B_end.jpg")
        wclean
        call pub_dance_claire2_dialogues_react(10) from _rcall_pub_dance_claire2_dialogues_react_10
        call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_56
        customers1 "ЕЕЕЕ! Давай-давай!"
        customers5 "Я тащусь от этой крошки!"
    if result == "down":
        scene black
        image videov_Claire_Strip_4C = Movie(play="video/v_Claire_Strip_4C.mkv", fps=25, loop=False, image="/images/Slides/v_Claire_Strip_4C_end.jpg")
        show videov_Claire_Strip_4C
        pause 1.8
        hide videov_Claire_Strip_4C
        show screen poledance_shoot("/images/Slides/v_Claire_Strip_4C_end.jpg")
        wclean
        call pub_dance_claire2_dialogues_react(10) from _rcall_pub_dance_claire2_dialogues_react_11
        call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_57
        customers2 "Вот это задница, наконец-то!"
        customers3 "Я не могу, я сейчас кончу! ААААА!!!"
        customers2 "Приласкай свою киску! Покажи, как ты делаешь это!"

    if arrowUp == True or arrowSide == True or arrowDown == True:
        jump pub_dance2_claire_dance2_move4

    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    hide screen poledance_shoot
    hide screen poledance_coins
    fadeblack 1.5
    music stageCurrentMusicIntro
    # Клэр, когда во время танца поворачивается спиной к залу, поднимает руку к маске, снимает ее, но к залу не поворачивается
    imgf 34184
    w
    imgd 34185
    w
    imgd 34186
    w
    sound vjuh3
    img 34187 hpunch
    w
    # видно, что ей по кайфу, она проводит рукой по своей груди, прикрывая глаза
    imgf 34188
    w
    sound wow
    img 34189 vpunch
    w



    # потом медлит, не поворачиваясь и как-будто очнувшись снова надевает маску, поворачивается к залу и продолжает танец
    imgf 34187
    w
    imgd 34190
    w
    sound vjuh3
    img 34186 hpunch
    w
    imgd 34185
    w
    # один из посетителей пробирается к сцене в тот момент, когда она бросила трусики на сцену
    # его рука тянется к трусикам, хватет их и его силуэт быстро смывается оттуда
    imgf 34181
    w
    imgd 34182
    w
    sound Jump1
    img 34183 hpunch
    w
    imgf 34191


    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = False
    $ loopCnt = 0

    $ pose = "claire_dance5"
label pub_dance2_claire_dance2_move5:
    $ loopCnt += 1
    $ notif_clean()
    show screen poledance()
    show screen love_bar_screen(stage_Claire_Excitement_Last, stage_Claire_Excitement_Current)
    $ result = ui.interact()
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    hide screen poledance_shoot
    hide screen poledance_coins
    if loopCnt == 1: # первый цикл
        fadeblack 1.5
        music stageCurrentMusicLoop
        pause 0.5
    if result == "up":
        scene black
        image videov_Claire_Strip_5A = Movie(play="video/v_Claire_Strip_5A.mkv", fps=25, loop=False, image="/images/Slides/v_Claire_Strip_5A_end.jpg")
        show videov_Claire_Strip_5A
        pause 1.8
        hide videov_Claire_Strip_5A
        show screen poledance_shoot("/images/Slides/v_Claire_Strip_5A_end.jpg")
        wclean
        call pub_dance_claire2_dialogues_react(10) from _rcall_pub_dance_claire2_dialogues_react_12
        call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_58
        customers4 "Клэр! Наконец-то я увидел ее голой!"
        customers2 "Не толкайтесь, мне надо сделать фото!"
        call photoshop_flash() from _rcall_photoshop_flash_12
        w

    if result == "side":
        scene black
        image videov_Claire_Strip_5B = Movie(play="video/v_Claire_Strip_5B.mkv", fps=25, loop=False, image="/images/Slides/v_Claire_Strip_5B_end.jpg")
        show videov_Claire_Strip_5B
        pause 1.8
        hide videov_Claire_Strip_5B
        show screen poledance_shoot("/images/Slides/v_Claire_Strip_5B_end.jpg")
        wclean
        call pub_dance_claire2_dialogues_react(10) from _rcall_pub_dance_claire2_dialogues_react_13
        call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_59
        customers5 "Детка, снимай маску! Будь как те остальные развратные шлюхи!"
        customers1 "Снимай маску, ДА!"
        customers2 "Снимай маску и покажи нам мастерство танца Клэр!"
    if result == "down":
        scene black
        image videov_Claire_Strip_5C = Movie(play="video/v_Claire_Strip_5C.mkv", fps=25, loop=False, image="/images/Slides/v_Claire_Strip_5C_end.jpg")
        show videov_Claire_Strip_5C
        pause 1.8
        hide videov_Claire_Strip_5C
        show screen poledance_shoot("/images/Slides/v_Claire_Strip_5C_end.jpg")
        wclean
        call pub_dance_claire2_dialogues_react(10) from _rcall_pub_dance_claire2_dialogues_react_14
        call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_60
        customers2 "Она танцует чуть-ли не лучше всех!"
        customers1 "Маска, маска!"
        customers5 "Сними маску и сядь на шпагат, крошка!"
    if arrowUp == True or arrowSide == True or arrowDown == True:
        jump pub_dance2_claire_dance2_move5


    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = False
    $ loopCnt = 0

    $ pose = "claire_dance6"
label pub_dance2_claire_dance2_move6:
    $ loopCnt += 1
    $ notif_clean()
    show screen poledance()
    show screen love_bar_screen(stage_Claire_Excitement_Last, stage_Claire_Excitement_Current)
    $ result = ui.interact()
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    hide screen poledance_shoot
    hide screen poledance_coins
#    if loopCnt == 1: # первый цикл
#        fadeblack 1.5
#        music stageCurrentMusicLoop
#        pause 0.5
    if result == "up":
        scene black
        image videov_Claire_Strip_6A = Movie(play="video/v_Claire_Strip_6A.mkv", fps=25, loop=False, image="/images/Slides/v_Claire_Strip_6A_end.jpg")
        show videov_Claire_Strip_6A
        pause 1.8
        hide videov_Claire_Strip_6A
        show screen poledance_shoot("/images/Slides/v_Claire_Strip_6A_end.jpg")
        wclean
        call pub_dance_claire2_dialogues_react(10) from _rcall_pub_dance_claire2_dialogues_react_15
#        call pub_dance_battle_dialogues_applause("std")
        sound3 men_scream5
        customers1 "Ты чертовски охренительна, крошка!"
        customers2 "Я покупаю ее! Ведите ее в приват, скорее!"
        customers3 "Нет, мы все хотим видеть задницу Клэр! Танцуй еще!"

    if result == "side":
        scene black
        image videov_Claire_Strip_6B = Movie(play="video/v_Claire_Strip_6B.mkv", fps=25, loop=False, image="/images/Slides/v_Claire_Strip_6B_end.jpg")
        show videov_Claire_Strip_6B
        pause 1.8
        hide videov_Claire_Strip_6B
        show screen poledance_shoot("/images/Slides/v_Claire_Strip_6B_end.jpg")
        wclean
        call pub_dance_claire2_dialogues_react(10) from _rcall_pub_dance_claire2_dialogues_react_16
#        call pub_dance_battle_dialogues_applause("std")
        sound3 men_scream2
        customers5 "Смотрите как она танцует! Она профессионал!"
        customers3 "На члене! Я хочу чтобы она вертелась также на моем члене!"
        customers4 "Я сейчас кончу!!!"

    if result == "down":
        scene black
        image videov_Claire_Strip_6C = Movie(play="video/v_Claire_Strip_6C.mkv", fps=25, loop=False, image="/images/Slides/v_Claire_Strip_6C_end.jpg")
        show videov_Claire_Strip_6C
        pause 1.8
        hide videov_Claire_Strip_6C
        show screen poledance_shoot("/images/Slides/v_Claire_Strip_6C_end.jpg")
        wclean
        call pub_dance_claire2_dialogues_react(10) from _rcall_pub_dance_claire2_dialogues_react_17
        call pub_dance_battle_dialogues_applause("std") from _rcall_pub_dance_battle_dialogues_applause_61
        customers4 "О, даааа!"
        customers5 "Эта Клэр! Она бесподобна!"
        customers3 "Клянусь мой член будет у нее между ног!"
        customers1 "Эта детка сделала мой день!"
    if arrowUp == True or arrowSide == True or arrowDown == True:
        jump pub_dance2_claire_dance2_move6


    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    hide screen poledance_shoot
    hide screen poledance_coins
    fadeblack 2.0
    music Road_Trip

    $ money = tmpMoney

    sound wow
    imgd 34195
    w
    imgf 34183
    w
#    fadeblack 2.0
#    music Road_Trip
    imgfl 34196
    sound highheels_short_walk
    w

    return


#
