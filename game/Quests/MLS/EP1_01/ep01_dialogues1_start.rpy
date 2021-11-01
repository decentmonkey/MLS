define v_Mark_Sister_Older_Blowjob1_sound_name = "v_Mark_Sister_Older_Blowjob1"
define v_Mark_Sister_Older_Blowjob1b_sound_name = "v_Mark_Sister_Older_Blowjob1b"
define v_Mark_Sister_Older_Kissing1_25_sound_name = "v_Mark_Sister_Older_Kissing1_25"
define v_Mark_Sister_Older_Licking1_25_sound_name = "v_Mark_Sister_Older_Licking1_25"
define v_Mark_Sister_Older_Licking2_sound_name = "v_Mark_Sister_Older_Licking2"
define v_Mark_Sister_Older_Sex1_25_sound_name = "v_Mark_Sister_Older_Sex1_25"
define v_Mark_Sister_Older_Sex2_25_sound_name = "v_Mark_Sister_Older_Sex2_25"
define v_Mark_Sister_Older_Sex3_sound_name = "v_Mark_Sister_Older_Sex3"
define v_Mark_Sister_Older_Sex3b_sound_name = "v_Mark_Sister_Older_Sex3b"

define v_MC_Intro1_25_sound_name = "v_Mark_Sister_Older_Blowjob1"
define v_MC_Intro_Titjob1_25_sound_name = "v_Mark_Sister_Older_Licking2"
define v_MC_Intro_Sex1_sound_name = "v_Mark_Sister_Older_Sex1_25"
define v_MC_Intro_Sex2_25_sound_name = "v_Mark_Sister_Older_Sex1_25"
define v_MC_Intro_Sex2b_25_sound_name = "v_Mark_Sister_Older_Sex1_25"
define v_MC_Intro_Sex2b2_25_sound_name = "v_Mark_Sister_Older_Sex1_25"
define v_MC_Intro_Sex2c_25_sound_name = "v_Mark_Sister_Older_Sex1_25"
define v_MC_Intro_Sex3_25_sound_name = "v_Mark_Sister_Older_Sex1_25"

default intro_choice1 = False
#call ep01_dialogues1_start_1a() # пляж, показываем геймплей
#call ep01_dialogues1_start_1b() # подглядывание за Оливией и Марком
#call ep01_dialogues1_start_2() # поезд
#call ep01_dialogues1_start_3() # вокзал


label ep01_dialogues1_start_1a:
    # здесь показываем геймплей с помощью двух девушек (Хлоя и Эмили или тетя и училка по живописи или взять не из героев игры)
    # всю сцену смотрим глазами игрока
    # они лежат в бикини на шезлонгах, загорают, в руках коктейли
    # рядом с ними стоит один пустой шезлонг
    # girl1 смотрит в камеру и расплывается в улыбке
    fadeblack 2.0
#    music Deeper_For_You
    music Carefree_Ukulele
#    music Elle_avait_pas_les_yeux_noirs
    music2 ocean_waves
    imgfl 910196
    w
    imgf 910197
    w
#    imgd 910198
#    w
#    imgd 910199
#    w
    imgf 910200
    w
    sound Jump2
    img 910201 vpunch
    girl1 "Эй! Привет, приятель!"
    # girl2 смотрит сначала на подругу, потом в камеру
    imgd 910202
    girl2 "Лили, это твой знакомый?"
    girl1 "Впервые его вижу, Меган. Но он определенно мне нравится."
    imgf 910203
    girl2 "Хм, пожалуй, он ничего..."
    girl2 "Как тебя зовут, красавчик?"
    # здесь ввод имени главного героя [mcname] [mcsurname], по дефолту Барди Джонс (Bardi Jones)
    $ mcname = t__("Томас")
    if renpy.android == True:
        call screen input_softkeyboard
        $ mcname = _return
    else:
        $ mcname = renpy.input(t__("Меня зовут... (enter для ввода)"), mcname)
    if mcname == False:
        $ mcname = t__("Томас")

    $ bardi = Character((mcname), who_color=c_blue) # ГГ Bardi Jones
    $ bardi_t = Character((mcname), who_color=c_blue, what_color=c_blue, what_italic=True) # ГГ Bardi Jones thinking

    $ mcsurname = t__("Джонс")
    if renpy.android == True:
        call screen input_softkeyboard
        $ mcsurname = _return
    else:
        $ mcsurname = renpy.input(t__("Меня зовут... (enter для ввода)"), mcsurname)
    if mcsurname == False:
        $ mcsurname = t__("Джонс")
    imgd 910204
    girl2 "Привет, [mcname]!"
    girl1 "Привет."
    # girl1 указывает на свободный шезлонг
    imgd 910205
    girl1 "Составишь нам компанию?"
    girl2 "Просто кликни на любую из нас и выбери [действие]."
    # при этом демонстрируются иконки при наведении курсора на шезлонг
    girl1 "Или ты можешь просто [смотреть], чтобы узнать что-то об этом предмете."
    return

label ep01_dialogues1_start_1a2:
    music Story_of_One_Success_short
    #music Elle_avait_pas_les_yeux_noirs
    #music Carefree_Ukulele
    imgd 910206
    girl2 "Кстати, [смотреть] можно будет не только на предметы..."
    # при этом она подмигивает ему
    img 910207
    girl1 "Не забегай вперед, Меган. Давай по порядку."
    # показываем (подсвечиваем) иконку EventList и девушка указывает пальцем на нее
    #music Deeper_For_You
    sound2 Jump1
    img 910208
    show screen hud_screen(hud_presets[hud_preset_current])
    with diss
    w
    show screen intro_focus("/images/Other/intro/intro_focus1.png")
    with diss
    girl1 "Посмотри сюда, [mcname]. Это Event List."
    # разворачиваем Event List
    girl1 "Здесь ты сможешь увидеть текущие задачи, а также получить подсказку по прохождению игры."
    girl1 "Чтобы получить подсказку по конкретному квесту, тебе просто нужно кликнуть на него в Event List."
    # сворачиваем Event List
    hide screen intro_focus
    call miniMapHouseGenerate() from _rcall_miniMapHouseGenerate
    img 910209
    $ miniMapOpened = False
    show screen hud_screen(hud_presets[hud_preset_current])
    show screen hud_minimap(miniMapData)
    with fade
    w
    $ miniMapOpened = True
    show screen hud_minimap(miniMapData)
    show screen intro_focus("/images/Other/intro/intro_focus2.png")
    sound metal_slide
    with diss
    girl2 "Также тебе доступно быстрое перемещение по локациям."
    girl2 "Для этого тебе достаточно кликнуть на иконку нужной локации в меню быстрого перемещения."
    # девушка показывает пальцем в сторону иконки
    girl2 "Оно расположено в правом верхнем углу."
    # показываем (подсвечиваем) иконку телефона
    # в телефоне заблокированы иконки соц.сети и иконки галереи (они откроются позже), в сообщениях пока пусто
    $ miniMapOpened = False

    show screen hud_minimap(miniMapData)
    show screen intro_focus("/images/Other/intro/intro_focus2.png")
    sound metal_slide
