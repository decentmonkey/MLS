init python:
    import time
    def brig(image, b=-0.1):
        return im.MatrixColor(image, im.matrix.brightness(b))
    def br_col(image, r = "00", g = "00", b = "00", r2 = "ea", g2 = "ea", b2 = "ea", a = "ff", a2 = "ff"):
        col = "#" + r + g + b + a
        col2 =  "#" + r2 + g2 + b2 + a2
        return im.MatrixColor(image, im.matrix.colorize(col, col2))
    sel_0 = False
    sel_1 = False
    sel_2 = False
    nnn = ""
    cutter = 0
    #0079fe
transform up_down:
    on show:
        yoffset 1220
        linear 1 yoffset 0
    on hide:
        yoffset 0
        linear 1 yoffset 1220
transform camera_rotate:
    on show:
        alpha 0
        pause 0.5
        alpha 1
        linear 0.7 rotate 90 xalign 0.5 yalign -0.1
    on hide:
        linear 0.7 rotate 90 xalign 0.5 yalign -0.1
screen down_button:
    zorder 11
    imagebutton:
        idle "iphone_x/mess/favorite.png"
        hover brig("iphone_x/mess/favorite.png", 0.2)
        selected_idle br_col("iphone_x/mess/favorite.png", "00", "79", "fe")
        xpos 110
        ypos 850
        selected sel_0
        action [Show("favorite"), Hide("contacts"), SetVariable("sel_0", True), SetVariable("sel_1", False), SetVariable("sel_2", False)]

    imagebutton:
        idle "iphone_x/mess/history.png"
        hover brig("iphone_x/mess/history.png", 0.2)
        selected_idle br_col("iphone_x/mess/history.png", "00", "79", "fe")
        xpos 170
        ypos 850
        selected sel_1
        #action [Show("contacts"), Hide("favorite"), SetVariable("sel_1", True), SetVariable("sel_0", False), SetVariable("sel_2", False)]

    imagebutton:
        idle "iphone_x/mess/contact.png"
        hover brig("iphone_x/mess/contact.png", 0.2)
        selected_idle br_col("iphone_x/mess/contact.png", "00", "79", "fe")
        xpos 230
        ypos 850
        selected sel_2
        action [Show("contacts"), Hide("favorite"), SetVariable("sel_2", True), SetVariable("sel_0", False), SetVariable("sel_1", False)]


screen iphone_x(showw = "false"):
    tag iphone_xx
    modal True
    imagebutton:
        idle "#0000"
        area (0, 0, 1920, 1080)
        action Hide("iphone_x")
    imagebutton:
        idle "iphone_x/bg_1.png"
        xpos 102
        ypos 100
        focus_mask True
        action Show("iphone_x")
        if showw == "false":
            at up_down
    add "iphone_x/ico_bg.png" xpos 110 ypos 794:
        if showw == "false":
            at up_down
    imagebutton:
        idle "iphone_x/messager.png"
        hover brig("iphone_x/messager.png", 0.2)
        xpos 130
        ypos 812
        focus_mask True
        action Show("message")
        if showw == "false":
            at up_down
    imagebutton:
        idle "iphone_x/Phone.png"
        hover brig("iphone_x/Phone.png", 0.2)
        xpos 215
        ypos 812
        focus_mask True
        action [Show("number"), SetVariable("sel_2", False), SetVariable("sel_0", False), SetVariable("sel_1", False)]
        if showw == "false":
            at up_down
    imagebutton:
        idle "iphone_x/preferens.png"
        hover brig("iphone_x/preferens.png", 0.2)
        xpos 300
        ypos 812
        focus_mask True
        action Show("options")
        if showw == "false":
            at up_down
    imagebutton:
        idle "iphone_x/contacts.png"
        hover brig("iphone_x/contacts.png", 0.2)
        xpos 385
        ypos 812
        focus_mask True
        action [Show("contacts"), SetVariable("sel_0", True), SetVariable("sel_1", False), SetVariable("sel_2", False)]
        if showw == "false":
            at up_down
    imagebutton:
        idle "iphone_x/instagram.png"
        hover brig("iphone_x/instagram.png", 0.2)
        xpos 120
        ypos 170
        if showw == "false":
            at up_down
        focus_mask True
        action Show("insta")

    imagebutton:
        idle "iphone_x/gal.png"
        hover brig("iphone_x/gal.png", 0.2)
        xpos 210
        ypos 170
        if showw == "false":
            at up_down
        focus_mask True
        action Show("gallery")
    imagebutton:
        idle "iphone_x/photo.png"
        hover brig("iphone_x/photo.png", 0.2)
        xpos 300
        ypos 170
        if showw == "false":
            at up_down
        focus_mask True
        action [Hide("iphone_x"), Show("photo")]
    imagebutton:
        idle "iphone_x/notes.png"
        hover brig("iphone_x/notes.png", 0.2)
        xpos 390
        ypos 170
        if showw == "false":
            at up_down
        focus_mask True
        action Show("notes")
    imagebutton:
        idle "iphone_x/frame.png"
        xpos 74
        ypos 74
        focus_mask True
        action Show("iphone_x")
        if showw == "false":
            at up_down
    imagebutton:
        idle "iphone_x/home.png"
        hover brig("iphone_x/home.png", -0.2)
        xpos 230
        ypos 898
        area (0, 0, 250, 50)
        action [Show("iphone_x"), Hide("insta"), Hide("options"), Hide("message"), Hide("contacts"), Hide("phone"), Hide("favorite")]
        if showw == "false":
            at up_down
    use scr_game_time(showw1 = showw)
    timer 2 action SetVariable("showw", "false")
