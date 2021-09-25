default questLogDataEnabled = {}
default questLogLinesUpdated = []

#call question_helper_enable("question_helper_hairdye_find_julia")
#call question_helper_disable()

label questLog_init:
    $ questLogData = [
#    [55, t_("Барди совсем обнаглел и заставляет меня быть мамой для своего одноклассника. Такого же неудачника как он сам!"), True, t_("Барди")],
    ]
    return

label questHelp_init:
    # в начале игры активно:
    $ questHelpDataQuests = {
        # ДОМ
#        "house_1" : [t_("ДОМ"), t_("Хорошая гувернантка"), t_("Убираться в доме каждый день. Уровень отношений с Бетти начинает расти после 3-х уборок подряд и увеличивается при каждой уборке.")],
    }


    $ questHelpDataCategoriesDescriptions = [
        # ДОМ
#        ["house_desc1", t_("ДОМ"), t_("Бетти ждет от меня, что я буду регулярно убираться в доме.")],
    ]
    return

label show_questlog:
    $ questLogJustUpdated = False
    call questLog_init() from __rcall_questLog_inita1
    $ inText = ""
    python:
        lastCategory = False
        for questLogLine in questLogData:
            if str(questLogLine[0]) in questLogDataEnabled and questLogDataEnabled[str(questLogLine[0])] == True and questLogLine[2] == True:
                if t__(questLogLine[3]) != lastCategory:
                    lastCategory = t__(questLogLine[3])
                    inText = inText + "{=questlog_text_category_style}{u}" + t__(lastCategory) + "{/u}{/=questlog_text_category_style}\n{vspace=5}"
                if str(questLogLine[0]) in questLogLinesUpdated:
                    inText = inText + "{b}{color=#002810}" + t__(questLogLine[1]) + "{/color}{/b}\n\n"
                else:
                    inText = inText + t__(questLogLine[1]) + "\n\n"
    sound open_map
    call screen questlog_screen(inText)
    $ questLogLinesUpdated = []
    sound open_map
    return

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
