define whore = Character(_("Проститутка"), who_color=c_pink) # проститутка
define unknown = Character(_("Неизвестный"), who_color=c_orange) # нежданный гость Шона

default mlsBardiSeanDay3Whore1 = 0 # Барди назвал шлюху миссис Кларк
default mlsBardiSeanDay3Whore2 = 0 # Барди назвал шлюху миссис Адамс

# при клике на локацию Дом Шона
# мысли перед его домом
label ep02_dialogues3_sean_1:
    # мысли, не рендерить!!
    # если была переписка с Шоном до колледжа
    bardi_t "Какие там за важные дела у Шона?"
    bardi_t "Что он даже на колледж забил сегодня?"
    # если переписки утром не было
    bardi_t "По-моему, Шона сегодня не было в колледже."
    bardi_t "Может, у него что-то случилось?"
    return

# клик на дом Шона
label ep02_dialogues3_sean_2:
    # Барди поднимается на крыльцо, стучит в дверь, но ему не открывает никто
    img 900526
    bardi_t "Никого нет что-ли?"
    # снова стучит, но безрезультатно
    bardi_t "Позвоню ему..."
    # Барди берет в руки телефон, тыкает пальцем в экран и прикладывает телефон к уху
    # идут длинные гудки, потом резко короткие - Шон сбросил звонок
    # Барди смотрит в телефон
    img 900527
    bardi_t "???"
    # в этот момент открывается дверь и на пороге возникает Шон с озабоченным видом
    img 900528
    w
    img 900530
    bardi "О, чувак! А я тебе..."
    img 900529
    w
    img 900531
    sean "Тсс! Тихо!"
    # Шон нервно смотрит по сторонам, потом говорит
    img 900532
    sean "Заходи быстрее!.."
    # скрывается в дверях
    # смена кадра
    # гостиная в доме Шона
    img 900533
    w
    img 900534
    bardi "Эй, у тебя все в порядке, Шон?"
    img 900535
    sean "Да, все окей."
    # Шон бросает взгляд в сторону своей комнаты, потом снова смотрит на Барди
    img 900536
    sean "У меня просто дела."
    img 900537
    bardi "Может, я могу чем-то помочь?.."
    # в этот момент раздается звонок в дверь
    img 900538
    sean "Черт!"
    sean "Я сейчас, бро. Подожди меня здесь."
    img 900539
    # Шон выходит из гостиной
    # со стороны входной двери раздаются голоса
    img 900540
    unknown "Я эту огромную вазу не могу поднять. У меня сил не хватает. Она почти с меня ростом, представляешь?"
    unknown "Или я ее уроню на пол и разобью... А эта ваза стоит больше, чем весь ваш дом..."
    unknown "Или на себя уроню и все свои старые кости к чертям переломаю. Ну ладно хоть ваза при этом цела останется..."
    unknown "Но если ты мне поможешь, по-соседски, я тебе подкину деньжат немного."
    unknown "Пошли, Шон, поможешь старушке-соседке. Я уже задолбалась с этой вазой возиться."
    sean "Да, конечно. Без проблем."
    img 900535
    sean "Эй, бро!"
    img 900537
    bardi "Что?"
    img 900541
    sean "Я ненадолго отлучусь помочь соседке. Подожди меня."
    img 900537
    bardi "Окей."
    img 900540
    unknown "И, кстати, там кроме вазы есть еще одна старинная вещь..."
    # звук закрывающейся двери
    # Барди остается один
    # переход на движок
    return

# при клике на выход из дома Шона
label ep02_dialogues3_sean_2a:
    # мысли, не рендерить!!
    bardi_t "Нужно дождаться Шона."
    bardi_t "Он как-то странно себя ведет. Вдруг ему нужна моя помощь?"
    return

# при клике на телек в гостиной
label ep02_dialogues3_sean_2b:
    # мысли, не рендерить!!
    bardi_t "Не хочу смотреть телек..."
    return

# при клике на кухню
label ep02_dialogues3_sean_2c:
    # мысли, не рендерить!!
    bardi_t "Там кухня. Наверняка, ничего интересного."
    return

# при клике на лестницу, ведущую к комнате Шона
label ep02_dialogues3_sean_2d:
    # мысли, не рендерить!!
    bardi_t "Сколько еще ждать Шона?.."
    bardi_t "Мне еще нужно успеть домой к ужину."
    bardi_t "..."
    bardi_t "По-моему, в прошлый раз я видел мяч в комнате Шона..."
    bardi_t "Хоть чем-то заняться, пока жду его."
    # Барди идет к лестнице
    # затемнение, шаги
    return

