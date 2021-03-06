python early:
    language_fields = {None:1, "english":2, "german":3, "spanish":4, "chinese":5, "french":6, "turkish":7, "italian":8, "ukrainian":9, "hungarian":10, "czech":11}

    language_credits = {
        "english": "Thanks for the English translation to\n[Aesthetic Dialectic] & [bambam]",
        "german": "Thanks for the German translation to\n[Ragnaroekr] & [Londo Mollari]",
        "spanish": "Thanks for the Spanish translation to\n[kt9]",
        "french": "Thanks for the French translation to\n[Jay Staff] & [Poussin1er]",
#        "italian": "Thanks for the Italian translation to\n[5n4k3]",
        "turkish": "Thanks for the Turkish translation to\n[LEGOLAS]",
        "ukrainian": "Thanks for the Ukrainian translation to\n[EraRamp]",
        "chinese": "Thanks for the Chinese translation to\n[freeacer]",
        "czech" : "Thanks for the Czech translation to\n[Mr_Missclick]",
        "None": "Thanks for the Russian proofread to\n[Ms. Mansfield] & [EraRamp]"
    }

    def overlay_parse(lex):
        img = lex.simple_expression()
        overlay = lex.simple_expression()
        return (img, overlay)
    def overlay_exec(o):
        imgName, overlayName = o
        try:
            imagePathExt = img_find_path_ext(str(renpy.eval(imgName)) + "_oversprite")
        except:
            imagePathExt = img_find_path_ext(str(imgName) + "_oversprite")
        if imagePathExt[0] == False:
            imagePath = "images/Slides/img_" + imagePathExt[1] + ".jpg"
        else:
            imagePath = imagePathExt[0]
            imgName = imagePathExt[1]
        try:
            overlayName = renpy.eval(overlayName)
        except:
            overlayName = overlayName
        canvas_offsets = get_overlay_canvas_offset(imgName)
        renpy.show_screen("show_image_screen_image_overlay", imagePath, canvas_offsets, overlayName)
        return

    def overlay_pred(o):
        imgName, overlayName = o
        try:
            imagePathExt = img_find_path_ext(str(renpy.eval(imgName)) + "_oversprite")
        except:
            imagePathExt = img_find_path_ext(str(imgName) + "_oversprite")
        if imagePathExt[0] == False:
            imagePath = "images/Slides/img_" + imagePathExt[1] + ".jpg"
        else:
            imgName = imagePathExt[1]
            imagePath = imagePathExt[0]
        return [Image(imagePath)]
    renpy.register_statement("overlay", parse=overlay_parse, execute=overlay_exec, predict=overlay_pred) #?????????????????? overlay

    def img_disp(l):
        return (l.simple_expression(), l.rest())
#        return l.string()

    def imgd_disp(l):
        return (l.simple_expression(), "d")
    def imgf_disp(l):
        return (l.simple_expression(), "f")
    def imgfl_disp(l):
        return (l.simple_expression(), "fl")

    def img_exec(s_in):
        global dialogue_active_flag, screenActionHappened, config, blink_preset, blink_preset2, blink_preset3, blink_preset4, blink_preset5, blink_preset6, images_history_list, day, current_slide, blinksListStopped, blinksListActive, current_slide_image, blink1, blink2, blink3, blink4, blink5, blink6
#        config.has_autosave = False
#        config.autosave_on_choice = False
        s = s_in[0]
        transition = s_in[1]
        try:
            imagePathExt = img_find_path_ext(renpy.eval(s))
            current_slide = renpy.eval(s)
        except:
            imagePathExt = img_find_path_ext(s)
            current_slide = s
        if imagePathExt[0] == False:
            imagePath = "images/Slides/img_" + imagePathExt[1] + ".jpg"
        else:
            imagePath = imagePathExt[0]
        if renpy.exists(imagePath) == False and not renpy.android:
            imagePath = "images/Overlays/black_screen.jpg"

        images_history_list[imagePathExt[1]] = day
        check_achievement(imagePathExt[1])
        if (renpy.get_screen("say") != None or renpy.get_screen("choice") != None or renpy.get_screen("window") != None or dialogue_active_flag == True) and persistent.pause_before_change_slide == True and renpy.get_screen("show_image_screen_image") != None:
            renpy.hide_screen("say")
            renpy.hide_screen("choice")
            renpy.hide("window")
            renpy.show_screen("dialogue_down_arrow")
            renpy.pause()
            renpy.hide_screen("dialogue_down_arrow")
            dialogue_active_flag = False
        storeImagesList(imagePath, s)
        if current_slide_image != imagePath:
            renpy.scene()
        renpy.show_screen("show_image_screen_image", imagePath)
        renpy.show_screen("phone_camera_capture_hud_screen")

        if current_slide_image != imagePath:
