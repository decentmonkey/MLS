default mlsBardiWorkMallBecky1 = 0 # Барди воспользовался пунктом Бесплатная услуга
default mlsBardiWorkMallBecky2 = 0 # Барди воспользовался пунктом Работа ручками
default mlsBardiWorkMallBecky3 = 0 # Барди воспользовался пунктом Минет
default mlsBardiWorkMallBecky4 = 0 # Барди воспользовался пунктом Классика
default mlsBardiWorkMallBecky5 = 0 # Барди воспользовался пунктом Анал

# локация ТЦ на карте города откроется только после встречи с Бекки в прокате

#Сцена возможна только вечером и начинается после клика на Бекки у ТЦ.

#При клике на Бекки.
label ep04_dialogues7_work_becky_1:
    # Бекки стоит у тележки с мороженым и курит
    if mlsBardiSeanDay3Whore1 > 0 or mlsBardiSeanDay3Whore2 > 0:
        bardi_t "О, это же та шлюшка с велопроката! Которую я еще у Шона трахнул!"
        bardi_t "Как ее? Бекки!"
        bardi_t "Да, она вроде говорила, что тут работает..."
    else:
        bardi_t "О это же та шлюшха с велопроката!"
        bardi_t "Как ее? Бекки!"
        bardi_t "Да, она вроде говорила, что тут работает... Честно говоря, не думал даже, что наткнусь на нее..."
    #Бекки замечает Барди и слегка удивляется. Бекки улыбаясь машет ему рукой и подзывает его к себе.
    becky "О, [mcname]! Это ты?"
    becky "Наконец-то, ты решил заглянуть ко мне!"
    becky "Я уж заждалась тебя..."
    #Барди подходит ближе.
    if mlsBardiSeanDay3Whore1 > 0 or mlsBardiSeanDay3Whore2 > 0:
        bardi_t "Блеск... Появляются связи с местными шлюхами..."
        bardi_t "С другой стороны, это даже неплохо. Может, удастся выбить себе скидку..."
    else:
        bardi_t "Хм... Не думал, что она запомнит меня после той короткой встречи..."
        bardi_t "С другой стороны, это даже неплохо. Может, удастся выбить себе скидку... Я же пошел ей на встречу в велопрокате..."
    #Бекки улыбается Барди. Стоит облокотившись о мороженицу. в руке тлеет сигарета.
    bardi "Да, привет! Пришлось же повозиться с твоими поисками..."
    becky "Ну... Результат ведь того стоил?.."
    bardi "Однозначно."
    bardi_t "Учитывая, что я ничего для этого не сделал..."
    bardi "Только вот я не ожидал увидеть тебя в роли продавца мороженого..."
    becky "Ахаха! Будем считать это моим прикрытием, красавчик." # подмигивает
    becky "Или ты думал, я буду здесь стоять с объявлением и прайсом в руках?"
    bardi "Хах. Представляю эту картину."
    #Бекки двусмысленно ухмыляется.
    becky "Ну что, красавчик? Угостишь даму сигареткой?"
    bardi "Сигареткой?"
    bardi "Это что, ваш профессиональный сленг какой-то?"
    # если был секс у Шона дома или если был минет в велопрокате
    if mlsBardiSeanDay3Whore1 > 0 or mlsBardiSeanDay3Whore2 > 0:
        bardi "Тебе ли не знать, что у меня там целый кальян."
        #Бекки смотрит на Барди удивленно, затем начинает ржать.
        becky "Ахаха! Это я знаю! Почувствовала это всем своим естеством, так сказать!"
        #Если Бекки отсосала Барди в велопрокате.
        if mlsBardiWorkDay1BikeRental5 > 0:
            becky "Даже почти два раза!"
        #
    #Бекки улыбается тыча в барда рукой в которой между пальцев держит сигарету.
    becky "Я про настоящие сигареты, красавчик."
    #Если Бекки отсосала Барди в велопрокате.
    if mlsBardiWorkDay1BikeRental5 > 0:
        becky "Еще одного шанса сделать это бесплатно, тем более, прямо на моем рабочем месте, у тебя не будет!"
    else:
        becky "Сделать это бесплатно, тем более, прямо на моем рабочем месте, у тебя не будет!"
    becky "Даже не надейся..."
    bardi_t "Ах ты стерва неблагодарная!"
    bardi "Ну это не честно! В велопрокате я тебе на встречу пошел!"
    #Бекки ржет прям от души.
    becky "Ахаха! Ну ты, конечно, и сравнил... Меня и эту старую рухлядь..."
    bardi_t "Ах так?!"
    bardi "Я, вообще-то, человека знаю, который на этом велике бэху на буксире протащил!"
    #Бекки ржет уже согнувшись в животе.
    becky "Водитель бэхи, наверное, просто со смеху подох!"
    #Бекки разогнулась и вытирает слезу с глаза.
    becky "Ладно, фантазер... Рассмешил ты меня, конечно..."
    becky "Сигарета то есть?"
    bardi "Но ты уже куришь..."
    #Бекки смотрит на сигарету  не меняя позу. потом сново переводит взгляд на Барди. лицо нейтральное.
    becky "Так она дотлеет скоро..."
    becky "Ты же не был таким жмотом в прокате! Что вдруг с тобой стало?.."
    bardi "Сигарет действительно нет. Я не курю. Могу только побаловаться изредка..."
    #Бекки хмурая стоит облокотившись к мороженице и затягивая сигарету.
    becky "Тьфу... Поразведется же зожников!.."
    #Бекки зажала сигарету в зубах и копается в сумочке. Достает почти полную пачку сигарет. Открыв ее протягивает Барди.
    bardi "Ну нихрена себе ты настреляла сигареток!"
    becky "Ага, надеялась и ты чего-нибудь оставишь..."
    #Барди берет одну в руку.
    bardi "Ну, что поделать? Приходи в велопрокат, бесплатно покатаешься..."
    #Бекки Двусмысленная улыбка с намеком.
    becky "На велике уже не интересно."
    bardi "Да? Ну значит на кое-чем другом..."
    #Бекки прикусывает губу.
    becky "Хорошо. Но как только ты заработаешь денег на мои услуги..."
    #Барди наклонившись к Бекки, которая держит зажигалку, прикуривает сигарету.
    #Изобразите так чтоб было видно ее формы. Бекки убирает руку с сигаретой и Барди видит ее фигуру лучше. (не показываем, как Барди курит)
    becky "Нравится?"
    bardi "Однозначно."
    becky "Ну и отлично. Должен же ты хорошенько рассмотреть товар перед покупкой..."
    #Бекки пеняет позу на более сексуалную.
    becky "А так?"
    bardi "Просто огонь! Зачем тебе вообще с таким горячим телом зажигалка?"
    #Барди выпрямился. Бекки сексуально смотрит на него.
    becky "Мой привлекательный вид - мои бабки. Я горжусь своим телом, оно охрененное."
    #Бекки задумчиво смотрит в сторону.
    #Бекки затягивается и смотрит на Барди. На ее лице самодовольная улыбка.
    becky "Ну и? Я вроде сказала тебе, где работаю. Почему ты так долго не приходил?"
    bardi_t "Фак! Да я и так случайно набрел!.."
    bardi "Да попробуй сориентируйся между этими улочками..."
    bardi "Я по началу, честно говоря, думал ты и забыла меня..."
    #Бекки соблазнительная поза и улыбка.
    becky "Ага, конечно... Такого красавчика забудешь..."
    becky "Я, знаешь ли, уже давно хотела снова увидеться с тобой."
    bardi "Так получается, нам ничего не мешает продолжить нашу прошлую встречу?.."
    #Бекки - соблазнительная задумчивость и предвкушение.
    becky "Мммм... Продолжить?.."
    #Бекки машет головой и отгоняет эти мысли.
    becky "Нет-нет-нет, Бекки! Нет!"
    #Бекки смотрит на Барди с желанием.
    if mlsBardiSeanDay3Whore1 > 0 or mlsBardiSeanDay3Whore2 > 0:
        bardi "А что такого? Разве ты сама не хочешь, чтоб я снова отодрал тебя, как в тот раз?"
    else:
        bardi "Что? По-моему, ты и сама хочешь этого побольше, чем я!"
    bardi "Да и там, в прокате, ты была готова чуть ли не средь белого дня прямо у пляжа!.."
    becky "Я и сейчас..."
    #Бард подходит к Бекки и начинает лапать ее. Изобразите это в нескольких рендерах.
    becky "Мммм... Я уже чувствую его..."
    bardi "Он стоит с тех пор, как я увидел тебя здесь."
    bardi "Ты просто обязана помочь мне снять это напряжение..."
    #Барди целует Бекки в шею. Бекки там вообще на кайфах уже.
    becky "Ох... Да-а-а..."
    #Барди просовывает ладонь В трусы к Бекки.
    bardi "Боже... Да ты же уже потекла водопадом..."
    bardi "Может мы уже отойдем в сторонку?"
    becky "Да..."
    #Бекки растерянная.
    becky "Нет!"
    bardi_t "Фак!"
    #Бекки отстраняется от Бардаи. Отходит и говорит сама с собой.
    becky "Нет-нет-нет, Бекки! Ты дала себе слово!"
    becky "А потом уточнила, что в том числе и не с [mcname]!"
    becky "Больше такого не повторится!"
    #Бекки оборачивается на Барди. лицо нейтральное.
    bardi "Что случилось то? В прокате ты чуть ли не сама запрыгивала мне на член!"
    #Бекки хмурая жалуется на жизнь.
    becky "Да я знаю! И сейчас готова! Но..."
    bardi "Но что?"
    becky "Да я просто уже задолбалась!"
    #Бекки повернулась к Барди. Растерянная. Рассказывает жестикулируя руками.
    becky "Это, конечно, офигенная работа для нимфоманки вроде меня."
    becky "Я обожаю свою работу!"
    #Поменяйте жестикуляцию Бекки.
    becky "Охрененный доход, наслаждение..."
    becky "Да и с моим восхитительным телом не бывает никаких проблем с количеством клиентов..."
    #Бекки хмурая. поза соответствующая.
    becky "Но твою мать!.."
    becky "Стоит только появиться на горизонте какому-нибудь сексуальному красавчику!.."
    becky "Как я тут же таю и готова отдаться ему бесплатно!"
    becky "Как с тобой в прокате!"
    #Бекки безысходность.
    becky "Я обязана начать контролировать себя!"
    becky "Иначе, такими темпами, я скоро перестану иметь хоть какой-нибудь заработок!"
    if mlsBardiSeanDay3Whore1 > 0 or mlsBardiSeanDay3Whore2 > 0:
        bardi "Почему бы тебе не подумать об этом завтра? А сегодня просто отдаться своим желаниям..."
        bardi "Как никак, сегодня праздник - наша третья встреча."
        bardi "Ты знала что три - это счастливое число?"
    else:
        bardi "Почему бы тебе не подумать об этом завтра? А сегодня просто отдаться своим желаниям..."
        bardi "Как никак, я наконец нашел тебя, а ты так обламываешь... Причем и меня, и себя..."
    #Бекки задумчивая сексуальная поза. Бекки снова хмурая.
    becky "Нет, нихрена!"
    becky "Я знаю себе цену. Таких, как я, во всем городе не сыщешь!"
    becky "А даже если и найдешь - далеко не каждая тебе даст!"
    becky "Если есть деньги, то погнали. Денег нет - свободен, красавчик."
    bardi_t "Вот облом! Фак!"
    #Бекки смотрит на Барди с надеждой.
    becky "Но я все же надеюсь, ты успел хоть что-то заработать со времени нашей прошлой встречи?.."
    becky "Ты же на работу устроился... Неужели у тебя нет денег?"
    bardi "..."
    #Бекки хмурая.
    becky "Черт с тобой! Я сделаю индивидуально скидку для тебя!"
    becky "Минус 50 процентов от стоимости каждой услуги."
    becky "В честь того, что ты только недавно сюда приехал..."
    bardi "Оу... Очень любезно с твоей стороны..."
    bardi "Кстати, а где ты оказываешь свои услуги?"
    bardi "Не за этой же тележкой с мороженым?"
    becky "Ахаха! Конечно, нет!"
    # подмигивает
    becky "В этом торговом центре весьма удобные кабинки в туалете..."
    bardi "О как?! А если кто-то спалит?"
    becky "У меня все под контролем, красавчик."
    becky "Ну так что? Ты определился со своими желаниями?.."
    #ВНИМАНИЕ! если Барди не соглашасля на бартер с Бекки в прокате (не было минета)
    #появляется еще один дополнительный выбор: "Бесплатная услуга"
    #После выбора которой проигрывается короткий диалог, за которым следует та же серия выборов но все бесплатные(!). Из них игрок может выбрать только один пункт
    label ep04_dialogues7_work_becky_1_repeat:
    bardi "..."
    $ menu_data = {
        "Бесплатная услуга.":{"enabled":True if mlsBardiWorkDay1BikeRental3 > 0 and mlsBardiWorkDay1BikeRental5 == 0 else False} # доступно, если Барди не соглашасля на бартер с Бекки в прокате
        }
    menu:
        "Бесплатная услуга.": # доступно только один раз
            $ mlsBardiWorkMallBecky1 = day # Барди воспользовался пунктом Бесплатная услуга
            #Бекки нейтральная. Стоит перед барди снова с сигаретой.
            #руки вроде и скрещены на груди но в одной сигарета и она поднята предплечьем и кистью вверх.
            #Ноги в таком положении что одна прям под ней, вторая суть в сторону, будто вес только на одной ноге.
            bardi "Хммм... Я тут вспомнил..."
            becky "Что?.."
            #Бекки удивленная, с нотками сарказма, тип такая "Да что ты говоришь..."
            bardi "Ты должна мне бесплатную услугу."
            becky "Даже так? И с чего же это вдруг?"
            #Бекки хмурая задумчивая.
            bardi "Мы так договорились, если ты вдруг забыла."
            becky "Когда?"
            #Бекки удивленно растерянная
            bardi "Когда я за просто так подогнал тебе велик. Ты сказала, что мы еще рассчитаемся."
            becky "Оу..."
            becky "Подожди..."
            #Бекки начинает ржать.
            becky "Ахаха! Ты действительно решил сравнивать меня с тем старьем?!"
            bardi "Раз уж на то пошло, великам от силы лет 27! И они в идеальном состоянии!.."
            bardi_t "Не считая того, что они разваливаются прямо на ходу..."
            #Бекки продолжает ржать но вытирая слезу с глаза смотрит на Барди.
            becky "Ахаха! Ты сейчас серьезно?!"
            bardi "Вполне."
            #Бекки смотрит на Барди более или менее серьезно.
            bardi "Самое время платить по счетам, я считаю."
            becky "Это даже немного обидно, красавчик..."
            #Бекки смотрит на Барди Возбужденным взглядом, можно чуть прикусить губу, все дела...
            bardi "Да брось..."
            bardi "Ты ведь сама только что искала повод, чтобы запрыгнуть на мой член."
            becky "Хмм..."
            bardi "А так это будет не бесплатно, а скорее, услуга за услугу."
            #Бекки все такая же возбужденная поднимает взгляд вверх и в сторону, словно о чем-то задумалась.
            becky "А в твоих словах есть смысл... Ты неплохо умеешь вести дела, красавчик."
            becky "Хах! Может, станешь моим сутенером?"
            bardi "А он имеет право трахать тебя, когда ему вздумается?"
            #Бекки улыбнувшись машет головой.
            becky "Нет."
            bardi "Тогда меня это предложение не интересует. Так что там? Рассчитаемся?"
            becky "Хорошо, хитрец."
            becky "Но выбирай тщательно. Это всего лишь на один раз."
            bardi "Хах! А мы бы могли построить очень даже выгодные взаимоотношения."
            bardi "Приходи в велопрокат почаще и катайся сколько угодно."
            #Бекки посмеиваясь
            becky "Нет, спасибо. Ненавижу велосипеды."
            bardi "А почему тогда подошла?"
            #Бекки снова возбужденная и сексуальная.
            becky "Увидела одного красавчика..."
            bardi "Оу... Спасибо."
            becky "Ладно, давай выбирай. На этот раз - одна услуга бесплатно. Но больше это не прокатит."
            bardi "Это мы еще увидим..."
            menu:
                "Работа ручками.": # 15
                    jump ep04_dialogues7_work_becky_1_1
                "Минет": # 30
                    jump ep04_dialogues7_work_becky_1_2
                "Классика.": # 70
                    jump ep04_dialogues7_work_becky_1_3
                "Анал.": # 90
                    jump ep04_dialogues7_work_becky_1_4
                "Уйти.":
                    jump ep04_dialogues7_work_becky_1_5
        "Работа ручками.":
            # минус 15 баксов у Барди
            #Бекки смотрит на барди с соблазнительной ухмылкой.
            label ep04_dialogues7_work_becky_1_1:
            $ mlsBardiWorkMallBecky2 = day # Барди воспользовался пунктом Работа ручками
            bardi "Поработаешь своими ручками."
            becky "Оу... Решил начать с малого?.."
            bardi "Да, оценить товар, как ты говорила..."
            becky "Что ж... Надеюсь у этого будет продолжение..."
            bardi "Смотря как ты себя покажешь."
            #Бекки разворачивается к барду спиной и начинает идти в сторону входа в ТЦ. Жестом руки она велит Барди следовать за ней.
            becky "Ну пойдем, посмотришь... А точнее, почувствуешь."
            #Затемнение.
            #Просветление.
            # смена локации - туалет ТЦ, кабинка
            #Барди стоит прижавшись спиной к стене и раздвинув ноги. Бекки стоит на коленях перед ним. и спускает штаны с Барди. Смотрит на Барди. Верхняя одежда все еще на ней.
            becky "Начнем?"
            bardi "Пожалуй."
            #Бекки переводит взгляд на пах Барди и спускает штаны высовывая член. Бекки берет его в руку. Покажите это в двух рендерах.
            becky "Офигеть! Ну и здоровяк!.."
            #Член Барди встает. Бекки удивлена.
            becky "Я никогда не перестану удивляться этому размеру!"
            #Бекки начинает дрочить барду. Сначала одной рукой.
            bardi "Ох... Да..."
            becky "Мммм, как же я его хочу..."
            #Бекки переводит взгляд на Барди.
            becky "И почему ты не мог выбрать минет, чтобы я тоже от души насладилась процессом?"
            becky "Думал, я сорвусь и дам себя трахнуть?"
            bardi "Честно говоря, я и сейчас на это надеюсь..."
            #Бекки второй рукой начинает тип стимулировать головку.
            becky "Что ж... У тебя почти получилось."
            becky "Я еле держусь, чтобы не затолкать его себе глубоко в глотку."
            becky "А затем оседлать твоего здоровяка, красавчик."
            bardi "Ох... Так чего же ты ждешь, я только за!"
            becky "Денег."
            becky "О, Боже! Он так близко, и не во мне!.."
            bardi "О, дааа!.."
            becky "Черт!.. Я уже вся мокрая!.."
            bardi "Твою мать, Бекки, еще одно слово и я поставлю тебя раком прямо здесь! Оооох!"
            becky "За это придется доплатить..."
            #Бекки дрочит Барди. Вторую руку убираете. Анимация ускоряется еще сильнее.
            bardi "Оооо!!!"
            bardi "О, да!!! Я уже скоро! Да!!!"
            becky "Давай! Сделай это мне на лицо!"
            menu:
                "Кончить на лицо Бекки.":
                    pass
            bardi "Оооо!.. Кончаю!.."
            #Барди кончает на лицо Бекки. Сделайте ей возбужденное лицо и откройте рот + высуньте язык.
            bardi "АААААА!!!"
            bardi "О, дааа..."
            bardi "Мммм..."
            becky "Обожаю этот вкус!"
            # затемнение
            #Член Барди в штанах. Бекки со спермой на лице подмигивает Барди.
            becky "Ну? И как я себя показала, красавчик?"
            bardi "Черт... Думаю, это высший балл!"
            #Бекки улыбается.
            #Затемнение.
            pass
        "Минет":
            # минус 30 баксов у Барди
            #Бекки смотрит на барди с соблазнительной ухмылкой.
            label ep04_dialogues7_work_becky_1_2:
            $ mlsBardiWorkMallBecky3 = day # Барди воспользовался пунктом Минет
            bardi "Поработаешь своим ротиком."
            becky "Оу... Хороший выбор. Жаль, только мне не насладиться этим так, как хотелось бы..."
            becky "Раньше тебе делали минет?"
            bardi "Пфф! Издеваешься?! Конечно, делали!"
            #Бекки самодовольная ухмылка.
            becky "Можешь забыть об этом, красавчик."
            becky "После моего язычка, ты забудешь все, что было раньше."
            bardi "Звучит многообещающе..."
            becky "Поверь мне. Ты не разочаруешься."
            #Бекки разворачивается к барду спиной и начинает идти в сторону входа в ТЦ
            #Жестом руки она велит Барди следовать за ней.
            becky "Пошли."
            #Затемнение.
            #Просветление.
            # смена локации - туалет ТЦ, кабинка
            #Барди стоит прижавшись спиной к стене и раздвинув ноги. Бекки стоит на коленях перед ним. и спускает штаны с Барди.
            #Смотрит на Барди. Бекки без верхней одежды.
            becky "Начнем?"
            bardi "Пожалуй."
            #Бекки переводит взгляд на пах Барди и спускает штаны высовывая член. Бекки берет его в руку. Покажите это в двух рендерах.
            becky "Офигеть! Ну и здоровяк!.."
            #Член Барди встает. Бекки удивлена.
            becky "Я никогда не перестану удивляться этому размеру!"
            #Бекки начинает дрочить барду. Сначала одной рукой.
            bardi "Ооох... Дааа!.."
            becky "Как же я его хочу!.."
            #Бекки переводит взгляд на Барди.
            becky "И почему ты не мог выбрать что-то такое, чтобы я тоже от души насладилась процессом?"
            becky "Мне безумно хочется почувствовать его у себя во рту..."
            becky "Но есть пара местечек, куда твой член пристроился бы намного лучше..."
            becky "Думал, я сама сорвусь и оседлаю тебя?"
            bardi "Честно говоря, я и сейчас на это надеюсь."
            #Бекки смотрит снова на член.
            becky "Что ж... У тебя почти получилось."
            becky "Я еле держусь, чтоб не оседлать твоего здоровяка сразу после минета!.."
            bardi "Ооох... Так что же тебя останавливает? Я только за!"
            becky "Деньги."
            #Барди кладет руку на голову Бекки. Бекки удивлена.
            bardi "Так ладно... Меньше слов..."
            becky "Что?"
            #Барди заталкивает член в рот Бекки по яйца. Глаза Бекки округлились, она в шоке.
            bardi "Больше дела!"
            bardi "Ох, дааа!.."
            becky "Мпфхфмм!.."
            #минета. Барди придерживает Бекки за голову,
            bardi "О, дааа!"
            bardi "Так глубоко!.. Дааа!"
            bardi "Оооох..."
            #Бекки ускоряется.
            bardi "Мммм!.."
            becky "Мпфхф..."
            bardi "Ох... Ты действительно лучшая в этом деле!.."
            bardi "Давай!"
            bardi "Быстрее!"
            #Бекки ускоряется еще сильнее.
            bardi "О, как охренительно! Да!"
            bardi "Я уже скоро!"
            bardi "О, да!.."
            menu:
                "Кончить в рот Бекки.":
                    #Барди хватает Бекки за голову и заталкивает член в глотку.
                    bardi "Оооо!.. Кончаю!.."
                    bardi "АААААА!!!"
                    bardi "О, дааа..."
                    becky "Мпфхф!!!"
                    bardi "Мммм..."
                    #Несколько Рендеров где Бекки в шоке а потом кайфует.
                    #Барди вытаскивает член из Бекки. Бекки откашливается.
                    bardi "Это было чертовски охренительно!"
                    becky "Кхе-кхе! Черт!.."
                    pass
                "Кончить на лицо Бекки.":
                    #Барди кончает на лицо Бекки
                    bardi "Оооо!.. Кончаю!.."
                    bardi "АААААА!!!"
                    bardi "О, дааа..."
                    becky "Мммм..."
                    bardi "Это было чертовски охренительно!"
                    pass
            #Бекки удивленная, через силу улыбается.
            becky "Черт! Он не должен был поместиться у меня во рту!"
            becky "Даже для меня это слишком!.."
            bardi "И, тем не менее, все прошло гладко."
            #Бекки поднимает глаза на Барди. улыбается.
            becky "Понравилось, красавчик?"
            bardi "Еще бы!"
            #Затемнение.
            pass
        "Классика.":
            # минус 70 баксов у Барди
            #Бекки смотрит на барди с соблазнительной ухмылкой.
            label ep04_dialogues7_work_becky_1_3:
            $ mlsBardiWorkMallBecky4 = day # Барди воспользовался пунктом Классика
            bardi "Секс."
            becky "Оу... Это уже мне нравится!.."
            becky "Наконец-то, я смогу насладиться твоим членом сполна!"
            bardi "Хах! Мне все больше начинает казаться, что ты должна начать платить мне за секс."
            bardi "Ты хочешь этого больше меня!"
            #Бекки самодовольная ухмылка.
            becky "Можешь забыть обо всем, что было у тебя до меня."
            becky "Сегодня я дам тебе наивысшее наслаждение."
            bardi "Надеюсь, это действительно будет так."
            #Бекки разворачивается к барду спиной и идет в сторону входа в ТЦ
            #Жестом руки она велит Барди следовать за ней.
            becky "Не сомневайся."
            #Затемнение.
            #Просветление.
            # смена локации - туалет ТЦ, кабинка
            #Барди стоит прижавшись спиной к стене и раздвинув ноги.
            #Бекки стоит на коленях перед ним. и спускает штаны с Барди.
            #Смотрит на Барди. Бекки без нижней одежды, в одних чулках. грудь оголена.
            becky "Начнем?"
            bardi "Пожалуй."
            #Бекки переводит взгляд на пах Барди и спускает штаны высовывая член.
            #Бекки берет его в руку. Покажите это в двух рендерах.
            becky "Офигеть, ну и здоровяк!"
            becky "Никогда не перестану удивляться этому размеру!.."
            becky "Пожалуй, для начала, его неплохо было бы смазать..."
            #Бекки берет его член в рот, лижет его и все дела. покажите это в нескольких рендерах.
            bardi "О, дааа!.."
            becky "Он огромен! Это же его еще протолкнуть в себя надо!.."
            #Бекки отстраняется от члена Барди и обнимая Барди целует его.
            #Затем Барди берет ее ногу за бедро и облокотив Бекки о стену прижимается членом к ее животу. Лицо Бекки в нетерпении.
            becky "О да, красавчик! Давай уже!"
            becky "Вставь его в мою киску! Заполни меня всю! Скорее же!"
            #Барди вставляет головку внутрь и медленно долбит Бекки.
            bardi "О, дааа!"
            becky "О, Боже! Да! Он во мне!"
            becky "Он входит в меня полностью!"
            bardi "Оооо! Как же хорошо!"
            becky "Жестче! Трахай меня жестче!"
            #Барди поднимает ее на руки и прижав к стене долбит быстрее.
            #Бекки кайфует.
            becky "Оооох!!! Дааа!"
            becky "Ты лучший!"
            bardi "О, да! Как же круто!"
            becky "Еще-еще!"
            #Барди ускоряется.
            becky "Да! Какой же он огромный, [mcname]!"
            becky "Аааа!"
            becky "Оооо! Я сейчас кончу!"
            bardi "Дааа! Я тоже! Уже почти!.."
            becky "Не смей вытаскивать! Слышишь?!"
            becky "Кончи в меня!"
            becky "Заполни мою киску!"
            bardi "О, дааа! Я сейчас!"
            # Бекки кончает
            becky "ААААА!"
            becky "АААААААА!!!"
            menu:
                "Кончить в киску Бекки.":
                    pass
            #Барди заталкивает член в киску Бекки и кончает внутрь.
            #Покажите в нескольких рендерах как сперма просачивается наружу.
            bardi "Оооо!.. Кончаю!.."
            bardi "АААААА!!!"
            bardi "О, дааа..."
            becky "Мммм..."
            becky "Ох!.. Как же это было охренительно!"
            bardi "О, да! Ты лучшая!"
            #На следующем рендере бард высовывает член из Бекки.
            becky "Мммм... Я чувствую, как твоя сперма вытекает из моейм киски! Обожаю!.."
            #Бекки садится на корточки
            becky "О, Боже!.. Я никогда не забуду это!"
            becky "Как мне теперь с другими клиентами трахаться?!"
            becky "Если это участится, ты растянешь меня до такой степени, что они перестанут что-либо чувствовать!"
            bardi "Зато тогда ты станешь только моей."
            #Бекки пытается встать облокотившись к стене. Ее ноги подкашиваются.
            becky "Ох, [mcname]!.. Я стоять не могу! У меня подкашиваются ноги!"
            bardi "Ееее... Согласен, это было улетно..."
            bardi "И мне все больше начинает казаться, что это ты должна платить мне за секс."
            becky "Честно говоря, мне уже тоже..."
            #Затемнение.
            pass
        "Анал.":
            # минус 90 баксов у Барди
            #Бекки смотрит на барди с соблазнительной ухмылкой.
            label ep04_dialogues7_work_becky_1_4:
            $ mlsBardiWorkMallBecky5 = day # Барди воспользовался пунктом Анал
            bardi "Анальный секс."
            becky "Хмм... Какой интересный выбор..."
            becky "Захотелось попробовать мою попку? Почему бы и нет?.."
            becky "Давно моя попка не развлекалась..."
            bardi "Хах. Что-то мне все больше начинает казаться, что это ты должна платить мне за секс."
            #Бекки самодовольная ухмылка.
            becky "Я заставлю забыть все, что у тебя было до этого дня, красавчик."
            becky "Готовься. Считай, что сегодня врата рая распахнулись пред тобой."
            bardi "Звучит очень даже многообещающе..."
            #Бекки разворачивается к барду спиной и идет в сторону входа в ТЦ
            #Жестом руки она велит Барди следовать за ней.
            becky "Можешь не сомневаться в этом..."
            # смена локации - туалет ТЦ, кабинка
            #Барди стоит прижавшись спиной к стене и раздвинув ноги.
            #Бекки стоит на коленях перед ним. и спускает штаны с Барди. Смотрит на Барди.
            #Бекки без нижней одежды, в одних чулках. грудь обнажена.
            becky "Начнем?"
            bardi "Пожалуй."
            #Бекки переводит взгляд на пах Барди и спускает штаны высовывая член. Бекки берет его в руку. Покажите это в двух рендерах.
            becky "Офигеть, ну и здоровяк!.."
            becky "Никогда не перестану удивляться этому размеру!"
            becky "Пожалуй, для начала его неплохо было бы смазать. В моей попке довольно узко..."
            #Бекки берет его член в рот, лижет его и все дела. покажите это в нескольких рендерах.
            becky "Мпфхф!"
            becky "Мпфхфмм!!!"
            bardi "О, дааа..."
            bardi "Мммм..."
            #Рендер: "#Бекки_съела_член_целиком" - Думаю вы поняли о чем я. На следующем рендере она вытаскивает его изо рта.
            becky "Он огромен! Даже не знаю, пролезет ли такой здоровяк в мою попку!.."
            #Бекки отстраняется от члена Барди и обнимая Барди целует его.
            becky "Ну что? Готов?"
            bardi "Пфф! Ты еще спрашиваешь?.."
            #Бекки поворачивается спиной к Барди, наклонившись и уперевшись спиной о стену.
            #Попу оттопырила, спинку прогнула.
            #Обернулась на Барди и смотрит на него с нотками страха в глазах. В общем тревожно. Член Барди между ягодиц Бекки.
            becky "Ох, твою мать!.. Он точно влезет в мою попку?"
            #Барди шлепает Бекки по ягодице. Выражение лица Бекки, сначала легкая боль, затем снова тревожность.
            becky "Ау!"
            #Барди трет член между ягодиц Бекки. не очень быстро.
            bardi "О, да!.."
            becky "Твою мать, он же как пол моей руки!"
            bardi "Боишься?"
            becky "Конечно! Я не особо разрабатывала свою попку! Она не готова к таким размерам!"
            becky "И хватит уже размазывать мою слюну! Я его так тщательно сосала, чтоб он легко вошел!"
            becky "Давай уже, действуй!.."
            #Барди прикладывает головку к анусу.
            becky "Черт! Только аккуратнее, не разорви меня..."
            #Барди шлепает Бекки по заднице.
            bardi "Расслабься и дай мне вставить!"
            becky "Ох!"
            #Барди вставляет головку внутрь, Бекки в шоке.
            becky "Ох черт! Только, пожалуйста, помедленнее..."
            becky "Погоди, дай мне немного привыкнуть."
            bardi "Помедленнее? А кто мне тут райское наслаждение обещал, м?.."
            becky "Да... Но..."
            #Барди заталкивает член до упора. Бекки сильно выгибается в спине от боли. Лицо к стене и задранно вверх.
            bardi "О, ДААА!"
            becky "А-А-А!! Черт, [mcname]! Я же попросила!"
            #Бекки снова повернула лицо к барди. Изобразите на ее лице боль. Тип прищурен глаз а второй и вовсе закрыт чуть хмурая итд...
            bardi "Терпи, я начинаю двигаться."
            becky "Только помедленнее! Ты же меня порвешь!"
            #Барди медленно долбит Бекки В задничу. Бекки обернувшись смотрит на все это дело. Ей по началу больно.
            bardi "Ох, черт!.. Какая же ты узенькая!.."
            bardi "Мммм..."
            becky "Я же говорила, что не разрабатывала свою попку..."
            bardi "Оооох... Это безумно приятно!.."
            becky "Я же тебе говорила..."
            bardi "Мммм..."
            becky "Аккуратнее! Не порви меня!.."
            becky "Оооох!.."
            becky "Кажется, мне начинает нравится..."
            becky "Не могу поверить... Оооо!.. Что он помещается в мою попку весь!.."
            becky "Оооох... Да!.."
            bardi "Твою мать! Как же это охрененно!.."
            becky "О, да!.. Ты можешь чуть-чуть ускориться?.. Мммм..."
            #Бекки начинает получать удовольствие. Рот приоткрыт, щеки краснеют, в глазах уже нет боли.
            bardi "О, да!"
            becky "Ох, твою мать! Я сейчас разорвусь!"
            becky "Мне так хорошо, [mcname]!"
            becky "Не останавливайся! Двигайся! Еще!"
            becky "Какой же он огромный! И весь в моей тугой узкой попке!"
            becky "Дааа!"
            becky "Как же это кайфово!"
            becky "Я чувствую, как он расширяет мою дырочку!"
            bardi "Ееее!.. Какая же узкая у тебя попка!"
            bardi "Я собираюсь ускориться! Твоя попка готова?"
            becky "Черт! [mcname]! Да-да!"
            becky "Да! Оттрахай меня еще жестче!"
            #Барди ускоряется еще сильнее. Бекки там вообще уже в афиге. глаза закатаны язык высунула ноги подкашиваются.
            becky "А-А-А-А! Дааа!"
            becky "[mcname]! Еще! Еще сильнее!"
            #Барди шлепает Бекки по заднице.
            becky "Аааах! Даааа!"
            bardi "Ееее!.."
            becky "Охренеть, я никогда не ощущала подобного!"
            becky "Я скоро кончу!"
            bardi "Я тоже!"
            becky "Давай! Заполни мою попку!"
            # Бекки кончает
            becky "ААААА!"
            becky "АААААААА!!!"
            #Барди заталкивает член в задницу.
            menu:
                "Кончить в попу Бекки.":
                    pass
            bardi "Оооо!.. Кончаю!.."
            bardi "АААААА!!!"
            becky "О, дааа... Она вытекает в меня!"
            becky "Заполняет меня! Даа..."
            bardi "О, дааа..."
            becky "Мммм..."
            #Барди вынимает член. Из раздолбанной задницы Бекки просачивается сперма.
            becky "Охренеть!.. Я кончила!"
            becky "О, дааа..."
            bardi "Твою мать, Бекки. Это было охренительно!.."
            becky "Да, это было чертовски охренительно, красавчик!"
            #Бекки опускается на корточки.
            bardi "Как ты?"
            becky "Ты... Ты чуть не разорвал меня надвое... Но это было божественно..."
            becky "Черт... Мне кажется, я еще не скоро смогу ходить..."
            becky "И сидеть..."
            becky "Дай... Дай мне прийти в себя..."
            becky "Еще несколько минут..."
            bardi "Ееее... Согласен, это было улетно..."
            bardi "И мне все больше начинает казаться, что это ты должна платить мне за секс."
            becky "Честно говоря, мне уже тоже..."
            # затемнение
            pass
        "Уйти.":
            label ep04_dialogues7_work_becky_1_5:
            bardi "Нет, не сегодня... Как-нибудь в следующий раз."
            #Бекки разочарованная.
            becky "Совсем нет?"
            bardi "Совсем."
            #Бекки хмурая, затем нейтральная.
            becky "Жаль, конечно, ну ладно... Значит в следующую нашу встречу."
            becky "Приходи, когда заработаешь для меня много денежек."
            bardi "Обязательно."
            #Бекки подмигивает Барди. Поза сексуальная. Бекки ставит руку на ягодицу.
            becky "Не забывай. Эта попка ждет не дождется тебя, красавчик."
            bardi "И мы с ней обязательно встретимся."
            # затемнение.
            return
    # Бекки и Барди стоят у ТЦ после затемнения
    becky "Приходи в следующий раз, когда заработаешь для меня много денежек."
    bardi "Обязательно."
    #Бекки подмигивает Барди. Поза сексуальная. Бекки ставит руку на ягодицу.
    becky "Не забывай. Эта попка ждет не дождется тебя, красавчик."
    bardi "И мы с ней обязательно встретимся."
    #Конец сцены. Игрок получает свободу действий.
    #если Эротичесских действий не было, конец сцены - вечер. если были - ночь.
    return

#мини-сцена, если Барди повторно пойдет к Бекки.
label ep04_dialogues7_work_becky_2:
    #Бекки все так же стоит у ТЦ, как и в первой сцене.
    #Сцена активируется после клика на Бекки. Барди подходит ближе к Бекки. Бекки замечает его и машет ему рукой.
    becky "О! [mcname]! Какими судьбами?"
    becky "Уже соскучился по мне, красавчик?"
    bardi "Еще бы!.. Прохожу мимо и думаю, а почему бы мне не заскочить на рандеву с этой нимфоманкой?.."
    becky "Надеюсь, ты заработал много денежек для меня. Я безумно хочу твой член!"
    # повтор меню выбора (jump ep04_dialogues7_work_becky_1_repeat)
    return
