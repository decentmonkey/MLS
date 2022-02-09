define mr_wright = Character(t_("Мистер Райт"), who_color=c_orange) # друг Генри, владелец велопроката (Wright)

default mlsBardiDay4BikeRental1 = 0 # Барди встретился с Райтом на пляже
default mlsBardiDay4BikeRental2 = 0 # Барди согласился работать в велопрокате

#call ep03_dialogues4_bike_rental_1() # мысли Барди, когда вышел из колледжа
#call ep03_dialogues4_bike_rental_2() # клик на пляж, встреча с Райтом
#call ep03_dialogues4_bike_rental_2a() # смс на телефон после разговора с Райтом
#call ep03_dialogues4_bike_rental_3() # клик на пляж на след. день, знакомство с велопрокатом

#### 1-й день

# мысли Барди, когда вышел из колледжа
label ep03_dialogues4_bike_rental_1:
    ## не рендерить!!
    bardi_t "Софи сказала, что мистер Райт на пляже." ##->#####inc
    #####inc bardi "Мама сказала, что мистер Райт будет на пляже."
    bardi_t "Что же, отличная погода для прогулки..."
    bardi_t "Надеюсь, переговоры с этим Райтом пройдут успешно."
    # квест-лог "Пойти на пляж на встречу с мистером Райтом."
    return

# локация на карте  - пляж

# при клике на локацию
label ep03_dialogues4_bike_rental_2:
    # Барди стоит на пляже, у пальмы
    sound run_stairs_floor
    fadeblack 2.0
    music Elle_avait_pas_les_yeux_noirs
    music2 ocean_waves
    imgfl 901351
    bardi_t "И как я найду этого Райта?.."
    # недалеко на шезлонге лежат девушки (студентки из колледжа, которые будут целоваться на вечеринке) и Барди на них пялится
    # девушки смеются и прикасаются друг к другу
    imgf 901352
    bardi_t "По-моему, одна из них учится со мной в одной группе..."
    imgd 901353
    bardi_t "Мне кажется или у них не совсем дружеские отношения? По ходу они встречаются..."
    imgf 901354
    bardi_t "Хмм.. А в колледже она ведет себя более скромно..."
    # внезапно в кадре появляется лицо Райта (father_friend), загораживая картину с девушками
    music stop
    sound plastinka1b
    img 901355 hpunch
    bardi "Оу!"
    music Adventures_of_the_Deaf_Dreamer
    imgd 901356
    mr_wright "Ты [mcname]?"
    imgd 901357
    bardi "Да, это я. А вы мистер Райт?"
    # Райт довольно улыбается
    imgd 901358
    mr_wright "Да. Привет, [mcname]."
    mr_wright "Я с трудом тебя узнал! Ты так вырос!"
    mr_wright "Я помню тебя еще совсем мелким сопляком!"
    imgd 901357
    bardi_t "Я вообще его не помню... Откуда он меня знает?"
    bardi_t "Хотя, в этом долбанном Санвиле все друг друга знают. Ничего удивительного."
    imgd 901359
    mr_wright "Слушай, [mcname], я тороплюсь. Так что давай перейдем к делу."
    imgd 901360
    bardi "Ага. Генри сказал мне, что вам нужен работник..."
    imgd 901361
    mr_wright "Да-да."
    mr_wright "Недалеко отсюда у меня есть велопрокат." # машет в сторону рукой, указывая
    imgd 901359
    mr_wright "Мне нужно, чтобы кто-то приглядывал за ним и сдавал велосипеды клиентам в аренду."
    mr_wright "Также брал с ним плату за аренду. Ну, в общем, следил за порядком. Вот."
    mr_wright "Справишься?"
    imgd 901360
    bardi "Думаю, да."
    bardi "А сколько я буду получать, мистер Райт?"
    # Райт мнется
    imgd 901362
    mr_wright "Нуу... Для начала я мог бы платить тебе 15 долларов за день работы."
    imgd 901363
    bardi "15 баксов в день?!"
    # Райт продолжает мяться
    sound Jump1
    img 901364 hpunch
    mr_wright "Да, мой мальчик..."
    mr_wright "Понимаешь, дела у проката сейчас не очень..."
    mr_wright "Работа идет в убыток..."
    mr_wright "Парк, где расположен прокат, не в лучшем состоянии... Дороги разбиты..."
    imgd 901365
    mr_wright "В общем, поток клиентов значительно порядел в последнее время."
    mr_wright "Вместе с этим, и прибыль..."
    imgd 901366
    w
    music The_Heat
    imgf 901367
    sound2 snd_longkiss1
    w
    imgd 901368
    w
    sound kiss1
    imgd 901369
    w
    imgf 901370
    w
    # за спиной у Райта девушки встают с шезлонгов и, поцеловавшись, уходят с пляжа, держась за руки
    # Райт продолжает вещать, уже более воодушевленно
    music Adventures_of_the_Deaf_Dreamer
    imgd 901371
    mr_wright "Но знаешь что? Если ты сможешь подтянуть клиентов, то мы сможем обсудить твое повышение!"
    mr_wright "Ты сможешь зарабатывать больше!"
    imgd 901372
    bardi "Угу."
    imgd 901371
    mr_wright "Ну, что скажешь? Возьмешься за работу?"
    imgd 901372
    bardi "Конечно, я рассчитывал на большее, мистер Райт..."
    bardi "А я могу посмотреть ваш велопрокат, прежде чем давать ответ?"
    imgd 901373
    mr_wright "Да, конечно."
    mr_wright "Сейчас у меня нет времени..."
    mr_wright "Но я проконсультирую тебя о том, что тебе нужно будет делать на работе в прокате, в любой другой день."
    mr_wright "Возможно, ты найдешь эту работу интересной..."
    mr_wright "Не торопись давать ответ прямо сейчас. Подумай."
    mr_wright "Приходи сюда на днях и я тебе все покажу, [mcname]."
    imgd 901374
    bardi "Окей. Договорились, мистер Райт."
    imgd 901375
    mr_wright "До встречи."
    imgd 901374
    bardi "До свиданья, мистер Райт."
    imgf 901376
    sound steps_park
    w
    # Райт уходит, Барди остается один
    imgd 901377
    bardi_t "Вот дерьмо!"
    bardi_t "Я рассчитывал на большее, чем 15 баксов в день!.."
    bardi_t "Черт! Нужно будет поискать еще варианты подработки..."
    sound iphone_text_message1
    ### смс на телефон
    label ep03_dialogues4_bike_rental_2a:
    $ mlsBardiDay4BikeRental1 = day # Барди встретился с Райтом на пляже
    # в этот момент приходит смс от Софи на телефон - сигнал
    fadeblack 1.5
    music2 stop
    return
    # sophie_chat5
    sophie "[mcname], мы ждем тебя на ужин. Ты не забыл?"
    sophie "Моя сестра Дейзи уже пришла. Поторопись, пожалуйста, милый."  ##->#####inc
    #####inc mother "Твоя тетя Дейзи уже пришла. Поторопись, пожалуйста, милый."
    bardi "Окей. Уже иду домой."
    sophie "Хорошо :)"
    fadeblack 1.5
    music2 stop
    return


