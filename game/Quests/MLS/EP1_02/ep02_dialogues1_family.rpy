default mlsBardiDay3SophieMoney1 = 0 # Барди взял у Софи первые 5 долларов (крыса)
default mlsBardiDay3SophieMoney2 = 0 # Барди взял у Софи первые 5 долларов, пообещав отдать их (кролик)

#call ep02_dialogues1_family_1() # утро, комната Барди, душ
#call ep02_dialogues1_family_2() # кухня, разговор с Софи

define v_MC_Dream1_Sister_Older_1_25_sound_name = "v_MC_Dream1_Sister_Older_1_25"
define v_MC_Dream1_Sister_Older2_25_sound_name = "v_MC_Dream1_Sister_Older2_25"
define v_MC_Dream1_Nice_Girl1_25_sound_name = "v_MC_Dream1_Nice_Girl1_25"
define v_MC_Dream1_Maurice1_25_sound_name = "v_MC_Dream1_Maurice1_25"
define v_MC_Dream_Maurice2_25_sound_name = "v_MC_Dream_Maurice2_25"

# момент, на котором закончился 1-й апдейт
# комната Барди
label ep02_dialogues1_family_1:
    # Софи, шикоро раскрыв глаза, удивленно смотрит на оттопыренное одеяло в районе паха Барди
    # он в шоке смотрит на нее (мы всю сцену смотрим глазами Барди)
    music Story_of_One_Success_1
    imgf 900450
    bardi_t "Вот тебе и 'доброе утро', твою мать!"
    # немая пауза
    sound vjuh3
    imgd 900451
    sophie_t "Это?.. О, Боже!"
    sophie_t "Как неловко вышло!.."
    # Софи прикрывает глаза рукой
    # Барди выходит из ступора, садится на кровати, прикрывая стояк рукой
    sound vjuh3
    img 900452 vpunch
    bardi "Софи, я.."
    # она его перебивает, быстро проговорив
    music Little_Tomcat
    imgf 900454
    sophie "[mcname], милый..."
    sophie "Тебе не стоит волноваться из-за этого..."
    imgd 900455
    sophie "В твоем возрасте это... В общем, это нормально."
    sophie "И мне очень неудобно, что я поставила тебя в такую неловкую ситуацию."
    # неловкая пауза
    imgd 900453
    bardi "..."
    sophie "..."
    # Софи смущенно опускает взгляд и говорит
    imgd 900455
    sophie "Жду тебя на кухне, милый. Завтрак уже готов."
    # и она быстро выходит из его комнаты, он ей бросает в догонку
    imgf 900456
    sound snd_walk_barefoot
    bardi "Хорошо, Софи."
    # Барди остается один в своей комнате, психует
    music Adventures_of_the_Deaf_Dreamer
    imgd 900457
    bardi_t "Вот какого хрена!?"
    bardi_t "Мне такой сон прикольный снился!.."
    bardi_t "И такой облом!"
    # Барди откидывает одеяло и встает, смотрит на свой стояк
    sound snd_walk_barefoot
    imgf 900458
    bardi_t "С ЭТИМ на кухню точно не стоит идти..."
    bardi_t "Сначала нужно сбросить напряжение."
    bardi_t "Самое время принять душ."
    return 

