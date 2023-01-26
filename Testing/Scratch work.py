import arcade

arcade.open_window(600, 600, "My Drawing")
arcade.set_background_color(arcade.csscolor.RED)

arcade.start_render()

arcade.draw_circle_filled(350, 250, 150, arcade.csscolor.YELLOW)


arcade.run()
