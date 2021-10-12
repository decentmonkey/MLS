init python:
    licenses_text = "\nFollowing music compositions used in project 'MILFs of Sunville' are licensed by Jamendo S.A. (licensing.jamendo.com)\n\n"

    licenses_music_list = [
        ["Adventures of the Deaf Dreamer (JOSH WOODWARD)", "Music/Adventures_of_the_Deaf_Dreamer.ogg"],
        ["Border Blaster (JOSH WOODWARD)", "Music/Border_Blaster.ogg"],
        ["Carefree Ukulele (SEASTOCK)", "Music/Carefree_Ukulele.ogg"],
        ["Corporate BPM120 (ARACHANG)", "Music/Corporate_BPM120.ogg"],
        ["Deeper For You (MELANIE UNGAR)", "Music/Deeper_For_You.ogg"],
        ["Don't Close Your Eyes (JOSH WOODWARD)", "Music/Dont_Close_Your_Eyes.ogg"],
        ["Fly With Me (STEEP)", "Music/Fly_With_Me_short.ogg"],
        ["Little Tomcat (JOSH WOODWARD)", "Music/Little_Tomcat.ogg"],
        ["Montana (DANIEL ROBINSON)", "Music/Montana.ogg"],
        ["Postcard From Hell (JOSH WOODWARD)", "Music/Postcard_From_Hell.ogg"],
        ["Right Now (LAU)", "Music/Right_Now_Vocal.ogg"],
        ["Secretions (HELLO CITIZEN)", "Music/Secretions_Vocal.ogg"],
        ["Shining Through (ALUMO)", "Music/Shining_Through.ogg"],
        ["Step By Step (STEFANO VITA)", "Music/Step_By_Step.ogg"],
        ["Story of One Success (AKASHIC RECORDS)", "Music/Story_of_One_Success_1.ogg"],
        ["Stylish Fashion Electronic Rock (ALEXGROHL)", "Music/Stylish_Fashion_Electronic_Rock.ogg"],
        ["Stylish Hip Hop Rock (ALEXGROHL)", "Music/Stylish_Hip_Hop_Rock.ogg"],
        ["The Heat (INFRACTION)", "Music/The_Heat.ogg"],
        ["Visions Of Plenty (KEN VERHEECKE)", "Music/Visions_Of_Plenty.ogg"],
        ["Write Your Story (JOYSTOCK)", "Music/Write_Your_Story.ogg"]
    ]
    licenses_music_list_playing_idx = -1

    def licenses_play_music(idx):
        global licenses_music_list_playing_idx, licenses_music_list
        renpy.music.play(licenses_music_list[idx][1], fadein=0.5, fadeout=0.5)
        licenses_music_list_playing_idx = idx
        return

    def licenses_stop_music(idx):
        global licenses_music_list_playing_idx, licenses_music_list
        licenses_music_list_playing_idx = -1
        renpy.music.stop(channel=u'music', fadeout=1.0)
        return

screen licenses():
    tag menu

    use game_menu(t_("Licenses"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "Licenses"
            text t__(licenses_text)

            for idx in range(0, len(licenses_music_list)):
                hbox:
                    frame:
                        background None
                        pos (0,4)
                        text (licenses_music_list[idx][0])
                    if idx == licenses_music_list_playing_idx:
                        imagebutton:
                            idle "/images/Icons/play_pause_icon_selected.png"
                            hover im.MatrixColor("/images/Icons/play_pause_icon_selected.png", im.matrix.brightness(0.1))
                            action [
                                Function(licenses_stop_music, idx)
                            ]
                    else:
                        imagebutton:
                            idle "/images/Icons/play_pause_icon.png"
                            hover im.MatrixColor("/images/Icons/play_pause_icon.png", im.matrix.brightness(0.1))
                            action [
                                Function(licenses_play_music, idx)
                            ]





#