#    img 910208
    with diss
    pause 1.0
    show screen intro_focus("/images/Other/intro/intro_focus3.png")
    with diss
    girl2 "Здесь ты можешь открыть карту города."
    return

label ep01_dialogues1_start_1ab3:
    hide screen action_menu_screen
    girl2 "Карта города доступна только [на улице] или в твоей комнате."
    girl2 "По мере истории, здесь будет много мест, которые можно посетить."
    call map_close() from _rcall_map_close
    sound open_map
    img 910208
    show screen hud_screen(hud_presets[hud_preset_current])
    show screen hud_minimap(miniMapData)
    with fade
    pause 1.0
    show screen intro_focus("/images/Other/intro/intro_focus4.png")
    with Dissolve(1.0)
    girl2 "Это [кнопка домой]."
    girl2 "С помощью нее, ты можешь сразу попасть к себе в комнату."
    girl1 "Если только доступна карта!"
    girl2 "Ну да."


    sound vjuh3
    img 910210
    show screen hud_screen(hud_presets[hud_preset_current])
    show screen hud_minimap(miniMapData)
    show screen intro_focus("/images/Other/intro/intro_focus5.png")
    with diss
    girl1 "А это твой смартфон."
    hide screen intro_focus
#    show screen iphone_x
    with diss
#    pause 0.5
    $ phone_menu_active = "main"
    sound metal_slide
    show screen phone(phone_menu_active)
    pause 0.5
    show screen intro_focus("/images/Other/intro/intro_focus8.png")
    with diss
    girl1 "В нем ты сможешь найти полезную информацию, а также обмениваться сообщениями и просматривать социальные сети."
    imgf 910211
    girl2 "Ты кое-что забыла расскать, Лили..."
    imgd 910212
    girl1 "Ах, да!"
#    girl2 "[mcname], видишь, иконку камеры рядом с телефоном?"
#    hide screen phone
    show screen phone_camera_capture_hud_screen_intro(False)
    show screen intro_focus("/images/Other/intro/intro_focus6.png")
    with diss
    girl1 "[mcname], видишь, иконку камеры сверху экрана?"
    show screen phone_camera_capture_hud_screen_intro(True)
    show screen intro_focus("/images/Other/intro/intro_focus6.png")
    with diss
    girl1 "При наведении мышки, она загорается."
    hide screen phone_camera_capture_hud_screen_intro
    hide screen intro_focus
    with diss
    $ phone_menu_active = "camera"
    $ phone_orientation = 1
    $ phone_camera_image = phone_camera_get_current_image()
    show screen phone_camera_screen2_intro(phone_camera_image)
    pause 1.0
    show screen intro_focus("/images/Other/intro/intro_focus7.png")
    with diss
    girl1 "В некоторых сценах, используя эту камеру, ты сможешь делать фото."
    # girl2 с хитрой улыбочкой
    #music Story_of_One_Success_short
    imgf 910206
    girl2 "Это будет незаметно для того персонажа, которого ты будешь фотографировать."
    girl2 "Фото ты сможешь просматривать в галерее, которая находится в твоем телефоне."
    imgd 910213
    girl1 "На этом вроде бы все, Меган?"
    girl2 "Нет, не все. Лили, ты, как обычно, все забываешь!"
    sound vjuh3
    img 910214
    girl2 "Есть один важный момент, [mcname]..."
    # подсвечиваем шкалу RR, девушка уазывает на нее рукой
    $ phone_orientation = 0
#    $ phone_menu_active = "main"
    sound metal_slide
