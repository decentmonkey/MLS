screen end_update_screen():
    fixed:
        add "/images/Other/end_update.jpg" at end_update_img

        text t__("Следующее обновление уже в пути!") style "end_update_text1":
            if steamVersion == False:
                xanchor 0.5
                pos(1920/2, 460)
                at transform_end_update_text1
            else:
                xanchor 0.5
                pos(1920/2, 460)
                at transform_end_update_text1b
        if steamVersion == False:
            frame:
    #            background "#30303080"
                background None
                xanchor 1.0
    #            xsize 1150
                xmaximum 1150
                pos (1820, 200)
                vbox:
                    spacing 0
                    first_spacing 0
                    box_wrap_spacing 0

                    text t__("Мы убеждены в том, что игры должны быть качественными") style "end_update_text2" at transform_end_update_text2
    #                    pos(0, 0)
                    text t__("И обновления выходить регулярно и вовремя!") style "end_update_text2" at transform_end_update_text3
    #                    pos
                    null height 30
                    text t__("Станьте частью чего-то большего и поддержите нашу идею подпиской на {color=#303030}{a=https://patreon.com/Love7}Patreon{/a}{/color}!") style "end_update_text2" at transform_end_update_text4
            frame:
    #            background "#30303080"
                background None
                xanchor 1.0
    #            xsize 1150
                xmaximum 1300
                pos (1820, 730)
                vbox:
                    spacing 0
                    first_spacing 0
                    box_wrap_spacing 0
                    text t__("Если вы поддерживаете то, что вам нравится, сегодня") style "end_update_text3" at transform_end_update_text5
                    text t__("Вы получите больше того, что вам нравится, завтра! ;-)") style "end_update_text3" at transform_end_update_text6
            imagebutton:
                xpos 970
                ypos 915
                idle "gui/patreon_button.png"
                hover "gui/patreon_button_hover.png"
                action OpenURL("https://www.patreon.com/Love7")
                at transform_end_update_button

            imagebutton:
                xpos 1420
                ypos 909
                idle "gui/web_button.png"
                hover "gui/web_button_hover.png"
                action OpenURL("http://love7team.com/news/")
                at transform_end_update_button

style end_update_text1:
    color "#e1d1b0"
    size 60
    font "fonts/SF-Pro-Display-Regular.otf"
    outlines [(7, "#000000", 0, 0)]

style end_update_text2:
#    font "fonts/NotoSerifCJKsc-Regular.otf"
#    font "fonts/OpenSans-Regular.ttf"
#    font "fonts/tahoma.ttf"
#    font "fonts/Ubuntu-Condensed.ttf"
    font "fonts/arial.ttf"

#    font "fonts/Ubuntu-Condensed.ttf"
    color "#fa8132"
#    color "#ffffff"
    size 37
    outlines [(8, "#000000", 0, 0)]

style end_update_text3:
#    font "fonts/Ubuntu-Condensed.ttf"
    font "fonts/SF-Pro-Display-Regular.otf"
    color "#ffffff"
    size 37
    outlines [(8, "#000000", 0, 0)]

transform end_update_img:
    alpha 0.0
    linear 0.7 alpha 1.0


transform transform_end_update_text1:
    alpha 0.0
    pause 0.5
    linear 0.7 alpha 1.0
    pause 1.0
    linear 0.4 xanchor 1.0 xpos 1820 ypos 60

transform transform_end_update_text1b:
    alpha 0.0
    pause 0.5
    linear 0.7 alpha 1.0

transform transform_end_update_text2:
    alpha 0.0
    pause 4.0
    linear 0.7 alpha 1.0
transform transform_end_update_text3:
    alpha 0.0
    pause 6.0
    linear 0.7 alpha 1.0
transform transform_end_update_text4:
    alpha 0.0
    pause 8.0
    linear 0.7 alpha 1.0
transform transform_end_update_text5:
    alpha 0.0
    pause 10.0
    linear 0.7 alpha 1.0
transform transform_end_update_text6:
    alpha 0.0
    pause 12.0
    linear 0.7 alpha 1.0
transform transform_end_update_button:
    alpha 0.0
    pause 14.0
    linear 0.7 alpha 1.0

label end_update:
    $ camera_icon_enabled = False
    stop music
    sound snd_cinematic_impact
    img black_screen
    $ renpy.pause(3.0, hard=True)
    music Corporate_BPM120
    show screen end_update_screen()
    if steamVersion == False:
        $ renpy.pause(16.0, hard=True)
    else:
        $ renpy.pause(3.0, hard=True)
    w
    music stop
    scene black
    hide screen end_update_screen
    with fadelong
    pause 2.0
    $ MainMenu(confirm=False)()
