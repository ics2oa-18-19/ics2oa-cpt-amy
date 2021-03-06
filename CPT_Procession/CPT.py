import arcade
import random
import math

WIDTH = 640
HEIGHT = 480
PLAYER_RADIUS = 15
BLACK_CLOUD_RADIUS = 15
RAINBOW_RADIUS = 15

current_screen = "menu"

cloud_x_positions = []
cloud_y_positions = []
black_cloud_x_position = []
black_cloud_y_position = []
rainbow_x_position = []
rainbow_y_position = []
player_y_position = HEIGHT/2
player_x_position = 30
point = 0
rainbow_point = 100
updated_points = ""
speed = 5
updated_speed = ""

up_pressed = False
down_pressed = False

for cloud in range(100):
    x = random.randrange(0, WIDTH)
    y = random.randrange(0, HEIGHT)
    cloud_x_positions.append(x)
    cloud_y_positions.append(y)

for black_cloud in range(10):
    x = random.randrange(0, WIDTH)
    y = random.randrange(0, HEIGHT)
    black_cloud_x_position.append(x)
    black_cloud_y_position.append(y)

for rainbow in range(1):
    x = random.randrange(0, WIDTH)
    y = random.randrange(0, HEIGHT)
    rainbow_x_position.append(x)
    rainbow_y_position.append(y)

def update(delta_time):
    global up_pressed, down_pressed, player_y_position, point, current_screen
    global updated_points, speed, updated_speed, black_cloud

    if current_screen == "play":

        for index in range(len(cloud_x_positions)):
            cloud_x_positions[index] -= speed
            if cloud_x_positions[index] < 0:
                cloud_y_positions[index] = random.randrange(0, HEIGHT)
                cloud_x_positions[index] = random.randrange(WIDTH, WIDTH * 2)

        for index in range(len(black_cloud_x_position)):
            black_cloud_x_position[index] -= speed
            if black_cloud_x_position[index] < 0:
                black_cloud_y_position[index] = random.randrange(0, HEIGHT)
                black_cloud_x_position[index] = random.randrange(WIDTH, WIDTH * 2)

        for index in range(len(rainbow_x_position)):
            rainbow_x_position[index] -= speed
            if rainbow_x_position[index] < 0:
                rainbow_y_position[index] = random.randrange(0, HEIGHT)
                rainbow_x_position[index] = random.randrange(WIDTH, WIDTH * 2)

        if player_y_position > 480:
            player_y_position = 460
        if player_y_position < 0 :
            player_y_position = 20

        if up_pressed == True:
            player_y_position += 17
            point += 1
            updated_points = point
            speed += 0.1
            updated_speed = speed

        if down_pressed == True:
            player_y_position -= 17
            point += 1
            updated_points = point
            speed += 0.1
            updated_speed = speed

        # loop through blackcloud list using zip()
        for x, y in zip(black_cloud_x_position, black_cloud_y_position):
            a = player_x_position - x
            b = player_y_position - y
            dist = math.sqrt(a**2 + b**2)
            if dist < PLAYER_RADIUS + BLACK_CLOUD_RADIUS:
                current_screen = "game_over"
        
        for x, y in zip (rainbow_x_position, rainbow_y_position):
            c = player_x_position - x
            d = player_y_position - y
            rainbow_distance = math.sqrt(c**2 + d**2)
            if rainbow_distance < PLAYER_RADIUS + RAINBOW_RADIUS:
                point += rainbow_point
    elif current_screen == "game_over":
        global up_pressed, down_pressed, player_y_position, point, current_screen
        global updated_points, speed, updated_speed, black_cloud, cloud_x_positions, cloud_y_positions, black_cloud_x_position, black_cloud_y_position, rainbow_x_position, rainbow_y_position

        cloud_x_positions = []
        cloud_y_positions = []
        black_cloud_x_position = []
        black_cloud_y_position = []
        rainbow_x_position = []
        rainbow_y_position = []
        player_y_position = HEIGHT / 2
        player_x_position = 30
        point = 0
        rainbow_point = 100
        updated_points = ""
        speed = 5
        updated_speed = ""
    elif current_screen == "menu":
        for index in range(len(cloud_x_positions)):
            cloud_x_positions[index] -= 10
            if cloud_x_positions[index] < 0:
                cloud_y_positions[index] = random.randrange(0, HEIGHT)
                cloud_x_positions[index] = random.randrange(WIDTH, WIDTH * 2)
    elif current_screen == "instructions":
        for index in range(len(cloud_x_positions)):
            cloud_x_positions[index] -= 10
            if cloud_x_positions[index] < 0:
                cloud_y_positions[index] = random.randrange(0, HEIGHT)
                cloud_x_positions[index] = random.randrange(WIDTH, WIDTH*2)


