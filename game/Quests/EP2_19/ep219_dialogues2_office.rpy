define ryan = Character(_("Райен"), who_color=c_blue)  # Guest4 (Ryan), фотограф Кэмпбелла
define beatrice = Character(_("Беатрис"), who_color=c_blue)  # Beatrice, ассистентка Кэмпбелла

default monicaCampbellOfficePhotoshoot1 = 0 # Моника сразу согласилась поехать на фотосессию в офис Кэмпбелла
default monicaCampbellOfficePhotoshoot2 = 0 # Моника согласилась поехать на фотосессию в офис Кэмпбелла со 2-го раза
default monicaCampbellOfficePhotoshoot3 = 0 # Моника согласилась на фотосессию в раме
default monicaCampbellOfficePhotoshoot4 = 0 # сотрудники Моники сплетничают о фотосессии в раме

define monicaPhotoshootFrameCorruptionRequired1 = 550 # Моника согласилась поехать в офис Кэмпбелла на фотосессию
define monicaPhotoshootFrameCorruptionRequired2 = 600 # Моника согласилась провести фотосессию в раме
define monicaPhotoshootFrameCorruptionRequired3 = 630 # Моника согласилась позировать более откровенно
define monicaPhotoshootFrameCorruptionRequired4 = 670 # Моника согласилась сделать кадр в полный рост

#call ep219_dialogues2_office_1() # офис, разговор с Бифом перед поездкой к Кэмпбеллу
#call ep219_dialogues2_office_2() # офис, если в первый раз отказалась от фотосессии
#call ep219_dialogues2_office_3() # фотосессия
#call ep219_dialogues2_office_4() # мысли Моники после фотосессии

# при условии, что была встреча с инвестором и Линдой в кабинете Бифа
# Моника в др. день заходит к Бифу
label ep219_dialogues2_office_1:
    # как обычно подходит к нему
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Hidden_Agenda
    imgfl 13904
    m "Биф..."
    m "Ты говорил, что есть работа для меня..."
    # Биф нетерпеливо перебивает ее
    music Groove2_85
    imgf 13902
    biff "Да-да!"
    biff "Для тебя, цыпочка, сегодня есть очень важная работа!"
    img 15889
    mt "Мне это уже не нравится!"
    mt "!!!"
    imgd 15893
    m "Что за работа?"
    m "Снова какая-нибудь дурацкая презентация?!"
    # Биф наставническим тоном
    biff "Что значит, дурацкая презентация?"
    imgf 15894
    biff "Ну хорошо, папочка добрый сегодня..."
    biff "Поэтому он будет терпеливым и попытается донести до цыпочки всю важность..."
    music Stealth_Groover
    img 15891
    m "Я знаю, Биф!"
    m "Давай к делу!"
    m "Что за важная работа?!"
    # Биф недоволен, что она его перебила
    imgd 12789
    biff "Фотосессия."
    m "Так бы сразу и сказал, Биф."
    m "Тогда я пошла в фотостудию."
    # Моника разворачивается, чтобы уйти, но Биф ее останавливает
    music Pyro_Flow
    img 15902 vpunch
    biff "А ну-ка стой!!!"
    # Моника закатывает глаза
    imgd 12810
    mt "Чего еще этому недоумку нужно от меня?!"
    mt "!!!"
    # поворачивается к Бифу
    m "Что?"
    img 15870 hpunch
    biff "Что-то я не понял!.."
    biff "Ты чего тут строишь из себя важную персону, а?"
    biff "Настолько вошла в роль?!"
    imgd 15897
    biff "Посидела своей двадцатидолларовой задницей в МОЕМ кресле..."
    biff "И думаешь, что ты можешь себя вести как настоящая Бакфетт?!"
    biff "Ты совсем охренела, кукла, так со мной разговаривать?!"
    imgd 15868
    biff "Зазвездившаяся дешевая уличная шлюшка!"
    m "Хватит называть меня так, Биф! Я не!.."
    img 15902 vpunch
    biff "Молчать!!!"
    biff "Здесь Я решаю, кого и как мне называть!"
    biff "Я здесь БОСС!!!"
    imgd 15900
    m "!!!"
    biff "Какого черта ты уходишь из моего кабинета, не дослушав меня?!"
    img 15892
    m "..."
    biff "Вот и правильно! Стой и молчи!"
    biff "Намного умнее выглядишь, когда не открываешь свой рот!"
    m "!!!"
    # Биф снова расслаблено откидывается на кресло и объясняет Монике ее работу
    music Groove2_85
    imgf 12825
    biff "В общем, слушай, кукла..."
    biff "Как ты знаешь, наш многоуважаемый Мистер Кэмпбелл является владельцем крупной дизайнерской студии."
    biff "Он уже предоставлял великолепную дизайнерскую одежду нам для работы..."
    imgd 12780
    m "Мне что, снова нужно будет надевать его пошлые костюмы?!"
    m "Я не!.."
    # Биф на нее рявкает
    img 15898 vpunch
    biff "Закрой свой рот!"
    biff "Еще раз перебьешь меня - накажу!"
    img 13900
    m "!!!"
    imgf 13902
    biff "Мистер Кэмпбелл обратился ко мне с интересным предложением."
    biff "Так как его студия занимается дизайном не только одежды, но и разными другими дизайнерскими штуками..."
    biff "Он мне предложил помочь ему в создании рекламного проекта какой-то очередной ерунды, которую он выпустил."
    imgd 12845
    biff "Я не вдавался в подробности, что это. Но точно знаю, что не одежда."
    biff "В общем, тебе нужно будет сделать снимки для рекламы этой ерунды."
    biff "И часть из этих снимков мы разместим в моем журнале..."
    biff "Тебе все ясно, кукла?"
    img 15899
    m "Нет!"
    m "Вообще ничего не ясно!"
    m "В каком формате будет проходить фотосессия и с каким реквизитом?"
    imgd 15896
    biff "Вот только не надо тут корчить из себя всезнающую модель!"
    biff "Приедем и разберемся на месте!"
    m "В смысле? Куда приедем?"
    m "Это что, выездная фотосессия?"
    imgd 15894
    biff "Ага..."
    biff "Собирайся и поехали."
    biff "Мистер Кэмбелл нас уже ждет в своем офисе."
    imgf 15868
    m "Он что, будет присутствовать на фотосессии?"
    sound Jump1
    imgd 12875
    biff "Ты совсем глупая, кукла?!"
    biff "Ты думаешь, что тебе выдадут эту дизайнерскую хреновину и дадут в руки камеру, чтобы ты сама сделала селфи?!"
    m "!!!"
    imgd 12785
    biff "Конечно, он будет присутствовать! Мистер Кэмпбелл лично будет контролировать ход фотосессии!"
    biff "Какая же ты безмозглая, я удивляюсь!"
    biff "Тебе с твоими мозгами, вернее с их полным отсутствием, до настоящей Бакфетт далеко!"
    music Pyro_Flow
    img 12782
    mt "Скотина!"
    mt "!!!"
    #corruption
    $ menu_corruption = [monicaPhotoshootFrameCorruptionRequired1, 0]
    menu:
        "Поехать на фотосессию.":
            $ monicaCampbellOfficePhotoshoot1 = day # Моника сразу согласилась поехать на фотосессию в офис Кэмпбелла
            pass
        "Отказаться.":
            imgf 15868
            mt "Черт! Выездная фотосессия в офисе Кэмпбелла!"
            mt "Не нравится мне все это!"
            mt "Тут однозначно есть какой-то подвох!"
            imgd 15889
            mt "Лучше я откажусь сразу от этой очередной бредовой идеи Бифа!"
            mt "!!!"
            imgf 15900
            m "Биф, я не буду проводить фотосессию в присутствии этого инвестора!"
            m "Тем более, в его офисе!"
            m "Я не хочу, чтобы он на меня пялился!"
            m "Почему я?! Почему не Мелани?"
            imgd 15897
            biff "Потому что Мистер Кэмпбелл так хочет."
            biff "Ты не получишь никакую другую работу..."
            biff "Пока не проведешь эту фотосессию!"
            img 12817 vpunch
            mt "Чертов Мистер Кэмпбелл! Чертов Биф! Ненавижу их всех!"
            mt "!!!"
            fadeblack
            sound highheels_short_walk
            pause 2.0
            # Моника уходит (Биф не будет давать ей фотосессии, пока она не проведет эту)
            return False
    imgf 12780
    mt "Дъявол!"
    mt "Он вышвырнет меня с работы, если я откажусь."
    mt "А мне нужны деньги..."
    mt "Где я смогу заработать $ 5 000 в месяц для сучки Виктории?"
    imgd 12810
    mt "К тому же я решила притворяться перед Бифом, что я слушаюсь его..."
    mt "Чтобы усыпить его бдительность и, перехитрив его в подходящий момент, выгнать вон из моего офиса!"
    mt "..."
    music Hidden_Agenda
    imgf 12812
    m "Я проведу эту фотосессию..."
    # довольный Биф встает с кресла и подходит к Монике
    imgd 12845
    biff "Отлично. Папочка доволен, что цыпочка решила стать снова хорошей..."
    biff "И перестала спорить с папочкой."
    menu:
        "Сказать, что Моника хорошая цыпочка.":
            imgd 12801
            m "Да..."
            m "Я хорошая цыпочка..."
            pass
        "Промолчать.":
            music Groove2_85
            imgd 15889
            mt "Да пошел ты, придурок!"
            m "..."
            pass
    # Биф хлопает Монику по попе
