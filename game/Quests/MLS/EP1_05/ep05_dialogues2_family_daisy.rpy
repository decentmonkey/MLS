define nicole = Character(t_("Николь"), who_color=c_orange) # дочь Дейзи - Николь

default mlsBardiFamilyDaisyCrashTest1 = 0 # Дейзи прислала Барди свои фотки
default mlsBardiFamilyDaisyCrashTest2 = 0 # Дейзи назначила краш-тест на вечер пятницы
default mlsBardiFamilyDaisyCrashTest3 = 0 # Барди пришел вечером к Дейзи на краш-тест
default mlsBardiFamilyDaisyCrashTest4 = 0 # Барди отказался от краш-теста у Дейзи

## утро субботы

# как только Барди встает с кровати (регулярный лейбл, где просыпается), ему на телефон приходит сообщение от Дейзи
label ep05_dialogues2_family_daisy_1:
    ## отрендерить 2 фото Дейзи - наподобие тех, что Барди скидывал себе на телефон в прошлом апдейте. Игрушка только одна, но ракурсы и действия разные
    ## не рендерить сам чат
    ## chat daisy
    daisy "Привет, красавчик! :)"
    menu:
        "Ответить.":
            bardi "О, Дейзи! Привет!"
            bardi "Как у тебя дела? Как бизнес?"
            daisy "Ой, все хорошо!"
            daisy "Как раз пишу тебе, чтобы похвастаться новым поступлением товара :):):):):)"
            bardi "Ну круто. И что это за товары?"
            daisy "Вряд ли их названия тебе что-то скажут..."
            daisy "Но я могу показать фотографии ;)"
            bardi "Хммм... Ну, давай."
            daisy "Ты сейчас один?"
            bardi "Да."
            daisy "Тогда держи ;)"
            # На телефон приходит две фотки Дейзи.
            bardi_t "Ну нихрена себе!.."
            bardi "Вау! Ты безумно секси!"
            daisy "У тебя встал? :)"
            bardi "Естественно!"
            daisy "Я знала. Можешь использовать мои фото, чтобы снять напряжение..."
            daisy "Ну а если об игрушке..."
            daisy "Это охрененно!"
            daisy "Материал безумно приятный для кожи."
            daisy "При этом совершенно не раздражает ее, а еще он гипоаллергенный."
            daisy "В общем, качество на высоте."
            daisy "Да и на практике показывает себя вполне достойно."
            daisy "Я кончила с ним 4 раза!"
            bardi "Я смотрю, ты там веселишься вовсю?"
            daisy "Ничего подобного! Это рабочий процесс!"
            bardi "Хах! Охрененная у тебя работа!.."
            daisy "Я знаю ;)"
            daisy "Кстати, о работе. Заходи ко мне вечером."
            daisy "У меня для тебя есть кое-какая работа."
            bardi "Окей. Отлично."
            daisy "Ладно, надеюсь, я смогла поднять тебе настроение."
            daisy "Пошла дальше работать."
            daisy "Удачи :)"
            bardi "И тебе тоже :)"
            $ mlsBardiFamilyDaisyCrashTest1 = day # Дейзи прислала Барди свои фотки
            return
        "Позже.":
            bardi_t "Позже ей напишу."
            return
    return


# в субботу днем или вечером Барди может пойти к Дейзи

# при клике на дом Дейзи днем (!)
# доступно, если Барди утром переписывался с Дейзи
label ep05_dialogues2_family_daisy_2:
    # Барди стоит у двери Дейзи
    img 901902
    menu:
        "Войти.":
            # Барди звонит в дверь
            # Дейзи открывает дверь и игриво смотрит на Барди (она в своем красном платье)
            img 901903
            w
            img 901904
            w
            img 901905
            daisy "О, привет! Ты, наконец-то, пришел поработать?"\
            img 901906
            bardi "Привет, Дейзи!"
            bardi "Да, я готов к работе."
            # Дейзи смотрит на Барди кокетливым игривым, и возбужденным взглядом.
            img 902525
            daisy "Ох, [mcname], мы же договаривались на вечер..."
            bardi_t "Фак!"
            daisy "Какой же ты нетерпеливый."
            img 902526
            bardi "А может не обязательно ждать до вечера, м?.."
            # Дейзи возбужденная чуть поднимает взгляд прикусывая губу.
            img 902527
            daisy "Ну...."
            # Дейзи разочарованная.
            img 902528
            daisy "Черт!.. Нет, [mcname]."
            daisy "К сожалению, не выйдет. У меня небольшой перерыв, после которого я должна буду работать."
            # Дейзи смотрит на Барди сочувствующим взглядом.
            img 901905
            daisy "Я не могу позволить себе отвлекаться, если хочу развивать свой бизнес."
            daisy "А пятиминутный краш-тест между делом меня не устроит."
            img 901906
            bardi_t "Твою мать!"
            # Дейзи сочувственно улыбается Барди.
            img 901905
            daisy "Давай все-таки вечером, как и договаривались..."
            img 901906
            bardi "Да, конечно. Я все понимаю."
            bardi "Удачной тебе работы."
            # Дейзи ему многообещающе подмигивает и скрывается за дверью
            img 902527
            daisy "Пока, красавчик. Приходи вечером."
            $ mlsBardiFamilyDaisyCrashTest2 = day # Дейзи назначила краш-тест на вечер пятницы
            return
        "Поработать.":
            # Барди звонит в дверь
            # Открывается дверь. Выходит Дейзи. Смотрит на Барди кокетливым игривым, и возбужденным взглядом.
            img 901903
            w
            img 901904
            w
            img 901905
            daisy "О, [mcname], ты уже пришел?"
            daisy "Но мы же договаривались на вечер... Какой же ты нетерпеливый."
            img 901906
            bardi "Да, я пришел работать."
            # Дейзи мнется (она думала, что он пришел на краш-тест, а не работать курьером)
            img 902527
            daisy "А... Я подумала, что..."
            img 902528
            daisy "Черт! Ладно, неважно..."
            img 902529
            bardi_t "Дебил! Вот я дебил!"
            bardi_t "Нахрена я это ей сказал?!"
            bardi "Но если что, мы могли бы устроить и незапланированный краш-тест..."
            # Дейзи нормальная, серьезная. указывает пальцем в дом.
            img 901905
            daisy "Нет-нет, ты прав. Дела не ждут."
            daisy "Сейчас я тебе выдам товары, которые нужно разнести в ближайшее время."
            img 901906
            bardi_t "Ну твою же мать!"
            bardi "Вас понял, босс..."
            # Дейзи снова сексуальная и игривая.
            img 902527
            daisy "Но ты не забывай обо мне... Загляни ко мне вечером..."
            bardi "Обязательно!"
            # Затемнение.
            $ mlsBardiFamilyDaisyCrashTest2 = day # Дейзи назначила краш-тест на вечер пятницы
            # переход на стандартный рабочий день курьером из прошлого апдейта
            jump ep04_dialogues4_family_daisy_2
        "Уйти.":
            img 901903
            bardi_t "Не сейчас. Займусь пока другими делами."
            return
    return

