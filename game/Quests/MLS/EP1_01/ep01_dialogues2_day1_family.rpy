define help = Character(_("HELP"), who_color=c_green) # helper
define sophie_t = Character(_("Софи"), who_color=c_pink, what_color=c_gray, what_italic=True) # Sophie Evans thinking
define henry = Character(_("Генри"), who_color=c_gray) # Henry Evans - муж Софи
define cynthia = Character(_("Синтия"), who_color=c_green) # Cynthia Evans - соседка, младшая дочь Софи
#####inc define mother_t = Character(_("Мама"), who_color=c_pink, what_color=c_gray, what_italic=True) # mother thinking

#####inc
##->#####inc

label ep01_dialogues2_day1_family_1:
    # кадр на комнату Барди
    # звук шагов, звук открывающейся двери
    # на пол или на кровать падает рюкзак
    fadeblack
    sound snd_door_open1
    pause 1.5
    music Mandeville
    imgfl 900026
    bardi_t "Это и есть моя комната?!" ##->#####inc
    #####inc bardi_t "Снова эта долбанная комната!"
    imgf 900027
    bardi_t "Я не хочу находиться здесь! Я не хочу ЖИТЬ здесь!"
    sound Jump1
    img 900028 hpunch
    bardi_t "Не хочу и не буду!"
    sound snd_walk_barefoot
    imgd 900029
    bardi_t "Надолго я здесь не задержусь!"
    bardi_t "!!!"
    # голос Софи из-за двери
    imgf 900030
    sophie "[mcname], милый, мой руки и спускайся на ужин. Мы все ждем тебя!"
    bardi "Иду!"
    # злой пинок по стулу, кровати или рюкзаку
    sound vjuh3
    imgd 900031
    w
    img 900032
    w
    sound snd_kick_fred1
    img 900033 vpunch
    bardi "!!!"
    menu:
        "Пойти на кухню.":
            jump ep01_dialogues2_day1_family_2
        "Позже, сначала осмотреться.":
            # игрок может побродить по комнате и дому
            # затем сам топает до кухни, след. сцена запускается при клике на локацию Кухня
            pass
    imgf 900034
    bardi_t "Думаю, ничего страшного, что им придется немного подождать меня..."
    return

# в телефоне в Инсте можно сделать в аккаунте Барди один опубликованный (или сохраненный в галерее) пост
# фотка - селфи Барди на фоне вокзала, он показывает фак в камеру
# и текст:
# "Наконец-то, этот долгожданный день настал! Сегодня я оставляю это гребаное захолустье!"
# "Прощайте, деревенщины-одноклассники! Я уезжаю!"
# "Меня ждет новая, счастливая и богатая жизнь в огромном городе!"
# "Я поступлю в лучший колледж страны! Я смогу позволить себе ВСЕ!"
# "Крутые тачки, крутые девчонки, элитные ночные клубы и улетные вечеринки!.."
# "У меня все только начинается!"
# "Завидуйте мне, лузеры!"
# если не inc - под постом коммент от Гарри "Сам ты лузер! Увижу - надеру тебе зад, ушлепок!"
#####inc под этим постом стоит 1 лайк и коммент от Оливии "Тебе повезло, говнюк, что ты свалил отсюда!"

## мысли не рендерить!!
# комната Барди
# мысли при клике на кровать, если утро или день, вечером и ночью меню из лейбла ep01_dialogues2_day1_family_3
label ep01_dialogues2_day1_family_1_1:
    bardi_t "Мне еще рано ложиться спать."
    return
# мысли при клике на окно
label ep01_dialogues2_day1_family_1_2:
    bardi_t "Может, сбежать отсюда? Вокзал, поезд..."
    bardi_t "И что дальше?"
    bardi_t "Отец меня не ждет, а больше мне некуда идти."
    return
# мысли при клике на стол
label ep01_dialogues2_day1_family_1_3:
    bardi_t "Здесь я буду делать домашние задания для колледжа."
    bardi_t "Черт! Колледж. Не хочу сейчас думать об этом."
    return
