init python:
    class BlinkStrip(renpy.Displayable):
        def __init__(self, image, blinkAmount, preset, **kwargs):
            super(BlinkStrip, self).__init__(**kwargs)
            self.imageName = image
            self.image = Image(image)
            self.image_size = im.cache.get(self.image).get_size()
            self.preset = preset
            self.play = True

            width, height = self.image_size
            width = width/blinkAmount
            self.width, self.height = width, height

            args = [ ]
            args.append(Transform(self.image, crop=(0, 0, 0, 0)))

            for r in range(0, blinkAmount):
                x = r * width
                args.append(Transform(self.image, crop=(x, 0, width-1, height)))
            self.frames = args
            self.index = 0
            self.stage = 0
            self.firstBlink = True

        def render(self, width, height, st, at):
            global blinksListStopped
            if self.stage == 0:
                if self.index == 0:
                    # choose random preset part
                    self.preset_data = self.preset[renpy.random.randint(0,len(self.preset)-1)]

                if self.index == 0:
                    delay1 = float(self.preset_data[0])
                    if self.firstBlink == True:
                        self.firstBlink = False
                        delay1 = 1.0
                else:
                    delay1 = float(self.preset_data[1] / (len(self.frames)-1))
                t = self.frames[self.index]
                self.index = self.index + 1

                if self.index >= len(self.frames):
                    self.stage = 1
                    self.index = len(self.frames)-1
            else:
                if self.stage == 1:
                    if self.index == len(self.frames)-1:
                        delay1 = float(self.preset_data[2])
                    else:
                        delay1 = float(self.preset_data[3]/(len(self.frames)-1))
                    t = self.frames[self.index]
                    self.index = self.index - 1
                    if self.index == 0:
                        self.stage = 0
                        self.index = 0

            child_render = renpy.render(t, width, height, st, at)
            render = renpy.Render(self.width, self.height)
            render.blit(child_render, (0, 0))
            if self.imageName not in blinksListStopped:
#            blinksList.append(self)
#            if self.play == True:
                renpy.redraw(self, delay1)
            return render

        def stop(self):
            self.play = False
            return

        def visit(self):
            return [self.image]
