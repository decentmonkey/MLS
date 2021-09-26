init python:
    currentPhotoImage = "images/bg room.jpg"
screen photo():
    #tag iphone_xx
    modal True
    frame:
        background None
        add "iphone_x/bg_photo.png" xpos 102 ypos 98
        add currentPhotoImage xpos -52 ypos 108 xsize 570 ysize 376 rotate -90
        add "iphone_x/frame.png" xpos 74 ypos 74
        imagebutton:
            xpos 254
            ypos 766
            idle "iphone_x/photo_button.png"
            hover br_col("iphone_x/photo_button.png", "05", "05", "05", "fc", "05", "05")
            focus_mask True
            action Function(list_append, photo_list, currentPhotoImage)
        imagebutton:
            idle "iphone_x/home.png"
            hover brig("iphone_x/home.png", -0.2)
            xpos 230
            ypos 898
            area (0, 0, 250, 50)
            action [Show("iphone_x"), Hide("insta"), Hide("options"), Hide("message"), Hide("contacts"), Hide("phone"), Hide("photo")]
        at camera_rotate
screen gallery():
    default row = (len(photo_list))/2
    default photo_0 = len(photo_list)
    add "#999"
    viewport id "vp2":
        draggable True
        child_size (280, 5000)
        xysize (346, 666)
        xpos 110
        ypos 180
        yinitial 1.0
        arrowkeys True
        mousewheel True
        text "[photo_0]" xpos 500 ypos 100
        if len(photo_list) >= 2:
            text '||[photo_list]||' xpos 500 ypos 100
            for photo in photo_list[0:3]:
                imagebutton:
                    xpos 10
                    ypos 10
                    idle photo
                    hover brig(photo)
                    action NullAction()
        elif  len(photo_list) == 1:
            text '|[photo_list]|' xpos 500 ypos 100
            imagebutton:
                idle photo
                hover photo
                action NullAction()
