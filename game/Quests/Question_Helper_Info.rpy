default questLogDataEnabled = {}
default questLogLinesUpdated = []

#call question_helper_enable("question_helper_hairdye_find_julia")
#call question_helper_disable()

label questLog_init:
    $ questLogData = [
        [0, t_("Миссис Морис"), True, t_("Список желаний")],
        [1, t_("Роуз"), True, t_("Список желаний")],
        [2, t_("Оливия"), True, t_("Список желаний")],
        [4, t_("Миссис Кларк"), True, t_("Список желаний")],
        [5, t_("Профессор Ричардсон."), True, t_("Список желаний")],
        [6, t_("Миссис Адамс"), True, t_("Список желаний")],
        [7, t_("Мама Шона"), True, t_("Список желаний")],
        [8, t_("Оливия"), True, t_("Список желаний")],
        [9, t_("Синтия"), True, t_("Список желаний")],
        [10, t_("Эмили"), True, t_("Список желаний")],
        [11, t_("Тренер Брукс"), True, t_("Список желаний")],
        [12, t_("Миссис Уилсон"), True, t_("Список желаний")],
        [13, t_("Мисс Янг"), True, t_("Список желаний")],
        [14, t_(""), True, t_("Список желаний")],
        [3, t_("Найти способ получать деньги."), True, t_("Жизнь в городе")]

    ]
    return

