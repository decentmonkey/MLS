# Комната Барди.
# Моника спрашивает, получил-ли Барди чего хотел? И что там с Бетти?
# Барди отвечает что все отлично. И теперь Бетти ответит за все.
# Моника спрашивает и что, она занималась какими-то отвратительными вещами с инструктором?
# В зависимости от того занималась Бетти или нет, Барди отвечает.
# Что да, эта Бетти трахается со всеми подряд, как я и думал.
# У Бетти с Ральфом подписан брачный договор.
# И, если Бетти не хочет остаться без всего что имеет и уехать назад в свою дыру, то ей придется хорошо себя вести.
# Но это теперь моя забота! И только попробуй рассказать об этом кому-то!
# Только Барди имеет право говорить об этом Ральфу, иначе Моника сама знает что будет!
# Моника злая спрашивает и что будет?
# Барди говорит что имеет ввиду штраф.
# Моника морщится.
# Если Бетти не трахалась, то Барди говорит что она этого не делала, но того что он снял
# вполне достаточно для того чтобы так казалось.
# У Бетти с Ральфом подписан брачный договор.
# И, если Бетти не хочет остаться без всего что имеет и уехать назад в свою дыру, то ей придется хорошо себя вести.
# И Барди имеет право говорить об этом Ральфу, иначе Моника сама знает что будет!
# Моника злая спрашивает и что будет?
# Барди говорит что имеет ввиду штраф.
# Моника морщится.

label ep24_dialogues4_bardie1:
    if cloth != "Governess":
        mt "Мне надо переодеться!"
        return

    music Groove2_85
    img 10251
    with fade
    m "Ну что, ты получил что хотел?"
    m "Что там с Бетти?"

    # Если Барди еще не узнал
    if bettyBardieFitnessStage < 3:
        music Sneaky_Snitch
        img 10252
        with fade
        bardie "Да, она определенно трахается с ним!"
        bardie "Но мне пока не хватает доказательств."
        bardie "Мне нужно еще раз оказаться там!"
        bardie "Позови меня снова в следующий раз!"
        mt "Посмотрим..."
        return
    # Если Барди все узнал

# Барди отвечает что все отлично. И теперь Бетти ответит за все.
# Моника спрашивает и что, она занималась какими-то отвратительными вещами с инструктором?
# В зависимости от того занималась Бетти или нет, Барди отвечает.
# Что да, эта Бетти трахается со всеми подряд, как я и думал.
# У Бетти с Ральфом подписан брачный договор.

    img 10253
    with fade
    music Groove2_85
    bardie "Да, Моника! Все отлично!"
    bardie "Теперь Бетти ответит за все!"
    img 10254
    m "И что, она действительно занималась сексом с инструктором?"

    #
# И, если Бетти не хочет остаться без всего что имеет и уехать назад в свою дыру, то ей придется хорошо себя вести.
# Но это теперь моя забота! И только попробуй рассказать об этом кому-то!
# Только Барди имеет право говорить об этом Ральфу, иначе Моника сама знает что будет!
# Моника злая спрашивает и что будет?
# Барди говорит что имеет ввиду штраф.
# Моника морщится.

    # Бетти занималась сексом
    if bettyInstructorSex1 == True:
        img 10255
        with fade
        bardie "Да, Бетти трахается со всеми подряд, как я и думал!"
        bardie "Между прочим, у Бетти с Ральфом подписан брачный договор!"
        bardie "И, если Бетти не хочет остаться без всего того что она имеет..."
        bardie "И если не хочет уехать назад в свою дыру, то ей теперь придется хорошо себя вести!"
        img 10256
        mt "..."
        img 10257
        with fade
        bardie "Но теперь это моя забота! И только попробуй рассказать об этом кому-то еще!"
        bardie "Особенно Ральфу!"
        img 10258
        with diss
        "Только я могу это сделать! Иначе ты знаешь что с тобой будет!"
        music Power_Bots_Loop
        img 10259
        with fade
        m "И ЧТО СО МНОЙ БУДЕТ ЕСЛИ Я РАССКАЖУ ПРО ЭТУ СУЧКУ РАЛЬФУ?!"
        img 10260
        bardie "Я расскажу про тебя, ты знаешь кому! И тебе выпишут штраф!"
        img 10261
        with fade
        m "!!!"
    else:
    # Бетти не занималась сексом