#            print "showing blink!"
            #blink controller
            blinksListStopped = []
            for blinkName in blinksListActive:
                blinksListStopped.append(blinkName)
            blinksListActive = []
            blinkBase = imagePathExt[1]
            offsets_blink_process = offsets_blink
            if gui.flag720 == True:
                offsets_blink_process = offsets_blink_720p
            if offsets_blink_process.has_key(blinkBase):
                blinkCharacterIdx = 0
                for blink_character in offsets_blink_process[blinkBase]:
                    blink_data = offsets_blink_process[blinkBase][blink_character]
                    blinkImage = "images/Overlays/Blink/" + blinkBase + "_blink_" + blink_character + ".png"
                    blinksListActive.append(blinkImage)
                    blinkPresetId = blink_data[3]
                    if blinkCharacterIdx == 0:
                        if blink_preset != False:
                            blinkPresetId = blink_preset
                            blink_preset = False
                        blink1 = BlinkStrip(blinkImage, blink_data[2], blink_presets[blinkPresetId])
                        renpy.show_screen("blink_screen1a", blinkImage, blink_data, blink_presets[blinkPresetId], blink1)
                    if blinkCharacterIdx == 1:
                        if blink_preset2 != False:
                            blinkPresetId = blink_preset2
                            blink_preset2 = False
                        blink2 = BlinkStrip(blinkImage, blink_data[2], blink_presets[blinkPresetId])
                        renpy.show_screen("blink_screen2a", blinkImage, blink_data, blink_presets[blinkPresetId], blink2)
                    if blinkCharacterIdx == 2:
                        if blink_preset3 != False:
                            blinkPresetId = blink_preset3
                            blink_preset3 = False
                        blink3 = BlinkStrip(blinkImage, blink_data[2], blink_presets[blinkPresetId])
                        renpy.show_screen("blink_screen3a", blinkImage, blink_data, blink_presets[blinkPresetId], blink3)
                    if blinkCharacterIdx == 3:
                        if blink_preset4 != False:
                            blinkPresetId = blink_preset4
                            blink_preset4 = False
                        blink4 = BlinkStrip(blinkImage, blink_data[2], blink_presets[blinkPresetId])
                        renpy.show_screen("blink_screen4a", blinkImage, blink_data, blink_presets[blinkPresetId], blink4)
                    if blinkCharacterIdx == 4:
                        if blink_preset5 != False:
                            blinkPresetId = blink_preset5
                            blink_preset5 = False
                        blink5 = BlinkStrip(blinkImage, blink_data[2], blink_presets[blinkPresetId])
                        renpy.show_screen("blink_screen5a", blinkImage, blink_data, blink_presets[blinkPresetId], blink5)
                    if blinkCharacterIdx == 5:
                        if blink_preset6 != False:
                            blinkPresetId = blink_preset6
                            blink_preset6 = False
                        blink6 = BlinkStrip(blinkImage, blink_data[2], blink_presets[blinkPresetId])
                        renpy.show_screen("blink_screen6a", blinkImage, blink_data, blink_presets[blinkPresetId], blink6)
                    blinkCharacterIdx += 1

        current_slide_image = imagePath
        image_screen_scene_flag = False
        screenActionHappened = True
        if transition and transition != "":
            transitions_dict = {
                "f": fade,
                "d": diss,
                "fl": fadelong
            }
            if transitions_dict.has_key(transition):
                transition = transitions_dict[transition]
            else:
                try:
                    transition = renpy.eval(transition)
                except:
                    transition = transition
            renpy.with_statement(transition)
        return

    def img_pred(s_in):
        s, transition = s_in
        try:
            imagePathExt = img_find_path_ext(renpy.eval(s))
        except:
            imagePathExt = img_find_path_ext(s)
        if imagePathExt[0] == False:
            imagePath = "images/Slides/img_" + imagePathExt[1] + ".jpg"
        else:
            imagePath = imagePathExt[0]
        return [Image(imagePath)]
    renpy.register_statement("img", parse=img_disp, execute=img_exec, predict=img_pred) #?????????????????? scene
    renpy.register_statement("imgd", parse=imgd_disp, execute=img_exec, predict=img_pred)
    renpy.register_statement("imgf", parse=imgf_disp, execute=img_exec, predict=img_pred)
    renpy.register_statement("imgfl", parse=imgfl_disp, execute=img_exec, predict=img_pred)

    def imgl_exec(s_in):
        s, transition = s_in
        global dialogue_active_flag, screenActionHappened
        storeImagesList(img_find_path(s), s)
        renpy.show_screen("dialogue_image_black_overlay")
        renpy.show_screen("dialogue_image_left", img_find_path(s), config.screen_width / 2, config.screen_height)
        screenActionHappened = True

    renpy.register_statement("imgl", parse=img_disp, execute=imgl_exec, predict=img_pred)

    def imgr_exec(s_in):
        s, transition = s_in
        global dialogue_active_flag, screenActionHappened
        storeImagesList(img_find_path(s), s)
        renpy.show_screen("dialogue_image_black_overlay")
        renpy.show_screen("dialogue_image_right", img_find_path(s), config.screen_width / 2, config.screen_height)
        screenActionHappened = True

    renpy.register_statement("imgr", parse=img_disp, execute=imgr_exec, predict=img_pred)

    def imgcenter_exec(s_in):
        s, transition = s_in
        global dialogue_active_flag, screenActionHappened
        storeImagesList(img_find_path(s), s)
        renpy.show_screen("dialogue_image_black_overlay")
        renpy.show_screen("dialogue_image_center", img_find_path(s), config.screen_width / 2, config.screen_height)
        screenActionHappened = True

    renpy.register_statement("imgc", parse=img_disp, execute=imgcenter_exec, predict=img_pred)

    def playvideo_disp(l):
        return (l.simple_expression(), l.simple_expression(), l.simple_expression(), l.simple_expression(), l.simple_expression(), l.simple_expression(), l.simple_expression())

    def playvideo_pred(s_in):
        video_filename_in, sounds_filename_in, from_time_in, sound_volume_in, music_volume_in, loop_in, transition = s_in
        try:
            video_filename = renpy.eval(video_filename_in)
        except:
            video_filename = video_filename_in
        try:
            sounds_filename = renpy.eval(sounds_filename_in)
        except:
            sounds_filename = sounds_filename_in
        try:
            from_time = renpy.eval(from_time_in)
        except:
            from_time = from_time_in
        try:
            sound_volume = renpy.eval(sound_volume_in)
        except:
            sound_volume = sound_volume_in
        try:
            music_volume = renpy.eval(music_volume_in)
        except:
            music_volume = music_volume_in
        try:
            loop = renpy.eval(loop_in)
        except:
            loop = loop_in
        video_filename = "<from " + str(from_time) + " loop 0.0>" + video_filename
        sounds_filename = "<from " + str(from_time) + " loop 0.0>" + sounds_filename
        return [Movie(video_filename, channel="movie", loop=True)]

    def playvideo_exec(s_in):
        global sound_for_video, sound_for_video_volume, start_video_image, video_audio_duration, current_slide_image_blocked_args, camera_icon_enabled, camera_icon_enabled_stored
        current_slide_image_blocked_args = False
        video_filename_in, sounds_filename_in, from_time_in, sound_volume_in, music_volume_in, loop_in, transition_in = s_in
        try:
            video_filename = renpy.eval(video_filename_in)
        except:
            video_filename = video_filename_in
        try:
            sounds_filename = renpy.eval(sounds_filename_in)
        except:
            sounds_filename = sounds_filename_in
        try:
            from_time = renpy.eval(from_time_in)
        except:
            from_time = from_time_in
        try:
            sound_volume = renpy.eval(sound_volume_in)
        except:
            sound_volume = sound_volume_in
        try:
            music_volume = renpy.eval(music_volume_in)
        except:
            music_volume = music_volume_in
        try:
            transition = renpy.eval(transition_in)
        except:
            transition = transition_in
        try:
            loop = renpy.eval(loop_in)
        except:
            loop = loop_in

        renpy.scene()
