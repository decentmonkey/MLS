screen camera_record_screen():
    fixed:
        xpos getRes(1600)
        ypos getRes(43)
        add "images/Icons2/Rec_Icon1.png" at camera_record_icon_transform

screen camera_viewfinder_screen():
    add "images/Icons2/Camera_ViewFinder.png"

screen achievements_screen():
    $ width1 = int(1217 * gui.resolution.koeff)
    $ height1 = int(872 * gui.resolution.koeff)
    $ x1 = int(377 * gui.resolution.koeff)
    $ y1 = int(107 * gui.resolution.koeff)

    $ rowOffset = getRes(22) #244x137
    $ cellSizeX = getRes(296)
    $ cellSizeY = getRes(170)
    $ cellsInRow = 4
    $ category_height = gui.resolution.gallery.category_height

    # calculate viewport size
    $ rowsAmount = 0
    for category in achievements_categories:
        $ rowsAmount += int(math.ceil(float(len(achievements_list[category[0]]))/float(cellsInRow)))
    $ viewportHeight = len(achievements_categories) * (category_height+gui.resolution.gallery.category_margin_down) + rowsAmount * cellSizeY

    layer "master"
    zorder 60
    modal True
    button:
        xfill True
        yfill True
        action [
            Return()
        ]
    frame:
        background Frame("gui/frame4" + res.suffix + ".png", left=2, top=int(80*gui.resolution.koeff), right=2, bottom=2)
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
                Return()
            ]
        viewport id "questlog_viewport":
#            xpos getRes(377+10)
#            ypos getRes(107+10)
            xpos 0
            ypos getRes(85)
            draggable True
            scrollbars "vertical"
            xmaximum getRes(1217-15)
            ymaximum getRes(852-85)
            mousewheel True
            pagekeys True
            child_size (getRes(852-85), viewportHeight)
            $ galleryX = 0
            $ galleryY = 0
            $ curY = 0
            for category in achievements_categories:
#                text category[1] style "char_face_style_caption":
                text t__(category[1]):
                    pos(rowOffset, curY)
                    font "fonts/BebasNeue Regular.ttf"
                    color category[2]
                    size 40
                $ curY += category_height
                $ cellsList = achievements_list[category[0]]

                for i in range(0,len(cellsList)):
                    $ posX = i%cellsInRow * cellSizeX + rowOffset
                    $ posY = int(i/cellsInRow) * cellSizeY
                    if get_achievement(cellsList[i][0]) == True: #########  or 1==1
                        if len(cellsList[i]) >= 3 and cellsList[i][2] != False:
                            add "images/Achievements/ach_" + cellsList[i][0] + ".jpg":
                                pos(posX, posY + curY)
                            imagebutton:
                                idle "gui/gallery_frame_play" + res.suffix + ".png"
                                hover "gui/gallery_frame_play_hover" + res.suffix + ".png"
                                xpos posX-gui.resolution.gallery.frame.offset
                                ypos posY-gui.resolution.gallery.frame.offset + curY
                                action [
                                    Call("process_gallery", cellsList[i][2])
                                ]
                        else:
                            add "images/Achievements/ach_" + cellsList[i][0] + ".jpg":
                                pos(posX, posY + curY)
                            add "gui/gallery_frame" + res.suffix + ".png":
                                pos(posX-gui.resolution.gallery.frame.offset, posY-gui.resolution.gallery.frame.offset + curY)
                    else:
                        add "images/Achievements/ach_" + cellsList[i][0] + "_disabled.jpg":
                            pos(posX, posY + curY)
                        add "gui/gallery_frame" + res.suffix + ".png":
                            pos(posX-gui.resolution.gallery.frame.offset, posY-gui.resolution.gallery.frame.offset + curY)
                    text t__(cellsList[i][1]) style "gallery_caption_text":
                        pos(posX + getRes(244/2), posY + curY + getRes(137+15))
                        anchor (0.5, 0.5)
                $ curY += int(math.ceil(float(len(cellsList))/float(cellsInRow))) * cellSizeY + gui.resolution.gallery.category_margin_down