#    m "!!!"
    music Groove2_85
    imgf 12781
    biff "Поехали, цыпочка."
    biff "Мистер Кэмпбелл звонил и сказал, что фотограф уже на месте."
    imgd 12780
    m "???"
    m "Какой еще фотограф? Алекс?"
    imgf 12847
    biff "Нет, Алекс не работает у Кэмпбелла, если ты не заметила, кукла."
    biff "Фотосессию будет проводить другой фотограф, которого специально для этой фотосессии нанял Мистер Кэмпбелл."
    biff "Все, хватит болтать! Нас ждут."
#    biff "Иди за мной!"
#    music Power_Bots_Loop
    img 12786
    mt "Черт!"
    mt "Что еще за фотограф?!"
    mt "Не нравится мне все это..."
    fadeblack
    sound highheels_short_walk
    pause 2.0
    sound snd_car_door
    $ renpy.pause (1.0, hard=True)
    sound snd_car_turn_on
    $ renpy.pause (1.0, hard=True)
    img scene_Map_Evening
    with fade
    sound snd_car_engine
    $ renpy.pause(6.0, hard=True)
    img black_screen
    with fade
    sound snd_car_door
    $ renpy.pause (2.0, hard=True)
    return True


# если Моника отказалась фотографироваться в этом платье и оказалась на улице, но потом передумала и пришла к Бифу
# офис, кабинет Бифа
label ep219_dialogues2_office_2:
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Hidden_Agenda
    imgfl 13904
    m "Биф..."
    m "Мне нужна работа."
    music Groove2_85
    imgf 13905
    biff "Если цыпочка хочет работать, она сделает фотосессию."
    biff "В офисе Мистера Кэмпбелла и в его присутствии."
    imgd 13900
    m "..."
    biff "Ты согласна?"
    mt "!!!"
    #corruption
    $ menu_corruption = [monicaPhotoshootFrameCorruptionRequired1, 0]
    menu:
        "Поехать на фотосессию.":
            $ monicaCampbellOfficePhotoshoot2 = day # Моника согласилась поехать на фотосессию в офис Кэмпбелла со 2-го раза
            pass
        "Отказаться.":
            music Pyro_Flow
            imgf 15868
            mt "Черт! Выездная фотосессия в офисе Кэмпбелла!"
#            mt "Не нравится мне все это!"
            mt "Тут однозначно есть какой-то подвох!"
            mt "!!!"
            imgd 15900
            m "Биф, я не буду проводить фотосессию в присутствии этого инвестора!"
            m "Тем более, в его офисе!"
            m "Я не хочу, чтобы он на меня пялился!"
            m "Почему я?! Почему не Мелани?"
            imgd 15897
            biff "Потому что Мистер Кэмпбелл так хочет."
            biff "Ты не получишь никакую другую работу..."
            biff "Пока не проведешь эту фотосессию!"
            imgf 12817 vpunch
            mt "Чертов Мистер Кэмпбелл! Чертов Биф! Ненавижу их всех!"
            mt "!!!"
            fadeblack
            sound highheels_short_walk
            pause 2.0
            # Моника уходит
            return False
    music Pyro_Flow
    imgf 12780
    mt "Дъявол!"
    mt "Он вышвырнет меня с работы, если я откажусь."
    mt "А мне нужны деньги."
    mt "Где я смогу заработать $ 5 000 в месяц для сучки Виктории?"
    imgd 12810
    mt "К тому же я решила притворяться перед Бифом, что я слушаюсь его..."
    mt "Чтобы усыпить его бдительность и, перехитрив его в подходящий момент, выгнать вон из моего офиса!"
    mt "..."
    music Hidden_Agenda
    imgf 12812
    m "Я проведу эту фотосессию..."
    # Биф встает с кресла и подходит к Монике
    imgd 12845
    biff "Отлично. Папочка доволен, что цыпочка решила стать снова хорошей..."
    biff "И перестала спорить с папочкой."
    menu:
        "Сказать, что Моника хорошая цыпочка.":
            imgd 12801
            m "Да..."
            m "Я хорошая цыпочка..."
            pass
        "Промолчать.":
            music Groove2_85
            imgd 15889
            mt "Да пошел ты, придурок!"
            m "..."
            pass
    # Биф хлопает Монику по попе
#    m "!!!"
    music Groove2_85
    imgf 12781
    biff "Поехали, цыпочка."
    biff "Я сейчас позвоню Мистеру Кэмпеллу и предупрежу, что мы едем."
    biff "Надеюсь, фотограф успеет прибыть к нашему приезду."
    # если Моника сорвала фотосессию в первый раз, то просто уходят
    imgd 12780
    mt "Черт!"
    mt "!!!"
    #
    # если еще не была в офисе Кэмпбелла, то говорят про фотографа
    if monicaCampbellOfficePhotoshoot1 > 0:
        imgd 12780
        m "Какой еще фотограф? Алекс?"
        imgf 12847
        biff "Нет, Алекс не работает у Кэмпбелла, если ты не заметила, кукла."
        biff "Фотосессию будет проводить другой фотограф, которого специально для этой фотосессии нанял Мистер Кэмпбелл."
        biff "Все, хватит болтать! Нас ждут."
        #music Power_Bots_Loop
        img 12786
        mt "Черт!"
        mt "Что еще за фотограф?!"
        mt "Не нравится мне все это..."
    # затемнение, звук мотора
    fadeblack
    sound highheels_short_walk
    pause 2.0
    sound snd_car_door
    $ renpy.pause (1.0, hard=True)
    sound snd_car_turn_on
    $ renpy.pause (1.0, hard=True)
    img scene_Map_Evening
    with fade
    sound snd_car_engine
    $ renpy.pause(6.0, hard=True)
    img black_screen
    with fade
    sound snd_car_door
    $ renpy.pause (2.0, hard=True)
    return True