#    show screen phone(phone_menu_active)
#    pause 1.5
#    sound phone_click
    $ phone_menu_active = "preferences_rrmeter"
    show screen phone(phone_menu_active)
    pause 0.7
    show screen intro_focus("/images/Other/intro/intro_focus8.png")
    with diss
    pause 0.5
    girl2 "Это твой RabbitRat-meter. Я называю его проще - RR-meter."
    girl2 "Он находится в Настройках твоего телефона."
    girl2 "Эта шкала будет отображать твой путь в соответствии с твоими поступками."
    imgd 910210
    girl1 "Точно! Как я могла забыть?!"
    girl1 "Это важно, так как твой уровень RR влияет на развитие сюжета..."
    girl1 "А также на доступность опеределенных действий и сцен."
    imgf 910213
    girl2 "Кем ты станешь в итоге, зависит от тебя, [mcname]."
    girl2 "Уверена, что ты сможешь стать коварным и умным Rat."
    girl1 "Нет, Меган. Ты ошибаешься. [mcname] - милый и добрый Rabbit."
    # girl2 смеется
    sound snd_woman_laugh4
    img 910215
    girl2 "Ха-ха! Конечно, нет! Что за глупости, Лили?!"
    girl2 "Чем хитрее он будет, тем круче."
    # girl1 возмущенно смотрит на подругу
    music stop
    sound plastinka1b
    img 910216 vpunch
    girl1 "Что?! Нет!"
    music Adventures_of_the_Deaf_Dreamer_short
    girl1 "Будет круче, если он станет Rabbit!"
    girl1 "Он не превратится в Rat!"
    # girl2 тоже возмущенно смотрит в ответ
    img 910217
    girl2 "Превратится! Он будет Rat!"
    ###

    girl1 "Нет! Rabbit!"
    girl2 "Rat!"
    girl1 "Rabbit!"
    # игрок примирительно поднимает две руки (продолжаем смотреть его глазами)
    music Story_of_One_Success_short
    sound2 Jump1
    img 910218 hpunch
    bardi "Девочки, тише-тише!"
    bardi "Все окей. Я уверен, что сам с этим разберусь."
    imgd 910219
    sound kiss1
    pause 1.0
    sound snd_woman_laugh4
    girl2 "Хм, а ты уверенный в себе..."
    girl2 "Мне это нравится."
    girl1 "Удачи тебе, [mcname]."
    # девушки откидываются обратно на свои шезлонги
    fadeblack 1.5
    music Deeper_For_You
    imgf 910200
    w
    imgd 910220
    girl2 "Что ж, посмотрим, Лили, получится ли у него достичь своей цели."
    girl2 "Думаю, что да... Во время учебы в колледже в городе он стал таким уверенным в себе, целеустремленным."
    girl2 "Он не может так быстро растерять все это."
    girl2 "Парню нужно совсем немного времени и он придет в себя."
    imgf 910389
    girl1 "Я уверена, Меган, что у него все получится."
    girl2 "Ну, кто знает... Возможно, в попытках достичь одной цели он приобретет что-то более ценное..."
    girl1 "Возможно..."
    girl1 "Например, откроет для себя новые удовольствия? Что это может быть? Как ты думаешь, Меган?"
    sound vjuh3
    imgd 910390
    girl2 "Хочешь пофантазировать, Лили? Ха-ха!"
    girl1 "Интересно, о чем он сейчас думает?"
    girl2 "Я бы предпочла что-то запретное..."
    imgd 910391
    sound snd_woman_laugh4
    girl2 "Обман, подглядывание, может быть шантаж..."
    girl2 "Хи-хи!"
    imgd 910392
    girl1 "А я бы предпочла что-нибудь светлое!"
    girl1 "Ему есть о чем вспомнить!"
    girl1 "Он может быть хорошим Rabbit!"
    #sound Jump2
    imgd 910393
    girl2 "Давай посмотрим?"
    girl1 "Давай!"
    ###
    label ep01_dialogues1_start_1ab3_loot1:
    $ interact_data = None
    show screen rat_rabbit_choice()
    $ interact_data = ui.interact()
    if interact_data != "rat" and interact_data != "rabbit":
        jump ep01_dialogues1_start_1ab3_loot1

    sound click1
    hide screen rat_rabbit_choice
    imgd 910393
    girl2 "Но чтобы ты там себе не представляла... Случится ли это на самом деле или так и останется твоими фантазиями - все зависит только от [mcname]..."
#    menu:
#        "Светлое.":
    $ intro_choice1 = interact_data
    if intro_choice1 == "rabbit":
        fadeblack 1.0
        music2 stop
        jump ep01_dialogues1_start_1b1
#        "Темное.":
    if intro_choice1 == "rat":
        fadeblack 1.0
        music2 stop
        jump ep01_dialogues1_start_1b
    return

label ep01_dialogues1_start_1a3:
    imgf 910198
    bardi "Хм, кролик?"
    return
label ep01_dialogues1_start_1a4:
    imgf 910199
    bardi "Хм, крыска?"
    return
label ep01_dialogues1_start_1a5:
    girl1 "Эй, мы здесь!"
    return

# сцена из прошлого
label ep01_dialogues1_start_1b1:
    fadeblack 1.5
    #music Step_By_Step
    music The_Heat
    # номер отеля, где проходила встреча в ФБ Линды и инвестора
    # смотрим глазами Барди
    # он полулежа валяется на кровати, в руке бутылка пива
    # у кровати стоит девушка и пьяно улыбается ему, флиртует
    imgfl 910321
    w
    imgf 910322
    w
    imgd 910320
    w
    imgf 910323
    bardi "Эй, детка, не заставляй меня долго ждать..."
#    bardi "[mcname] хочет увидеть, как ты раздеваешься для него."
    # он делает глоток, другой рукой демонстративно хватает себя за пах
    sound snd_drinking_water
    imgd 910324
    bardi "Начинай!"
    # она пьяно хихикает
    imgd 910325
    w
    imgd 910324
    w
    sound snd_drinking_water
    imgf 910326
    w
    imgd 910327
    girl3 "[mcname], тебе так не терпится?"
    bardi "Мне не терпится увидеть тебя под собой!"
    girl3 "Именно меня?"
    girl3 "Сегодня на вечеринке было много красивых девочек!"
    bardi "Ты знаешь, что ты самая классная!"
    imgd 910328
    sound snd_woman_laugh4
    girl3 "Знаю, хи-хи..."
    # она бросает на пол платье, остается в одном нижнем белье
    # встает в сексуальную позу и призывно улыбается Барди (возможно, обсматривание)
    sound vjuh3
    img 910329 hpunch
    w
    sound vjuh3
    img 910330 vpunch
    w
    imgf 910331
    girl3 "Так тебе больше нравится, красавчик?"
    # еще глоток пива
    sound snd_drinking_water
    imgd 910332
    w
    imgd 910333
    bardi "Снимай с себя все!"
    bardi "И иди сюда!"
    imgd 910334
    bardi "Я кое-что приготовил для тебя."
    # расстегивает ширинку и достает стояк
    # девушка жадно смотрит на его член
    sound Jump2
    img 910335 vpunch
    sound2 oooh4
    girl3 "Ох!.. Так это правда!.. Я думала, девчонки преувеличивали, когда обсуждали твой..." # указывает пальчиком на стояк Барди
    # Барди садится на кровать, ставит бутылку на пол и хватает девушку за руку, она хихикает
    sound vjuh3
    img 910336
#    girl3 "Хи-хи-хи..."
    bardi "Ну все, хватит болтать!" # дергает ее на себя
    ## возможно стоит добавить фразу типа "Спукайся на пол, сейчас дам тебе попробовать"
    # смена кадра
    # на той же кровати, они оба уже голые
    # она лежит на спине, а Барди нависает над ее лицом, член Барди у нее во рту (может быть та поза, в которой Моника, лежа на столе, делала минет Гарри в квартире у Эбби)
    # он толкается в ее рот
