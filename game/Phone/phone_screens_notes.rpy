screen phone_notes_screen():
    fixed:
        viewport id "vp9":
            draggable True
            xpos 28
            ypos 95
            xysize(380, 742)
            yinitial 0.0
            arrowkeys True
            mousewheel True
            frame:
                padding (20,10)
                background None
                xsize 368
                text phone_notes_text style "phone_notes_text":
                    if _preferences.language == "chinese":
                        font gui.text_font_chinese
                        size 26

    vbar value YScrollValue("vp9") xpos 396 ypos 96 xsize 8 ysize 730