screen favorite:
    tag iphone_xx
    modal True
    zorder 10
    add "#fff" xsize 385 ysize 812 pos(100, 100)
    add "iphone_x/frame.png" xpos 74 ypos 74
    text "{size=34}favorite" xpos 220 color "#1a1aa1" ypos 140
    textbutton "{size=54}{color=#d44d}x" action Hide("favorite") xpos 400 ypos 120
    if list_favorite != None:
        for c in range(len(list_favorite)):
            vbox:
                ypos 180
                spacing 160
                hbox:
                    xpos 120
                    ypos 10+c*76
                    spacing 10
                    $ v1 = list_favorite[c][0]
                    $ v2 = list_favorite[c][1]
                    $ v3 = list_favorite[c][2]
                    $ v4 = list_favorite[c][3]
                    add "[v1]"

                    text "[v2] [v3]" ypos 8
            imagebutton:
                idle "iphone_x/mess/i.png"
                hover brig("iphone_x/mess/i.png", 0.2)
                ypos 198 +c*76
                xpos 410
                action Show("information", info = v4)
            #text "[v4]" ypos 198 +c*76 xpos 400
    else:
        text "not favorites"
    use down_button
screen insta:
    tag iphone_xx
    modal True
    zorder 10
    text "{size=34}insta" xpos 200 color "#fafa55" ypos 200
    textbutton "hide" action Hide("insta") xpos 200 ypos 700
screen options:
    tag iphone_xx
    modal True
    zorder 10
    add "iphone_x/option/bg_2.png" xpos 104 ypos 100
    add "iphone_x/frame.png" xpos 74 ypos 74
    text "{size=34}options" xpos 220 color "#fafa55" ypos 140
    viewport id "vp":
        draggable True
        xysize (800, 600)#Размер рабочей области
        child_size (800, 1600)#Размер области скрола
        #Содержимое скрола
    vbar: #Сам бар
        xsize 33
        ysize 474
        left_bar "iphone_x/option/slider.png"
        right_bar "iphone_x/option/slider.png"
        left_gutter 2
        right_gutter 2
        thumb "iphone_x/option/bl_bar.png"
        xpos 420
        ypos 200
        value YScrollValue("vp")
    textbutton "{size=54}{color=#d44d}x" action Hide("options") xpos 400 ypos 120
    imagebutton:
        idle "iphone_x/home.png"
        hover brig("iphone_x/home.png", -0.2)
        xpos 230
        ypos 898
        area (0, 0, 250, 50)
        action [Show("iphone_x"), Hide("insta"), Hide("options"), Hide("message"), Hide("contacts"), Hide("phone")]