def on_draw():
    arcade.start_render()
    if current_screen == "menu":
        draw_menu()
    elif current_screen == "instructions":
        draw_instructions()
    elif current_screen == "play":
        draw_play()
    elif current_screen == "game_over":
        draw_gameover()

def on_key_press(key, modifiers):
    global current_screen
    if current_screen == "menu":
        if key == arcade.key.I:
            current_screen = "instructions"
        elif key == arcade.key.P:
            current_screen = "play"
    elif current_screen == "instructions":
        if key == arcade.key.ESCAPE:
            current_screen = "menu"
    elif current_screen == "play":
        global up_pressed, down_pressed
        if key == arcade.key.W:
            up_pressed = True
        if key == arcade.key.S:
            down_pressed = True
        elif key == arcade.key.ESCAPE:
            current_screen = "menu"
    elif current_screen == "game_over":
        if key == arcade.key.ESCAPE:
            current_screen = "menu"

def on_key_release(key, modifiers):
    global current_screen, up_pressed, down_pressed
    if current_screen == "play":
        if key == arcade.key.W:
            up_pressed = False
        if key == arcade.key.S:
            down_pressed = False

def on_mouse_press(x, y, button, modifiers):
    pass

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

def draw_menu():
    arcade.draw_text("UNICORN RUN", WIDTH/2, HEIGHT/2,
                     arcade.color.NAVY_BLUE, font_size=30)
    arcade.draw_text("Press I for Instructions", WIDTH/2, HEIGHT/2-60,
                     arcade.color.COOL_BLACK, font_size=20)
    arcade.draw_text("Press P to Play", WIDTH/2, HEIGHT/2-90,
                     arcade.color.COOL_BLACK, font_size=20)
    arcade.set_background_color(arcade.color.LIGHT_BLUE)

    for x, y in zip(cloud_x_positions, cloud_y_positions):
        arcade.draw_circle_filled(x, y, 5, arcade.color.WHITE)

def draw_instructions():
    arcade.set_background_color(arcade.color.LIGHT_PINK)
    global player_x_position, player_y_position
    arcade.draw_text("Instructions", 20, 400,
                     arcade.color.BLACK, font_size=30)
    arcade.draw_text("""
           1. Avoid touching the black clouds by moving the 
           unicorn up and down.
           2. Press W to go up, S to go down
           3. For every movement the unicorn makes, 1 point is given. 
           4. Eat the green clouds for a ramdom amount of bonus points!
           5. The clouds will move faster as the time goes by """, 0, HEIGHT / 2, arcade.color.BLACK, font_size=15)
    arcade.draw_text("ESC to go back", 20, 20,
                     arcade.color.BLACK, font_size=20)

    for x, y in zip(cloud_x_positions, cloud_y_positions):
        arcade.draw_circle_filled(x, y, 5, arcade.color.WHITE)



def draw_play():
    arcade.set_background_color(arcade.color.LIGHT_BLUE)
    global black_cloud
    for x, y in zip(cloud_x_positions, cloud_y_positions):
        arcade.draw_circle_filled(x, y, 15, arcade.color.WHITE)
    for x, y in zip(black_cloud_x_position, black_cloud_y_position):
        black_cloud = arcade.draw_circle_filled(x, y, BLACK_CLOUD_RADIUS, arcade.color.BLACK)
    for x, y in zip(rainbow_x_position, rainbow_y_position):
        arcade.draw_circle_filled(x, y, 15, arcade.color.SPRING_GREEN)

    arcade.draw_circle_filled(player_x_position, player_y_position, PLAYER_RADIUS, arcade.color.CORAL_PINK)

    arcade.draw_text(f"{updated_points}", 10, 440, arcade.color.COOL_BLACK, font_size= 20)

def draw_gameover():
    arcade.set_background_color(arcade.color.BLACK)
    arcade. draw_text("""GAME 
                         OVER""", 20, HEIGHT/2, arcade.color.WHITE, font_size= 30)
    arcade.draw_text("ESC to go back", 20, 20,
                     arcade.color.WHITE, font_size=20)


if __name__ == '__main__':
    setup()