#    label test_video:
    fadeblack 1.0
    music Stylish_Hip_Hop_Rock
    imgfl 910337
    w
    imgf 910338
    w
    imgd 910339
    girl3 "Мммм..."
    sound drkanje5
    imgd 910340
    w
    sound drkanje5
    imgd 910339
    w
    sound drkanje5
    imgd 910340
    girl3 "Мпфхфмм..."
    imgf 910341
    w
    imgd 910339
    bardi "О, еее!.."
    sound chpok7
    imgd 910342
    bardi "А еще глубже сможешь, м?"
    imgd 910339
    w
    sound chpok6
    img 910343 hpunch
    bardi "Оооо..."
    imgf 910344
    w

    # video
    # v_MC_Intro1_25
    $ localSoundVolume = 1.0
    $ localSoundName = v_MC_Intro1_25_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(getMusicScenes(0.2), 0.5, channel="music")
    play music2 "<from " + str((0*1.166)) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_MC_Intro1_25 = Movie(play="video/v_MC_Intro1_25.mkv", fps=25)
    show videov_MC_Intro1_25
    wclean
    girl3 "Мпфхфмм..."
    bardi "Дааа!.. Ты супер, малышка!.."
    wclean
    bardi "Давай еще!.."
    girl3 "Мммм..."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")


    # выходит из ее рта, она смотрит на него и жадно облизывается
    sound chpok7
    imgd 910345
    w
    imgd 910346
    w
    # смена позы через затемнение
    ## немного титсджоб
    sound Jump1
    img 910347 hpunch
    w
    sound vjuh3
    img 910348 vpunch
    w
    imgf 910349
    w
    imgd 910350
    w
    sound drkanje5
    imgd 910351
    w
    sound drkanje5
    imgd 910350
    w
    sound drkanje5
    imgd 910351
    w

    # video
    # v_MC_Intro_Titjob1_25
    $ localSoundVolume = 1.0
    $ localSoundName = v_MC_Intro_Titjob1_25_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(getMusicScenes(0.2), 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_MC_Intro_Titjob1_25= Movie(play="video/v_MC_Intro_Titjob1_25.mkv")
    show videov_MC_Intro_Titjob1_25
    with fade
    bardi "Оооо..."
    wclean
    bardi "Ооо да, детка!"
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 910352
    w
    # Барди на спине, она страстно прыгает на нем
    fadeblack 0.5
    music Stylish_Hip_Hop_Rock
    imgfl 910353
    w
    imgf 910354
    w

    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(getMusicScenes(0.2), 0.5, channel="music")
    # video
    # v_MC_Intro_Sex2c_25
    $ localSoundVolume = 1.0
    $ localSoundName = v_MC_Intro_Sex2c_25_sound_name
    img black_screen
    with diss
    pause 1.5
    scene black
    sound v_MC_Intro_Sex2c_25
    image videov_MC_Intro_Sex2c_25 = Movie(play="video/v_MC_Intro_Sex2c_25.mkv", fps=25, loop=False, image="/images/Slides/v_MC_Intro_Sex2c_2_end.jpg")
    show videov_MC_Intro_Sex2c_25
    $ renpy.pause(0.5, hard=True)
    pause 6.5
    img v_MC_Intro_Sex2c_2_end
    w
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    bardi "Мммм..."

    imgf 910355
    w
    sound drkanje5
    imgd 910356
    w

    sound2 woman_moan7
    imgd 910357
    girl3 "Ооо! Вот это кайф!!!"
    imgd 910358
    girl3 "Твой член, какой же он охрененный!"
    girl3 "Он заполняет меня всю! Ооох!"
    imgf 910359
    w
    sound drkanje5
    imgd 910360
    w
    sound drkanje5
    imgd 910359
    w
    sound drkanje5
    imgd 910360
    w

    # video
    # v_MC_Intro_Sex1
    $ localSoundVolume = 1.0
    $ localSoundName = v_MC_Intro_Sex1_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(getMusicScenes(0.2), 0.5, channel="music")
    play music2 "<from " + str((0*1.166)) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_MC_Intro_Sex1 = Movie(play="video/v_MC_Intro_Sex1.mkv", fps=30)
    show videov_MC_Intro_Sex1
    wclean
    bardi "Дааа, детка..."
    wclean
    girl3 "Хочу тебя, [mcname]! Еще-еще!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 910361
    w
    sound ahhh11
    imgd 910362
    w
    imgd 910363
    w
    sound vjuh3
    img 910364 hpunch
    w
    imgd 910365
    bardi "Мммм..."
    sound drkanje5
    imgd 910366
    w
    sound drkanje5
    imgd 910365
    w
    sound drkanje5
    imgd 910366
    w
    sound drkanje5
    imgd 910365
    w
    sound drkanje5
    imgd 910366
    w
    sound Jump1
    img 910367 hpunch
    w

    # video
    # v_MC_Intro_Sex3_25
    $ localSoundVolume = 1.0
    $ localSoundName = v_MC_Intro_Sex3_25_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(getMusicScenes(0.2), 0.5, channel="music")
    play music2 "<from " + str((0*1.166)) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_MC_Intro_Sex3_25 = Movie(play="video/v_MC_Intro_Sex3_25.mkv", fps=25)
    show videov_MC_Intro_Sex3_25
    wclean
    girl3 "Обожаю твой член! Дааа!!!"
    wclean
    girl3 "Ооо! Я скоро кончу, [mcname]!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")


    # ставит на четвереньки, держа за волосы
    # и начинает вколачиваться в нее, шлепает по попе
    # она кайфует
    fadeblack 0.5
    music Stylish_Hip_Hop_Rock
    imgf 910368
    w
    imgd 910369
    w
    sound drkanje5
    imgd 910370
    w

    # video
    # v_MC_Intro_Sex2b_25
    $ localSoundVolume = 1.0
    $ localSoundName = v_MC_Intro_Sex2b_25_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(getMusicScenes(0.2), 0.5, channel="music")
    play music2 "<from " + str((0*1.166)) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_MC_Intro_Sex2b_25 = Movie(play="video/v_MC_Intro_Sex2b_25.mkv", fps=25)
    show videov_MC_Intro_Sex2b_25
    wclean
    girl3 "Сделай это! Быстрее!"
    wclean
    bardi "Дааа, детка..."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 910371
    w
    sound chpok6
    sound2 woman_moan15
    img 910372 hpunch
    girl3 "Да! О, да!"
    imgd 910373
    w

    # video
    # v_MC_Intro_Sex2_25
    $ localSoundVolume = 1.0
    $ localSoundName = v_MC_Intro_Sex2_25_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(getMusicScenes(0.2), 0.5, channel="music")
    play music2 "<from " + str((0*1.166)) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_MC_Intro_Sex2_25 = Movie(play="video/v_MC_Intro_Sex2_25.mkv", fps=25)
    show videov_MC_Intro_Sex2_25
    wclean
    girl3 "Вытрахай всю меня, [mcname]!"
    bardi "Дааа!!!"
    wclean
    girl3 "Еще! Оооо!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")


    imgf 910374
    w
    sound drkanje5
    imgd 910375
    w
    sound drkanje5
    imgd 910374
    w
    sound drkanje5
    imgd 910375
    w
    sound drkanje5
    imgd 910374
    w
    sound drkanje5
    imgd 910375
    w

    # video
    # v_MC_Intro_Sex2b2_25
    $ localSoundVolume = 1.0
    $ localSoundName = v_MC_Intro_Sex2b2_25_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(getMusicScenes(0.2), 0.5, channel="music")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_MC_Intro_Sex2b2_25= Movie(play="video/v_MC_Intro_Sex2b2_25.mkv")
    show videov_MC_Intro_Sex2b2_25
    with fade
    girl3 "Оооо!!!"
    wclean
    bardi "Дааа!!!"
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 910376
    girl3 "Еще! Оооо!"
    sound ahhh11
    imgd 910377
    girl3 "Оооо!!!"
    # девушка кончает
    img 910376
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    girl3 "АААА!!!"
    img 910377
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    sound woman_moan14
    girl3 "АААААААА!!!"
    bardi "О, дааа!!!"
    menu:
        "Кончить в нее.":
            # Барди бурно кончает в нее
            imgd 910374
            w
            sound drkanje5
            imgd 910375
            bardi "Дааа!!!"
            img 910378
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            bardi "Оооо!!!"
            img 910379
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            w
            img 910380
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man moan8
            bardi "О, какой кайф..."
            imgd 910382
            w
            sound chpok5
            imgd 910383
            w
            # она резко распахивает глаза
            sound ahhh11
            imgf 910373
            w
            sound Jump2
            img 910381 hpunch
            girl3 "Эй, [mcname], какого хрена ты не вытащил?!"
            pass
        "Кончить на нее.":
            # Барди бурно кончает на девушку
            imgd 910374
            w
            sound drkanje5
            imgd 910375
            w
            sound chpok7
            imgd 910371
            w
            img 910384
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            bardi "Дааа!!!"
            sound2 chpok5
            imgd 910385
            w
            img 910386
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man moan8
            bardi "Оооо!!!"
            sound2 chpok5
            imgd 910387
            bardi "О, какой кайф..."
            # она смотрит ему в глаза, вся в сперме
            # подмигивает ему и улыбается
            sound ahhh11
            imgd 910388
            girl3 "О, дааа!.."
            girl3 "Ты лучший, красавчик!.."
            pass
    # затемнение
    call rrmeter(5, "intro1")
    pause 4.0
    return

