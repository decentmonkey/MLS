default mlsBardiFamilyV4Daisy1 = 0 # Барди был на складе товаров у Дейзи
default mlsBardiFamilyV4Daisy2 = 0 # Барди отработал первый рабочий день у Дейзи


#Сцена возможна в любой день кроме того, когда Софи с Синти в гости к Дейзи.
#Сцена активируется после клика по входной двери Дэйзи.
#Дэйзи в этой сцене должна быть откровенно сексуально одета.
label ep04_dialogues4_family_daisy_1:
    #Барди стоит на крыльце дома Дейзи
    img 901902
    bardi_t "Ну... Работа от Дэйзи звучала многообещающе..."
    bardi_t "Сегодня произойти может все, что угодно... Учитывая ее поведение в нашу прошлую встречу..."
    bardi_t "Что ж... Надеюсь, в доме мы будем одни."
    #Барди звонит в звонок
    #Звук звонка
    img 901903
    bardi_t "Никого дома что ли нет?"
    #Барди снова звонит
    bardi_t "..."
    #Дверь открывается с соответствующим звуком. Дэйзи нейтральная. После она видит Барди и радуется.
    img 901904
    w
    img 901905
    daisy "О! [mcname]! Я уже и не думала, что ты придешь!"
    img 901906
    bardi "Почему? Я же сказал, что приду..."
    img 901907
    daisy "Проходи!"
    #Дэйзи освобождает проход, Барди входит в дом. Они идут в гостинную к дивану. Дэйзи говорит с бардом пока идет.
    img 901908
    w
    img 901909
    w
    img 901910
    daisy "Ну как там Софи?"
    #Если Софи была у дэйзи по сцене Синти до того как Барди пришел сюда.
    if mlsBardiFamilyV4Olivia1 > 0:
        img 901910
        daisy "По-моему, ее слегка смутила работа, которую я тебе предложила..."
        img 901911
        bardi "Да, она говорила об этом со мной. Но я ее успокоил."
        bardi "Я ведь просто доставляю коробки с товаром и ничего более."
        img 901910
        daisy "Да? Отлично!"
    else:
        img 901911
        bardi "С ней все хорошо."
        img 901910
        daisy "Ну и отлично."
    #Дэйзи и Барди стоят у дивана. Дэйзи повернута к Барди. Выражение лица как и поза нейтральные.
    img 901912
    bardi "А твоя дочь, Николь, сегодня не дома?"
    bardi_t "Было бы плохо, если она нам помешает... Работать..."
    #Дейзи смотрит на Барди вопросительно а потом снова нейтрально
    img 901913
    daisy "Нет."
    #Дэйзи смотрит на барда игриво, словно заигрывая.
    img 901914
    daisy "А что?"
    img 901912
    bardi "Просто спросил. Переживаю, чтобы никто не мешал вести дела, так сказать..."
    #Дэйзи  с такой легкой двузначной ухмылкой оценивающе смотрит на барда в сексуальной позе.
    img 901915
    daisy "Да?.. Ясно."
    #Дейзи смотрит на диван. После - переводит разочарованный взгляд на барди.
    img 901916
    w
    img 901917
    daisy "Эх... Хотела бы я с тобой... Поговорить..."
    daisy "Но, к сожалению, попить чай под милый диалог сегодня не получится..."
    daisy "Заказы не доставлялись уже несколько недель и их накопилось целое море."
    img 901911
    bardi_t "Черт..."
    bardi "Да без проблем. Я ведь и пришел узнать о работе. А попить чай, я думаю, мы еще успеем..."
    #Дэйзи смотрит на барди с эротичесской ухмылкой. и в эротичесской позе.
    img 901915
    daisy "Конечно..."
    img 901918
    bardi "Ладно... Ну и где ты хранишь товары?"
    #Дэйзи смотрит на барди оценивающим взглядом.
    img 901919
    daisy "Оу... Пошли, я тебе все покажу. Думаю, ты удивишься..."
    img 901920
    bardi_t "Хах. Посмотрим на эту коллекцию..."
    #Дэйзи ведет Барди на склад. Т.е они просто заходят в определенную темную комнату под звук открывания двери.
    #Дэйзи закрывает за Барди дверь и барди офигевает. Все, буквально все в писюнах!
    #А дэйзи довольная гордая своей коллекцией стоит рядом с диваном задрав нос
    img 901921
    bardi "!!!"
    bardi "!!!!"
    bardi "НУ НИХРЕНА СЕБЕ!"
    img 901923
    daisy "Вижу, ты слегка поражен ассортиментом моего маленького магазинчика, [mcname]?"
    img 901922
    bardi_t "Слегка?!"
    bardi_t "Подожди, маленького?! Это маленький магазинчик, по-твоему?!"
    #Дэйзи скучая с пофигистическим лицом смотрит на ногти.
    img 901924
    daisy "..."
    img 901925
    bardi_t "Да тут же ступить негде! Тут все в членах!"
    bardi_t "Одно неосторожное падение и можешь сказать своей анальной девственности прощай!"
    #Дэйзи удивленно смотрит на Барди.
    img 901926
    bardi "Фак! А это для чего?! Тут даже моя извращенная фантазия не может сказать, для чего может понадобиться эта приблуда!"
    daisy "Оу... Уже даже в слух?"
    img 901927
    bardi "О, прости, Дейзи... Я просто слегка растерялся..."
    #Дэйзи смеется.
    img 901928
    daisy "Да, я понимаю."
    #Дэйзи улыбается.
    img 901929
    bardi "Ты говорила, что у тебя маленький интим-магазин... Но здесь столько всего!"
    #Дэйзи гордо улыбается.
    img 901928
    daisy "Да. Я пытаюсь развивать свой маленький бизнес."
    #Дэйзи нейтральная. и поза тоже.
    img 901929
    bardi_t "А почему столько распакованных дилдаков?"
    img 901930
    daisy "Краш-тесты."
    img 901929
    bardi "Краш-тесты?"
    #Дэйзи согнув руки в локтях разводит руки в стороны. вся такая объясняет ему
    img 901931
    daisy "Должна же я знать, что продаю и делать обзоры?.."
    daisy "Какой из меня бизнесмен, если я не буду знать, что продаю?"
    img 901932
    bardi_t "А, по-моему, у тебя просто лютый недотрах!"
    #Дэйзи задумчиво смотрит вверх и загибает пальцы.
    img 901933
    daisy "В описании каждого товара нужно писать о материале, качестве сборки..."
    #Дэйзи с мстительной ухмылкой.
    daisy "Ну и короткий отзыв о выполнении их прямого назначения."
    img 901932
    bardi "Ты хочешь сказать, что просто осматриваешь их?"
    img 901930
    daisy "А что, ты хочешь посмотреть, как проходит эта процедура?"
    img 901929
    bardi "Прямо сейчас?!"
    #Дэйзи с ухмылкой в сексуальной позе смотрит на Барди. такая вся из себя соблазнительная издевается над ним.
    img 901934
    daisy "А почему нет?.."
    img 901927
    bardi_t "Она что, собралась делать это прямо сейчас?!"
    bardi_t "Черт! Я, конечно, догадывался, что она та еще извращенка!.."
    bardi_t "Но совершенно не представлял, на сколько!"
    bardi_t "Я вообще думал, что она меня просто так на работу приманивает!"
    bardi_t "Да если бы я знал - первым делом бы сюда кинулся!"
    bardi "Ну... Не сказать, что я против... Даже помочь могу, если нужно..."
    #Дэйзи смеется.
    img 901935
    daisy "Ха-ха! Нет, пока помощь не нужна."
    daisy "к сожалению, на полноценный краш-тест у нас времени нет. А я не люблю возиться по мелочевке."
    daisy "Как говорится, если делать, то по крупному, да?"
    #Дэйзи снова сексуальная.
    img 901930
    daisy "Но, может, в будущем... В ближайшем будущем... Мне твоя помощь понадобится."
    daisy "А сейчас..."
    #Дэйзи достает телефон и начинает копаться в фотографиях.
    img 901929
    bardi_t "Она и на телефон все это записывает?!"
    bardi "Ты и съемку ведешь?"
    #Дэйзи не отрываясь от телефона
    img 901931
    daisy "Конечно. Но это все для работы."
    img 901936
    bardi_t "Ага, конечно!.."
    bardi_t "И никак не ради удовлетворения чьих-то извращенных фетишей!.."
    #Дэйзи радостная показывает Барди телефон.
    
    daisy "Вот! Нашла!"
    #Барди берет телефон с ее рук, смотрит фотки.

    #В общем, механика следующая. Вы, наши прекрасные распрекрасные художники, включаете свою фантазию,
    #и  делаете несколько фотографий с дэйзи, самых разнообразных, с самыми разными ракурсами и позами,
    #с разными размерами и приблудами для всяхих адских дрочилень, а я тюлень.
    #Я просто прописываю пару тройку фразочек которые будут появляться в течении листания этих фоток
    #И да... закиньте пару фоток где дэйзи покрыта чем-то на подобии спермы. Если хардкорим то по полной.

    ## !!сделать листание фоток, по аналогии с листанием ленты в Инсте
    #Барди листает фотки и всячески комментирует их у себя в голове.
    bardi_t "Ну нихрена себе! Господи! А выглядит очень даже горячо..."
    bardi_t "Фак! Это прям так что ли?! Вау!"
    bardi_t "Так вот для чего это было нужно!.."
    bardi_t "О, Боже! Где тут верх, а где низ вообще?!"
    bardi_t "Оу, какая же она гибкая... И такая сексуальная..."
    bardi_t "Вау!"
    bardi_t "Воу! Это еще что за хардкор?!"
    bardi "Ну нихрена себе!"

    #Фотки заканчиваются.
    bardi_t "Хмм... Это все?"
    #Барди переводит взгляд на Дэйзи. Она в свою очередь вальяжно расселась на диване,
    #вся из тебя такая ножка на ножку, вся такая сексуальная все дела... Ждет пока Барди досмотрит фотки.
    daisy "Вижу, тебе понравилось. Знаешь? Мне приятно..."
    bardi "Что?"
    #Дэйзи переводит взгляд на член барда. следуя за ее взглядом Барди делает то же самое.
    daisy_t "Вау! Ну и громадина!.. Впервые вижу настоящий член таких размеров..."
    bardi "О, фак!"
    bardi "Это не могло не произойти! Ты слишком сексуальна, Дейзи."
    #Дэйзи сексуально ухмыляясь смотрит оценивающим взглядом на Барди. Так, словно пожирает глазами. поза сексуальная.
    daisy "Спасибо, [mcname]. Рада, что тебе так понравились мои фото."
    daisy "Ты, к слову, первый, кто увидел эти фотки."
    daisy "Я удивлена, что такой молодой парень вроде тебя не испугался подобного..."
    daisy "Думаю, для многих это было бы слишком."
    bardi "Ну... Тут действительно много хардкора... Но даже там ты выглядишь очень сексуально."
    #Меняйте позу Дэйзи на другую сексуальную. Чтоб не приелось.
    daisy "Спасибо, милый."
    bardi "Кстати, а что за жидкость у тебя на лице на некоторых фото?"
    daisy "Оу... Это, если по простому, то искусственная сперма."
    daisy "Цвет, текстура, вкус... Все, как настоящее."
    #Дэйзи веселая.
    daisy "К слову, она тоже есть в ассортименте. Так что, если тебе когда-то было интересно..."
    bardi "Нет, спасибо! Обойдусь."
    bardi "Ох... Чувствую скоро нас, мужиков, заменят нахрен..."
    #Дэйзи нейтральная.
    daisy "[mcname], какой бы не была игрушка, настоящий член она не заменит. Уж поверь мне..."
    #Дэйзи переводит взгляд на член гг и прикусывает губу. Поза сексуальная.
    daisy "И уж тем более это не грозит тебе..."
    bardi "Что?"
    daisy_t "Черт... Надеюсь, глаза меня не подводят..."
    daisy "Он у тебя и правда такой огромный?"
    bardi "Если тебе так интересно, ты могла бы это проверить."
    #Дэйзи мечтательно смотрит на барда.
    daisy "Звучит заманчиво..."
    bardi_t "Черт! Да! Да-да-да!"
    #Дэйзи строгая нейтральная.
    daisy "Но, к сожалению, не сегодня."
    bardi_t "Фаааак!"
    #Дэйзи сексуальная, возбужденная, соблазнительная.
    daisy "На сегодня у нас много работы, [mcname]."
    daisy "Откладывать ее больше нельзя."
    daisy "А если я занимаюсь сексом, то предпочитаю наслаждаться долго и без остановок."
    daisy "Не хочу тешить себя быстрым перепихоном..."
    bardi_t "Облом..."
    #Дэйзи вальяжно указывает пальцем на телефон.
    daisy "Прости, что мне придется оставить тебя в таком состоянии."
    daisy "В качестве утешительного приза можешь отправить себе несколько фотографий."
    bardi "Серьезно?!"
    daisy "Только с условием, что их никто не увидит, кроме тебя."
    bardi "Ну естественно."
    daisy "Тогда можешь скинуть на свой телефон все, что тебе понравилось."
    bardi_t "О, Боже! Спасибо тебе за эту работу!"

    #Сделайте, пожалуйста, хотя бы какую-то систему выборов артов
    #Может, путем пролистывания фотографий, где у читателя кнопка "сохранить\нет".
    #Если это невозможно, то пусть это будет выбор из всех артов, где читатель поочередно может выбрать каждый арт.
    #Если читатель закончил то он просто нажимает на выбор "Завершить".

    menu:
        "Скинуть на свой телефон все фото.":
            bardi "Вроде все."
            #Дейзи переводит удивленный взгляд на Бардаи
            daisy "Все фото?!"
            daisy "Не думала что тебе настолько понравилось..."
            pass
        "Выбрать фото.":
            bardi "Вроде все."
            #Барди передает телефон обратно Дейзи. Дейзи смотрит удивленная в экран.
            daisy "Оу... [mcname], да ты гурман!.."
            pass
        pass
    #Дэйзи сексуально улыбается.
    bardi "Так вышло. Просто ты очень сексуальная..."
    daisy "Спасибо."
    bardi "Нет правда. Ты отпадно выглядишь. Просто охрененно!"
    daisy "Ох... Чувствую, скоро ты сможешь увидеть все это в живую..."
    bardi_t "Скорей бы..."
    #Дэйзи строгая. Вся из себя деловая.
    daisy "Так, я бы с радостью послушала еще комплиментов. Да и не только..."
    daisy "Но нам пора закругляться."
    bardi "Жаль..."
    daisy "Очень... Но работа не ждет."
    bardi "Может все же подождет денек?.."
    #Дэйзи мечтатеьная, по следом опять образ сексуальной обломщицы.
    daisy "Нет. Всему свое время. Потерпи."
    bardi_t "Фак..."
    bardi "Ладно... Что мне нужно делать?"
    daisy "Секунду."
    #Дэйзи подходит к стеллажам. достает планшет
    #возвращается к барди. Смотрит на планшет.
    #Дэйзи переводит взгляд на коробки и указывает на них пальцем. Выражение лица строгое, деловое.
    daisy "Так... Это, это..."
    daisy "Это..."
    daisy "Это... И вон та коробка сверху."
    daisy "Эти заказы лежат уже третью неделю. Их нужно доставить в первую очередь."
    #Дэйзи переводит взгляд на Барди и протягивает ему планшет.
    daisy "Вот. В нем все адреса и наименования товаров, привязанных к ним."
    #Бард взял планшет. Дэйзи с той же аурой но уже без планшета.
    bardi "Понял."
    daisy "К слову, старайся не оставлять товары в почтовых ящиках."
    daisy "Всяких любопытных соседей, любителей заглядывать в чужие почтовые ящики, целое море."
    daisy "А практически все мои клиенты хотели бы остаться инкогнито."
    daisy "Поэтому товары нужно вручать лично в руки."
    bardi "Окей..."
    daisy "Как закончиль, просто напиши мне. После этого, в принципе, можешь идти домой."
    #Дейзи смотрит на Барди сочувствующим взглядом.
    bardi "Хорошо. Я все понял, Дейзи. Вроде ничего сложного."
    bardi_t "Фак! Какой же это облом! И как с таким стояком мне прикажете работать?!"
    daisy "Ох и кислая же у тебя мина, [mcname]..."
    daisy "Так уж и быть, я сделаю кое-что еще для затравочки..."
    daisy "Считай, что это за комплименты, которыми ты меня осыпал и возбудил..."
    bardi "Что?.."
    #Дэйзи целует Барди взасос.
    bardi_t "Вау!.."
    #Несколько рендеров о том как Барди лапает Дэйзи в процессе поцелуя.
    daisy "Мммм..."
    #Дэйзи отстраняется. Смотрит на Барди Сексуальным взглядом.
    daisy "А сейчас иди."
    daisy "Но обязательно возвращайся как-нибудь в другой день."
    daisy "Думаю, мне однозначно нужно независимое мнение для краш-теста..."
    #Дэйзи сексуально подмигивает Барди.
    daisy "Да, и тут много чего есть для парочек... И одна я с ними уж точно не справлюсь."
    #Дэйзи сексуальная поза и взгляд. окинула этим взглядом окружающие ее игрушки.
    daisy "Ну а сейчас я, пожалуй, займусь своей работой наедине сама с собой..."
    bardi "Оу!.. Помощь точно не нужна?"
    #Дэйзи буквально выталкивает Барди из комнаты. потом исчезает в комнате, и выносит ему коробки.
    daisy "Точно. Все, иди!"
    #Дэйзи улыбаясь выглядывает из-за двери.
    daisy "Удачи, [mcname]."
    bardi "До встречи, Дейзи."
    #Дэйзи закрывает дверь.
    bardi_t "Я обязательно еще вернусь..."
    #Барди окидывает взглядом коробки которые нужно доставить.
    bardi_t "Ну а сейчас... Эх..."
    #Барди смотрит на свой стояк.
    bardi_t "Твою же мать!.."
    #Затемнение.
    $ mlsBardiFamilyV4Daisy1 = day # Барди был на складе товаров у Дейзи
    return

