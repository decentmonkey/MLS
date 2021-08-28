default monicaBettyLiamFred1 = 0 # Бетти пошла к соседу забирать свой утюг
default monicaBettyLiamFred2 = 0 # Бетти согласилась помочь соседу с утюгом
default monicaBettyLiamFred3 = 0 # Бетти согласилась на секс с соседом (DP с Фредом)

default monicaBettyLiamVisit3_cumzone1 = 0

default v_Betty_Neighbour_Blowjob2_1_sound_name = "v_Betty_Neighbour_Blowjob2_1"
default v_Betty_Neighbour_Sex2_1_sound_name = "v_Betty_Neighbour_Sex2_1"
default v_Betty_Neighbour_Fred_Sex1_1_sound_name = "v_Betty_Neighbour_Fred_Sex1_1"

#call ep217_dialogues3_betty_1() # Бетти пошла к соседу забирать свой утюг
#call ep217_dialogues3_betty_2() # Бетти секс с Фредом и соседом


# при условии, что Бетти уже помогла соседу
# при переходе Моники на какую-нибудь локацию
# показываем Бетти в доме
label ep217_dialogues3_betty_1:
    # тем временем
    # Бетти стоит у зеркала и смотрит на себя
    scene black_screen
    with Dissolve(1)
    music stop
    call textonblack(t_("Утро...")) from _rcall_textonblack_17
    scene black_screen
    with Dissolve(1)
    music Groove2_85
    imgfl 14655
    betty_t "Этот Лиам так переживает из-за своей проблемы..."
    betty_t "Кто та черствая женщина, кто мог поселить в нем такую неуверенность?"
    betty_t "Сразу видно, что это была непорядочная женщина."
    betty_t "Не то, что я!"
    imgf 19246
    betty_t "Я ему помогла, потому что я добрая и отзывчивая."
    betty_t "Он хороший сосед, а соседям нужно помогать!"
    betty_t "И с утюгом я ему помогла! Я не могла поступить иначе."
    betty_t "Ведь я хорошая хозяйка!"
    music Hidden_Agenda
    imgd 14656
    betty_t "Только... Надо бы забрать у него мой утюг..."
    betty_t "Как я могла его забыть? Все из-за Фреда!"
    betty_t "Еще несколько секунд и он увидел бы, что я помогала Лиаму."
    betty_t "Водителю совсем необязательно знать, чем занимается хозяйка дома!"
    music Groove2_85
    imgf 32872
    betty_t "Это мое личное дело - помогать соседу или нет!"
    betty_t "И вообще! Лиам мог бы и сам принести утюг!"
    betty_t "Теперь мне приходится тратить на это свое время!"
    menu:
        "Сходить к соседу за утюгом.":
            $ monicaBettyLiamFred1 = day # Бетти пошла к соседу забирать свой утюг
            pass
        "Не ходить. (прерывание квеста)":
            imgd 32873
            betty_t "Хотя..."
            betty_t "Достаточно того, что я уже ему помогла!"
            betty_t "Пусть сам принесет мне мой утюг!"
            betty_t "А у меня есть другие важные дела!"
            return False
    # Бетти выходит из комнаты
    # затемнение
    # Бетти выходит во двор, и с деловым видом идет в сторону ворот
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Hidden_Agenda
    imgfl 32874
    w
    imgf 32875
    fred "Добрый день, Миссис Робертс!"
    betty "Здравствуй, Фред."
    # Бетти проходит мимо него
    sound highheels_short_walk
    imgd 32876
    w
    # Фред за ней наблюдает, смотрит ей вслед, многозначительно улыбаясь
    return True