label questHelp_init:
    # в начале игры активно:
    $ questHelpDataQuests = {
        # СТАРТ
        "start_1" : [t_("СТАРТ"), t_("Знакомство с геймплеем. Начало истории."), t_("Поговорить с девочками на пляже.")],
        # срабатывание: Ты кое-что забыла расскать, Лили...
        # открываем house_1

        # ДОМ
        "house_1" : [t_("ДОМ"), t_("Новая семья."), t_("Пойти на кухню и поужинать с новой семьей.")],
        # срабатывание: Наконец-то, ты притащил свою задницу сюда, придурок!
        # открываем house_2
        # house_desc1
        "house_2" : [t_("ДОМ"), t_("Завтра сложный день."), t_("Пойти в свою комнату и лечь спать.")],
        # срабатывание: Ненавижу тиканье часов.
        # открываем house_3 и house_4
        "house_3" : [t_("ДОМ"), t_("Приятная неожиданность."), t_("Утром зайти в ванную комнату.")],
        # срабатывание: И не услышала, что я зашел...
        # открываем college_4
        # house_desc1 -> house_desc2
        # при отказе - стоп для college_4
        "house_4" : [t_("ДОМ"), t_("Завтрак."), t_("Пойти на кухню и поговорить с Софи.")],
        # срабатывание: Завтракай и бегом в колледж, иначе ты опоздаешь.
        # открываем college_1
        # college_desc1
        "house_5" : [t_("ДОМ"), t_("Ужин с семьей."), t_("Поговорить с Софи и Генри по поводу денег. Сказать Софи правду про синяк.")],
        # срабатывание: Я с этим идиотом Гарри еще со школы не ладил.
        # открываем house_6
        # house_desc3 -> house_desc4
        "house_5a" : [t_("ДОМ"), t_("Ужин с семьей."), t_("Поговорить с Софи и Генри по поводу денег. Солгать Софи про синяк.")],
        # срабатывание: Я просто ударился о дверцу своего шкафчика.
        # открываем house_6
        # house_desc3 -> house_desc5
        "house_5b" : [t_("ДОМ"), t_("Идти спать."), t_("Пойти в свою комнату и лечь спать.")],
        "house_6" : [t_("ДОМ"), t_("Фотки Оливии."), t_("Посмотреть аккаунт Оливии в сети.")],
        # срабатывание: Хотел бы я быть на месте того, кто ее фоткает для Инсты.
        # открываем house_7, house_8
        # house_desc6
        # при отказе - стоп для house_7, house_8
        "house_7" : [t_("ДОМ"), t_("Телефон Оливии."), t_("Лечь спать. Ночью пойти на 1 этаж и попытаться стащить телефон Оливии пока она в душе.")],
        # срабатывание: Возможно, даже успею посмотреть какие-то фотки.
        "house_8" : [t_("ДОМ"), t_("Слежка за Оливией."), t_("Лечь спать. Ночью пойти на 1 этаж и подглядывать за Оливией пока она в душе.")],
        # срабатывание: Но что у нее тату внизу живота, об этом я не знал.
        # Оливия попадает в WishList
        "house_9" : [t_("ДОМ"), t_("Избавиться от стояка."), t_("Принять душ.")],
        # срабатывание: Забиваешь себе голову всякой хренью с самого утра. Придурок.
        # открываем house_10
        "house_10" : [t_("ДОМ"), t_("Идти на кухню."), t_("Пойти на кухню и поговорить с Софи.")],
        # срабатывание: Вот твои пять долларов, о которых мы вчера говорили.
        # открываем college_14
        # house_desc4, house_desc5 -> house_desc7
        "house_11" : [t_("ДОМ"), t_("Возвратиться домой."), t_("Пойти домой. Ужин с семьей.")],
        # срабатывание: Я сейчас на минутку поднимусь наверх и подойду.
        # открываем house_12
        "house_12" : [t_("ДОМ"), t_("Идти в свою комнату."), t_("После ухода Софи и Генри пойти в свою комнату. Знакомство с парнем Оливии.")],
        # срабатывание: А! Ты парень Оливии?
        # открываем house_13
        "house_13" : [t_("ДОМ"), t_("Проверить инстаграм Эмили."), t_("После ухода Оливии и Марка пойти в свою комнату и посмотреть фото Эмили в сети.")],
        # срабатывание: Эмили хорошо смотрится в купальнике...
        # открываем house_14, house_15
        # college_desc11
        "house_14" : [t_("ДОМ"), t_("Посмотреть кино с Синтией."), t_("Пойти на кухню. Разговор с Синтией в холле. Согласиться посмотреть с ней фильм.")],
        # срабатывание: Спасибо за компанию и хорошего сна!
        # открываем house_16
        # house_desc2 -> house_desc8
        "house_15" : [t_("ДОМ"), t_("Откровения Оливии."), t_("Пойти в комнату Оливии и поговорить с ней. Массаж для Оливии.")],
        # срабатывание: Тренируйся на сверстницах, опытный!
        # открываем house_16
        # house_desc6 -> house_desc9
        "house_16" : [t_("ДОМ"), t_("Лечь спать."), t_("Пойти в свою комнату и лечь спать.")],


        # КОЛЛЕДЖ
        "college_1" : [t_("КОЛЛЕДЖ"), t_("Пойти в колледж."), t_("Кликнуть на карту и выбрать локацию Колледж.")],
        # срабатывание: Я надеюсь, что никто из моих бывших одноклассников сюда не поступил.
        # открываем college_2
        "college_2" : [t_("КОЛЛЕДЖ"), t_("Старый знакомый."), t_("Поговорить с Шоном. Зайти в колледж.")],
        # срабатывание: Рад тебя видеть, чувак!
        # открываем college_3
        # college_desc1 -> college_desc2
        "college_3" : [t_("КОЛЛЕДЖ"), t_("Знакомство с миссис Кларк."), t_("Поговорить с Шоном в колледже. Встреча с Синтией.")],
        # срабатывание: Да что же это такое?!
        # открываем college_4, college_5, college_6
        "college_4" : [t_("КОЛЛЕДЖ"), t_("Рассматривать Синтию."), t_("Поднять папку преподавательницы и посмотреть на Синтию.")],
        # срабатывание: Забавно. Совсем недавно я видел свою соседку в душе голой.
        "college_5" : [t_("КОЛЛЕДЖ"), t_("Рассматривать миссис Кларк."), t_("Поднять папку преподавательницы и посмотреть на миссис Кларк.")],
        # срабатывание: Хмм... А эта преподавательница ничего.
        "college_6" : [t_("КОЛЛЕДЖ"), t_("Приемная директора."), t_("Идти на 3 этаж колледжа и зайти в приемную директора. Поговорить с секретарем.")],
        # срабатывание: Пойдем, я покажу тебе твой шкафчик.
        # открываем college_7
        # при отказе - стоп для college_7
        "college_7" : [t_("КОЛЛЕДЖ"), t_("Найти кабинет английского."), t_("Идти на 2 этаж и поговорить с мисс Хилл.")],
        # срабатывание: Я уже сильно опоздал на занятие по английскому.
        # открываем college_8
        # при отказе - стоп для college_8
        "college_8" : [t_("КОЛЛЕДЖ"), t_("Посетить занятие по английскому."), t_("Зайти в кабинет английского. Знакомство с одногруппниками.")],
        # срабатывание: Представься нам и скажи пару слов о себе.
        # открываем college_9, college_10
        # при отказе - стоп для college_9, college_10
        "college_8a" : [t_("КОЛЛЕДЖ"), t_("Гарри уставился на меня."), t_("Посмотреть на Гарри.")],
        "college_9" : [t_("КОЛЛЕДЖ"), t_("Флешбек из школьных лет. Послать Гарри."), t_("После окончания английского поговорить с миссис Адамс и выйти из кабинета. Послать Гарри.")],
        # срабатывание: Школьные времена давно прошли, если ты не заметил!
        # открываем college_11
        # при отказе - стоп для college_11
        "college_10" : [t_("КОЛЛЕДЖ"), t_("Флешбек из школьных лет. Толкнуть Гарри"), t_("После окончания английского поговорить с миссис Адамс и выйти из кабинета. Толкнуть Гарри.")],
        # срабатывание: Хреновый из тебя воспитатель!
        # открываем college_12
        # при отказе - стоп для college_12
        "college_11" : [t_("КОЛЛЕДЖ"), t_("Роуз."), t_("Поговорить с Роуз.")],
        # срабатывание: Чтобы ты не обращал внимания на этого придурка Гарри.
        # открываем college_13
        # college_desc3
        # Роуз попадает в WishList
        "college_12" : [t_("КОЛЛЕДЖ"), t_("Миссис Морис."), t_("Поговорить с миссис Морис.")],
        # срабатывание: Ты так и будешь лежать на полу?
        # открываем college_13
        # college_desc4
        # Миссис Морис попадает в WishList
        "college_13" : [t_("КОЛЛЕДЖ"), t_("Окончание первого учебного дня."), t_("Выйти из колледжа во двор.")],
        # срабатывание: Осталось придумать, где же мне взять денег...
        # открываем house_5, house_5a, sean_1
        # house_desc3
        "college_14" : [t_("КОЛЛЕДЖ"), t_("Идти в колледж."), t_("Кликнуть на карту и выбрать локацию Колледж.")],
        # срабатывание: Шона нет сегодня... Наверное, уже ушел на занятия.
        # открываем college_15
        "college_15" : [t_("КОЛЛЕДЖ"), t_("Позвонить Шону."), t_("Кликнуть на контакт Шона в телефоне.")],
        # срабатывание: Окей. Ты меня заинтриговал, бро.
        # открываем college_16
        "college_16" : [t_("КОЛЛЕДЖ"), t_("Приемная директора."), t_("Идти на 3 этаж колледжа и зайти в приемную директора. Поговорить с секретарем.")],
        # срабатывание: Профессор Ричардсон снова требует горячий кофе?
        # открываем college_17, college_18
        # college_desc5
        "college_17" : [t_("КОЛЛЕДЖ"), t_("Урок математики."), t_("Пойти на второй этаж в кабинет математики.")],
        # срабатывание: Тема нашего следующего занятия – Однородные дифференциальные уравнения первого порядка.
        # открываем college_19, college_20, college_21
        # college_desc6
        "college_18" : [t_("КОЛЛЕДЖ"), t_("Разглядеть Мисс Янг."), t_("Попытаться открыть папку на столе мисс Янг.")],
        # срабатывание: Хмм... Неплохо, мисс Янг.
        "college_19" : [t_("КОЛЛЕДЖ"), t_("Помощник Миссис Морис."), t_("Помочь Миссис Морис в ее просьбе.")],
        # срабатывание: Я говорю, что, конечно же, я помогу вам, миссис Морис.
        # открываем college_21
        # college_desc4 -> college_desc7
        "college_20" : [t_("КОЛЛЕДЖ"), t_("В раздевалке с Роуз."), t_("Спрятаться в раздевалке.")],
        # срабатывание: Раздевалка для девочек? Если она открыта и там никого нет, то можно попробовать.
        # открываем college_21
        # college_desc3 -> college_desc8
        "college_21" : [t_("КОЛЛЕДЖ"), t_("Первый урок физкультуры."), t_("Идти в спортзал на первом этаже колледжа.")],
        # срабатывание: Студентов без спортивной формы я к занятиям не допускаю!
        # открываем college_23
        "college_22" : [t_("КОЛЛЕДЖ"), t_("Рассмотреть своего тренера."), t_("")],
        # срабатывание: Классный костюмчик у этой тренерши. Да сама она очень даже ничего.
        # college_desc9
        "college_23" : [t_("КОЛЛЕДЖ"), t_("Посетить библиотеку."), t_("Библиотека на третьем этаже.")],
        # срабатывание: Тут библиотека и нужно соблюдать тишину!
        # открываем sean_2
        "college_24" : [t_("КОЛЛЕДЖ"), t_("Рассмотреть Миссис Уилсон."), t_("Попросить миссис Уилсон достать книгу с верхней полки.")],
        # срабатывание: Я могу попросить достать вон ту книгу?
        # college_desc10

        # ШОН
        "sean_1" : [t_("ШОН"), t_("В гостях у друга."), t_("Пойти к Шону. Знакомство с его мамой. Поговорить с Шоном.")],
        # срабатывание: Ладно, я пойду. До встречи, Шон.
        # sean_desc1
        "sean_2" : [t_("ШОН"), t_("Интересно, чем там занят Шон?"), t_("Навестить Шона.")],
        # срабатывание: Она поймет, что трахалась не с Шоном.
        # открываем house_11
        "sean_3" : [t_("ШОН"), t_("Как Шон умудряется встречаться с Бекки без денег?"), t_("Позвонить Шону после встречи с Бекки у него дома.")]
        # sean_desc1 -> sean_desc2

    }


    $ questHelpDataCategoriesDescriptions = [
        # ДОМ
        ["house_desc1", t_("ДОМ"), t_("Не все рады моему появлению в этом доме. Мне нужно немного времени и я найду способ уехать отсюда обратно в город.")],
        ["house_desc2", t_("ДОМ"), t_("Я случайно увидел Синтию в душе. Она не просто милая, но еще и очень симпатичная девчонка.")],
        ["house_desc3", t_("ДОМ"), t_("Мне нужно придумать, где взять денег. Они мне понадобятся, чтобы свалить из этой дыры как можно скорее.")],
        ["house_desc4", t_("ДОМ"), t_("У меня появилась возможность устроиться на подработку. Это отличная новость. Но есть и плохая новость - Софи смотрит на меня, как на сопливого пацана, который не может постоять за себя.")],
        ["house_desc5", t_("ДОМ"), t_("У меня появилась возможность устроиться на подработку. Это отличная новость. Но есть и плохая новость - мне уже приходится врать Софи...")],
        ["house_desc6", t_("ДОМ"), t_("Оливия... Она настоящая красотка... Такая уверенная в себе и... Секси.")],
        ["house_desc7", t_("ДОМ"), t_("Еее! Первые деньги на билет уже в кармане. Начало положено!")],
        ["house_desc8", t_("ДОМ"), t_("Просмотр фильма с Синтией - это нечто. Она такая... такая прикольная. Надо бы почаще проводить время с ней...")],
        ["house_desc9", t_("ДОМ"), t_("На какой-то момент мне показалось, что Оливия стала ко мне относится нормально... Алкоголь и массаж действуют на нее успокаивающе.")],

        # КОЛЛЕДЖ
        ["college_desc1", t_("КОЛЛЕДЖ"), t_("О, фак. Все-таки мне придется тащиться в этот колледж. Я надеюсь, что никто из моих бывших одноклассников сюда не поступил.")],
        ["college_desc2", t_("КОЛЛЕДЖ"), t_("Я рад, что встретил Шона. Он единственный человек из моей бывшей школы, который нормально ко мне относился.")],
        ["college_desc3", t_("КОЛЛЕДЖ"), t_("Роуз очень приятная и симпатичная девушка. Может, стоит познакомиться с ней поближе?")],
        ["college_desc4", t_("КОЛЛЕДЖ"), t_("Миссис Морис преподает живопись. Кажется, я определился с дополнительным предметом.")],
        ["college_desc5", t_("КОЛЛЕДЖ"), t_("Интересно, что в этой папке на столе у мисс Янг?.. Вдруг там какая-нибудь важная инфа? Надо будет проверить при первой же возможности...")],
        ["college_desc6", t_("КОЛЛЕДЖ"), t_("Эта Кларк настолько суровая, что ей лучше бы не в колледже работать, а надзирателем в тюрьме.")],
        ["college_desc7", t_("КОЛЛЕДЖ"), t_("Мне нужно обязательно попасть на занятия к миссис Моррис. Живопись - это скучно. Но мне пофиг. Буду старательно изображать интерес к ее предмету.")],
        ["college_desc8", t_("КОЛЛЕДЖ"), t_("Милашка Роуз сказала в раздевалке, что за мной должок... Хм, интересно, каким образом мне нужно будет с ней расплачиваться?")],
        ["college_desc9", t_("КОЛЛЕДЖ"), t_("У тренера Брукс отпадная фигура. Думаю, стоит сходить к ней на тренировку...")],
        ["college_desc10", t_("КОЛЛЕДЖ"), t_("Хмм... Возможно, мне стоит почаще заглядывать в библиотеку?..")],
        ["college_desc11", t_("КОЛЛЕДЖ"), t_("Эмили такая красотка!.. Вот бы отбить ее у этого безмозглого качка Гарри...")],

        # ШОН
        ["sean_desc1", t_("ШОН"), t_("Шон сказал, что ему нравятся милфы. Хмм, никогда бы не подумал... Интересно, с кем он был на фотке?")],
        ["sean_desc2", t_("ШОН"), t_("Вот это прайс у проститутки Бекки! Мне сейчас не по карману даже минет в ее исполнении... Как Шону удалось организовать встречу с ней?")]
    ]
    return