# мысли при клике на печатную машинку
label ep01_dialogues2_day1_family_1_4:
    bardi_t "А это еще что за древность?"
    bardi_t "Они мне вместо компа поставили ЭТО?!"
    return
# мысли при клике на лист в печатной машинке
label ep01_dialogues2_day1_family_1_5:
    bardi_t "Там что-то написано..."
    # можно сделать приближение к листу
    bardi_t "Меня не покидают мысли о том, что я совершила ошибку."
    bardi_t "Если бы я могла повернуть все назад, вернуться в прошлое..."
    bardi_t "Я не стала бы вступать в эти болезненные отношения."
    bardi_t "Я потеряла свою индивидуальность, я потеряла себя."
    bardi_t "Я забыла, что такое быть любимой и желанной..."
    bardi_t "К сожалению, сейчас уже ничего не изменишь."
    bardi_t "Каждый день я вынуждена улыбаться и притворяться счастливой."
    bardi_t "А на самом деле..."
    bardi_t "Только ночь знает мои истинные чувства и переживания."
    # лист отдаляется
    bardi_t "Похоже на отрывок из какого-то дневника."
    bardi_t "Интересно, кто написал это?"
    return
# холл на втором этаже
# мысли при клике на двери соседних комнат
label ep01_dialogues2_day1_family_1_6:
    bardi_t "Эта дверь закрыта." ##->#####inc
    #####inc bardi_t "Почему-то, двери закрыты... Раньше в этом доме было не принято запирать двери."
    return
# мысли при клике на флипчарт
label ep01_dialogues2_day1_family_1_7:
    bardi_t "Зачем эта хрень тут стоит?" ##->#####inc
    bardi_t "Они устроили здесь свалку из ненужных вещей?" ##->#####inc
    #####inc bardi_t "Раньше на этой доске мама оставляла мне всякие записки. Наподобие 'Завтрак в холодильнике'..."
    #####inc bardi_t "Или просто '[mcname] и Оливия, мама вас очень любит'. Это было очень мило."
    return
# мысли при клике на стол
label ep01_dialogues2_day1_family_1_8:
    bardi_t "Чей-то рабочий стол." ##->#####inc
    bardi_t "Странно, что его поставили здесь, а не в комнате." ##->#####inc
    #####inc bardi_t "Старый рабочий стол мамы."
    #####inc bardi_t "Она любила по вечерам сидеть за ним и что-нибудь рисовать."
    return
# мысли при клике на картины
label ep01_dialogues2_day1_family_1_9:
    bardi_t "Какие-то дурацкие картины." ##->#####inc
    #####inc bardi_t "Раньше вместо этих картин здесь были наши семейные фотографии."
    return
# гостиная
# мысли при клике на ТВ
label ep01_dialogues2_day1_family_1_10:
    bardi_t "Я не хочу сейчас смотреть телек."
    return
# мысли при клике на диван
label ep01_dialogues2_day1_family_1_11:
    bardi_t "Здесь все такое старое. Когда они последний раз делали ремонт и меняли мебель?" ##->#####inc
    #####inc bardi_t "Этот диван стоит тут с моего детства... Когда они последний раз делали ремонт и меняли мебель?"
    return
# мысли при клике на входную дверь
label ep01_dialogues2_day1_family_1_12:
    bardi_t "Мне пока там нечего делать."
    return
# ванная комната
# мысли при клике на унитаз
label ep01_dialogues2_day1_family_1_13:
    bardi_t "Я недавно отлил. Пока не хочу."
    return
