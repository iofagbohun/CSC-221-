import random
import arcade

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
SPRITE_SCALING_LASER = 0.8
AlIEN_COUNT = 25
ALIEN_COUNT2 = 15
METEOR_COUNT = 8

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BULLET_SPEED = 5

class Meteor_moving(arcade.Sprite):
    def __init__(self, file, scale):
        super().__init__(file, scale)

    def update(self):
        self.center_y -= 1
        if self.center_y == 0:
            self.center_y = SCREEN_HEIGHT

class Alien_sprite(arcade.Sprite):
    def __init__(self, file, scale):
        super().__init__(file, scale)

    def update(self):
        self.center_y -= 1
        if self.center_y == 0:
            self.center_y = SCREEN_HEIGHT

class Alien2_ship2(arcade.Sprite):
    def __init__(self, file, scale):
        super().__init__(file, scale)

    def update(self):
        self.center_y -= 1
        if self.center_y == 0:
            self.center_y = SCREEN_HEIGHT

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Space Invader")

        # Variables that will hold sprite lists
        self.player_list = None
        self.alien_list = None
        self.bullet_list = None
        self.meteor_list = None
        self.alien_ship2_list = None
        self.game_over = False


        # Set up the player info
        self.player_sprite = None
        self.score = 0

        self.laser_sound = arcade.load_sound("laserLarge_003.ogg")

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):

        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.alien_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.meteor_list = arcade.SpriteList()
        self.alien_ship2_list = arcade.SpriteList()

        # Set up the player
        self.score = 0

        # All images are from kenney.nl
        self.player_sprite = arcade.Sprite("playerShip1_blue.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 70
        self.player_list.append(self.player_sprite)

        # creating meteor # image from kenny.nl
        # create instance of METEORS
        for i in range(METEOR_COUNT):
            meteor = Meteor_moving("meteorBrown_big1.png", scale=0.5)

            meteor.center_x = random.randrange(SCREEN_WIDTH)
            meteor.center_y = random.randrange(SCREEN_HEIGHT)

            self.meteor_list.append(meteor)

        for i in range(ALIEN_COUNT2):
            alien_ship2 = Alien2_ship2("shipYellow_manned.png", scale=0.4)

            alien_ship2.center_x = random.randrange(SCREEN_WIDTH)
            alien_ship2.center_y = random.randrange(SCREEN_HEIGHT)


            self.alien_ship2_list.append(alien_ship2)



        # Create the aliens
        # Create the aliens instance
        # alien image from kenney.nl
        for i in range(AlIEN_COUNT):

            alien_ship = Alien_sprite("shipBlue_manned.png", SPRITE_SCALING_COIN)

            # Position the aliens
            alien_ship.center_x = random.randrange(SCREEN_WIDTH)
            alien_ship.center_y = random.randrange(120, SCREEN_HEIGHT)

            # Add the aliens to the lists
            self.alien_list.append(alien_ship)

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.alien_list.draw()
        self.bullet_list.draw()
        self.player_list.draw()
        self.meteor_list.draw()
        self.alien_ship2_list.draw()

        # Render the text
        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.WHITE, 14)

        if len(self.alien_list) == 0:
            arcade.draw_text("YOU WIN", 200, 300, arcade.color.BLUE, 75)
        elif self.game_over:
            arcade.draw_text("GAME OVER", 100, 300, arcade.color.RED, 75)


    def on_mouse_motion(self, x, y, dx, dy):
        self.player_sprite.center_x = x

    def on_mouse_press(self, x, y, button, modifiers):
        # Create a bullet
        bullet = arcade.Sprite("laserBlue01.png", SPRITE_SCALING_LASER)

        arcade.play_sound(self.laser_sound)

        # The image points to the right, and we want it to point up. So
        # rotate it.
        bullet.angle = 360

        # Position the bullet
        bullet.center_x = self.player_sprite.center_x
        bullet.bottom = self.player_sprite.top
        bullet.change_y = BULLET_SPEED

        # Add the bullet to the appropriate lists
        self.bullet_list.append(bullet)

    def update(self, delta_time):

        if not self.game_over:

            # Call update on all sprites
            self.alien_list.update()
            self.bullet_list.update()
            self.meteor_list.update()
            self.alien_ship2_list.update()

            # Loop through each bullet
            for bullet in self.bullet_list:

                # Check the bullet to see if it hit a alien
                hit_list = arcade.check_for_collision_with_list(bullet, self.alien_list)

                # If it did, get rid of the bullet
                if len(hit_list) > 0:
                    bullet.remove_from_sprite_lists()

                # For every alien we hit, add to 1 to the score
                for alien in hit_list:
                    alien.remove_from_sprite_lists()
                    self.score += 1
                    arcade.play_sound(self.laser_sound)

                # If the bullet flies off-screen, remove it.
                if bullet.bottom > SCREEN_HEIGHT:
                    bullet.remove_from_sprite_lists()

        # when collide with meteor, game over
            meteor_sprite_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.meteor_list)
            if len(meteor_sprite_hit_list) > 0:
                self.game_over = True







def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()