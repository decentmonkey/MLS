define client_sexshop = Character(t_("Клиентка"), who_color=c_pink) # клиентка при работе курьером у Дейзи
define client_carrie = Character(t_("Кэрри"), who_color=c_pink) # клиентка Кэрри

default mlsBardiWorkDaisyClientCarrie1 = 0 # Барди отказался заходить в дом клиентки
default mlsBardiWorkDaisyClientCarrie2 = 0 # у Барди был секс с клиенткой магазина Дейзи

# воскресенье, утро

# Сцены курьера (Не конкретно эта а в принципе все) открываются только тогда, когда Барди посмотрел комментарии в интернет магазине и увидел что его там уже медленно возводят в культ.
# Там будут сцены, по большей части с милфами. Примерно ровесницы самой Дейзи.
# В данном апдейте выйдет только одна сцена, т.к, как я и написал, количество сцен курьера на прямую зависит от развития отношений с Дейзи и развития интернет магазина.

# за 1 день, доступна лишь одна сцена курьера
# сцена доступна лишь в том случае, если Барди был у Дейзи дома и согласился на краш-тест (mlsBardiFamilyDaisyCrashTest3 > 0)

# мысли в воскресенье утром, когда Барди еще дома и собирается выйти в город
label ep05_dialogues3_work_daisy_1:
    ## не рендерить!
    bardi_t "Итак, сегодня в колледже выходной и у меня впереди целый день..."
    bardi_t "Я могу сегодня заработать кучу бабок..."
    bardi_t "А не тратить свое время на бесполезные занятия в этой шараге..."
    menu:
        "Пойти работать у Дейзи.":
            bardi_t "Хмм... Работа в прокате может принести больше денег..."
            bardi_t "Но я ведь не могу оставить без внимания клиенток магазина Дейзи, верно?"
            bardi_t "Тем более, после того, как я ознакомился с их комментариями..."
            # Барди перекидывает к дому Дейзи
            pass
        "Поработать в велопрокате.":
            bardi_t "Отличный денек, чтобы продуктивно поработать в прокате у Райта..."
            bardi_t "Сегодня от клиентов не должно быть отбоя."
            # квест-лог "Идти в велопрокат."
            pass
    return

# дом Дези
label ep05_dialogues3_work_daisy_2:
    # Барди стоит у двери Дейзи и звонит в дверь
    # Открывается дверь. Выходит Дейзи. игриво улыбается ему
    daisy "Неожиданно."
    daisy "Привет, [mcname]."
    bardi "Привет."
    daisy "Тебе так понравились мои ночные фотки, что ты не удержался и пришел?"
    daisy "Краш-тесты могут быть только по вечерам..."
    daisy "И только по предварительной договоренности..."
    bardi "Да-да, я помню, что только по вечерам."
    bardi "Но твои фотки - это что-то!"
    bardi "Надеюсь, ты мне скинешь еще что-нибудь? Твои рабочие будни, например..."
    daisy "Ха-ха! Ты не только нетерпеливый и непослушный мальчик. Ты еще, оказывается, и ненасытный..."
    bardi "Ну... Есть такое дело..."
    daisy "Хорошо, [mcname]. Как будет что-то подходящее, я отправлю тебе фото..."
    bardi "Отлично! Буду ждать."
    bardi "А еще, я хотел узнать..."
    bardi "У меня сегодня выходной в колледже и я решил немного поработать."
    bardi "Может, есть какие-нибудь заказы?"
    # Дейзи улыбается
    daisy "Заказов целая гора!"
    daisy "Впрочем, как и комментариев о моем сексуальном курьере..."
    daisy "Сейчас я тебе выдам товары, которые нужно разнести в ближайшее время."
    bardi "Вас понял, босс..."
    # Дейзи подмигивает ему и скрывается за дверью
    # Затемнение, шуршание пакетов.
    # переход на след. лейбл
    return

