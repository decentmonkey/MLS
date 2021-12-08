# 381 617 617

screen questhelp_screen():
    $ width1 = int(1617 * gui.resolution.koeff)
    $ height1 = int(872 * gui.resolution.koeff)
    $ x1 = int(177 * gui.resolution.koeff)
    $ y1 = int(107 * gui.resolution.koeff)

    zorder 110
    modal True
    button:
        xfill True
        yfill True
        action [
            Return(False)
        ]
    frame:
        background Frame("gui/frame6" + res.suffix + ".png", left=2, top=int(80*gui.resolution.koeff), right=2, bottom=2)
        pos(x1, y1)
        anchor(0, 0)
        xysize (width1, height1)
        imagebutton:
            xpos 1.0
            ypos 0.0
            anchor (0.5, 0.5)
            idle "/icons/window_close" + res.suffix + ".png"
            hover "/icons/window_close_hover" + res.suffix + ".png"
            action [
                Return(False)
            ]
        if questHelpActivated == True:
            viewport id "questhelp_viewport_categories":
                xpos 0
                ypos getRes(85)
                draggable True
                xmaximum getRes(381-15)
                ymaximum getRes(852-85)
                mousewheel True
                pagekeys True

                frame:
                    background None
                    padding (getRes(10), getRes(10))
                    vbox:
                        # active categories (bold)
                        for category in reversed(questHelpCategoriesHistory):
                            if questHelpDataCategoriesBold.has_key(category):
                                python:
                                    categoryStyle = False
                                    if questHelpDataLastCategoryMemory.has_key(category) == True and questHelpDataCategoriesBold[category] == True:
                                        categoryStatus = questHelpDataLastCategoryMemory[category]
                                        if categoryStatus == -1:
                                            categoryStyle = "questhelp_category_failed"
                                        if categoryStatus == 1:
                                            categoryStyle = "questhelp_category_completed"
                                        if categoryStatus == 0:
                                            categoryStyle = "questhelp_category_active"
                                        categoryStyle = categoryStyle + "_bold"
                                        if questHelpCurrentCategory != category:
                                            pass
                                        else:
                                            categoryStyle = categoryStyle + "_selected"
                                if categoryStyle != False:
                                    textbutton t__(category) style categoryStyle:
                                        xsize getRes(350)
                                        xpadding gui.questhelp.category.xpadding1
                                        top_padding gui.questhelp.category.top_padding
                                        bottom_padding gui.questhelp.category.bottom_padding
                                        action [
                                            Return(["category_click", category])
                                        ]

                        # not-bold inactive categories
                        for category in questHelpCategoriesHistoryStatic:
                            if questHelpDataLastCategoryMemory.has_key(category):
                                python:
                                    categoryStyle = False
                                    if questHelpDataCategoriesBold.has_key(category) == False or questHelpDataCategoriesBold[category] != True:
                                        categoryStatus = questHelpDataLastCategoryMemory[category]
                                        if categoryStatus == -1:
                                            categoryStyle = "questhelp_category_failed"
                                        if categoryStatus == 1:
                                            categoryStyle = "questhelp_category_completed"
                                        if categoryStatus == 0:
                                            categoryStyle = "questhelp_category_active"
                                        if questHelpCurrentCategory == category:
                                            categoryStyle = categoryStyle + "_selected"
                                if categoryStyle != False and categoryStatus == 0:
                                    textbutton t__(category) style categoryStyle:
                                        xsize getRes(350)
                                        xpadding gui.questhelp.category.xpadding1
                                        top_padding gui.questhelp.category.top_padding
                                        bottom_padding gui.questhelp.category.bottom_padding
                                        action [
                                            Return(["category_click", category])
                                        ]


                        null height getRes(20)

                        for category in reversed(questHelpCategoriesHistory):
                            if questHelpDataLastCategoryMemory.has_key(category):
                                python:
                                    categoryStyle = False
                                    if questHelpDataCategoriesBold.has_key(category) == False or questHelpDataCategoriesBold[category] != True:
                                        categoryStatus = questHelpDataLastCategoryMemory[category]
                                        if categoryStatus == -1:
                                            categoryStyle = "questhelp_category_failed"
                                        if categoryStatus == 1:
                                            categoryStyle = "questhelp_category_completed"
                                        if categoryStatus == 0:
                                            categoryStyle = "questhelp_category_active"
                                        if questHelpCurrentCategory == category:
                                            categoryStyle = categoryStyle + "_selected"
                                if categoryStyle != False and categoryStatus != 0:
                                    textbutton t__(category) style categoryStyle:
                                        xsize getRes(350)
                                        xpadding gui.questhelp.category.xpadding1
                                        top_padding gui.questhelp.category.top_padding
                                        bottom_padding gui.questhelp.category.bottom_padding
                                        action [
                                            Return(["category_click", category])
                                        ]
            fixed:
                xpos 0
                ypos getRes(85 + 852-85 - 52)

                add "gui/frame6_overlay" + res.suffix + ".png":
                    size (getRes(381-15), getRes(52))

            viewport id "questhelp_viewport_events":
                xpos getRes(381)
                ypos getRes(85)
                draggable True
                scrollbars "vertical"
                xmaximum getRes(617-15)
                ymaximum getRes(852-85)
                mousewheel True
                pagekeys True
                frame:
                    background None
                    padding (getRes(10), getRes(10))
                    vbox:
                        #description
                        python:
                            descriptionText = ""
                            for idx in range(0, len(questHelpDataCategoriesDescriptions)):
                                if questHelpDataCategoriesDescriptionsData.has_key(questHelpDataCategoriesDescriptions[idx][0]) and questHelpDataCategoriesDescriptions[idx][1] == questHelpCurrentCategory:
                                    if len(descriptionText) > 0:
                                        descriptionText = descriptionText + "\n\n"
                                    descriptionText = descriptionText + t__(questHelpDataCategoriesDescriptions[idx][2])


                        if len(descriptionText) > 0:
                            text descriptionText style "questhelp_category_description"
                            #рисуем разделитель
                            null height getRes(20)
                            frame:
                                left_margin getRes(20)
                                xysize(getRes(617 - 15 - 60), 1)
                                background "#c0c0c0"
                            null height getRes(10)

                        if questHelpData.has_key(questHelpCurrentCategory) == True:
                            # выводим квесты
                            # Сначала жирные или активные

                            for idx in range(len(questHelpData[questHelpCurrentCategory])-1, -1, -1):
                                $ questData = questHelpData[questHelpCurrentCategory][idx]
                                if questData[1] == 0 or (questHelpDataLastQuestsBold.has_key(questData[0]) == True and questHelpDataLastQuestsBold[questData[0]] == True): # если квест не жирный (не только что)
                                    python:
                                        questStyle = False
                                        questTextPrefix = ""
                                        if questData[1] == 1:
                                            questStyle = "questhelp_quest_completed"
                                            questTextPrefix = "{image=images/Icons/questhelp/checkmark_completed" + res.suffix + ".png}  "
                                        if questData[1] == -1:
                                            questStyle = "questhelp_quest_failed"
                                            questTextPrefix = "{image=images/Icons/questhelp/checkmark_failed" + res.suffix + ".png}  "
                                        if questData[1] == 0:
                                            questTextPrefix = "{image=images/Icons/questhelp/checkmark_active" + res.suffix + ".png}  "
                                            questStyle = "questhelp_quest_active"

                                        if questHelpDataLastQuestsBold.has_key(questData[0]) == True and questHelpDataLastQuestsBold[questData[0]] == True: # если жирный
                                            questStyle = questStyle + "_bold"
                                        if questData[0] == questHelpCurrentQuest:
                                            questStyle = questStyle + "_selected"
                                    if questStyle != False:
                                        # выводим
                                        textbutton questTextPrefix + t__(questHelpDataQuests[questData[0]][1]) style questStyle:
                                            xsize getRes(617 - 15 - 20)
                                            xpadding gui.questhelp.quest.xpadding
                                            top_margin gui.questhelp.quest.top_margin
                                            top_padding gui.questhelp.quest.top_padding
                                            bottom_padding gui.questhelp.quest.bottom_padding
                                            action [
                                                Return(["quest_click", questData[0]])
                                            ]

                            # затем завершенные и проваленные
                            for idx in range(len(questHelpData[questHelpCurrentCategory])-1, -1, -1):
                                $ questData = questHelpData[questHelpCurrentCategory][idx]
                                if questData[1] == 1 or questData[1] == -1:
                                    if questHelpDataLastQuestsBold.has_key(questData[0]) == False or questHelpDataLastQuestsBold[questData[0]] == False: # если квест не жирный (не только что)
                                        python:
                                            questStyle = False
                                            questTextPrefix = ""
                                            if questData[1] == 1:
                                                questStyle = "questhelp_quest_completed"
                                                questTextPrefix = "{image=images/Icons/questhelp/checkmark_completed_lowbright" + res.suffix + ".png}  "
                                            if questData[1] == -1:
                                                questStyle = "questhelp_quest_failed"
                                                questTextPrefix = "{image=images/Icons/questhelp/checkmark_failed_lowbright" + res.suffix + ".png}  "
                                            if questData[0] == questHelpCurrentQuest:
                                                questStyle = questStyle + "_selected"
                                        if questStyle != False:
                                            # выводим
                                            textbutton questTextPrefix + t__(questHelpDataQuests[questData[0]][1]) style questStyle:
                                                xsize getRes(617 - 15)
                                                xpadding gui.questhelp.quest.xpadding
                                                top_margin gui.questhelp.quest.top_margin
                                                top_padding gui.questhelp.quest.top_padding
                                                bottom_padding gui.questhelp.quest.bottom_padding
                                                action [
                                                    Return(["quest_click", questData[0]])
                                                ]
            fixed:
                xpos getRes(381)
                ypos getRes(85 + 852-85 - 52)

                add "gui/frame6_overlay" + res.suffix + ".png"


            viewport id "questhelp_viewport_event_descriptions":
                xpos getRes(381 + 617)
                ypos getRes(85)
                draggable True
                xmaximum getRes(617-15)
                ymaximum getRes(852-85)
                mousewheel True
                pagekeys True
                frame:
                    background None
                    padding (getRes(10), getRes(10))
                    vbox:
                        if questHelpCurrentQuest != False and questHelpDataQuests.has_key(questHelpCurrentQuest) and len(questHelpDataQuests[questHelpCurrentQuest]) > 2:
                            text t___(questHelpDataQuests[questHelpCurrentQuest][2]) style "questhelp_quest_description_text"
        else:
            add "images/Icons2/questHelp_disabled_background.png":
                xpos 0
                ypos getRes(80)

            text t__("Для активации списка событий необходимо начать новую игру, либо загрузить игру, созданную в Episode 1") style "questhelp_disabled_text":
                xpos 0.5
                ypos 0.4
                xanchor 0.5

    key "e" action [
        Return(False)
    ]

screen rat_rabbit_choice():
    zorder 100
    button:
        xfill True
        yfill True
        action [
            Return(False)
        ]
    fixed:
        imagebutton:
#            pos(640,560)
            pos (0.4,0.65)
            anchor (0.5, 0.5)
            idle "/images/Icons2/rat_button.png"
            hover im.MatrixColor("/images/Icons2/rat_button.png", im.matrix.brightness(0.1))
            action [
                Return("rat")
            ]
        imagebutton:
#            pos(640,560)
            pos (0.6,0.65)
            anchor (0.5, 0.5)
            idle "/images/Icons2/rabbit_button.png"
            hover im.MatrixColor("/images/Icons2/rabbit_button.png", im.matrix.brightness(0.1))
            action [
                Return("rabbit")
            ]

screen image_shake(imagePath):
    layer "master"
    zorder 15
    add imagePath at image_shake1
