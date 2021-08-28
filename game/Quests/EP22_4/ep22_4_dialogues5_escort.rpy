define neighbor2 = Character(_("Сосед Эбби"), who_color=c_red)  # сосед Эбби
define brian = Character(_("Брайан"), who_color=c_orange)  # клиент Эбби вне эскорта

default monicaAbbyNoEscortClient1 = 0 # Моника согласилась поехать домой к Эбби и встретиться с ее клиентом вне эскорта
default monicaAbbyNoEscortClient2 = 0 # Моника изменила свое решение и согласилась работать с клиентами Эбби
default monicaAbbyNoEscortClient3 = 0 # Моника согласилась на секс с клиентом Эбби, не стала выгонять его
default monicaAbbyNoEscortClient4 = 0 # Моника не оставила Эбби процент, забрала все деньги
default monicaAbbyNoEscortClient5 = 0 # Моника оставила Эбби процент

define v_Monica_AbbyCustomer_Blowjob1_1_25_sound_name = "v_Monica_AbbyCustomer_Blowjob1_1_25"
define v_Monica_AbbyCustomer_Sex1_1_25_sound_name = "v_Monica_AbbyCustomer_Sex1_1_25"
define v_Monica_AbbyCustomer_Sex1_1_sound_name = "v_Monica_AbbyCustomer_Sex1_1"
define v_Monica_AbbyCustomer_Sex2_1_25_sound_name = "v_Monica_AbbyCustomer_Sex2_1_25"
define v_Monica_AbbyCustomer_Sex2_1_sound_name = "v_Monica_AbbyCustomer_Sex2_1"

default ep22_4_abby_customer_monica_cum_zone = 0

define monicaAbbyCustomer1CorruptionRequired1 = 800 # Моника изменила свое решение и согласилась работать с клиентами Эбби вне эскорта
define monicaAbbyCustomer1CorruptionRequired2 = 820 # Моника согласилась поехать домой к Эбби и обслужить ее клиента
define monicaAbbyCustomer1CorruptionRequired3 = 830 # Моника не выгоняет клиента Эбби, терпит его домогательства
define monicaAbbyCustomer1CorruptionRequired4 = 850 # Моника не выгоняет клиента Эбби, соглашается на секс с ним
define monicaAbbyCustomer1CorruptionRequired5 = 880 # Моника проглотила сперму клиента Эбби

#call ep22_4_dialogues5_escort_1() # разговор с Эбби в ресторане
#call ep22_4_dialogues5_escort_2() # разговор с Эбби в ресторане, если Моника отказалась в первый раз
#call ep22_4_dialogues5_escort_3() # мысли перед домом Эбби до встречи с клиентом
#call ep22_4_dialogues5_escort_4() # комната Эбби, встреча с клиентом
#call ep22_4_dialogues5_escort_5() # мысли Моники после встречи с клиентом Эбби, если забрала все деньги
#call ep22_4_dialogues5_escort_5a() # мысли Моники после встречи с клиентом Эбби, если оставила треть денег Эбби
#call ep22_4_dialogues5_escort_6() # мысли Моники после встречи с клиентом Эбби, если выгнала его и не стала с ним работать
#call ep22_4_dialogues5_escort_7() # мысли Моники после встречи с клиентом Эбби, хочет вернуться или пришла в любой другой день
#call ep22_4_dialogues5_escort_8() # Моника пришла в эскорт после того, как отработала с клиентом Эбби, разговор с Эбби