# при повторном клике на дом Дейзи днем (!), если уже было меню и кликнуть еще раз на дверь
label ep05_dialogues2_family_daisy_2a:
    ## не рендерить
    bardi_t "Дейзи просила зайти вечером..."
    return

## суббота, вечер

# при клике на дом Дейзи вечером (!)
# доступно, если Барди утром переписывался с Дейзи
label ep05_dialogues2_family_daisy_3:
    # Барди стоит у двери Дейзи, но не звонит
    img 901270
    bardi_t "Хмм... По-моему, дверь открыта..."
    bardi_t "Видимо, Дейзи ждет меня..."
    # затемнение, звук двери
    # Барди попадает в дом Дейзи, в гостиную
    # Дейзи идет через гостиную в сторону своей рабочей комнаты и не замечает Барди
    # Она идет туда, пялясь в планшет.
    img 902530
    bardi "Эй, Дейзи. Привет!"
    # Дейзи встает на месте и смотрит на Барди с улыбкой. радостная его приходу.
    img 902531
    daisy "О, [mcname]! Ты, наконец, пришел помочь мне с краш-тестом?"
    daisy "Я уже заждалась тебя. Думала уже, что ты забыл..."
    menu:
        "Как бы я мог забыть?!":
            $ mlsBardiFamilyDaisyCrashTest3 = day # Барди пришел вечером к Дейзи на краш-тест
            pass
        "Не сегодня.":
            img 902532
            bardi "Я не забыл, но..."
            img 902533
            daisy "Но?.."
            img 902534
            bardi "На самом деле, мне надо по делам... Я просто проходил мимо и зашел поздороваться."
            # Дейзи слегка разочарованная смотрит на барди.
            img 902535
            daisy "Вот как?.. Что ж, ну ладно..."
            img 902536
            bardi "Я все еще помню про краш-тест, Дейзи, и обязательно вернусь. Ты не думай, что я забыл."
            # Дейзи смотрит на Барди игривым взглядом.
            img 902537
            daisy "Только смотри, не опоздай. Я же тут сама могу все осилить и твоя помощь не понадобиться..."
            img 902538
            bardi "Не забуду, не переживай. Мне и самому это очень интересно."
            img 902533
            daisy "Тогда, я буду ждать тебя. Заходи ко мне как-нибудь вечером..."
            img 902534
            bardi "Окей. Пока, Дейзи."
            img 902534
            daisy "Пока, красавчик."
            # Дейзи исчезает в комнате.
            # Барди оказывается на улице перед ее домом
            $ mlsBardiFamilyDaisyCrashTest4 = day # Барди отказался от краш-теста у Дейзи
            ## можно вернуться только на следующий день. а при клике на дверь, оказывается что она закрыта.
            return
    img 902532
    bardi "Шутишь что ли?! Как бы я мог забыть?!"
    bardi "Работа для меня превыше всего!"
    # Дейзи смотрит на Барди смеясь.
    img 902537
    daisy "А работа ли тебя так заинтересовала?"
    img 902538
    bardi "Ну конечно!"
    bardi "Все, что запланировано на сегодня, имеет исключительно рабочий интерес!"
    # Дейзи смотрит на барди возбужденным оценивающим взглядом.
