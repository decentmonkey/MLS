label ep24_dialogues5_betty0a:
    help "Прогресс Бетти активирован!"
    return


label ep24_dialogues5_betty0:
    # Нажато в меню Согласиться и предупредить Барди
    music Hidden_Agenda
    img 10607
    with fade
    m "Миссис Робертс, Вы дадите мне минуту, чтобы собраться?"
    img 6027
    betty "Не более минуты, гувернантка. Я не собираюсь ждать тебя."
    img 10608
    with fade
    m "Да, Миссис Робертс, я быстро вернусь..."
    return

label ep24_dialogues5_betty1:
# На следующий день, при попытке войти в любую локацию дома, происходит сцена разговора Бетти и Моники
# (Барди подглядывает)
# Бетти окликает Монику.
# Бетти напряжена и недовольна.
# Бетти говорит Монике что узнала кое-что о Монике.
    if cloth != "Governess":
        return False
    music Groove2_85
    img 10331
    with fadelong
    betty "Эй! Моника, гувернантка!"
    img 10332
    m "???"
    img 10333
    betty "Подойди-ка сюда..."
    sound highheels_short_walk
    img 10334
    with fadelong
    m "..."
    m "Да, Миссис Робертс. Чем могу быть полезна?"
    betty "..."
    img 10335
    with fade
    betty "Гувернантка, я кое-что узнала о тебе..."

# Моника напряжена (неужели она узнала кто я?)
# Бетти говорит что узнала что Моника носит ее трусики!
# Моника в шоке.
    img 10336
    music Power_Bots_Loop
    mt "?!?!?!"
    mt "НЕУЖЕЛИ?!?!"
    mt "НЕУЖЕЛИ ОНА УЗНАЛА КТО Я?!?"
    img 10337
    with diss
    mt "ЧТО ЖЕ ТЕПЕРЬ БУДЕТ?! МНЕ КОНЕЦ!!!"

#    music Groove2_85
    img 10338
    with fade
    betty "Я знаю..."
    music Groove2_85
    img 10339
    with diss
    sound Jump2
    betty "Я знаю, что ты носишь мои трусики..."

    if cloth == "Governess":

        if monicaBettyPanties == False:
            if monicaUnder != "Nude":
                img 10345
        else:
            #betty
            if monicaBettyPantiesId == 1:
                img 10340
            if monicaBettyPantiesId == 2:
                img 10341
            if monicaBettyPantiesId == 3:
                img 10342
            if monicaBettyPantiesId == 4:
                img 10343
            if monicaBettyPantiesId == 5:
                img 10344
        with fade
    mt "!!!"

# Бетти шипит: знаешь что я с тобой сделаю за это... нерадивая служанка...
# Барди смотрит на Бетти
# Бетти смотрит на Барди и смущается, напряженно (Бетти под шантажом)
# Я... Я разрешаю тебе носить мои трусики
    music Power_Bots_Loop
    img 10346
    betty "Знаешь... Что я с тобой сделаю за это..."
    img 10347
    with fade
    betty "... нерадивая служанка..."
    music Sneaky_Snitch
    img 10348
    with diss
    betty "..."
    img 10349
    with diss
    bardie "..."
    img 10350
    with fade
    mt "!!!"
    img 10351
    betty "..."
    img 10352
    with diss
    bardie "..."
    music Groove2_85
    img 10353
    with fade
    betty "Я... Я разрешаю тебе носить мои трусики..."
    img 10354
    mt "!!!"

# Дальше шипит... Но только попробуй одеть те, которые я постирала и собираюсь одеть!
# Моника кривится...
# Бетти смотрит на Барди снова. Барди улыбается.
# Бетти с трудом говорит.
# Моника должна носить те трусики, которые Бетти одевала в предыдущий день.
    music Groove2_85
    img 10355
    with fade
    betty "..."
    betty "Но..."
    img 10356
    betty "Только попробуй надеть те, которые я постирала и собираюсь одеть!"
    img 10357
    mt "!!!"
    music Sneaky_Snitch
    img 10358
    with fade
    betty "..."
    img 10359
    bardie "..."
    img 10360
    betty "..."
    img 10361
    bardie "..."
    music Groove2_85
    img 10362
    with fade
    betty "И..."
    img 10363
    with diss
    betty "И... Ты..."
    img 10364
    with diss
    betty "И... Ты должна носить только те трусики, которые я одевала в предыдущий день..."

