
default mlsBardiSeanDay3Whore1 = 0 # Барди назвал шлюху миссис Кларк
default mlsBardiSeanDay3Whore2 = 0 # Барди назвал шлюху миссис Адамс
default mlsBardiSeanDay3WhorePhone = False

define v_MC_Whore_Blowjob1_25_sound_name = "v_MC_Whore_Blowjob1_25"
define v_MC_Whore_Hand1_25_sound_name = "v_MC_Whore_Hand1_25"
define v_MC_Whore_Sex1_25_sound_name = "v_MC_Whore_Sex1_25"
define v_MC_Whore_Sex2_25_sound_name = "v_MC_Whore_Sex2_25"
define v_MC_Whore_Tits1_25_sound_name = "v_MC_Whore_Tits1_25"

#call ep02_dialogues3_sean_1() # мысли перед домом Шона
#call ep02_dialogues3_sean_2() # клик на дом Шона
#call ep02_dialogues3_sean_2a() # мысли при клике на выход из дома Шона
#call ep02_dialogues3_sean_2b() # мысли при клике на телек в гостиной
#call ep02_dialogues3_sean_2c() # мысли при клике на кухню
#call ep02_dialogues3_sean_2c1() # мысли при клике на спалью родителей Шона
#call ep02_dialogues3_sean_2d() # мысли при клике на лестницу, ведущую к комнате Шона
#call ep02_dialogues3_sean_3() # комната Шона, сцена с Бекки
#call ep02_dialogues3_sean_4() # после сцены с Бекки, мысли при клике на любую локацию, кроме дома Барди
#call ep02_dialogues3_sean_5() # телефон, при клике на строку контакта "whore", 1-я переписка после сцены
#call ep02_dialogues3_sean_5a() # телефон, при повторном клике на строку контакта "whore", если уже переписывался с ней
#call ep02_dialogues3_sean_5b() # телефон, если еще раз кликает на контакт "whore" после того, как она прислала фотку
#call ep02_dialogues3_sean_5c() # мысли после переписки со шлюхой
#call ep02_dialogues3_sean_6() # телефон, клик на строку контакта "sean" после сцены со шлюхой в его доме


# при клике на локацию Дом Шона
# мысли перед его домом
label ep02_dialogues3_sean_1:
    # мысли, не рендерить!!
    # если была переписка с Шоном до колледжа
    if mlsBardiDay3College8 > 0:
        bardi_t "Какие там за важные дела у Шона?"
        bardi_t "Что он даже на колледж забил сегодня?"
    # если переписки утром не было
    else:
        bardi_t "По-моему, Шона сегодня не было в колледже."
        bardi_t "Может, у него что-то случилось?"
    return

# клик на дом Шона
label ep02_dialogues3_sean_2:
    # Барди поднимается на крыльцо, стучит в дверь, но ему не открывает никто
    fadeblack 1.5
    music Shining_Through
    imgfl 900526
    sound2 snd_door_knock
    bardi_t "Никого нет что-ли?"
    # снова стучит, но безрезультатно
    bardi_t "Позвоню ему..."
    # Барди берет в руки телефон, тыкает пальцем в экран и прикладывает телефон к уху
    # идут длинные гудки, потом резко короткие - Шон сбросил звонок
    # Барди смотрит в телефон
    sound phone_beep
    imgf 900527
    bardi_t "???"
    # в этот момент открывается дверь и на пороге возникает Шон с озабоченным видом
#    sound2 step_stairs_short
    sound snd_door_open1
    sound2 Jump2
    img 900528 vpunch
    bardi "О, чувак! А я тебе..."
    img 900531
    sean "Тсс! Тихо!"
    imgd 900530
    w
#    sound vjuh3
    imgd 900529
    w
    # Шон нервно смотрит по сторонам, потом говорит
#    sound vjuh3
    imgd 900532
    sean "Заходи быстрее!.."
    # скрывается в дверях
    # смена кадра
    # гостиная в доме Шона
    sound step_stairs
    imgf 900533
    w
    imgd 900534
    bardi "Эй, у тебя все в порядке, Шон?"
    imgd 900535
    sean "Да, все окей."
    # Шон бросает взгляд в сторону своей комнаты, потом снова смотрит на Барди
    sound vjuh3
    imgd 900536
    sean "У меня просто дела."
    imgd 900537
    bardi "Может, я могу чем-то помочь?.."
    # в этот момент раздается звонок в дверь
    sound snd_door_bell1
    imgd 900536
    sean "Черт!"
    sound Jump1
    imgd 900538
    sean "Я сейчас, бро. Подожди меня здесь."
    sound step_stairs_short
    imgf 900539
    w
    # Шон выходит из гостиной
    # со стороны входной двери раздаются голоса
    sound snd_door_open1
    imgd 900540
    unknown_woman "Я эту огромную вазу не могу поднять. У меня сил не хватает. Она почти с меня ростом, представляешь?"
    unknown_woman "Или я ее уроню на пол и разобью... А эта ваза стоит больше, чем весь ваш дом..."
    unknown_woman "Или на себя уроню и все свои старые кости к чертям переломаю. Ну ладно хоть ваза при этом цела останется..."
    unknown_woman "Но если ты мне поможешь, по-соседски, я тебе подкину деньжат немного."
    unknown_woman "Пошли, Шон, поможешь старушке-соседке. Я уже задолбалась с этой вазой возиться."
    sean "Да, конечно. Без проблем."
    sound step_stairs_short
    imgf 900535
    sean "Эй, бро!"
    imgd 900537
    bardi "Что?"
    imgd 900541
    sean "Я ненадолго отлучусь помочь соседке. Подожди меня."
    imgd 900537
    bardi "Окей."
    sound step_stairs
    imgf 900540
    unknown_woman "И, кстати, там кроме вазы есть еще одна старинная вещь..."
    fadeblack
    sound snd_door_open1
    pause 1.5
    # звук закрывающейся двери
    # Барди остается один
    # переход на движок
    return

