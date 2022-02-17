"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the dimensions (width and height)
arcade.open_window(600, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.color.LIGHT_BLUE)

# Get ready to draw
arcade.start_render()

# (The drawing code will go here.)
#Draw the left rectangle
arcade.draw_lrtb_rectangle_filled(0, 150, 280, 0, arcade.csscolor.DARK_GREEN)
#Draw the middle rectangle
arcade.draw_lrtb_rectangle_filled(150, 450, 280, 260,arcade.csscolor.BLACK)
#Draw the right rectangle
arcade.draw_lrtb_rectangle_filled(450, 600, 280, 0, arcade.csscolor.DARK_GREEN)
#Draw the rear wheel
arcade.draw_circle_filled(350, 310, 30, arcade.csscolor.BLACK)
#Draw the front wheel
arcade.draw_circle_filled(180, 310, 30, arcade.csscolor.BLACK)
#Base of the vehicle
arcade.draw_lrtb_rectangle_filled(180, 350, 310, 305,arcade.csscolor.RED)
#Handlebar of the vehicle
arcade.draw_lrtb_rectangle_filled(180, 190, 280, 260,arcade.csscolor.RED)






# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()