# сцена из будущего
label ep01_dialogues1_start_1b:
#    scene black_screen
#    with Dissolve(1)
#    music stop
#    call textonblack(t_("НЕДАЛЕКОЕ БУДУЩЕЕ"))
# from _rcall_textonblack
#    scene black_screen
#    with Dissolve(1)
    fadeblack 1.5
    # темный коридор, в конце коридора через щель приоткрытой двери виден свет
    # взволнованное тяжелое дыхание, затем осторожные шаги и скрип пола
    # дверь с каждым шагом все ближе и ближе
    # рука (как будто видим свою руку) медленно поднимается и берется за ручку двери
    sound floor_creak
    imgfl 910242
    sound heavy_breathing_male2
    sound2 woman_moan12
    bardi_t "Главное, не шуметь. Если они заметят меня - это будет конец."
    sound floor_creak
    imgf 910304
    sound sneaks_2
    bardi_t "Фак! У меня дрожат колени, но я не могу остановиться."
    sound2 door_creaky
    imgd 910305
    bardi_t "Я не могу ничего с собой поделать. Какое-то наваждение..."
    sound woman_moan8a
    imgd 910306
    w
    # скрип двери, следом звуки секса - женские стоны
    # кадр на комнату
    # на кровати Оливия и Марк занимаются страстным сексом, они не видят Барди
    # анимация их секса
    ## дописать начало для blowjob

    music Stylish_Hip_Hop_Rock
    imgf 910243
    w
    imgd 910244
    mark "Ооо, Оливия, я обожаю, когда ты делаешь это..."
    olivia "А я обожаю сосать твой член, Марк."
    ## мысли Барди
    imgf 910245
    bardi_t "О, еее... Какой отличный вид..."
    bardi_t "Уверен, тот день, когда трахать ее буду Я, наступит совсем скоро..."
    imgd 910246
    w
    imgf 910247
    w
    imgd 910248
    w
    sound lick3
    imgd 910249
    w
    sound lick3
    imgd 910250
    w
    sound lick3
    imgd 910249
    w

    # video
    # v_Mark_Sister_Older_Licking1_25
    $ localSoundVolume = 1.0
    $ localSoundName = v_Mark_Sister_Older_Licking1_25_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(getMusicScenes(0.2), 0.5, channel="music")
    play music2 "<from " + str((0*1.166)) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Mark_Sister_Older_Licking1_25 = Movie(play="video/v_Mark_Sister_Older_Licking1_25.mkv", fps=25)
    show videov_Mark_Sister_Older_Licking1_25
    wclean
    mark "Оооо, да!.."
    mark "Еще, еще!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")


    imgf 910251
    w
    sound lick3
    imgd 910252
    w
    sound lick3
    imgd 910251
    w
    sound lick3
    imgd 910252
    w
    sound lick3
    imgd 910253
    w
    sound chpok9
    imgd 910254
    w
    sound chpok8
    img 910255 vpunch
    w
    imgf 910256
    w
    sound chpok7
    img 910257 hpunch
    sound2 man_moan1
    w

    # video
    # v_Mark_Sister_Older_Blowjob1
    $ localSoundVolume = 1.0
    $ localSoundName = v_Mark_Sister_Older_Blowjob1_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(getMusicScenes(0.2), 0.5, channel="music")
    play music2 "<from " + str((0*1.166)) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Mark_Sister_Older_Blowjob1 = Movie(play="video/v_Mark_Sister_Older_Blowjob1.mkv", fps=30)
    show videov_Mark_Sister_Older_Blowjob1
    wclean
    mark "Оооу, как же круто!"
    wclean
    olivia "Мммм..."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    # 2
    # v_Mark_Sister_Older_Blowjob1b
    $ localSoundVolume = 1.0
    $ localSoundName = v_Mark_Sister_Older_Blowjob1b_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(getMusicScenes(0.2), 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Mark_Sister_Older_Blowjob1b= Movie(play="video/v_Mark_Sister_Older_Blowjob1b.mkv")
    show videov_Mark_Sister_Older_Blowjob1b
    with fade
    mark "Да, Оливия... Возьми его еще глубже!.."
    wclean
    olivia "Мммм..."
    mark "Оооох!.."
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 910258
    mark "Ооо, детка... Охренеть как круто!"
    olivia "Сейчас мы с тобой сделаем кое-что покруче, красавчик."
    imgf 910259
    w
    ## мысли Барди
    imgd 910273
    bardi_t "Ооох, черт!.. Жаль, я не могу оказаться на месте ее парня..."
    bardi_t "Пока что..."
    imgf 910259
    w
    sound vjuh3
    img 910260
    w
    imgd 910261
    music2 audio_longkiss1
    w
    imgd 910262
    w
    imgd 910263
    w
    imgd 910264
    music2 stop

    # video
    # v_Mark_Sister_Older_Kissing1_25
    $ localSoundVolume = 1.0
    $ localSoundName = v_Mark_Sister_Older_Kissing1_25_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(getMusicScenes(0.2), 0.5, channel="music")
    play music2 "<from " + str((0*1.166)) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Mark_Sister_Older_Kissing1_25 = Movie(play="video/v_Mark_Sister_Older_Kissing1_25.mkv", fps=25)
    show videov_Mark_Sister_Older_Kissing1_25
    wclean
    olivia "Мммм..."
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")


    imgf 910265
    w

    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(getMusicScenes(0.2), 0.5, channel="music")
    # video
    # v_Mark_Sister_Older_Sex1_25
    $ localSoundVolume = 1.0
    $ localSoundName = v_Mark_Sister_Older_Sex1_25_sound_name
    img black_screen
    with diss
    pause 1.5
    scene black
    sound v_Mark_Sister_Older_Sex1_25
    image videov_Mark_Sister_Older_Sex1_25 = Movie(play="video/v_Mark_Sister_Older_Sex1_25.mkv", fps=25, loop=False, image="/images/Slides/v_Mark_Sister_Older_Sex1_1_end.jpg")
    show videov_Mark_Sister_Older_Sex1_25
    $ renpy.pause(0.5, hard=True)
    pause 5.5
    img v_Mark_Sister_Older_Sex1_1_end
    w
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    mark "Ооо да, детка!"

    imgf 910266
    w
    sound2 ahhh6
    imgd 910267
    olivia "Ааааа!"

    # video
    # v_Mark_Sister_Older_Sex2_25
    $ localSoundVolume = 1.0
    $ localSoundName = v_Mark_Sister_Older_Sex2_25_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(getMusicScenes(0.2), 0.5, channel="music")
    play music2 "<from " + str((0*1.166)) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Mark_Sister_Older_Sex2_25 = Movie(play="video/v_Mark_Sister_Older_Sex2_25.mkv", fps=25)
    show videov_Mark_Sister_Older_Sex2_25
    wclean
    mark "Ооо, детка, какая же ты красивая!"
    wclean
    mark "Ооох!.. Я готов трахаться с тобой сутки напролет!"
    olivia "Даааа!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 910268
    w
    imgd 910269
    w
    imgd 910270
    w
    sound drkanje5
    imgd 910271
    w
    sound drkanje5
    imgd 910270
    w
    sound drkanje5
    imgd 910271
    w
    sound drkanje5
    imgd 910270
    w
    sound drkanje5
    imgd 910271
    w
    ## мысли Барди
    sound2 ahhh7
    imgf 910272
    olivia "Оооо, Мааарк... Еще немного и я так кончуууу!.."
    ## фраза Марка про смену позы
    imgd 910274
    mark "Подожди, не торопись, Оливия!.. Меня тоже так надолго не хватит."
    mark "Встань на колени на кровати и раздвинь ножки. Хочу приласкать твою киску."
    olivia "О, мне нравится эта идея. Моей киске уже не терпится!.."
    ## дописать для куни
    imgf 910275
    sound ahhh10
    olivia "Давай скорее, Марк!"
    olivia "Проведи своим языком по моей киске! Давай же!"
    imgd 910276
    w

    # video
    # v_Mark_Sister_Older_Licking2
    $ localSoundVolume = 1.0
    $ localSoundName = v_Mark_Sister_Older_Licking2_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(getMusicScenes(0.2), 0.5, channel="music")
    play music2 "<from " + str((0*1.166)) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Mark_Sister_Older_Licking2 = Movie(play="video/v_Mark_Sister_Older_Licking2.mkv", fps=30)
    show videov_Mark_Sister_Older_Licking2
    wclean
    olivia "Оооох!.. Еще, Марк!"
    wclean
    olivia "Аааах..."
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgd 910277
    w
    sound ahhh11
    imgd 910278
    w
    imgf 910279
    w
    sound lick3
    imgd 910280
    w
    sound lick3
    imgd 910279
    w
    sound lick3
    imgd 910280
    w
    sound lick3
    imgd 910279
    w
    sound lick3
    imgd 910280
    w
    imgd 910281
    sound ahhh12
    w
    ## таже поза с пальцем (может какой-то текст)
    imgd 910282
    w
    imgf 910283
    mark "Мммм... Какая сладкая киска..."
    imgd 910284
    w
    sound drkanje5
    imgd 910285
    mark "Такая узкая, такая горячая..."
    sound drkanje5
    imgd 910284
    w
    sound drkanje5
    imgd 910285
    w
    imgf 910286
    mark "Сейчас твоей киске мало не покажется..."
    mark "Сейчас Марк тебя оттрахает, детка."
    olivia "Да, Марк! Давай! Я так хочу тебя!"
    imgd 910287
    w
    sound chpok6
    img 910288 hpunch
    sound2 ahhh6
    olivia "О, Мааарк!"
    olivia "Я обожаю, когда ты трахаешь меня!"
    imgd 910289
    sound ahhh7
    w

    # video
    # v_Mark_Sister_Older_Sex3
    $ localSoundVolume = 1.0
    $ localSoundName = v_Mark_Sister_Older_Sex3_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(getMusicScenes(0.2), 0.5, channel="music")
    play music2 "<from " + str((0*1.166)) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Mark_Sister_Older_Sex3 = Movie(play="video/v_Mark_Sister_Older_Sex3.mkv", fps=30)
    show videov_Mark_Sister_Older_Sex3
    wclean
    olivia "Ооох, глубже, Марк!"
    wclean
    mark "Вот так тебе нравится?"
    olivia "О, да, Марк! О, как же кайфово!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")


    imgf 910290
    mark "Ооо, да!"
    sound drkanje5
    imgd 910291 vpunch
    sound2 ahhh8
    olivia "Я хочу чувствать твой огромный член! Полностью!"
    mark "Да, Оливия, да!"
    imgf 910293
    mark "Обожаю трахать тебя, детка!.."
    olivia "Шлепни меня, Марк!"
    # он шлепает ее по ягодице
    imgd 910294
    w
    sound snd_slap1
    img 910295 hpunch
    olivia "Оооо, еще сильнее!"
    img 910296
    mark "Да, еще! Какая же ты дикая, детка!"
    # еще шлепок по ягодице
    imgd 910294
    w
    sound snd_slap1
    img 910295 hpunch
    w
    img 910296
    olivia "Ооох, как круто!"
    # смена кадра - взгляд из глаз Барди, его рука лезет в штаны
    imgf 910292
    w
    imgd 910307
    bardi_t "Какая же она страстная..."
    imgd 910308
    bardi_t "И такая красивая."
    sound Jump2
    img 910309 vpunch
    bardi_t "Ох, черт! Как же она меня заводит!.."
    # его рука начинает двигаться по члену вверх-вниз
    sound drkanje5
    imgd 910310
    bardi_t "Вот бы не Марк, а я сейчас был с ней."
    sound drkanje5
    imgd 910309
    w
    sound drkanje5
    imgd 910310
    bardi_t "И она извивалась бы подо мной и стонала."
    sound drkanje5
    imgd 910309
    w
    sound drkanje5
    imgd 910310
    bardi_t "И просила бы трахать ее снова и снова..."
