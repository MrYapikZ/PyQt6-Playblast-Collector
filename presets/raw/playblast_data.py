import bpy

scenes = bpy.data.scenes["Scene"]

scenes.render.use_simplify = True
scenes.render.simplify_subdivision = 1

#Format playblast
scenes.render.resolution_x = 1920
scenes.render.resolution_y = 1080
scenes.render.resolution_percentage = 80
scenes.render.use_border = False
scenes.render.fps = 25
scenes.render.image_settings.file_format = "FFMPEG"
scenes.render.ffmpeg.format = "QUICKTIME"
scenes.render.ffmpeg.audio_codec = "MP3"
# scenes.render.filepath = "path output shot"

#Metadata
# scenes.render.metadata_input = "SCENE"
scenes.render.use_stamp_date = True
scenes.render.use_stamp_time = True
scenes.render.use_stamp_render_time = False
scenes.render.use_stamp_frame = True
scenes.render.use_stamp_frame_range = False
scenes.render.use_stamp_memory = False
scenes.render.use_stamp_hostname = False
scenes.render.use_stamp_camera = False
scenes.render.use_stamp_lens = True
scenes.render.use_stamp_scene = False
scenes.render.use_stamp_marker = False
scenes.render.use_stamp_filename = True
scenes.render.use_stamp_sequencer_strip = False
scenes.render.use_compositing = False
scenes.render.use_sequencer = False

#Note
scenes.render.use_stamp_note = True
# scenes.render.stamp_note_text = "Nama pc"

#Burn Into Image
scenes.render.use_stamp = True
scenes.render.stamp_font_size = 15
scenes.render.stamp_foreground = (0.799238, 0.715663, 0, 1)
scenes.render.stamp_background = (0, 0, 0, 0.5)
