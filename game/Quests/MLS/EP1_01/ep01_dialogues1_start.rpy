#####inc - обозначение строк для инц патча
##->#####inc - обозначение строк, которые заменяются инц патчем

define bardi = Character(_("Игрок"), who_color=c_blue) # ГГ Bardi Jones
define bardi_t = Character(_("Игрок"), who_color=c_blue, what_color=c_gray, what_italic=True) # ГГ Bardi Jones thinking
define olivia = Character(_("Оливия"), who_color=c_orange) # соседка, старшая дочь Софи - Olivia Jones
define mark = Character(_("Марк"), who_color=c_gray) # парень Оливии Mark
define father = Character(_("Отец"), who_color=c_red) # отец Барди
define sophie = Character(_("Софи"), who_color=c_pink) # хозяйка дома Sophie Evans
##### define mother = Character(_("Мама"), who_color=c_pink) # мать Sophie Evans (sophie)
define girl1 = Character(_("Незнакомка"), who_color=c_blue) # girl1, перед стартом игры
define girl2 = Character(_("Незнакомка"), who_color=c_red) # girl2, перед стартом игры

define v_Mark_Sister_Older_Blowjob1_sound_name = "v_Monica_PunksGB_Blowjob1"
define v_Mark_Sister_Older_Blowjob1b_sound_name = "v_Monica_PunksGB_Blowjob1"
define v_Mark_Sister_Older_Kissing1_25_sound_name = "snd_longkiss1"
define v_Mark_Sister_Older_Licking1_25_sound_name = "v_Monica_Perry_Licking1"
define v_Mark_Sister_Older_Licking2_sound_name = "v_Monica_Perry_Licking1"
define v_Mark_Sister_Older_Sex1_25_sound_name = "v_Monica_PunksGangbang_Sex1"
define v_Mark_Sister_Older_Sex2_25_sound_name = "v_Monica_PunksGangbang_Sex1"
define v_Mark_Sister_Older_Sex3_sound_name = "v_Monica_PunksGangbang_Sex1"
define v_Mark_Sister_Older_Sex3b_sound_name = "v_Monica_PunksGangbang_Sex1"

# в начале игры обязательно прописать, что все герои достигли 18 лет
# по умолчанию мать Софи Эванс - это подруга детства отца Барди, которая согласилась принять Барди к себе
# дочери Софи не являются сестрами Барди, просто соседки
#####inc в инцест-патче задается вопрос, кем является Софи для Барди
#####inc варианты: мать или хозяйка дома
#####inc если в патче выбран вариант, что Софи - это мать, то автоматически дочерям Софи присваивается статус сестер Барди


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
    music Deeper_For_You
    music2 ocean_waves
    imgfl 910196
    w
    imgf 910197
    w
    imgd 910198
    w
    imgd 910199
    w
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
    $ mcname = t__("Барди")
    if renpy.android == True:
        call screen input_softkeyboard
        $ mcname = _return
    else:
        $ mcname = renpy.input(t__("Меня зовут... (enter для ввода)"), mcname)
    if mcname == False:
        $ mcname = t__("Барди")

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
    girl2 "Просто кликни на шезлонг и выбери [действие]."
    # при этом демонстрируются иконки при наведении курсора на шезлонг
    girl1 "Или ты можешь просто [смотреть], чтобы узнать что-то об этом предмете."
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
    imgd 910208
    girl1 "Посмотри сюда, [mcname]. Это Event List."
    # разворачиваем Event List
    girl1 "Здесь ты сможешь увидеть текущие задачи, а также получить подсказку по прохождению игры."
    girl1 "Чтобы получить подсказку по конкретному квесту, тебе просто нужно кликнуть на него в Event List."
    # сворачиваем Event List
    sound Jump2
    imgd 910209
    girl2 "Также тебе доступно быстрое перемещение по локациям."
    girl2 "Для этого тебе достаточно кликнуть на иконку нужной локации в меню быстрого перемещения."
    # девушка показывает пальцем в сторону иконки
    girl2 "Оно расположено в правом верхнем углу."
    # показываем (подсвечиваем) иконку телефона
    # в телефоне заблокированы иконки соц.сети и иконки галереи (они откроются позже), в сообщениях пока пусто
    sound vjuh3
    imgd 910210
    girl1 "А это твой смартфон."
    girl1 "В нем ты сможешь найти полезную информацию, а также обмениваться сообщениями и просматривать социальные сети."
    imgf 910211
    girl2 "Ты кое-что забыла расскать, Лили..."
    imgd 910212
    girl2 "[mcname], видишь, иконку камеры рядом с телефоном?"
    girl1 "Ах, да!"
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
    girl2 "Это твой RabbitRat-meter. Я называю его проще - RR-meter."
    girl2 "Эта шкала будет отображать твой путь в соответствии с твоими поступками."
    girl1 "Точно! Как я могла забыть?!"
    imgd 910210
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
    girl1 "Я уверена, Меган, что у него все получится."
    girl2 "Ну, кто знает..."
    girl2 "Возможно, в попытках достичь одной цели он приобретет что-то более ценное..."
    fadeblack 1.0
    music2 stop
    return