#    bardi_t "..."
    # смена кадра на парочку в постели
    imgf 910292
    olivia "Еще! Отшлепай меня, Марк! Давай же!"
    # шлепок, еще шлепок, она стонет
    imgd 910294
    w
    sound snd_slap1
    img 910295 hpunch
    w
    img 910296
    olivia "Сильнее! Оооо!"
    # Оливия откидывает голову или поворачивает ее в сторону двери, глаза закрыты, она стонет
    imgd 910292
    sound ahhh10
    w

    # video
    # v_Mark_Sister_Older_Sex3b
    $ localSoundVolume = 1.0
    $ localSoundName = v_Mark_Sister_Older_Sex3b_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(getMusicScenes(0.2), 0.5, channel="music")
    play music2 "<from " + str((0*1.166)) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Mark_Sister_Older_Sex3b = Movie(play="video/v_Mark_Sister_Older_Sex3b.mkv", fps=30)
    show videov_Mark_Sister_Older_Sex3b
    wclean
    olivia "О, Марк! Я скоро кончу!"
    wclean
    olivia "Не останавливайся, Марк, трахай меня! Да-да!"
    mark "Да, детка! Я хочу, чтобы ты кончила!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")


    imgf 910297
    olivia "Ооо! Еще, Марк! Еще!"
    olivia "Трахай меня!"
    # Марк в это время продолжает ее жарить
    imgd 910298
    w
    imgf 910299
    olivia "Заполни меня всю, Марк!"
    # тут Оливия резко распахивает глаза и смотрит прямо в камеру (т.е. на Барди)
    # немая пауза, на ее лице испуг
    imgd 910297
    w
    music stop
    sound plastinka1b
    img 910300 vpunch
    olivia "?!"
    bardi_t "!!!"
    # испуг меняется на удивление
    music Fly_With_Me_short
    img 910301
    olivia "?!?!"
    bardi_t "Она меня спалила!"
    # затем она злобно начинает орать на Барди
    img 910302 hpunch
    olivia "Какого хрена ты здесь делаешь?!"
    olivia "Кретин!"
    bardi_t "!!!"
    imgd 910303
    olivia "Пошел вон отсюда, мерзкий ушлепок! Лузер!"
    bardi_t "ФАК!!!"
    fadeblack
    sound run_stairs_floor
    bardi_t "Черт! Какого хрена?!"
    bardi_t "Я должен был быть на его месте!"
    call rrmeter(-5, "intro1")
    pause 4.0
    # затемнение, звук быстрых шагов по коридору, бег
    # потом все затихает и сразу резкая смена кадра на поезд
    return