#### 2-й день

# в колледже выходной, до визита к Дейзи

# при клике на пляж
label ep03_dialogues4_bike_rental_3:
    sound run_stairs_floor
    # у пальмы его ждет Райт
    fadeblack 2.0
    music Adventures_of_the_Deaf_Dreamer
    music2 ocean_waves
    imgf 901371
    mr_wright "[mcname], привет!"
    mr_wright "Ну что, готов увидеть свое рабочее место?"
    imgd 901372
    bardi "Да, но я еще не решил насчет..."
    # Райт его перебивает жестом
    imgd 901378
    mr_wright "Пошли за мной. Покажу тебе, что и как устроено у нас."
    mr_wright "Тут недалеко."
    # смена кадра - за пляжем, среди деревьев в глуши стоит трейлер (картинка - https://cdn.discordapp.com/attachments/902366000870203413/902372152672657498/unknown.png)
    # возле него два старых велика
    # они подходят к прокату
    # Райт горделиво указывает рукой
    fadeblack
    music2 stop
    sound steps_park
    pause 1.5
    music Shining_Through
    music2 city_park
    imgf 901379
    w
    imgd 901380
    mr_wright "Вот! Представляю тебе мой велопрокат 'Allen Wright' bikes'!"
    # Барди в афиге
    imgd 901381
    bardi "?!"
    bardi_t "Прокат?! Это какой-то сарай!"
    bardi_t "И здесь я должен буду работать?!"
    # Райт, видя замешательство Барди
    imgd 901382
    mr_wright "Да, согласен. Выглядит так себе..."
    mr_wright "Но это моя первая точка велопроката и я хотел чтобы она ожила вновь."
    imgd 901383
    bardi_t "Ну и старье!.."
    bardi "Почему-то я не удивлен, мистер Райт, что у вас мало клиентов..."
    imgd 901384
    mr_wright "Да, клиентов совсем мало..."
    mr_wright "Но я рассчитываю на тебя, [mcname]!"
    # в этот момент по дорожке мимо проката бежит тренер Брукс в своей спортивной форме
    imgf 901385
    sound running_tennis_shoes
    w
    imgd 901386
    w
    imgd 901387
    w
    imgd 901388
    mr_wright "О! Миссис Брукс! Отличная погодка для пробежки на свежем воздухе!"
    imgd 901389
    sound steps_park
    trainer_brooks "Добрый день, мистер Райт."
    # она останавливается возле них
    imgf 901390
    bardi "Здрасьте, тренер Брукс."
    # Барди смотрит на ее фигуру, пока она разговаривает с Райтом
    imgd 901391
    trainer_brooks "А ты что здесь делаешь, студент?"
    imgd 901392
    mr_wright "[mcname] помогает мне с делами в велопрокате..."
    imgf 901393
    w
    imgd 901394
    trainer_brooks "Вот как?!"
    imgd 901395
    bardi "Да..."
    imgd 901396
    mr_wright "Возможно, в следующий раз, ты предпочтешь велосипед, а не пробежку по парку?"
    mr_wright "Это очень полезно!"
    imgf 901397
    bardi_t "Если Брукс станет постоянной клиенткой проката, то я согласен на эту работу..."
    # Брукс с интересом смотрит на Барди
    imgd 901399
    trainer_brooks "Посмотрим..."
    trainer_brooks "От велопрогулки по вечерам после работы я не отказалась бы."
    # она бросает взгляд на велики у трейлера
    imgd 901398
    w
    imgd 901400
    trainer_brooks "Но точно не сейчас. Ладно, мне пора. Дела!"
    sound running_tennis_shoes
    imgf 901401
    mr_wright "Хорошего дня, миссис Брукс."
    trainer_brooks "Удачи!"
    # тренер убегает, Райт и Барди смотрят ей вслед, потом Райт говорит Барди
    imgd 901402
    mr_wright "Думаю, ты сможешь что-нибудь придумать, чтобы привлечь как можно больше клиентов!"
    mr_wright "Больше клиентов - больше заработок!"
    mr_wright "Ну что скажешь, [mcname]?"
    mr_wright "Решишься попробовать?"
    imgd 901403
    bardi_t "Очень сомневаюсь, что этот велопрокат можно оживить..."
    bardi_t "Но если я хочу быстрее свалить из этой дыры, то мне нужен заработок."
    bardi_t "15 баксов в день - это лучше, чем совсем ничего."
    imgd 901404
    bardi "Думаю, стоит попробовать, мистер Райт."
    bardi "Мне нужны деньги, а вариантов подработки у меня не сказать, чтобы было много..."
    imgf 901405
    bardi_t "Кстати, нужно будет сходить к Дейзи. Может, удастся договориться о подработке и у нее тоже."
    bardi_t "Было бы неплохо. Больше работы - больше денег."
    imgd 901406
    mr_wright "Вот и отлично!"
    mr_wright "Рад, что ты согласился, [mcname]!"
    mr_wright "Ты можешь приступить к работе прямо сейчас."
    imgd 901404
    bardi "Сейчас?"
    imgd 901407
    mr_wright "Конечно! Чего тянуть то?"
    imgd 901404
    bardi "У меня на сегодня запланированы кое-какие дела..."
    bardi "Думаю, что я мог бы начать работать на днях."
    imgd 901407
    mr_wright "О, понимаю. Наверное, свидание с какой-нибудь подружкой?" # подмигивает Барди
#    imgd 901408
#    w
    sound Jump1
    imgd 901409
    w
    imgd 901404
    bardi "Нуу... Можно и так сказать..."
    imgd 901406
    mr_wright "Тогда вопросов нет, хе-хе."
    mr_wright "Приходи сюда на днях после колледжа."
    mr_wright "Я тебе все объясню. И ты сможешь сразу начать работу."
    mr_wright "Первый день я буду работать с тобой и расскажу тебе о всех тонкостях."
    mr_wright "Договорились, [mcname]?"
    imgd 901404
    bardi "Окей."
    bardi "До свиданья, мистер Райт."
    mr_wright "Хорошего тебе дня!"
    # Райт отходит к великам у трейлера
    imgf 901410
    sound steps_park
    bardi_t "Да уж... Я рассчитывал на что-то большее, чем эта развалюха вместо проката..."
    bardi_t "Нужно сходить к Дейзи. Послушаю, что она мне может предложить..."
    fadeblack 1.5
    music2 stop
    return

# далее ep03_dialogues3_family_evening_5 - мысли перед посещением Дейзи