# конференц-зал Кэмпбелла
label ep219_dialogues2_office_3:
    # спустя некоторое время Моника с Бифом заходят в конференц-зал Кэмпбелла
    # к ним с важным видом подходит  ассистентка Кэмпбелла, она в очках, в руках папка
    pause 1.5
    sound snd_door_open1
    pause 1.0
    sound snd_door_locked1
    pause 1.5
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 60001
    w
    imgf 60000
    beatrice "Добрый день! Миссис Бакфетт, полагаю?"
    # Биф, жадно пожирая ее глазами
    imgd 60002
    w
    imgd 60003
    biff "Добрый день, Мисс!"
    biff "Передайте Мистеру Кэмпбеллу, что прибыла Миссис Бакфетт и Мистер Биф..."
    # секретарша продолжает важно
    music ZigZag
    imgf 60004
    beatrice "Я Беатрис. Являюсь ассистентом Мистера Кэмпбелла."
    imgd 60005
    beatrice "Я тоже буду присутствовать на сегоднящней фотосессии." # она неприязненно смотрит на Монику
    sound highheels_short_walk
    imgf 60006
    # Беатрис разворачивается и говорит на ходу
    beatrice "Пойдемте за мной. Я проведу вас."
    sound Jump2
    img 60007 vpunch
    mt "!!!"
    mt "А ей какого черта нужно присутствовать?!"
    mt "Может, вообще весь коллектив соберется?!"
    mt "Что за бред?!"
    # Биф смотрит на ее попу и шепчет Монике
    sound highheels_short_walk
    imgd 60008
    biff "Вот это ассистентка!"
    biff "Вот бы мне такую! На место Сиськи, например..."
    music Power_Bots_Loop
    img 60009
    m "Биф!"
    mt "Похотливое животное!"
    mt "!!!"
    # Биф смотрит на Монику
    music Groove2_85
    sound2 Jump1
    imgd 60010
    biff "Пошли, цыпочка."
    biff "И я тебя предупреждаю сразу! Никаких глупостей!"
    biff "Эта фотосессия должна пройти без накладок!"
    biff "Если ты сделаешь что-то не так и сорвешь ее..."
    biff "Дорогу в мой офис можешь забыть!"
    biff "Поняла меня?!"
    m "..."
    menu:
        "Да.":
            m "Да..."
            pass
        "Промолчать.":
            mt "Да пошел ты, придурок!"
            m "..."
            pass
    sound man_steps
    imgf 60011
    biff "Все, пошли!"
    # затемнение
    # они идут вслед за Беатрис
    # затемнение, звук шагов
    # смена кадра на сцену
    # Беатрис, Моника и Биф выходят на сцену, где их стоят и ждут Кэмпбелл и фотограф Райен (Guest4 с паблик ивента)
    # на сцене уже все готово для фотосессии, в т.ч. рама
    # Моника в недоумении оглядывается
    # Беатрис с важным видом подходит к Кэмпбеллу
    # возле сцены
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 60012
    w
    imgf 60013
    beatrice "Мистер Кэмпбелл, они прибыли..."
    campbell "Спасибо, Беатрис."
    # Биф, следом Моника тоже подходят к нему
    imgd 60014
    biff "Здравствуйте, Мистер Кэмпбелл!"
    biff "Очень рад встрече с вами и..."
    music Hidden_Agenda
    sound2 Jump1
    img 60015
    # пялясь на Беатрис
    biff "И вашими сотрудниками!"
    music Groove2_85
    imgf 60016
    campbell "Здравствуйте, Мистер Биф."
    campbell "Миссис Бакфетт, рад, что вы согласились на эту фотосессию."
    # Кэмпбелл делает жест рукой в сторону Райена
    sound Jump2
    imgd 60017
    campbell "Сегодня мы будем сотрудничать с одним из лучших фотографов нашего города."
    campbell "Знакомтесь, Мистер Райен."
    sound man_steps
    imgf 60018
    ryan "Добрый день, Миссис Бакфетт."
    ryan "Рад встрече с вами."
    m "Здравствуй, Райен..."
    ryan "Давно мечтал поработать с вами, Миссис Бакфетт."
    music Stealth_Groover
    imgd 60019
    mt "Вот черт!"
    mt "Этот никчемный Райен будет проводить фотосессию?!"
    mt "В прошлый раз он взял на себя наглость критиковать работу Алекса!"
    #
    $ notif(_("Моника разговаривала с Райеном на мероприятии в клубе Кэмпбелла."))
    #
    mt "А потом говорил, что видел мои снимки с закрытой фотосессии!!"
    mt "Самодовольный индюк!"
    music Groove2_85
    imgf 60020
    # Кэмпбелл говорит Райену
    campbell "Райен, можете приступать к работе."
    campbell "Мы с Мистером Бифом и Беатрис будем наблюдать за процессом с зала." # показывает на кресла в первом ряду перед сценой
    # потом поворачивается к Монике
    fadeblack
    sound man_steps
    pause 2.0
    music Groove2_85
    imgfl 60021
    w
    imgf 60022
    campbell "Миссис Бакфетт, скорее всего, Мистер Биф рассказал вам, какого рода снимки мне нужны..."
    campbell "Но я уточню, что это..." # показывает рукой на раму
    imgd 60023
    campbell "Это очень дорогая дизайнерская рама для картины."
    imgf 60024
    campbell "Мои лучшие дизайнеры провели тщательную и кропотливую работу..."
    campbell "Чтобы сделать ее неповторимой и потрясающе прекрасной."
    campbell "Это ваш реквизит для съемок, Миссис Бакфетт."
    # Моника с недоумением смотрит на раму
    music Stealth_Groover
    imgd 60025
    mt "Обычная рама... Не вижу в ней ничего потрясающего и неповторимого."
    mt "И еще этот Райен! Он меня раздражает!"
    mt "Одно дело работать с Алексом. Ему можно сказать, чтобы он не брал какие-то определенные ракурсы..."
    mt "Может, у меня получится также руководить и этим Райеном?.."
    imgd 60026
    mt "Моника Бакфетт снимается для рекламы дурацкой рамы!"
    mt "Какой-то идиотизм!"
    # Кэмпбелл прерывает ее мысли
    music Groove2_85
    imgf 60027
    campbell "Можете приготовиться к съемке, Миссис Бакфетт..."
    m "А где я могу переодеться и где костюм для съемки?"
    campbell "Мистер Биф не сказал вам?"
    campbell "Рама - единственный ваш реквизит. Никакой одежды."
    music Power_Bots_Loop
    img 60028 vpunch
    m "?!"
    m "В смысле?"
    music Groove2_85
    imgd 60029
    campbell "Миссис Бакфетт, это реклама рамы, а не одежды."
    campbell "Любая одежда будет только отвлекать от изысканного дизайна рамы."
    m "!!!"
    imgd 60030
    campbell "Готовьтесь к съемке, Миссис Бакфетт. Мы скоро начинаем."
    campbell "Пойдем, Беатрис. Мистер Биф, присоединяйтесь к нам в зале."
    biff "Одну минуту, Мистер Кэмпбелл..."
    # Кэмпбелл идет к выходу со сцены, чтобы сесть в зрительном зале
    # Беатрис говорит Монике
    music ZigZag
    sound2 highheels_short_walk
    imgf 60031
    beatrice "И поаккуратнее с реквизитом, Миссис Бакфетт!"
    beatrice "Эта рама стоит целое состояние!"
    m "!!!"
    # потом с гордым видом идет вслед за Кэмпбеллом
    # Моника все еще пребывает в шоке, смотрит им вслед
    # Райен отходит к оборудованию и реквизиту, подготавливая камеру
    # Биф подбегает к Монике, они разговаривают в стороне от всех, так что их никто не слышит
    # затемнение
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgf 60032
    biff "Так, цыпочка!"
    biff "Ты все слышала."
    biff "Давай, раздевайся и за работу! Не заставляй папочку и Мистера Кэмбелла ждать!"
    music Pyro_Flow
    img 60033 vpunch
    m "Раздеваться?!"
    m "Какого черта, Биф, я узнаю об этом здесь?!"
    m "?!"
    sound Jump1
    img 60034
    biff "Это твоя работа! Ты получаешь за это немаленькие деньги!"
    biff "А если будешь спорить!.."
    biff "Я не заплачу тебе ни цента!"
    biff "Так что не порть папочке настроение!"
    imgd 60035
    biff "Если хочешь и дальше зарабатывать неоправданно большие деньги..."
    biff "Только за то, что кривляешься перед камерой!"
    biff "То закрой свой рот и будь хорошей цыпочкой!"
    biff "Сорвешь съемку - сразу же позвоню охране в мой офис и тебя туда больше не пустят!"
    biff "Поняла меня?"
##### с этого момента начинается сцена, если Моника сорвала съемку в первый раз + # некоторое время спустя
#    music Groove2_85
    imgd 60036
    biff "Раздевайся! Тебя все ждут!"
    m "!!!"
    #corruption
    $ menu_corruption = [monicaPhotoshootFrameCorruptionRequired2, 0]
    menu:
        "Провести фотосессию.":
            $ monicaCampbellOfficePhotoshoot3 = day # Моника согласилась на фотосессию в раме
            pass
        "Отказаться!":
            fadeblack
            sound highheels_run2
            pause 1.5
            music Pyro_Flow
            img 60037 vpunch
            m "Биф, я не буду фотографироваться голой!"
            m "Да еще в присутствии этого инвестора и этого фотографа!"
            m "И этой жирной коровы!"
            m "Я не хочу, чтобы они на меня пялились!"
            m "И указывали мне, что делать!"
            biff "Ты не получишь никакую другую работу..."
            biff "Пока не проведешь эту фотосессию!"
            biff "Кукла безмозглая!"
            biff "Если будешь и дальше спорить со мной..."
            biff "Я заставлю тебя фотографироваться с членом во рту!"
            # Моника идет к выходу
            m "Да пошел ты!!!"
            m "!!!"
            fadeblack
            sound highheels_run2
            pause 2.0
            # Моника оказывается на улице
            # Биф не дает ей работу, пока она не сделает эту фотосессию
            return False
    # Моника зло смотрит на него
    mt "Гребаный Биф!"
    mt "Убью его!"
    mt "!!!"
    imgf 60038
    mt "Я, Моника Бакфетт, буду сниматься обнаженной!"
    mt "В какой-то безвкусной, отвратительной раме!!!"
    mt "Что делать, Моника?!"
    mt "Сволочь Биф сказал, что не пустит меня в офис!"
    mt "Черт-черт-черт!!!"
    mt "!!!"
    # задумчиво смотрит на раму
    music Hidden_Agenda
    imgd 60039
    mt "Может, я смогу принимать такие позы, в которых из-за чертовой рамы ничего не будет видно?.."
    mt "И попрошу этого придурка Райена делать соответствующие кадры..."
    mt "..."
    imgd 60040
    mt "Я не могу из-за какой-то фотосессии сорвать свой план!"
    music Stealth_Groover
    mt "Мне нужно вернуть себе все, что у меня отняли!"
    mt "А для этого необходимо мое присутствие в моем офисе!"
    mt "В конце концов, это МОЙ офис и МОЙ журнал!"
    mt "!!!"
    imgf 60041
    # Моника зло говорит Бифу
    m "Я проведу эту фотосессию!"
    music Groove2_85
    # Биф радостно
    biff "Отлично, цыпочка!"
    imgd 60042
    biff "Папочка рад, что у тебя хватило мозгов не сорвать съемку!"
    biff "Раздевайся и лезь в эту дизайнерскую хреновину!"
    # Биф уходит, Моника с ненавистью смотрит ему вслед
    # затемнение, звук одежды
    # смена кадра
    # Моника стоит на сцене, на съемочной площадке голая, прикрываясь руками
    # Биф с самодовольной миной смотрит на нее из зала, сидя рядом с Кэмпбеллом
    # Кэмпбелл сидит в центре, сбоку Биф, со второго боку - Беатрис
    # Беатрис смотрит на Монику с неприязнью
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Groove2_85
    imgfl 60043
    w
    imgf 60044
    mt "Боже! Чувствую себя отвратительно!"
    mt "!!!"
    # if если танцевала на сцене паба голой
    if ep29_quests_pub_forgiveness_dancing_quest_in_progress == True or monica_shiny_hole_queen_day > 0:
        #
        $ notif(_("Моника танцевала стриптиз в Shiny Hole."))
        #
        mt "Конечно, мне не впервые находиться на сцене без одежды..."
        mt "Но в этой грязной дыре, которую извращенка Эшли называет баром..."
        mt "Никто не знает, кто я такая на самом деле."
        mt "А здесь!.."
        #