# Барди приходит к дверям одного из домов клиента (HOUSE_FOREIGNTEACHER -?)
# нам понадобится в доме максимум 3 комнаты, это кухня, гостиная, и может быть спальная в будущем
label ep05_dialogues3_work_daisy_3:
    # В руках Барди коробка (можно пакет) и планшет с документом для подписи клиента (или просто лист, текст на листе не показываем)
    bardi_t "Какое-то знакомое место... Разве я сюда уже не доставлял заказ?"
    # Барди смотрит в планшет, чтоб сверить адрес, после чего на следующем рендере убирает планшет обратно.
    bardi_t "Адрес вроде верный..."
    bardi_t "Хммм... А вдруг это какая-нибудь милфочка из моего фан-клуба?"
    bardi_t "Ну или просто девушка, решившая купить что-то еще?.."
    bardi_t "Эх, [mcname]... Не стоит тебе питать ложных надежд..."
    # Барди подходит к двери и на следующем рендере звонит в звонок.
    # Звук звонка.
    # Дверь открывается. За дверью показывается секси милфочка, возрастом примерно с Дейзи.
    # Она стоит в сексуальной позе облокотившись о дверной косяк. observing-? акцентировав внимание на груди.
    bardi_t "Вау! Мадам! Вам нахрена эти игрушки?!"
    bardi_t "Пойди да подцепи себе любого мужика!"
    # клиентка игриво улыбается Барди
    client_sexshop "И снова здравствуй, красавчик."
    bardi "Здрасьте..."
    bardi_t "Ну точно! Я знал, что уже был здесь!"
    # Женщина от дверного косяка отстранилась.
    # Стоит прямо, скрестив руки. лицо такое... Игриво вопросительное. Будто ты спрашиваешь то, на что уже знаешь ответ.
    # Она считает что барди ошеломлен ее внешним видом, поэтому в дальнейшем она вся из себя довольная и раскованная. Как победитель.
    client_sexshop "Все в порядке?"
    bardi "Да... Просто место было знакомое... А сейчас я вспомнил, что точно был уже здесь."
    # Барди смотрит на планшет чтоб проверить имя.
    bardi "Вы же мисс Кэрри?"
    bardi_t "Точно! Я помню ее."
    bardi_t "Правда, в прошлый раз она выглядела намного проще... Может, она куда-то собирается?"
    # Барди смотрит на Кэрри. Кэрри наигранно обиженная.
    client_carrie "Оу... А я надеялась, ты запомнил мое имя, [mcname]..."
    bardi_t "Ох, даже так? Да ты попробуй запомнить! В прошлый раз ты выглядела куда скромнее!"
    bardi "Так я и не забывал. Просто сверился с документом."
    bardi "Вдруг у вас есть сестра-близнец с таким же именем?.."
    # Кэрри с ухмылкой.
    client_carrie "Да-да... Отмазывайся."
    bardi "Ладно, прошу прощения, мисс Кэрри."
    bardi "В следующий раз я точно не забуду ваше имя."
    bardi "Если, конечно, этот инцидент вас не сильно огорчил, и следующий раз произойдет."
    # Кэрри заигрываючи подмигивает.
    client_carrie "Ох... Все зависит от тебя. Исправляйся."
    bardi "Хах... Конечно."
    # Кэрри нейтральная, только легкая улыбка.
    client_carrie "Да, я Кэрри."
    # Барди протягивает посылку Кэрри.
    bardi "Значит, это для вас!"
    # Кэрри берет посылку с рук Барди.
    client_carrie "О, отлично!"
    bardi "Итак... Посылка уже оплачена, доставлена из рук в руки, как и просили. Верно?"
    client_carrie "Да..."
    # Барди протягивает Кэрри планшет (лист)
    bardi "Тогда распишитесь, пожалуйста, мисс Кэрри."
    # Кэрри в ответ лишь машет рукой с пофигистическим выражением лица.
    client_carrie "Да, я все помню."
    client_carrie "Но я хочу проверить соответствие товара с фотографией на сайте."
    client_carrie "Если все соответствует - подпишу. Хорошо?"
    bardi "Да, конечно..."
    client_carrie "Но я не хочу делать это на улице, на глазах у всех."
    client_carrie "Заходи в дом, не будешь же ты ждать тут."
    # Кэрри отходит в сторону пропуская Барди в дом.
    # Барди пока остается на месте, не заходит. она выжидательно смотрит на него
    bardi_t "Хмм... В прошлый раз она не показалась мне такой уж..."
    bardi_t "Тааак... Стоп!"
    bardi_t "Что это у нас тут намечается?.. Да и есть ли у меня на это время?.."
    menu:
        "Нет. Мне надо спешить.": # + Rabbit
            ## возможность повтора сцены, если отказал в этот раз - ep05_dialogues3_work_daisy_4
            $ mlsBardiWorkDaisyClientCarrie1 = day # Барди отказался заходить в дом клиентки
            # Барди не заходит в дом
            bardi_t "Черт!.. У меня еще целая куча заказов!"
            bardi_t "Вряд ли у меня есть на это время..."
            bardi_t "Фак!"
            # Барди смотрит на Кэрри. Кэрри в предвкушении.
            bardi "Простите, мисс Кэрри, но, к сожалению, сейчас я не могу задержаться."
            # Кэрри расстроенная, но лишь едва заметно расстроенная.
            bardi "У меня совсем нет времени... Столько работы еще сегодня..."
            bardi "А с вашим товаром все в порядке. В этом я могу вас заверить."
            bardi "Как с его качеством, так и с соответствием. Я уверен в этом на все сто!"
            bardi "Если же с ним что-то будет не так, то вы запросто сможете вернуть деньги..."
            bardi "Просто оставьте комментарий в техподдержке магазина или на форуме."
            # Кэрри поникшая. Опущенные плечи, взгляд... итд.
            client_carrie "Ну... Хорошо."
            bardi "В прошлый раз ведь все было в порядке?"
            # Кэрри понимает взгляд на Барди. На лице наигранная улыбка.
            client_carrie "Да."
            bardi "Уверяю вас, в этот раз будет так же."
            bardi "Нам ведь и самим очень важно, чтобы вы остались довольны заказом, мисс Кэрри."
            # Кэрри протягивает руку чтоб взять планшет (лист).
            client_carrie "Да, конечно. Я вас понимаю."
            # Барди протягивает ей планшет, и в след рендере Кэрри уже ставит свою роспись.
            client_carrie "Вот и все. Удачи."
            bardi "Спасибо, вам тоже. И спасибо за понимание."
            bardi "Надеюсь, это не последняя наша встреча..."
            # На лице Кэрри настоящая искренняя милая улыбка. Она машет Барди рукой.
            client_carrie "Надеюсь, в следующий раз ты будешь не так сильно загружен работой."
            bardi "Что?.."
            # Кэрри, слегка раздосадованное лицо и поза.
            client_carrie "Ой! Я имела ввиду... Просто, ты так много работаешь..."
            bardi "Ах... Да все хорошо, мисс Кэрри. Но спасибо вам за заботу."
            bardi "До свидания."
            # Кэрри снова улыбаясь машет Барди рукой.
            client_carrie "Пока."
            # Кэрри заходит домой и закрывает дверь.
            bardi_t "Боже..."
            bardi_t "Вот дверь закрылась и пришло осознание..."
            bardi_t "Какой же я все-таки придурок!"
            bardi_t "Кажется, я упустил что-то очень интересное!"
            bardi_t "Фак!"
            bardi_t "Если подобное повторится, нужно будет обязательно соглашаться..."
            bardi_t "Если следующий раз вообще произойдет!"
            bardi_t "Какой-же я идио-о-от!!!"
            # Затемнение.
            return
        "Конечно есть!": # + Rat
            # Барди медлит
            bardi_t "Черт! У меня сегодня еще целая куча заказов!.."
            bardi_t "Но я просто не могу упустить такой шанс!"
            bardi_t "Фааак! Чувствую, потом у меня будет полный завал!.."
            bardi_t "Но ведь это будет потом, верно?"
            # Барди смотрит на Кэрри. Кэрри в предвкушении.
            bardi "Да... Думаю, я не сильно отстану если задержусь..."
            # Кэрри радостно улыбнулась Барди
            bardi_t "Как же ты читаема, Кэрри... Скрыла бы хоть свои эмоции..."
            bardi_t "Хммм..."
            bardi "К слову... Мисс Кэрри, у вас какое-то недоверие к нашему магазину?"
            # Кэрри слегка растеряна. Палец у рта, будто пытается быстро придумать ответ.
            client_carrie "Нет, я... Просто..."
            bardi "В прошлый раз возникли какие-то проблемы с товаром?"
            # Кэрри улыбаясь отнекивается. Это что-то типо виноватой улыбки.
            client_carrie "Нет-нет! Все в порядке! Просто..."
            bardi "Вы мне как-то не доверяете?"
            # Кэрри растерянная как в предпоследнем рендере, отнекивается.
            client_carrie "Ну что вы?.."
            bardi_t "Хах... Ладно, наверное, стоит завязывать..."
            bardi "Банальная осторожность?"
            # Кэрри с виноватой улыбкой, одной рукой чешет затылок.
            client_carrie "Да... Просто меня уже кинули так один раз недавно... И я..."
            bardi "Да, все хорошо. Я вас понимаю."
            bardi_t "Очень хорошо понимаю..."
            label ep05_dialogues3_work_daisy_4_repeat:
            $ mlsBardiWorkDaisyClientCarrie2 = day # у Барди был секс с клиенткой магазина Дейзи
            # Кэрри приглашает Барди в дом. На лице нормальная улыбка.
            client_carrie "Проходи в дом. Не хочу задерживать тебя больше, чем нужно."
            bardi "Ага."
            # Затемнение, дверь, шаги
            # Просветление.
            # Барди в гостиной у Кэрри
            # Комнатка просторная, должен быть диван и столик перед диваном. Она приглашает его сесть на диван.
            client_carrie "Садись, я скоро буду. Только заварю кофе."
            bardi "Кофе? Но..."
            # Кэрри наигранная строгость.
            client_carrie "И не отнекивайся! Я не могу отпустить тебя, даже не напоив кофе."
            client_carrie "Ты как раз устал, наверное."
            bardi_t "Ага... Вот тебе и 'Я не хочу занимать больше времени, чем потребуется...'"
            bardi_t "Конечно... Знаем мы таких..."
            # Барди садится на диван.
            # Планшет с заказами оказывается на столике, тип барди его туда положил.
            bardi "Ох... Спасибо за заботу, мисс Кэрри."
            # Кэрри уходит на кухню. Она только развернулась и начала движение только отойдя от барди.
            # Попа Кэрри крупным планом. Секси ракурс (observing-?)
            bardi "Воу! А сзади то она тоже ничего!.. Думаю сегодня я смогу рассмотреть ее получше..."
            # Кэрри ушла на кухню.
            bardi_t "Итак, я у своей клиентки..."
            bardi_t "По всей видимости, одной из тех, кто буквально хотел запрыгнуть мне на член..."
            bardi_t "Хмм... Когда Дейзи говорила, что я могу перепасть с клиенткой... Я даже и не думал, что это возможно..."
            bardi_t "Благодать-то какая!"
            bardi_t "Интересно, что же будет дальше-е-е?.."
            bardi_t "Кстати, в что она вообще заказала?"
            # Кэрри появляется в гостиной с подносом. на подносе пара кружек с кофе.
            bardi_t "Ага... Вот и она..."
            # Кэрри подходит ближе и ставит поднос на столик. Сделайте здесь секси ракурс на сиськи.
            bardi_t "Вау!"
            client_carrie "Не скучал?"
            bardi_t "Ох... С такими мыслями не заскучаешь..."
            bardi "Нет, все в порядке."
            # Кэрри распрямляется, взяв одну из кружек, а на следующем рендере подсаживается к Барди. Поза сходу сексуальная, нога на ногу, все дела.
            # если столик стоит не у дивана, она может подать сама ему кофе
            client_carrie "Вот."
            # Барди берет кружку с кофе, делает глоток.
            bardi_t "Хмм... Какой-то знакомый привкус."
            bardi "Мисс Кэрри, а что это за кофе? Привкус какое-то знакомый..."
            # Кэрри посмеивается.
            client_carrie "Ну... У нас в городке не особо широкий выбор кофе."
            client_carrie "Наверняка, ты такой кофе уже пробовал где-то."
            # Барди смотрит на кофе.
            bardi "Да, наверное..."
            # Барди снова смотрит на Кэрри. Та, в свою очередь, с каким-то предвкушением смотрит на Барди.
            bardi "Ладно. Так что там с товаром? Вы проверили?"
            # Кэрри с наигранной улыбкой смотрит на Барди.
            client_carrie "С товаром? С ним все нормально. Вот только..."
            bardi "Что-то не так?"
            bardi_t "Да говори уже. Мы же оба знаем, что не для того я сюда пришел..."
            bardi_t "Что?!" # Барди смотрит на свою ширинку - у него встает
            bardi_t "Уже встает?.. Черт!"
            client_carrie "Нет, с товаром все хорошо. Все соответствует."
            client_carrie "Просто..."
            # Кэрри растерянно смотрит вниз.
            client_carrie "Ну... Я как бы..."
            bardi "Что такое?"
            # Барди тем временем пялится на ее грудь или ноги
            bardi_t "А эта мисс Кэрри очень сексуальная..."
            bardi_t "Неужели она нарядилась так для меня?"
            # Кэрри смотрит на Барди. Выражение лица - наивная улыбка. Поза слегка зажатая.
            client_carrie "Я совершенно не знаю, как ею пользоваться..."
            bardi_t "Опа! И что такого она могла заказать?.."
            bardi "Что было в описании товара?"
            # Кэрри кладет ноги на диван, и опирается спиной о подлокотник. юбка задралась, но ноги сомкнуты. Так что Барди не видно ничего.
            # В следующих рендерах жестикуляция только руками. Ноги не двигаются.
            bardi_t "Ееее... Вот это позы!.."
            client_carrie "Ой, не люблю я читать эти ваши описания!"
            # Кэрри с сексуальной ухмылкой.
            bardi "Давайте, я помогу вам. Где этот товар?"
            bardi_t "Фак! Что это за чувство такое странное?.."
            bardi_t "Какое-то гребаное дежавю!.."
            # кадр на допитую чашку кофе.
            bardi "Этот кофе был каким-то странным..."
            client_carrie "А что с ним не так?"
            bardi_t "Хотя бы то, что после него я безумно хочу тебя оттрах..."
            bardi_t "ФА-А-А-А-АК!"
            # Барди поднимает взгляд на Кэрри. Кэрри возбужденная сексуальная ухмылка. Поза зажатая, но поменяйте ее слегка.
            bardi_t "ТВОЮ МАТЬ!"
            bardi_t "Странный кофе, заваренный милфой! Секс-игрушки! Помощь, чтобы разобраться с ними!"
            bardi_t "Вот я идиот! Фак!"
            bardi_t "Та гребаная вигра уже в продаже?!"
            bardi_t "Нет, я, конечно, рад происходящему... Но почему снова эта чертова виагра?!"
            # Кэрри смотрит на вставший член Барди.
            client_carrie "Ого!"
            bardi "Ага!.. Где игрушка?"
            # Кэрри поднимает взгляд на Барди.
            bardi_t "Ох, пипец тебе, Кэрри! С Дейзи не вышло, но на тебе то я точно отыграюсь!"
            # Кэрри достает пульт и дает его Барди, Барди протягивает руку и берет его. (В паре рендеров.) Выражение лица Кэрри возбужденное и игривое.
            client_carrie "И долго же до тебя доходит, малыш..."
            bardi "Что это?"
            # Барди смотрит на пульт.
            client_carrie "Волшебный пульт..."
            bardi_t "Что? А где сам причиндал?"
            bardi_t "Или она его уже запихала в себя?.."
            bardi_t "Хах! Ну сейчас мы твои ножки раздвинем, мисс Кэрри..."
            # Барди смотрит на Кэрри. Также должно быть видно пульт.
            bardi "Ну, значит, будем творить магию."
            menu:
                "Максимальная мощность.":
                    pass
            # Барди выкручивает мощность пульта (До этого был на минимуме.) На максимум. (либо просто нажимает кнопки, показывать не обязательно)
            # Кэрри в афиге. Покрасневшая, приоткрыт рот. Ноги сильно прижались друг к другу, Одна рука уперлась в киску.
            client_carrie "Ах! Черт!"
            client_carrie "О, да!"
            #Барди выкручивает мощность снова на минимум.
            # Кэрри расслабляется, ноги расслаблены раздвинуты и мы видим вибратор в ее киске. Лицо покрасневшее, довольное. Рот приоткрыт, глаза закатаны.
            client_carrie "Ох, как же это было здорово!.."
            bardi "И к чему были все эти формальности?"
            # Барди приближается к Кэрри, Просовывает руку в вырез ее груди, и целует ее в губы.
            client_carrie "Мммм..."
            # Барди отстраняется от нее,
            menu:
                "Средняя мощность.":
                    pass
            # Снова выкручивает пульт но не на максимум.
            client_carrie "Ах! Да!.."
            client_carrie "О, дааа!.."
            # Барди валит ее на диван, и срывает пуговицы с рубашки. Начинает ласкать ее грудь, изобразите это в нескольких рендерах.
            # Далее меняем ракурс и показываем как он второй рукой тянется к ее киске и дрочит ей. (Клитор.)
            bardi "Дааа... Ты же вся уже мокрая, Кэрри..."
            client_carrie "Кто бы говорил! Оооо!.."
            client_carrie "О Боже! У самого стояк! Ааах!.."
            bardi "И почему нельзя было просто сказать об этом изначально?"
            client_carrie "А так разве интересно?"
            # Барди растегивает и приспускает штаны. После вынимает член.
            # Кэрри не смотрит на происходящее так как голова запрокинута назад.
            menu:
                "Вытащить из нее вибратор.":
                    pass
            # Барди, не выключая вибратор, вытаскивает его из нее
            client_carrie "Ты уже?! Такой нетерпеливый?"
            # Кэрри поднимает взгляд на него. На следующем рендере видит его стояк. и офигевает.
            client_carrie "Ничего себе!"
            client_carrie "Он же просто огромный! Он точно в меня поместится?"
            # Кэрри в шоке переводит взгляд от его стояка на лицо Барди
            bardi "Не переживай. Если что, поможем..."
            client_carrie "Что?"
            # Барди вставляет член в Кэрри, Она кайфует и запрокидывает голову назад, выгибается в спине.
            client_carrie "Ах! Боже!"
            client_carrie "Мммм..."
            # Включается анимация (если тут будет). Кэрри лежит на спине, руки в локтях согнуты. Кисти направлены вверх. Ноги раздвинуты.
            # Барди долбит ее сходу на средней скорости.
            client_carrie "О Господи! Подожди!"
            client_carrie "[mcname]! Помедленнее!"
            client_carrie "Ах!"
            client_carrie "Дааа!"
            bardi "Мммм..."
            client_carrie "О Боже!"
            client_carrie "О да!"
            bardi "Ееее!.."
            client_carrie "О Боже! [mcname]!"
            client_carrie "Прошу только не останавливайся!"
            client_carrie "О дааа!"
            menu:
                "Использовать вибратор.":
                    pass
            bardi_t "А может мы еще и так попробуем?.."
            #Анимация. (если тут будет) - Барди продолжает ахать Кэрри, при этом придерживает рукой у ее клитора вибратор.
            client_carrie "ООООО! Даааа!"
            client_carrie "ААААА!"
            client_carrie "[mcname]! О дааа!"
            client_carrie "Господи! Я!.. Я сейчас!"
            bardi_t "А вот хрена с два тебе!"
            # Барди останавливается.
            # Кэрри поднимает возбужденный взгляд на барди. Ее лицо красное, рот приоткрыт
            client_carrie "Что?"
            client_carrie "Нет-нет! [mcname]!"
            client_carrie "Ты чего?! Я уже почти!.."
            bardi "Тсс... Без паники."
            # Барди вынимает член из Кэрри.
            client_carrie "О, нет! Только не говори, что ты уже все!"
            client_carrie "Ты же еще не кончил, верно?!"
            client_carrie "Ты же можешь продолжать!"
            bardi "Так просто я тебя не отпущу..."
            # Барди берет Кэрри за талию и переворачивает ее.
            # Кэрри встает на локти, оглядывается на Барди, смотрит на него вопросительным взглядом.
            client_carrie "Что... Что ты задумал?.."
            # Барди приподнимает ее за талию вверх, чтоб она встала на колени. На следующем рендере надавливает ее на спину, чтоб прогнулась.
            # Наконец третий рендер, на котором Барди закидывает одну ногу на диван, вторая нога на полу
            # Кэрри отвернулась вперед. Одна рука Барди у нее на заднице, в другой игрушка.
            # Барди шлепает ее по заднице.
            bardi "Готова?"
            client_carrie "Да!"
            # Барди заталкивает Кэрри в киску игрушку. Кэрри удивленная оглядывается на Барди. В руках Барди пульт.
            client_carrie "Что? Ты собираешься..."
            menu:
                "Средняя мощность.":
                    pass
            # Барди включает игрушку на средней скорости. Кэрри краснеет и прикрывает глаза.
            client_carrie "Мммм..."
            client_carrie "Да..."
            # Барди прикладывает член к анусу Кэрри. Та удивленная оборачивается.
            client_carrie "Подожди! Я не..."
            # Анимацией (если будет) вставляйте член в задницу Кэрри. Кэрри в свою очередь выгнулась на локтях и запрокинула голову вверх.
            client_carrie "ООООО!"
            bardi "О ееее!.. Узенько же тут у тебя..."
            # Включается анимация. Медленно.
            client_carrie "Ох! Боже!"
            client_carrie "Он слишком большой!"
            client_carrie "Ты разорвешь меня!"
            bardi "Тише-тише. Все в порядке."
            menu:
                "Максимальная мощность.":
                    pass
            # Барди выкручивает игрушку на максимум.
            client_carrie "А-а-а-а! Да!"
            bardi "Вот так то лучше."
            client_carrie "О Боже!"
            client_carrie "[mcname]! Помедленнее!"
            client_carrie "Ах!"
            client_carrie "Боже!"
            bardi "Ммммм..."
            # Анимация ускоряется еще сильнее.
            client_carrie "О да!"
            client_carrie "Господи! Как же мне хорошо!"
            bardi "О дааа!.."
            client_carrie "[mcname]! Я сейчас!.. Я уже почти!.."
            # Анимация заканчивается
            # Кэрри кончает
            client_carrie "АААААА!!!"
            client_carrie "ААААААААА!!!"
            # Барди кончает
            bardi "Дааа!"
            bardi "АААААА!!!"
            client_carrie "Ох... Да..."
            bardi "Кайф..."
            # Кэрри оттопырив попу опускает локти и падает лицом на кровать. Голова повернута в сторону.
            # вибратор так и торчит в ее киске
            client_carrie "Ох... Как же это было офигенно!"
            # Затемнение, шуршание одежы
            # Просветление.
            # Барди сидит на диване на расслабоне. Кэрри лежит головой у него на коленях. она наполовину раздета (может, в рубашке и трусиках -?)
            # Одна рука барди лежит на груди Кэрри. Одна нога Кэрри свисает с дивана. Лицо Кэрри расслабленное, красное и довольное. Волосы растрепаны.
            client_carrie "Это было потрясно, [mcname]!"
            bardi "Хмм... Согласен."
            client_carrie "Я теперь, наверное, неделю ходить не смогу."
            client_carrie "Во мне впервые был такой огромный член."
            bardi "Хах! Спасибо!"
            # Кэрри смотрит на Барди с ухмылкой. Лицо все еще красное а волосы растрепаны. Несколько локонов волос на лице.
            client_carrie "Ты знаешь, что иметь такой член незаконно по отношению к другим мужчинам?"
            bardi "Что ж, надеюсь, ты меня не сдашь."
            # Кэрри с удивленным лицом.
            client_carrie "После такого-то?! Конечно, нет! Ни за что!"
            # Кэрри нейтральная.
            client_carrie "Но только с одним условием..."
            bardi "Воу... И с каким же?"
            client_carrie "Ты вернешься ко мне еще раз."
            bardi "Заметано."
            client_carrie "И..."
            bardi_t "И?"
            # Кэрри смотрит на Барди виноватым лицом.
            client_carrie "Если ты простишь меня..."
            bardi_t "Ого! Это еще за что?"
            bardi "За что мне тебя прощать? Ты же ничего не сделала."
            # Кэрри приподнялась и села рядом с Барди. Поза слегка зажатая, ноги сомкнуты, руки на бедрах. Выражение лица виноватое. Смотрит вниз.
            client_carrie "На самом деле, я использовала виагру..."
            # Кэрри смотрит на Барди. поза почти такая же, просто исправьте чуть-чуть сделав какую-то жестикуляцию рукой, Выражение лица такое же виноватое.
            client_carrie "Просто, я боялась что ты не захочешь... Знаешь же... Профессиональная этика, все дела..."
            client_carrie "Прости, я... Ты мне очень понравился..."
            bardi "Ну в этом мы похожи. Ты тоже зацепила меня..."
            # Кэрри удивленная. Смотрит на Барди убирая волосы с лица.
            bardi "А насчет виагры я знаю. Ты ведь это в мой кофе подсыпала?"
            client_carrie "Что?!"
            client_carrie "Как ты догадался?!"
            bardi "Говорю же... Привкус знакомый..."
            # Кэрри наигранно хмурая.
            client_carrie "Вот как? А почему ты ничего не сказал сразу?"
            bardi "А почему ты сразу не сказала, что зовешь меня трахаться?"
            client_carrie "Ты знаешь, я уже описала проблему!"
            bardi "Хах! Нашла же ты проблему!.."
            bardi "Ты себя видела? Прикрываться профессиональной этикой станет только какой-нибудь импотент!"
            # Кэрри слегка смущенная.
            client_carrie "Спасибо..."
            client_carrie "Я переживала, что ты меня возненавидишь из-за виагры..."
            client_carrie "А магазин вообще добавит меня в черный список..."
            # Кэрри удивленная и задумчивая смотрит в сторону.
            client_carrie "[mcname], а откуда ты знаешь вкус виагры? Тем более, разведенной в кофе."
            bardi_t "Фак!"
            bardi "Да так... Была тут одна ситуация..."
            # Кэрри смотрит на Барди с ухмылкой.
            client_carrie "О, даже так? А я думала, ты скажешь, что знаешь о том, что в моем заказе была виагра!"
            client_carrie "Поэтому просто догадался, так как вкус кофе был странным..."
            bardi_t "Фак! Можно же было просто так и отмазаться!"
            client_carrie "Так я не первая отчаянная клиентка?"
            bardi "Ну, можно и так сказать..."
            bardi_t "Не рассказывать же мне, что мы случайно затестировали на мне эту виагру... Причем таким же методом."
            # Кэрри такая же ухмылка, но уже со стебом.
            client_carrie "Ну ладно, дело твое..."
            client_carrie "Хотя, говоря по правде, я думала, что первая додумалась до такого плана..."
            client_carrie "Даже горда собой была."
            bardi_t "Ну, план действительно рабочий. В этом ты права."
            # Кэрри со слегка расстроенным выражением лица, поза чуть зажатая.
            client_carrie "Наверное, теперь наше рандеву стоит оставить в тайне от всех?"
            bardi "Да, если это возможно."
            client_carrie "Я не могу не похвастаться этой встречей перед подружками..."
            client_carrie "Но сделаю, что смогу, чтоб оставить тебя инкогнито!"
            # Кэрри улыбается
            bardi "Окей."
            # Кэрри сексуальная поза и ухмылка.
            bardi "К слову, мне очень даже понравилось."
            client_carrie "Да, и мне тоже. Я надеюсь, мы сможем еще ни один раз это повторить?"
            bardi "Я как раз об этом..."
            # Кэрри внимательно слушает. На лице такая же сосредоточенность. Если выйдет изобразите ее вместе с легкой улыбкой. Тип, услышанное ей нравится.
            bardi "В магазине пока только один курьер. И это я."
            bardi "Поэтому если вдруг захочешь повторить нашу встречу... Просто закажи какую-нибудь самую дешевую безделушку."
            # Кэрри радостная.
            client_carrie "Правда?! Это отлично!"
            bardi "И..."
            bardi "Мне было очень приятно видеть на тебе этот наряд..."
            bardi "А осознание того, что ты приоделась так из-за меня, радует вдвойне."
            # Кэрри сексуальная игривая ухмылка.
            client_carrie "Хи-хи. Я тебя поняла."
            # Кэрри вальяжно и не глядя указывает пальцем в дверь одной из комнат.
            client_carrie "У меня полный гардероб прикольных костюмов..."
            client_carrie "Даже есть костюм сексуальной кошечки! Может, как-нибудь мы устроим показ мод?"
            bardi "Вау!.. Звучит заманчиво."
            bardi "Только в следующий раз давай ка обойдемся без виагры?"
            # Кэрри улыбается. Позу меняйте
            client_carrie "Значит, договорились?"
            bardi "Конечно!"
            # Барди достает планшет со столика. и смотрит на заказы. В двух рендерах.
            bardi_t "Фак! Сколько же времени я потратил!"
            bardi "Ладно, я мне пора идти. У меня еще море заказов на сегодня."
            client_carrie "Да, конечно. Не хочу тебя задерживать больше, чем потребуется..."
            bardi_t "Да-да... Я вижу."
            #Барди встает с дивана. Кэрри ложится на диван полностью и прикрывает глаза. Сделайте сексуальную позу
            client_carrie "[mcname], прости, но после такого проводить тебя я не в состоянии."
            client_carrie "Я все еще плохо чувствую свои ноги..."
            client_carrie "[mcname], ты просто волшебник. Такого оргазма у меня не было уже давно."
            bardi "Ты, знаешь ли, тоже та еще искусительница..."
            # Кэрри поворачивает голову в сторону Барди, улыбается ему
            client_carrie "Спасибо. Я старалась."
            # Кэрри сново поворачивает голову обратно и смотрит вверх.
            client_carrie "Просто закрой за собой дверь."
            bardi "Окей. До встречи. Надеюсь, она скоро произойдет."
            client_carrie "Ох... Она обязательно произойдет."
            # Барди разворачивается и в нескольких рендерах выходит из дома.
            # Барди у двери снаружи дома.
            bardi_t "Господи, спасибо! Это лучшая работа в моей жизни!"
            # Барди смотрит на планшет с заказами
            bardi_t "И меня попрут с нее нахрен, если я продолжу так терять время!"
            bardi_t "Фак! Остальные заказы придется доставлять бегом."
            bardi_t "Но оно того стоило. Я ни о чем не жалею..."
            # К концу рабочего дня, Барди получает нормальное стандартное зп для этого уровня интернет магазина + хорошие чаевые.
            # Затемнение.
            return
    # Просветление.
    # Барди у рандомного дома звонит в звонок.
    # Нам не нужен весь дом. Просто рендер как Барди стоит перед дверью.
    # Дверь открывает девушка, ее не показываем.
    bardi "Здрасьте. Ваш заказ."
    # Барди отдает заказ.
    # затемнение
    # Просветление.
    # Барди у другого дома звонит в звонок.
    # Дверь открывает другая девушка, ее тоже не показываем.
    # Барди отдает заказ.
    # Затемнение.
    # Просветление.
    # Барди стоит у своего дома (вечер воскресенья)
    bardi_t "Фух... Вот и все..."
    # Барди достает телефон заходит в чат с Дэйзи.
    ## chat daisy
    bardi "Дейзи, я закончил. Все товары доставлены."
    daisy "Отлично. Молодец, [mcname]! Сейчас скину оплату."
    bardi "Окей."
    # Барди закрывает чат и выходит из телефона.
    # Появляется уведомление о пополнении счета барди и на экране появляется количество заработанного Барди бабла с плюсиком.
    if mlsBardiWorkDaisyClientCarrie1 > 0:
        # + 5 баксов у Барди
        $ add_money(5.0)
    if mlsBardiWorkDaisyClientCarrie2 > 0:
        #
        $ notif(_("[mcname] получил чаевые от Кэрри."))
        #
        # + 35 баксов у Барди
        $ add_money(35.0)
    bardi "Ну вот и отлично!"
    # Конец сцены.
    return