# мысли при клике на душ или ванную
label ep01_dialogues2_day1_family_1_14:
    bardi_t "В этом старом доме только один душ."
    bardi_t "Это не очень удобно."
    menu:
        "Принять душ.":
            # кадры стены душа и капли воды, как будто Барди смотрит
            # вид из глаз вниз, видно член
            bardi_t "Совсем недавно я жил в доме, где у меня были собственный душ и туалет."
            bardi_t "А тут, по ходу, можно и в очередь попасть, если приспичит."
            bardi_t "Такие контрасты... Жесть."
            bardi_t "Надеюсь, мне недолго придется жить здесь..."
        "Позже.":
            bardi_t "Я пока не хочу принимать душ."
            pass
    return
# кухня
# при клике на любой предмет
label ep01_dialogues2_day1_family_1_15:
    bardi_t "Какая маленькая кухня. Не то что в новом доме отца." ##->#####inc
    #####inc bardi_t "На кухне совсем ничего не изменилось."
    return


label ep01_dialogues2_day1_family_2:
    # кухня
    # вся сцена проигрывается так, что мы смотрим глазами Барди
    # на столе перед каждым тарелки, столовые приборы и стаканы с соком
    # одно место за столом свободно, стоит пустой стул для Барди
    # за столом сидят Софи, ее муж Генри и две сестры - старшая Оливия и младшая Синтия
    # Софи и Синтия мило улыбаются Барди
    # Генри бросает в его сторону равнодушный взгляд и снова принимается за еду
    # Оливия отрывается от своего телефона и смотрит зло на Барди
    music Cheery_Monday
    imgf 900000
    w
    sound snd_eating
    imgd 900001
    w
    imgf 900002
    w
    imgd 900003
    olivia "Наконец-то, ты притащил свою задницу сюда, придурок!"
    olivia "Какого черта мы должны ждать тебя?!"
    imgd 900004
    bardi_t "Вот так встреча..."
    bardi "Эм... Ну я..."
    # Софи делает ей замечание
    img 900005
    sophie "Оливия! Что за выражения?!" ##->#####inc
    #####inc mother "Оливия! Как ты разговариваешь с братом?!"
    # Софи поворачивается к Барди, машет на Оливию рукой и улыбаясь говорит
    imgf 900006
    sophie "[mcname], не обращай на нее внимания! Она всегда такая колючая..."
    # младшая Синтия тоже сердито говорит Оливии
    imgd 900007
    cynthia "Он наш гость! Зачем ты так?!" ##->#####inc
    #####inc cynthia "Он наш брат! Зачем ты так?!"
    # Оливия с презрением фыркает
    olivia "Пфф!!!"
    # Синтия с милой улыбкой говорит Барди
    imgf 900008
    cynthia "Я очень рада, что ты теперь будешь жить у нас, [mcname]." ##->#####inc
    #####inc cynthia "Я очень рада, что ты вернулся в этот дом и будешь жить с нами, [mcname]."
    imgd 900009
    bardi "Угу... Я тоже."
    imgd 900008
    w
    # Софи говорит ему, мило улыбаясь
    imgf 900010
    sound snd_eating
    sophie "[mcname], милый, я тоже рада, что твой отец решил вернуть тебя в твой родной город. И что ты теперь будешь жить с нами." ##->#####inc
    sophie "Все равно та комната, в которой ты теперь будешь жить, уже много лет стоит пустая." ##->#####inc
    sophie "И моим девочкам будет веселее, что у них появился такой милый сосед. Надеюсь, вы подружитесь." ##->#####inc
    # Оливия зло косится на Барди
    imgd 900011
    olivia "Еще чего!" ##->#####inc
    # Софи не обращает внимания на дочь и продолжает разговаривать с Барди
    imgf 900012
    sophie "А в городе... Ну что тебе там делать одному, когда отец постоянно пропадает на работе?" ##->#####inc
    imgd 900013
    sophie "Зато здесь ты можешь спокойно общаться с друзьями и вообще весело проводить время." ##->#####inc
    imgd 900012
    bardi "..."
    #####inc mother "[mcname], сынок, я тоже очень рада, что ты вернулся..."
    #####inc mother "И теперь будешь жить с нами."
    #####inc mother "Я очень по тебе скучала!"
    #####inc mother "Уверена, что твои друзья тоже обрадуются, когда узнают, что ты вернулся..."
    #####inc olivia "У этого недоумка нет друзей! Он здесь никому не нужен, кроме тебя, мам."
    #####inc bardi_t "!!!"
    # муж Софи Генри говорит равнодушно
    imgf 900014
    henry "Барди, я вчера разговаривал с директором колледжа..."
    henry "Твои документы уже приняли и ты зачислен к ним."
    henry "Так что завтра у тебя начинаются занятия."
    # и Генри снова теряет интерес к происходящему
    imgd 900015
    sophie "В этом колледже учатся многие из твоих бывших одноклассников. Здорово, правда?!"
    sophie "Ты, наверное, очень скучал по ним, милый?"
    imgd 900016
    bardi "Угу... Очень..."
    imgd 900017
    sophie "Синтия учится на курсе на год младше твоего. Так что будете ходить в колледж вместе."
    # Синтия мило улыбается Барди
    imgf 900008
    cynthia "Скажи, прикольно, [mcname]?! Мы не только соседи по комнатам, но и учимся в одном колледже!" ##->#####inc
    #####inc cynthia "Прикольно, у меня теперь есть старший брат! И он будет учиться со мной в одном колледже!"
    # Барди угрюмо
    imgd 900009
    bardi_t "Чему эта дурочка Синтия так радуется?!"
    bardi_t "Меня тошнит от одной мысли о колледже!"
    imgf 900018
    sophie "[mcname], милый, занятия в колледже начинаются завтра в 9 утра..." ##->#####inc
    #####inc mother "Сынок, милый, занятия в колледже начинаются завтра в 9 утра..."
    # Генри равнодушно бросает
    imgd 900019
    henry "Но сначала не забудь зайти в приемную директора."
    henry "Тебе нужно подписать какие-то документы."
    imgd 900020
    bardi_t "Твою мать!!!"
    imgd 900018
    sophie "Я приготовлю тебе на завтрак сэндвичи... Ты любишь сэндвичи, [mcname]?"  ##->#####inc
    #####inc mother "[mcname], я приготовлю тебе на завтрак твои любимые сэндвичи..."
    imgd 900020
    bardi "Да, Софи." ##->#####inc
    #####inc bardi "Хорошо, мам."
    # кадр на Синтию - мило улыбается Барди
    imgf 900021
    cynthia "..."
    bardi_t "Хм... Ну окей... Вроде, Синтия и правда мне рада."
    # кадр на Оливию - пялится в свой смартфон
    imgd 900022
    olivia "У этой страшной дуры лайков больше, чем у меня! Какого черта?!"
    bardi_t "Чего не скажешь про Оливию!"
    bardi_t "Вообще ее не узнаю... Обозвала меня придурком и залипла в своем телефоне..."
    # кадр на Генри - он с безразличным видом ужинает
    imgf 900023
    henry "..."
    bardi_t "Этого Генри вообще интересует, что происходит? Он всегда такой безучастный?"
    bardi_t "И что Софи в нем нашла? Не понимаю." ##->#####inc
    #####inc bardi_t "И что мама в нем нашла? Не понимаю."
    imgd 900024
    bardi_t "..."
    bardi_t "Все! С меня на сегодня хватит милого общения с моими соседями!" ##->#####inc
    #####inc bardi_t "Все! С меня на сегодня хватит милого общения с семьей!"
    bardi_t "Не хочу больше никого видеть..."
    # Барди кладет вилку на стол и встает
    sound snd_plates1
    imgf 900025
    bardi "Я устал. Пойду спать."
    # Софи улыбается ему
    sophie "Да, конечно, [mcname]."
    bardi "Спасибо за ужин, Софи." ##->#####inc
    #####inc bardi "Спасибо за ужин, ма."
    # смена кадра на комнату Барди
    return