label ep219_dialogues2_office_3a:

    imgd 60045
    mt "Так, Моника, соберись! Возьми себя в руки!"
    mt "Ты профессионал! Ты справишься!"
    # Райен держит камеру в руках, с улыбкой
    imgf 60046
    ryan "Миссис Бакфетт, начнем?"
    ryan "Сначала сделаем кадр, как-будто вы..."
    # Моника перебивает его
    m "Райен..."
    menu:
        "Попросить фотографа не делать откровенных кадров.":
            pass
    ryan "Да, Миссис Бакфетт?"
    music Hidden_Agenda
    imgd 60047
    m "Я хотела бы попрочить тебя..."
    m "Не брать крупных ракурсов и..."
    # теперь он ее перебивает
    music Groove2_85
    img 60048
    ryan "Миссис Бакфетт, я чувствую, что вы нервничаете."
    ryan "Вы ведете себя скованно и это будет усложнять процесс съемки."
    ryan "Мои снимки шедевральны, Миссис Бакфетт. Это искусство."
    ryan "Вы не найдете в моей работе никакой пошлости, не переживайте."
    imgd 60049
    m "Ты уверен, Райен?"
    m "Ничего лишнего не будет видно?"
    ryan "Я абсолютно уверен."
    ryan "К тому же, в массовую рекламу попадут только самые приличные снимки."
    m "..."
    imgd 60050
    ryan "Приступим?"
    menu:
        "Да.":
            pass
        "Отказаться!":
            fadeblack
            sound highheels_run2
            pause 2.0
            music Pyro_Flow
            img 60037 vpunch
            m "Биф, я не буду фотографироваться голой!"
            m "Да еще в присутствии этого инвестора и этого фотографа!"
            m "И этой жирной коровы!"
            m "Я не хочу, чтобы они на меня пялились!"
            m "И указывали мне, что делать!"
            biff "Ты не получишь никакую другую работу..."
            biff "Пока не проведешь эту фотосессию!"
            biff "Кукла безмозглая!"
            biff "Если будешь и дальше спорить со мной..."
            biff "Я заставлю тебя фотографироваться с членом во рту!"
            # Моника идет к выходу
            m "Да пошел ты!!!"
            m "!!!"
            fadeblack
            sound highheels_run2
            pause 2.0
            # Моника оказывается на улице
            # Биф не дает ей работу, пока она не сделает эту фотосессию
            return False
    mt "Черт!"
    m "Да..."
    return True

label ep219_dialogues2_office_3_photoshoot:
    $ shotsAmount = PS11_shots_amount
    $ shotsTotalAmount = 36

    $ shots = 2
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True

    # 1-й кадр (поза № 1 со ссылки https://www.daz3d.com/z-framed--prop-and-poses-for-genesis-3-and-8-female) +
    # Моника принимает позу, Райен делает кадры
    music Stealth_Groover
    imgf 60051
    ryan "Миссис Бакфетт, первый кадр."
    ryan "Присядьте позади рамы, придеживайте ее руками и повернитесь ко мне немного боком."
    m "Райен, я боюсь, что так будет видно мою..."
    ryan "Нет, все в порядке, Миссис Бакфетт."
    ryan "Ничего лишнего в кадре не будет видно."

    #up
#    img 60052
#    w
    #side
#    img 60053
#    ryan "Потрясающе!"
    #down
#    img 60054
#    ryan "Я завидую Алексу, что он работает с вами!"
#    ryan "Хотел бы я оказаться на его месте..."

