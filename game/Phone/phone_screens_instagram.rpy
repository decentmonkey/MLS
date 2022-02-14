screen phone_instagram_screen():
    fixed:
        add "#ffffff" xsize 376 ysize 571 pos(28, 100)
        add "#c2c2c2" xsize 376 ysize 1 pos(28,100)
    viewport id "vp8":
        draggable True
        xpos 28
        ypos 95
        xysize(380, 742)
        yinitial 0.0
        arrowkeys True
        mousewheel True
        vbox:
            spacing 0
            first_spacing 0
            box_wrap_spacing 0
            if phone_instagram_mode == 0:
                $ posts_feed = phone_instagram_posts
            if phone_instagram_mode == 1:
                $ posts_feed = phone_instagram_posts_multi[phone_instagram_current_name]["posts"]

            for post in posts_feed:
                $ instagramPost = Image(post[0])
                $ imgSize = getImageSize(instagramPost, post[0])
                $ postWidth = 368
                $ postHeight = int(imgSize[1] * (imgSize[0]/postWidth))
                button:
                    margin (0,0)
                    padding (0,0)
                    ypos 0
                    xpos 0
                    xsize 380
                    ysize postHeight
                    background None
                    add post[0]:
                        xsize postWidth
                        ysize postHeight
                    if len(post)>1:
                        frame:
                            xmaximum 348
                            yminimum 50
                            background "#ffffff"
                            pos(10,485)
                            text t__(post[1]) style "phone_instagram_caption":
                                if _preferences.language == "chinese":
                                    font gui.text_font_chinese
                                pos(0, 0.5)
                                yanchor 0.5
                                line_spacing 3
                    action [
                        Return([False])
                    ]

    vbar value YScrollValue("vp8") xpos 396 ypos 96 xsize 8 ysize 730
#        style_prefix "blue"


screen phone_instagram_list_screen():
    frame:
        pos(46,85)

        background None
        xmaximum 378
        text t__("Instagram") style "phone_header1":
            if _preferences.language == "chinese":
                font gui.text_font_chinese
                size 32
            xpos -8
            ypos 16

        viewport id "vp2":
            draggable True
            xpos -24
            ypos 70
            xysize(378, 690)
            yinitial 0.0
            arrowkeys True
            mousewheel True
            vbox:
#                xpos -24
                spacing 0
                first_spacing 0
                box_wrap_spacing 0
                for contact_name in phone_instagram_posts_multi:
#                    $ contactImg = Image(contact["img"])
                    $ contact = phone_instagram_posts_multi[contact_name]
                    $ newPosts = False
                    if contact_name in phone_instagram_new:
                        $ newPosts = True

                    if contact.has_key("visible") == False or (contact.has_key("visible") == True and contact["visible"] == True):
                        $ contactImg = Transform(contact["img"], size=(65,65))

                        button:
                            margin (0,0)
                            padding (0,0)
                            ypos 0
                            xpos 0
                            ysize 79
                            xsize 378
        #                    xpos -64

                            if newPosts == True:
                                idle_background "#e5ffe5"
                                hover_background "#e0f0e0"
                            else:
                                idle_background "#feffff"
                                hover_background "#e0e0e0"

#                            idle_background "#feffff"
#                            hover_background "#e0e0e0"
                            add "/images/Phone/mess/bg_contact.png":
                                pos (0,0)
                            add AlphaMask(contactImg, "/images/Phone/mess/contact_circle.png"):
                                pos (8,8)
    #                            xsize 65
    #                            ysize 65
                            text t__(contact["caption"]) style "phone_instagram_contact_name":
                                if _preferences.language == "chinese":
                                    font gui.text_font_chinese
                                    size 24
                                if newPosts == True:
                                    xpos 105
                                else:
                                    xpos 83
                                ypos 20
                            if newPosts == True:
                                add Transform("/images/Phone/new_mess.png", size=(16,16)):
                                    pos(83,30)
                            add "/images/Phone/mess/ellipsis.png":
                                pos(340,23)
                            action [
                                Return(["open_instagram_page", contact_name, contact])
                            ]
        vbar value YScrollValue("vp2") xpos 343 ypos 70 xsize 8 ysize 654    