# при условии, если Моника была в гостях у Эбби
# ресторан отеля Ле Гранд
label ep22_4_dialogues5_escort_1:
    # у входа в ресторан, перед столиками Моника видит Эбби
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Poppers_and_Prosecco
    imgfl 30003
    w
    imgf 30005
    abby "[monica_hotel_name], привет."
    abby "Как у тебя дела?"
    mt "Какая ей разница, как у меня дела?!"
    mt "!!!"
    imgd 35044
    mt "Так, Моника, нужно быть более осторожной с этой Эбби."
    mt "Во-первых, она знает, кто главный в ВИП-эскорте."
    mt "Если я сделаю так, что она начнет мне доверять..."
    mt "То она поделится со мной этой информацией."
    music Stealth_Groover
    # если была в гостях у Линды
    if monicaLindaMirandaFriendship4 > 0:
        imgf 17527
        mt "Надеюсь, что она не знает о моей 'дружбе' с лицемерками Линдой и Мирандой."
        mt "Если она что-то заподозрит, то ни о каком доверии и речи быть не может."
    # если Моника сука
    if monicaBitch == True:
        $ notif_monica()
        imgd 30015
        mt "Я сделаю все, чтобы обыграть этих проституток-эскортниц!"
        mt "Я здесь самая умная и только я достойна занять место администраторши!"
    # если бичность низкая
    else:
        imgd 30015
        mt "Не известно, насколько верно я поступаю, обманывая этих проституток..."
        mt "Но пока у меня нет иного выхода..."
        mt "Я вынуждена притворяться их подругой."
        #
    # Моника притворно
    fadeblack 1.5
    music Poppers_and_Prosecco
    imgfl 30004
    m "Привет, Эбби."
    m "Все нормально. Как у тебя дела?"
    abby "У меня всегда все окей."
    abby "Я хотела спросить тебя..."
    # если Моника согласилась работать с клиентами Эбби
    if monicaAbbyRentHelp7 > 0:
        imgf 41422
        abby "Как у тебя с доходами от работы в эскорте?"
        m "Могло быть и лучше..."
        abby "Отлично. Значит, ты будешь заинтересована в подработке..."
        label ep22_4_dialogues5_escort_1a:
        music Groove2_85
        imgd 30006
        abby "Мне сегодня позвонил один из моих клиентов вне ВИП-эскорта."
        abby "Хочет встретиться, а у меня на него нет времени."
        abby "Да и желания особого нет с ним встречаться..."
        imgd 41424
        m "Что за клиент?"
        abby "Да он нормальный чувак. Жадный немного, но в целом пойдет... Если совсем нет денег."
        abby "Короче, я сейчас ему позвоню и скажу, что его обслужит моя напарница, то есть ты."
        sound Jump2
        img 35045 hpunch
        m "Подожди-подожди! Что, прямо сегодня?!"
        abby "Ага."
        m "А где?"
        abby "У меня дома. Я встречаюсь с этими клиентами только там."
        abby "В ВИП-эскорте никто об этом не должен узнать."
        imgd 35046
        abby "Мне не нужны лишние проблемы с администраторшей."
        abby "Ну что? Ты готова?"
        mt "Черт!"
        mt "!!!"
        # коррапшн
        $ menu_corruption = [monicaAbbyCustomer1CorruptionRequired2, 0]
        menu:
            "Да, готова.":
                $ monicaAbbyNoEscortClient1 = day # Моника согласилась поехать домой к Эбби и встретиться с ее клиентом вне эскорта
                pass
            "Нет!":
                # Моника недовольно
                music Stealth_Groover
                imgf 35047
                mt "Я не собираюсь возиться с этими извращенцами!"
                mt "Еще и дома у этой проститутки-эскортницы!"
                mt "Не смотря на то, что мне нужны деньги, я не хочу идти на это!"
                mt "По крайней мере, не сегодня!"
                music Groove2_85
                imgd 41426
                m "Нет, Эбби! На сегодня у меня другие планы!"
                m "Возможно, в следующий раз..."
                imgd 41425
                abby "Окей. Как знаешь."
                abby "Если что - обращайся."
                # Эбби отходит от Моники
                fadeblack
                sound highheels_short_walk
                pause 2.0
                return False
    # если Моника в первый раз отказалась работать с клиенами Эбби
    else:
        imgf 41422
        abby "Ты не передумала насчет моего предложения?"
        m "Какого предложения?"
        music Groove2_85
        abby "Хорош тупить, [monica_hotel_name]!"
        m "!!!"
        imgd 30006
        abby "Я про своих клиентов вне ВИП-эскорта..."
        abby "Может, ты передумала и хочешь, чтобы я поделилась с тобой ими?"
        m "..."
        # коррапшн
        $ menu_corruption = [0, monicaAbbyCustomer1CorruptionRequired1]
        menu:
            "Отказаться!":
                # Моника задумчиво
                music Stealth_Groover
                imgd 35047
                mt "Она предлагает мне обслуживать каких-то нищебродов за гроши?!"
                mt "А сама хочет занять место на ресепшене?!"
                mt "Хитрая дешевая подстилка!"
                mt "!!!"
                mt "Это Я стану главной и буду решать, когда и под кого ты будешь ложиться!"
                mt "Сучка!!!"
                # Моника притворно улыбается
                music Groove2_85
                imgf 41426
                m "Мне хватает того, что я зарабатываю в отеле..."
                m "А когда ты станешь... Кхм... Главной..."
                m "Я буду зарабатывать еще лучше."
                m "Спасибо, что предложила."
                imgd 41425
                m "Если я по какой-то причине изменю свое решение, я дам тебе знать."
                abby "Окей. Как знаешь."
                abby "Если что - обращайся."
                # Эбби отходит от Моники
                fadeblack
                sound highheels_short_walk
                pause 2.0
                music Stealth_Groover
                imgf 30007
                mt "Не хватало мне еще возиться с каким-то жалким отребьем!"
                mt "Я найду способ заработать деньги без этой гадости!"
                mt "!!!"
                return False
            "Согласиться.":
                $ monicaAbbyNoEscortClient2 = day # Моника изменила свое решение и согласилась работать с клиентами Эбби
                music Pyro_Flow
                imgd 35047
                mt "Черт!"
                mt "Я должна каждую неделю отдавать этой мерзкой сикалявке Виктории $ 5 000!"
                # если должна Перри
                if fallingPathStarted == True:
                    mt "И еще выплачивать долг мерзкой Перри!"
                # если арендует апартаменты у Джека
                if slumsApartmentsRentActive == True:
                    mt "И платить за грязную дыру, которую мне сдает Джек!"
                    #
                imgd 41429
                mt "Мне нужны эти деньги!"
                mt "Но, Моника, неужели ты ради денег..."
                mt "Будешь обслуживать каких-то жалких, никчемных отбросов от Эбби?!"
                mt "Ты готова пойти на это?!"
                mt "?!?!?!"
                mt "Черт!!!"
                music Groove2_85
                imgf 41426
                m "Я... Я думаю, что..."
                m "Что я попробую..."
                imgd 41425
                abby "Окей!"
                abby "Ты приняла верное решение, [monica_hotel_name]."
                jump ep22_4_dialogues5_escort_1a
    label ep22_4_dialogues5_escort_1b:
    # Моника задумчиво
    music Groove2_85
    imgf 35048
    mt "Если я сейчас откажусь от встречи с ее гребаным клиентом..."
    mt "То рискую вообще ничего не заработать сегодня."
    mt "А мне нужны деньги."
    mt "Но это так отвратительно!"
    mt "!!!"
    music Hidden_Agenda
    imgd 35049
    mt "С другой стороны, возможно, мне стоит попробовать?"
    mt "Всего один раз..."
    mt "Зато я смогу заработать."
    mt "А если мне что-то не понравится..."
    mt "То я просто пошлю эту Эбби с ее дурацкими клиентами ко всем чертям!"
    mt "Да, я думаю, что это самое верное решение!"
    # Моника, притворно улыбаясь
    music Groove2_85
    imgf 35050
    m "Да, Эбби. Я поеду."
    abby "Окей. Я тогда сейчас позвоню клиенту."
    abby "Короче, слушай..."
    abby "Сейчас поедешь ко мне домой."
    imgd 35051
    abby "Первое правило - ты должна принять душ до работы с клиентом."
    m "Не логичнее это сделать после?"
    abby "Нет! Вообще-то, ты будешь обслуживать его на моей постели!"
    abby "Так что, сначала в душ, а потом - трах с ним."
    img 35052
    mt "Фу, как грубо!"
    mt "!!!"
    imgd 35053
    abby "И клиента, кстати, тоже отправь в душ! Это обязательно!"
    abby "Полотенце для душа можешь взять мое. Я его, по-моему, на кровати оставила."
    imgd 35052
    mt "Надеюсь, оно чистое!"
    mt "!!!"
    abby "К клиенту обращайся по имени. Его зовут Брайан."
    # Моника язвительно
    music Stealth_Groover
    imgf 35054
    m "Постараюсь не перепутать и не назвать его другим именем."
    m "Какие-то еще инструкции будут?"
    music Groove2_85
    abby "Да. У меня через стену живет один придурок."
    abby "Везде сует свой нос. Любитель поскандалить и поворчать."
    abby "На него внимания не обращай."
    abby "Если он будет надоедать, скажи ему 'пошел на хрен отсюда, трахаюсь с кем хочу' и он отстанет."
    sound Jump2
    img 35055 vpunch
    m "Что, так и сказать?!"
    m "Это же не прилично!"
    abby "Клиентов домой водить тоже неприлично."
    imgd 35056
    abby "Я снимаю всего-лишь одну комнату в общей квартире."
    abby "И ты, между прочим, не высокосветская леди, так что можно обойтись без реверансов."
    m "!!!" # зло
    # Эбби сосредоточенно
    abby "Так, вроде бы я все тебе сказала."
    imgf 35057
    m "Тогда я пошла."
    abby "А, вот еще!"
    abby "Треть денег, которые Брайан тебе заплатит, оставишь на столе."
    abby "Это будет мой процент."
    abby "Теперь все."
    fadeblack
    sound highheels_short_walk
    pause 2.0
    # затемнение, каблуки
    return True

# ресторан отеля Ле Гранд
# если Моника отказалась поехать к клиенту Эбби
# при клике на Эбби
label ep22_4_dialogues5_escort_2:
    # у входа в ресторан, перед столиками
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Poppers_and_Prosecco
    imgfl 35058
    w
    imgf 35059
    m "Привет, Эбби."
    abby "[monica_hotel_name], привет."
    abby "Что насчет подработки?"
    abby "Я с тем клиентом так и не встретилась."
    imgd 35048
    abby "А ему не терпится и он готов приехать в любую минуту."
    abby "Если ты готова, то я позвоню ему..."
    mt "Черт!"
    mt "!!!"
    # коррапшн
    $ menu_corruption = [monicaAbbyCustomer1CorruptionRequired2, 0]
    menu:
        "Да, готова.":
            $ monicaAbbyNoEscortClient1 = day # Моника согласилась поехать домой к Эбби и встретиться с ее клиентом вне эскорта
            jump ep22_4_dialogues5_escort_1b
        "Нет!":
            # Моника недовольно
            music Stealth_Groover
            imgd 35047
            mt "Я не собираюсь возиться с этими извращенцами!"
            mt "Еще и дома у этой проститутки-эскортницы!"
            mt "Не смотря на то, что мне нужны деньги, я не хочу идти на это!"
            mt "По крайней мере, не сегодня!"
            music Groove2_85
            imgf 35046
            m "Нет, Эбби! На сегодня у меня другие планы!"
            m "Возможно, в следующий раз..."
            abby "Окей. Как знаешь."
            abby "Если что - обращайся."
            fadeblack
            sound highheels_short_walk
            pause 2.0
            # Эбби отходит от Моники
            return False
    return

