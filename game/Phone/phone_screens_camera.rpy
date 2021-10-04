screen phone_camera_screen(phone_camera_image):
    tag phone
    layer "master"
    zorder 130
    button:
        background "#00000050"
        xfill True
        yfill True
        action [
            Return(["close"])
        ]
        alternate ShowMenu("save")
    frame:
        at camera_rotate
        pos(740+432/2,170 + 886/2)
        background None
        xysize(432,886)
        xanchor(0.5)
        yanchor(0.5)
        button:
            xsize 432
            ysize 886
            action [
                Return("None")
            ]
            alternate ShowMenu("save")

        fixed:
            pos (28,22)
            add "/images/Phone/bg_photo.png"

            imagebutton:
                pos(150,700)
                idle "/images/Phone/icons/photo_button.png"
                hover "/images/Phone/icons/photo_button_hover.png"
                action [
                    Return(["camera_shoot"])
                ]
            $ img = im.MatrixColor(
                phone_camera_image, im.matrix.saturation(1.0))
#                im.matrix.contrast(1.3) * im.matrix.saturation(1.1) * im.matrix.brightness(0.1))
            add img:
                xsize 645
                ysize 380
                pos(190, 330)
                xanchor 0.5
                yanchor 0.5
                rotate -90
                at camera_picture
        imagebutton:
            pos(45,42)
            idle "/images/Icons/window_close.png"
            hover im.MatrixColor("/images/Icons/window_close.png", im.matrix.brightness(0.1))
            action [
                Return(["close"])
            ]
        add "/images/Phone/frame.png"

screen phone_camera_screen2_intro(phone_camera_image):
    tag phone
    layer "master"
    zorder 150
    button:
        background "#00000080"
        xfill True
        yfill True
        at phone_background_fill2
    frame:
        at camera_show
        pos(740+432/2,170 + 886/2)
        background None
        xysize(432,886)
        xanchor(0.5)
        yanchor(0.5)
        button:
            xsize 432
            ysize 886
            action [
            ]

        fixed:
            pos (28,22)
            add "/images/Phone/bg_photo.png"

            add "/images/Phone/icons/photo_button.png":
                pos(150,700)
            $ img = im.MatrixColor(
                phone_get_gallery_image_path(phone_camera_image), im.matrix.saturation(1.0))
#                im.matrix.contrast(1.3) * im.matrix.saturation(1.1))
            add img:
                xsize 645
                ysize 380
                pos(190, 330)
                xanchor 0.5
                yanchor 0.5
                rotate -90
                at camera_picture
        add "/images/Icons/window_close.png":
            pos(45,42)
        add "/images/Phone/frame.png"

screen phone_camera_screen2(phone_camera_image):
    tag phone
    zorder 500
    button:
        background "#00000080"
        xfill True
        yfill True
        action [
            Function(phone_open_camera_capture_action, "close")
        ]
        alternate ShowMenu("save")
        at phone_background_fill2
    frame:
        at camera_show
        pos(740+432/2,170 + 886/2)
        background None
        xysize(432,886)
        xanchor(0.5)
        yanchor(0.5)
        button:
            xsize 432
            ysize 886
            action [
#                Return("None")
            ]
            alternate ShowMenu("save")

        fixed:
            pos (28,22)
            add "/images/Phone/bg_photo.png"

            imagebutton:
                pos(150,700)
                idle "/images/Phone/icons/photo_button.png"
                hover "/images/Phone/icons/photo_button_hover.png"
                action [
                    Function(phone_open_camera_capture_action, "shoot")
                    #Return(["camera_shoot"])
                ]
            $ img = im.MatrixColor(
                phone_get_gallery_image_path(phone_camera_image), im.matrix.saturation(1.0))
#                im.matrix.contrast(1.1) * im.matrix.saturation(1.1))
            add img:
                xsize 645
                ysize 380
                pos(190, 330)
                xanchor 0.5
                yanchor 0.5
                rotate -90
                at camera_picture
        imagebutton:
            pos(45,42)
            idle "/images/Icons/window_close.png"
            hover im.MatrixColor("/images/Icons/window_close.png", im.matrix.brightness(0.1))
            action [
                Function(phone_open_camera_capture_action, "close")
#                Return(["close"])
            ]
        add "/images/Phone/frame.png"

screen phone_camera_screen2_shoot():
    zorder 100
    fixed:
        add "Overlays/white_screen.jpg" at camera_shoot
    timer 1.0 action [
        Hide("phone_camera_screen2_shoot"),
        Hide("phone_camera_screen2")
    ]

screen phone_camera_capture_hud_screen_intro(flag):
    layer "master"
    zorder 50
    tag hud
    fixed:
        if flag == False:
            add "/images/Phone/icons/photo_capture_icon.png"
            pos (1827, 12)
        else:
            add "/images/Phone/icons/photo_capture_icon_hover.png"
            pos (1827, 12)

screen phone_camera_capture_hud_screen():
#    layer "master"
    zorder 500
    tag hud
    if camera_icon_enabled == True:
        fixed:
            if camera_enabled == True:
                imagebutton:
                    pos (1827, 12)
                    idle "/images/Phone/icons/photo_capture_icon.png"
                    hover "/images/Phone/icons/photo_capture_icon_hover.png"
                    action [
                        Function(phone_open_camera_capture, _update_screens=True)
#                        Return(False)
                    ]
            else:
                imagebutton:
                    pos (1827, 12)
                    idle "/images/Phone/icons/photo_capture_icon_Disabled.png"
                    hover "/images/Phone/icons/photo_capture_icon_Disabled_hover.png"
                    action [
                        Function(phone_open_camera_capture_action, "denied")
#                        Return(False)
                    ]