# при клике на выход из дома Шона
label ep02_dialogues3_sean_2a:
    # мысли, не рендерить!!
    bardi_t "Нужно дождаться Шона."
    bardi_t "Он как-то странно себя ведет. Вдруг ему нужна моя помощь?"
    return False

# при клике на телек в гостиной
label ep02_dialogues3_sean_2b:
    # мысли, не рендерить!!
    bardi_t "Не хочу смотреть телек..."
    return False

# при клике на кухню
label ep02_dialogues3_sean_2c:
    # мысли, не рендерить!!
    bardi_t "Там кухня. Наверняка, ничего интересного."
    return

# при клике на спалью родителей Шона
label ep02_dialogues3_sean_2c1:
    # мысли, не рендерить!!
    bardi_t "Эта спальня родителей Шона."
    bardi_t "И дверь открыта... В отличие от спальни Софи и Генри..."
    bardi_t "Интересно, сколько бессонных ночей проводят родители Шона на этой кровати?.."
    return

# при клике на лестницу, ведущую к комнате Шона
label ep02_dialogues3_sean_2d:
    # мысли, не рендерить!!
    bardi_t "Сколько еще ждать Шона?.."
    bardi_t "Мне еще нужно успеть домой к ужину."
    bardi_t "..."
    bardi_t "По-моему, в прошлый раз я видел мяч в комнате Шона..."
    bardi_t "Хоть чем-то заняться, пока жду его."
    return

# комната Шона
label ep02_dialogues3_sean_3:
    # Барди заходи в комнату Шона
    music Step_By_Step
    sound2 step_stairs
    imgfl 900542
    bardi_t "Он же не будет против, что я возьму его мяч..."
    # внезапно к нему подлетает шлюха с завязанными глазами (повязка на глаза у нас есть в сцене админ-Виктория-Моника)
    # кожанку и пояс от чулков со шлюхи нужно будет сразу снять, оставить только топ-сетку, юбку и сапоги
    # она радостная, что она пришел (думает, что это Шон)
    imgf 900688
    w
    imgd 900543
    w
    music stop
    sound plastinka1b
    img 900544 hpunch
    whore "Ну наконец-то ты вернулся!"
    music Story_of_One_Success_short
    imgd 900545
    whore "Твоя Бекки тебя заждалась!"
    imgd 900554
    bardi_t "?!?!"
    # она берет его за руку
    sound vjuh3
    imgd 900546
    whore "Зачем ты так надолго меня оставил одну?"
    # Барди в ступоре молчит
    imgd 900547
    bardi_t "..."
    bardi_t "Кто это?!"
    imgf 900548
    bardi_t "И что она здесь делает?!"
    imgd 900549
    bardi_t "Вот черт! Неужели, это та тетка, которая была на фотке у Шона?!"
    imgf 900546
    whore "Шалунишка ведь хочет поиграть с Бекки?"
    imgd 900547
    bardi_t "Она что, приняла меня за Шона?.."
    bardi_t "Твою мать! Что теперь делать?!"
    bardi_t "Притвориться, что я Шон?.."
    sound vjuh3
    imgd 900550
    whore "Бекки так любит игры..."
    # она прикладывает руку Барди к своей груди
    music The_Heat
    sound2 Jump2
    img 900551 hpunch
    whore "В какую игру ты хочешь поиграть, м?"
    bardi "Эммм... Я..."
    # шлюха настораживается, но рука Барди так же у нее на груди
    imgd 900552
    whore "У тебя странный голос..."
    imgd 900553
    bardi_t "Черт с ним! Притворюсь Шоном!"
    bardi_t "Будет еще хуже, если она поймет, что это кто-то другой. Тогда я подставлю Шона..."
    # Барди кашляет
    imgf 900555
    bardi "Кхе-кхе!.. Кхм..."
    # Барди кладет вторую руку на ее вторую грудь
    sound Jump1
    img 900556 hpunch
    bardi "Просто я... Я так возбужден, что аж голос охрип..."
    # она воодушевленно выпячивает грудь навстречу его рукам
    imgf 900557
    w
    sound snd_woman_laugh4
    imgd 900558
    whore "Хи-хи. Бекки такая, да."
    imgf 900559
    bardi_t "У нее такая грудь... Она даже не помещается в мои ладони..."
    bardi_t "Черт! Когда я последний раз трахался?.."
    bardi_t "Я даже вспомнить не могу!.."
    bardi_t "Охренеть!"
    # шлюха тем временем кладет руку на его ширинку, там уже стояк