# И...
# Бетти зло смотрит на Барди. Барди улыбается.
# Если тебе понадобится узнать какие трусики я ношу сегодня, то...
# Бетти снова зло смотрит на Барди, тот улыбается.
# То ты можешь спросить у меня и я покажу тебе... (Бетти злая и надменная)
    img 10365
    with fade
    betty "..."
    img 10366
    with diss
    bardie "..."
    img 10367
    with fade
    betty "И..."
    img 10368
    mt "?!?!?!"
    img 10369
    with fade
    betty "И... Если тебе понадобится узнать какие трусики я ношу сегодня, то..."
    music Sneaky_Snitch
    img 10370
    with fade
    betty "..."
    img 10371
    bardie "..."
    music Groove2_85
    img 10372
    mt "???"
    img 10373
    with fade
    betty "То ты можешь спросить у меня и я покажу тебе..."
    img 10374
    with diss
    betty "И брей свою киску! Мне не нужны твои волосы на моих трусиках!"
    betty "!!!"

# Моника в шоке и немного морщится.
    music Hidden_Agenda
    img 10375
    mt "..."
# Выбор что ответить
# Говорит спасибо, Миссис Робертс. Это будет намного удобнее.
# Тогда Бетти зло смотрит на Монику.
# Либо промолчать.
    menu:
        "Спасибо, Миссис Робертс. Это будет намного удобнее.":
            #bitchiness
            call bitch(10, "ep24_dialogues5_betty1") from _call_bitch_186
            img 10376
            with fade
            m "Спасибо, Миссис Робертс. Это будет намного удобнее."
            img 10377
            betty "!!!"
            img 10378
            m "..." # Моника злорадствует
            img black_screen
            with Dissolve(1.0)
            pause 1.0
            return True
        "Промолчать...":
            img black_screen
            with Dissolve(1.0)
            pause 1.0
            return False

    return



label ep24_dialogues5_betty2:
# Теперь, когда Бетти находится в спальне, там периодически находится Барди, который проверяет ее трусики.
# Моника может подойти к Бетти в спальне и проверить ее трусики.
# Также Моника может подойти к Бетти у зеркала на floor2 и проверить трусики тоже.


    # Бетти в спальне, Барди проверяет ее трусики
    $ store_music()
    music Sneaky_Snitch high
    img 10402
    with fadelong
    w
    img 10403
    w
    img 10404
    with diss
    sound Jump1
    bardie "Бетти! Можешь не отвлекаться!"
    img 10420
    with fade
    sound Jump2
    if bettyPantiesCurrent >= 1:
        bardie "Я лишь проверю, что у тебя все в порядке с твоими трусиками!"
    else:
        w

    #betty
    if bettyPantiesCurrent == 1:
        img 10405
        with fade
        w
        img 10406
        with diss
        w
    #
    if bettyPantiesCurrent == 2:
        img 10407
        with fade
        w
        img 10408
        with diss
        w
    #
    if bettyPantiesCurrent == 3:
        img 10409
        with fade
        w
        img 10410
        with diss
        w
    #
    if bettyPantiesCurrent == 4:
        img 10411
        with fade
        w
        img 10412
        with diss
        w
    #
    if bettyPantiesCurrent == 5:
        img 10413
        with fade
        w
        img 10414
        with diss
        w
    #
    if bettyPantiesCurrent == 0:
        #nude
        img 10415
        with fade
        bardie "Я лишь проверю, что ты соблюдаешь правила этого дома!"
            #random
        call showRandomImagesDiss([10416, 10417, 10418, 10419], 2) from _call_showRandomImagesDiss
#        w
#    bardie "Я лишь проверю, что у тебя все в порядке с твоими трусиками!"
    #
#    bardie "Я лишь проверю, что ты соблюдаешь правила этого дома!"

    betty "!!!"

    $ restore_music()
    music Sneaky_Snitch
    return
