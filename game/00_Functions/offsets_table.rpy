
define offsets_table = {
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