label show_questlog:
    $ questLogJustUpdated = False
    call questLog_init() from __rcall_questLog_inita1
    $ inText = ""
    python:
        firstCategory = True
        lastCategory = False
        for questLogLine in questLogData:
            if str(questLogLine[0]) in questLogDataEnabled and questLogDataEnabled[str(questLogLine[0])] == True and questLogLine[2] == True:
                if t__(questLogLine[3]) != lastCategory:
                    lastCategory = t__(questLogLine[3])
                    if firstCategory != True:
                        inText = inText + "\n"
                    inText = inText + "{=phone_notes_category_text}{u}" + t__(lastCategory) + "{/u}{/=questlog_text_category_style}\n{vspace=5}"
                    firstCategory = False
                if str(questLogLine[0]) in questLogLinesUpdated:
                    inText = inText + "{=phone_notes_text_new}" + t__(questLogLine[1]) + "{/=phone_notes_text_new}\n"
                else:
                    inText = inText + t__(questLogLine[1]) + "\n"
#    sound open_map
#    call screen questlog_screen(inText)
    $ questLogLinesUpdated = []
#    sound open_map
    return inText

label show_questhelp:
    $ questHelpJustUpdated = False
    call questHelp_init() from _rcall_questHelp_init_1

    python:
        questHelpDataLastCategoryMemory = {}
        questHelpDataLastQuestsBold = {}
        questHelpDataCategoriesBold = {}
        for questCategoryName in questHelpData:
            for idx1 in range(0, len(questHelpData[questCategoryName])):
                tempVar1 = questHelpData[questCategoryName][idx1]
                if questHelpDataLastMemory.has_key(tempVar1[0]) == False:
                    questHelpDataLastMemory[tempVar1[0]] = tempVar1[1]
                    questHelpDataLastQuestsBold[tempVar1[0]] = True
                    questHelpDataCategoriesBold[questCategoryName] = True
                    questHelpCurrentCategory = questCategoryName
                else:
                    if questHelpDataLastMemory[tempVar1[0]] != tempVar1[1]:
                        questHelpDataLastQuestsBold[tempVar1[0]] = True
                        questHelpDataCategoriesBold[questCategoryName] = True
                        questHelpCurrentCategory = questCategoryName

                if questHelpDataLastCategoryMemory.has_key(questCategoryName) == False:
                    questHelpDataLastCategoryMemory[questCategoryName] = -100
                if questHelpDataLastCategoryMemory[questCategoryName] == -100:
                    questHelpDataLastCategoryMemory[questCategoryName] = tempVar1[1]
                else:
                    if questHelpDataLastCategoryMemory[questCategoryName] == -1:
                        questHelpDataLastCategoryMemory[questCategoryName] = tempVar1[1]
                    else:
                        if questHelpDataLastCategoryMemory[questCategoryName] == 1:
                            questHelpDataLastCategoryMemory[questCategoryName] = tempVar1[1]
                        else:
                            if questHelpDataLastCategoryMemory[questCategoryName] == -100:
                                questHelpDataLastCategoryMemory[questCategoryName] = tempVar1[1]

    $ questHelpJustUpdated = False
    sound keyboard_click
label show_questhelp_loop:
    $ interact_data_questhelp = None
    show screen questhelp_screen()
    $ interact_data_questhelp = ui.interact()
    if interact_data_questhelp != None and interact_data_questhelp != False:
        if interact_data_questhelp[0] == "category_click":
            if questHelpCurrentCategory != interact_data_questhelp[1]:
                $ questHelpCurrentQuest = False
            $ questHelpCurrentCategory = interact_data_questhelp[1]
            $ questHelpCurrentQuest = ""
            sound keyboard
            jump show_questhelp_loop

        if interact_data_questhelp[0] == "quest_click":
            $ questHelpCurrentQuest = interact_data_questhelp[1]
            if questHelpCurrentQuest == "other2":
                $ questHelp("other2", True)
            sound keyboard
            jump show_questhelp_loop

    hide screen questhelp_screen
    sound snd_ui_not_working

    python:
        for questCategoryName in questHelpData:
            for idx1 in range(0, len(questHelpData[questCategoryName])):
                tempVar1 = questHelpData[questCategoryName][idx1]
                questHelpDataLastMemory[tempVar1[0]] = tempVar1[1]

    return


label show_achievements:
    sound open_map
    call screen achievements_screen()
    sound open_map
    return