label ep02_dialogues1_family_1c():
    fadeblack 1.0
    sound sneaks_1
    pause 1.5
    # затемнение, шаги
    # смена локации на душ, шум воды
    # Барди стоит в душе голый, со стояком
    # обхватывает стояк рукой и начинает водить по нему
    music Adventures_of_the_Deaf_Dreamer
    music2 snd_shower3
    imgf 900471
    bardi_t "Здесь мне точно никто не помешает..."
    imgd 900472
    w
    sound drkanje5
    imgd 900473
    w
    sound drkanje5
    imgd 900474
    w
    sound drkanje5
    imgd 900473
    w
    sound drkanje5
    imgd 900472
    w
    sound drkanje5
    imgd 900473
    w
    menu:
        "Оливия." if mlsBardiDay2Family2 > 0:
            # у него перед глазами возникает голая Оливия (с ним в душе)
            # она стоит голая рядом с ним, улыбается ему игриво
            # Барди смотрит вниз
            # уже не его рука двигается на члене, а ее
            #
            $ notif(_("[mcname] подсматривал за Оливией в душе."))
            #
            # Оливия пошло улыбается ему и подмигивает
            fadeblack 1.5
            music Stylish_Hip_Hop_Rock
            imgf 900475
            olivia "[mcname], пошалим немного, пока Софи не видит?"
            #sound vjuh3
            imgd 900476
            olivia "Мне так нравится твой член..."
            # она водит рукой по члену, прикасаясь к головке
            sound drkanje5
            imgd 900477
            w
            sound drkanje5
            imgd 900476
            w
            sound drkanje5
            imgd 900477
            w

            # video
            # v_MC_Dream1_Sister_Older_1_25
            $ localSoundVolume = 1.0
            $ localSoundName = v_MC_Dream1_Sister_Older_1_25_sound_name
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(getMusicScenes(0.2), 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_MC_Dream1_Sister_Older_1_25= Movie(play="video/v_MC_Dream1_Sister_Older_1_25.mkv")
            show videov_MC_Dream1_Sister_Older_1_25
            with fade
            olivia "Мммм..."
            wclean
            olivia "Он такой большой и твердый..."
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")


            # Оливия пристально смотрит на лицо Барди и пошло улыбается
            imgf 900478
            olivia "Я вижу, как ты хочешь меня, [mcname]..."
            olivia "Хочешь прикасаться ко мне... Целовать меня..."
            imgd 900479
            bardi "Даа..."
            imgd 900478
            olivia "Хочешь трахнуть меня?.."
            imgd 900480
            bardi "О, даа!.."
            imgd 900481
            olivia "Мммм... Да, я вижу, как ты этого хочешь."
            # лицо Оливии приближается к Барди и она томно шепчет
            imgf 900482
            w
            imgd 900483
            olivia "А я хочу, чтобы ты кончил, [mcname]..."
            # Барди смотрит вниз на свой член, как рука Оливии двигается по нему
            imgf 900484
            w
            sound drkanje5
            imgd 900485
            w
            sound drkanje5
            imgd 900484
            w

            # video
            # v_MC_Dream1_Sister_Older2_25
            $ localSoundVolume = 1.0
            $ localSoundName = v_MC_Dream1_Sister_Older2_25_sound_name
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(getMusicScenes(0.2), 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_MC_Dream1_Sister_Older2_25= Movie(play="video/v_MC_Dream1_Sister_Older2_25.mkv")
            show videov_MC_Dream1_Sister_Older2_25
            with fade
            olivia "Мммм..."
            wclean
            olivia "Сделай это... Ну давай же..."
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            # Барди поднимает глаза на лицо Оливии и внезапно вместо него видит лицо Софи (лицо крупным планом, тела не видно)
            sound vjuh3
            img 900486 vpunch
            sophie "Сделай это для меня, [mcname]..."
            # Барди при ее появлении бурно кончает
            img 900487
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
            bardi "Оооо!.."
            bardi "ОООООО!!!"
            img 900486
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man moan8
            bardi "О, ЧЕЕЕРТ!!!"
            sound2 chpok5
            img 900488
            w
            # Софи улыбается и исчезает, Барди снова один в душе, психует
            imgf 900489
            w
            music Adventures_of_the_Deaf_Dreamer_short
            img 900490 vpunch
            bardi_t "Да что за хрень со мной происходит?!"
            bardi_t "Фак!!!"
            # смотрит вниз на свой опавший член, он в ступоре
            imgd 900491
            bardi_t "..."
            bardi_t "....."
            bardi_t "Что это было сейчас?!"
            bardi_t "Я же не мог так отреагировать на появление Софи?.."
            imgf 900492
            bardi_t "Или..."
            bardi_t "Да твою мать! Что за идиотские мысли?"
            bardi_t "Конечно, не мог! Что за бред?!"
            bardi_t "Я просто еще не проснулся, вот что происходит."
            bardi_t "Это просто остатки сна."
            bardi_t "Забиваешь себе голову всякой хренью с самого утра. Придурок."
            pass
        "Оливия ([mcname] не подсматривал за Оливией в душе) (disabled)" if mlsBardiDay2Family2 == 0:
            pass
        "Роуз." if mlsBardiFirstDayCollege1 == 0:
            # у него перед глазами возникает голая Роуз (с ним в душе)
            # она голая сидит перед ним на коленях, смущенно улыбается и смотрит в глаза снизу вверх
            # уже не его рука двигается на члене, а ее
            #
            $ notif(_("[mcname] в колледже общался с Роуз."))
            #
            # Роуз смущена
            fadeblack 1.5
            music Stylish_Hip_Hop_Rock
            imgf 900493
            student_rose "[mcname], а ты уверен, что Софи нас не застанет?"
            student_rose "Это будет крайне неловко для меня..."
            # она опускает взгляд и смотрит на его член, водит рукой по нему
            imgd 900494
            w
            sound vjuh3
            imgd 900495
            student_rose "Мне так нравится прикасаться к твоему члену."
            imgd 900496
            student_rose "А тебе нравится, как я делаю это?"
            imgf 900497
            bardi "Да, Роуз... Главное, не останавливайся..."
            # Роуз снова поднимает лицо и смотрит на лицо Барди
            imgd 900498
            student_rose "Хи-хи. Я стараюсь, [mcname]."
            imgd 900499
            bardi "Обхвати его сильнее, Роуз."
            # Роуз вновь смотрит на член
            imgf 900500
            student_rose "Вот так?"
            sound drkanje5
            imgd 900501
            bardi "Даа!.. И двигай быстрее рукой."
            sound drkanje5
            imgd 900502
            student_rose "Ох, еще быстрее? Сейчас."
            sound drkanje5
            imgd 900501
            w
            sound drkanje5
            imgd 900500
            w

            # video
            # v_MC_Dream1_Nice_Girl1_25
            $ localSoundVolume = 1.0
            $ localSoundName = v_MC_Dream1_Nice_Girl1_25_sound_name
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(getMusicScenes(0.2), 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_MC_Dream1_Nice_Girl1_25= Movie(play="video/v_MC_Dream1_Nice_Girl1_25.mkv")
            show videov_MC_Dream1_Nice_Girl1_25
            with fade
            student_rose "Вот так хорошо?"
            wclean
            bardi "Мммм... Еще!.."
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 900503
            w
            # Роуз снова смотрит на лицо Барди
            # Барди смотрит вниз на свой член, как рука Роуз двигается по нему
            imgd 900498
            student_rose "Я все правильно делаю, [mcname]?"
            # Барди фокусируется на своем члене и руке на нем, не смотрит на лицо
            imgd 900504
            student_rose "Думаю, что все правильно. Ты совсем скоро кончишь..."
            sound drkanje5
            imgd 900505
            w
            sound drkanje5
            imgd 900504
            w
            sound drkanje5
            imgd 900505
            w
            sound drkanje5
            imgd 900504
            w
            # Барди переводит фокус на лицо Роуз и внезапно вместо него видит лицо Софи  (лицо крупным планом, тела не видно)
            sound vjuh3
            img 900486 vpunch
            sophie "Сделай это для меня, [mcname]..."
            # Барди при ее появлении бурно кончает
            img 900506
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
            bardi "Оооо!.."
            bardi "ОООООО!!!"
            sound2 chpok5
            img 900507
            bardi "О, ЧЕЕЕРТ!!!"
            # Софи улыбается и исчезает, Барди снова один в душе, психует
            imgf 900489
            w
            music Adventures_of_the_Deaf_Dreamer_short
            img 900490 vpunch
            bardi_t "Да что за хрень со мной происходит?!"
            bardi_t "Фак!!!"
            # смотрит вниз на свой опавший член, он в ступоре
            imgd 900491
            bardi_t "..."
            bardi_t "....."
            bardi_t "Что это было сейчас?!"
            bardi_t "Я же не мог так отреагировать на появление Софи?.."
            imgf 900492
            bardi_t "Или..."
            bardi_t "Да твою мать! Что за идиотские мысли?"
            bardi_t "Конечно, не мог! Что за бред?!"
            bardi_t "Я просто еще не проснулся, вот что происходит."
            bardi_t "Это просто остатки сна..."
            bardi_t "Забиваешь себе голову всякой хренью с самого утра. Придурок."
            pass
        "Роуз ([mcname] толкнул Гарри и не разговаривал с Роуз) (disabled)" if mlsBardiFirstDayCollege1 > 0:
            pass
        "Миссис Морис." if mlsBardiFirstDayCollege1 > 0:
            # у него перед глазами возникает преподавательница (с ним в душе)
            # она голая сидит перед ним на коленях
            # уже не его рука двигается на члене, а ее
            #
            $ notif(_("[mcname] в колледже познакомился с миссис Морис."))
            #
            # училка игриво улыбается и смотрит в глаза снизу вверх
            fadeblack 1.5
            music Stylish_Hip_Hop_Rock
            imgf 900508
            teacher_morris "[mcname], мне так нравится, когда ты такой возбужденный..."
            teacher_morris "Меня так заводит это..."
            imgd 900509
            w
            # она опускает взгляд и смотрит на его член, водит рукой по нему
            imgd 900510
            teacher_morris "Может, в следующий раз попробуем сделать это в кабинете живописи?"
            imgf 900511
            teacher_morris "Останешься после занятий, мы закроем дверь и уединимся с тобой..."
            bardi "Да, миссис Морис..."
            # училка смотрит на его член
            # медленно приближает к нему лицо и облизывает головку языком
            imgd 900512
            teacher_morris "Мммм... Как же мне нравится твой член."
            sound vjuh3
            imgd 900513
            teacher_morris "Такой твердый, такой горячий..."
            sound lick3
            imgd 900514
            w
            # еще раз проводит языком
            imgf 900515
            bardi "Даа!.. Еще!.."
            sound lick3
            imgd 900516
            w
            sound lick3
            imgd 900517
            w
            # она продолжает работать рукой

            # video
            # v_MC_Dream1_Maurice1_25
            $ localSoundVolume = 1.0
            $ localSoundName = v_MC_Dream1_Maurice1_25_sound_name
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(getMusicScenes(0.2), 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_MC_Dream1_Maurice1_25= Movie(play="video/v_MC_Dream1_Maurice1_25.mkv")
            show videov_MC_Dream1_Maurice1_25
            with fade
            teacher_morris "Мпфхфмм..."
            wclean
            bardi "О, как же это охрененно!.."
            teacher_morris "Мммм..."
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 900518
            w
            imgd 900508
            teacher_morris "Тебе нравится?"
            imgd 900519
            bardi "Даа... О, даа!.."
            imgf 900520
            teacher_morris "Хочешь заняться чем-то более интимным со мной, [mcname]?."
            # училка снова смотрит на лицо Барди
            # Барди смотрит вниз на свой член, как рука училки двигается по нему
            imgd 900521
            teacher_morris "Мммм... Да, я вижу, как ты этого хочешь."
            sound drkanje5
            imgd 900522
            w
            # Барди фокусируется на своем члене и руке на нем, не смотрит на лицо
            sound drkanje5
            imgd 900523
            w
            sound drkanje5
            imgd 900522
            w
            sound drkanje5
            imgd 900521
            w

            # video
            # v_MC_Dream_Maurice2_25
            $ localSoundVolume = 1.0
            $ localSoundName = v_MC_Dream_Maurice2_25_sound_name
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(getMusicScenes(0.2), 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_MC_Dream_Maurice2_25= Movie(play="video/v_MC_Dream_Maurice2_25.mkv")
            show videov_MC_Dream_Maurice2_25
            with fade
            teacher_morris "Мммм..."
            wclean
            teacher_morris "А я хочу, чтобы ты кончил, [mcname]..."
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            # Барди переводит фокус на лицо училки и внезапно вместо него видит лицо Софи (лицо крупным планом, тела не видно)
            sound vjuh3
            img 900486 vpunch
            sophie "Сделай это для меня, [mcname]..."
            # Барди при ее появлении бурно кончает
            img 900524
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
            bardi "Оооо!.."
            bardi "ОООООО!!!"
            sound2 chpok5
            img 900525
            bardi "О, ЧЕЕЕРТ!!!"
            # Софи улыбается и исчезает, Барди снова один в душе, психует
            imgf 900489
            w
            music Adventures_of_the_Deaf_Dreamer_short
            img 900490 vpunch
            bardi_t "Да что за хрень со мной происходит?!"
            bardi_t "Фак!!!"
            # смотрит вниз на свой опавший член, он в ступоре
            imgd 900491
            bardi_t "..."
            bardi_t "....."
            bardi_t "Что это было сейчас?!"
            bardi_t "Я же не мог так отреагировать на появление Софи?.."
            imgf 900492
            bardi_t "Или..."
            bardi_t "Да твою мать! Что за идиотские мысли?"
            bardi_t "Конечно, не мог! Что за бред?!"
            bardi_t "Я просто еще не проснулся, вот что происходит."
            bardi_t "Это просто остатки сна..."
            bardi_t "Забиваешь себе голову всякой хренью с самого утра. Придурок."
            pass
        "Миссис Морис ([mcname] нагрубил Гарри и не разговаривал с миссис Морис) (disabled)" if mlsBardiFirstDayCollege1 == 0:
            pass
    music2 stop
    fadeblack 1.5
    # шум воды прекращается - Барди выключает душ
    # затемнение
    # квест-лог "Идти на кухню."
    return


# кухня
label ep02_dialogues1_family_2:
    # Барди заходит на кухню, Софи стоит там у столешницы
    # при клике на нее (она все еще немного смущена)
    music Little_Tomcat
    imgf 900459
    sophie "[mcname], ты так долго..."
    sophie "Завтракай и бегом в колледж, иначе ты опоздаешь."
    imgd 900058
    bardi "Хорошо, Софи."
    imgd 900460
    sophie "Я еще хотела сказать..."
    sophie "Может быть, это не совсем удобно для тебя, что я бужу тебя по утрам, [mcname]?"
    imgd 900461
    bardi_t "Черт!.. Она снова об этом."
    bardi_t "Нужно сделать вид, что ничего особого не произошло."
    bardi_t "В том числе, и в душевой..."
    bardi "Все окей, Софи."
    bardi "Будильник вряд ли справится с этой сложной задачей."
    # Софи улыбается ему
    imgd 900057
    sophie "Хорошо, милый."
    # она прикасается к его лицу
    sound snd_walk_barefoot
    imgf 900462
    sophie "Как твой синяк? Не болит?"
    imgd 900463
    bardi "Не-а."
    # если солгал Софи про синяк
    if mlsBardiDay2Family1 > 0:
        #
        $ notif(_("[mcname] солгал Софи и сказал, что ударился о шкафчик."))
        #
        imgd 900464
        sophie "Ты поаккуратнее сегодня с этим коварным шкафчиком в колледже."
        imgd 900463
        bardi "Хорошо, Софи."
    # если сказал правду про синяк
    else:
        imgd 900464
        sophie "Если этот хулиган Гарри и дальше тебя будет доставать..."
        imgd 900463
        bardi "Перестань беспокоиться об этом, Софи. Я сам с ним разберусь."
    # она улыбается и треплет его по волосам
    imgd 900464
    sophie "Надеюсь, тебя ждет удачный день."
    sophie "Ох, я чуть не забыла!"
    # она берет со столешницы или из кармана халата купюру и протягивает ее Барди
    sound swish
    imgf 900465
    w
    sound vjuh3
    imgd 900466
    sophie "Вот твои пять долларов, о которых мы вчера говорили."
    # Барди смотрит на руку Софи с зажатой купюрой
    imgd 900467
    bardi_t "По ее реакции за ужином было понятно, что эти пять баксов для нее совсем не лишние."
    bardi_t "..."
    $ menu_data = {
        "Мне эти деньги нужнее.": {"info_rat":True},
        "Взять в долг.": {"info_rabbit":True}
    }
    menu:
        "Мне эти деньги нужнее.": # (+Rat)
            call rrmeter(-5, "ep02_dialogues1_family_2")
            imgd 900467
            bardi_t "Но мне эти деньги нужнее."
            bardi_t "Притом, что такое пять баксов? Это же ерунда..."
            # Барди протягивает руку и забирает деньги
            imgf 900468
            $ add_money(5.0)
            bardi "Спасибо, Софи."
            imgd 900056
            bardi "Следующие пять баксов будут через неделю?"
            # она смущенно улыбается
            imgd 900469
            sophie "Да, [mcname]. Я смогу дать тебе еще денег не раньше, чем через неделю..."
            imgd 900056
            bardi "Окей."
            $ mlsBardiDay3SophieMoney1 = day # Барди взял у Софи первые 5 долларов (крыса)
            pass
        "Взять в долг.": # (+Rabbit)
            call rrmeter(5, "ep02_dialogues1_family_2")
            imgd 900467
            bardi_t "Но мне они тоже нужны. Мне нужно собирать деньги на билет..."
            bardi_t "Я могу сейчас взять эти деньги в долг."
            # Барди протягивает руку и забирает деньги
            imgf 900468
            $ add_money(5.0)
            bardi "Софи, я тут подумал..."
            imgd 900056
            bardi "Если у Генри получится договориться о моей подработке..."
            bardi "То я тебе отдам эти пять долларов, когда заработаю денег."
            # Софи умиляется
            imgd 900469
            sophie "Хорошо, [mcname]."
            sophie "[mcname], как же ты повзрослел..."
            $ mlsBardiDay3SophieMoney2 = day # Барди взял у Софи первые 5 долларов, пообещав отдать их (кролик)
            pass
    # + 5 баксов у Барди
    imgd 900056
    bardi "До вечера, Софи."
    imgd 900057
    sophie "До вечера, милый."
    # она снова ему мило улыбается и принимается что-то делать на кухне
    sound snd_walk_barefoot
    imgf 900470
    if mlsBardiDay3SophieMoney1 > 0:
        bardi_t "Еее! Первые деньги на билет уже в кармане. Начало положено!"
    bardi_t "Надо бы вечером поинтересоваться у Генри про подработку в велопрокате..."
    # квест-лог "Идти в колледж."
    return

# при повторном клике на Софи, если уже разговаривали - ep01_dialogues3_day2_family_5 (регулярный разговор)
