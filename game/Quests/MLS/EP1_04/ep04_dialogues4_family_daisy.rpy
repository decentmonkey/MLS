define daisy_t = Character(t_("Дейзи"), who_color=c_pink, what_color=c_gray, what_italic=True) # Daisy thinking

default mlsBardiFamilyV4Daisy1 = 0 # Барди был на складе товаров у Дейзи
default mlsBardiFamilyV4Daisy2 = 0 # Барди отработал первый рабочий день у Дейзи

default mlsBardiFamilyV4Daisy_photo_amount = 0
#call ep04_dialogues4_family_daisy_1() # сцена у Дейзи дома
#call ep04_dialogues4_family_daisy_2() # работа курьером
#call ep04_dialogues4_family_daisy_3() # если повторно пришел к Дейзи после сцены

#Сцена возможна в любой день кроме того, когда Софи с Синти в гости к Дейзи.
#Сцена активируется после клика по входной двери Дэйзи.
#Дэйзи в этой сцене должна быть откровенно сексуально одета.
label ep04_dialogues4_family_daisy_1:
    #Барди стоит на крыльце дома Дейзи
    music Adventures_of_the_Deaf_Dreamer
    sound2 step_stairs_short
    imgfl 901902
    bardi_t "Ну... Работа от Дэйзи звучала многообещающе..."
    bardi_t "Сегодня произойти может все, что угодно... Учитывая ее поведение в нашу прошлую встречу..."
    bardi_t "Что ж... Надеюсь, в доме мы будем одни."
    #Барди звонит в звонок
    #Звук звонка
    sound snd_door_bell1
    imgf 901903
    bardi_t "Никого дома что ли нет?"
    #Барди снова звонит
    bardi_t "..."
    #Дверь открывается с соответствующим звуком. Дэйзи нейтральная. После она видит Барди и радуется.
    fadeblack 1.0
    sound snd_door_open1
    pause 1.5
    music Shining_Through
    imgf 901904
    sound2 highheels_short_walk
    w
    imgd 901905
    daisy "О! [mcname]! Я уже и не думала, что ты придешь!"
    imgd 901906
    bardi "Почему? Я же сказал, что приду..."
    imgd 901907
    daisy "Проходи!"
    #Дэйзи освобождает проход, Барди входит в дом. Они идут в гостинную к дивану. Дэйзи говорит с бардом пока идет.
    sound snd_door_open1
    imgf 901908
    sound2 highheels_short_walk
    w
    imgd 901909
    w
    sound highheels_short_walk
    imgf 901910
    daisy "Ну как там Софи?"
    #Если Софи была у дэйзи по сцене Синти до того как Барди пришел сюда.
    if mlsBardiFamilyV4Olivia1 > 0:
        #img 901910
        daisy "По-моему, ее слегка смутила работа, которую я тебе предложила..."
        imgd 901911
        bardi "Да, она говорила об этом со мной. Но я ее успокоил."
        bardi "Я ведь просто доставляю коробки с товаром и ничего более."
        imgd 901910
        daisy "Да? Отлично!"
    else:
        imgd 901911
        bardi "С ней все хорошо."
        imgd 901910
        daisy "Ну и отлично."
    #Дэйзи и Барди стоят у дивана. Дэйзи повернута к Барди. Выражение лица как и поза нейтральные.
    imgd 901912
    bardi "А твоя дочь, Николь, сегодня не дома?"
    bardi_t "Было бы плохо, если она нам помешает... Работать..."
    #Дейзи смотрит на Барди вопросительно а потом снова нейтрально
    imgd 901913
    daisy "Нет."
    #Дэйзи смотрит на барда игриво, словно заигрывая.
    imgd 901914
    daisy "А что?"
    imgd 901912
    bardi "Просто спросил. Переживаю, чтобы никто не мешал вести дела, так сказать..."
    #Дэйзи  с такой легкой двузначной ухмылкой оценивающе смотрит на барда в сексуальной позе.
    imgd 901915
    daisy "Да?.. Ясно."
    #Дейзи смотрит на диван. После - переводит разочарованный взгляд на барди.
    imgd 901916
    w
    imgd 901917
    daisy "Эх... Хотела бы я с тобой... Поговорить..."
    daisy "Но, к сожалению, попить чай под милый диалог сегодня не получится..."
    daisy "Заказы не доставлялись уже несколько недель и их накопилось целое море."
    imgd 901911
    bardi_t "Черт..."
    bardi "Да без проблем. Я ведь и пришел узнать о работе. А попить чай, я думаю, мы еще успеем..."
    #Дэйзи смотрит на барди с эротичесской ухмылкой. и в эротичесской позе.
    imgd 901915
    daisy "Конечно..."
    imgd 901918
    bardi "Ладно... Ну и где ты хранишь товары?"
    #Дэйзи смотрит на барди оценивающим взглядом.
    imgd 901919
    daisy "Оу... Пошли, я тебе все покажу. Думаю, ты удивишься..."
    imgd 901920
    bardi_t "Хах. Посмотрим на эту коллекцию..."
    #Дэйзи ведет Барди на склад. Т.е они просто заходят в определенную темную комнату под звук открывания двери.
    #Дэйзи закрывает за Барди дверь и барди офигевает. Все, буквально все в писюнах!
    #А дэйзи довольная гордая своей коллекцией стоит рядом с диваном задрав нос
    fadeblack 1.0
    sound2 highheels_short_walk
    imgfl 901921
    music Step_By_Step
    bardi "!!!"
    bardi "!!!!"
    with vpunch
    bardi "НУ НИХРЕНА СЕБЕ!"
    imgf 901923
    daisy "Вижу, ты слегка поражен ассортиментом моего маленького магазинчика, [mcname]?"
    imgd 901922
    bardi_t "Слегка?!"
    bardi_t "Подожди, маленького?! Это маленький магазинчик, по-твоему?!"
    #Дэйзи скучая с пофигистическим лицом смотрит на ногти.
    imgd 901924
    daisy "..."
    imgf 901925
    bardi_t "Да тут же ступить негде! Тут все в членах!"
    bardi_t "Одно неосторожное падение и можешь сказать своей анальной девственности прощай!"
    #Дэйзи удивленно смотрит на Барди.
    imgd 901926
    bardi "Фак! А это для чего?! Тут даже моя извращенная фантазия не может сказать, для чего может понадобиться эта приблуда!"
    daisy "Оу... Уже даже в слух?"
    music stop
    sound plastinka1b
    img 901927 hpunch
    bardi "О, прости, Дейзи... Я просто слегка растерялся..."
    music Shining_Through
    #Дэйзи смеется.
    imgd 901928
    daisy "Да, я понимаю."
    #Дэйзи улыбается.
    imgd 901929
    bardi "Ты говорила, что у тебя маленький интим-магазин... Но здесь столько всего!"
    #Дэйзи гордо улыбается.
    imgd 901928
    daisy "Да. Я пытаюсь развивать свой маленький бизнес."
    #Дэйзи нейтральная. и поза тоже.
    imgd 901929
    bardi_t "А почему столько распакованных дилдаков?"
    imgd 901930
    daisy "Краш-тесты."
    imgd 901929
    bardi "Краш-тесты?"
    #Дэйзи согнув руки в локтях разводит руки в стороны. вся такая объясняет ему
    imgd 901931
    daisy "Должна же я знать, что продаю и делать обзоры?.."
    daisy "Какой из меня бизнесмен, если я не буду знать, что продаю?"
    imgd 901932
    bardi_t "А, по-моему, у тебя просто лютый недотрах!"
    #Дэйзи задумчиво смотрит вверх и загибает пальцы.
    imgd 901933
    daisy "В описании каждого товара нужно писать о материале, качестве сборки..."
    #Дэйзи с мстительной ухмылкой.
    daisy "Ну и короткий отзыв о выполнении их прямого назначения."
    imgd 901932
    bardi "Ты хочешь сказать, что просто осматриваешь их?"
    imgd 901930
    daisy "А что, ты хочешь посмотреть, как проходит эта процедура?"
    imgd 901929
    bardi "Прямо сейчас?!"
    #Дэйзи с ухмылкой в сексуальной позе смотрит на Барди. такая вся из себя соблазнительная издевается над ним.
    sound vjuh3
    imgd 901934
    daisy "А почему нет?.."
    imgd 901927
    bardi_t "Она что, собралась делать это прямо сейчас?!"
    bardi_t "Черт! Я, конечно, догадывался, что она та еще извращенка!.."
    bardi_t "Но совершенно не представлял, на сколько!"
    bardi_t "Я вообще думал, что она меня просто так на работу приманивает!"
    bardi_t "Да если бы я знал - первым делом бы сюда кинулся!"
    bardi "Ну... Не сказать, что я против... Даже помочь могу, если нужно..."
    #Дэйзи смеется.
    imgd 901935
    daisy "Ха-ха! Нет, пока помощь не нужна."
    daisy "к сожалению, на полноценный краш-тест у нас времени нет. А я не люблю возиться по мелочевке."
    daisy "Как говорится, если делать, то по крупному, да?"
    #Дэйзи снова сексуальная.
    imgd 901930
    daisy "Но, может, в будущем... В ближайшем будущем... Мне твоя помощь понадобится."
    daisy "А сейчас..."
    #Дэйзи достает телефон и начинает копаться в фотографиях.
    imgd 901929
    bardi_t "Она и на телефон все это записывает?!"
    bardi "Ты и съемку ведешь?"
    #Дэйзи не отрываясь от телефона
    imgd 901931
    daisy "Конечно. Но это все для работы."
    imgf 901936
    bardi_t "Ага, конечно!.."
    bardi_t "И никак не ради удовлетворения чьих-то извращенных фетишей!.."
    #Дэйзи радостная показывает Барди телефон.
    imgd 911428
    sound phone_click
    daisy "Вот! Нашла!"
    #Барди берет телефон с ее рук, смотрит фотки.
    sound2 vjuh3
    imgd 911429
    w
    imgd 911430
    w
    #В общем, механика следующая. Вы, наши прекрасные распрекрасные художники, включаете свою фантазию,
    #и  делаете несколько фотографий с дэйзи, самых разнообразных, с самыми разными ракурсами и позами,
    #с разными размерами и приблудами для всяхих адских дрочилень, а я тюлень.
    #Я просто прописываю пару тройку фразочек которые будут появляться в течении листания этих фоток
    #И да... закиньте пару фоток где дэйзи покрыта чем-то на подобии спермы. Если хардкорим то по полной.

    ## !!сделать листание фоток, по аналогии с листанием ленты в Инсте
    #Барди листает фотки и всячески комментирует их у себя в голове.
    music The_Heat
    #imgf Daisy_foto_1
    imgf 911737
    sound2 wow
    bardi_t "Ну нихрена себе! Господи! А выглядит очень даже горячо..."
    #imgd Daisy_foto_2
    sound phone_click
    imgd 911738
    bardi_t "Вау!"
    #imgd Daisy_foto_5
    sound phone_click
    imgd 911741
    bardi_t "Фак! Это прям так что ли?! Вау!"
    #imgd Daisy_foto_4
    sound phone_click
    imgd 911740
    bardi_t "Так вот для чего это было нужно!.."
    bardi_t "О, Боже! Где тут верх, а где низ вообще?!"
    #imgd Daisy_foto_3
    sound phone_click
    imgd 911739
    sound2 wow
    bardi_t "Оу, какая же она гибкая... И такая сексуальная..."
    #imgd Daisy_foto_6
    sound phone_click
    imgd 911742
    bardi_t "Воу! Это еще что за хардкор?!"
    bardi "Ну нихрена себе!"
    #Фотки заканчиваются.
    sound phone_click
    imgd 911737
    bardi_t "Хмм... Это все?"

    #Барди переводит взгляд на Дэйзи. Она в свою очередь вальяжно расселась на диване,
    #вся из тебя такая ножка на ножку, вся такая сексуальная все дела... Ждет пока Барди досмотрит фотки.
    music Shining_Through
    imgf 901937
    daisy "Вижу, тебе понравилось. Знаешь? Мне приятно..."
    imgd 901938
    bardi "Что?"
    #Дэйзи переводит взгляд на член барда. следуя за ее взглядом Барди делает то же самое.
    imgd 911837
    w
    sound erection1
    imgd 901941
    bardi "О, фак!"
    imgd 901939
    w

    imgf 901940
    daisy_t "Вау! Ну и громадина!.. Впервые вижу настоящий член таких размеров..."
    imgf 901942
    bardi "Это не могло не произойти! Ты слишком сексуальна, Дейзи."
    #Дэйзи сексуально ухмыляясь смотрит оценивающим взглядом на Барди. Так, словно пожирает глазами. поза сексуальная.
    imgd 901943
    daisy "Спасибо, [mcname]. Рада, что тебе так понравились мои фото."
    daisy "Ты, к слову, первый, кто увидел эти фотки."
    daisy "Я удивлена, что такой молодой парень вроде тебя не испугался подобного..."
    daisy "Думаю, для многих это было бы слишком."
    imgd 901942
    bardi "Ну... Тут действительно много хардкора... Но даже там ты выглядишь очень сексуально."
    #Меняйте позу Дэйзи на другую сексуальную. Чтоб не приелось.
    imgd 901944
    daisy "Спасибо, милый."
    imgd 901945
    bardi "Кстати, а что за жидкость у тебя на лице на некоторых фото?"
    imgd 901944
    daisy "Оу... Это, если по простому, то искусственная сперма."
    daisy "Цвет, текстура, вкус... Все, как настоящее."
    #Дэйзи веселая.
    daisy "К слову, она тоже есть в ассортименте. Так что, если тебе когда-то было интересно..."
    imgd 901945
    bardi "Нет, спасибо! Обойдусь."
    bardi "Ох... Чувствую скоро нас, мужиков, заменят нахрен..."
    #Дэйзи нейтральная.
    #img 901945
    daisy "[mcname], какой бы не была игрушка, настоящий член она не заменит. Уж поверь мне..."
    #Дэйзи переводит взгляд на член гг и прикусывает губу. Поза сексуальная.
    imgd 901946
    w
    imgd 901947
    daisy "И уж тем более это не грозит тебе..."
    imgd 901946
    bardi "Что?"
    daisy_t "Черт... Надеюсь, глаза меня не подводят..."
    imgd 901948
    daisy "Он у тебя и правда такой огромный?"
    imgd 901949
    bardi "Если тебе так интересно, ты могла бы это проверить."
    #Дэйзи мечтательно смотрит на барда.
    music The_Heat
    imgd 901950
    daisy "Звучит заманчиво..."
    imgd 901949
    bardi_t "Черт! Да! Да-да-да!"
    #Дэйзи строгая нейтральная.
    imgd 901944
    daisy "Но, к сожалению, не сегодня."
    music Visions_Of_Plenty
    imgd 901945
    bardi_t "Фаааак!"
    #Дэйзи сексуальная, возбужденная, соблазнительная.
    imgd 901950
    daisy "На сегодня у нас много работы, [mcname]."
    daisy "Откладывать ее больше нельзя."
    daisy "А если я занимаюсь сексом, то предпочитаю наслаждаться долго и без остановок."
    daisy "Не хочу тешить себя быстрым перепихоном..."
    imgd 901949
    bardi_t "Облом..."
    #Дэйзи вальяжно указывает пальцем на телефон.
    imgd 901951
    daisy "Прости, что мне придется оставить тебя в таком состоянии."
    imgd 901943
    daisy "В качестве утешительного приза можешь отправить себе несколько фотографий."
    imgd 901942
    bardi "Серьезно?!"
    imgd 901952
    daisy "Только с условием, что их никто не увидит, кроме тебя."
    imgd 901942
    bardi "Ну естественно."
    imgd 901950
    daisy "Тогда можешь скинуть на свой телефон все, что тебе понравилось."
    imgd 901949
    bardi_t "О, Боже! Спасибо тебе за эту работу!"

    #Сделайте, пожалуйста, хотя бы какую-то систему выборов артов
    #Может, путем пролистывания фотографий, где у читателя кнопка "сохранить\нет".
    #Если это невозможно, то пусть это будет выбор из всех артов, где читатель поочередно может выбрать каждый арт.
    #Если читатель закончил то он просто нажимает на выбор "Завершить".

    menu:
        "Выбрать фото.":
            pass
    $ menu_choice_down_forced_flag = True
    music The_Heat
    #imgf Daisy_foto_1
    sound phone_click
    imgf 911737
    menu:
        "Скинуть фото.":
            sound iphone_text_message2
            $ notif(t__("Фото отправлено"))
            $ phone_gallery_add_image("Daisy_foto_1")
            $ mlsBardiFamilyV4Daisy_photo_amount += 1
            w
        "Дальше.":
            pass
    #imgd Daisy_foto_2
    sound phone_click
    imgd 911738
    menu:
        "Скинуть фото.":
            sound iphone_text_message2
            $ notif(t__("Фото отправлено"))
            $ phone_gallery_add_image("Daisy_foto_2")
            $ mlsBardiFamilyV4Daisy_photo_amount += 1
            w
        "Дальше.":
            pass
    #imgd Daisy_foto_5
    sound phone_click
    imgd 911741
    menu:
        "Скинуть фото.":
            sound iphone_text_message2
            $ notif(t__("Фото отправлено"))
            $ phone_gallery_add_image("Daisy_foto_5")
            $ mlsBardiFamilyV4Daisy_photo_amount += 1
            w
        "Дальше.":
            pass
    #imgd Daisy_foto_4
    sound phone_click
    imgd 911740
    menu:
        "Скинуть фото.":
            sound iphone_text_message2
            $ notif(t__("Фото отправлено"))
            $ phone_gallery_add_image("Daisy_foto_4")
            $ mlsBardiFamilyV4Daisy_photo_amount += 1
            w
        "Дальше.":
            pass
    #imgd Daisy_foto_3
    sound phone_click
    imgd 911739
    menu:
        "Скинуть фото.":
            sound iphone_text_message2
            $ notif(t__("Фото отправлено"))
            $ phone_gallery_add_image("Daisy_foto_3")
            $ mlsBardiFamilyV4Daisy_photo_amount += 1
            w
        "Дальше.":
            pass
    #imgd Daisy_foto_6
    sound phone_click
    imgd 911742
    menu:
        "Скинуть фото.":
            sound iphone_text_message2
            $ notif(t__("Фото отправлено"))
            $ phone_gallery_add_image("Daisy_foto_6")
            $ mlsBardiFamilyV4Daisy_photo_amount += 1
            w
        "Дальше.":
            pass
    #Фотки заканчиваются.
    $ menu_choice_down_forced_flag = False

    if mlsBardiFamilyV4Daisy_photo_amount >= 6:
#    menu:
#        "Скинуть на свой телефон все фото.":
        fadeblack 1.0
        music Shining_Through
        imgf 911451
        bardi "Вроде все."
        #Дейзи переводит удивленный взгляд на Бардаи
        imgd 911452
        daisy "Все фото?!"
        imgd 911453
        daisy "Не думала что тебе настолько понравилось..."
    else:
#        "Выбрать фото.":
        fadeblack 1.0
        music Shining_Through
        imgf 911451
        bardi "Вроде все."
        #Барди передает телефон обратно Дейзи. Дейзи смотрит удивленная в экран.
        imgd 911452
        daisy "Оу... [mcname], да ты гурман!.."


    #Дэйзи сексуально улыбается.
    imgd 901953
    bardi "Так вышло. Просто ты очень сексуальная..."
    imgd 901954
    daisy "Спасибо."
    imgd 901953
    bardi "Нет правда. Ты отпадно выглядишь. Просто охрененно!"
    imgd 901954
    daisy "Ох... Чувствую, скоро ты сможешь увидеть все это в живую..."
    imgd 901953
    bardi_t "Скорей бы..."
    #Дэйзи строгая. Вся из себя деловая.
    imgd 901937
    daisy "Так, я бы с радостью послушала еще комплиментов. Да и не только..."
    daisy "Но нам пора закругляться."
    imgd 901955
    bardi "Жаль..."
    imgd 901937
    daisy "Очень... Но работа не ждет."
    imgd 901955
    bardi "Может все же подождет денек?.."
    #Дэйзи мечтатеьная, по следом опять образ сексуальной обломщицы.
    imgd 901956
    daisy "Нет. Всему свое время. Потерпи."
    imgd 901957
    bardi_t "Фак..."
    bardi "Ладно... Что мне нужно делать?"
    imgd 901956
    daisy "Секунду."
    #Дэйзи подходит к стеллажам. достает планшет
    #возвращается к барди. Смотрит на планшет.
    #Дэйзи переводит взгляд на коробки и указывает на них пальцем. Выражение лица строгое, деловое.
    sound highheels_short_walk
    imgf 901958
    w
    imgd 901959
    w
    imgf 901960
    w
    imgd 901961
    w
    sound highheels_short_walk
    imgf 901962
    daisy "Так... Это, это..."
    sound vjuh3
    imgd 901963
    daisy "Это..."
    sound vjuh3
    imgd 901964
    daisy "Это... И вон та коробка сверху."
    imgd 901965
    daisy "Эти заказы лежат уже третью неделю. Их нужно доставить в первую очередь."
    #Дэйзи переводит взгляд на Барди и протягивает ему планшет.
    sound Jump1
    imgd 901966
    daisy "Вот. В нем все адреса и наименования товаров, привязанных к ним."
    #Бард взял планшет. Дэйзи с той же аурой но уже без планшета.
    imgd 901967
    bardi "Понял."
    imgf 901968
    daisy "К слову, старайся не оставлять товары в почтовых ящиках."
    daisy "Всяких любопытных соседей, любителей заглядывать в чужие почтовые ящики, целое море."
    daisy "А практически все мои клиенты хотели бы остаться инкогнито."
    daisy "Поэтому товары нужно вручать лично в руки."
    imgd 901969
    bardi "Окей..."
    imgd 901968
    daisy "Как закончиль, просто напиши мне. После этого, в принципе, можешь идти домой."
    #Дейзи смотрит на Барди сочувствующим взглядом.
    imgd 901969
    bardi "Хорошо. Я все понял, Дейзи. Вроде ничего сложного."
    bardi_t "Фак! Какой же это облом! И как с таким стояком мне прикажете работать?!"
    imgd 901970
    daisy "Ох и кислая же у тебя мина, [mcname]..."
    daisy "Так уж и быть, я сделаю кое-что еще для затравочки..."
    daisy "Считай, что это за комплименты, которыми ты меня осыпал и возбудил..."
    imgd 901971
    bardi "Что?.."

    #Дэйзи целует Барди взасос.
    music The_Heat
    imgf 911431
    w
    sound2 Jump2
    img 911432 hpunch
    music2 snd_longkiss1
    bardi_t "Вау!.."
    #Несколько рендеров о том как Барди лапает Дэйзи в процессе поцелуя.
    imgf 911433
    w
    imgd 911434
    w
    imgd 911435
    w
    imgf 911436
    music2 stop
    w
    imgd 911437
    daisy "Мммм..."
    #Дэйзи отстраняется. Смотрит на Барди Сексуальным взглядом.
    imgd 911438
    daisy "А сейчас иди."
    daisy "Но обязательно возвращайся как-нибудь в другой день."
    daisy "Думаю, мне однозначно нужно независимое мнение для краш-теста..."
    #Дэйзи сексуально подмигивает Барди.
    sound Jump1
    imgd 911439
    daisy "Да, и тут много чего есть для парочек... И одна я с ними уж точно не справлюсь."
    #Дэйзи сексуальная поза и взгляд. окинула этим взглядом окружающие ее игрушки.
    imgd 911440
    daisy "Ну а сейчас я, пожалуй, займусь своей работой наедине сама с собой..."
    bardi "Оу!.. Помощь точно не нужна?"
    #Дэйзи буквально выталкивает Барди из комнаты. потом исчезает в комнате, и выносит ему коробки.
    ## думаю тут нужно поменять фразу на "Точно. Все, возьми заказы и иди!"
    imgd 911441
    daisy "Точно. Все, возьми заказы и иди!"
    music Visions_Of_Plenty
    imgf 911443
    w
    #Дэйзи улыбаясь выглядывает из-за двери.
    imgd 911442
    daisy "Удачи, [mcname]."
    bardi "До встречи, Дейзи."
    #Дэйзи закрывает дверь.
    fadeblack 1.5
    music Adventures_of_the_Deaf_Dreamer
    sound2 step_stairs_short
    imgf 911444
    bardi_t "Я обязательно еще вернусь..."
    #Барди окидывает взглядом коробки которые нужно доставить.
    sound vjuh3
    imgd 911445
    bardi_t "Ну а сейчас... Эх..."
    #Барди смотрит на свой стояк.
    bardi_t "Твою же мать!.."
    #Затемнение.
    $ mlsBardiFamilyV4Daisy1 = day # Барди был на складе товаров у Дейзи
    fadeblack 1.5
    return