# комната Шона
label ep02_dialogues3_sean_3:
    # Барди заходи в комнату Шона
    img 900542
    bardi_t "Он же не будет против, что я возьму его мяч..."
    # внезапно к нему подлетает шлюха с завязанными глазами (повязка на глаза у нас есть в сцене админ-Виктория-Моника)
    # кожанку и пояс от чулков со шлюхи нужно будет сразу снять, оставить только топ-сетку, юбку и сапоги
    # она радостная, что она пришел (думает, что это Шон)
    img 900543
    w
    img 900544
    whore "Ну наконец-то ты вернулся!"
    img 900545
    whore "Твоя Бекки тебя заждалась!"
    img 900554
    bardi_t "?!?!"
    # она берет его за руку
    img 900546
    whore "Зачем ты так надолго меня оставил одну?"
    # Барди в ступоре молчит
    img 900547
    bardi_t "..."
    bardi_t "Кто это?!"
    img 900548
    bardi_t "И что она здесь делает?!"
    img 900549
    bardi_t "Вот черт! Неужели, это та тетка, которая была на фотке у Шона?!"
    img 900546
    whore "Шалунишка ведь хочет поиграть с Бекки?"
    img 900547
    bardi_t "Она что, приняла меня за Шона?.."
    bardi_t "Твою мать! Что теперь делать?!"
    bardi_t "Притвориться, что я Шон?.."
    img 900550
    whore "Бекки так любит игры..."
    # она прикладывает руку Барди к своей груди
    img 900551
    whore "В какую игру ты хочешь поиграть, м?"
    bardi "Эммм... Я..."
    # шлюха настораживается, но рука Барди так же у нее на груди
    img 900552
    whore "У тебя странный голос..."
    img 900553
    bardi_t "Черт с ним! Притворюсь Шоном!"
    bardi_t "Будет еще хуже, если она поймет, что это кто-то другой. Тогда я подставлю Шона..."
    # Барди кашляет
    img 900555
    bardi "Кхе-кхе!.. Кхм..."
    # Барди кладет вторую руку на ее вторую грудь
    img 900556
    bardi "Просто я... Я так возбужден, что аж голос охрип..."
    # она воодушевленно выпячивает грудь навстречу его рукам
    img 900557
    w
    img 900558
    whore "Хи-хи. Бекки такая, да."
    img 900559
    bardi_t "У нее такая грудь... Она даже не помещается в мои ладони..."
    bardi_t "Черт! Когда я последний раз трахался?.."
    bardi_t "Я даже вспомнить не могу!.."
    bardi_t "Охренеть!"
    # шлюха тем временем кладет руку на его ширинку, там уже стояк
    img 900560
    whore "Ох, я вижу, что ты очень-очень хочешь Бекки!"
    img 900561
    # она начинает водить рукой по его стояку
    img 900556
    bardi "Да..." # мнет ее грудь
    img 900562
    bardi_t "Хочу! Шон меня убьет, но я хочу трахнуть ее!.."
    img 900556
    bardi_t "Это же просто шлюха..."
    img 900562
    w
    img 900556
    w
    img 900558
    whore "У меня идея!"
    whore "Давай поиграем в мою любимую игру - преподаватель и студент?"
    img 900563
    bardi "Я не против..."
    img 900564
    whore "Я знала, что тебе понравится моя идея! Хи-хи-хи."
    # она отстраняется от него, снимает свой топ и бросает его на пол (остается только в юбке и сапогах)
    img 900565
    w
    img 900566
    w
    img 900567
    bardi_t "Твою мать, какие же клевые сиськи у этой шлюхи!.."
    # Барди кладет руки на ее голую грудь
    img 900568
    bardi_t "Да, я определенно ее сейчас трахну..."
    # щипает за сосок, оттягивает его
    img 900569
    w
    img 900572
    w
    img 900573
    w
    img 900570
    whore "Как ты будешь меня называть?"
    whore "Я могу быть кем угодно, только скажи..."
    img 900571
    bardi "..." # руки также на груди
    # сцена минета в пунктах меню одна и та же. там, где нет лиц училок - использовать одинаковые арты
    menu:
        "Миссис Кларк.": # математичка
            $ mlsBardiSeanDay3Whore1 = day # Барди назвал шлюху миссис Кларк
            img 900574
            bardi "Ты будешь миссис Кларк."
            img 900575
            whore "Да, я сегодня буду миссис Кларк, хи-хи."
            # она достает его член и водит по нему рукой
            img 900576
            w
            img 900577
            w
            img 900578
            w
            img 900579
            w
            img 900580
            w
            img 900581
            w
            img 900575
            whore "А какой предмет я преподаю в колледже?"
            img 900574
            bardi "Гребаную математику..."
            # она хихикает и встает на колени перед Барди
