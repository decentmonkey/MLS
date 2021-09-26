# sms.rpy by Руслан barsunduk Небыков
# 10.04.2016 (доработано 19.06.2017) лизензия: CC0
init:
    transform _a(alpha=0.0):
        alpha alpha

init python:
    sms_text = []
    sms_text2 = []
    what2 = ""
    who2 = ""
    # заголовок можно менять в любой момент, меняя эту переменную
    sms_name = "Неизвестный"
    pp = 20
    test_sms_def = 0
    # изъять текст смс из текстбокса и закинуть в экран смс
    def sms(txt, txt2):
        global what2, who2, sms_text2, sms_text, test_sms_def
        what2 = txt
        who2 = txt2
        #if ("{#l}" in txt) or ("{#r}" in txt):
        test_sms_def += 10
        if (who2 == "me") or (who2 == "mama"):
            sms_text.append(txt)
            sms_text2.append(txt2)
            test_sms_def += 1
            what2 = ""
            who2 = ""
        # разные звуки для сообщений
        #if ("{#l}" in txt):
            #renpy.music.play("sound/incoming.mp3", channel="sound", loop=False)
        #if ("{#r}" in txt):
            #renpy.music.play("sound/send.mp3", channel="sound", loop=False)
    SMS = renpy.curry(sms) # функцию в Action
    # показать экран смс
    def sms_on(effect=dissolve):
        renpy.show_screen("sms_screen", _layer="master")
        renpy.with_statement(effect)
    # спрятать экран смс
    def sms_off(effect=dissolve):
        renpy.hide_screen("sms_screen", layer="master")
        renpy.with_statement(effect)
    # очистить экран смс
    def sms_clear(effect=dissolve):
        global sms_text, sms_text2
        sms_text = []
        sms_text2 = []
        renpy.restart_interaction()
init python:
    # положение окна с смс
    sms_xalign, sms_yalign = .065, .78

    # размеры окна с смс (экран сотового)
    sms_width, sms_height = 380, 950

    # размеры одного смс
    sms_w, sms_h = int(sms_width * .75), int(config.screen_height * .05)

    # листать вниз
    yadjValue = float("inf")
    yadj = ui.adjustment()

init:
    # стиль для фрейма с смсками
    style sms_frame is frame:
        # изображение пустого экрана
        yfill True
        xminimum sms_width xmaximum sms_width
        yminimum sms_height ymaximum sms_height
        xmargin 0 ymargin 0
        xpadding 0 ypadding 0

# экран с смсками
screen sms_screen:
    python:
        yadj.value = yadjValue
    on "show" action Preference("auto-forward", "toggle")
    on "hide" action Preference("auto-forward", "toggle")
    tag iphone_xx
    add "#fff" xsize 380 ysize 812 pos(100, 100)
    textbutton "{size=54}{color=#d44d}x" action [Hide("sms_screen"), Show("iphone_x", showw = "true")] xpos 410 ypos 80
    vbox:
        align(sms_xalign, sms_yalign)
        frame:
            style "sms_frame"
            background None
            viewport:
                id "sms_vp"
                xinitial 1.0
                yfill False
                mousewheel True
                draggable False
                side_xfill True
                transclude
                yadjustment yadj
                vbox:
                    xfill True
                    yanchor 1.0
                    yalign 1.0
                    frame:
                        # изображение пустого экрана
                        background "#0000"
                        align(.065, .9)
                        yfill True
                        # ширина
                        xminimum 380
                        xmaximum 380
                        # контейнер для пузырьков с сообщениями
                        vbox:
                            spacing 16
                            xfill True
                            yanchor 1.0
                            yalign 0.83
                            for i in range(len(sms_text)):
                                # пузырьки с сообщениями
                                $sms_go_to = sms_text[i]
                                textbutton _("{color=#000}" + sms_go_to + "{/color}"):
                                    xminimum 160
                                    top_padding pp
                                    bottom_padding pp
                                    left_padding pp
                                    right_padding pp
                                    if "me" in sms_text2[i]:
                                        xalign 0.8
                                        background Frame("smsright", 60, 38)
                                    else:
                                        xalign 0.0
                                        background Frame("smsleft", 60, 38)
                                    action []

    add "iphone_x/frame.png" xpos 74 ypos 74
# копия стандартного экрана say, с небольшими изменениями,
# которые позволяют скрыть основное окно, если в тексте есть теги для смс
screen say_duplicate:
    default side_image = None
    default two_window = False
    on "show" action SMS(what, who) # сначала обрабатываем наши теги для СМС
    on "replace" action SMS(what, who)
    if not two_window:
        window:
            id "window"
            if not what2:
                background None
            vbox:
                style "say_vbox"
                text what id "what":
                    if not what2:
                        at _a(0)
    else:
        vbox:
            style "say_two_window_vbox"
            if who and what2:
                window:
                    style "say_who_window"
                    if not what2:
                        background None
                    text who:
                        id "who"
                        if not what2:
                            at _a(0)
            window:
                id "window"
                if not what2:
                    background None
                vbox:
                    style "say_vbox"
                    text what id "what"
                    if not what2:
                        at _a(0)
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0
    use quick_menu