# Если Бетти не трахалась, то Барди говорит что она этого не делала, но того что он снял
# вполне достаточно для того чтобы так казалось.
# У Бетти с Ральфом подписан брачный договор.
# И, если Бетти не хочет остаться без всего что имеет и уехать назад в свою дыру, то ей придется хорошо себя вести.
# И Барди имеет право говорить об этом Ральфу, иначе Моника сама знает что будет!
# Моника злая спрашивает и что будет?
# Барди говорит что имеет ввиду штраф.
# Моника морщится.

        img 10262
        with fade
        bardie "Нет, она не стала этого делать..."
        img 10263
        with diss
        bardie "Но!"
        bardie "Того что я успел снять, достаточно для того чтобы так казалось."
        img 10264
        with fade
        bardie "Между прочим, у Бетти с Ральфом подписан брачный договор!"
        bardie "И, если Бетти не хочет остаться без всего того что она имеет..."
        img 10265
        bardie "И если не хочет уехать назад в свою дыру, то ей теперь придется хорошо себя вести!"
        img 10266
        mt "..."
        img 10257
        with fade
        bardie "Но теперь это моя забота! И только попробуй рассказать об этом кому-то еще!"
        bardie "Особенно Ральфу!"
        img 10258
        "Только я могу это сделать! Иначе ты знаешь что с тобой будет!"
        music Power_Bots_Loop
        img 10259
        with fade
        m "И ЧТО СО МНОЙ БУДЕТ ЕСЛИ Я РАССКАЖУ ПРО ЭТУ СУЧКУ РАЛЬФУ?!"
        img 10260
        bardie "Я расскажу про тебя, ты знаешь кому! И тебе выпишут штраф!"
        img 10261
        with fade
        m "!!!"

    return




label ep24_dialogues4_bardie2:
# Барди делает замечания когда видит что Моника в трусиках.
    bardie "Моника, ты знаешь правила дома!"
    bardie "Почему на тебе надеты трусики?!"
    mt "!!!"
    bardie "Если ты будешь нарушать правила, то тебя будет ждать наказание!"
    $ bardieMonicaNonNudeCount += 1

    return

label ep24_dialogues4_bardie3:
    $ restore_music()
    music Groove2_85
# Если Моника нарушает правила дома (убирается в трусиках при Барди) 3 раза, то происходит наказание
# После уборки Барди зовет Монику вниз.
    img 10267
    with fadelong
    bardie "Гувернантка, иди вниз в свою спальню!"
    img 10268
    bardie "Твой хозяин хочет поговорить с тобой!"
    img 10269
    with fade
    mt "!!!"
    return


label ep24_dialogues4_bardie4:
    # Спальня в подвале
# Барди говорит что Моника нерадивая гувернантка и заслужила наказание.
    music stop
    img black_screen
    with Dissolve(1.0)
    pause 1.0
    music Groove2_85
    img 10270
    with fadelong
    m "Что тебе снова надо, Барди?!"
    music Power_Bots_Loop
    img 10271
    bardie "Моника, ты нерадивая гувернантка."
    #governess
    if monicaBettyPanties == False:
        if monicaUnder != "Nude":
            img 10272
    else:
        if monicaBettyPantiesId == 1:
            #betty
            img 10273
        if monicaBettyPantiesId == 2:
            img 10274
        if monicaBettyPantiesId == 3:
            img 10275
        if monicaBettyPantiesId == 4:
            img 10276
        if monicaBettyPantiesId == 5:
            img 10277
    #
    sound Jump1
    with diss
    bardie "Ты не соблюдаешь правила дома."
    img 10278
    bardie "И ты заслужила наказание!"