label ep01_dialogues2_day1_family_3:
    # комната Барди, вечер
    # свободное перемещение по комнате и дому, если игрок кликает на кровать, то возникает меню
    # при клике на кровать
    menu:
        "Лечь спать.":
            bardi_t "Уже поздно. Я сегодня очень устал и хочу спать."
            return
        "Позже, я пока не устал.":
            # игрок может побродить по комнате и дому
            pass
    bardi_t "Я пока не хочу спать..."
    return

label ep01_dialogues2_day1_family_4:
    # Барди зашел вечером на кухню, Софи стоит у столешницы и что-то делает (например, моет посуду)
    # клик на Софи
    # она поворачивается к нему и улыбается
    music Cheery_Monday
    imgf 900035
    sophie "[mcname]? Я думала, ты уже лег спать." ##->#####inc
    #####inc mother "Сынок? Я думала, ты уже лег спать."
    imgd 900036
    bardi "Да, я как раз собираюсь..."
    imgd 900035
    sophie "Хорошо, милый. Тебе нужно выспаться - завтра рано вставать."
    sophie "Я тебя разбужу утром."
    imgd 900036
    bardi "Окей, Софи. Спасибо." ##->#####inc
    #####inc bardi "Окей, ма."
    return

label ep01_dialogues2_day1_family_4_1:
    # если повторный клик после этого диалога
    music Cheery_Monday
    imgd 900035
    sophie "Ты еще что-то хотел, милый?"
    imgd 900036
    bardi "Нет, Софи. Спокойной ночи." ##->#####inc
    #####inc bardi "Нет, ма. Спокойной ночи."
    imgd 900035
    sophie "Спокойной ночи, [mcname]."
    return

