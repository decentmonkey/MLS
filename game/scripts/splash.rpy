default splashMode = False
label splashscreen:
    $ splashMode = True
    call init_launch() from _rcall_init_launch
    if debugMode == True:
        return
    img black_screen
    with Dissolve(0.5)
    img all_over_18
    with Dissolve(0.7)
    $ renpy.pause(2.0)
    img black_screen
    with Dissolve(0.5)

    scene black
    image videoIntro_Video = Movie(play="video/MLS_Trailer1.mkv", fps=30)
    show videoIntro_Video
    $ renpy.pause(0.5, hard=True)
    $ renpy.pause(47.5)
    stop music fadeout 0.5
    img black_screen
    with Dissolve(0.5)
    imgd black_screen
    $ renpy.pause(1.5)

    $ splashMode = False
    return

    stop music fadeout 0.5
    img black_screen
    with Dissolve(0.5)
    img splash_thanks
    with Dissolve(0.7)
    $ renpy.pause(1.0)
    pause 4.0
    img black_screen
    with Dissolve(0.7)
    img black_screen
    with Dissolve(0.5)
    img all_over_18
    with Dissolve(0.7)
    $ renpy.pause(2.0)

    img black_screen
    with Dissolve(0.5)
    img Patreon_Game_Logo
    with Dissolve(0.7)
    $ renpy.pause(1.0, hard=True)
    pause 4.0
    img black_screen
    $ renpy.pause(2.0)


    return

    wclean
    img decentmonkey_logo
    with fade
    pause 3.0
    img all_over_18
    with fade
    pause 3.0
    scene black
    with dissolve
    return