# Первый раз:
# Моника кривится и говорит какое еще наказание?!
    img 10279
    with fade
    m "Какое еще наказание?!"

# Барди садится на кровать и говорит чтобы сняла запрещенные трусики,
#подняла попу вверх и легла к нему на колени.
    img 10280
    with fade
    bardie "Сними запрещенные в этом доме трусики!"
    img 10281
    with diss
    bardie "Ложись ко мне на коленки и подними попу вверх!"
# Выбор:
# Моника говорит что не собирается этого делать! С нее хватит!
# Она уйдет из этого дурацкого дома!
# Моника не собирается терпеть такие унижения из-за какой-то крыши над головой!
# Барди говорит что пусть только попробует уйти! Тогда он сразу пожалуется Мистеру Маркусу на нее!
# Моника в ярости!
# Вот малявка! Он продолжает шантажировать меня!
# Барди говорит чтобы не испытывала его терпения и быстро легла для получения наказания!
    img 10282
    with fade
    menu:
        "Я не собираюсь этого делать! С меня хватит!":
            music Pyro_Flow
            img 10283
            with fade
            m "Я не собираюсь этого делать! С меня хватит!"
            img 10284
            with fade
            m "Я уйду из этого дурацкого дома!"
            m "Я не буду терпеть такие унижения из-за какой-то крыши над головой!"
            music Power_Bots_Loop
            img 10285
            with diss
            bardie "Только попробуй уйти!"
            bardie "Я сразу пожалуюсь Мистеру Маркусу на тебя!"
            mt "!!!"
            img 10286
            with fade
            mt "Вот малявка! Он продолжает шантажировать меня!"
            img 10287
            bardie "Не испытывай моего терпения и быстро ложись для получения наказания!"
            img 10288
            menu:
                "Послушаться хозяина дома...":
                    pass
                "Убежать...":
                    $ move_object("Bardie", "bedroom_bardie")
                    call change_scene("street_house_main_yard", "Fade_long", "highheels_run2") from _call_change_scene_206
                    return False
        "Послушаться хозяина дома...":
            pass

    $ bardieMonicaPunishmentCount += 1
# Моника снимает трусики и ложится к Барди на коленки
    music Groove2_85
    img 10289
    with fade
    w
    img 10290
    with fade
    w
    img 10291
    with fade
    w
    sound snd_fabric1
    if monicaBettyPanties == False:
        if monicaUnder != "Nude":
            #governess
            img 10292
            with diss
            w
            img 10293
            with diss
            w
    else:
        if monicaBettyPantiesId == 1:
            #betty
            img 10295
            with diss
            w
            img 10294
            with diss
            w
            img 10305
            with diss
            w
    #
        if monicaBettyPantiesId == 2:
            img 10296
            with diss
            w
            img 10297
            with diss
            w
            img 10306
            with diss
            w
    #
        if monicaBettyPantiesId == 3:
            img 10299
            with diss
            w
            img 10298
            with diss
            w
            img 10307
            with diss
            w
    #
        if monicaBettyPantiesId == 4:
            img 10300
            with diss
            w
            img 10301
            with diss
            w
            img 10308
            with diss
            w
    #
        if monicaBettyPantiesId == 5:
            img 10303
            with diss
            w
            img 10302
            with diss
            w
            img 10304
            with diss
            w

    #
    img 10309
    with fade
    w
    img 10310
    with fade
    w
    img 10311
    with fade
    w
    img 10312
    with fade
    w
    img 10313
    with fade
    w
    img 10314
    with fade
    w
    img 10315
    with fade
    w
    img 10316
    with fade
    w
    img 10317
    with fade
    w
    img 10318
    with fade
    w
    img 10319
    with fade
    w


# Барди шлепает Монику по попе, со следами.