label ep04_dialogues4_family_daisy_2:
    #Просветление.
    #Барди у рандомного дома звонит в звонок.
    #Нам не нужен весь дом. Просто рендер как Барди стоит перед дверью.
    #Дверь открывает девушка.
    bardi "Здрасьте. Ваш заказ."
    #Барди отдает заказ.
    #Девушка закрывает дверь
    # затемнение
    #Просветление.
    #Барди у рандомного дома звонит в звонок.
    #Дверь открывает другая девушка.
    bardi "Здрасьте. Ваш заказ."
    #Барди отдает заказ.
    #Девушка закрывает дверь
    # затемнение
    #Просветление.
    #Барди у рандомного дома звонит в звонок.
    #Дверь открывает третья девушка.
    bardi "Здрасьте. Ваш заказ."
    #Барди отдает заказ.
    #Девушка закрывает дверь
    #Затемнение.
    #Просветление.
    #Барди стоит у своего дома. уже вечером.
    bardi_t "Фух... Вот и все..."
    #Барди достает телефон заходит в чат с Дэйзи.
    # chat daisy
    bardi "Дейзи, я закончил. Все товары доставлены."
    daisy "Отлично. Молодец, [mcname]! Сейчас скину оплату."
    bardi "Окей."
    #Барди закрывает чат и выходит из телефона.
    #Появляется уведомление о пополнении счета барди и на экране появляется количество заработанного Барди бабла с плюсиком.
    bardi "Ну вот и отлично!"
    #Конец Барди получает бабосики. Время суток - вечер Игрок получает свободу действий.
    $ mlsBardiFamilyV4Daisy2 = day # Барди отработал первый рабочий день у Дейзи
    return