#        if transition_in == "vpunch" or transition_in == "hpunch" or transition_in == "None" or from_time > 0.0:
#            renpy.show("black")

#        imagePathExt = img_find_path_ext(start_video_image)
#        start_image = imagePathExt[0]
        start_image = start_video_image
        video_audio_duration = 0

        if loop == True:
            video_filename = "<from " + str(from_time) + " loop 0.0>" + video_filename
            if sounds_filename != None and sounds_filename != False and sounds_filename != "False":
                imagePathExt = img_find_path_ext(sounds_filename)
                sounds_filename = imagePathExt[0]
                sounds_filename = "<from " + str(from_time) + " loop 0.0>" + sounds_filename
            else:
                sounds_filename = False
    #        sounds_filename = sounds_filename
    #        sounds_filename = "<sync music>" + sounds_filename
            movie1 = Movie(play=video_filename, channel="movie",loop=True, play_callback=playvideo_exec_play_callback, start_image = start_image)
            renpy.show_screen("show_image_screen_movie", movie1)
            sound_for_video = False
            if sounds_filename != False:
    #            renpy.music.play(sounds_filename, channel="music2", loop=True, fadein=0.5, relative_volume=sound_volume, synchro_start=True)
                sound_for_video = sounds_filename
                sound_for_video_volume = sound_volume
                renpy.music.set_volume(music_volume, delay=0.5, channel="music")
        else:
            video_filename = "<from " + str(from_time) + ">" + video_filename
            if sounds_filename != None and sounds_filename != False and sounds_filename != "False":
                imagePathExt = img_find_path_ext(sounds_filename)
                sounds_filename = imagePathExt[0]
                sounds_filename = "<from " + str(from_time) + ">" + sounds_filename
            else:
                sounds_filename = False

            # finding end image
            baseName = os.path.basename(os.path.splitext(video_filename)[0]).lower()
            imagePathExt = img_find_path_ext(baseName + "_end")

            movie1 = Movie(play=video_filename, channel="movie",loop=False, play_callback=playvideo_exec_play_callback, image=imagePathExt[1], start_image = start_image)
            renpy.show_screen("show_image_screen_movie", movie1)
            sound_for_video = False
            if sounds_filename != False:
                sound_for_video = sounds_filename
                sound_for_video_volume = sound_volume
                renpy.music.set_volume(music_volume, delay=0.5, channel="music")

        renpy.with_statement(transition)
        camera_icon_enabled_stored = camera_icon_enabled
        camera_icon_enabled = False


    def playvideo_exec_play_callback(old, new):
        global sound_for_video, sound_for_video_volume, video_audio_duration
        renpy.music.play(new._play, channel=new.channel, loop=new.loop, synchro_start=True)
        if sound_for_video != False:
#            renpy.music.play(sound_for_video, channel="music2", loop=new.loop, fadein=0.5, relative_volume=sound_for_video_volume, synchro_start=True)
            renpy.music.play(sound_for_video, channel="music2", loop=new.loop, fadein=0.5, synchro_start=True)
            renpy.music.set_volume(sound_for_video_volume, delay=0.0, channel="music2")
            video_audio_duration = renpy.music.get_duration("music2")

    #playvideo "video_file_name" "sound_file_name" from_time sound_volume music_volume transition
    renpy.register_statement("playvideo", parse=playvideo_disp, execute=playvideo_exec, predict=playvideo_pred)

    renpy.music.register_channel("movie", "music", loop=True, movie=True, framedrop=True)

    def stopvideo_disp(l):
        return (l.rest())
    def stopvideo_exec(s_in):
        global currentMusic2, camera_icon_enabled, camera_icon_enabled_stored
        renpy.hide_screen("show_image_screen_movie")
        renpy.music.stop(channel="music2", fadeout=0.2)
        renpy.music.set_volume(1.0, delay=0.5, channel="music")
        renpy.music.set_volume(1.0, delay=0.5, channel="music2")
        currentMusic2 = False
        camera_icon_enabled = camera_icon_enabled_stored

    renpy.register_statement("stopvideo", parse=stopvideo_disp, execute=stopvideo_exec)

    def saywrapper_parse(lex):
        who = lex.simple_expression()
        what = lex.simple_expression()