<<<<<<< Updated upstream

            whore "Миссис Кларк хочет похвалить тебя, студент..."
=======
            img 900582
            w
            img 900583
            whore "Миссис Кларк хочет похвалить тебя, шалунишка..."
>>>>>>> Stashed changes
            whore "Ты показываешь высокую успеваемость по математике."
            # проводит языком по головке члена
            img 900584
            bardi "Мммм..."
            img 900585
            w
            img 900586
            w
            img 900583
            whore "Миссис Кларк любит таких хороших студентов."
            whore "И готова вознаграждать их хорошим минетом после занятий."
            # облизывает головку и вбирает член в себя
            img 900584
            w
            img 900585
            w

            whore "Мпфх!.."
            # вытаскивает и, удерживая член рукой, шлепает себя по губам
            # на несколько кадров, лицо шлюхи в повязке сменяется на лицо Кларк в повязке
            teacher_clark "Миссис Кларк просто обожает..."
            teacher_clark "Отсасывать у своих студентов после математики."
            # снова резко и глубоко вбирает в себя член
            bardi "Оооох..."
            bardi "Даа!.."
            # лицо шлюхи возвращается
            whore "Мпфх!.."
            whore "Мммм..."
            # шлюха вытаскивает член изо рта
            whore "Тебе нравится, как усердно тебя благодарит миссис Кларк?"
            bardi "Да..."
            bardi "Но хотелось бы большей благодарности, миссис Кларк."
            # она облизывает член и пошло улыбается
            ## можено убрать это слово под юбкой, так как юбку она сняла
            whore "Миссис Кларк любит, когда наглые студенты трогают ее под юбкой..."
            # Барди хватает шлюху за руку и поднимает на ноги
            bardi "А может, вы любите пожестче, миссис Кларк?"
            # смена лица на Кларк
            teacher_clark "Обожаю..."
            teacher_clark "Трахни меня скорее, студент!.."
            # смена лица обратно на шлюху
            whore "Давай быстрее, мне не терпится!"
            # Барди ставит ее к стене у кровати (либо нагибает над кроватью)
            # задирает юбку (она без трусиков) и шлепает по попе
            bardi "А вот так вам нравится, миссис Кларк?"
            whore "О, да!.."
            # снова шлепает
            whore "Ооо!.."
            # напрявляет член на киску и входит
            bardi "Ееее!.."
            whore "Оооох!.."
            # шлепок по попе и начинает ее ахать
            # во время секса можно показать лицо Кларк еще раз, не показывая полностью голого тела (типа Барди себе представляет ее вместо шлюхи)
            whore "Оооо!"
            whore "Какой у тебя клевый член!.."
            bardi "Мммм..."
            whore "Даа!.. Как же кайфово!"
            bardi "Чертовски охренительно трахать вас, миссис Кларк!.."
            whore "Аааа!"
            whore "Оттрахай миссис Кларк, студент! Оттрахай как следует!"
            bardi "О, ееее!.."
            whore "Миссис Кларк сейчас кончит!"
            # шлюха кончает
            whore "ААААА!"
            whore "АААААААА!!!"
            bardi "О, дааа!!!"
            menu:
                "Кончить в нее.":
                    # Барди бурно кончает в нее
                    bardi "Дааа!!!"
                    bardi "Оооо!!!"
                    bardi "О, какой кайф..."
                    pass
                "Кончить на нее.":
                    # Барди бурно кончает на нее
                    bardi "Дааа!!!"
                    bardi "Оооо!!!"
                    bardi "О, какой кайф..."
                    pass
            # дверь в комнату Шона резко открывается и он в кипише влетает внутрь
            sean "Бро! Твою мать!"
            sean "Моя мама домой пришла! Убегайте! Быстро!"
            bardi "Фак!.."
            # он подбегает к Барди и шлюхе и подталкивает их к окну
            pass
        "Миссис Адамс.": # препод по инглишу
            $ mlsBardiSeanDay3Whore2 = day # Барди назвал шлюху миссис Адамс - минет + cowgirl
            img 900574
            bardi "Ты будешь миссис Адамс."
            img 900575
            whore "Да, я сегодня буду миссис Адамс, хи-хи."
            img 900576
            w
            img 900577
            w
            img 900578
            w
            img 900579
            # она достает его член и водит по нему рукой
            img 900580
            w
            img 900581
            w
            img 900575
            whore "А какой предмет я преподаю в колледже?"
            img 900574
            bardi "Английский и литературу..."
            # она хихикает и встает на колени перед Барди
            img 900582
            w
            img 900583
            whore "Миссис Адамс хочет пошалить немного со своим студентом..."
            whore "Прямо в кабинете английского языка. Пока никто их не видит."
            # проводит языком по головке члена
            img 900584
            bardi "Мммм..."
            img 900585
            w
            img 900586
            w
            img 900583
            whore "Миссис Адамс любит шалить после занятий в колледже."
            whore "Прямо на рабочем месте..."
            # облизывает головку и вбирает член в себя
            img 900584
            w
            img 900585
            w

            whore "Мпфх!.."
            # вытаскивает и, удерживая член рукой, шлепает себя по губам
            # на несколько кадров, лицо шлюхи в повязке сменяется на лицо Кларк в повязке
            teacher_adams "Миссис Адамс просто обожает..."
            teacher_adams "Отсасывать у своих студентов после английского."
            # снова резко и глубоко вбирает в себя член
            bardi "Оооох..."
            bardi "Даа!.."
            # лицо шлюхи возвращается
            whore "Мпфх!.."
            whore "Мммм..."
            # шлюха вытаскивает член изо рта
            whore "Тебе нравится, как усердно миссис Адамс отсасывает у тебя?"
            bardi "Да..."
            whore "Тебе хотелось бы большего, м?.."
            bardi "Да..."
            # она облизывает член и пошло улыбается
            whore "Миссис Адамс любит, когда наглые студенты трогают ее под юбкой..."
            # она поднимается на ноги и толкает Барди на кровать
            # смена лица на Кларк
            teacher_adams "И еще я просто обожаю, когда член заполняет всю мою киску."
            teacher_adams "Хочу скорее трахнуть тебя, студент!.."
            # смена лица обратно на шлюху
            bardi "Приступайте, миссис Адамс."
            # она снимает юбку (она без трусиков)
            whore "О, да!.."
            whore "Сейчас ты увидишь, какой шалуньей может быть миссис Адамс!"
            # она лезет на него
            whore "Мммм!.."
            # берет его член в руку и напрявляет на свою киску, вводит
            bardi "Ееее!.."
            whore "Оооох!.."
            # он шлепает ее по попе и она начинает скакать на нем
            # во время секса можно показать лицо Адамс еще раз, не показывая полностью голого тела (типа Барди себе представляет ее вместо шлюхи)
            whore "Оооо!"
            whore "Какой у тебя клевый член!.."
            bardi "Мммм..."
            whore "Даа!.. Как же кайфово!"
            bardi "Чертовски охренительно трахать вас, миссис Адамс!.."
            whore "Аааа!"
            whore "Оттрахай миссис Адамс, студент! Оттрахай как следует!"
            bardi "О, ееее!.."
            whore "Миссис Адамс сейчас кончит!"
            # шлюха кончает
            whore "ААААА!"
            whore "АААААААА!!!"
            bardi "О, дааа!!!"
            menu:
                "Кончить в нее.":
                    # Барди бурно кончает в нее
                    bardi "Дааа!!!"
                    bardi "Оооо!!!"
                    bardi "О, какой кайф..."
                    pass
                "Кончить на нее.":
                    # Барди бурно кончает на нее
                    bardi "Дааа!!!"
                    bardi "Оооо!!!"
                    bardi "О, какой кайф..."
                    pass
            # дверь в комнату Шона резко открывается и он в кипише влетает внутрь
            sean "Бро! Твою мать!"
            sean "Моя мама домой пришла! Убегайте! Быстро!"
            # Барди и шлюха вскакивают с кровати
            bardi "Фак!.."
            # Шон подбегает к ним и подталкивает их к окну
            pass
    sean "Быстро убегайте!"
    # Барди хватает одежду, а Шон впихивает одежду шлюхи ей в руки
    sean "Мать меня убьет, если увидит что здесь происходит!"
    bardi "Как мы убежим, чувак?!"
    bardi "Твоя мама внизу?"
    sean "Да! Она поднимается сюда!"
    whore "Шон? С кем ты разговариваешь?"
    # Шон нетерпеливо отмахивается от нее
    sean "Некогда! Все потом!"
    sean "Сваливайте быстрее! Мне будет конец, если мама увидит ЭТО!"
    whore "Что происходит?"
    sean "Давайте в окно!"
    bardi "В окно?!"
    whore "Эй! Какое окно?! Вы чего, совсем сдурели?!"
    # она хватается за маску
    whore "Чертова маска!.."
    # в это время голос из-за двери и стук, шлюха застывает, не сняв маску
    bardie_friend_mother "ШОН?"
    bardie_friend_mother "Почему у тебя закрыта дверь?!"
    bardie_friend_mother "Открой дверь, Шон! Что там у тебя происходит?!"
    # стук
    # Шон подталкивает к окну сначала Барди (показываем как Барди забирается на подоконник)
    # и берет за руку шлюху, притягивая ее к себе, та до сих пор не сняла свою повязку
    bardi "!!!"
    sean "Да быстрее же!!!"
    bardi "!!!!!"
    # затемнение
    # Барди со шлюхой стоят на улице под окном Шона (на улице уже вечер)
    # сверху доносится голос Шона
    sean "Вы целы, чувак?"
    bardi "Да, все в порядке."
    sean "Окей. Тогда до связи. Пока."
    bardi "Пока, Шон."
    # Барди смотрит на шлюху
    # шлюха подносит руку к повязке
    bardi_t "Если она сейчас снимает свою дурацкую повязку..."
    bardi_t "Она поймет, что трахалась не с Шоном."
    whore "Эта гребаная повязка меня уже достала!.."
    # шлюха снимает повязку и удивленно смотрит на Барди
    # начинает одеваться
    whore "?!?!"
    bardi "..."
    whore "Ты кто такой вообще?!"
    whore "Где Шон?"
    whore "Какого хрена мы вышли в окно? Что блин происходит?!"
    bardi "Эй, Бекки. Без паники."
    bardi "Я [mcname], друг Шона."
    whore "Друг?!"
    whore "Он что, притащил меня сюда для тебя?"
    bardi "Нуу..."
    whore "Ну вы вообще, парни!.."
    whore "Я и так отработала бы с тобой. Зачем нужен был весь этот цирк?"
    whore "А что случилось то? Кто пришел и зачем мы убегали?"
    whore "Я вообще ничего не поняла."
    whore "И что это за место?" # оглядывается
    whore "Это дом Шона что-ли?!"
    bardi "Эээ..."
    whore "Этот придурок заставил меня нацепить дурацкую повязку..."
    whore "Чтобы я не поняла, что он притащил меня к себе домой?!"
    bardi "Это дом... Дом одного приятеля..."
    bardi "В общем, неважно."
    # Бекки достает сигарету и закуривает
    whore "Ну неважно, так неважно."
    whore "Блин, весь кайф обломали!"
    whore "В кои то веки кончила при трахе с клиентом, а тут такая хрень с выходом через окно..."
    bardi "Обычно не кончаешь?"
    whore "Обычно я хорошо притворяюсь."
    whore "Но с тобой я кайфанула... Как ты говоришь твое имя?"
    bardi "[mcname]."
    whore "Вот и познакомились, ха-ха..."
    label ep02_dialogues3_sean_loop1:
    bardi "..."
    menu:
        "Сколько Шон тебе заплатил?":
            bardi "Бекки, а сколько Шон тебе заплатил за сегодняшнюю встречу?"
            whore "У нас с этим мелким свои дела..."
            bardi "То есть?"
            # он подмигивает Барди
            whore "Не вникай, красавчик."
            jump ep02_dialogues3_sean_loop1
        "Дашь свой номер телефона?":
            bardi "Если я захочу с тобой провести время..."
            whore "Без проблем."
            whore "Вот мой номер телефона." # новый контакт в телефоне Барди
            whore "Напишешь мне, как надумаешь..."
            jump ep02_dialogues3_sean_loop1
        "Уйти.":
            # Бекки бросает докуренную сигарету на землю
            whore "Ну что, студент. Мне пора. Время - деньги."
            whore "Хорошо потрахались, да?"
            bardi "Да. Было прикольно."
            whore "Пиши, когда захочешь повторить, красавчик."
            whore "Пока."
            # шлюха уходит
            pass
    # Барди смотрит ей вслед
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
label ep02_dialogues3_sean_5a:
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