#Барди получает рандомную сумму. если это возможно, сделайте вероятность выпадения большой суммы ниже.

#со временем магазин Дейзи становится популярней, появляются рандомные случайные сцены с девушками,
#и чем круче магазин, тем больше этих сцен и чаще они могут выпасть. И денег может капнуть больше.

#ВНИМАНИЕ!! Это не полноценная работа для Барди. Заработать в ней должно быть возможно намного меньше, чем в велопрокате

#Если бард уже увидел первую сцену с Дэйзи.
# при переходе на локацию Дэйзи, при нажатии на входную дверь, появляется выбор. Войти\поработать.
# if mlsBardiFamilyV4Daisy2 > 0
label ep04_dialogues4_family_daisy_3:
    menu:
        "Войти.":
            #Выбор: "Войти" - не активен до следующего апдейта
            bardi "Дэйзи напишет, когда ей будет удобно начать краш-тест."
            bardi "А до тех пор мне там делать нечего."
            jump ep04_dialogues4_family_daisy_3
        "Поработать.":
            bardi "Так... Время поработать курьером..."
            #Затемнение.
            jump ep04_dialogues4_family_daisy_2
        "Уйти.":
            bardi_t "Не сейчас. Займусь пока другими делами."
            return
    return


#Вот и все. Удачи дорогим иллюстраторам)