#        what = lex.string()
        if what == None:
            what = who
            who = "Noone"
        return (who,what)

    def saywrapper_lint(o):
        who, what = o
        try:
            eval(who)
        except:
            renpy.error("Character not defined: %s" % who)

        tte = renpy.check_text_tags(what)
        if tte:
            renpy.error(tte)


    def saywrapper_execute(o):
        global last_dialogue_character
        global dialogue_active_flag, screenActionHappened, config

        who, what = o
        if who == "Noone":
            who = last_dialogue_character
        else:
            last_dialogue_character = who
#        who = t__(eval(who).name)
        what = what[1:-1]
#        what = re.sub(r'\n' , '\s', what)
        dialogue_active_flag = True
        screenActionHappened = True

        keyPressed = pygame.key.get_pressed()
        if keyPressed[pygame.K_SLASH]:
            return

        what = t___(what)
#        what = re.sub(r'(\n\s*)', " ", what)
#        what = t__(what)
#        what = what.replace("??", " ")
#        what = re.sub("\!\s{1,}", "!\n", what)
#        what = re.sub("\?\s{1,}", "?\n", what)
#        what = re.sub("\.\s{1,}", ".\n", what)
#        what = re.sub("Mr\.\\n", "Mr. ", what)
#        what = re.sub("Mrs\.\\n", "Mrs. ", what)
#        what = re.sub("Ms\.\\n", "Ms. ", what)

        if persistent.auto_clipboard == True:
            copy_what = re.sub("\!\s{1,}", "!\n", what)
            copy_what = re.sub("\?\s{1,}", "?\n", copy_what)
            copy_what = re.sub("\.\s{1,}", ".\n", copy_what)
            mycopytext(copy_what) #put into clipboard

        renpy.say(who, what)

    renpy.register_statement("", parse=saywrapper_parse, execute=saywrapper_execute, lint = saywrapper_lint, translatable=True) #?????????????? ?????? say, ?????????? ???????????????? ???????? ?????????????????? ??????????????


    def w_parse(l):
        return None

    def w_exec(o):
        global dialogue_active_flag, screenActionHappened
        renpy.hide_screen("say")
        renpy.hide_screen("choice")
        renpy.hide("window")
        renpy.show_screen("dialogue_down_arrow")
        dialogue_active_flag = True
        keyPressed = pygame.key.get_pressed()
        if not keyPressed[pygame.K_SLASH]:
            renpy.pause()
        dialogue_active_flag = False
        renpy.hide_screen("dialogue_down_arrow")
        dialogue_active_flag = False
        screenActionHappened = True

    def wclean_exec(o):
        global dialogue_active_flag, screenActionHappened
        renpy.hide_screen("say")
        renpy.hide_screen("choice")
        renpy.hide("window")
        dialogue_active_flag = True
        renpy.pause()
        dialogue_active_flag = False
        screenActionHappened = True

    renpy.register_statement("w", parse=w_parse, execute=w_exec) #w - ???????????????? ???????????????? ?? ???????????????? ????????????????
    renpy.register_statement("wclean", parse=w_parse, execute=wclean_exec) #w - ???????????????? ???????????????? ?? ???????????????? ????????????????

    def wc_exec(o):
        global dialogue_active_flag
        dialogue_active_flag = False

    renpy.register_statement("wc", parse=w_parse, execute=wc_exec) #wait dialogue clear, ?????????????? ???????? ???????? ?????? ?????????? ???????????????? ???????????? (?????? ????????)


    def sound_parse(l):
        return l.simple_expression()

    def sound_exec(o):
        try:
            soundName = renpy.eval(o)
        except:
            soundName = o
        checkPath = "Sounds/" + str(soundName) + ".ogg"
        if renpy.loadable(checkPath):
            renpy.play(checkPath, channel="sound")
            return
        checkPath = "Sounds/" + str(soundName) + ".wav"
        if renpy.loadable(checkPath):
            renpy.play(checkPath, channel="sound")
            return
        checkPath = "Sounds/" + str(soundName) + ".mp3"
        if renpy.loadable(checkPath):
            renpy.play(checkPath, channel="sound")
            return
        checkPath = "Music/" + str(soundName) + ".ogg"
        if renpy.loadable(checkPath):
            renpy.play(checkPath, channel="sound")
            return
        checkPath = "Music/" + str(soundName) + ".wav"
        if renpy.loadable(checkPath):
            renpy.play(checkPath, channel="sound")
            return
        checkPath = "Music/" + str(soundName) + ".mp3"
        if renpy.loadable(checkPath):
            renpy.play(checkPath, channel="sound")
            return

    renpy.register_statement("sound", parse=sound_parse, execute=sound_exec) #sound - ???????????????? ?????????????????????????????? ??????????

    def sound2_parse(l):
        return l.simple_expression()

    def sound2_exec(o):
        try:
            sound2Name = renpy.eval(o)
        except:
            sound2Name = o
        checkPath = "Sounds/" + str(sound2Name) + ".ogg"
        if renpy.loadable(checkPath):
            renpy.play(checkPath, channel="sound2")
            return
        checkPath = "Sounds/" + str(sound2Name) + ".wav"
        if renpy.loadable(checkPath):
            renpy.play(checkPath, channel="sound2")
            return
        checkPath = "Sounds/" + str(sound2Name) + ".mp3"
        if renpy.loadable(checkPath):
            renpy.play(checkPath, channel="sound2")
            return
        checkPath = "Music/" + str(sound2Name) + ".ogg"
        if renpy.loadable(checkPath):
            renpy.play(checkPath, channel="sound2")
            return
        checkPath = "Music/" + str(sound2Name) + ".wav"
        if renpy.loadable(checkPath):
            renpy.play(checkPath, channel="sound2")
            return
        checkPath = "Music/" + str(sound2Name) + ".mp3"
        if renpy.loadable(checkPath):
            renpy.play(checkPath, channel="sound2")
            return

    renpy.music.register_channel("sound2", "sfx", False)
    renpy.register_statement("sound2", parse=sound2_parse, execute=sound2_exec) #sound2 - ???????????????? ?????????????????????????????? ??????????

    def sound3_parse(l):
        return l.simple_expression()

    def sound3_exec(o):
        try:
            sound3Name = renpy.eval(o)
        except:
            sound3Name = o
        checkPath = "Sounds/" + str(sound3Name) + ".ogg"
        if renpy.loadable(checkPath):
            renpy.play(checkPath, channel="sound3")
            return
        checkPath = "Sounds/" + str(sound3Name) + ".wav"
        if renpy.loadable(checkPath):
            renpy.play(checkPath, channel="sound3")
            return
        checkPath = "Sounds/" + str(sound3Name) + ".mp3"
        if renpy.loadable(checkPath):
            renpy.play(checkPath, channel="sound3")
            return
        checkPath = "Music/" + str(sound3Name) + ".ogg"
        if renpy.loadable(checkPath):
            renpy.play(checkPath, channel="sound3")
            return
        checkPath = "Music/" + str(sound3Name) + ".wav"
        if renpy.loadable(checkPath):
            renpy.play(checkPath, channel="sound3")
            return
        checkPath = "Music/" + str(sound3Name) + ".mp3"
        if renpy.loadable(checkPath):
            renpy.play(checkPath, channel="sound3")
            return

    renpy.music.register_channel("sound3", "sfx", False)
    renpy.register_statement("sound3", parse=sound3_parse, execute=sound3_exec) #sound3 - ???????????????? ?????????????????????????????? ??????????

    def music_parse(l):
        return (l.simple_expression(), l.rest())

    def music_exec(ob1):
        global currentMusic, currentMusicPriority
        o, priority = ob1

        if o == "stop":
            currentMusic = False
            currentMusicPriority = 0
            renpy.music.stop(channel='music', fadeout=1.0)
            return
        try:
            musicName = renpy.eval(o)
        except:
            musicName = o
        if musicName == currentMusic:
            return

        try:
            priority1 = int(priority)
        except ValueError:
            priority1 = 0
        if str(priority) == "low":
            priority1 = 0
        if str(priority) == "high":
            priority1 = 10
        if priority1 < currentMusicPriority:
            return
        currentMusic = musicName
        currentMusicPriority = priority1
        checkPath = "Music/" + str(musicName) + ".ogg"
        if renpy.loadable(checkPath):
            print "play!" + str(checkPath)
            renpy.music.play(checkPath, channel="music", loop=True, fadeout=1.0, fadein=1.0)
        else:
            checkPath = "Sounds/" + str(musicName) + ".ogg"
            if renpy.loadable(checkPath):
                renpy.music.play(checkPath, channel="music", loop=True, fadeout=1.0, fadein=1.0)
        return

    renpy.register_statement("music", parse=music_parse, execute=music_exec) #music - ???????????????? ?????????????????????????????? ????????????

    def fadeblack_parse(l):
        return (l.rest())
    def fadeblack_exec(ob1):
        music_exec(("stop", ""))
        img_exec(("black_screen", "d"))
        try:
            if float(ob1) > 0:
                renpy.pause(float(ob1))
        except:
            return
        return

    renpy.register_statement("fadeblack", parse=fadeblack_parse, execute=fadeblack_exec) #fadeblack - ???????????????? ?????????????????? ????????????

    def store_music():
        global storedMusic, currentMusic, currentMusicPriority
        storedMusic.insert(0, currentMusic)
        storedMusicPriority.insert(0, currentMusicPriority)
        return

    def restore_music():
        global storedMusic, currentMusic, currentMusicPriority
        currentMusic1 = False
        if len(storedMusic) > 0:
            currentMusic1 = storedMusic.pop(0)
            currentMusicPriority1 = storedMusicPriority.pop(0)
        if currentMusic1 == False:
#            renpy.music.stop(channel='music', fadeout=1.0)
            return
        if currentMusic1 == currentMusic:
            return
        currentMusic = currentMusic1
        currentMusicPriority = currentMusicPriority1
        checkPath = "Music/" + str(currentMusic) + ".ogg"
        if renpy.loadable(checkPath):
            renpy.music.play(checkPath, channel="music", loop=True, fadeout=1.0, fadein=1.0)
        return

    def clear_music_stack():
        storedMusic = []
        currentMusicPriority = 0
        return

    def music2_exec(ob1):
        global currentMusic2
        o, priority = ob1
        if o == "stop":
            currentMusic2 = False
            renpy.music.stop(channel='music2', fadeout=1.0)
            return
        try:
            musicName = renpy.eval(o)
        except:
            musicName = o
        if musicName == currentMusic2:
            return

        currentMusic2 = musicName
        checkPath = "Music/" + str(musicName) + ".ogg"
        if renpy.loadable(checkPath):
#            print "play music: " + checkPath
            renpy.music.play(checkPath, channel="music2", loop=True, fadeout=1.0, fadein=1.0)
        else:
            checkPath = "Sounds/" + str(musicName) + ".ogg"
            if renpy.loadable(checkPath):
                renpy.music.play(checkPath, channel="music2", loop=True, fadeout=1.0, fadein=1.0)
        return

    renpy.music.register_channel("music2", "music", True)
    renpy.register_statement("music2", parse=music_parse, execute=music2_exec) #music - ???????????????? ?????????????????????????????? ????????????

    def music3_exec(ob1):
        global currentMusic3
        o, priority = ob1
        if o == "stop":
            currentMusic3 = False
            renpy.music.stop(channel='music3', fadeout=1.0)
            return
        try:
            musicName = renpy.eval(o)
        except:
            musicName = o
        if musicName == currentMusic3:
            return

        currentMusic3 = musicName
        checkPath = "Music/" + str(musicName) + ".ogg"
        if renpy.loadable(checkPath):
#            print "play music: " + checkPath
            renpy.music.play(checkPath, channel="music3", loop=True, fadeout=1.0, fadein=1.0)
        else:
            checkPath = "Sounds/" + str(musicName) + ".ogg"
            if renpy.loadable(checkPath):
                renpy.music.play(checkPath, channel="music3", loop=True, fadeout=1.0, fadein=1.0)
        return

    renpy.music.register_channel("music3", "music", True)
    renpy.register_statement("music3", parse=music_parse, execute=music3_exec) #music - ???????????????? ?????????????????????????????? ????????????

    def video_parse(l):
        return l.simple_expression()
    def video_exec(o):
        try:
            videoName = get_filename(renpy.eval(o))
        except:
            videoName = get_filename(o)
        print(videoName)
        playing_video = Movie(play=videoName, channel="movie") #?????


    renpy.register_statement("video", parse=video_parse, execute=video_exec) #video - ???????????????? ?????????????????????????????? ??????????


    def custom_tag1(tag, argument, contents):
        return [
                (renpy.TEXT_TAG, u"color=#e8b131"),
            ] + contents + [
                (renpy.TEXT_TAG, u"/color"),
            ]