# если Барди в первый раз отказал Кэрри
# при работе курьером у Дейзи он снова приходит к дому Кэрри
label ep05_dialogues3_work_daisy_4:
    ## ! рендеры использовать из предыдущего лейбла
    bardi_t "И снова здорова... В третий раз уже?"
    # Барди смотрит на коробку (пакет) в руках
    bardi_t "Это снова Кэрри."
    bardi_t "Она заказала самые дешевые презервативы и доплатила за доставку из рук в руки..."
    bardi_t "Она точно меня хочет."
    bardi_t "И сегодня я так не лоханусь, как в прошлый раз!"
    # Барди подходит к двери и на следующем рендере звонит в звонок.
    # Звук звонка.
    # Дверь открывается. За дверью показывается Кэрри, снова в том же сексуальном наряде и улыбается Барди.
    # Она стоит в сексуальной позе облокотившись о дверной косяк.
    bardi_t "Вау! И снова такой же соблазнительный видок..."
    client_sexshop "И снова здравствуй, [mcname]..."
    bardi "Да... Здрасьте."
    # Кэрри смотрит на Барди игривым взглядом.
    bardi_t "Ну точно! Она точно заказала меня, а не эти презервативы!"
    bardi_t "Ну или меня в этих презервативах... Что тоже неплохо..."
    bardi "Мисс Кэрри?"
    # Кэрри сексуально ухмыляется Барди
    client_carrie "А ты видишь тут кого-то еще?"
    bardi "Нет..."
    client_carrie "И давай без этого 'мисс'. Я еще не так стара..."
    # Барди протягивает Кэрри посылку.
    bardi "Хорошо, простите. Это для вас."
    # Кэрри берет посылку с рук Барди.
    client_carrie "О, отлично!"
    bardi "Итак... Посылка уже оплачена, доставлена из рук в руки, как и просили. Верно?"
    client_carrie "Да."
    # Барди протягивает Кэрри Планшет и ручку. Кэрри принимает их и смотрит на планшет.
    bardi "Тогда вам осталось только расписаться, как всегда."
    # Кэрри поднимает взгляд на Барди.
    bardi "Если у вас, конечно, не осталось вопросов..."
    # Кэрри расписывается и возвращает планшет Барди. Лицо сосредоточенное.
    client_carrie "Знаешь, [mcname]... У меня есть один вопрос. Правда, он немного по другой теме..."
    # Барди принимает планшет.
    bardi_t "Бинго!"
    bardi "Что за вопрос?"
    # Кэрри с задумчивым лицом. смотрит в сторону.
    client_carrie "Да так... По прошлому товару..."
    # Кэрри смотрит на Барди
    client_carrie "Качество и соответствие идеальные, но..."
    client_carrie "Я не совсем понимаю, как им пользоваться."
    bardi "Оу... Это действительно проблема. Может, я могу чем-то помочь?"
    # Кэрри смотрит на Барди с ухмылкой.
    client_carrie "Если у тебя, конечно, есть время..."
    bardi "Помощь клиентам - это часть моей работы."
    # Кэрри с радостной улыбкой отходит в сторону пропуская Барди в дом.
    jump ep05_dialogues3_work_daisy_4_repeat