label ep24_dialogues4_bardie4_loop1:
    # Барди шлепает Монику

    music stop
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Basement_Bardie_Monica_Spanking_1.mp3"
    scene black
    image videov_Basement_Bardie_Monica_Spanking_1_1 = Movie(play="video/v_Basement_Bardie_Monica_Spanking_1_1.mkv", fps=30)
    show videov_Basement_Bardie_Monica_Spanking_1_1
    wclean
    stop music

    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Basement_Bardie_Monica_Spanking_1.mp3"
    scene black
    image videov_Basement_Bardie_Monica_Spanking_1_2 = Movie(play="video/v_Basement_Bardie_Monica_Spanking_1_2.mkv", fps=30)
    show videov_Basement_Bardie_Monica_Spanking_1_2
    bardie "Получай!"
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Basement_Bardie_Monica_Spanking_1.mp3"
    scene black
    image videov_Basement_Bardie_Monica_Spanking_1_3 = Movie(play="video/v_Basement_Bardie_Monica_Spanking_1_3.mkv", fps=30)
    show videov_Basement_Bardie_Monica_Spanking_1_3
    bardie "Получай!"
    bardie "Нерадивая гувернантка!"
    bardie "Я научу тебя соблюдать правила дома!"
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Basement_Bardie_Monica_Spanking_1.mp3"
    scene black
    image videov_Basement_Bardie_Monica_Spanking_1_4 = Movie(play="video/v_Basement_Bardie_Monica_Spanking_1_4.mkv", fps=30)
    show videov_Basement_Bardie_Monica_Spanking_1_4
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Basement_Bardie_Monica_Spanking_1.mp3"
    scene black
    image videov_Basement_Bardie_Monica_Spanking_1_5 = Movie(play="video/v_Basement_Bardie_Monica_Spanking_1_5.mkv", fps=30)
    show videov_Basement_Bardie_Monica_Spanking_1_5
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Basement_Bardie_Monica_Spanking_1.mp3"
    scene black
    image videov_Basement_Bardie_Monica_Spanking_1_6 = Movie(play="video/v_Basement_Bardie_Monica_Spanking_1_6.mkv", fps=30)
    show videov_Basement_Bardie_Monica_Spanking_1_6
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Basement_Bardie_Monica_Spanking_1.mp3"
    scene black
    image videov_Basement_Bardie_Monica_Spanking_1_7 = Movie(play="video/v_Basement_Bardie_Monica_Spanking_1_7.mkv", fps=30)
    show videov_Basement_Bardie_Monica_Spanking_1_7
    bardie "Ну что, ты поняла? Ты будешь слушаться хозяина?"
    wclean
    stop music

    music Power_Bots_Loop
    menu:
        "Отпусти меня немедленно, малявка!":
            img 10320
            with fade
            m "Отпусти меня немедленно, малявка!"
            jump ep24_dialogues4_bardie4_loop1
        "Я поняла! Я буду слушаться хозяина!":
            pass


    music Groove2_85
    img 10321
    with fade
    m "Я поняла! Я буду слушаться хозяина!"
    img 10322
    with fade
    m "Я обещаю! Я буду себя хорошо вести!"
    img 10323
    with fade
    bardie "Так-то лучше!"
    img 10324
    with diss
    bardie "Если будешь себя снова плохо вести, получишь еще!"
    img 10325
    with fade
    bardie "Гувернантка, можешь продолжать работать..."
    bardie "Ты мне пока не нужна."

    music stop
    img black_screen
    with Dissolve(1.0)
    pause 1.0
    music Pyro_Flow
    img 10326
    with fadelong
    mt "Не могу поверить!"
    mt "Этот малявка отшлепал меня словно я маленький ребенок!"

    #Если повтор
    if bardieMonicaPunishmentCount > 1:
        img 10327
        with fade
        mt "И уже не первый раз!!!"
        #
        img 10327
        mt "В моем же доме!"
        mt "Отшлепали! Меня!!!"
        mt "Монику Бакфетт!!!"
        #

    img 10328
    with fade
    mt "У меня попа горит!"
    img 10329
    with diss
    mt "Что этот Барди себе позволяет?!"

    music stop
    img black_screen
    with diss
    pause 1.0
    music Groove2_85
    img 10330
    with fadelong
    mt "Как унизительно!"
    mt "Мне надо как-то избавиться от него!"

    return





#