screen hud_block:
    layer "master"
    zorder 61
    fixed:
        imagebutton:
            focus_mask True
            idle "/images/Other/intro/hud_block_button.png"
            hover "/images/Other/intro/hud_block_button.png"
            action [
                Return(["special", "intro_block"])
            ]
            alternate ShowMenu("save")

screen intro_focus(focus_img_path):
    layer "master"
    zorder 61
    fixed:
        add focus_img_path

screen train1():
    layer "master"
    zorder 10
    add "/images/Other/train/train_sky.jpg"
    frame:
        background None
        at train1_animation
        ypos 0
        add "/images/Other/train_road1.png":
            xpos 0
        add "/images/Other/train_road2.png":
            xpos 1920
        add "/images/Other/train_road3.png":
            xpos 3840
        add "/images/Other/train_road4.png":
            xpos 5760
        add "/images/Other/train_road4.png":
            xpos 6351
            xzoom -1.0
        add "/images/Other/train_road3.png":
            xpos 6351+591
            xzoom -1.0
        add "/images/Other/train_road2.png":
            xpos 6351+591+1920
            xzoom -1.0
        add "/images/Other/train_road1.png":
            xpos 6351+591+1920+1920
            xzoom -1.0
        add "/images/Other/train_road1.png":
            xpos 6351+591+1920+1920+1920

screen train2():
    layer "master"
    zorder 10
    add "/images/Other/train/train_sky.jpg"
    frame:
        at train2_animation2
        background None
        frame:
            at train2_animation
            background None
            ypos -165

            add "/images/Other/train_road1.png":
                xpos 0
            add "/images/Other/train_road2.png":
                xpos 1920
            add "/images/Other/train_road3.png":
                xpos 3840
            add "/images/Other/train_road4.png":
                xpos 5760
            add "/images/Other/train_road4.png":
                xpos 6351
                xzoom -1.0
            add "/images/Other/train_road3.png":
                xpos 6351+591
                xzoom -1.0
            add "/images/Other/train_road2.png":
                xpos 6351+591+1920
                xzoom -1.0
            add "/images/Other/train_road1.png":
                xpos 6351+591+1920+1920
                xzoom -1.0
            add "/images/Other/train_road1.png":
                xpos 6351+591+1920+1920+1920
            add "/images/Other/train_road2.png":
                xpos 6351+591+1920+1920+1920+1920
                xzoom -1.0

screen train3():
    layer "master"
    zorder 10
    add "/images/Other/train/train_sky.jpg"
    frame:
        at train3_animation2
        background None
        frame:
            at train3_animation
            background None
            ypos -400
            add "/images/Other/train_road1.png":
                xpos 0
            add "/images/Other/train_road2.png":
                xpos 1920
            add "/images/Other/train_road3.png":
                xpos 3840
            add "/images/Other/train_road4.png":
                xpos 5760
            add "/images/Other/train_road4.png":
                xpos 6351
                xzoom -1.0
            add "/images/Other/train_road3.png":
                xpos 6351+591
                xzoom -1.0
            add "/images/Other/train_road2.png":
                xpos 6351+591+1920
                xzoom -1.0
            add "/images/Other/train_road1.png":
                xpos 6351+591+1920+1920
                xzoom -1.0
            add "/images/Other/train_road1.png":
                xpos 6351+591+1920+1920+1920
            add "/images/Other/train_road2.png":
                xpos 6351+591+1920+1920+1920+1920

screen train_image(train_image_path):
    layer "master"
    zorder 20
    add train_image_path

#6351, 12702

transform train1_animation:
    xpos 0
    linear 8.0 xpos -12701
    repeat

transform train2_animation:
    zoom 0.7
    xpos 0
    linear 8.0 xpos -8890
    repeat

transform train2_animation2:
    rotate -3.2

transform train3_animation:
    zoom 0.8
    xpos 0
    linear 8.0 xpos -10160
    repeat

transform train3_animation2:
    rotate -1



#