# мысли Моники перед домом Эбби, до встречи с клиентом
label ep22_4_dialogues5_escort_3:
    # не рендерить!!
    mt "Моника, ты понимаешь, что сейчас происходит?"
    mt "Ты сейчас пойдешь обслуживать какого-то отброса вместо проститутки Эбби!"
    mt "Ты действительно пойдешь на ЭТО?!"
    mt "Стоят ли эти деньги таких жертв с твоей стороны?!"
    mt "?!?!?!"
    return

# комната Эбби
label ep22_4_dialogues5_escort_4:
    # Моника заходит с отвращением на лице
    fadeblack
    sound snd_door_close1
    pause 1.5
    sound highheels_short_walk
    pause 2.0
    music Stealth_Groover
    imgfl 35063
    w
    imgf 35064
    mt "Детская комната!.."
    mt "В которой гребаная Эбби обслуживает своих гребаных клиентов!"
    mt "И теперь ты, Моника, будешь делать то же самое! Кошмар!"
    mt "Зачем я только согласилась на это безумие?!"
    mt "!!!"
    imgd 35065
    mt "Так, что мне нужно сделать сначала?"
    mt "Что там говорила эта проститутка Эбби?"
    mt "Принять самой душ, потом отправить туда клиента..."
    mt "Называть клиента только по имени."
    imgd 35066
    mt "Хмм... По-моему, я забыла его имя..."
    mt "Неважно! Обойдется!"
    mt "Еще я не обращалась по имени ко всяким ничтожествам!"
    mt "!!!"
    menu:
        "Принять душ.":
            pass
    # Моника подходит к кровати и смотрит на полотенце
    sound highheels_short_walk
    imgf 35067
    mt "Это же то полотенце, в котором проститутка Эбби брила свою... В общем, брилась."
    mt "Я к этому полотенцу даже прикасаться не хочу!.."
    mt "А мне придется воспользоваться им после душа! Фи!"
    # Моника тянет руку к полотенцу
    # затемение, шуршание одежы, шаги босиком
    # смена кадра
    # душ, Моника заходит и брезгливо оглядывается
    sound vjuh3
    imgd 35068
    w
    fadeblack
    sound snd_fabric1
    pause 2.0
    sound snd_door_close1
    pause 1.5
    music Groove2_85
    imgfl 35069
    w
    imgf 35070
    w
    imgd 35071
    mt "Фууу!!!"
    mt "Это что, общий душ?!"
    mt "Здесь такое все!.. Грязное!"
    imgd 35072
    mt "Моника, постарайся ни к чему не прикасаться!"
    mt "Ты сейчас быстро примешь душ и пойдешь в комнату..."
    # затемнение, кран, шум воды
    # Моника стоит в душе
    fadeblack
    sound barefoot_walk2
    pause 1.5
    music Groove2_85
    music2 snd_shower3
    imgfl 35073
    w
    imgf 35074
    mt "Как же все-таки приятно..."
    imgd 35075
    mt "Мне вода всегда помогала успокоиться..."
    imgf 35076
    mt "Очистить голову от лишних мыслей..."
    imgd 35077
    mt "Расслабиться..."
    imgf 35078
    mt "Мммм..."
    # хлопает дверь
    # Моника испуганно открывает глаза
    sound snd_door_close1
    pause 1.0
    music stop
    sound plastinka1b
    img 35079 hpunch
    mt "Это еще что такое?!"
    mt "Я что, не закрыла дверь?!"
    music Groove2_85
    imgd 35080
    m "Кто там?!"
    m "Вообще-то, здесь занято!"
    # к душевой кабинете подходит сосед Эбби
    music Turbo_Tornado
    imgd 35081
    neighbor2 "А ты кто такая?"
    neighbor2 "Что ты здесь делаешь?!"
    # Моника прикрывается руками или хватает полотенце и прикрывается им
    sound Jump2
    img 35082 vpunch
    m "Отвернулся быстро!"
    m "Ты что, не видишь, что перед тобой дама?!"
    neighbor2 "Тоже мне дама нашлась!"
    neighbor2 "Чего я там не видел?!"
    m "Отвернись!!!"
    img 35083
    neighbor2 "Еще чего!!!"
    neighbor2 "Это не твой душ! Ты чего сюда приперлась?!"
    m "Я!.. Мне!.."
    m "Мне Эбби разрешила!"
    imgd 35084
    neighbor2 "Эбби?! Шлюшка из соседней комнаты?!"
    neighbor2 "Так значит, ты ее подружка будешь?!"
    neighbor2 "Или коллега?!"
    m "Не твое дело!"
    music Pyro_Flow
    neighbor2 "Вот именно, что МОЕ дело!"
    imgd 35085
    neighbor2 "Устроили тут проститутошную, а я должен все это терперть?!"
    neighbor2 "Я буду жаловаться хозяину апартаментов!"
    neighbor2 "Какие-то дешевые шлюхи таскают сюда своих клиентов!"
    img 35086 vpunch
    neighbor2 "Идите на улице работать, проститутки!"
    neighbor2 "Я у себя же дома отлить не могу спокойно сходить из-за вас!"
    # Монику бомбит
    imgd 35087
    m "Ты где здесь проститутку увидел, придурок?!"
    m "Пошел вон отсюда, пока я полицию не вызвала!!!"
    imgd 35085
    neighbor2 "Вызывай! Полиция мне поверит, а не какой-то шлюхе!"
    img 35088 vpunch
    m "Я не шлюха!!!"
    m "Я скажу, что ты меня домогался и тебя посадят за решетку!"
    imgd 35089
    neighbor2 "Я?! Что я домогался тебя?!"
    neighbor2 "Нужна ты мне больно, грязная шлюшка."
    m "Кретин!!!"
    # сосед осматривает Монику с головы до ног
    music Turbo_Tornado
    imgf 35090
    w
    imgd 35091
    w
    imgf 35092
    neighbor2 "Если хочешь, чтоб я ушел, покажи мне свои сиськи."
    img 35093 vpunch
    m "ЧТООО?!"
    m "Совсем охренел, старый извращенец?!"
    m "А ну-ка пошел вон отсюда!"
    neighbor2 "Покажешь сиськи - не буду жаловаться хозяину апартаментов."
    # Моника зло его выталкивает из ванной комнаты
    sound vjuh3
    imgd 35094
    w
    img 35095
    m "ВООООН!"
    sound anger2
    img 35096 hpunch
    m "!!!"
    # остается одна
    fadeblack
    sound snd_door_close1
    pause 1.5
    music Power_Bots_Loop
    imgfl 35097
    mt "Какое-то безумие!!!"
    mt "Грязные отбросы общества позволяют себя так вести с тобой, Моника!"
    mt "Как он мог?!"
    mt "Мерзкий, противный старикашка!!!"
    mt "!!!"
    imgf 35098
    w
    music2 stop
    fadeblack 1.5
    music Groove2_85
    imgfl 35099
    mt "Нужно быстрее уходить отсюда!"
    mt "Вдруг он вернется! Не хочу видеть его..."
    # Моника прерывается на полуслове, т.к. в ванную комнату заходит клиент Эбби, Брайан
    sound snd_door_close1
    imgf 35100
    w
    music stop
    sound plastinka1b
    img 35101 hpunch
    mt "!!!"
    music Groove2_85
    mt "!!!!"
    brian "Ох ни хрена себе, какая у меня сегодня девка!"
    imgf 35102
    brian "Крошка Эбби не обманула, сказав, что мне понравится!"
    mt "О, нет! Это и есть клиент Эбби?!"
    brian "Познакомимся или сразу возьмешься за работу, а? Хе-хе!"
    # Моника растерянно
    imgd 35104
    m "Я..."
    m "Я [monica_hotel_name]..."
    brian "Зови меня Брайан."
    brian "Покажешь, что ты там прячешь под своим полотенцем?"
    img 35103
    m "Н-нет!"
    m "Сначала душ!"
    brian "Какая стеснительная малышка. Хе-хе-хе!"
    brian "Сегодня у Брайана будет отличный секс с новой телкой!"
    img 35105
    m "!!!"
    imgd 35106
    sound barefoot_walk2
    m "Я подожду тебя в коридоре!"
    imgd 35107
    w
    # Моника выбегает
    # затемнение, коридор возле душа
    # Моника стоит у стены, придерживая полотенце
    fadeblack
    sound snd_door_close1
    pause 1.5
    music Groove2_85
    imgfl 35108
    w
    imgf 35109
    mt "Что-то я все меньше уверена в своей адекватности..."
    mt "В тот момент, когда приняла предложение гребанной Эбби..."
    mt "Зачем я согласилась на это?!"
    mt "Что мне сейчас..."
    img 35110
    neighbor2 "Ага!"
    music Turbo_Tornado
    imgd 35111
    neighbor2 "Попалась, проститутка!"
    # сосед появляется неожиданно, Моника пугается
    m "!!!"
    m "!!!!"
    m "!!!!!"
    sound Jump2
    img 35112 vpunch
    m "Напугал меня!"
    m "Идиот!"
    neighbor2 "Думала, так легко от меня избавишься?!"
    m "Чего тебе нужно от меня?!"
    imgf 35113
    neighbor2 "Покажешь?"
    m "Что тебе показать?"
    neighbor2 "Свои сиськи."
    m "НЕТ!"
    # он зло на нее смотрит
    imgd 35114
    neighbor2 "Какая-то проститутка строит из себя леди!"
    img 35115
    mt "Я и есть Леди!"
    mt "Знал бы этот недоумок, кто перед ним стоит!"
    mt "!!!"
    imgf 35116
    neighbor2 "Только поглядите на нее!"
    neighbor2 "Кто там в душе сейчас? А?"
    neighbor2 "Очередной твой хмырь?"
    m "Сам ты хмырь!"
    neighbor2 "Собралась трахаться с ним?"
    sound Jump1
    img 35117 vpunch
    m "Тебя это не касается! Иди, куда шел!"
    neighbor2 "Невозможно больше жить в таких условиях!"
    neighbor2 "Устроили бордель!"
    neighbor2 "Спят с незнакомыми мужиками за деньги!"
    music Pyro_Flow
    mt "Все! Он меня достал!"
    imgd 35118
    m "Ты!"
    m "Импотент гребаный!"
    m "Тащи свою задницу подальше отсюда!"
    m "Пока я сама не нажаловалась на тебя хозяину апартаментов Гарри!"
    imgd 35119
    m "Одно мое слово и он вышвырнет тебя отсюда!"
    m "Мерзкий старикашка!"
    # он на нее удивленно смотрит
    music Groove2_85
    neighbor2 "Ты знаешь Гарри?"
    neighbor2 "Откуда?"
    # если у Моники был секс с Гарри
    if monicaAbbyRentHelp3 > 0:
        #
        $ notif(_("Моника переспала с Гарри по просьбе Кэндис."))
        #
    m "Он мой друг!!!"
    # сосед в замешательстве
    imgd 35120
    neighbor2 "Не надо ничего говорить Гарри."
    neighbor2 "Я пойду... У меня еще столько дел, а ты меня отвлекаешь своими пустыми разговорами..."
    # уходит и про себя ворчит, не смотря на Монику
    sound snd_barefoot3
    imgf 35121
    neighbor2 "Какая-то проститутка знает Гарри..."
    neighbor2 "Гарри хороший парень и не водится с такими, как она..."
    neighbor2 "С Гарри она дружит..."
    neighbor2 "Так я и поверил!.."
    music Power_Bots_Loop
    imgd 35122
    mt "Какой же этот сосед отвратительный тип!"
    mt "ААААА!!!"
    mt "Ненавижу!!!"
    mt "!!!"
    # из ванной комнаты выходит клиент
    fadeblack
    sound snd_door_close1
    pause 1.5
    music Groove2_85
    imgfl 35123
    brian "Малышка! Я готов!"
    imgf 35124
    m "Наконец-то!"
    brian "Тебе так не терпится? Хе-хе!"
    brian "Пошли скорее!" # хлопает Монику по попе
    #sound Jump1
    sound snd_slap1
    img 35125 vpunch
    w
    img 35126
    m "!!!"
    # затемнение
    # смена кадра, комната Эбби
    # заходит Моника, следом клиент
    # он тянет ее за руку к себе
    fadeblack
    sound barefoot_walk2
    pause 1.5
    sound snd_door_close1
    pause 1.5
    music Groove2_85
    imgfl 35127
    w
    imgf 35128
    w
    sound wow
    imgd 35129
    w
    sound Jump1
    img 35130 hpunch
    brian "Иди сюда, малышка!"
    # начинает лапать за попу, грудь
    img 35131
    w
    imgd 35132
    w
    sound Jump2
    img 35133 vpunch
    w
    imgd 35134
    brian "Сейчас я с тобой буду делать все, что захочу!"
    imgf 35135
    brian "Какая ты сексуальная! Мммм!"
    # лезет рукой под полотенце на попе
    imgd 35136
    w
    imgf 35137
    brian "Такая аппетитная! Идем скорее на кровать!"
    music Pyro_Flow
    imgd 35138
    mt "Боже, как все это мерзко и грязно!"
    mt "Я вижу его впервые в своей жизни и даже не запомнила его имени!"
    mt "А он меня уже всю облапал своими ручищами!"
    mt "Грязный никчемный людишка!"
    mt "!!!"
    # коррапшн
    $ menu_corruption = [monicaAbbyCustomer1CorruptionRequired3, 0]
    menu:
        "Терпеть клиента Эбби.":
            pass
        "Выгнать его!":
            imgf 35139
            mt "Я, Моника Бакфетт!"
            mt "Леди из высшего общества и владелица многомиллионного бизнеса!"
            mt "Я мечта любого мужчины этого города и даже страны!"
            mt "И я не позволю какому-то грязному отребью прикасаться ко мне!"
            # Моника его отталкивает
            sound snd_punch_face
            img 35140 hpunch
            m "Хватит!"
            imgd 35141
            m "Убери свои руки!"
            sound vjuh3
            img 35142 vpunch
            brian "Эй, малышка! Ты чего?!"
            m "Ничего! Я не буду работать!"
            sound Jump1
            img 35143
            brian "В смысле?! Ты прикалываешься?!"
            imgd 35144
            m "Уходи!"
            brian "Но как же?.. Ведь Эбби..."
            img 35145
            m "Мне наплевать, что тебе пообещала Эбби!"
            m "Я не буду работать!"
            m "Пошел вон отсюда!!!"
            sound man_steps
            imgf 35146
            brian "Дура!"
            fadeblack
            sound snd_door_close1
            pause 1.5
            return False
    # клиент продолжает лапать Монику и ведет ее к кровати
    fadeblack 1.5
    music Groove2_85
    imgfl 35147
    w
    imgf 35148
    mt "Мне нужно успокоиться!"
    mt "Глубокий вдох - выдох..."
    imgd 35149
    mt "Скоро, совсем скоро, этот кошмарный сон закончится!"
    mt "Если я все сделаю правильно, то совсем скоро Я буду зарабатывать деньги на том..."
    imgd 35150
    mt "Что эти проститутки будут обслуживать разных козлов!"
    mt "И буду штрафовать их! Всех! Особенно, Эбби!"
    mt "!!!"
    # он валит ее на кровать и срывает полотенце
    sound Jump2
    img 35151 vpunch
    brian "Ну что, малышка! С чего начнем, а?"
    # Моника молча зло на него смотрит
    imgd 35152
    m "!!!"
    brian "Скажи мне для начала, как ты хочешь мой член!"
    # Моника продолжает зло молчать
    imgd 35153
    mt "Ни за что!"
    mt "Озабоченное грязное животное!"
    mt "!!!"
    imgf 35154
    brian "Говори! Я хочу услышать это!"
    brian "Хочешь его? Посмотри!"
    # достает свой стояк
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Groove2_85
    imgf 35155
    brian "Смотри, какой он огромный!"
    imgd 35156
    brian "Тебе ведь не терпится ощутить его внутри, да?"
    # Моника зло на него смотрит
    music Power_Bots_Loop
    img 35157
    mt "Никто и никогда не слышал от Моники Бакфетт эти слова!"
    mt "И не услышит!!!"
    mt "!!!"
    music Groove2_85
    imgf 35158
    brian "Вижу по глазам, что не терпится! Хе-хе!"
    brian "Все девки, как только видят его, готовы сразу раздвинуть ноги!"
    brian "И ты тоже хочешь!"
    img 35159
    mt "Фу! Нет!"
    mt "Мразь!"
    imgd 35160
    brian "Сейчас я удовлетворю тебя, малышка!"
    brian "Я буду трахать тебя, как никто и никогда, да!"
    brian "Раком!"
    img 35161 hpunch
    m "Что?!"
    brian "Повернулась ко мне задом и встала раком! Быстро!"
    mt "!!!"
    # коррапшн
    $ menu_corruption = [monicaAbbyCustomer1CorruptionRequired4, 0]
    menu:
        "Сделать, как говорит клиент.":
            $ monicaAbbyNoEscortClient3 = day # Моника согласилась на секс с клиентом Эбби, не стала выгонять его
            pass
        "Выгнать его!":
            music Pyro_Flow
            imgf 35162
            mt "Я, Моника Бакфетт!"
            mt "Леди из высшего общества и владелица многомиллионного бизнеса!"
            mt "Я мечта люього мужчины этого города и даже страны!"
            imgd 35163
            mt "И я не позволю какому-то грязному отребью прикасаться ко мне!"
            # Моника его отталкивает
            sound anger2
            img 35164 vpunch
            m "Хватит!"
            img 35165
            m "Убери свои руки!"
            brian "Эй, малышка! Ты чего?!"
            m "Ничего! Я не буду работать!"
            imgd 35166
            brian "В смысле?! Ты прикалываешься?!"
            m "Уходи!"
            sound Jump1
            img 35167 vpunch
            brian "Но как же?.. Ведь Эбби..."
            m "Мне наплевать, что тебе пообещала Эбби!"
            imgd 35168
            m "Я не буду работать!"
            m "Пошел вон отсюда!!!"
            sound man_steps
            imgf 35169
            brian "Дура!"
            fadeblack
            sound snd_door_close1
            pause 1.5
            return False
    # Моника недовольно
    music Pyro_Flow
    imgf 35162
    mt "Грубый, неотесанный мужлан!"
    mt "Теперь я понимаю, почему гребаная Эбби не хочет с ним сама работать!"
    mt "Подсунула мне этого идиота! Сучка Эбби!"
    mt "!!!"
    imgd 35163
    mt "Так, Моника, если уж ты решилась на это..."
    mt "То нужно быть сильной и довести это дело до конца!"
    mt "Думай о том, что скоро все это закончится..."
    mt "А в твоем кармане станет больше денег!"
    # Моника встает в коленно-локтевую, лицо злое
    fadeblack 1.5
    music Loved_Up
    imgfl 35170
    w
    imgf 35171
    w
    imgd 35158
    brian "О, дааа! Какая послушгая малышка!"
    # он лапает ее попу
    imgf 35172
    brian "Какая у тебя бархатная кожа... Мммм..."
    sound vjuh3
    imgd 35173
    brian "Как ты обалденно пахнешь..."
    sound vjuh3
    imgd 35172
    w
    sound vjuh3
    imgd 35173
    w
    imgf 35174
    brian "Кайфовая шлюшка от Эбби! Хе-хе!"
    brian "Как там тебя зовут? Напомни, я забыл."
    mt "Ты не достоин произносить мое имя, никчемный неудачник!"
    mt "Даже дышать на меня не достоин, тварь!"
    imgd 35175
    brian "Имя!"
    brian "Иначе буду называть грязной шлюшкой или сучкой!"
    # шлепает ее по попе
    imgf 35176
    w
    sound snd_slap1
    img 35177 hpunch
    sound2 snd_monica_ahh
    w
    img 35178
    m "Ай! [monica_hotel_name]!"
    brian "Другое дело!"
    brian "Кайфовая шлюшка [monica_hotel_name]..."
    brian "Сейчас я войду в тебя своим огромным членом!"
    # пристраивает член к киске Моники
    imgf 35179
    w
    imgd 35181
    brian "Ты жаждешь почувствовать его?"
    brian "Да, ты мечтаешь о нем!"
    # входит в нее
    imgf 35179
    w
    sound chpok6
    img 35180 vpunch
    brian "Дааа!"
    imgd 35182
    w
    imgf 35184
    w

    # video
    #1 -25
    $ localSoundVolume = 1.0
    $ localSoundName = v_Monica_AbbyCustomer_Sex1_1_25_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_AbbyCustomer_Sex1_1_25= Movie(play="video/v_Monica_AbbyCustomer_Sex1_1_25.mkv")
    show videov_Monica_AbbyCustomer_Sex1_1_25
    with fade
    brian "О, какая бархатная киска у шлюшки [monica_hotel_name]!"
    wclean
    brian "Еееее!!!"
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    # начинает пялить ее, жестко
    imgf 35183
    w

    #2 -25
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_AbbyCustomer_Sex1_2_25= Movie(play="video/v_Monica_AbbyCustomer_Sex1_2_25.mkv")
    show videov_Monica_AbbyCustomer_Sex1_2_25
    with fade
    brian "Не будь ты шлюшкой, я всегда бы тебя трахал!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 35185
    brian "Дааа!"
    imgd 35186
    w

    #3 -25
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_AbbyCustomer_Sex1_3_25= Movie(play="video/v_Monica_AbbyCustomer_Sex1_3_25.mkv")
    show videov_Monica_AbbyCustomer_Sex1_3_25
    with fade
    brian "Теперь я твой постоянный клиент!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 35187
    w

    # video
    #4
    $ localSoundVolume = 1.0
    $ localSoundName = v_Monica_AbbyCustomer_Sex1_1_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_AbbyCustomer_Sex1_4= Movie(play="video/v_Monica_AbbyCustomer_Sex1_4.mkv")
    show videov_Monica_AbbyCustomer_Sex1_4
    with fade
    brian "Буду покупать тебя и трахать!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 35188
    w

    #5
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_AbbyCustomer_Sex1_5= Movie(play="video/v_Monica_AbbyCustomer_Sex1_5.mkv")
    show videov_Monica_AbbyCustomer_Sex1_5
    with fade
    brian "Трахать-трахать!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    #6
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_AbbyCustomer_Sex1_6= Movie(play="video/v_Monica_AbbyCustomer_Sex1_6.mkv")
    show videov_Monica_AbbyCustomer_Sex1_6
    with fade
    brian "Аааа!!!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    # хватает ее за волосы на затылке (как у товарища ICSTOR'a)
    # продолжает пялить и держать за волосы
    imgf 35189
    w
    imgd 35190
    w
    imgd 35251
    w
    sound Jump2
    img 35191 vpunch
    sound2 snd_monica_ahh
    m "Что ты делаешь?!"
    img 35192
    m "Мне больно!!!"
    brian "Аааа!!!"
    brian "Кааайф!"
    imgf 35194
    m "Отпусти мои волосы, придурок!"