label ep24_dialogues5_betty2b:
    # Бетти у зеркала, Барди проверяет ее трусики
    $ store_music()
    music Sneaky_Snitch high
    img 10421
    with fadelong
    w
    img 10422
    with diss
    sound Jump1
    bardie "Бетти! Можешь не отвлекаться!"

    #betty
    if bettyPantiesCurrent == 1:
        img 10423
        with diss
        sound Jump2
        w
        bardie "Я лишь проверю, что у тебя все в порядке с твоими трусиками!"
        img 10424
        with diss
        w
    #
    if bettyPantiesCurrent == 2:
        img 10426
        with diss
        sound Jump2
        w
        bardie "Я лишь проверю, что у тебя все в порядке с твоими трусиками!"
        img 10425
        with diss
        w
    #
    if bettyPantiesCurrent == 3:
        img 10427
        with diss
        sound Jump2
        w
        bardie "Я лишь проверю, что у тебя все в порядке с твоими трусиками!"
        img 10428
        with diss
        w
    #
    if bettyPantiesCurrent == 4:
        img 10430
        with diss
        sound Jump2
        w
        bardie "Я лишь проверю, что у тебя все в порядке с твоими трусиками!"
        img 10429
        with diss
        w
    #
    if bettyPantiesCurrent == 5:
        img 10431
        with diss
        sound Jump2
        w
        bardie "Я лишь проверю, что у тебя все в порядке с твоими трусиками!"
        img 10432
        with diss
        w
    #nude
    if bettyPantiesCurrent == 0:
        img 10433
        with diss
        sound Jump2
        bardie "Я лишь проверю, что ты соблюдаешь правила этого дома!"
        #random
        img 10434
        with diss
        w
        call showRandomImagesDiss([10435, 10436, 10437, 10438], 2) from _call_showRandomImagesDiss_1

#    bardie "Я лишь проверю, что у тебя все в порядке с твоими трусиками!"
    #
#    bardie "Я лишь проверю, что ты соблюдаешь правила этого дома!"
    img 10439
    betty "!!!"

    $ restore_music()

    return


label ep24_dialogues5_betty3:
    # Моника в спальне проверяет трусики Бетти
    $ store_music()
    music Hidden_Agenda high
#    menu:
#        "Миссис Робертс, я бы хотела проверить Ваши трусики...":
#            pass
#        "Уйти.":
#            return False
    img 10469
    with fade
    w
    img 10470
    with fade
    m "Миссис Робертс, я бы хотела проверить Ваши трусики..."
    music Groove2_85 high
    img 10471
    betty "!!!"
    if bettyShowedPantiesLastDay == day:
        betty "Гувернантка, Я уже показывала тебе сегодня!"
        $ restore_music()
        return False
    img 10472
    with diss
    m "..."
    img 10473
    with fade
    betty "Ладно..."
    sound snd_fabric1
    img 10474
    with fade
    w

    #betty
    if bettyPantiesCurrent == 1:
        img 10475
        with fade
        w
        img 10476
        with diss
        betty "На, гувернантка, смотри."
        w
        img 10477 #общий
        with diss
        w
        img 10478
        with diss
        w
    #
    if bettyPantiesCurrent == 2:
        img 10479
        with fade
        w
        img 10480
        with diss
        betty "На, гувернантка, смотри."
        w
        img 10477 #общий
        with diss
        w
        img 10481
        with diss
        w
    #
    if bettyPantiesCurrent == 3:
        img 10482
        with fade
        w
        img 10483
        with diss
        betty "На, гувернантка, смотри."
        w
        img 10477 #общий
        with diss
        w
        img 10484
        with diss
        w
    #
    if bettyPantiesCurrent == 4:
        img 10485
        with fade
        w
        img 10486
        with diss
        betty "На, гувернантка, смотри."
        w
        img 10477 #общий
        with diss
        w
        img 10487
        with diss
        w
    #
    if bettyPantiesCurrent == 5:
        img 10488
        with fade
        w
        img 10489
        with diss
        w
        img 10477 #общий
        with diss
        w
        img 10490
        with diss
        w
    #

    betty "И не вздумай одеть другие!"

#    betty "На, гувернантка, смотри. И не вздумай надеть другие!"
    img 10491
    with fade
    mt "..."

    $ restore_music()
    return

label ep24_dialogues5_betty4:
    # Моника у зеркала проверяет трусики Бетти
    $ store_music()
    music Hidden_Agenda high
    img 10440
    with fade
    m "Миссис Робертс, я бы хотела проверить Ваши трусики..."
    music Groove2_85 high
    img 10441
    betty "!!!"
    if bettyShowedPantiesLastDay == day:
        betty "Гувернантка, Я уже показывала тебе сегодня!"
        $ restore_music()
        return False
    img 10442
    with fade
    m "..."
    #betty
    sound snd_fabric1
    if bettyPantiesCurrent == 1:
        img 10443
        with fade
        betty "На, гувернантка, смотри."
        img 10444
        with fade
        w
        betty "И не вздумай одеть другие!"
    #
    if bettyPantiesCurrent == 2:
        img 10446
        with fade
        betty "На, гувернантка, смотри."
        img 10445
        with fade
        w
        betty "И не вздумай одеть другие!"
    #
    if bettyPantiesCurrent == 3:
        img 10447
        with fade
        betty "На, гувернантка, смотри."
        img 10448
        with fade
        w
        betty "И не вздумай одеть другие!"
    #
    if bettyPantiesCurrent == 4:
        img 10450
        with fade
        betty "На, гувернантка, смотри."
        img 10449
        with fade
        w
        betty "И не вздумай одеть другие!"
    #
    if bettyPantiesCurrent == 5:
        img 10451
        with fade
        betty "На, гувернантка, смотри."
        img 10452
        with fade
        w
        betty "И не вздумай одеть другие!"

