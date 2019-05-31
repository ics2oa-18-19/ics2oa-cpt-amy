import arcade
import random

WIDTH = 640
HEIGHT = 480

cloud_x_positions = []
cloud_y_positions = []
black_cloud_x_position = []
black_cloud_y_position = []
player_y_position = HEIGHT/2
player_x_position = WIDTH/2

up_pressed = False
down_pressed = False
left_pressed = False
right_pressed = False

for cloud in range(100):
    x = random.randrange(0, WIDTH)
    y = random.randrange(0, HEIGHT)
    cloud_x_positions.append(x)
    cloud_y_positions.append(y)

for black_cloud in range (10):
    x = random.randrange(0, WIDTH)
    y = random.randrange(0, HEIGHT)
    black_cloud_x_position.append(x)
    black_cloud_y_position.append(y)

def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.LIGHT_BLUE)
    arcade.schedule(update, 1/60)



    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


def update(delta_time):
    global up_pressed, player_y_position
    for index in range(len(cloud_x_positions)):
        # modify list using square-brakets and the index
        cloud_x_positions[index] -= 10
        # read list values with square braket notation
        # eg. my_list 3
        if cloud_x_positions[index] < 0:
            # modify list values using square braket notation
            cloud_y_positions[index] = random.randrange(0, HEIGHT)
            cloud_x_positions[index] = random.randrange(WIDTH, WIDTH*2)
    for index in range(len(black_cloud_x_position)):
        black_cloud_x_position[index] -= 10
        if black_cloud_x_position[index] < 0:
            black_cloud_y_position[index] = random.randrange(0,HEIGHT)
            black_cloud_x_position[index] = random.randrange(WIDTH, WIDTH*2)
        if up_pressed:
            player_y_position += 5
    

def on_draw():
    global player_x_position, player_y_position
    arcade.start_render()
    # Draw in here...
    for x, y in zip (cloud_x_positions, cloud_y_positions):
        arcade.draw_circle_filled(x, y, 15,arcade.color.WHITE)
    for x, y in zip (black_cloud_x_position, black_cloud_y_position):
        arcade.draw_circle_filled(x, y, 15, arcade.color.BLACK)

    arcade.draw_circle_filled(player_x_position, player_x_position, 10, arcade.color.CORAL_PINK)


def on_key_press(key, modifiers):
    global up_pressed
    if key == arcade.key.W:
        up_pressed = True

def on_key_release(key, modiwfiers):
    global up_pressed
    if key == arcade.key.W:
        up_pressed = False

def on_mouse_press(x, y, button, modifiers):
    pass


if __name__ == '__main__':
    setup()