#    w

    # video
    #1 -25
    $ localSoundVolume = 1.0
    $ localSoundName = v_Monica_AbbyCustomer_Sex2_1_25_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_AbbyCustomer_Sex2_1_25= Movie(play="video/v_Monica_AbbyCustomer_Sex2_1_25.mkv")
    show videov_Monica_AbbyCustomer_Sex2_1_25
    with fade
    m "Хватит! Ааай!!!"
    wclean
    brian "Поверещи еще, шлюшка [monica_hotel_name]! Меня это заводит еще больше!"
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 35193
    w

    #2 -25
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_AbbyCustomer_Sex2_2_25= Movie(play="video/v_Monica_AbbyCustomer_Sex2_2_25.mkv")
    show videov_Monica_AbbyCustomer_Sex2_2_25
    with fade
    brian "ДАА!!!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 35198
    w
    imgd 35196
    w
    sound hlup25
    imgd 35197
    w
    sound hlup25
    imgd 35196
    w
    sound hlup25
    imgd 35197
    w
    imgf 35195
    w

    #3 -25
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_AbbyCustomer_Sex2_3_25= Movie(play="video/v_Monica_AbbyCustomer_Sex2_3_25.mkv")
    show videov_Monica_AbbyCustomer_Sex2_3_25
    with fade
    brian "Чертовски охренительно!!!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 35199
    mt "Грязная скотина!"
    mt "Чертов садист!"
    mt "Ублюдок!!!"
    mt "!!!"
    # внезапно в дверь раздается громкий стук
    sound snd_door_knock
    pause 0.5
    sound2 Jump1
    img 35200 vpunch
    w

    #4 -25
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_AbbyCustomer_Sex2_4_25= Movie(play="video/v_Monica_AbbyCustomer_Sex2_4_25.mkv")
    show videov_Monica_AbbyCustomer_Sex2_4_25
    with fade
    mt "!!!!"
    wclean
    mt "!!!!!"
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    #5 -25
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_AbbyCustomer_Sex2_5_25= Movie(play="video/v_Monica_AbbyCustomer_Sex2_5_25.mkv")
    show videov_Monica_AbbyCustomer_Sex2_5_25
    with fade
    neighbor2 "Развели тут бордель!"
    wclean
    mt "!!!!!"
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    imgf 35245
    neighbor2 "Устроили проститутошную!"
    sound snd_door_knock
    imgd 35246
    neighbor2 "Хватит так скрипеть кроватью!"

    #6 -25
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_AbbyCustomer_Sex2_6_25= Movie(play="video/v_Monica_AbbyCustomer_Sex2_6_25.mkv")
    show videov_Monica_AbbyCustomer_Sex2_6_25
    with fade
    brian "Ееее!"
    wclean
    neighbor2 "На весь этаж вас слышно, бесстыдники!"
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")


    $ ep22_4_dialogues5_escort_4_loop1_flag = False