# дом соседа, при клике на входную дверь
label ep217_dialogues3_betty_2:
    # затемнение, стук в верь, звук двери, шаги
    # Бетти и Лиам стоят в его гостиной
    # сосед удивлен ее визиту
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 32877
    w
    imgf 32878
    sound snd_door_knock
    w
    fadeblack
    sound man_steps
    pause 2.0
    sound snd_door_open1
    pause 1.5
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 32879
    w
    imgf 32880
    liam "Мэм, рад вас видеть!"
    music Hidden_Agenda
    imgd 19262
    betty "Лиам, здравствуйте."
    betty "Я в прошлый раз так торопилась, что..."
    betty "Забыла у вас утюг."
    # он делает удивленный вид
    img 32881
    liam "Правда, Мэм?"
    liam "Я даже не обратил внимания на это..."
    # Бетти с соседом смотрят на стол, на нем расстелены штаны и рядом стоит утюг, продукты со стола, которые мешают, можно убрать. Остальные оставить
    sound Jump2
    imgd 32882
    w
    imgf 32883
    betty "Не обратил внимания?"
    liam "Да, Мэм..."
    liam "Я даже не знаю, как просить вас об этом..."
    liam "Но мне снова нужна ваша помощь, Мэм..."
    music Groove2_85
    imgd 32884
    betty "Какая еще помощь?"
    liam "Мне нужно погладить штаны, а я забыл, как пользоваться этим сложным механизмом..."
    liam "Со множеством кнопок..."
    liam "Вы же знаете, я бы предпочел одну большую кнопку для управления всеми функциями."
    imgf 32885
    betty "Лиам, я же вам все показала в прошлый раз..."
    betty "Там нет ничего сложного."
    liam "Если Мэм мне напомнит, я ей буду очень благодарен за помощь."
    menu:
        "Помочь Лиаму.":
            $ monicaBettyLiamFred2 = day # Бетти согласилась помочь соседу с утюгом
            pass
        "Сам разберется! (прерывание квеста)":
            imgd 32886
            betty "Там нет ничего сложного, поэтому вы сами сможете разобраться!"
            liam "Хорошо, я попробую, Мэм..."
            fadeblack
            sound highheels_short_walk
            pause 2.0
            # Бетти разворачивается и уходит, а он смотрит ей вслед
            return False
    # Бетти задумчиво
    imgd 32887
    betty_t "Если я сейчас откажу ему, это будет грубостью с моей стороны..."
    betty_t "Ведь в прошлый раз я помогла ему."
    betty_t "По-соседски."
    imgd 19279
    betty "Да, Лиам, я помогу вам."
    # Бетти идет в сторону стола, берет в руку утюг
    # Бетти стоит спиной к нему и объясняет как пользоваться утюгом
    sound highheels_short_walk
    imgf 32888
    betty "Включаете утюг..."
    sound switch_steve
    betty "Потом эту кнопку поворачиваете сюда..."
    betty "А потом нажимаете вот сюда."
    # сосед подходит к ней сзади и прижимается
    sound man_steps
    imgd 32889
    w
    music Hidden_Agenda
    imgf 32890
    liam "Ох, Мэм..."
    liam "Я готов вечно смотреть на ваши волшебные ручки."
    liam "Как ловко вы ими управляете."
    liam "И вы такая добрая и отзывчивая, Мэм..."
    # Бетти делает вид, что не замечает его прикосновений
    music Groove2_85
    imgd 19254
    betty "Да, Лиам, я знаю..."
    betty "Я хорошая хозяйка и у меня всегда все получается."
    betty "За что бы я ни бралась..."
    imgd 19255
    liam "Да, Мэм, я заметил это в прошлый раз..."
    liam "Вы мне очень помогли не только с утюгом."
    #
    $ notif(_("Бетти помогла соседу, проверив, достаточно ли твердый у него член."))
    #
    betty "Да?"
    liam "Это правда, Мэм..."
    # он проводит руками по ее попе, талии
    sound Jump1
    img 32891 hpunch
    w
    sound Jump2
    img 32892 vpunch
    liam "Мне перестали сниться кошмары по ночам."
    liam "И я чувствую себя немного увернее, но..."