#    betty "На, гувернантка, смотри. И не вздумай одеть другие!"
    $ restore_music()
    return True



# Все это происходит пока прогресс Барди не достигнет след. уровня
# После этого, Моника, при входе в любую локацию дома из подвала, натыкается на Бетти.
# Снова цена Бетти, Моника и подглядывающий Барди.
# Бетти говорит Монике что теперь в доме новые правила.
# Моника спрашивает подозрительно какие новые правила, Миссис Робертс?
# Бетти говорит что теперь в доме Моника должна ходить и убираться без трусиков.
# Моника в шоке!
# Но почему, Миссис Робертс?!
# Ведь она просто наемный работник и Бетти не имеет права требовать этого!
# Бетти злится и кричит что если еще раз увидит гувернантку в трусиках, та вылетит из дома в тот же миг!
# Моника оборачивается на Барди и шипит: мелкий гаденышь! я знаю, это все ты!!!
# Барди улыбается.

label ep24_dialogues5_betty5:
    music Groove2_85
    img 10379
    with fadelong
    betty "Моника, гувернантка."
    img 10380
    betty "Подойди ко мне!"

    sound highheels_short_walk
    img 10381
    with fade
    m "Да, Миссис Робертс. Чем могу быть полезна?"
    img 10382
    betty "Гувернантка, я хочу сказать тебе."
    betty "В этом доме теперь новые правила..."
    img 10383
    m "Какие новые правила, Миссис Робертс?" #подозрительно
    music Sneaky_Snitch
    img 10384
    with fade
    betty "..."
    img 10385
    bardie "..."
    img 10386
    with fade
    betty "..."
    img 10387
    m "..."
    img 10388
    with fade
    bardie "..."
    img 10389
    with diss
    betty "..."
    music Groove2_85
    img 10390
    with fade
    betty "В общем Моника..."
    img 10391
    with diss
    betty "С этого дня ты должна ходить по дому и убираться без трусиков..."
    music Pyro_Flow
    img 10392
    m "!!!"
    img 10393
    with fade
    m "Но почему, Миссис Робертс?!?!"
    img 10394
    with fade
    m "Ведь я просто наемный работник!"
    img 10395
    m "И Вы не имеете права требовать этого!"
    music Power_Bots_Loop
    img 10396
    with fade
    betty "Нерадивая гувернантка!"
    betty "Если я еще раз увижу тебя в трусиках, то ты вылетишь из дома в тот же миг!"
    img 10397
    with diss
    betty "Поняла меня?!"
    music Sneaky_Snitch
    img 10398
    with fade
    m "!!!" #смотрит на Барди
    img 10399
    bardie "..."
    img 10400
    with fade
    mt "Мелкий гаденыш!"
    mt "Я знаю, это все Ты!!!"
    img 10401
    bardie "..."

    return

label ep24_dialogues5_betty5a:
    mt "Мелкий гаденыш!"
    return

# После этого, когда Моника проверяет у Бетти трусики в спальне, либо у зеркала и у Моники что-то надето,
# то она комментирует что не будет проверять у Бетти трусики, потому что сама сейчас носит их.
# И Бетти может попросить проверить в ответ и Моника рискует потерять крышу над головой.

label ep24_dialogues5_betty6:
    # Моника проверяет без трусиков Бетти в спальне
#    menu:
#        "Миссис Робертс, я бы хотела проверить Ваши трусики...":
#            pass
#        "Уйти.":
#            return False

    # Если есть какие-то трусики
    if monicaUnder != "Nude":
        mt "Мне не следует проверять трусики у Бетти, потому что я сама сейчас в трусиках..."
        mt "Бетти может проверить в ответ и я рискую потерять крышу над головой..."
        return False
    #

    $ store_music()
    music Hidden_Agenda high
    img 10492
    with fade
    w
    img 10493
    m "Миссис Робертс, я бы хотела проверить Ваши трусики..."
    music Groove2_85 high
    img 10494
    with fade
    betty "!!!"
    if bettyShowedPantiesLastDay == day:
        betty "Гувернантка, Я уже показывала тебе сегодня!"
        $ restore_music()
        return False

    if char_info["Betty"]["level"] < 6:
        #обычный
        # Бетти показывает попу
        img 10495
        with fade
        w

        img 10496
        with fade
        w
        sound snd_fabric1
        img 10497
        with fade
        w

        #random
        call showRandomImagesDiss([10498, 10499, 10500, 10501, 10502, 10503, 10504, 10505], rand(3,4)) from _call_showRandomImagesDiss_2
        #

        img 10506
        with diss
        betty "Я соблюдаю правила этого дома..."
        img 10507
        with fade
        betty "Покажи, что ты тоже!"
        img 10508
        w
        img 10509
        with fade
        m "Да, Миссис Робертс, конечно..."

        sound snd_fabric1
        img 10510
        with fade
        w
        img 10511
        with diss
        w
        img 10512
        with diss
        w
        img 10513
        with diss
        w

        #random
        call showRandomImagesDiss([10514, 10515, 10516, 10517, 10518, 10519, 10520, 10521], rand(3,4)) from _call_showRandomImagesDiss_3