label ep01_dialogues1_start_2:
    # звук поезда
    # в кадре окно поезда, за окном идет дождь (смотрим глазами Барди)
    # появляется и исчезает надпись на кадре: Некоторое время назад
    # потом поднимается рука (как будто видим свою руку), проводит пальцем по стеклу и снова опускается
    fadeblack 1.5
#    scene black_screen
#    with Dissolve(1)
#    music stop
#    call textonblack(t_("НАСТОЯЩЕЕ ВРЕМЯ"))
# from _rcall_textonblack_1
#    scene black_screen
#    with Dissolve(1)
    music2 train_ambience
#    img 910221
    scene black_screen
    show screen train2()
    show screen train_image("images/Other/train/img_910221_sprite.png")
    with fadelong
    w
#    imgf 910222
    scene black_screen
    show screen train1()
    show screen train_image("images/Other/train/img_910222_sprite.png")
    with fade
    music Border_Blaster
    bardi_t "Это что, какой-то стремный сон?"
#    imgd 910223
    show screen train_image("images/Other/train/img_910223_sprite.png")
    with diss
    bardi_t "Разговор с отцом... Этот поезд..."
#    imgd 910224
    show screen train_image("images/Other/train/img_910224_sprite.png")
    with diss
    w
    sound window_hit