label ep22_4_dialogues5_escort_4_loop1:

    music Turbo_Tornado
    imgf 35201
    sound snd_door_knock
    mt "!!!"

    menu:
        "Уйди вон!":
            #7 -25
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_AbbyCustomer_Sex2_7_25= Movie(play="video/v_Monica_AbbyCustomer_Sex2_7_25.mkv")
            show videov_Monica_AbbyCustomer_Sex2_7_25
            with fade
            m "Чеееерт!!!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 35202
            sound snd_door_knock
            m "Уйди вон!"
            imgd 35247
            neighbor2 "Я не уйду! Это возмутительно!"
            jump ep22_4_dialogues5_escort_4_loop1
        "Я сейчас полицию вызову!":
            #5 -25
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_AbbyCustomer_Sex2_5_25= Movie(play="video/v_Monica_AbbyCustomer_Sex2_5_25.mkv")
            show videov_Monica_AbbyCustomer_Sex2_5_25
            with fade
            neighbor2 "Развели тут бордель!"
            wclean
            mt "!!!!!"
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 35203
            sound snd_door_knock
            m "Я сейчас полицию вызову!"
            imgd 35248
            neighbor2 "Я сам тебя в полицию сдам, проститутка окаянная!"
            jump ep22_4_dialogues5_escort_4_loop1
        "Отстань от меня, старый извращенец!":
            #4 -25
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_AbbyCustomer_Sex2_4_25= Movie(play="video/v_Monica_AbbyCustomer_Sex2_4_25.mkv")
            show videov_Monica_AbbyCustomer_Sex2_4_25
            with fade
            mt "!!!!"
            wclean
            mt "!!!!!"
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 35202
            sound snd_door_knock
            m "Отстань от меня, старый извращенец!"
            imgd 35249
            neighbor2 "Устроила тут проститутошную, а меня извращенцем называет!"
            neighbor2 "Бесстыдница!!!"
            jump ep22_4_dialogues5_escort_4_loop1
        "Ты меня достал! Отвали!":
            $ ep22_4_dialogues5_escort_4_loop1_flag = True
            imgf 35203
            sound snd_door_knock
            w

            #8 -25
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_AbbyCustomer_Sex2_8_25= Movie(play="video/v_Monica_AbbyCustomer_Sex2_8_25.mkv")
            show videov_Monica_AbbyCustomer_Sex2_8_25
            with fade
            brian "ДАА!!!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            #9 -25
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_AbbyCustomer_Sex2_9_25= Movie(play="video/v_Monica_AbbyCustomer_Sex2_9_25.mkv")
            show videov_Monica_AbbyCustomer_Sex2_9_25
            with fade
            m "Ты меня достал! Отвали!"
            wclean
            neighbor2 "Окаянная шлюха!"
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 35250
            neighbor2 "Весь этаж слышит, что ты тут устроила!"
            jump ep22_4_dialogues5_escort_4_loop1
        "Пошел на хрен отсюда! Трахаюсь, с кем хочу!" if ep22_4_dialogues5_escort_4_loop1_flag == True:
            sound snd_door_knock
            imgf 35204
            w

            # video
            #10
            $ localSoundVolume = 1.0
            $ localSoundName = v_Monica_AbbyCustomer_Sex2_1_sound_name
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_AbbyCustomer_Sex2_10= Movie(play="video/v_Monica_AbbyCustomer_Sex2_10.mkv")
            show videov_Monica_AbbyCustomer_Sex2_10
            with fade
            m "Пошел на хрен отсюда! Трахаюсь, с кем хочу!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            pass
    # стук замолкает
    imgf 35199
    mt "Старый извращенец!!!"
    mt "!!!"
    # он резко выходит из нее и, продолжая держать за волосы, подставляет к ее губам свой член
    imgd 35180
    w
    sound chpok6
    img 35179 vpunch
    w
    fadeblack 1.5
    music Groove2_85
    imgf 35205
    w
    imgd 35206
    brian "Оближи его! Быстро!"
    img 35207
    mt "Дьявол!"
    mt "Он толко что был внутри моей... Внутри меня!"
    mt "Я должна теперь это все слизать?!"
    imgd 35208
    m "Но!.."
    # он водит членом по лицу Моники
    imgf 35207
    w
    sound Jump1
    imgd 35209
    mt "Фууу!"
    brian "Бери его в рот! Выполняй!"
    menu:
        "Сделать, как говорит клиент. (Extra animated version)" if game.extra == True:
            # Моника открывает рот
            fadeblack 1.5
            music Loved_Up
            imgfl 35212
            brian "В глаза мне смотри, шлюшка [monica_hotel_name]!"
            # Моника поднимает взгляд и с ненавистью смотрит на него
            imgf 35210
            brian "Вот тааак!"
            # он резко и глубоко вводит свой член
            # Моника давится
            sound chpok6
            img 35211 vpunch
            m "Мммпфф!!!"
            sound chavc6
            img 35213 hpunch
            w
            imgd 35214
            m "Мпфхфпфф!!!"
            brian "Ееее! Каааайф!"
            imgf 35215
            w

            # video
            #1 -25
            $ localSoundVolume = 1.0
            $ localSoundName = v_Monica_AbbyCustomer_Blowjob1_1_25_sound_name
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_AbbyCustomer_Blowjob1_1_25= Movie(play="video/v_Monica_AbbyCustomer_Blowjob1_1_25.mkv")
            show videov_Monica_AbbyCustomer_Blowjob1_1_25
            with fade
            brian "Давай, работай!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 35216
            w

            #2 -25
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_AbbyCustomer_Blowjob1_2_25= Movie(play="video/v_Monica_AbbyCustomer_Blowjob1_2_25.mkv")
            show videov_Monica_AbbyCustomer_Blowjob1_2_25
            with fade
            brian "Ооо, какая шлюшкааа!"
            wclean
            brian "Дааа!"
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 35217
            w

            # video
            #3 -25
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_AbbyCustomer_Blowjob1_3_25= Movie(play="video/v_Monica_AbbyCustomer_Blowjob1_3_25.mkv")
            show videov_Monica_AbbyCustomer_Blowjob1_3_25
            with fade
            brian "Оооо, какая ты клевая!"
            wclean
            brian "Ммммм..."
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            #4
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_AbbyCustomer_Blowjob1_4_25= Movie(play="video/v_Monica_AbbyCustomer_Blowjob1_4_25.mkv")
            show videov_Monica_AbbyCustomer_Blowjob1_4_25
            with fade
            brian "Каааайф!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            #5
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_AbbyCustomer_Blowjob1_5_25= Movie(play="video/v_Monica_AbbyCustomer_Blowjob1_5_25.mkv")
            show videov_Monica_AbbyCustomer_Blowjob1_5_25
            with fade
            brian "Давай, шлюшка, соси старательнее!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            imgf 35213
            sound chavc6
            w
            imgd 35214
            w
            sound chpok6
            imgd 35213
            w
            sound chpok6
            imgd 35214
            w

            #6
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_AbbyCustomer_Blowjob1_6_25= Movie(play="video/v_Monica_AbbyCustomer_Blowjob1_6_25.mkv")
            show videov_Monica_AbbyCustomer_Blowjob1_6_25
            with fade
            brian "Вижу, как ты тащишься от моего огромного члена!"
            wclean
            m "Мпфхфпфф!!!"
            brian "Дааа!"
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            music Loved_Up2
            imgf 35218
            w

            #7
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_AbbyCustomer_Blowjob1_7_25= Movie(play="video/v_Monica_AbbyCustomer_Blowjob1_7_25.mkv")
            show videov_Monica_AbbyCustomer_Blowjob1_7_25
            with fade
            brian "Еще немного!!! Ооооо!!!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

        "Сделать, как говорит клиент. (animated scene in Extra version) (disabled)." if game.extra == False:
            pass

        "Сделать, как говорит клиент." if game.extra == False:
            # Моника открывает рот
            fadeblack 1.5
            music Loved_Up
            imgfl 35212
            brian "В глаза мне смотри, шлюшка [monica_hotel_name]!"
            # Моника поднимает взгляд и с ненавистью смотрит на него
            imgf 35210
            brian "Вот тааак!"
            # он резко и глубоко вводит свой член
            # Моника давится
            sound chpok6
            img 35211 vpunch
            m "Мммпфф!!!"
            sound chavc6
            img 35213 hpunch
            w
            imgd 35214
            m "Мпфхфпфф!!!"
            brian "Ееее! Каааайф!"
            imgf 35215
            brian "Давай, работай!"
            imgd 35216
            brian "Ооо, какая шлюшкааа!"
            brian "Дааа!"
            imgf 35217
            brian "Оооо, какая ты клевая!"
            brian "Каааайф!"
            brian "Давай, шлюшка, соси старательнее!"
            imgd 35213
            sound chavc6
            w
            imgd 35214
            w
            sound chpok6
            imgd 35213
            w
            sound chpok6
            imgd 35214
            brian "Вижу, как ты тащишься от моего огромного члена!"
            sound chpok6
            imgd 35213
            w
            sound chpok6
            imgd 35214
            m "Мпфхфпфф!!!"
            sound chpok6
            imgd 35213
            w
            sound chpok6
            imgd 35214
            brian "Дааа!"
            music Loved_Up2
            imgf 35218
            brian "Еще немного!!! Ооооо!!!"
            pass

    menu:
        "Кончить в рот Моники.":
            $ ep22_4_abby_customer_monica_cum_zone = 1
            imgf 35217
            brian "Аааа! Сейчас я кончу тебе в рот, шлюшка [monica_hotel_name]!"
            img 35214
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan18
            brian "Даааа!!!"
            img 35219
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan18
            sound2 hlup25
            brian "АААААА!!"
            imgf 35220
            w
            imgd 35221
            brian "Глотай!"
            $ menu_corruption = [monicaAbbyCustomer1CorruptionRequired5, 0]
            menu:
                "Проглотить.":
                    imgf 35222
                    sound snd_gulp
                    mt "Фууу!"
                    imgd 35223
                    mt "Мерзость!!!"
                    $ add_corruption(5, "monica_abby_customer_blowjob_sperm")
                    imgd 35224
                    mt "Меня сейчас стошнит!"
                "Выплюнуть!":
                    imgf 35225
                    sound chavc26
                    mt "Фууу!"
                    imgd 35226
                    w
                    imgd 35227
                    mt "Мерзость!!!"
            pass
        "Кончить на лицо Моники.":
            $ ep22_4_abby_customer_monica_cum_zone = 2
            imgf 35217
            brian "Аааа! Хочу обкончать твое лицо, шлюшка [monica_hotel_name]!"
            imgd 35214
            w
            img 35228
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan18
            brian "Даааа!!!"
            img 35229
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan18
            sound2 hlup25
            brian "АААААА!!"
            imgf 35230
            w
            pass
        "Кончить на грудь Моники.":
            $ ep22_4_abby_customer_monica_cum_zone = 3
            imgf 35217
            brian "Аааа! Сейчас я кончу тебе на сиськи, шлюшка [monica_hotel_name]!"
            imgd 35211
            w
            img 35231
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan18
            brian "Даааа!!!"
            img 35232
            sound bulk1
            show screen photoshot_screen()
            with hpunch
            pause 0.7
            hide screen photoshot_screen
            sound man_moan18
            sound2 hlup25
            brian "АААААА!!"
            imgf 35233
            w
            pass
    # он довольно отстраняется от нее, Моника злая
    fadeblack 1.5
    music Pyro_Flow
    img 35234 vpunch
    mt "Сволочь!!!"
    mt "!!!"
    imgf 35235
    brian "Повторим, малышка?"
    brian "Хочу еще раз войти в твою киску."
    m "Нет!!!"
    m "Твое время вышло!!!"
    imgd 35236
    m "А благотворительностью я не занимаюсь!!!"
    m "Деньги на стол и иди отсюда!"
    music Groove2_85
    brian "Хе-хе! Какая ты строптивая, шлюшка [monica_hotel_name]..."
    brian "Мне это нравится!"
    imgd 35237
    brian "Я к тебе вернусь совсем скоро. Хе-хе!"
    # затемнение, шаги, дверь
    # Моника стоит посередине комнаты, одетая
    fadeblack
    sound snd_fabric1
    pause 2.0
    sound snd_door_close1
    pause 1.5
    music Power_Bots_Loop
    imgf 35238
    mt "Поверить не могу, что я сделала это!"
    mt "Терпеть такое унижение ради заработка!.."
    mt "Разве эта цель оправдывает средства?"
    imgd 35239
    mt "Это было омерзительно!!!"
    mt "Гадко!!!"
    mt "Тошнотворно!!!"
    mt "!!!"
    # Моника смотрит на стол, на котором лежат деньги
    music Groove2_85
    imgd 35240
    mt "Хмм..."
    mt "Интересно, сколько этот неудачник-садист оставил денег?"
    # подходит к тумбочке
    sound highheels_short_walk
    imgf 35241
    mt "150 долларов?!"
    mt "Всего?! За то, что мне пришлось вытерпеть?!"
    music Pyro_Flow
    mt "Жадный ублюдок!!!"
    mt "Урод! Скотина!"
    img 35242
    mt "Ненавижу, тварь!"
    mt "!!!"
    mt "И мне еще треть отдавать гребаной Эбби?!"
    mt "..."
    # бичность
    menu:
        "Оставить $ 50 на столе и уйти." if monicaBitch == False: # низкая бичность
            $ monicaAbbyNoEscortClient5 = day # Моника оставила Эбби процент
            music Stealth_Groover
            imgf 35244
            mt "Пусть эта никчемная проститутка Эбби подавится своими $ 50!"
            mt "Придет время и я отомщу ей за это!"
            mt "Будет обслуживать самых грязных извращенцев за копейки!!!"
            mt "!!!"
            $ add_money(100.0)
            # оставляет 50 баксов, себе забирает 100
            # затемнение
            pass
        "Оставить $ 50 на столе и уйти. (Моника недостаточно приличная) (disabled)" if monicaBitch == True:
            pass
        "Забрать все деньги и уйти.":
            $ monicaAbbyNoEscortClient4 = day # Моника не оставила Эбби процент, забрала все деньги
            music Stealth_Groover
            imgf 35243
            mt "Пошла она к черту!"
            mt "Я заработала эти деньги!"
            mt "Они все мои, до последнего цента!"
            $ add_money(150.0)
            # забирает все деньги
            # затемнение
            pass
    fadeblack
    sound highheels_short_walk
    pause 2.0
    sound snd_door_close1
    pause 1.5
    return True