screen message:
    tag iphone_xx
    modal True
    zorder 10
    add "#eee" xsize 375 ysize 812 pos(102, 100)

    add "iphone_x/frame.png" xpos 74 ypos 74
    text "{size=34}message" xpos 200 color "#333" ypos 140
    textbutton "{size=54}{color=#d44d}x" action [Hide("message"), Show("iphone_x", showw = "true")] xpos 400 ypos 120
    if list_contact != None:
        for c in range(len(list_contact)):
            vbox:
                ypos 180
                spacing 160
                $ v1 = list_contact[c][0]
                $ v2 = list_contact[c][1]
                $ v3 = list_contact[c][2]
                $ v4 = list_contact[c][3]
                $ v5 = list_contact[c][4]
                hbox:
                    spacing 10
                    button:
                        xpos 114
                        ypos 10+c*78
                        background v1
                        text "[v2] [v3]" ypos -14 xpos 70
                        action Jump("sms_text")
                hbox:
                    xpos 198
                    ypos -180+c*78
                    spacing 10
                    text "{size=22}[v5]" ypos 6
            imagebutton:
                idle "iphone_x/mess/i.png"
                hover brig("iphone_x/mess/i.png", 0.2)
                ypos 198 +c*78
                xpos 420
                action Call("information", info = v4)

screen phone:
    tag iphone_xx
    modal True
    zorder 10
    add "#fff" xsize 375 ysize 812 pos(100, 100)
    add "iphone_x/frame.png" xpos 74 ypos 74
    text "{size=34}phone" xpos 220 color "#fa55fa" ypos 140

    imagebutton:
        idle "iphone_x/home.png"
        hover brig("iphone_x/home.png", -0.2)
        xpos 230
        ypos 898
        area (0, 0, 250, 50)
        action [Show("iphone_x"), Hide("insta"), Hide("options"), Hide("message"), Hide("contacts"), Hide("phone")]
screen information(info):
    modal True
    zorder 12
    frame:
        xpadding 16
        ypadding 16
        xpos 118
        ypos 184
        text "[info]" xmaximum 310
    timer 2 action Hide("information")#Скроется через 1.5 секунды
screen number:
    default cut = ""
    zorder 20
    tag iphone_xx
    add "#fff" xsize 380 ysize 812 pos(100, 100)
    modal True
    grid 3 4:
        xpos 136
        ypos 350
        spacing 40
        for i in range(1, 10):
            imagebutton:
                idle "iphone_x/mess/numb/" + str(i) + ".png"
                hover br_col("iphone_x/mess/numb/" + str(i) + ".png", "fc", "fc", "fc", "05", "95", "05")
                focus_mask True
                action [SetVariable("nnn",  nnn + str(i)), Hide("number"), Show("number")]
        imagebutton:
            idle "iphone_x/mess/numb/Asterisk.png"
            hover br_col("iphone_x/mess/numb/Asterisk.png", "09", "09", "09", "c0", "ca", "c0")
            focus_mask True
            action [SetVariable("nnn",  nnn + "*"), Hide("number"), Show("number")]
        imagebutton:
            idle "iphone_x/mess/numb/0.png"
            hover br_col("iphone_x/mess/numb/0.png", "fc", "fc", "fc", "05", "95", "05")
            focus_mask True
            action [SetVariable("nnn", nnn + "0"), Hide("number"), Show("number")]
        imagebutton:
            idle "iphone_x/mess/numb/Hashtag.png"
            hover br_col("iphone_x/mess/numb/Hashtag.png", "09", "09", "09", "c0", "ca", "c0")
            focus_mask True
            action [SetVariable("nnn", nnn + "#"), Hide("number"), Show("number")]


    if len(nnn)<=5:
        text "{size=60}[nnn]" xpos 120 ypos 200 color "222222"
    elif len(nnn)==6:
        text "{size=58}[nnn]" xpos 120 ypos 200 color "222222"
    elif len(nnn)==7:
        text "{size=56}[nnn]" xpos 120 ypos 200 color "222222"
    elif len(nnn)==8:
        text "{size=54}[nnn]" xpos 120 ypos 200 color "222222"
    elif len(nnn)==9:
        text "{size=52}[nnn]" xpos 120 ypos 200 color "222222"
    elif len(nnn)==10:
        text "{size=50}[nnn]" xpos 120 ypos 200 color "222222"
    elif len(nnn)==11:
        text "{size=48}[nnn]" xpos 120 ypos 200 color "222222"
    elif len(nnn)>=12:
        $cutter = len(nnn) - 11
        $cut = str(nnn[cutter:])
        text "{size=48}[cut]" xpos 120 ypos 200 color "222222"

    imagebutton:
        idle "iphone_x/mess/numb/Delete_icon.png"
        hover br_col("iphone_x/mess/numb/Delete_icon.png", "05", "05", "05")
        focus_mask True
        xpos 386
        ypos 810
        action [SetVariable("nnn",  nnn[:-1]), Hide("number"), Show("number")]
    imagebutton:
        idle "iphone_x/mess/numb/Phone.png"
        hover br_col("iphone_x/mess/numb/Phone.png", "09", "09", "09", "c9", "d2", "c9")
        focus_mask True
        xpos 253
        ypos 790
        action Show("phone_call", num = nnn)
    add "iphone_x/frame.png" xpos 74 ypos 74