#    sound ahhh9
    imgf 32893
    betty "Что?"
    liam "Я тут подумал, а вдруг это была простая случайность?"
    music2 stop
    sound plastinka1b
    img 32894 hpunch
    betty_t "Какая еще случайность?"
    music Groove2_85
    betty_t "Что он несет?"
    imgd 32893
    betty "Случайность?"
    liam "Да..."
    music Hidden_Agenda
    liam "Ведь вполне может быть, что..."
    liam "Мой член всего один раз был такой твердый..."
    imgd 19256
    liam "И больше такого не повторится."
    liam "Я теперь очень переживаю из-за этого."
    # Бетти поворачивает голову и смотрит на него подозрительно, не отстраняется
    music Groove2_85
    imgf 32894
    betty_t "На что это он намекает?"
    betty_t "Он что, хочет, чтобы я снова ему помогала?"
    imgd 32895
    betty "Уверена, что это была не случайность, Лиам."
    betty "Ваш член был очень твердый. Это не может быть случайностью..."
    music Hidden_Agenda
    liam "Все же эти навязчивые мысли мешают мне..."
    liam "Если вы, Мэм, как моя хорошая и добрая соседка еще раз мне поможете..."
    imgf 32896
    liam "И я смогу убедиться, что это была не случайность..."
    liam "Тогда я буду самым счастливым мучиной на свете!"
    betty "Помочь еще раз?!"
    liam "Да. Это как прийти к врачу после выздоровления."
    liam "Чтобы убедиться, что ты выздоровел."
    imgd 32897
    liam "Вы же не бросите меня, терзающегося в сомнениях соседа?"
    liam "Ведь я ни к кому больше не могу обратиться с этой проблемой..."
    liam "Я доверился вам одной..."
    liam "Что скажете, Мэм?"
    menu:
        "Я верная жена!":
            $ monicaBettyLiamFred3 = day # Бетти согласилась на секс с соседом (DP с Фредом)
            pass
        "Нет! Я не буду этого делать! (прерывание квеста)":
            # Бетти отстраняется от него, встает руки в боки, возмущенно
            music Groove2_85
            imgf 32898
            betty "Как вы можете мне предлагать подобные вещи?!"
            betty "Я верная жена и порядочная женщина!"
            betty "Вы придумали сами себе какую-то нелепую проблему!"
            betty "Вот сами с этим и разбирайтесь!"
            imgd 32886
            w
            fadeblack
            sound highheels_short_walk
            pause 2.0
            # Бетти разворачивается и уходит возмущенно, а он смотрит ей вслед
            return False
    # Бетти поворачивается к нему, начинает ломаться
    music Groove2_85
    imgf 19257
    betty "Лиам..."
    imgd 32899
    betty "Я верная жена и порядочная женщина..."
    betty "А вы просите меня о подобном..."
    music Hidden_Agenda
    liam "Мэм, у вас поистине целебные ручки."
    liam "Я был под таким впечатлением от них, что долго не мог прийти в себя..."
    imgf 32900
    liam "Теперь Мэм мне снится каждую ночь."
    betty "Правда? Я вам снюсь?"
    # достает свой стояк
    # Бетти снова на него залипает
    imgd 32901
    w
    sound Jump2
    img 32902 vpunch
    w
    imgd 32903
    betty "Но... На вид он достаточно упругий и твердый..."
    betty "Не думаю, что нужна моя помощь..."
    imgf 32904
    liam "Он только кажется таким, Мэм."
    liam "На самом деле, я думаю, что у меня вряд ли получится..."
    # Бетти 'отлипает' от его стояка, как бы приходит в себя
    # пытается возмущаться
    music Groove2_85
    imgd 32905
    betty "Лиам, я не собраюсь делать этого!"
    betty "Мой дом буквально в двух шагах отсюда!"
    betty "И меня ждет мой муж!"
    betty "Тем более, мой водитель чуть не увидел нас в прошлый раз!"
    # берет в руку его член и продолжает ломаться
    sound Jump1
    img 32906 vpunch
    w
    imgd 32907
    betty "Я еще раз вам повторяю, что я верная жена!"
    liam "Вашему мужу очень повезло с такой красивой и верной женой, Мэм!"
    liam "Я искренне ему завидую!"
    liam "У вас такой богатый дом!"
    imgf 32908
    betty "Да! Я хозяйка богатого дома!"
    betty "И я не собираюсь ему изменять!"
    liam "Мэм, ваша помощь - это не измена."
    liam "Вы просто очень хорошая соседка. Поэтому и помогаете мне."
    # Бетти начинает водить рукой по его члену
    sound drkanje5
    imgd 32906
    w
    sound drkanje5
    imgd 32909
    w
    sound drkanje5
    imgd 32906
    w
    sound drkanje5
    imgd 32909
    w
    sound drkanje5
    imgd 32906
    w
    sound drkanje5
    imgd 32909
    w
    sound Jump1
    imgd 32910
    w
    imgf 32907
    betty "Он твердый, как и в прошлый раз!"
    betty "Я уверена, что не нужно ничего больше проверять!"
    music Hidden_Agenda
    liam "Я ведь сосвем чуть-чуть, Мэм..."
    liam "Просто чтобы проверить..."
    imgd 32911
    liam "И сразу уберу его."
    music Groove2_85
    betty "Нет, я не собираюсь делать этого, Лиам!"
    betty "Вы злоупотребляете тем, что у вас такая хорошая соседка!"
    # Бетти идет к дивану, держа соседа за член и ведя таким образом за собой
    # сосед садится на диван, Бетти наклоняется над ним и приближает лицо к его члену
    sound highheels_short_walk
    imgf 32912
    w
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Loved_Up
    imgf 32913
    w
    imgd 32914
    betty_t "Я просто прикоснусь к нему немного..."
    betty_t "Хоть мне это и не нравится."
    betty_t "Но прикосновение - это не измена..."
    imgf 32915
    w
    imgd 32916
    betty "Не вижу необходимости какой-либо проверки!"
    # проводит языком по члену
    sound lick3
    imgf 32917
    w
    imgd 32916
    betty "И вообще!"
    betty "Я никогда не делаю подобного с дургими мужчинами, кроме своего мужа!"
    betty "И вы, Лиам, не исключение!"
    # берет его член в рот, начинает водить голвоой вверх-вниз
    sound hlup25
    imgd 32918
    w
    imgd 32919
    w
    sound chpok6
    img 32920 hpunch
    w

    $ localSoundVolume = 1.0
    $ localSoundName = v_Betty_Neighbour_Blowjob2_1_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Blowjob2_1= Movie(play="video/v_Betty_Neighbour_Blowjob2_1.mkv", fps=25)
    show videov_Betty_Neighbour_Blowjob2_1
    with fade
    liam "О, дааа! Мэээм!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Blowjob2_2= Movie(play="video/v_Betty_Neighbour_Blowjob2_2.mkv", fps=25)
    show videov_Betty_Neighbour_Blowjob2_2
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 32921
    liam "Мээээммммм..."

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Blowjob2_3= Movie(play="video/v_Betty_Neighbour_Blowjob2_3.mkv", fps=25)
    show videov_Betty_Neighbour_Blowjob2_3
    with fade
    liam "Какая же вы замечательная соседка... Мммм..."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Blowjob2_4= Movie(play="video/v_Betty_Neighbour_Blowjob2_4.mkv", fps=25)
    show videov_Betty_Neighbour_Blowjob2_4
    with fade
    liam "Ооох... Еще!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 32922
    w

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Blowjob2_5= Movie(play="video/v_Betty_Neighbour_Blowjob2_5.mkv", fps=25)
    show videov_Betty_Neighbour_Blowjob2_5
    with fade
    liam "Вот так... Да... Не останавливайтесь, Мэм..."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Blowjob2_6= Movie(play="video/v_Betty_Neighbour_Blowjob2_6.mkv", fps=25)
    show videov_Betty_Neighbour_Blowjob2_6
    with fade
    liam "Возьмите его немного глубже... Ооооо..."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 32923
    w
    imgd 32924
    liam "Мммммм..."

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Blowjob2_7= Movie(play="video/v_Betty_Neighbour_Blowjob2_7.mkv", fps=25)
    show videov_Betty_Neighbour_Blowjob2_7
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Blowjob2_8= Movie(play="video/v_Betty_Neighbour_Blowjob2_8.mkv", fps=25)
    show videov_Betty_Neighbour_Blowjob2_8
    with fade
    liam "Быстрее, Мэм! Еще-еще! Дааа!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    fadeblack 1.5
    # Бетти отстраняется, встает
    imgf 32925
    w
    music Groove2_85
    imgd 32926
    betty "Думаю, что этого будет достаточно!"
    img 32927
    liam "Но Мэм..."
    liam "А как же..."
    imgd 32928
    w
    # пока Лиам мямлит, шуршание одежды, кадр на пол, там лежит платье Бетти
    sound put_dress
    imgf 32929
    w
    music Loved_Up
    imgd 32930
    betty_t "Отказывать в помощи соседу, когда он так нуждается в ней - это не по-соседски..."
    betty_t "Я быстренько помогу ему и пойду домой."
    betty_t "Мне еще нужно приготовить Ральфу обед..."
    imgd 32931
    betty "Лиам, только совсем чуть-чуть!"
    betty "И быстро!"
    liam "Да, Мэм... Я только попробую, как в прошлый раз!"
    # Бетти сама лезет на соседа, раскорячивается над ним и садится на его член
    # начинает двигаться
    imgf 32932
    w
    imgd 32933
    w
    imgd 32934
    w
    fadeblack 1.5
    music Loved_Up
    sound ahhh6
    img 32935 vpunch
    w
    sound ahhh8
    imgf 32936
    liam "Оооо, как же хорошо у вас внутри, Мэм..."


    $ localSoundVolume = 1.0
    $ localSoundName = v_Betty_Neighbour_Sex2_1_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Sex2_1= Movie(play="video/v_Betty_Neighbour_Sex2_1.mkv", fps=30)
    show videov_Betty_Neighbour_Sex2_1
    with fade
    betty "Аааах! Дааа..."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")


    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Sex2_2= Movie(play="video/v_Betty_Neighbour_Sex2_2.mkv", fps=30)
    show videov_Betty_Neighbour_Sex2_2
    with fade
    liam "Мне так нравится быть с вами!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")


    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Sex2_3= Movie(play="video/v_Betty_Neighbour_Sex2_3.mkv", fps=30)
    show videov_Betty_Neighbour_Sex2_3
    with fade
    liam "Как же мне повезло, что у меня такая соседка!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Sex2_4= Movie(play="video/v_Betty_Neighbour_Sex2_4.mkv", fps=30)
    show videov_Betty_Neighbour_Sex2_4
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 32937
    sound ahhh6
    betty "Хорошая и порядочная..."
    w

    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Sex2_5= Movie(play="video/v_Betty_Neighbour_Sex2_5.mkv", fps=30)
    show videov_Betty_Neighbour_Sex2_5
    with fade
    wclean
    liam "Да..."
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Sex2_6= Movie(play="video/v_Betty_Neighbour_Sex2_6.mkv", fps=30)
    show videov_Betty_Neighbour_Sex2_6
    with fade
    liam "Еще и хорошая хозяйка..."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 32938
    w
    imgd 32939
    sound ahhh6
    w

    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Sex2_7= Movie(play="video/v_Betty_Neighbour_Sex2_7.mkv", fps=30)
    show videov_Betty_Neighbour_Sex2_7
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Sex2_8= Movie(play="video/v_Betty_Neighbour_Sex2_8.mkv", fps=30)
    show videov_Betty_Neighbour_Sex2_8
    with fade
    betty "Да... И верная жена своего мужа..."
    betty "Поэтому не позволяйте при мне всякие пошлости!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 32940
    sound ahhh8
    w

    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Sex2_9= Movie(play="video/v_Betty_Neighbour_Sex2_9.mkv", fps=30)
    show videov_Betty_Neighbour_Sex2_9
    with fade
    wclean
    liam "О да, Мэм! Ему очень повезло с такой женой, как вы..."
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")


    imgd 32941
    sound ahhh8
    w


    # в самый разгар секса затемнение
    # звук скрип двери
    # смена кадра - в дверь заходит Фред со своей профессиональной улыбочкой
    # Лиам Фреда увидел сразу и самодовольно улыбается ему
    # sound snd_back1
    sound snd_door_open1
    imgf 32942
    w
    sound man_steps
    imgd 32943
    liam "..."
    fred "..."
    # Фред наблюдает с улыбочкой за Бетти и расстегивает штаны
    # Бетти его не замечает и продолжает скакать на Лиаме
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Sex2_10= Movie(play="video/v_Betty_Neighbour_Sex2_10.mkv", fps=30)
    show videov_Betty_Neighbour_Sex2_10
    with fade
    betty "Оооо, еще!!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")


    imgf 32944
    w

    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Sex2_11= Movie(play="video/v_Betty_Neighbour_Sex2_11.mkv", fps=30)
    show videov_Betty_Neighbour_Sex2_11
    with fade
    betty "Мммм..."
    betty "Ох..."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    sound snd_zip
    imgd 32946
    w
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Loved_Up
    imgfl 32945
    betty "Я думаю, что эта проверка..."
    betty "Пройдет успешно... Оооо..."
    # Фред подходит к Бетти
    imgf 32947
    w
    # Лиам приподнимает Бетти за бедра, она прогибается в спине и Фреду открывается доступ к попе
    sound Jump1
    imgd 32948
    w
    sound chpok6
    img 32949 hpunch
    w
    # Фред пристраивает член к попе Бетти и вводит его немного
    # Бетти останавливается
    music stop
    sound plastinka1b
    img 32950 vpunch
    betty "АЙ!!! ЧТО ЭТО?!"
    betty "!!!"
    # Бетти возмущенно оглядывается
    music Pyro_Flow
    img 32951 hpunch
    betty "Фред! Что ты делаешь?!! Не смей!!!"
    betty "Быстро убери из меня ЭТО!!!"
    # Фред вводит член и спокойно говорит, улыбаясь
    music Groove2_85
    imgd 32949
    w
    sound hlup25
    img 32952 hpunch
    w
    imgd 32953
    fred "Миссис Робертс..."
    fred "Я как ответственный работник..."
    fred "Нахожу своей профессиональной обязанностью..."
    fred "Не допустить того, чтобы моя хозяйка осталась неудовлетворенной..."
    music Pyro_Flow
    img 32954
    betty "Нет!!! Не смей!!!"
    betty "Не трогай меня!!!"
    betty "Твоя хозяйка тебе приказывает!"
    # Фреду по фиг
    music Groove2_85
    imgd 32955
    fred "Миссис Робертс, сначала я выполню свои профессиональные обязанности."
    fred "А потом, с чувством выполненного профессионального долга, покину это помещение."
    fred "Уверен, Лиам не против того, чтобы я проявил свой профессионализм и помог ему..."
    # Лиам молча улыбается и делает несколько движений бедрами, двигаясь в Бетти
    # она плывет от этого
    imgf 32956
    w
    sound drkanje5
    imgd 32957
    w
    sound drkanje5
    imgd 32958
    w
    music Loved_Up2
    imgf 32959
    betty "Ооох..."
    betty "Ааах, перестань, Фред!"
    # уже менее уверенно говорит Фреду

    $ localSoundVolume = 1.0
    $ localSoundName = v_Betty_Neighbour_Fred_Sex1_1_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Fred_Sex1_1= Movie(play="video/v_Betty_Neighbour_Fred_Sex1_1.mkv", fps=30)
    show videov_Betty_Neighbour_Fred_Sex1_1
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")


    sound ahhh6
    imgd 32960
    betty "Фред, я приказываю тебе..."