label ep01_dialogues2_day1_family_5:
    # Барди зашел вечером в гостиную, Генри сидит с банкой или бутылкой пива и смотрит телек
    # клик на Генри
    # он поворачивается к Барди

    henry "[mcname], ты еще не спишь?"
    henry "Будешь пиво?"
    bardi "Нет, Генри. Как-нибудь в следующий раз."
    henry "Ладно. Мне больше достанется, хе-хе."
    # Генри отворачивается и снова утыкается в телек
    bardi_t "После пива он становится более дружелюбным."
    bardi_t "Если это можно так назвать..."
    return

label ep01_dialogues2_day1_family_6:
    # Барди пытается зайти в комнату старшей Оливии
    # клик на ее дверь
    olivia "Кто там?"
    olivia "Мам, это ты? Я не хочу сейчас разговаривать..."
    olivia "И вообще, я занята и мне некогда!"
    bardi_t "Чем эта Оливия там занимается, что не может открыть дверь?.."
    return

label ep01_dialogues2_day1_family_7:
    # Барди пытается зайти в комнату младшей Синтии
    # клик на ее дверь
    # дверь приоткрывается и выглядывает приветливая мордашка Синтии
    cynthia "[mcname]? Ты пришел пожелать мне спокойной ночи?"
    bardi "Ммм... Да."
    bardi "Спокойной ночи, Синтия."
    cynthia "Это так мило с твоей стороны, [mcname]." ##->#####inc
    #####inc cynthia "Это так мило с твоей стороны, братик."
    cynthia "И тебе спокойной ночи. Завтра увидимся."
    # улыбается ему
    # дверь закрывается
    return