#    img 910230 hpunch
    show screen train_image("images/Other/train/img_910230_sprite.png")
    with hpunch
    bardi_t "Если это и правда сон, то я хочу скорее проснуться."
    # кадры с поезда резко меняются на воспоминания Барди, звук поезда затихает
    # перед нами стоит мужчина в деловом костюме (его лицо не показываем - кадр от нижней части лица (видно только рот) и ниже)
    # на заднем фоне мужчины тачка на фоне улицы (или дороги, или деревьев)
    music2 stop
    imgf 910225
    father "Сын, пойми, так будет лучше для всех."
    father "Давний друг нашей семьи Софи обрадовалась твоему возвращению в родной город."
    father "Она с радостью согласилась принять тебя в своей семье."
    imgd 910226
    father "Тем более, что я уже оплатил аренду комнаты в их доме для тебя."
    img 910227
    bardi "Но, отец!!"
    bardi "Я не хочу возвращаться! Я хочу остаться здесь, с тобой!.."
    # недовольный, жесткий изгиб губ отца
    imgd 910228
    w
    img 910241
    father "Я уже принял решение, сын."
    # протягивает ему билет
    imgd 910229
    father "Поезд завтра в 2 часа дня. Это твой билет."
    # звук поезда
    # образ отца тает и картинка сменяется снова поездом
    # кадр на руку Барди (как будто видим свою руку), лежащую на его колене или рюкзаке - рука сжимается в кулак
    music2 train_ambience
    imgf 910231
    w
    music Adventures_of_the_Deaf_Dreamer_short
    img 910232 vpunch
    bardi_t "Никогда его не прощу!"
    bardi_t "Как он мог променять меня, своего сына (!), на какую-то лживую девку?!"
    bardi_t "Это же очевидно, что ей нужен не он! Ее интересуют только его деньги!"
    bardi_t "А он..."
    bardi_t "Он просто взял и выбросил меня из своей жизни!"
    # кадр на дождь за окном
#    imgd 910233
    scene black_screen
    show screen train3()
    show screen train_image("images/Other/train/img_910233_sprite.png")
    with diss

    bardi_t "Как будто и не было огромного мегаполиса, богатого дома и лучшего в стране колледжа..."
    bardi_t "Поверить не могу, что я возвращаюсь в эту дыру."
    bardi_t "Сколько прошло времени с того дня, когда я и отец уехали в большой город?"
    bardi_t "Мне кажется, целая жизнь..."
    sound window_hit
#    img 910230 hpunch
    show screen train1()
    show screen train_image("images/Other/train/img_910230_sprite.png")
    with hpunch
    bardi_t "..."
    bardi_t "Еще полчаса и я окажусь в этой чертовой деревне, откуда так хотел уехать и не возвращаться никогда."
    bardi_t "Меня затянет в эту серую трясину, как в болото."
    # рука на колене снова сжимается в кулак
    imgd 910231
    w
    imgd 910232
    bardi_t "Нет-нет! Я не допущу этого!"
    # кадр на окно поезда, за которым идет дождь
    music Border_Blaster
#    imgf 910221
    scene black
    show screen train2()
    show screen train_image("images/Other/train/img_910221_sprite.png")
    with fade
    bardi_t "В этой жалкой дыре я надолго не задержусь!"
    # звук поезда стихает и кадр меняется на вокзал
    music2 stop

    #4 sec + 14 sec
    # video
    # INTRO_Animation3_25
    img black_screen
    with diss
    pause 1.5
    scene black
    sound train
    image videoINTRO_Animation3_25 = Movie(play="video/INTRO_Animation3_25.mkv", fps=25, loop=False)
    show videoINTRO_Animation3_25
    $ renpy.pause(0.5, hard=True)
    pause 3.5

    # INTRO_Animation3_25
#    img black_screen
#    with diss
#    pause 1.5
#    scene black
    sound train2
    image videoINTRO_Animation2_25 = Movie(play="video/INTRO_Animation2_25.mkv", fps=25, loop=False, image="/images/Slides/INTRO_Animation2_end.jpg")
    show videoINTRO_Animation2_25
    with fade
    $ renpy.pause(0.5, hard=True)
    pause 13.5
    pause 1.0
    scene black
    with fadelong
#    pause 2.0
#    wclean
    return

label ep01_dialogues1_start_3:
    # вокзал
    # звуки жд вокзала, шум толпы
    # Барди стоит у перрона рядом с вагоном, откуда только что сошел
    # показываем Барди либо издали со спины, либо снова кадры с его глаз
    # он оглядывается
    music Border_Blaster
    music2 train_station
    imgfl 910234
    sound train
    bardi_t "Ничего не изменилось с того дня, когда я уезжал отсюда."
    imgf 910235
    bardi_t "Уезжал навсегда."
    bardi_t "Не думал, что так скоро вернусь сюда..."
    # далее кадры глазами Барди
    # к нему внезапно подбегает Софи с радостной улыбкой и раскрывает свои объятия
    music stop
    sound plastinka1b
    img 910236 hpunch
    w
    music Write_Your_Story
    imgf 910237
    w
    imgd 910238
    sophie "О, Боже! Как же я рада!"
    sophie "С возвращением, милый!"
    sound Jump2
    img 910239
    w
    sound vjuh3
    img 910240 vpunch
    w
    music2 stop
    # обнимает его
    # смена кадра с вокзала на кадр пустой комнаты Барди
    return