#2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Fred_Sex1_2= Movie(play="video/v_Betty_Neighbour_Fred_Sex1_2.mkv", fps=30)
    show videov_Betty_Neighbour_Fred_Sex1_2
    with fade
    betty "Мммм..."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

#3
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Fred_Sex1_3= Movie(play="video/v_Betty_Neighbour_Fred_Sex1_3.mkv", fps=30)
    show videov_Betty_Neighbour_Fred_Sex1_3
    with fade
    betty "Иди... Оооох..."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    # Фред уже пялит ее
    imgd 32961
    betty "Нееет... Не надоооо..."
    betty "Я не собираюсь делать этогоооо..."

    imgf 32962
    liam "Все в порядке, Мэм..."
    liam "Вам понравится..."

    #4
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Fred_Sex1_4= Movie(play="video/v_Betty_Neighbour_Fred_Sex1_4.mkv", fps=30)
    show videov_Betty_Neighbour_Fred_Sex1_4
    with fade
    fred "Я ведь профессионал..."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    #1
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Fred_Sex1_5= Movie(play="video/v_Betty_Neighbour_Fred_Sex1_5.mkv", fps=30)
    show videov_Betty_Neighbour_Fred_Sex1_5
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    #2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Fred_Sex1_6= Movie(play="video/v_Betty_Neighbour_Fred_Sex1_6.mkv", fps=30)
    show videov_Betty_Neighbour_Fred_Sex1_6
    with fade
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 32963
    betty "Фред, не смей! Ооооо!!!"

    #5
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Fred_Sex1_7= Movie(play="video/v_Betty_Neighbour_Fred_Sex1_7.mkv", fps=30)
    show videov_Betty_Neighbour_Fred_Sex1_7
    with fade
    betty "ОООООО!!!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    #6
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Fred_Sex1_8= Movie(play="video/v_Betty_Neighbour_Fred_Sex1_8.mkv", fps=30)
    show videov_Betty_Neighbour_Fred_Sex1_8
    with fade
    betty "Я не разрешалаааааа..."
    betty "ААААА!!!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    #7
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Fred_Sex1_9= Movie(play="video/v_Betty_Neighbour_Fred_Sex1_9.mkv", fps=30)
    show videov_Betty_Neighbour_Fred_Sex1_9
    with fade
    betty "Я приказываю!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 32964
    fred "Мэм, мне его вынуть из вас?"

    #8
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Fred_Sex1_10= Movie(play="video/v_Betty_Neighbour_Fred_Sex1_10.mkv", fps=30)
    show videov_Betty_Neighbour_Fred_Sex1_10
    with fade
    betty "Что? Нет, не надо вынимать! АААААА!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    #9
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Fred_Sex1_11= Movie(play="video/v_Betty_Neighbour_Fred_Sex1_11.mkv", fps=30)
    show videov_Betty_Neighbour_Fred_Sex1_11
    with fade
    liam "О, Мэээм..."
    liam "Это чертовски охренительно, Мэээм!!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 32965
    w
    imgf 32966
    fred "Дааа, черт!"
    fred "Мммм..."

    #10
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Fred_Sex1_12= Movie(play="video/v_Betty_Neighbour_Fred_Sex1_12.mkv", fps=30)
    show videov_Betty_Neighbour_Fred_Sex1_12
    with fade
    betty "Ооооох!!!"
    betty "ОООООО!!!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    imgd 32967
    w
    imgf 32960
    betty "Я так долго не смогууу!!!"

    #11
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Fred_Sex1_13= Movie(play="video/v_Betty_Neighbour_Fred_Sex1_13.mkv", fps=30)
    show videov_Betty_Neighbour_Fred_Sex1_13
    with fade
    fred "Кончайте, Миссис Робертс!!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 32968
    liam "Да!"

    #12
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Fred_Sex1_14= Movie(play="video/v_Betty_Neighbour_Fred_Sex1_14.mkv", fps=30)
    show videov_Betty_Neighbour_Fred_Sex1_14
    with fade
    betty "Яяяаааа... Кончу сейчааааас!!!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")


    #13
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Betty_Neighbour_Fred_Sex1_15= Movie(play="video/v_Betty_Neighbour_Fred_Sex1_15.mkv", fps=30)
    show videov_Betty_Neighbour_Fred_Sex1_15
    with fade
    betty "Ааааах!!!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    fadeblack 1.5
    music Loved_Up2
    # Бетти кончает
    img 32959
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    sound woman_moan14
    betty "Ааааах!!!"
    betty "АААААХ!!!"
    betty "АААААААА!!!"
    menu:
        "Кончить внутрь Бетти.":
            # Фред и Лиам кончают внутрь Бетти
            $ monicaBettyLiamVisit3_cumzone1 = 1
            imgf 32970
            liam "Я тоже..."
            liam "Кончаааааю!!!"
            img 32974
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            w
            img 32973
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan18
            liam "ААА!"
            liam "АААААА!!"
            img 32975
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            w
            img 32971
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan3
            fred "МММММММ!!!"
            imgf 32969
            w
            sound hlup25
            imgd 32972
            w
            pass
        "Кончить на Бетти.":
            # Фред и Лиам кончают на киску и на попу Бетти
            $ monicaBettyLiamVisit3_cumzone1 = 2
            imgf 32970
            liam "Я тоже..."
            liam "Кончаааааю!!!"
            imgd 32974
            w
            sound man_moan18
            img 32973
            liam "ААА!"
            liam "АААААА!!"
            imgd 32975
            w
            sound man_moan3
            imgd 32971
            fred "МММММММ!!!"
            img 32976
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan3
            w
            img 32977
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan18
            w
            pass
    # затемнение, шуршание одежды
    # голая Бетти лежит на диване в гостиной у соседа в отключке
    # Фред и Лиам стоят уже одетые
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Groove2_85
    imgfl 32978
    w
    imgf 32979
    liam "А она горячая штучка..."
    fred "Да, горячая. Это точно."
    imgd 32980
    liam "А почему ты называешь ее хозяйкой?"
    liam "Раньше ведь была другая..."
    # если Моника закатила соседу иск
    if neighborOffendedSueBig == True:
        $ notif(_("Моника хотела закатить соседу иск на $ 100 000."))
        imgd 32981
        liam "Какая-то стерва, которая мне закатила огромный иск за царапину на заборе."
        #
    liam "Как ее там звали? Бакфетт что-ли?"
    # Фред усмехается
    imgf 32982
    fred "Да. Миссис Бакфетт."
    liam "А где она?"
    # если Моника закатила соседу иск
    if neighborOffendedSueBig == True:
        liam "Из-за нее у меня чуть не отняли мой дом!"
        #
    fred "О, Лиам."
    imgd 32983
    fred "Это очень интересная история..."
    fred "Как-нибудь я тебе расскажу ее..."
    # затемнение, спустя несколько минут
    # Бетти, Фред и Лиам стоят в гостиной соседа, Бетти уже в одежде
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Groove2_85
    imgfl 32984
    w
    imgf 32985
    betty "Фред! Лиам!"
    fred "Да, Миссис Робертс?"
    betty "Фред, ты все не так понял, Я не изменяю своему мужу!"
    imgd 32986
    fred "Ну разве это измена, Миссис Робертс?"
    fred "Вы просто немного отдыхаете от домашних забот..."
    fred "Вы настолько хорошая хозяйка, что у вас совсем нет времени на отдых."
    # Бетти надменно
    imgf 32987
    betty "Да, это так! Я хорошая хозяйка и порядочная женщина!"
    betty "И вообще, я пришла сюда, чтобы забрать мой утюг!"
    # она подходит к столу и тянет руку к утюгу
    # крупным планом показываем, как рука Фреда ложится на ее руку, не давая взять утюг
    imgd 32988
    sound highheels_short_walk
    w
    imgf 32989
    w
    sound Jump1
    img 32990 hpunch
    w
    music Hidden_Agenda
    img 32991
    fred "Миссис Робертс, я думаю, что вам нужно оставить это здесь..."
    # Бетти непонимающе на него смотрит
    betty "Зачем?"
    fred "Вашему соседу в любой момент может понадобится ваша помощь..."
    fred "Ведь он совсем не умеет гладить этим утюгом..."
    # Бетти косится на фреда, на соседа (они улыбаются), а потом смущенно опускает глаза, убирая руку от утюга
    imgf 32992
    betty "Я..."
    fred "Да, Мэм?"
    betty "Нет, ничего! Мне пора готовить обед для своего мужа!"
    imgd 32993
    w
    fadeblack
    sound highheels_run2
    pause 2.0
    # выбегает из гостиной
    return True


# после этого игра переключается на события с Моникой