screen phone_call(num = "None"):
    zorder 101
    add "images/iphone_x/mess/numb/bg_call.png" xpos 100 ypos 100
    text "{size=38}[num]" xpos .13 ypos .24 color "#ddd"
    add "iphone_x/frame.png" xpos 74 ypos 74
    timer 5 action Hide("phone_call")

screen my_chat(xx = 0):
    tag iphone_xx
    add "#fff" xsize 380 ysize 812 pos(100, 100)
    textbutton "{size=54}{color=#d44d}x" action [Hide("my_chat"), Show("iphone_x", showw = "true")] xpos 410 ypos 80
    frame:
        # изображение пустого экрана
        background "smsbg"
        align(.85, .0)
        yfill True
        # ширина
        xminimum 450
        xmaximum 450
        # отступ сообщений от верха
        top_padding 92
        # контейнер для пузырьков с сообщениями
        vbox:
            xfill True
            yanchor 1.0
            yalign 1.0
            for i in sms_text:
                # пузырьки с сообщениями
                textbutton _("{color=#000}" + i + "{/color}"):
                    xminimum 160
                    yminimum 100
                    top_padding pp
                    bottom_padding pp
                    left_padding pp*4
                    right_padding pp*4
                    if "{#r}" in i:
                        xalign 1.0
                        background Frame("smsright", 60, 38)
                    else:
                        xalign 0.0
                        background Frame("smsleft", 60, 38)
                    action []
            # это чтобы первые сообщения появлялись сверху
        # заголовочная часть интерфейса, прячет верхние сообщения
        add "smscaption" align(.5, .0) yoffset -92
        # имя собеседника
        text "{color=#fff}" + sms_name + "{/color}" align(.5, .0) yoffset -46


    add "iphone_x/frame.png" xpos 74 ypos 74

screen notes():
    tag iphone_xx
    add "iphone_x/bg_notes.png" xpos 100 ypos 100

    add "iphone_x/frame.png" xpos 74 ypos 74
    style_prefix "input"
    viewport id "vp2":
        draggable True
        child_size (280, 5000)
        xysize (346, 666)
        xpos 110
        ypos 180
        yinitial 1.0
        arrowkeys True
        mousewheel True
        text "[notes_text]"

    vbar value YScrollValue("vp2") xpos 471 ypos 182 xsize 4 ysize 654
    textbutton "{size=52}{color=#d44d}x" action [SetVariable("notes_text", ""), Show("iphone_x"), Hide("notes")] xpos 410 ypos 120
transform pauss(pas):
    alpha 0
    pause pas
    linear .1 alpha 1
transform up_scr(pas, ch):
    pause pas
    linear .5 ypos -0+1*ch
    linear 2.1 ypos -0+1*ch
    linear .1 ypos -0+1*ch
    linear .1 ypos -0+1*ch
    linear .1 ypos -0+1*ch