# мысли Моники после встречи с клиентом Эбби, если забрала все деньги
label ep22_4_dialogues5_escort_5:
    # не рендерить!!
    mt "Я считаю, что поступила правильно, забрав все деньги!"
    mt "Мне пришлось терпеть этого мерзкого клиента!"
    mt "И я не обязана делиться ни с кем этим заработком!"
    mt "Я придумаю, что сказать гребаной Эбби!"
    mt "Пошла она!"
    return

# мысли Моники после встречи с клиентом Эбби, если оставила треть денег Эбби
label ep22_4_dialogues5_escort_5a:
    # не рендерить!!
    mt "Черт! Может, нужно было забрать все деньги?"
    mt "Наврала бы гребаной Эбби, что клиент не заплатил..."
    mt "..."
    mt "Нет, лучше так не рисковать. Эта Эбби не так проста, как может показаться."
    mt "Мне нужно втереться к ней в доверие."
    mt "Придет время и я припомню ей этого мерзкого клиента!"
    return

# мысли Моники после встречи с клиентом Эбби, если выгнала его и не стала с ним работать
label ep22_4_dialogues5_escort_6:
    # не рендерить!!
    mt "Это было омерзительно!!!"
    mt "Гадко!!!"
    mt "Ненавижу, тварь!"
    mt "Какого черта эта Эбби подсунула мне этого придурка?!"
    mt "!!!"
    return