#        img 10514
#        img 10515
#        img 10516
#        img 10517
#        img 10518
#        img 10519
#        img 10520
#        img 10521
        #
        img 10522
        with diss
        w
        img 10523
        with diss
        w
        img 10524
        with fade
        m "Я тоже соблюдаю правила этого дома..."
        $ restore_music()
        return

    else:
        #бонус
        music Loved_Up high
        sound snd_fabric1
        img 10525
        with fade
        w
        img 10526
        with fade
        w
        img 10527
        with diss
        w
        img 10528
        with diss
        w
        img 10529
        with diss
        w
        #random
        call showRandomImagesDiss([10530, 10531, 10532, 10533, 10534, 10535], 3) from _call_showRandomImagesDiss_4
#        img 10530
#        img 10531
#        img 10532
#        img 10533
#        img 10534
#        img 10535
        #

        img 10536
        with fade
        betty "Я соблюдаю правила этого дома..."
        betty "Покажи, что ты тоже!"

        img 10537
        with fade
        m "Да, Миссис Робертс, конечно..."
        sound snd_fabric1
        img 10538
        with fade
        w
        img 10539
        with diss
        w
        #random
        call showRandomImagesDiss([10540, 10541, 10542, 10543, 10544, 10545], 3) from _call_showRandomImagesDiss_5
#        img 10540
#        img 10541
#        img 10542
#        img 10543
#        img 10544
#        img 10545
        #
        img 10546
        with diss
        w
        img 10547
        with diss
        w
        img 10548
        with diss
        w
        img 10549
        with diss
        w
        img 10550
        with diss
        w
        img 10551
        with diss
        w
        img 10552
        with diss
        w
        img 10553
        with fade
        m "Я тоже соблюдаю правила этого дома..."

    $ restore_music()
    return

label ep24_dialogues5_betty7:
    # Моника проверяет без трусиков Бетти у зеркала
#    menu:
#        "Миссис Робертс, я бы хотела проверить Ваши трусики...":
#            pass
#        "Уйти.":
#            return False

    # Если есть какие-то трусики
    if monicaUnder != "Nude":
        mt "Мне не следует проверять трусики у Бетти, потому что я сама сейчас в трусиках..."
        mt "Бетти может проверить в ответ и я рискую потерять крышу над головой..."
        return False
    #

    $ store_music()
    music Hidden_Agenda high
    img 10453
    with fade
    m "Миссис Робертс, я бы хотела проверить Ваши трусики..."
    music Groove2_85 high
    img 10454
    betty "..."
    if bettyShowedPantiesLastDay == day:
        betty "Гувернантка, Я уже показывала тебе сегодня!"
        $ restore_music()
        return False
    w
    # Бетти показывает попу
    sound snd_fabric1
    img 10455
    with fade
    w
    #random
    call showRandomImagesDiss([10456, 10457, 10458], 1) from _call_showRandomImagesDiss_6
#    img 10456
#    img 10457
#    img 10458
#    w

    img 10459
    with diss
    w
    betty "Я соблюдаю правила этого дома..."
    img 10460
    with fade
    betty "Покажи, что ты тоже!"
    m "Да, Миссис Робертс, конечно..."

    # Моника показывает попу
    sound snd_fabric1
    img 10461
    with fade
    w
    img 10462
    with diss
    w
    #random
    call showRandomImagesDiss([10463, 10464, 10465, 10466, 10467, 10468], 3) from _call_showRandomImagesDiss_7
#    img 10463
#    img 10464
#    img 10465
#    img 10466
#    img 10467
#    img 10468


    img 10462
    with fade
    m "Я тоже соблюдаю правила этого дома..."
    $ restore_music()

    return


















#