#    bardi "Ради процветания нашего дела - все что угодно!"
    #Дейзи смотрит на Барди улыбаясь.
    img 902531
    daisy "Ну и отлично. Заходи в мой рабочий кабинет, а я скоро буду..."
    bardi "Окей."
    # затемнение, шаги
    # Барди заходит в кабинет. Все то же самое. т.е диван, дилдаки на полу, дилдаки по полочкам, в коробках
    # около дивана стоит несколько не распакованных коробок дилдо.

    bardi_t "Никогда не перестану удивляться этому 'рабочему кабинету'..."
    bardi_t "Запах смазки и пота... Я словно в порностудии."
    # Барди заостряет взгляд на коробках, аккуратно сложенных у дивана.
    bardi_t "Это и есть новый товар?.."
    bardi_t "И как Дейзи успевает... Протестировать... Это все за раз?!"
    bardi_t "Охренеть!.."
    # Барди садится на диван, берет один из дилдо из коробки
    bardi_t "Хмм... Вроде обычный дилдак..."
    bardi_t "Ну-ка, а этот?.."
    # Барди достает вибратор
    bardi_t "Это просто вибратор какой-то..."
    # Барди достает какой-нибудь необычный дилдо
    Барли: "Твою мать, а это вообще что за штуковина?!"
    bardi "Ее вообще куда?.. И как?.."
    # внезапно голос Дейзи на фоне
    daisy "Может быть, потом как-нибудь покажу..."
    # Барди резко поворачивается к двери.
    # Там стоит Дейзи с подносом и двумя чашками кофе. Она смотрит на Барди сексуально улыбаясь.
    bardi "Ты уже тут?"
    daisy "А мне оставить тебя наедине?"
    bardi "Пожалуй, нет... Не надо."
    # Дейзи смеется.
    daisy "Да брось, я шучу. Вряд ли ты со всем тут разберешься."
    bardi "Это уж точно..."
    # Барди указывает пальцем на непонятный дилдо, которая был у него в руке пару мгновений назад.
    bardi "Так а что это за... Хреновина?"
    # Дейзи смотрит на Барди серьезным и уверенным взглядом, с легкой ухмылкой.
    daisy "Зря ты так. На самом деле, это очень даже удобное приспособление..."
    daisy "Да и практичное, к тому же..."
    bardi "Думаю, не для меня уж точно."
    # Дейзи смотрит на Барди с ухмылкой, словно с издевкой.
    daisy "Ты в этом уверен? Мало ли какие фетиши ты в себе можешь открыть, работая со мной..."
    bardi "Так! А ну-ка без вот этих твоих угроз!"
    # Дейзи смеется.
    daisy "Да я шучу. Расслабься, [mcname]."
    # Дейзи нейтральная смотрит на Барди.
    daisy "К слову, это все новые товары, которые я должна протестировать."
    # Дейзи чуть задирает голову. взгляд направлен на другую коробку (не ту, в которой рылся Барди)
    daisy "Думаю, вон ту коробочку тебе понравилось бы тестировать больше всего..."
    # Барди смотрит на коробку и берет из нее упаковку презервативов.
    bardi "Презервативы?"
    daisy "Именно."
    # Дейзи подходит к Барди с подносом. ставит его на одну из закрытых коробок.
    # Берет одну чашку и садится на диван. Смотрит на Барди указывая свободной рукой на поднос.
    daisy "Вон твой кофе. Бери."
    # Барди берет в руки кружку, делает глоток.
    # Дейзи сидит на диване. На бедре лежит планшет. В руке кружка, взгляд направлен в планшет.
    daisy "Сейчас разберемся с отчетностями и формальностями, а потом продолжим..."
    bardi "Выбираешь новые товары?"
    daisy "Нет. Комментарии читаю."
    # Дейзи смотрит с ухмылкой на Барди
    daisy "К слову, я смотрю, ты тот еще ловелас..."
    bardi "Что?"
    # Дейзи смотрит на барди с легким удивлением.
    daisy "Ты что, комментарии нашего магазина не читаешь?"
    bardi "Нет."
    daisy "Тогда слушай..."
    daisy "Все супер! Доставили быстро, упаковано качественно. Соседи даже если увидят, ничего не заподозрят."
    daisy "Товаром очень довольна, выполняет свои обязанности на все сто! Но есть один минус..."
    daisy "Я была очень расстроена, когда оказалось, что красавчик-курьер не идет в комплекте с товаром."
    # Барди смотрит на Дейзи. Та в свою очередь с ухмылкой смотрит на него.
    bardi "Ну нихрена себе!.."
    daisy "Хах... А теперь слушай ответы к этому комментарию."
    daisy "Да, очень жаль! Но я постеснялась спросить курьера об этом напрямую. Все-таки профессиональная этика..."
    daisy "Что? Там какой-то новый сексуальный курьер? Почему я его еще не видела?"
    daisy "Да, молоденький сексуальный мальчик. По-моему, он совсем недавно начал работать. Он тако-о-о-ой миленький!"
    daisy "Ого! Звучит многообещающе. Надо будет сделать себе заказ..."
    daisy "Вы даже не представляете, какой он хорошенький! Просто хочется взять и забрать его к себе жить!"
    daisy "Курьер, если ты это читаешь, надеюсь, ты зайдешь ко мне на чай..."
    daisy "Хмм... Если он действительно такой милашка, то его ждут хорошие чаевые. Если он, конечно, не затупит."
    daisy "Надеюсь, ты прочитаешь этот коментарий до того, как возьмешься за мой заказ. Не разочаруй мои ожидания, загадочный курьер..."
    # Барди смотри на Дейзи. Она смотрит на Барди с ухмылкой.
    bardi "Да ладно?! Серьезно?!"
    daisy "Да. Ты приглянулся некоторым клиенткам. И их количество растет."
    daisy "Некоторые клиентки даже делают повторные заказы, чтоб увидеть тебя снова... И попробовать охмурить."
    daisy "Не удивлюсь, если они скоро откроют твой фан-клуб."
    bardi "Охренеть!.. Почему я узнаю об этом только сейчас?!"
    # Дейзи откидывается на спинку дивана.
    daisy "Не знаю... Я думала, ты следишь за делами нашего интернет-магазина."
    daisy "В любом случае, благодаря тебе, дела у нас пошли в гору."
    # Дейзи поворачивается к Барди с ухмылкой.
    daisy "Смотри только не перетрахай всех моих клиенток, красавчик-курьер."
    daisy "Не хочу, чтобы у них пропал интерес к моим товарам..."
    bardi "Ахаха! Не переживай, Дейзи, вряд ли у меня это получится."
    # Дейзи смотрит на Барди оценивающим взглядом. в сексуальной позе.
    daisy "Ну смотри мне... Ловелас."
    bardi_t "Я ничего не обещаю... Меня хочет половина милф города! Да я чертов милф-хантер!"
    bardi_t "Хотелось бы одну из них сюда..."
    bardi_t "Стоп! О чем это я? Я же сейчас с Дейзи!.."
    # Барди начинает фантазироваит - пара кадров фантазии барди где Дейзи без одежды (можно тут же на диване).
    bardi_t "Дейзи такая секси..." ##->#####inc
    #####inc bardi_t "Тетя Дейзи такая секси..."
    bardi_t "Черт!.. Кажется, у меня начинает вставать..."
    # фантазия рассеивается
    # Дейзи обеспокоенная смотрит на Барди.
    daisy "Эй, [mcname], все хорошо?"
    bardi "Да, все отлично."
    # Барди смотрит на свою ширинку - у него стояк
    bardi "Так... Может, начнем уже работу?"
    # Дейзи посмеивается, или ухмыляется барди с издевкой.
    daisy "Какой же ты нетерпеливый. Это твои поклонницы так возбудили тебя?"
    bardi "Ох, нет. Это точно не поклонницы..." # смотрит на грудь Дейзи или на ноги
    # Дейзи перевозит взгляд на член Барди.
    daisy "Вижу..."
    # Дейзи смотрит на барди сексуальным взглядом.
    daisy "По правде говоря, я тоже уже вся в нетерпении..."
    daisy "Только, есть условие: работа не ждет, поэтому сначала мы проведем тест-драйв."
    daisy "Согласен?"
    menu:
        "Да, конечно.":
            pass
    bardi "Да, конечно. Тестируем презервативы?"
    # Дейзи смеется.
    daisy "Нет. Сначала 2-3 игрушки. Потом уже презервативы, малыш..."
    bardi "Окей."
    # Дейзи начинает раздеваться.
    # Затемнение.
    # Просветление.
    # Дейзи голая, обнимает Барди. Расположите их в такую позу где Барди сверху на ней (они на диване). Барди в одежде.
    img 911840
    w
    img 911839
    w
    img 911840
    bardi "Господи!.. Какая же ты секси, Дейзи." ##->#####inc
    #####inc bardi "Господи!.. Какая же у меня сексуальная тетушка..."
    # Дейзи смотрит на барди с возбужденной ухмылкой.
    img 911842
    daisy "Так! Сначала тест-драйв! Никаких ответвлений от программы!"
    img 911843
    bardi "Может, хоть немного?.."
    img 911842
    daisy "Нет! Предвкушай! Потом будет слаще."
    img 911843
    bardi_t "Твою же мать!"
    bardi "И что мы тестируем первым?"
    # Дейзи Указывает рукой наугад на коробку с дилдо.
    img 911844
    daisy "Вытащи любой из коробки."
    # Барди тянется к коробоке, берет рандомный дилдо.
    img 911845
    w
    img 911846
    bardi "Так... И как запускается твоя шайтан-машина для жесткого секса?"
    # Дейзи смотрит а него сексуальной возбужденной ухмылкой.
    img 911847
    daisy "Сегодня моя шайтан-машина для жесткого секса называется '[mcname]'."
    daisy "Придется тебе поработать ручками и порадовать свою госпожу."
    img 911848
    bardi "Да без проблем!"
    # барди лезет рукой к киске Дейзи и раздвигает ей ноги. Гладит.
    img 911849
    w
    img 911850
    w
    img 911851
    w
    img 911852
    w
    img 911855
    w
    img 911852
    w
    img 911853
    w
    img 911852
    w
    img 911853
    w
    img 911856
    daisy "Ох, [mcname], хватит уже церемониться! Вставь уже!"
    # Барди вставляет пальцы в Дейзи.
    img 911854
    w
    img 911857
    daisy "Ах!"
    daisy "Да! Вот так!"
    img 911856
    daisy "А теперь шевелись. В темпе."
    # Барди пальцами водит в киске Дейзи туда-сюда. Пока 2 пальца. Дейзи лежит расслабленно и ловит кайфы.
    img 911854
    w
    img 911858
    w
    img 911854
    w
    img 911858
    bardi_t "Какая же она секси!.. Ееее!.."
    img 911859
    w
    img 911860
    bardi_t "Фак!.. У меня в штанах уже все дымится!.."
    # Барди вставляет третий палец, и двигает пальцами в более быстром темпе.
    # Дейзи чуть красная, в наслаждении вся на расслабоне.
    img 911854
    w
    img 911861
    w
    img 911862
    w
    img 911848
    w
    img 911857
    daisy "О Боже! Как же хорошо!.."
    img 911863
    daisy "Мммм..."
    img 911864
    daisy "А у тебя офигенные пальчики, малыш..."
    img 911856
    daisy "Ты не представляешь, как это расслабляет... Ооох..."
    daisy "Как же давно у меня не было настоящего секса..."
    img 911865
    bardi_t "Твою же мать! Видимо, у меня тоже давненько уже не было."
    bardi "Дейзи, я безумно тебя хочу."
    # Дейзи хмурит брови.
    img 911866
    daisy "Так! Сначала тест-драйв! Потом уже остальное!"
    daisy "Сосредоточься, а то ничего не получишь!"
    # Дейзи снова расслаблено прикрывает глаза и кайфует
    img 911865
    daisy "Продолжай!"
    # Барди продолжает водить пальцами в киске Дейзи
    img 911867
    w
    img 911868
    daisy "Мммм..."
    img 911867
    bardi_t "Сосредоточишься тут с таким стояком!"
    img 911868
    bardi_t "Что со мной вообще творится?.."
    img 911867
    bardi_t "Я еле сдерживаюсь!.."
    # анимация
    daisy "Да, малыш..."
    daisy "Как же хорошо!.."
    # При выборе продолжать, барди дрочит Дейзи до тех пор пока игрок не кликнет по экрану.
    #после клика по экрану вновь появляется этот выбор.
    label ep05_dialogues2_family_daisy_3_loop:
    menu:
        "Продолжать.":
            # та же анимация продолжается
            daisy "Ооох!.."
            daisy "Не вздумай останавливаться, [mcname]!"
            bardi_t "И что это вообще за тест-драйв?.. Тест-драйв моих пальцев?!"
            daisy "О, дааа..."
            daisy "Ааах!.."
            jump ep05_dialogues2_family_daisy_3_loop
        "Заканчивать.":
            pass
    # Анимация останавливается
    img 911861
    bardi_t "Так! Пора заканчивать с этим."
    # Барди высовывает пальцы. Дейзи смотрит на него хмуро и удивленно.
    img 911869
    daisy "Что ты де?.."
    # Барди резко пронзает ее священным дилдосом до упора. Дейзи в афиге.
    img 911871
    daisy "Ааай!"
    img 911872
    daisy "[mcname]!"
    img 911873
    bardi "Прости, Дейзи, но мое терпение не бесконечное."
    bardi "Я так долго не продержусь. У меня член сейчас взорвется!"
    # Дейзи смотрит на Барди хмуро.
    img 911874
    daisy "Заткнись и делай что я го..."
    # Барди высовывает дилдак и снова резко вставляет его в Дейзи.
    img 911875
    w
    img 911876
    w
    img 911871
    daisy "Ах!"
    # Барди долбит Дейзи дилдо, она кайфует
    img 911877
    daisy "Ах! Дааа!"
    daisy "О Боже! [mcname]!"
    daisy "Оооо!.."
    img 911878
    bardi "Фак! Я сейчас взорвусь нахрен!.."
    daisy "О дааа!"
    daisy "[mcname]! Быстрее!"
    daisy "О да! Да!"
    img 911879
    bardi "Мать твою! Когда же ты, наконец, надрочишься?!"
    daisy "Прошу! Только не останавливайся!"
    daisy "О БОЖЕ! ДА!"
    img 911880
    bardi_t "Твою мать! Да что со мной?! Меня сейчас разорвет нахрен!"
    bardi_t "Такое чувство, как будто..."
    bardi_t "..."
    bardi_t "Так! Стоп!"
    # Барди продолжая водить дилдо в киске Дейзи, спрашивает у нее
    img 911881
    bardi "Дейзи, что было в том кофе?.."
    # она кайфует
    img 911882
    daisy "Какая... Ооох... Какая разница?.."
    daisy "О да! Как же хорошо-о-о-о!"
    img 911881
    bardi "Черт! Ты мне что-то подсыпала?!"
    daisy "Я сейчас кончу! Ооох! Дааа!"
    img 911883
    daisy "Оооо!"
    daisy "Черт тебя побери, [mcname]! ДА!"
    # Барди буквально выдергивает дилдо из Дейзи и отшвыривает его в сторону.
    img 911875
    w
    img 911876
    w
    img 911884
    bardi "Все! Хватит с тебя!"
    # Дейзи вообще в кайфах лежит приоткрыв рот и закатив глаза
    # Барди расстегивает и приспускает штаны. Вытаскивает член и надевает презерватив.
    img 911885
    w
    img 911886
    w
    img 911887
    daisy "О боже, [mcname]... Но..."
    img 911888
    daisy "Но мы еще не закончили! У нас еще много иг..."
    # затем берет Дейзи за бедра и подтягивает к себе. Дейзи приоткрывая глаза смотрит на Барди.
    img 911889
    w
    img 911890
    bardi "Тихо! Мы тестируем презервативы!"
    # Барди вставляет в Дейзи член по яйца. Дейзи опять в афиге
    img 911891
    w
    img 911892
    daisy "Ооох!"
    bardi "О да-а-а!.."
    daisy "О Боже!"
    daisy "Твой член! Он такой огромный!.."
    # в этот момент внезапно раздается звонок в дверь
    # Дейзи красная с растрепанными волосами смотрит на барди испуганно.
    daisy "!!!"
    # Барди тычет пальцем в Дейзи.
    bardi "Нет! Даже не думай открывать дверь!"
    bardi "Только не сейчас!!!"
    # снова звонок в дверь
    daisy "Но!.."
    bardi "Дейзи! Пока я не накончаю в каждый презерватив из этой пачки, тебя нет дома!"
    bardi "Сколько их там в пачке? Двенадцать? Отлично!"
    # Дейзи смотрит на барди разочарованно.
    daisy "Не выйдет, [mcname]... Извини..."
    daisy "Кажется, это моя дочь..."
    # снова звонок
    bardi "Да твою же мать!"
    # Барди встает с дивана. и стягивает презерватив.
    bardi_t "Мне сегодня дадут потрахаться или нет?!"
    # Барди с силой швыряет презерватив в стену и он остается прилипшим к стене.
    bardi_t "!!!"
    # Барди оборачивается на Дейзи. Та смотрит на барда таким сочувствующим, извинительным взглядом.
    bardi "..."
    daisy "..."
    bardi "Вот ну и чего ты смотришь?"
    bardi "Одевайся и иди открывать дверь!"
    # Затемнение.
    # Просветление.
    # Барди и Дейзи стоят в гостиной, недалеко от входной двери. Дейзи смотрит на Барди нерешительно.
    img 902539
    w
    img 902540
    daisy "Готов?"
    img 902541
    bardi "Нет. Ты подожди еще полчаса. Я в душ схожу, причешусь..."
    # Дейзи закатывает глаза. Затем опускает взгляда на член Барди.
    # и удивленно округляет глаза
    img 902542
    w
    img 902543
    daisy "Ох, [mcname]! У тебя все еще стояк!"
    img 902544
    bardi "Да ну?! Правда что ли?!"
    bardi "А я то все думаю, что же это меня так распирает и трясет?!"
    # Дейзи снова закатывает глаза и смотрит на Барди.
    img 902545
    daisy "Ну я же уже извинилась, [mcname]..."
    img 902546
    daisy "Просто я хотела протестировать виагру. И причем на себе, а не на тебе..."
    daisy "Ну, понимаешь. Это для того, чтобы записать ощущения после ее приема..."
    img 902547
    bardi "Охрененно обнадеживающая новость..."
    # Дейзи сексуально и возбужденно смотрит на Барди. Сделайте позу соответствующую.
    img 902548
    daisy "Знаешь, [mcname]?"
    daisy "Сначала я даже думала, что она работает. Я так возбудилась!.."
    daisy "По правде говоря, это было так клево!"
    daisy "Ты был такой напористый!.. Мне очень понравилось!"
    daisy "Я даже рада, что ты ее выпил, а не я..."
    # Дейзи смотрит на Барди сочувственным взглядом.
    img 902549
    bardi "Ну круто. А я то как рад!"
    bardi "Просто безумно счастлив! Обожаю, когда меня пичкают виагрой и обламывают!.."
    img 902545
    daisy "Ну прости меня уже, [mcname]..."
    # звонок в дверь
    img 902549
    bardi "Проехали. Открой уже эту чертову дверь..."
    # Дейзи открывает дверь.
    # затемнение
    # в холле у двери появляются Синтия и дочь Дейзи - Николь.
    # Николь хмуро втыкает в телефон
    # Синтия с распростертыми руками и улыбкой бежит обнимать Дейзи. Дейзи расставила руки чтоб обнять ее в ответ.
    cynthia "Тетя Дейзи!"
    daisy "Малышка Синтия! Ты тоже тут?"
    # Синтия обнимает Дейзи. Дейзи обнимает ее в ответ.
    bardi_t "Хмм... Лучше бы ты так на мой член запрыгнула и..."
    bardi_t "Фа-а-а-а-ак!"
    bardi_t "Стоп! Код красный!"
    bardi_t "Гребаная виагра!"
    # Николь втыкая в телефон, жует жвачку и надувает пузырь (если получится сделать, если нет, то без жвачки)
    nicole "Че так долго?"
    # Синтия смотрит на Барди с улыбкой. И отстраняется от Дейзи.
    cynthia "О! [mcname]! Ты тоже тут?!"
    # Николь поднимает удивленный взгляд на Барди. Дейзи смотрит на Барди чуть испуганно, тип "ОЙ ЧО СЕЙЧАС БУ-У-У-УДЕ-Е-ЕТ..."
    bardi "Да мы тут работу работаем с Дейзи..." ##->#####inc
    #####inc bardi "Да мы тут работу работаем с тетей Дейзи..."
    bardi_t "Что за бред я несу?! Мысли совсем не в ту сторону думают!"
    daisy "Мы решали кое-какие дела моего магазина..."
    daisy "[mcname] же сейчас работает на меня. Вот и помогал."
    # Взгляд николь стервозный
    nicole "Кому помогал? Себе или тебе?"
    bardi_t "Ох, фак..."
    bardi_t "Матери твоей помогал. Себе не успел, так сказать..."
    bardi_t "С какого черта вас, девочки, вообще осенила идея так рано вернуться?!"
    # Синтия смотрит на Дейзи. На лице наивная улыбка. Дейзи улыбается ей в ответ но наигранно.
    cynthia "А что вы продаете в своем магазине, тетя Дейзи?"
    daisy "Мы... Кхм... Радость продаем."
    bardi_t "Ага. Счастливые таблетки, к примеру!"
    bardi_t "Не видно что ли, как меня тут всего распирает от радости?!"
    # Дейзи указывает жестом руки на Николь. Николь смотрит на Барди оценивающим взглядом.
    daisy "Кстати, [mcname], познакомься. Это моя дочь Николь." ##->#####inc
    #####inc daisy "Кстати, [mcname], ты помнишь мою дочь Николь?"
    daisy "Николь, а это [mcname]." ##->#####inc
    #####inc daisy "Вы в детстве часто играли вместе, когда мы приходили к вам в гости."
    bardi "Приятно познакомиться..." ##->#####inc
    #####inc bardi "Привет, Николь..."
    # Николь равнодушно смотрит на Барди и снова надувает пузырь.
    nicole "Ага..."
    bardi "Ну, на самом деле мне уже пора..."
    # Синтия смотрит на барди разочарованно. Николь все так же равнодушно. Дейзи - натянутая наигранная улыбка.
    cynthia "Что? Ты уже уходишь? Ну [mcname]!"
    cynthia "А мы с Николь столько всего рассказать хотели!"
    # Дейзи встревает в диалог. Синти смотрит на Дейзи. Николь палит в телефон.
    daisy "На самом деле, да. [mcname], наверное, ужасно вымотался. Столько всего перетаскал!.."
    daisy "Да и завтра трудный день, наверное?.."
    bardi "Ага. У меня, вообще, эссе по английскому!"
    bardi_t "И рандеву с порносайтами на всю ночь."
    # Николь смотрит на Барди с ухмылкой. Синтия смотрит на Николь с непониманием.
    nicole "Должно быть, ты очень сильный. Запаха пота от тебя совсем нет."
    nicole "А вот кое-чего другого..."
    bardi_t "Фа-а-ак!"
    bardi "Коробки легкие, но их много."
    nicole "Ну-ну..."
    bardi_t "Да пошла ты!.."
    # Синтия смотрит в пол. Барди обращается к ней.
    bardi "Синтия, не переживай. Расскажешь мне все дома."
    # Дейзи подталкивает Барди к выходу. Оборачиваясь бросает что-то вслед девочкам.
    daisy "Ладно, вы, девочки, идите на кухню, а я провожу [mcname]."
    cynthia "Ну ладно..."
    cynthia "До встречи, [mcname]." ##->#####inc
    #####inc cynthia "До встречи, братик."
    bardi "Пока, Синтия. Пока, Николь."
    # Синтия улыбается Барди, а Николь демонстративно его игнорит, уткнувшись в телефон
    #Барди и Дейзи выходят на Улицу.
    # затемнение, дверь
    # на улице, у входной двери в дом Дейзи
    # Дейзи закрывает дверь и стоит опираясь о нее спиной. Изобразите это так, словно она не может вообще на ногах стоять. Смотрит на Барди испуганно.
    img 902550
    w
    img 902551
    daisy "Думаешь, они все поняли?"
    img 902552
    bardi "Синтия точно нет. Она слишком наивна и невинна для этого мира."
    bardi "А вот твоя дочь... Она явно догоняет за ситуацию."
    # Дейзи опускает голову.
    img 902553
    daisy "Черт!"
    # Дейзи смотрит на Барди игриво.
    img 902554
    daisy "Ладно, сейчас не об этом."
    daisy "Я не чувствую ног, [mcname]! Это было так охрененно!"
    daisy "С этими игрушками я уже совсем забыла, каково это трахаться с парнем!"
    # Дейзи возбужденно.
    img 902555
    daisy "Когда сильные руки непослушного мальчика силой раздвигают ножки своей госпожи и..."
    # Дейзи, прикусывая губу с и извращенной улыбкой направив взгляд вверх, словно вспоминая.
    img 902556
    bardi "Давай, мы не будем об этом говорить сейчас, а?"
    bardi "Ты, может, и не чувствуешь своих ног... Но зато я охрененно чувствую свой стояк!"
    img 902557
    bardi "Эти таблетки долго еще будут действовать?!"
    img 902558
    daisy "Всю ночь, по идее..."
    img 902557
    bardi "Фа-а-ак! И как мне по улице домой то идти?!"
    # Дейзи смотрит на Барди возбужденная.
    img 902558
    daisy "Ладно, я тебя поняла."
    # Затем прильнула к нему, прижала к стене у крыльца. Встала на колени перед ним.
    img 902559
    w
    img 902560
    bardi "ЭЙ! Что ты делаешь?!"
    bardi "Дейзи! Тут ходят люди!"
    img 902561
    daisy "Плевать. Уже темно. Нас никто тут не заметит."
    # звук молнии на ширинке
    # Дейзи вынимает член Барди из штанов. смотрит на него в афиге.
    img 902562
    daisy "Охренеть! Как только эта штука влезла в меня?!"
    bardi "Хватит болтать, Дейзи! Давай скорее!"
    # Дейзи смотрит на Барди с ухмылкой.
    img 902563
    daisy "Слушай, а может мне все-таки тебя так домой отправить?"
    daisy "Чтобы ты послушнее был в следующий раз, м?"
    img 902564
    bardi "Дейзи, не провоцируй меня..."
    img 902563
    daisy "Ладно, я тебя прощу на этот раз. Все-таки, это случилось по моей вине..."
    # Дейзи берет в руку член Барди.
    img 902565
    daisy "Боже! Да он же как из камня!.."
    img 902566
    daisy "Нужно будет записать это в описании товара..."

    bardi "Да твою же мать!.."
    # Барди берет руками Дейзи за затылок и заталкивает ей в рот член. Дейзи в афиге. Руки в ладонях раскрыты на уровне плеч.
    daisy "Мммммм...."
    # Включается анимация (если она тут будет) как Барди толкается членом Дейзи в рот. (Именно Барди. Не она сама двигает головой) Дейзи держится руками за его бедра. Анимация идет быстро.
    bardi "Какого черта ты вообще решила!.."
    bardi "Проверять эти гребаные таблетки!.."
    bardi "Вот и отдувайся теперь!"
    daisy "Мпфхф!.."
    # У Дейзи закатываются глаза в анимации. Барди продолжает ее долбить.
    bardi "Ну вот нахрена надо было так делать?.."
    bardi "Если ты знала, что твоя дочь скоро придет?!"
    # Конец анимации.
    # Дейзи с силой отталкивается от Барди. Вдыхает свежий воздух.
    daisy "Я же так задохнусь!"
    # Барди вновь притягивает ее голову к себе и заталкивает ей член в горло
    bardi "Ну вот подышала и хватит!.."
    bardi "Мммм... Как же я долго этого ждал!"
    bardi "Весь сегодняшний вечер!"
    bardi "Под этими гребаными таблетками!.."
    # Барди кончает
    bardi "Дааа!"
    bardi "АААААА!!!"
    # Барди высовывает член, Дейзи падает на четвереньки.
    # Вытирая рот рукой смотрит на Барди.
    daisy "Кх... Кх..."
    daisy "Ты что творишь?! Кх..."
    daisy "Я же чуть не задохнулась!"
    bardi "Это меньшее, что тебя ждет при нашей следующей встрече!"
    bardi "Я накачаю тебя этими таблетками и заставлю скакать на моем члене всю ночь!.."
    # Дейзи смотрит пристально.
    daisy "Что ж я..."
    # внезапно на ее лице многообещающая улыбка
    daisy "Я буду ждать..."
    # Барди разворачивается и уходит.
    return