label ep01_dialogues1_start_1b:
    # темный коридор, в конце коридора через щель приоткрытой двери виден свет
    # взволнованное тяжелое дыхание, затем осторожные шаги и скрип пола
    # дверь с каждым шагом все ближе и ближе
    # рука (как будто видим свою руку) медленно поднимается и берется за ручку двери
    sound heavy_breathing_male2
    imgfl 910242
    sound2 woman_moan12
    bardi_t "Главное, не шуметь. Если они заметят меня - это будет конец."
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
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
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
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
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
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
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
    bardi_t "Ооох, смотрел бы вечно на это. Жаль, я не могу присоединиться..."
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
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
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

    # video
    # v_Mark_Sister_Older_Sex1_25
    img black_screen
    with diss
    pause 1.5
    scene black
    sound v_Mark_Sister_Older_Sex1_25
    image videov_Mark_Sister_Older_Sex1_25 = Movie(play="video/v_Mark_Sister_Older_Sex1_25.mkv", fps=25, loop=False)
    show videov_Mark_Sister_Older_Sex1_25
    $ renpy.pause(0.5, hard=True)
    pause 2.5
    wclean


    imgf 910266
    mark "Ооо да, детка!"
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
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str((0*1.166)) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Mark_Sister_Older_Sex2_25 = Movie(play="video/v_Mark_Sister_Older_Sex2_25.mkv", fps=25)
    show videov_Mark_Sister_Older_Sex2_25
    wclean
    mark "Ооо, детка, какая же ты красивая!"
    wclean
    mark "Ооох!.. Я готов трахаться с тобой сутки напролет!"
    olivia "Даааа!"
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
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
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
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str((0*1.166)) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Mark_Sister_Older_Sex3 = Movie(play="video/v_Mark_Sister_Older_Sex3.mkv", fps=30)
    show videov_Mark_Sister_Older_Sex3
    wclean
    olivia "Ооох, глубже, Марк!"
    wclean
    mark "Вот так тебе нравится?"
    olivia "О, да, Марк! О, как же кайфово!"
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
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str((0*1.166)) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Mark_Sister_Older_Sex3b = Movie(play="video/v_Mark_Sister_Older_Sex3b.mkv", fps=30)
    show videov_Mark_Sister_Older_Sex3b
    wclean
    olivia "О, Марк! Я скоро кончу!"
    wclean
    olivia "Не останавливайся, Марк, трахай меня! Да-да!"
    mark "Да, детка! Я хочу, чтобы ты кончила!"
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
    pause 4.0
    # затемнение, звук быстрых шагов по коридору, бег
    # потом все затихает и сразу резкая смена кадра на поезд
    return

label ep01_dialogues1_start_2:
    # звук поезда
    # в кадре окно поезда, за окном идет дождь (смотрим глазами Барди)
    # появляется и исчезает надпись на кадре: Некоторое время назад
    # потом поднимается рука (как будто видим свою руку), проводит пальцем по стеклу и снова опускается
    music2 train_ambience
    imgfl 910221
    w
    imgf 910222
    music Border_Blaster
    bardi_t "Это что, какой-то стремный сон?"
    imgd 910223
    bardi_t "Разговор с отцом... Этот поезд..."
    imgd 910224
    w
    sound window_hit
    img 910230 hpunch
    bardi_t "Если это и правда сон, то я хочу скорее проснуться."
    # кадры с поезда резко меняются на воспоминания Барди, звук поезда затихает
    # перед нами стоит мужчина в деловом костюме (его лицо не показываем - кадр от нижней части лица (видно только рот) и ниже)
    # на заднем фоне мужчины тачка на фоне улицы (или дороги, или деревьев)
    music2 stop
    imgf 910225
    father "Сын, пойми, так будет лучше для всех."
    father "Давний друг нашей семьи Софи обрадовалась твоему возвращению в родной город." ##->#####inc
    father "Она с радостью согласилась принять тебя в своей семье." ##->#####inc
    imgd 910226
    father "Тем более, что я уже оплатил аренду комнаты в их доме для тебя." ##->#####inc
    #####inc father "Твоя мать очень обрадовалась, что ты возвращаешься к ней."
    #####inc father "Уверен, ты быстро найдешь общий язык с ее мужем..."
    #####inc father "И подружишься со своими сестрами."
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
    imgd 910233
    bardi_t "Как будто и не было огромного мегаполиса, богатого дома и лучшего в стране колледжа..."
    bardi_t "Поверить не могу, что я возвращаюсь в эту дыру."
    bardi_t "Сколько прошло времени с того дня, когда я и отец уехали в большой город?"
    bardi_t "Мне кажется, целая жизнь..."
    sound window_hit
    img 910230 hpunch
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
    imgf 910221
    bardi_t "В этой жалкой дыре я надолго не задержусь!"
    # звук поезда стихает и кадр меняется на вокзал
    music2 stop

    # video
    # INTRO_Animation2_25
    img black_screen
    with diss
    pause 1.5
    scene black
    sound train
    image videoINTRO_Animation2_25 = Movie(play="video/INTRO_Animation2_25.mkv", fps=25, loop=False)
    show videoINTRO_Animation2_25
    $ renpy.pause(0.5, hard=True)
    pause 3.5
#    wclean

    # INTRO_Animation3_25
    img black_screen
    with diss
#    pause 1.5
    scene black
    sound train_ambience
    image videoINTRO_Animation3_25 = Movie(play="video/INTRO_Animation3_25.mkv", fps=25, loop=False)
    show videoINTRO_Animation3_25
    $ renpy.pause(0.5, hard=True)
    pause 2.5
    wclean

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
    sophie "С возвращением, милый!" ##->#####inc
    #####inc mother "С возвращением, сынок!"
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