label ep04_dialogues4_family_daisy_2:
    #Просветление.
    #Барди у рандомного дома звонит в звонок.
    #Нам не нужен весь дом. Просто рендер как Барди стоит перед дверью.
    #Дверь открывает девушка.
    music Adventures_of_the_Deaf_Dreamer
    imgfl 911446
    w
    sound snd_door_bell1
    imgf 911447
    w
#    bardi "Здрасьте. Ваш заказ."
    #Барди отдает заказ.
    #Девушка закрывает дверь
    # затемнение
    #Просветление.
    #Барди у рандомного дома звонит в звонок.
    #Дверь открывает другая девушка.
    sound snd_door_open1
    imgd 911448
    bardi "Здрасьте. Ваш заказ."
    #Барди отдает заказ.
    #Девушка закрывает дверь
    # затемнение
    #Просветление.
    #Барди у рандомного дома звонит в звонок.
    #Дверь открывает третья девушка.
    scene black_screen
    with Dissolve(1)
    sound step_stairs_short
    pause 1.0
#    fadeblack 1.0
#    music Adventures_of_the_Deaf_Dreamer
    imgfl 911449
    w
    sound snd_door_knock
    imgf 911450
    sound2 snd_door_open1
    bardi "Здрасьте. Ваш заказ."
    #Барди отдает заказ.
    #Девушка закрывает дверь
    #Затемнение.
    #Просветление.
    #Барди стоит у своего дома. уже вечером.
    scene black_screen
    with Dissolve(1)
    call textonblack(t_("СПУСТЯ ЧАС"))
    scene black_screen
    with Dissolve(1)
    music2 night_ambience
    music Adventures_of_the_Deaf_Dreamer
    imgfl 901159
    bardi_t "Фух... Вот и все..."
    #Барди достает телефон заходит в чат с Дэйзи.
    # chat daisy
    bardi "Дейзи, я закончил. Все товары доставлены."
    daisy "Отлично. Молодец, [mcname]! Сейчас скину оплату."
    bardi "Окей."
    #Барди закрывает чат и выходит из телефона.
    #Появляется уведомление о пополнении счета барди и на экране появляется количество заработанного Барди бабла с плюсиком.
    $ add_money(5.0)
    bardi "Ну вот и отлично!"
    #Конец Барди получает бабосики. Время суток - вечер Игрок получает свободу действий.
    fadeblack 1.5
    music2 stop
    $ mlsBardiFamilyV4Daisy2 = day # Барди отработал первый рабочий день у Дейзи
    return