# при повторном клике на дом Дейзи вечером (!), если Барди ответил ей "не сегодня" и игрок хочет вернуться к ней
label ep05_dialogues2_family_daisy_3a:
    ## не рендерить
    bardi_t "Вот я идиот! И зачем я ей так ответил?.."
    bardi_t "Это мог бы быть просто улетный вечер!"
    bardi_t "Ладно... Дейзи сказала, что будет ждать меня."
    bardi_t "Нужно будет прийти сюда как-нибудь вечером..."
    return

## суббота, вечер
## Барди идет домой, дома отыгрывают регулярные лейблы

# после того, как Барди придет домой и кликнет на свою комнату
label ep05_dialogues2_family_daisy_4:
    # Барди в своей комнате. Падает на кровать.
    bardi "Господи! Что за вечер?!"
    # На телефон Барди приходит уведомление.
    bardi "Это еще, мать его, кто?.."
    # Сообщение от Дейзи. Барди открывает чат с ней. Содержимое чата ниже.
    ## chat daisy
    ## не рендерить
    daisy "[mcname], прости за эти таблетки. Как ты?"
    bardi "Нормально... Ты сама то как?"
    daisy "Ох, лучше некуда. Только устала как собака..."
    bardi_t "Это она то устала?! Мне бы так уставать!"
    bardi "Понимаю..."
    daisy "В общем, прости за таблетки. И за то, что все так вышло..."
    daisy "Я не знала, что девочки вернутся так рано."
    daisy "Николь говорила, что они будут гулять допоздна..."
    bardi "Все окей, Дейзи."
    bardi "Но то, что я пообещал тебе перед уходом, так все и будет."
    daisy "Будто я против ;)"
    daisy "Когда все лягут спать, я скину тебе кое-что особенное. Так что жди :)"
    bardi "Окей. Жду :)"
    # Барди откладывает телефон и ложится спать.
    bardi_t "Чтобы потом снова мучатся со стояком? Ну его нахрен."
    bardi_t "Я спать."
    # затемнение
    return

## воскресенье, утро

# утром в телефоне Барди непрочитанное сообщение от Дейзи.
label ep05_dialogues2_family_daisy_5:
    ## отрендерить 5-7 фото Дейзи - эротических фотографий (не откровенная порнуха с дилдаками). Сделайте несколько поз и фоток от менее эротических к более эротическим (изобразите ее в процессе раздевания).
    ## не рендерить сам чат
    ## chat daisy
    daisy "Привет, красавчик. Я снова тут ;)"
    daisy "Как и обещала, кидаю тебе несколько фоток, чтобы снять напряжение :)"
    # Далее в чате одна за другой ее фотки
    bardi_t "Мдаа... Веселая же была ночка..."
    # Барди отправляет Дейзи
    bardi "Фотки огонь!"
    bardi "Ты такая секси! ;)"
    # и закрывает чат
    return

# пока у Барди есть какой-нибудь не прочитанный чат с новыми фотками Дейзи, она не будет ему писать и присылать новые фотки
# Это должно быть всегда. Т.е если у барди есть непросмотренный чат с Дейзи, он не может приступить к следующей сцене с ней