# мысли Моники после встречи с клиентом Эбби, хочет вернуться или пришла в любой другой день
label ep22_4_dialogues5_escort_7:
    # не рендерить!!
    mt "Мне нечего здесь делать сейчас..."
    return

label ep22_4_dialogues5_escort_7a:
    mt "Мне нужно надеть свое красивое платье."
    return


# Моника пришла в эскорт после того, как отработала с клиентом Эбби
label ep22_4_dialogues5_escort_8:
    # Эбби встречает ее на входе в ресторан
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 35058
    w
    imgf 35059
    m "Привет, Эбби."
    abby "[monica_hotel_name], привет."
    abby "Как ты отработала с Брайаном? Все окей?"
    # если Моника выгнала клиента и не стала с ним работать и если отработала и забрала все деньги себе
    if monicaAbbyNoEscortClient3 == 0 or monicaAbbyNoEscortClient4 > 0:
#    if ep224_quests_monica_kicked_client == True:
        imgd 35060
        m "Ничего не окей!"
        m "Я этого мерзкого неотесанного типа выгнала!"
        m "И не стала с ним работать!"
        abby "Выгнала?"
        m "Да!"
        imgd 35061
        abby "И ты ничего не заработала?"
        m "Конечно, ничего! Он не заплатил мне ни цента!"
        m "Мало того, что он грубый мужлан, так еще и жадный!"
        abby "Ладно, если он мне позвонит, я с ним сама буду работать."
        imgd 35062
        m "И сосед у тебя придурок!"
        abby "Да, я в курсе. Везде сует свой нос. Достал уже!"
        abby "Раз у тебя не получилось поработать с Брайаном, то..."
    # если оставила треть заработка Эбби
    if monicaAbbyNoEscortClient5 > 0:
        imgd 35060
        m "Я еле вытерпела этого придурка!"
        m "Какой же он отвратительный тип! Мерзкий грубый мужлан!"
        m "К тому же еще и жадный!!!"
        m "Он мне заплатил всего $ 150!!!"
        imgd 35061
        abby "Это он еще щедро. Ха-ха!"
        abby "Видимо, ему понравилось."
        abby "Оставила мой процент, как я просила, [monica_hotel_name]?"
        imgd 35062
        m "Да, оставила на столике."
        abby "Отлично, [monica_hotel_name]!"
        abby "Ты хорошо справилась."
    imgf 30006
    abby "Когда мне позвонит еще кто-нибудь из моих клиентов..."
    abby "Я тебе дам еще возможность подзаработать."
    abby "Ты же не против будешь?"
    imgd 41426
    m "Я подумаю..."
    abby "Уверена, ты примешь верное решение."
    abby "Ладно, [monica_hotel_name], мне пора бежать работать."
    abby "До встречи!"
    music Stealth_Groover
    # уходит
    # если Моника отработала и забрала все деньги себе
    if monicaAbbyNoEscortClient4 > 0:
        imgf 35057
        mt "Эта идиотка Эбби поверила мне, что клиент ничего не заплатил!"
        mt "Отлично!"
        mt "Я считаю, что не должна делиться с ней этими деньгами!"
        mt "Они все мои! Я их заработала!"
    # если Моника выгнала клиента и не стала с ним работать
    if monicaAbbyNoEscortClient3 == 0:
        imgf 35052
        mt "Пошла она к черту со своими клиентами-идиотами!"
        mt "Пусть сама с ними делает всякие грязные извращенства!"
        mt "Я не собираюсь терперть подобного!"
    # если Моника оставила треть заработка Эбби
    if monicaAbbyNoEscortClient5 > 0:
        imgf 35044
        mt "$ 150 - это щедро?!"
        mt "Из них я заработала всего $ 100!"
        mt "Пусть эта никчемная проститутка Эбби подавится своими $ 50!"
        mt "Придет время и я отомщу ей за это!"
    fadeblack
    sound highheels_short_walk
    pause 2.0
    return