# при выборе пункта меню "Лечь спать"
label ep01_dialogues2_day1_family_8:
    # ночь
    # комната Барди, темнота
    # тиканье часов
    bardi_t "Помню, однажды я лежал ночью в своей комнате и слушал, как мои родители ругались в гостиной..."
    bardi_t "Мама плакала и кричала, что отец променял нас на какую-то блондинистую шлюху..."
    bardi_t "Потом хлопнула входная дверь и стало тихо... Только тиканье часов... Как сейчас..."
    bardi_t "И мне было страшно. За маму, за отца. За нашу семью, которая в итоге распалась."
    bardi_t "Ненавижу тиканье часов."
    bardi_t "..."
    bardi_t "Возможно, для кого-то мой выбор, с кем из родителей остаться после их развода, покажется странным. Я выбрал отца."
    bardi_t "Хотя, он никогда не проявлял ко мне теплых отцовских чувств."
    bardi_t "Но я его единственный сын и он в состоянии обеспечить мне блестящее будущее..."
    bardi_t "Так и должно было быть. Все шло по плану: я поступил в лучший колледж в стране..."
    bardi_t "Но потом..."
    bardi_t "Потом появилась та лживая стерва! Из-за нее я теперь здесь, в глухой дыре!"
    # тиканье часов продолжается
    bardi_t "..."
    bardi_t "Думаю, Софи и правда рада, что я теперь буду жить у них." ##->#####inc
    bardi_t "И ее дочь Синтия тоже..." ##->#####inc
    bardi_t "Они обе кажутся очень дружелюбными и милыми..." ##->#####inc
    bardi_t "Чего не скажешь об Оливии!.." ##->#####inc
    #####inc bardi_t "Думаю, мама и правда рада, что я вернулся. И младшая сестра Синтия тоже..."
    #####inc bardi_t "Я раньше не особо с ней общался. Синтия мне казалась маленькой и глупой. Мне было неинтересно."
    #####inc bardi_t "Но теперь она повзрослела. И оказалось, что она очень милая и дружелюбная."
    #####inc bardi_t "Чего не скажешь о моей старшей сестре Оливии!.."
    # стук в дверь
    bardi_t "???"
    # дверь приоткрывается, заходит Софи
    sophie "[mcname], милый, ты уже спишь?" ##->#####inc
    #####inc mother "Сынок, милый, ты уже спишь?"
    bardi "Нет еще, Софи..." ##->#####inc
    #####inc bardi "Нет еще, ма..."
    sophie "Переживаешь из-за колледжа?"
    bardi "Вот еще! Нисколько!"
    # она садится на край его кровати
    sophie "Не переживай, [mcname]. Уверена, что все пройдет отлично." ##->#####inc
    #####inc mother "Не переживай, родной. Уверена, что все пройдет отлично."
    # она прикасается к его волосам и гладит его по голове
    bardi "..."
    # Софи задумчиво
    sophie "Когда ты со своим отцом уезжал из нашего городка..." ##->#####inc
    sophie "Ты был совсем юным подростком." ##->#####inc
    sophie "А сейчас ты кажешься таким взрослым..." ##->#####inc
    sophie "Ты так изменился за это время, [mcname]." ##->#####inc
    sophie_t "Стал такой высокий и такой... Хорошенький..." ##->#####inc
    sophie_t "И очень похож на своего отца в юности." ##->#####inc
    #####inc mother "Я так скучала по тебе, сынок."
    #####inc mother "И ты так подрос за это время... Не могу поверить, что мой сын уже такой взрослый..."
    #####inc mother_t "Мой сын. Мой любимый."
    #####inc mother_t "Теперь он не маленький мальчик. Он стал таким высоким и таким... Таким хорошеньким..."
    #####inc mother_t "Он очень похож на своего отца в юности, когда я увидела его впервые и влюбилась без памяти."
    #####inc mother_t "Надеюсь, мой милый сынок со временем не превратится в жестокого и бесчувственного мужчину, как произошло с моим бывшим мужем..."
    #####inc она улыбается ему, наклоняется и чмокает его в лоб
    #####inc он уворачивается от нее
    # она снова улыбается и еще раз проводит рукой по его волосам
    sophie "Не переживай, [mcname]. Все будет хорошо."
    bardi "Угу..."
    sophie "Спокойной ночи, милый..." ##->#####inc
    #####inc mother "Спокойной ночи, родной..."
    bardi "Спокойной ночи, Софи." ##->#####inc
    #####inc bardi "Спокойной ночи, мам."
    # Софи уходит
    # комната, тиканье часов
    return
