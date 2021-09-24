
define offsets_table = {
    "screen_down_arrow":(998,420,1079,1499),
    "screen_down_arrow_short1":(998,420,1079,1499),
    "screen_left_arrow":(0,0,1079,151),
    "screen_left_arrow_tight":(0,0,1079,106),
    "screen_right_arrow":(0,1768,1079,1919),
    "screen_right_arrow_tight":(0,1813,1079,1919),
}

init python:
    global offsets_table
    def get_canvas_offset(in_filename):
        in_filename = in_filename.lower()
        if offsets_table.has_key(in_filename) == False or in_filename == False:
            return False
        src_canvas_offsets = offsets_table[in_filename]
        canvas_offsets = [int(round(float(src_canvas_offsets[0]) / 1080.0 * config.screen_height,2)), int(round(float(src_canvas_offsets[1]) / 1920.0 * config.screen_width,2)), int(math.ceil(round(float(src_canvas_offsets[2]) / 1080.0 * config.screen_height,2))), int(math.ceil(round(float(src_canvas_offsets[3]) / 1920.0 * config.screen_width,2)))]
        return canvas_offsets

    def get_overlay_canvas_offset(in_filename):
        in_filename = in_filename.lower()
        if overlays_offsets_table.has_key(in_filename) == False or in_filename == False:
            if overlays_offsets_table.has_key("img_" + in_filename):
                return overlays_offsets_table["img_" + in_filename]
            return False
        return overlays_offsets_table[in_filename]