#Барди получает пока что 5 баксов за выход на работу, как они и договаривались с Дейзи в предыдущей версии

#со временем магазин Дейзи становится популярней, появляются рандомные случайные сцены с девушками,
#и чем круче магазин, тем больше этих сцен и чаще они могут выпасть. И денег может капнуть больше.

#Если бард уже увидел первую сцену с Дэйзи.
# при переходе на локацию Дэйзи, при нажатии на входную дверь, появляется выбор. Войти\поработать.
# if mlsBardiFamilyV4Daisy2 > 0
label ep04_dialogues4_family_daisy_3:
    music Adventures_of_the_Deaf_Dreamer
    sound2 step_stairs_short
    imgfl 901902
    w
    label ep04_dialogues4_family_daisy_3_loop:
    menu:
        "Войти.":
            #Выбор: "Войти" - не активен до следующего апдейта
            imgf 901903
            bardi "Дэйзи напишет, когда ей будет удобно начать краш-тест."
            bardi "А до тех пор мне там делать нечего."
            jump ep04_dialogues4_family_daisy_3_loop
#        "Поработать.":
#            imgf 901903
#            bardi "Так... Время поработать курьером..."
#            #Затемнение.
#            jump ep04_dialogues4_family_daisy_2
        "Уйти.":
            imgf 901903
            bardi_t "Не сейчас. Займусь пока другими делами."
            fadeblack 1.5
            return
    return


#Вот и все. Удачи дорогим иллюстраторам)
