define mr_wright = Character(_("Мистер Райт"), who_color=c_orange) # друг Генри, владелец велопроката (Wright)

default mlsBardiDay4BikeRental1 = 0 # Барди встретился с Райтом на пляже
default mlsBardiDay4BikeRental2 = 0 # Барди согласился работать в велопрокате

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
    img 901351
    bardi_t "И как я найду этого Райта?.."
    # недалеко на шезлонге лежат девушки (студентки из колледжа, которые будут целоваться на вечеринке) и Барди на них пялится
    # девушки смеются и прикасаются друг к другу
    img 901352
    bardi_t "По-моему, они учатся со мной в одной группе..."
    img 901353
    bardi_t "Мне кажется или у них не совсем дружеские отношения? По ходу они встречаются..."
    img 901354
    bardi_t "Хмм.. А в колледже они ведут себя более скромно..."
    # внезапно в кадре появляется лицо Райта (father_friend), загораживая картину с девушками
    img 901355
    w
    img 901356
    mr_wright "Ты [mcname]?"
    img 901357
    bardi "Оу!"
    bardi "Да, это я. А вы мистер Райт?"
    # Райт довольно улыбается
    img 901358
    mr_wright "Да. Привет, [mcname]."
    mr_wright "Я с трудом тебя узнал! Ты так вырос!"
    mr_wright "Я помню тебя еще совсем мелким сопляком!"
    img 901357
    bardi_t "Я вообще его не помню... Откуда он меня знает?"
    bardi_t "Хотя, в этом долбанном Санвиле все друг друга знают. Ничего удивительного."
    img 901359
    mr_wright "Слушай, [mcname], я тороплюсь. Так что давай перейдем к делу."
    img 901360
    bardi "Ага. Генри сказал мне, что вам нужен работник..."
    img 901361
    mr_wright "Да-да."
    mr_wright "Недалеко отсюда у меня есть велопрокат." # машет в сторону рукой, указывая
    img 901359
    mr_wright "Мне нужно, чтобы кто-то приглядывал за ним и сдавал велосипеды клиентам в аренду."
    mr_wright "Также брал с ним плату за аренду. Ну, в общем, следил за порядком. Вот."
    mr_wright "Справишься?"
    img 901360
    bardi "Думаю, да."
    bardi "А сколько я буду получать, мистер Райт?"
    # Райт мнется
    img 901362
    mr_wright "Нуу... Для начала я мог бы платить тебе 15 долларов за день работы."
    img 901363
    bardi "15 баксов в день?!"
    # Райт продолжает мяться
    img 901364
    mr_wright "Да, мой мальчик..."
    mr_wright "Понимаешь, дела у проката сейчас не очень..."
    mr_wright "Работа идет в убыток..."
    mr_wright "Парк, где расположен прокат, не в лучшем состоянии... Дороги разбиты..."
    img 901365
    mr_wright "В общем, поток клиентов значительно порядел в последнее время."
    mr_wright "Вместе с этим, и прибыль..."
    img 901366
    w
    img 901367
    w
    img 901368
    w
    img 901369
    w
    img 901370
    # за спиной у Райта девушки встают с шезлонгов и, поцеловавшись, уходят с пляжа, держась за руки
    # Райт продолжает вещать, уже более воодушевленно
    img 901371
    mr_wright "Но знаешь что? Если ты сможешь подтянуть клиентов, то мы сможем обсудить твое повышение!"
    mr_wright "Ты сможешь зарабатывать больше!"
    img 901372
    bardi "Угу."
    img 901371
    mr_wright "Ну, что скажешь? Возьмешься за работу?"
    img 901372
    bardi "Конечно, я рассчитывал на большее, мистер Райт..."
    bardi "А я могу посмотреть ваш велопрокат, прежде чем давать ответ?"
    img 901373
    mr_wright "Да, конечно."
    mr_wright "Сейчас у меня нет времени..."
    mr_wright "Но я проконсультирую тебя о том, что тебе нужно будет делать на работе в прокате, в любой другой день."
    mr_wright "Возможно, ты найдешь эту работу интересной..."
    mr_wright "Не торопись давать ответ прямо сейчас. Подумай."
    mr_wright "Приходи сюда на днях и я тебе все покажу, [mcname]."
    img 901374
    bardi "Окей. Договорились, мистер Райт."
    img 901375
    mr_wright "До встречи."
    img 901374
    bardi "До свиданья, мистер Райт."
    img 901376
    # Райт уходит, Барди остается один
    img 901377
    bardi_t "Вот дерьмо!"
    bardi_t "Я рассчитывал на большее, чем 15 баксов в день!.."
    bardi_t "Черт! Нужно будет поискать еще варианты подработки..."

    $ mlsBardiDay4BikeRental1 = day # Барди встретился с Райтом на пляже
    # в этот момент приходит смс от Софи на телефон - сигнал
    sophie "[mcname], мы ждем тебя на ужин. Ты не забыл?"
    sophie "Моя сестра Дейзи уже пришла. Поторопись, пожалуйста, милый."  ##->#####inc
    #####inc mother "Твоя тетя Дейзи уже пришла. Поторопись, пожалуйста, милый."
    bardi "Окей. Уже иду домой."
    sophie "Хорошо :)"
    return