label ep219_dialogues2_office_3_photoshoot_pose1:
    $ photoPoseLabel = "ep219_dialogues2_office_3_photoshoot_pose1"
    $ photoPoseNextLabel = "ep219_dialogues2_office_3_photoshoot_pose2"
    img 60051
    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True

        hide screen photoshoot_camera_icon
        hide screen photoshoot2
        # кадр на зал, где сидит Биф с Кэмпбеллом
        music Groove2_85
        imgfl 60055
        beatrice "Мистер Кэмпбелл, эта модель закрывает своей рукой часть рамы!"
        campbell "Все в порядке, Беатрис."
        campbell "Это всего лишь небольшой фрагмент рамы."
        # кадр на съемочную площадку

        # 2-й кадр (поза № 2) +
        # Моника встает в нужную позу
        music Stealth_Groover
        imgf 60056
        ryan "Следующий кадр, Миссис Бакфетт."
        ryan "Встаньте на колени."

        music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS11_shoots_array)
    show screen photoshoot2([60052, 60053, 60054], PS11_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 60052
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_33
        $ PS11_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 60053
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_34
        $ PS11_shoots_array.append(photoImage)
        w
        ryan "Потрясающе!"
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 60054
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_35
        $ PS11_shoots_array.append(photoImage)
        w
        ryan "Я завидую Алексу, что он работает с вами!"
        ryan "Хотел бы я оказаться на его месте..."
        jump expression photoPoseLabel




    # Райен делает снимки с разных ракурсов
    #up
#    img 60057
#    w
    #side
#    img 60058
#    ryan "Миссис Бакфетт, кадры получаются шикарные!"
#    ryan "Расслабтесь немного, я чувствую ваше напряжение."
    #down
#    img 60059
#    mt "Посмотрела бы я на тебя, кретин, если бы тебя голого поставили в эту дурацкую рамку!"

label ep219_dialogues2_office_3_photoshoot_pose2:
    $ photoPoseLabel = "ep219_dialogues2_office_3_photoshoot_pose2"
    $ photoPoseNextLabel = "ep219_dialogues2_office_3_photoshoot_pose3"
    img 60056
    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True

        hide screen photoshoot_camera_icon
        hide screen photoshoot2
        # кадр на зал, где сидит Биф с Кэмпбеллом
        music Groove2_85
        imgf 60060
        campbell "Мистер Биф, надеюсь, что фотосессия пройдет успешно и..."
        campbell "Мы подберем подходящие кадры для моей рекламной компании."
        biff "Да, Мистер Кэмпбелл, не сомневайтесь."
        biff "Миссис Бакфетт профессионал, она знает, что делать на съемочной площадке."
        imgd 60061
        # Беатрис недовольно
        beatrice "Главное, чтобы она не повредила раму!"
        campbell "Да, Беатрис, безусловно. Мы доверили Миссис Бакфетт очень ценную вещь."
        # кадр на съемочную площадку

        # 3-й кадр (поза № 3)  +
        music Stealth_Groover
        imgf 60062
        ryan "Следующий кадр, Миссис Бакфетт."
        ryan "Одной рукой придерживайте раму, а второй обопритесь о пол по другую сторону."

        music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS11_shoots_array)
    show screen photoshoot2([60057, 60058, 60059], PS11_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 60057
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_36
        $ PS11_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 60058
        img photoImage
        with Dissolve(0.2)
        w
        ryan "Миссис Бакфетт, кадры получаются шикарные!"
        ryan "Расслабтесь немного, я чувствую ваше напряжение."
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_37
        $ PS11_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 60059
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_38
        $ PS11_shoots_array.append(photoImage)
        w
        mt "Посмотрела бы я на тебя, кретин, если бы тебя голого поставили в эту дурацкую рамку!"
        jump expression photoPoseLabel



    # Моника принимает позу, Райен делает кадры
    #up
#    img 60063
#    ryan "Отлично!"
#    m "Райен, не нужно так близко брать..."
    #side
#    img 60064
#    ryan "Я фотограф и я вижу, как будет лучше, Миссис Бакфетт."
#    ryan "Еще пара кадров..."
    #down
#    img 60065
#    mt "Сволочь!"
#    mt "!!!"

label ep219_dialogues2_office_3_photoshoot_pose3:
    $ photoPoseLabel = "ep219_dialogues2_office_3_photoshoot_pose3"
    $ photoPoseNextLabel = "ep219_dialogues2_office_3_photoshoot_pose4"
    img 60062
    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True

        # кадр на зал, где сидит Биф с Кэмпбеллом
        hide screen photoshoot_camera_icon
        hide screen photoshoot2
        music Groove2_85
        imgf 60066
        beatrice "Мистер Кэмпбелл, она бросает тень на раму!"
        beatrice "Из-за этого становися не виден потрясающий рельеф рамы!"
        campbell "Беатрис, не переживай."
        campbell "Мы выберем те кадры, которые лучше всего передадут изяществ рамы."
        beatrice "Хорошо, Мистер Кэмпбелл."
        # кадр на съемочную площадку

        # 4-й кадр (поза № 4) +
        music Stealth_Groover
        imgf 60067
        ryan "Следующий кадр, Миссис Бакфетт."
        ryan "Теперь вам нужно лечь на бок и взять раму обеими руками."
        music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS11_shoots_array)
    show screen photoshoot2([60063, 60064, 60065], PS11_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 60063
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_39
        $ PS11_shoots_array.append(photoImage)
        w
        ryan "Отлично!"
        m "Райен, не нужно так близко брать..."
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 60064
        img photoImage
        with Dissolve(0.2)
        w
        ryan "Я фотограф и я вижу, как будет лучше, Миссис Бакфетт."
        ryan "Еще пара кадров..."
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_40
        $ PS11_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 60065
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_41
        $ PS11_shoots_array.append(photoImage)
        w
        mt "Сволочь!"
        mt "!!!"
        jump expression photoPoseLabel



    # Моника принимает позу, Райен делает кадры
    #up
#    img 60068
#    ryan "Хорошо, Миссис Бакфетт..."
#    ryan "Вы просто созданы быть моделью!"
    #side
#    img 60069
#    ryan "Камера любит вас!"
#    ryan "Еще пара кадров..."
#    img 60070
#    w
    #down
#    img 60071
#    mt "Я создана быть Большим Боссом и миллионером, придурок!"
#    mt "!!!"

label ep219_dialogues2_office_3_photoshoot_pose4:
    $ photoPoseLabel = "ep219_dialogues2_office_3_photoshoot_pose4"
    $ photoPoseNextLabel = "ep219_dialogues2_office_3_photoshoot_pose5"
    img 60067
    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True

        # кадр на зал, где сидит Биф с Кэмпбеллом
        hide screen photoshoot_camera_icon
        hide screen photoshoot2
        music Groove2_85
        imgf 60072
        campbell "Мистер Биф, после того, как мы с Беатрис подберем подходящие нам кадры..."
        campbell "Оставшиеся вы можете использовать для журнала Миссис Бакфетт."
        campbell "Но только после запуска моей рекламной компании, иначе ее эффективность значительно снизиться."
        biff "Мы с удовольствием опубликуем эти кадры, Мистер Кэмпбелл!"
        # Беатрис недовольно смотрит на Монику
        # кадр на съемочную площадку

        # 5-й кадр (поза № 5) +
        music Stealth_Groover
        imgf 60073
        ryan "Следующий кадр, Миссис Бакфетт."
        ryan "Поставьте ноги по другую сторону и закиньте одну ногу на другую."
        # Моника принимает позу
        m "Но так будет видно всю мою!.."
        ryan "Миссис Бакфетт, все в порядке."
        ryan "Видно только ваши шикарные ноги, ничего более."
        # corruption!
        $ menu_corruption = [monicaPhotoshootFrameCorruptionRequired3, 0]
        menu:
            "Позировать.":
                pass
            "Отказаться!":
                fadeblack
                sound highheels_run2
                pause 2.0
                music Pyro_Flow
                img 60037 vpunch
                m "Биф, я не буду так фотографироваться!"
                m "Да еще в присутствии этого инвестора и этого фотографа!"
                m "И этой жирной коровы!"
                m "Я не хочу, чтобы они на меня пялились!"
                m "И указывали мне, что делать!"
                biff "Ты не получишь никакую другую работу..."
                biff "Пока не проведешь эту фотосессию!"
                biff "Кукла безмозглая!"
                biff "Если будешь и дальше спорить со мной..."
                biff "Я заставлю тебя фотографироваться с членом во рту!"
                # Моника идет к выходу
                m "Да пошел ты!!!"
                m "!!!"
                fadeblack
                sound highheels_run2
                pause 2.0
                # Моника оказывается на улице
                # Биф не дает ей работу, пока она не сделает эту фотосессию
                return False
        mt "Черт!"

        music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS11_shoots_array)
    show screen photoshoot2([60068, 60070, 60071], PS11_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 60068
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_42
        $ PS11_shoots_array.append(photoImage)
        w
        ryan "Хорошо, Миссис Бакфетт..."
        ryan "Вы просто созданы быть моделью!"
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        img 60069
        with Dissolve(0.2)
        w
        ryan "Камера любит вас!"
        ryan "Еще пара кадров..."
        w
        call photoshop_flash() from _rcall_photoshop_flash_13
        w
        sound camera_lens1
        $ photoImage = 60070
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_43
        $ PS11_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 60071
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_44
        $ PS11_shoots_array.append(photoImage)
        w
        mt "Я создана быть Большим Боссом и миллионером, придурок!"
        mt "!!!"
        jump expression photoPoseLabel


    # Райен фотографирует
#    imgf 60073
#    w
#    #up
#    img 60074
#    ryan "Превосходно!"
#    #side
#    img 60075
#    ryan "Теперь с этого ракурса..."
#    img 60076
#    w
#    img 60077
#    w
#    #down
#    img 60078
#    w
#    img 60079
#    m "Ты уверен, что ничего не видно, Райен?"
#    ryan "Да, Миссис Бакфетт..."
#    img 60080
#    w


label ep219_dialogues2_office_3_photoshoot_pose5:
    $ photoPoseLabel = "ep219_dialogues2_office_3_photoshoot_pose5"
    $ photoPoseNextLabel = "ep219_dialogues2_office_3_photoshoot_pose6"
    img 60073
    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True

        # кадр на зал, где сидит Биф с Кэмпбеллом
        hide screen photoshoot_camera_icon
        hide screen photoshoot2
        music Groove2_85
        imgf 60081
        biff "А когда планируется запуск вашей рекламы, Мистер Кэмпбелл?"
        campbell "На днях."
        campbell "Я проведу презентацию этой рамы перед полным залом."
        biff "Здесь? В этом зале?"
        campbell "Да, все верно, в этом зале."
        imgd 60082
        campbell "Я буду выступать на сцене, а кадры будут транслироваться на экране позади меня."
        beatrice "Да, это будет отличная презентация нашего дизайнерского шедевра."
        campbell "Да, Беатрис. Я не сомневаюсь в успехе нашей рекламной компании."
        # кадр на съемочную площадку

        # 6-й кадр (поза № 8) +
        music Stealth_Groover
        imgf 60083
        ryan "Следующий кадр, Миссис Бакфетт."
        ryan "Садитесь так, чтобы ноги были по разные стороны рамы."
        # Моника принимает позу, пяткой упирается в раму
        # кадр на зал, где сидит Биф с Кэмпбеллом
        # Бетрис снова недовольно смотрит на Монику
        music Power_Bots_Loop
        sound2 oooh1
        img 60085 hpunch
        beatrice "Эта модель своей ступней опирается на нашу раму!"
        beatrice "Она испортит ее!"
        beatrice "Как можно настолько небрежно обращаться с таким ценным реквизитом?!"
        # кадр на съемочную площадку
        fadeblack 1.5
        music Stealth_Groover
        imgf 60084
        m "Райен, вся моя... Я ВСЯ видна!"
        ryan "Миссис Бакфетт, я сделаю так, что вашу прекрасную грудь, как и все остальное, не будет видно."
        ryan "Хотя, честно признаться, мне не хотелось бы этого делать..."
        m "Райен!.."
        ryan "Хорошо, но только ради вас, Миссис Бакфетт..."
        # Беатрис встает со своего места и идет к Монике
        music Pyro_Flow
        sound2 vjuh3
        img 60086 vpunch
        beatrice "Я подойду и скажу ей, чтоб так не делала, Мистер Кэмпбелл!"
        # затемнение
        sound highheels_run2
        imgf 60087
        ryan "Бетрис, что ты?.."
        beatrice "Одну секунду, Райен..."
        # она говорит Монике, наклонившись к ней
        sound Jump2
        imgd 60088
        beatrice "Буду признательна, если вы не будете упираться в раму своими ногами!"
        imgd 60089
        beatrice "Уберите ногу с рамы!"
        beatrice "Вы хоть представляете, сколько она стоит?!"
        img 60090
        beatrice "Вы делаете снимки для рекламы этого шедевра!"
        beatrice "А не для рекламы себя!"
        # Моника в афиге
        img 60091 vpunch
        m "!!!"
        m "Что?!"
        m "Да ты!..."
        # та недослушав Монику. уже более вежливо обращается к Райену
        music Groove2_85
        imgf 60092
        beatrice "Можешь работать дальше, Райен."
        beatrice "И, пожалуйста, следи, чтобы эта модель не заляпала раму и не закрывала собой ее."
        imgd 60093
        ryan "Конечно, Беатрис, без проблем." # улыбается
        imgd 60094
        beatrice "А я буду рядом, чтобы контролировать процесс!"
        beatrice "Все-таки это съемка для рекламной компании Мистера Кэмпбелла!"
        # Беатрис остается рядом со съемочной площакой, стоит в стороне
        music Pyro_Flow
        mt "Вот сучка!!!"
        mt "Как она, какая-то ничтожная секретарша, смеет так разговаривать со МНОЙ?!"
        sound Jump2
        img 60095 hpunch
        m "Следи за своим языком, корова!!!"
        m "!!!"
        imgd 60096
        ryan "Миссис Бакфетт, уберите, пожалуйста, вашу ногу с рамы."
        ryan "И продолжим."
        sound anger2
        mt "!!!"
        mt "!!!!"
        mt "!!!!!!"
        fadeblack 2.0
        # Моника немного сдвигает ногу
        imgf 60097



        music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS11_shoots_array)
    show screen photoshoot2([60074, 60077, 60080], PS11_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 60074
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_45
        $ PS11_shoots_array.append(photoImage)
        w
        ryan "Превосходно!"
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        img 60075
        with Dissolve(0.2)
        w
        ryan "Теперь с этого ракурса..."
        w
        call photoshop_flash() from _rcall_photoshop_flash_14
        w
        sound camera_lens1
        img 60076
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_15
        w
        sound camera_lens1
        $ photoImage = 60077
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_46
        $ PS11_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        img 60078
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_16
        w
        img 60079
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_17
        w
        m "Ты уверен, что ничего не видно, Райен?"
        ryan "Да, Миссис Бакфетт..."
        sound camera_lens1
        $ photoImage = 60080
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_47
        $ PS11_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

    # Райен фотографирует
#    music Stealth_Groover
#    imgf 60097
#    w
    #up
#    img 60097
#    w
    #side
#    img 60098
#    ryan "Прекрасные кадры!"
#    img 60099
#    w
    #down
#    img 60100
#    w
#    img 60101
#    ryan "Еще один снимок..."
#    img 60102
#    w

label ep219_dialogues2_office_3_photoshoot_pose6:
    $ photoPoseLabel = "ep219_dialogues2_office_3_photoshoot_pose6"
    $ photoPoseNextLabel = "ep219_dialogues2_office_3_photoshoot_pose7"
    img 60097
    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True

        # 7-й кадр (поза № 10) +
        hide screen photoshoot_camera_icon
        hide screen photoshoot2
        imgf 60103
        ryan "Следующий кадр, Миссис Бакфетт."
        ryan "Поставьте ноги по другую сторону рамы."
        # Беатрис продолжает прожигать Монику взглядом
        sound Jump2
        img 60139 vpunch
        beatrice "И попрошу быть аккуратнее с реквизитом!"
        beatrice "!!!"
        music Power_Bots_Loop
        imgd 60140
        # Моника зло на нее смотрит
        mt "Твою мать! Я что, должна слушать приказы какой-то никчемной секретарши?!"
        mt "Какого черта она тут корчит из себя начальника?!"
        mt "Дура!"
        # кадр на зал, где сидит Биф с Кэмпбеллом
        fadeblack 1.5
        music Groove2_85
        imgf 60141
        campbell "Мистер Биф, все хотел поинтересоваться у вас..."
        campbell "Миссис Бакфетт принимает участие в откровенных фотосъемках своего журнала..."
        biff "Да."
        imgd 60142
        campbell "Ей это действительно нравится?"
        campbell "Или это выгодно ей в финансовом плане, так как значительно возрастают продажи?"
        campbell "Думаю, вы, как ее личный ассистент в курсе этого..."
        imgd 60143
        biff "Миссис Бакфетт мне говорила, что получает от съемок огромное удовольствие..."
        imgf 60144
        campbell "Интересно, а согласилась бы Миссис Бакфетт на съемку полностью обнаженной..."
        campbell "Без присутствия на съемочной площадке реквизитов, подобных раме, которая частично прикрывает ее наготу..."
        biff "У вас имеются какие-либо идеи по поводу будущих фотосессий с Миссис Бакфетт?"
        imgd 60145
        campbell "Да, я тут обдумываю один проект..."
        campbell "Вполне возможно, что я снова обращусь к вам, Мистер Биф, чтобы договориться о фотосессии."
        imgd 60146
        biff "Всегда рад сотрудничеству с вами, Мистер Кэмпбелл!"
        imgf 60147
        campbell "Да, я тоже. Как показала практика, это сотрудничество весьма взаимовыгодно..."
        imgd 60148
        w
        fadeblack 1.5
        imgf 60103



        music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS11_shoots_array)
    show screen photoshoot2([60098, 60099, 60102], PS11_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 60098
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_48
        $ PS11_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 60099
        img photoImage
        with Dissolve(0.2)
        ryan "Теперь с этого ракурса..."
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_49
        $ PS11_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        img 60100
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_18
        w
        sound camera_lens1
        img 60101
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_19
        w
        ryan "Еще один снимок..."
        sound camera_lens1
        $ photoImage = 60102
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_50
        $ PS11_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel



    # кадр на съемочную площадку
    # Райен фотографирует
#    music Stealth_Groover
#    imgf 60103
#    w
    #up
#    img 60104
#    w


    #side

    #down
#    img 60108
#    ryan "Миссис Бакфетт, кадры будут шедевральными."

label ep219_dialogues2_office_3_photoshoot_pose7:
    $ photoPoseLabel = "ep219_dialogues2_office_3_photoshoot_pose7"
    $ photoPoseNextLabel = "ep219_dialogues2_office_3_photoshoot_pose8"
    img 60103
    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True

        # 8-й кадр (поза № 11) +
        hide screen photoshoot_camera_icon
        hide screen photoshoot2
        imgf 60109
        ryan "Следующий кадр, Миссис Бакфетт."
        ryan "Миссис Бакфетт, теперь вы как-будто выглядываете из рамы."
        # Моника принимает позу
        # Беатрис недовольно прикрикивает
        music Pyro_Flow
        img 60154 hpunch
        beatrice "Да аккуратнее же с реквизитом!"
        imgd 60155
        m "Я ничего не делаю с вашим реквизитом!!!"
        imgd 60156
        beatrice "И не закрывайте рукой рельеф рамы! Сколько можно говорить об этом?! Вы портите кадр!"
        # Моника бесится
        img 60157 vpunch
        m "Это Я порчу кадр?!"
        m "Здесь только одна особа все портит - это ТЫ!!!"
        mt "Сучка!!!"
        mt "!!!"
        fadeblack 1.5
        imgf 60109

        music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS11_shoots_array)
    show screen photoshoot2([60104, 60107, 60108], PS11_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 60104
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_51
        $ PS11_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side

        sound camera_lens1
        img 60105
        with Dissolve(0.2)
        w
        hide screen photoshoot_camera_icon
        hide screen photoshoot2
        imgf 60149
        ryan "Беатрис, вы попадаете в кадр. Не могли бы вы отойти?"
        music ZigZag
        imgd 60150
        beatrice "Ну и что такого, что я попала в кадр, Райен?!"
        ryan "Нууу..."
        img 60151
        mt "Меня бесит эта дурацкая секретарша!!!"
        mt "!!!"
        imgd 60152
        beatrice "Ладно, Райен, я отойду..." # недовольно
        beatrice "Не буду в кадре отвлекать собой внимание от шедевра..."
        # звук шагов, затемнение
        imgf 60105
        w
        sound highheels_short_walk
        imgd 60106
        w
        fadeblack
        sound highheels_short_walk
        pause 1.5
        music Stealth_Groover
        imgf 60153
        ryan "Продолжим, Миссис Бакфетт."

        sound camera_lens1
        img 60106
        with Dissolve(0.2)
        w
        ryan "Вы шикарно смотритесь, Миссис Бакфетт."
        w
        call photoshop_flash() from _rcall_photoshop_flash_20
        w

        sound camera_lens1
        $ photoImage = 60107
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_52
        $ PS11_shoots_array.append(photoImage)
        w
        mt "Я всегда великолепна в кадре!"
        mt "!!!"
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 60108
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_53
        $ PS11_shoots_array.append(photoImage)
        w
        ryan "Миссис Бакфетт, кадры будут шедевральными."
        jump expression photoPoseLabel



    # кадр на съемочную площадку, Райен фотографирует
#    music Stealth_Groover
#    imgf 60109
#    w
    #up
#    img 60110
#    ryan "Восхитительно!"
    #side
#    img 60111
#    ryan "Еще пара кадров..."
#    img 60112
#    w
    #down
#    img 60113
#    ryan "Прекрасно!"

label ep219_dialogues2_office_3_photoshoot_pose8:
    $ photoPoseLabel = "ep219_dialogues2_office_3_photoshoot_pose8"
    $ photoPoseNextLabel = "ep219_dialogues2_office_3_photoshoot_pose9"
    img 60109
    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True

        # 9-й кадр (поза № 12) +
        hide screen photoshoot_camera_icon
        hide screen photoshoot2
        imgf 60114
        ryan "Следующий кадр, Миссис Бакфетт."
        ryan "Повернитесь ко мне боком..."
        # Моника принимает позу
        m "Райен, мою грудь не будет видно?"
        ryan "Нет-нет, Миссис Бакфетт."
        ryan "Все в порядке."
        # кадр на злую Беатрис и Бифа, который сидит и истекает слюной на Беатрис
        imgd 60158
        beatrice "Модель, вы сейчас уроните раму!!!"
        beatrice "Если на этом шедевре появится хоть малейшая царапина!.."
        beatrice "Вы всю жизнь потом будете расплачиваться за него!"
        imgf 60159
        beatrice "Выполняйте свою работу как следует!"
        mt "Как можно так цепляться из-за какой-то дурацкой рамы!"
        mt "Жирная корова!"
        mt "!!!"
        fadeblack 1.5
        img 60114

        music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS11_shoots_array)
    show screen photoshoot2([60110, 60112, 60113], PS11_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 60110
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_54
        $ PS11_shoots_array.append(photoImage)
        w
        ryan "Восхитительно!"
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        img 60111
        with Dissolve(0.2)
        w
        ryan "Еще пара кадров..."
        w
        call photoshop_flash() from _rcall_photoshop_flash_21
        w
        sound camera_lens1
        $ photoImage = 60112
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_55
        $ PS11_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 60113
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_56
        $ PS11_shoots_array.append(photoImage)
        w
        ryan "Прекрасно!"
        jump expression photoPoseLabel





    # кадр на съемочную площадку, Райен фотографирует
#    imgf 60114
#    w
    #up
#    img 60115
#    w
#    img 60116
#    ryan "Отлично!"
    #side
#    img 60117
#    w
#    img 60118
#    ryan "Восхитительные кадры, Миссис Бакфетт!"
    #down
#    img 60119
#    ryan "Еще немного..."
#    img 60120
#    w

label ep219_dialogues2_office_3_photoshoot_pose9:
    $ photoPoseLabel = "ep219_dialogues2_office_3_photoshoot_pose9"
    $ photoPoseNextLabel = "ep219_dialogues2_office_3_photoshoot_pose10"
    img 60114
    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True


        # 10-й кадр (поза № 20) +
        imgf 60121
        ryan "Следующий кадр, Миссис Бакфетт."
        ryan "Сядь красиво за рамой и удерживайте ее руками."
        music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS11_shoots_array)
    show screen photoshoot2([60116, 60118, 60120], PS11_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        img 60115
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_22
        w
        sound camera_lens1
        $ photoImage = 60116
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_57
        $ PS11_shoots_array.append(photoImage)
        w
        ryan "Отлично!"
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        img 60117
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_23
        w
        sound camera_lens1
        $ photoImage = 60118
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_58
        $ PS11_shoots_array.append(photoImage)
        w
        ryan "Восхитительные кадры, Миссис Бакфетт!"
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        img 60119
        with Dissolve(0.2)
        w
        ryan "Еще немного..."
        w
        call photoshop_flash() from _rcall_photoshop_flash_24
        w
        sound camera_lens1
        $ photoImage = 60120
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_59
        $ PS11_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel



label ep219_dialogues2_office_3_photoshoot_pose10:
    $ photoPoseLabel = "ep219_dialogues2_office_3_photoshoot_pose10"
    $ photoPoseNextLabel = "ep219_dialogues2_office_3_photoshoot_pose11"
    img 60121
    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True

        # 11-й кадр (поза № 18) +
        music Stealth_Groover
        imgf 60125
        ryan "Следующий кадр, Миссис Бакфетт."
        ryan "Вы почти полностью выбираетесь из рамы."

        hide screen photoshoot_camera_icon
        hide screen photoshoot2
        # Моника принимает позу
        imgd 60163
        ryan "Ноги немного шире, Миссис Бакфетт."
        m "Но..."
        ryan "Никаких пошлых кадров. Помню-помню..."
        img 60164
        mt "Сволочь!"
        # Моника раздвигает ноги пошире
        music Pyro_Flow
        sound2 oooh1
        imgd 60165
        beatrice "Мистер Кэмпбелл, эта модель закрыла собой почти половину рамы!"
        # кадр на возмущенную Беатрис, которая подходит к краю сцены и говорит Кэмпбеллу, указывая рукой на Монику
        img 60166 vpunch
        m "ЧТО?!"
        m "!!!"
        imgd 60167
        beatrice "Она что, совсем не понимает, что делает?"
        beatrice "Как можно показывать такой непрофессионализм?!"
        beatrice "Над этим потрясающим рельефом работали лучшие ваши дизайнеры, а она что делает?!"
        # кадр на Бифа и Кэмпбелла
        music Groove2_85
        imgf 60168
        campbell "Беатрис, все хорошо."
        campbell "Мы возьмем не все кадры, а только те, на которых отчетливо видна наша рама."
        beatrice "Хорошо, Мистер Кэмпбелл..."
        # Беатрис идет обратно к съемочной площадке
        imgd 60169
        beatrice "Модель, продолжайте свою работу!"
        mt "Я с тобой позже разберусь, дрянь!"
        mt "!!!"
        fadeblack 1.5
        imgf 60125

        music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS11_shoots_array)
    show screen photoshoot2([60122, 60123, 60124], PS11_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 60122
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_60
        $ PS11_shoots_array.append(photoImage)
        w
        ryan "Еще пару кадров, Миссис Бакфетт..."
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 60123
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_61
        $ PS11_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 60124
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_62
        $ PS11_shoots_array.append(photoImage)
        w
        ryan "Прекрасно!"

        hide screen photoshoot_camera_icon
        hide screen photoshoot2
        music Groove2_85
        imgf 60160
        m "Райен, ты..."
        img 60161
        ryan "Я помню, Миссис Бакфетт. Вашу грудь не будет видно... Почти..."
        imgd 60162
        mt "Мерзавец!"
        mt "Говорит одно, а делает по-своему!"
        mt "Такой же обманщик, как Алекс!"
        mt "Все эти фотографы такие извращенцы?!"
        jump expression photoPoseLabel



label ep219_dialogues2_office_3_photoshoot_pose11:
    $ photoPoseLabel = "ep219_dialogues2_office_3_photoshoot_pose11"
    $ photoPoseNextLabel = "ep219_dialogues2_office_3_photoshoot_pose12"
    img 60125
    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True


        hide screen photoshoot_camera_icon
        hide screen photoshoot2
        imgf 60170
        m "Райен, если я увижу на снимках, что ты меня обманываешь..."
        m "Когда говоришь, что ничего пошлого не будет на них..."
        m "Я с тобой больше никогда не соглашусь работать!"
        sound Jump1
        img 60171 hpunch
        m "И всем буду говорить, что ты отвратительный фотограф!"
        imgf 60172
        ryan "Уверен, вам понравится моя работа!"
        ryan "Вы захотите со мной работать снова. Я в этом не сомневаюсь!"
        img 60173
        mt "Какая самоуверенность!!!"
        mt "!!!"




        # 12-й кадр (поза № 25) +
        music Stealth_Groover
        imgf 60174
        ryan "Следующий кадр, Миссис Бакфетт."
        ryan "Вам нужно встать в полный рост..."
        music Power_Bots_Loop
        m "Нет, Райен!"
        img 60175
        m "Вообще-то, я обнажена!"
        m "Как ты себе это представляешь?!"
        m "Я не буду делать этого!"
        music Groove2_85
        imgd 60176
        ryan "Но, Миссис Бакфетт, это будут последние кадры..."
        ryan "Я возьму такие ракурсы, что..."
        music Power_Bots_Loop
        img 60177 hpunch
        m "Я сказала НЕТ!"
        m "!!!"
        music Groove2_85
        imgf 60179
        campbell "Мне кажется или возникли какие-то сложности, Мистер Биф?.."
        imgd 60178
        biff "Одну минуту, Мистер Кэмпбелл..."
        # Райен растерянно оглядывается на Бифа, затемнение, шаги
        # тот вскакивает со своего места и идет к Монике, шепчет ей зло, наклонившись
        fadeblack
        sound man_steps
        pause 2.0
        music Groove2_85
        imgf 60180
        biff "Слышишь ты, кукла безмозглая!"
        biff "Что еще за капризы ты тут показываешь?!"
        biff "Быстро встала и сделала так, как тебе говорит Райен!"
        imgd 60181
        biff "Не заставляй меня нервничать!"
        biff "Не хочешь в полный рост - не оплачу эту съемку и выгоню с моего офиса на улицу!"
        biff "Будешь снова сосать члены прохожим за 20 баксов, шлюха, как ты это привыкла делать!"
        music Stealth_Groover
        imgf 60182
        mt "Черт!!!"
        mt "Я что, терпела всю эту кошмарную фотосессию..."
        mt "Чтобы из-за одного кадра лишиться денег за нее?!"
        mt "Моника, это будет неумный поступок с твоей стороны!"
    #    mt "..."
        imgd 60183
        mt "А с мерзавцем Бифом ты разберешься! Ты заставишь его отвечать за все эти унижения!"
        mt "Только нужно набраться терпения и делать вид, что слушаешься его!"
        mt "!!!"
        # коррапшн
        $ menu_corruption = [monicaPhotoshootFrameCorruptionRequired4, 0]
        menu:
            "Принять позу, которую просит фотограф.":
                pass
            "Отказаться!":
                # затемнение
                fadeblack
                sound highheels_run2
                pause 2.0
                music Pyro_Flow
                img 60037 vpunch
                m "Биф, я не буду фотографироваться голой!"
                m "Да еще в присутствии этого инвестора и этого фотографа!"
                m "И этой жирной коровы!"
                m "Я не хочу, чтобы они на меня пялились!"
                m "И указывали мне, что делать!"
                biff "Ты не получишь никакую другую работу..."
                biff "Пока не проведешь эту фотосессию!"
                biff "Кукла безмозглая!"
                biff "Если будешь и дальше спорить со мной..."
                biff "Я заставлю тебя фотографироваться с членом во рту!"
                # Моника идет к выходу
                m "Да пошел ты!!!"
                m "!!!"
                fadeblack
                sound highheels_run2
                pause 2.0
                # Моника оказывается на улице
                # Биф не дает ей работу, пока она не сделает эту фотосессию
                return False
        # затемнение
        # Моника принимает нужную позу, Биф отходит в сторону
        imgf 60131

        music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS11_shoots_array)
    show screen photoshoot2([60126, 60128, 60130], PS11_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        sound camera_lens1
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 60126
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_63
        $ PS11_shoots_array.append(photoImage)
        w
        ryan "Отличные кадры, Миссис Бакфетт!"
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        img 60127
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_25
        w
        sound camera_lens1
        $ photoImage = 60128
        img photoImage
        with Dissolve(0.2)
        ryan "Думаю, это будет одна из моих лучших работ!"
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_64
        $ PS11_shoots_array.append(photoImage)
        w
        m "С такой моделью, как Я, иначе быть не может, Райен!"
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        img 60129
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_26
        w
        sound camera_lens1
        $ photoImage = 60130
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_65
        $ PS11_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel




label ep219_dialogues2_office_3_photoshoot_pose12:
    $ photoPoseLabel = "ep219_dialogues2_office_3_photoshoot_pose12"
    $ photoPoseNextLabel = "ep219_dialogues2_office_3_photoshoot_pose_end"
    img 60131
    if shots == 0 or shotsAmount == 0:
        $ shots = 2
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True


        music stop
        jump expression photoPoseNextLabel
    show screen photoshoot_camera_icon(PS11_shoots_array)
    show screen photoshoot2([60132, 60135, 60138], PS11_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        sound camera_lens1
        $ photoImage = 60132
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_66
        $ PS11_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        img 60133
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_27
        w
        ryan "Да, отлично!"
        w
        sound camera_lens1
        img 60134
        with Dissolve(0.2)
        w
        ryan "О, Миссис Бакфетт, вы великолепны!"
        w
        call photoshop_flash() from _rcall_photoshop_flash_28
        w
        sound camera_lens1
        $ photoImage = 60135
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_67
        $ PS11_shoots_array.append(photoImage)
        w
        m "С такой моделью, как Я, иначе быть не может, Райен!"
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        img 60136
        with Dissolve(0.2)
        w
        ryan "Теперь с этого ракурса..."
        w
        call photoshop_flash() from _rcall_photoshop_flash_29
        w
        sound camera_lens1
        img 60137
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_30
        w
        ryan "Шикарный кадр!"
        w
        sound camera_lens1
        $ photoImage = 60138
        img photoImage
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_68
        $ PS11_shoots_array.append(photoImage)
        w
        jump expression photoPoseLabel

label ep219_dialogues2_office_3_photoshoot_pose_end:

    hide screen photoshoot_camera_icon
    hide screen photoshoot2
    # после последнего отснятого кадра
    music Groove2_85
    imgf 60184
    ryan "Съемка окончена!"
    m "Наконец-то!!!"
    # Моника прикрывается руками
    sound Jump2
    img 60185 vpunch
    ryan "Миссис Бакфетт, приятно было с вами поработать..."
    ryan "Это была одна из лучших моих фотосессий, Миссис Бакфетт!"
    ryan "Надеюсь, что это не последняя наша совместная работа."
    # Моника недовольно молчит
    m "!!!"


    # затемнение
    # звук одежды, шаги
    # смена кадра
    # на сцене стоят одетая Моника, фотограф, Кэмпбелл, Беатрис и Биф
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Groove2_85
    imgfl 60186
    campbell "Миссис Бакфетт, благодарю вас за сегодняшнюю фотосессию."
    mt "Ужасная фотосессия в какой-то дурацкой рамке!"
    mt "Носятся с ней, как с какой-то ценностью..."
    imgf 60187
    mt "Кому эта рамка вообще нужна?! Хлам!"
    mt "Идиоты!"
    mt "!!!"
    imgd 60188
    campbell "Вы прекрасно справились с работой."
    campbell "Уверен, что это будут отличные кадры."
    beatrice "Далеко не все..." # Беатрис с ухмылкой
    music Power_Bots_Loop
    img 60189 vpunch
    mt "Тебя забыли спросить, никчемная секретарша!"
    mt "!!!"
    music Groove2_85
    imgf 60190
    campbell "Мы с Беатрис отберем наиболее подходящие для нашей рекламной компании снимки..."
    campbell "Остальные Райен пришлет вам для публикации в вашем журнале, Миссис Бакфетт."
    m "Я..."
    img 60191
    # Биф перебивает
    biff "Спасибо вам больше, Мистер Кэмпбелл. Будем ждать с нетерпением!"
    biff "Надеюсь ваша рекламная компания пройдет успешно!"
    campbell "Я думаю, что успех гарантирован..."
    # он и Беатрис с восхищением смотрят на рамку, Биф с Млникой с недоумением
    imgd 60192
    campbell "Вы только посмотрите на этот восхитительный дизайн!"
    campbell "Только человек, не обладающий вкусом и не разбирающийся в искусстве..."
    campbell "Не увидит в этой прекрасной дизайнерской раме ничего необычного."
    imgf 60193
    campbell "Вы согласны со мной, Миссис Бакфетт?"
    campbell "Вы, как творческий человек, должны были оценить эту вещь по достоинству."
    m "Мммм... Да..."
    music Hidden_Agenda
    imgd 60194
    m "Уверена, что любой коллекционер изящных дизайнерских предметов..."
    m "Мечтал бы заполучить ее, Мистер Кэмпбелл."
    campbell "Я знал, что вам понравится, Миссис Бакфетт."
    imgf 60195
    mt "Хмм... А что, если забрать эту дурацкую раму? Интересно, за сколько ее можно продать?"
    mt "Какая-нибудь провинциалка, вроде Бетти, с радостью ее купит..."
    # если работает в пабе
    if monica_shiny_hole_queen_day > 0:
        mt "Или извращенка Эшли... Пусть повесит в эту раму какой-нибудь плакат с рекламой своего дряного пива."
        #
    imgd 60196
    m "Мистер Кэмпбелл, возможно, я смогу получить одну из ваших дизайнерских рам..."
    m "За участие в фотосессии для вашей рекламной компании?"
    m "Я в таком восхищении... перед этим шедевром..."
    music Groove2_85
    img 60197 vpunch
    beatrice "ЧТО?! Нашу раму?!"
    beatrice "Конечно, нет!!!"
    campbell "Миссис Бакфетт, я был бы рад подарить вам эту раму..."
    campbell "Но на данный момент эта рама - единственный наш экземпляр. Она эксклюзивна."
    imgd 60198
    mt "Черт!"
    mt "Это была отличная идея..."
    imgf 60199
    campbell "А сейчас я вынужден вас покинуть, к сожалению."
    campbell "Я уже опаздываю на важную встречу."
    biff "До свидания, Мистер Кэмпбелл."
    music Loved_Up
    imgd 60200
    biff "Мисс Беатрис..." # целует ей руку и жадно ее рассматривает
    biff "Надеюсь, до скорой встречи."
    # они уходят
    fadeblack
    sound highheels_run2
    pause 1.5
    sound snd_car_door
    $ renpy.pause (1.0, hard=True)
    sound snd_car_turn_on
    $ renpy.pause (1.0, hard=True)
    img scene_Map_Evening
    with fade
    sound snd_car_engine
    $ renpy.pause(6.0, hard=True)
    img black_screen
    with fade
    sound snd_car_door
    $ renpy.pause (2.0, hard=True)
    return True


# мысли Моники, когда вышла из офиса после проведения фотосессии
label ep219_dialogues2_office_4:
    # не рендерить!
    mt "Моника, я не могу поверить, что ты сделала ЭТО!!!"
    mt "Ты согласилась на фотосессию в обнаженном виде!!!"
    mt "Еще и перед этим никчменым самодовольным индюком Райеном!"
    mt "И перед инвестором с его мерзкой помощницей!"
    mt "Кошмар! Я надеюсь, что рекламная компания Кэмпбелла пройдет в узком кругу людей и не предастся широкой огласке!"
    mt "!!!"
    mt "Мне нужно придумать, как прекратить это издевательство Бифа!"
    mt "Это не может продолжаться бесконечно!"
    mt "Я должна отомстить ему!"
    mt "И забрать обратно МОЙ журнал!!!"
    mt "!!!"
    return




######### в след. апдейт #########

# при условии, что у Моники была фотосессия в раме
# через неделю Моника приходит на работу в отдел отчетов
# кадр на сотрудников отдела отчетов
label ep219_dialogues2_office_5:
    # по максимуму использовать имеющиеся арты!
    # близняшки и Лин, наклонившись друг к другу, шепчутся, сплетничают
    w7 "Девочки, помните, мы с вами удивлялись..." # Лин
    w7 "Что наша начальница фотографировалась для нашего журнала с голой грудью?"
    w3 "Да, не просто с голой грудью, а еще и перед какими-то мужчинами!"  # одна близняшка
    w4 "Перед толпой мужчин! И почти голая! Кошмар!"  # вторая близняшка
    w7 "Я сегодня увидела новый выпуск журнала..."
    w7 "А там!.." # делает фейспалм или закатывает глаза
    w4 "Что? Ну говори скорее, Лин!"
    w7 "Ой, девочки, вы сейчас будете в шоке!"
    w7 "Хи-хи-хи!"
    w3 "Ну, Лин!!!"
    w7 "Наша Миссис Бакфетт снялась для рекламы Кэмпбелла!"
    w7 "Об этом пишут во всех изданиях! И обсуждают все!"
    w4 "Что за реклама?"
    w7 "Какая-то дизайнерская рама для картины. Ничего интересного..."
    w7 "Интересен другой факт!"
    # близняшки смотрят на нее, сгорая от любопытства
    w3 "ЛИН!!!"
    w7 "Миссис Бакфетт на снимках голая! Абсолютно! В полный рост!"
    w4 "Совсем голая?!"
    w7 "Да!"
    w3 "Да ладно?!"
    w4 "Не может быть!"
    w7 "Да, девочки!"
    w7 "Я сама не поверила бы, если не увидела бы своими глазами!"
    w4 "Как вы думаете, может она и правда получает от этого удовольствие?"
    w4 "Как там таких извращенцев называют? Экбиги... Черт, не могу запомнить это слово..."
    w3 "Эксгибиционистка!"
    w4 "Да, точно!"
    w7 "Миллионерша-извращенка! Хи-хи-хи!"
    w3 "Хи-хи-хи!"
    # подкрадывается серая мышка в очках
    w1 "Вы о ком?"
    w3 "О нашей начальнице!"
    w1 "Миссис Бакфетт? А что случилось?"
    w4 "Она по ходу совсем с катушек съехала!"
    w4 "Фотографируется уже не просто полуобнаженная, а голая! Представляешь?!"
    w1 "Серьезно?!"
    # Лин резко
    w7 "Девочки! Бакфетт идет!"
    w1 "ОЙ!!!" # убегает
    w3 "Черт!"
    w4 "По местам!!!"
    # все разбегаются по местам и в этот момент заходит злая Моника
    # как обычно, с ней все здороваются, а она зло всех игнорит
    w1 "Добрый день, Миссис Бакфетт!"
    w3 "Здравствуйте!"
    w6 "Миссис Бакфетт, здравствуйте!"
    # Моника, не глядя ни на кого недовольно шагает в свой кабинет
    mt "Бесполезные муравьишки!"
    mt "Сидят занимаются своими мелкими заботами!"
    mt "Никому не нужными!"
    mt "Никчемные!"
    mt "!!!"
    return