#    sound vjuh3
    imgd 900560
    w
    imgd 900561
    w

    # video
    # v_MC_Whore_Hand1_25
    $ localSoundVolume = 1.0
    $ localSoundName = v_MC_Whore_Hand1_25_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(getMusicScenes(0.2), 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_MC_Whore_Hand1_25= Movie(play="video/v_MC_Whore_Hand1_25.mkv")
    show videov_MC_Whore_Hand1_25
    with fade
    whore "Ох, я вижу, что ты очень-очень хочешь Бекки!"
    wclean
    bardi "Да..."
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    # она начинает водить рукой по его стояку
    imgf 900556
    w
    # мнет ее грудь
    imgd 900562
    w
    imgd 900556
#    bardi_t "Это же просто шлюха..."
    w

    # video
    # v_MC_Whore_Tits1_25
    $ localSoundVolume = 1.0
    $ localSoundName = v_MC_Whore_Tits1_25_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(getMusicScenes(0.2), 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_MC_Whore_Tits1_25= Movie(play="video/v_MC_Whore_Tits1_25.mkv")
    show videov_MC_Whore_Tits1_25
    with fade
    whore "Ох..."
    wclean
    bardi_t "Хочу! Шон меня убьет, но я хочу трахнуть ее!.."
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 900558
    whore "У меня идея!"
    whore "Давай поиграем в мою любимую игру - преподаватель и студент?"
    imgd 900563
    bardi "Я не против..."
    imgd 900564
    whore "Я знала, что тебе понравится моя идея! Хи-хи-хи."
    # она отстраняется от него, снимает свой топ и бросает его на пол (остается только в юбке и сапогах)
    sound Jump2
    imgd 900565
    w
    sound vjuh3
    img 900566 vpunch
    w
    music Stylish_Hip_Hop_Rock
    imgf 900567
    bardi_t "Твою мать, какие же клевые сиськи у этой телки!.."
    # Барди кладет руки на ее голую грудь
    sound Jump1
    img 900568 hpunch
    bardi_t "Да, я определенно ее сейчас трахну..."
    # щипает за сосок, оттягивает его
    imgd 900569
    w
    imgf 900572
    w
    imgd 900573
    w
    imgd 900572
    w
    imgd 900573
    w
    imgf 900570
    whore "Как ты будешь меня называть?"
    whore "Я могу быть кем угодно, только скажи..."
    imgd 900571
    bardi "..." # руки также на груди
    # сцена минета в пунктах меню одна и та же. там, где нет лиц училок - использовать одинаковые арты
    menu:
        "Миссис Кларк.": # математичка
            $ mlsBardiSeanDay3Whore1 = day # Барди назвал шлюху миссис Кларк
            imgf 900574
            bardi "Ты будешь миссис Кларк."
            imgd 900575
            sound snd_woman_laugh4
            whore "Да, я сегодня буду миссис Кларк, хи-хи."
            # она достает его член и водит по нему рукой
            imgf 900576
            w
            sound vjuh3
            img 900577 vpunch
            w
            imgf 900578
            w
            imgd 900579
            sound highheels_short_walk
            w
            imgf 900580
            w
            imgd 900581
            w
            imgd 900575
            whore "А какой предмет я преподаю в колледже?"
            imgd 900574
            bardi "Гребаную математику..."
            # она хихикает и встает на колени перед Барди
            sound vjuh3
            img 900582 vpunch
            w
            imgf 900583
            whore "Миссис Кларк хочет похвалить тебя, студент..."
            whore "Ты показываешь высокую успеваемость по математике."
            # проводит языком по головке члена
            sound lick3
            imgd 900584
            bardi "Мммм..."
            sound lick3
            imgd 900585
            w
            sound lick3
            imgd 900586
            w
            imgd 900583
            whore "Миссис Кларк любит таких хороших студентов."
            whore "И готова вознаграждать их хорошим минетом после занятий."
            # облизывает головку и вбирает член в себя
            sound lick3
            imgd 900584
            w
            sound lick3
            imgd 900585
            w
            sound chpok6
            img 900587 hpunch
            whore "Мпфх!.."
            sound chpok7
            imgd 900588
            w
            sound chpok7
            imgd 900587
            w
            sound chpok7
            imgd 900588
            w

            # video
            # v_MC_Whore_Blowjob1_25
            $ localSoundVolume = 1.0
            $ localSoundName = v_MC_Whore_Blowjob1_25_sound_name
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(getMusicScenes(0.2), 0.5, channel="music")
            play music2 "<from " + str((0*1.166)) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_MC_Whore_Blowjob1_25 = Movie(play="video/v_MC_Whore_Blowjob1_25.mkv", fps=25)
            show videov_MC_Whore_Blowjob1_25
            wclean
            whore "Мпфх!.."
            wclean
            bardi "Ееее!.."
            whore "Мммм..."
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            # вытаскивает и, удерживая член рукой, шлепает себя по губам
            # на несколько кадров, лицо шлюхи в повязке сменяется на лицо Кларк в повязке
            sound chpok8
            imgd 900590
            w
            imgd 900622
            w
            imgd 900591
            w
            show screen dream()
            with diss
            show screen dream_focus(1000, 495, 4.5, 0.95)
            with Dissolve(1.0)
            pause 0.5
            sound snd_magic
            img 900594
            show screen dream()
            show screen dream_focus(1000, 495, 4.5, 0.95)
            with Dissolve(1.0)
            w
            sound lick3
            img 900595
            show screen dream()
            show screen dream_focus(1000, 495, 4.5, 0.95)
            with diss
            w
            img 900593
            show screen dream()
            show screen dream_focus(1000, 495, 4.5, 0.95)
            with diss
            teacher_clark "Миссис Кларк просто обожает..."
            teacher_clark "Отсасывать у своих студентов после математики."
#            imgd 900622
#            w
            # снова резко и глубоко вбирает в себя член
            sound chpok6
            img 900592
            show screen dream()
            show screen dream_focus(1000, 495, 4.5, 0.95)
            with hpunch
#            img 900588 hpunch
            teacher_clark "Мпфх!.."
            bardi "Оооох..."
            bardi "Даа!.."
            # лицо шлюхи возвращается
            sound chpok7
            imgd 900587
            w
            sound chpok7
            imgd 900588
            w
            sound chpok7
            imgd 900587
            w
            sound chpok7
            imgd 900588
            whore "Мммм..."
            # шлюха вытаскивает член изо рта
            sound chpok8
            imgd 900583
            whore "Тебе нравится, как усердно тебя благодарит миссис Кларк?"
            imgd 900589
            bardi "Да..."
            imgd 900583
            bardi "Но хотелось бы большей благодарности, миссис Кларк."
            # она облизывает член и пошло улыбается
            ## можено убрать это слово под юбкой, так как юбку она сняла
            sound lick3
            imgd 900584
            w
            sound lick3
            imgd 900585
            w
            imgd 900583
            whore "Миссис Кларк любит, когда наглые студенты трогают ее попку..."
            # Барди хватает шлюху за руку и поднимает на ноги
            imgf 900601
            bardi "А может, вы любите пожестче, миссис Кларк?"
            sound Jump2
            img 900602 hpunch
            w
            # смена лица на Кларк
            # смена лица обратно на шлюху
            sound highheels_short_walk
            imgd 900604
            whore "Обожаю..."
            show screen dream()
            with diss
            show screen dream_focus(980, 300, 3.0, 0.95)
            with Dissolve(1.0)
            pause 0.5
            sound snd_magic
#            sound vjuh3
            img 900603
            show screen dream()
            show screen dream_focus(980, 300, 3.0, 0.95)
            with Dissolve(1.0)
            with hpunch
            teacher_clark "Трахни меня скорее, студент!.."
            teacher_clark "Давай быстрее, мне не терпится!"
            imgd 900604
            w
            imgf 900605
            w
            sound Jump1
            img 900606 hpunch
            w
            # Барди ставит ее к стене у кровати (либо нагибает над кроватью)
            # задирает юбку (она без трусиков) и шлепает по попе
            sound step_stairs_short
            imgf 900607
            w
            sound vjuh3
            img 900608 vpunch
            w
            sound snd_slap1
            img 900609 hpunch
            w
            img 900610
            bardi "А вот так вам нравится, миссис Кларк?"
            sound ahhh6
            imgd 900611
            whore "О, да!.."
            # снова шлепает
            imgf 900612
            w
            sound snd_slap1
            img 900613 hpunch
            whore "Ооо!.."
            img 900614
            w
            # напрявляет член на киску и входит
            imgf 900615
            w
            sound chpok6
            img 900616 hpunch
            sound2 man moan5
            bardi "Ееее!.."
            imgd 900617
            sound ahhh4
            whore "Оооох!.."
            # шлепок по попе и начинает ее ахать
            # во время секса можно показать лицо Кларк еще раз, не показывая полностью голого тела (типа Барди себе представляет ее вместо шлюхи)
            imgf 900618
            w
            sound snd_slap1
            img 900619 hpunch
            w
            img 900620
            sound ahhh7
            whore "Оооо!"
            imgf 900621
            w

            # video
            # v_MC_Whore_Sex1_25
            $ localSoundVolume = 1.0
            $ localSoundName = v_MC_Whore_Sex1_25_sound_name
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(getMusicScenes(0.2), 0.5, channel="music")
            play music2 "<from " + str((0*1.166)) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_MC_Whore_Sex1_25 = Movie(play="video/v_MC_Whore_Sex1_25.mkv", fps=25)
            show videov_MC_Whore_Sex1_25
            wclean
            whore "Какой у тебя клевый член!.."
            bardi "Мммм..."
            wclean
            whore "Даа!.. Как же кайфово!"
            bardi "Чертовски охренительно трахать вас, миссис Кларк!.."
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 900623
            w
            imgd 900624
            whore "Аааа!"
            imgf 900625
            sound ahhh6
            w
            show screen dream()
            with diss
            show screen dream_focus(980, 400, 4.0, 0.95)
            with Dissolve(1.0)
            pause 0.5
            sound snd_magic
            img 900626
            show screen dream()
            show screen dream_focus(980, 400, 4.0, 0.95)
            with Dissolve(1.0)
            with vpunch
            teacher_clark "Оттрахай миссис Кларк, студент! Оттрахай как следует!"
            img 900627
            show screen dream()
            show screen dream_focus(980, 350, 5.0, 0.95)
            with diss
            teacher_clark "Миссис Кларк сейчас кончит!"
            bardi "О, ееее!.."
            img 900617
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound woman_moan11
            whore "ААААА!"
            # шлюха кончает
            img 900611
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound woman_moan12
            whore "АААААААА!!!"
            bardi "О, дааа!!!"
            menu:
                "Кончить в нее.":
                    # Барди бурно кончает в нее
                    img 900629
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    w
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    sound man moan8
                    bardi "Дааа!!!"
                    sound2 chpok5
                    imgd 900630
                    bardi "Оооо!!!"
                    bardi "О, какой кайф..."
                    pass
                "Кончить на нее.":
                    # Барди бурно кончает на нее
                    img 900631
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    w
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    sound man moan8
                    bardi "Дааа!!!"
                    sound2 chpok5
                    imgd 900632
                    bardi "Оооо!!!"
                    bardi "О, какой кайф..."
                    pass
            # дверь в комнату Шона резко открывается и он в кипише влетает внутрь
            $ questLog(4, True)
            music stop
            sound plastinka1b
            img 900664 hpunch
            sean "Бро! Твою мать!"
            music Fly_With_Me_short
            sean "Моя мама домой пришла! Убегайте! Быстро!"
            sound Jump2
            img 900653 vpunch
            bardi "Фак!.."
            # он подбегает к Барди и шлюхе и подталкивает их к окну
            pass
        "Миссис Адамс.": # препод по инглишу
            $ mlsBardiSeanDay3Whore2 = day # Барди назвал шлюху миссис Адамс - минет + cowgirl
            imgf 900574
            bardi "Ты будешь миссис Адамс."
            imgd 900575
            sound snd_woman_laugh4
            whore "Да, я сегодня буду миссис Адамс, хи-хи."
            imgf 900576
            w
            sound vjuh3
            img 900577 vpunch
            w
            imgf 900578
            w
            imgd 900579
            sound highheels_short_walk
            w
            # она достает его член и водит по нему рукой
            imgf 900580
            w
            imgd 900581
            w
            imgd 900575
            whore "А какой предмет я преподаю в колледже?"
            imgd 900574
            bardi "Английский и литературу..."
            # она хихикает и встает на колени перед Барди
            sound vjuh3
            img 900582 vpunch
            w
            imgf 900583
            whore "Миссис Адамс хочет пошалить немного со своим студентом..."
            whore "Прямо в кабинете английского языка. Пока никто их не видит."
            # проводит языком по головке члена
            sound lick3
            imgd 900584
            bardi "Мммм..."
            sound lick3
            imgd 900585
            w
            sound lick3
            imgd 900586
            w
            imgd 900583
            whore "Миссис Адамс любит шалить после занятий в колледже."
            whore "Прямо на рабочем месте..."
            # облизывает головку и вбирает член в себя
            sound lick3
            imgd 900584
            w
            sound lick3
            imgd 900585
            w
            sound chpok6
            img 900587 hpunch
            whore "Мпфх!.."
            sound chpok7
            imgd 900588
            w
            sound chpok7
            imgd 900587
            w
            sound chpok7
            imgd 900588
            w

            # video
            # v_MC_Whore_Blowjob1_25
            $ localSoundVolume = 1.0
            $ localSoundName = v_MC_Whore_Blowjob1_25_sound_name
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(getMusicScenes(0.2), 0.5, channel="music")
            play music2 "<from " + str((0*1.166)) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_MC_Whore_Blowjob1_25 = Movie(play="video/v_MC_Whore_Blowjob1_25.mkv", fps=25)
            show videov_MC_Whore_Blowjob1_25
            wclean
            whore "Мпфх!.."
            wclean
            bardi "Ееее!.."
            whore "Мммм..."
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            # вытаскивает и, удерживая член рукой, шлепает себя по губам
            # на несколько кадров, лицо шлюхи в повязке сменяется на лицо Кларк в повязке
            sound chpok8
            imgd 900590
            w
            imgd 900622
            w
            imgd 900591
            w
            show screen dream()
            with diss
            show screen dream_focus(1000, 395, 4.5, 0.95)
            with Dissolve(1.0)
            pause 0.5
            sound snd_magic
            img 900597
            show screen dream()
            show screen dream_focus(1000, 395, 4.5, 0.95)
            with Dissolve(1.0)
            w
            sound lick3
            img 900598
            show screen dream()
            show screen dream_focus(1000, 395, 4.5, 0.95)
            with diss
            w
            sound lick3
            img 900599
            show screen dream()
            show screen dream_focus(1000, 395, 4.5, 0.95)
            with diss
            w
            img 900600
            show screen dream()
            show screen dream_focus(1000, 395, 4.5, 0.95)
            with diss
            teacher_adams "Миссис Адамс просто обожает..."
            teacher_adams "Отсасывать у своих студентов после английского."
#            imgd 900622
#            w
            # снова резко и глубоко вбирает в себя член
            sound chpok6
            img 900596
            show screen dream()
            show screen dream_focus(1000, 450, 5.0, 0.95)
            with hpunch
            teacher_adams "Мпфх!.."
#            img 900588 hpunch
            bardi "Оооох..."
            bardi "Даа!.."
            # лицо шлюхи возвращается
            #whore "Мммм..."
            # шлюха вытаскивает член изо рта
            sound chpok7
            imgd 900587
            w
            sound chpok7
            imgd 900588
            w
            sound chpok7
            imgd 900587
            w
            sound chpok7
            imgd 900588
            w
            sound chpok8
            imgd 900583
            whore "Тебе нравится, как усердно миссис Адамс отсасывает у тебя?"
            imgd 900589
            bardi "Да..."
            imgd 900583
            whore "Тебе хотелось бы большего, м?.."
            imgd 900589
            bardi "Да..."
            # она облизывает член и пошло улыбается
            ## можено убрать это слово под юбкой, так как юбку она сняла
            sound lick3
            imgd 900584
            w
            sound lick3
            imgd 900585
            w
            imgd 900583
            w
            sound Jump2
            img 900601
            whore "Миссис Адамс любит, когда наглые студенты трогают ее попку..."
            # она поднимается на ноги и толкает Барди на кровать
            # смена лица на Кларк
            sound highheels_short_walk
            imgd 900634
            w
            show screen dream()
            with diss
            show screen dream_focus(980, 300, 3.0, 0.95)
            with Dissolve(1.0)
            pause 0.5
            sound snd_magic
#            sound vjuh3
            img 900633
            show screen dream()
            show screen dream_focus(980, 300, 3.0, 0.95)
            with diss
            with vpunch
            teacher_adams "И еще я просто обожаю, когда член заполняет всю мою киску."
            teacher_adams "Хочу скорее трахнуть тебя, студент!.."
            imgd 900634
            # смена лица обратно на шлюху
            bardi "Приступайте, миссис Адамс."
            # она снимает юбку (она без трусиков)
            imgf 900605
            w
            sound Jump1
            img 900606 hpunch
            w
            sound highheels_short_walk
            imgf 900635
            w
            sound vjuh3
            img 900636 vpunch
            whore "О, да!.."
            imgf 900637
            whore "Сейчас ты увидишь, какой шалуньей может быть миссис Адамс!"
            # она лезет на него
            imgd 900638
            whore "Мммм!.."
            # берет его член в руку и напрявляет на свою киску, вводит
            sound chpok6
            img 900639 hpunch
            bardi "Ееее!.."
            imgd 900640
            sound ahhh6
            whore "Оооох!.."
            # он шлепает ее по попе и она начинает скакать на нем
            # во время секса можно показать лицо Адамс еще раз, не показывая полностью голого тела (типа Барди себе представляет ее вместо шлюхи)
            imgf 900641
            whore "Оооо!"
            sound snd_slap1
            img 900642 hpunch
            w
            imgf 900643
            w
            #sound ahhh4

            # video
            # v_MC_Whore_Sex2_25
            $ localSoundVolume = 1.0
            $ localSoundName = v_MC_Whore_Sex2_25_sound_name
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(getMusicScenes(0.2), 0.5, channel="music")
            play music2 "<from " + str((0*1.166)) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_MC_Whore_Sex2_25 = Movie(play="video/v_MC_Whore_Sex2_25.mkv", fps=25)
            show videov_MC_Whore_Sex2_25
            wclean
            whore "Какой у тебя клевый член!.."
            bardi "Мммм..."
            wclean
            whore "Даа!.. Как же кайфово!"
            bardi "Чертовски охренительно трахать вас, миссис Адамс!.."
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 900644
            w
            imgd 900646
            whore "Аааа!"
#            sound vjuh3
            img 900647
            show screen dream()
            show screen dream_focus(1000, 265, 4.0, 0.95)
            with vpunch
            teacher_adams "Оттрахай миссис Адамс, студент! Оттрахай как следует!"
            teacher_adams "Миссис Адамс сейчас кончит!"
            bardi "О, ееее!.."
#            imgd 900646
            img 900645
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound woman_moan11
            whore "ААААА!"
            # шлюха кончает
            img 900646
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound woman_moan12
            whore "АААААААА!!!"
            bardi "О, дааа!!!"
            menu:
                "Кончить в нее.":
                    # Барди бурно кончает в нее
                    img 900648
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    w
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    sound man moan8
                    bardi "Дааа!!!"
                    bardi "Оооо!!!"
                    sound2 chpok5
                    imgd 900649
                    bardi "О, какой кайф..."
                    pass
                "Кончить на нее.":
                    # Барди бурно кончает на нее
                    img 900650
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    w
                    sound bulk1
                    show screen photoshot_screen()
                    with hpunch
                    pause 0.7
                    hide screen photoshot_screen
                    sound man moan8
                    bardi "Дааа!!!"
                    bardi "Оооо!!!"
                    sound2 chpok5
                    imgd 900651
                    bardi "О, какой кайф..."
                    pass
            # дверь в комнату Шона резко открывается и он в кипише влетает внутрь
            $ questLog(6, True)
            music stop
            sound plastinka1b
            img 900652 hpunch
            sean "Бро! Твою мать!"
            music Fly_With_Me_short
            sean "Моя мама домой пришла! Убегайте! Быстро!"
            # Барди и шлюха вскакивают с кровати
            sound Jump2
            img 900653 vpunch
            bardi "Фак!.."
            # Шон подбегает к ним и подталкивает их к окну
            pass
    img 900653
    sean "Быстро убегайте!"
    # Барди хватает одежду, а Шон впихивает одежду шлюхи ей в руки
    imgd 900654
    sean "Мать меня убьет, если увидит что здесь происходит!"
    imgd 900655
    bardi "Как мы убежим, чувак?!"
    bardi "Твоя мама в холле?"
    sound Jump2
    img 900654 vpunch
    sean "Да! Она идет сюда!"
    imgd 900656
    whore "Шон? С кем ты разговариваешь?"
    # Шон нетерпеливо отмахивается от нее
    sound vjuh3
    img 900657 hpunch
    sean "Некогда! Все потом!"
    sean "Сваливайте быстрее! Мне будет конец, если мама увидит ЭТО!"
    img 900658
    whore "Что происходит?"
    imgd 900659
    sean "Давайте в окно!"
    bardi "В окно?!"
    whore "Эй! Какое окно?! Вы чего, совсем сдурели?!"
    # она хватается за маску
    sound Jump1
    imgd 900660
    whore "Чертова маска!.."
    # в это время голос из-за двери и стук, шлюха застывает, не сняв маску
    sound snd_door_knock
    img 900661 vpunch
    bardie_friend_mother "ШОН?"
    bardie_friend_mother "Почему у тебя закрыта дверь?!"
    bardie_friend_mother "Открой дверь, Шон! Что там у тебя происходит?!"
    # стук
    # Шон подталкивает к окну сначала Барди (показываем как Барди забирается на подоконник)
    # и берет за руку шлюху, притягивая ее к себе, та до сих пор не сняла свою повязку
    sound2 snd_door_knock
    img 900660
    sean "Нахрен твою маску! Все потом!!!"
    imgd 900662
    sound snd_door_knock
    bardi "!!!"
    sean "Да быстрее же!!!"
    sound2 Jump1
    img 900663 vpunch
    bardi "!!!!!"
    # затемнение
    # Барди со шлюхой стоят на улице под окном Шона (на улице уже вечер)
    # сверху доносится голос Шона
    fadeblack
    sound snd_back1
#    sound snd_take_paper
    pause 2.0
    music Adventures_of_the_Deaf_Dreamer
    imgfl 900665
    sean "Вы целы, чувак?"
    bardi "Да, все в порядке."
    sean "Окей. Тогда до связи. Пока."
    bardi "Пока, Шон."
    # Барди смотрит на шлюху
    # шлюха подносит руку к повязке
    imgf 900666
    bardi_t "Если она сейчас снимает свою дурацкую повязку..."
    bardi_t "Она поймет, что трахалась не с Шоном."
    sound vjuh4
    img 900667 vpunch
    whore "Эта гребаная повязка меня уже достала!.."
    # шлюха снимает повязку и удивленно смотрит на Барди
    # начинает одеваться
    music stop
    sound plastinka1b
    img 900668 hpunch
    whore "?!?!"
    bardi "..."
    music Step_By_Step
    whore "Ты кто такой вообще?!"
    sound2 swish
    imgf 900669
    whore "Где Шон?"
    imgd 900670
    whore "Какого хрена мы вышли в окно? Что блин происходит?!"
    imgd 900671
    bardi "Эй, Бекки. Без паники."
    bardi "Я [mcname], друг Шона."
    imgd 900672
    whore "Друг?!"
    whore "Он что, притащил меня сюда для тебя?"
    whore "А я думала, что клиентом он будет..."
    imgd 900671
    bardi "Нуу..."
    whore "Ну вы вообще, парни!.."
    whore "Я и так отработала бы с тобой. Зачем нужен был весь этот цирк?"
    imgf 900673
    bardi_t "Эта Бекки работает проституткой?.."
    bardi_t "Хмм... Странно, откуда у Шона деньги на нее?"
    fadeblack
    sound put_dress
    pause 1.5
    music Step_By_Step
    imgf 900674
    whore "А что случилось то? Кто пришел и зачем мы убегали?"
    whore "Я вообще ничего не поняла."
    imgd 900675
    whore "И что это за место?" # оглядывается
    imgd 900676
    whore "Это дом Шона что-ли?!"
    imgd 900677
    bardi "Эээ..."
    imgd 900674
    whore "Этот придурок заставил меня нацепить дурацкую повязку..."
    whore "Чтобы я не поняла, что он притащил меня к себе домой?!"
    imgd 900677
    bardi "Это дом... Дом одного приятеля..."
    bardi "В общем, неважно."
    # Бекки достает сигарету и закуривает
    imgf 900678
    sound cigar-lighter
    w
    imgd 900679
    w
    imgd 900680
    whore "Ну неважно, так неважно."
    whore "Блин, весь кайф обломали!"
    whore "В кои то веки кончила при трахе с клиентом, а тут такая хрень с выходом через окно..."
    imgd 900681
    sound cigar-smoke2
    bardi "Обычно не кончаешь?"
    imgd 900682
    sound2 cigar-smoke3
    w
    imgd 900683
    whore "Обычно я хорошо притворяюсь."
    whore "Но с тобой я кайфанула... Как ты говоришь твое имя?"
    imgd 900684
    bardi "[mcname]."
    imgd 900683
    whore "Вот и познакомились, ха-ха..."
    label ep02_dialogues3_sean_loop1:
    imgd 900681
    sound cigar-smoke2
    w
    imgd 900682
    sound2 cigar-smoke3
    bardi "..."
    menu:
        "Сколько Шон тебе заплатил?":
            imgd 900684
            bardi "Бекки, а сколько Шон тебе заплатил за сегодняшнюю встречу?"
            imgd 900685
            whore "У нас с этим мелким свои дела..."
            imgd 900686
            bardi "То есть?"
            # он подмигивает Барди
            imgd 900687
            whore "Не вникай, красавчик."
            jump ep02_dialogues3_sean_loop1
        "Дашь свой номер телефона?":
            imgd 900684
            bardi "Если я захочу с тобой провести время..."
            imgd 900685
            whore "Без проблем."
            whore "Вот мой номер телефона." # + новый контакт в телефоне Барди
            if mlsBardiSeanDay3WhorePhone == False:
                call phone_contact4() from _rcall_phone_contact4
                $ whoreCallStage = 1
                $ mlsBardiSeanDay3WhorePhone = True
            whore "Напишешь мне, как надумаешь..."
            jump ep02_dialogues3_sean_loop1
        "Уйти.":
            # Бекки бросает докуренную сигарету на землю
            imgd 900687
            whore "Ну что, студент. Мне пора. Время - деньги."
            whore "Хорошо потрахались, да?"
            imgd 900686
            bardi "Да. Было прикольно."
            imgd 900687
            whore "Пиши, когда захочешь повторить, красавчик."
            whore "Пока."
            # шлюха уходит
            pass
    # Барди смотрит ей вслед
    sound steps_park
    imgf 900628
    bardi_t "Хмм... Удачно я зашел к Шону в гости..."
    bardi_t "Трах со шлюхой, да еще и на халяву."
    bardi_t "Интересно, сколько стоят ее услуги?"
    bardi_t "И что за дела могут быть у Шона и проститутки Бекки?"
    bardi_t "Нужно будет в этом разобраться..."
    return

# при клике на любую локацию, кроме дома Барди
label ep02_dialogues3_sean_4:
    # мысли, не рендерить!!
    bardi_t "Мне нужно идти домой. Я обещал Софи не задерживаться после колледжа..."
    return

# при клике на строку контакта "whore"
label ep02_dialogues3_sean_5:
    bardi "Привет, Бекки."
    whore "Привет. Это кто?"
    menu:
        "[mcname], друг Шона.":
            pass
        "Позже ей напишу.":
            pass
    bardi "[mcname], друг Шона."
    whore "А, поняла. Привет, красавчик."
    whore "У тебя появилось желание еще раз поиграть со мной?"
    bardi "Появилось. Я бы повторил."
    bardi "Сколько это будет стоить?"
    whore "По прайсу, красавчик."
    bardi "Это сколько?"
    whore "С проникновением 90 баксов."
    bardi "90?!"
    bardi "А минет?"
    whore "50."
    bardi "Окей. Я тебе позже напишу."
    whore "Стой. Для тебя я сделаю скидку. Возьму 70 за секс."
    bardi "А за минет 30?"
    whore "Да. Мне редко бывает прикольно с клиентами, так как было с тобой ;)"
    bardi "Как насчет вирта?"
    whore "Такое только для постоянных клиентов."
    whore "Давай хотя бы еще раз встретимся лично, красавчик?"
    bardi "Понял. Я тебе напишу, когда у меня будет возможность встретиться."
    whore "Буду ждать, красавчик. Пока."
    bardi "Пока."
    return

# при повторном клике на строку контакта "whore", если уже переписывался с ней
label ep02_dialogues3_sean_5a:
    menu:
        "Написать Бекки.":
            pass
        "Не писать.":
            bardi_t "Нет, я не буду платить за секс."
            bardi_t "Я найду способ сделать это, не потратив ни цента."
            bardi_t "Пусть даже не с этой Бекки..."
            return
    bardi "Привет, Бекки."
    whore "Привет, красавчик."
    whore "Надумал встретиться?"
    bardi "Еще думаю."
    bardi "Бекки, ты можешь мне скинуть свою фотку?"
    whore "Нахрена мне это делать, красавчик?"
    bardi "Я тебе заплачу 1 бакс за фотку."
    whore "1 бакс?"
    bardi "Да."
    whore "За бакс без обнаженки."
    bardi "Окей."
    # шлюха кидает фотку груди в топе-сеточки, крупным планом
    Whore_1 # img в телефон
    # у Барди на балансе минус 1 бакс
    whore "Доволен?"
    bardi "Ееее! Красотка!"
    whore "После личной встречи смогу кидать тебе фотки погорячее."
    bardi "Понял. Напишу тебе."
    whore "Буду ждать, красавчик. Пока."
    bardi "Пока."
    return

# если еще раз кликает на контакт "whore" после того, как она прислала фотку
label ep02_dialogues3_sean_5b:
    # мысли, не рендерить!!
    bardi_t "Я напишу ей позже. Сначала нужно найти денег на ее услуги."
    bardi_t "Я и так потратил один бакс из тех денег, что откладываю на билет."
    bardi_t "Целый бакс!.. За фотку сисек шлюхи!"
    bardi_t "Вот я придурок! Такими темпами я точно ничего не накоплю..."
    return

# после переписки со шлюхой
label ep02_dialogues3_sean_5c:
    # мысли, не рендерить!!
    bardi_t "Вот это прайс у проститутки Бекки!"
    bardi_t "Фак!"
    bardi_t "Мне сейчас не по карману даже минет в ее исполнении..."
    bardi_t "Да и Шону она не по карману с таким прайсом!"
    bardi_t "Тогда как он организовал встречу с ней?.."
    return

# клик на строку контакта "sean" после сцены со шлюхой в его доме
label ep02_dialogues3_sean_6:
    bardi "Эй, бро, ты как?"
    bardi "Твоя мама ничего не заподозрила?"
    sean "Привет, чувак!"
    sean "Нет, все в порядке."
    sean "Но палево было жесткое!"
    bardi "Эта твоя Бекки подумала, что я - это ты :)"
    sean "Я так и понял, бро. Не парься, все окей. xD"
    bardi "А нахрена ты ей повязку нацепил?"
    sean "Ты не поверишь, чувак. Бекки знакома с моей мамой - они раньше учились вместе."
    sean "Если бы они встретились, было бы капец как неудобно."
    bardi "xD"
    sean "Эх, жаль, что я не успел ей присунуть. Надо бы заказать ее еще раз."
    bardi "Еще раз? А откуда у тебя деньги на шлюху? Накопил?"
    sean "Не-а. Там другая тема, бро."
    sean "Пока не могу рассказать. Позже."
    bardi "Окей. Снова интрига :)"
    sean ";)"
    return