#### 2-й день

# в колледже выходной, до визита к Дейзи

# при клике на пляж
label ep03_dialogues4_bike_rental_3:
    # у пальмы его ждет Райт
    img 901371
    mr_wright "[mcname], привет!"
    mr_wright "Ну что, готов увидеть свое рабочее место?"
    img 901372
    bardi "Да, но я еще не решил насчет..."
    # Райт его перебивает жестом
    img 901378
    mr_wright "Пошли за мной. Покажу тебе, что и как устроено у нас."
    mr_wright "Тут недалеко."
    # смена кадра - за пляжем, среди деревьев в глуши стоит трейлер (картинка - https://cdn.discordapp.com/attachments/902366000870203413/902372152672657498/unknown.png)
    # возле него два старых велика
    # они подходят к прокату
    # Райт горделиво указывает рукой
    img 901379
    mr_wright "Вот! Представляю тебе мой велопрокат 'Allen Wright' bikes'!"
    # Барди в афиге
    bardi "?!"
    bardi_t "Прокат?! Это какой-то сарай!"
    bardi_t "И здесь я должен буду работать?!"
    # Райт, видя замешательство Барди
    mr_wright "Да, согласен. Выглядит так себе..."
    mr_wright "Но это моя первая точка велопроката и я хотел чтобы она ожила вновь."
    bardi_t "Ну и старье!.."
    bardi "Почему-то я не удивлен, мистер Райт, что у вас мало клиентов..."
    mr_wright "Да, клиентов совсем мало..."
    mr_wright "Но я рассчитываю на тебя, [mcname]!"
    # в этот момент по дорожке мимо проката бежит тренер Брукс в своей спортивной форме
    mr_wright "О! Миссис Брукс! Отличная погодка для пробежки на свежем воздухе!"
    trainer_brooks "Добрый день, мистер Райт."
    # она останавливается возле них
    bardi "Здрасьте, тренер Брукс."
    # Барди смотрит на ее фигуру, пока она разговаривает с Райтом
    trainer_brooks "А ты что здесь делаешь, студент?"
    mr_wright "[mcname] помогает мне с делами в велопрокате..."
    trainer_brooks "Вот как?!"
    bardi "Да..."
    mr_wright "Возможно, в следующий раз, ты предпочтешь велосипед, а не пробежку по парку?"
    mr_wright "Это очень полезно!"
    bardi_t "Если Брукс станет постоянной клиенткой проката, то я согласен на эту работу..."
    # Брукс с интересом смотрит на Барди
    trainer_brooks "Посмотрим..."
    trainer_brooks "От велопрогулки по вечерам после работы я не отказалась бы."
    # она бросает взгляд на велики у трейлера
    trainer_brooks "Но точно не сейчас. Ладно, мне пора. Дела!"
    mr_wright "Хорошего дня, миссис Брукс."
    trainer_brooks "Удачи!"
    # тренер убегает, Райт и Барди смотрят ей вслед, потом Райт говорит Барди
    mr_wright "Думаю, ты сможешь что-нибудь придумать, чтобы привлечь как можно больше клиентов!"
    mr_wright "Больше клиентов - больше заработок!"
    mr_wright "Ну что скажешь, [mcname]?"
    mr_wright "Решишься попробовать?"
    bardi_t "Очень сомневаюсь, что этот велопрокат можно оживить..."
    bardi_t "Но если я хочу быстрее свалить из этой дыры, то мне нужен заработок."
    bardi_t "15 баксов в день - это лучше, чем совсем ничего."
    bardi "Думаю, стоит попробовать, мистер Райт."
    bardi "Мне нужны деньги, а вариантов подработки у меня не сказать, чтобы было много..."
    bardi_t "Кстати, нужно будет сходить к Дейзи. Может, удастся договориться о подработке и у нее тоже."
    bardi_t "Было бы неплохо. Больше работы - больше денег."
    mr_wright "Вот и отлично!"
    mr_wright "Рад, что ты согласился, [mcname]!"
    mr_wright "Ты можешь приступить к работе прямо сейчас."
    bardi "Сейчас?"
    mr_wright "Конечно! Чего тянуть то?"
    bardi "У меня на сегодня запланированы кое-какие дела..."
    bardi "Думаю, что я мог бы начать работать на днях."
    mr_wright "О, понимаю. Наверное, свидание с какой-нибудь подружкой?" # подмигивает Барди
    bardi "Нуу... Можно и так сказать..."
    mr_wright "Тогда вопросов нет, хе-хе."
    mr_wright "Приходи сюда на днях после колледжа."
    mr_wright "Я тебе все объясню. И ты сможешь сразу начать работу."
    mr_wright "Первый день я буду работать с тобой и расскажу тебе о всех тонкостях."
    mr_wright "Договорились, [mcname]."
    mr_wright "Хорошего тебе дня!"
    bardi "До свиданья, мистер Райт."
    # Райт отходит к великам у трейлера
    bardi_t "Да уж... Я рассчитывал на что-то большее, чем эта развалюха вместо проката..."
    bardi_t "Нужно сходить к Дейзи. Послушаю, что она мне может предложить..."
    return

# далее ep03_dialogues3_family_evening_5 - мысли перед посещением Дейзи
