# TODO: Rust webassembly?
from math import cos, pi as π, sin
import arcade

class Body(object):
    def __init__(self):
        pass

class Planet(object):
    def __init__(self) -> None:
        super().__init__()
        self.centre = SCREEN_WIDTH / 2 + SCREEN_HEIGHT / 2 * 1j # m
        self.radius = 110 # m
        self.gravity = -40.0
        self.colour =  arcade.color.ANDROID_GREEN
        self.mass = 10 # kg
    
    def cartesian_position(self):
        return self.centre.real, self.centre.imag

class Actor(object):
    def __init__(self, size: complex, colour: arcade.Color):
        self.position = 90 * π/180.0
        self.velocity = 0.0
        self.jump_strength = 40.0
        self.jump_velocity = 0.0
        self.height_above_ground = 0.0
        self.walking_speed = 21.0
        self.size = size
        self.colour = colour

    def tick(self, planet: Planet, dt: float):
        self.position += self.velocity * dt
        self.height_above_ground = max(self.height_above_ground + self.jump_velocity * dt, 0.0)
        self.jump_velocity = self.jump_velocity + planet.gravity * dt

    def cartesian_position(self, planet: Planet):
        z = planet.centre + (planet.radius + self.size.imag * 0.5 + self.height_above_ground) * (cos(self.position) + sin(self.position)*1j)
        return z.real, z.imag

class World(object):
    def __init__(self):
        self.player = Actor()
    
    def tick(self, planet: Planet, dt: float):
        self.player.tick(planet, dt)

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Little Planet"

class LittlePlanet(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

        self.players = (
            Actor(20.0+30.0j, arcade.color.ORANGE_PEEL),
            Actor(12.0+18.0j, arcade.color.BLUE_SAPPHIRE))
        self.planet = Planet()

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        pass

    def on_draw(self):
        """Render the screen."""

        arcade.start_render()
        # Code to draw the screen goes here
        arcade.draw_text("Little Planet", 12, 12, arcade.color.BLACK, 14)
        arcade.draw_circle_filled(*self.planet.cartesian_position(), self.planet.radius, self.planet.colour, 100)
        
        for player in self.players:
            arcade.draw_rectangle_filled(
                *player.cartesian_position(self.planet),
                player.size.real, player.size.imag,
                player.colour,
                (-player.position + π/2) * 180/π
            )

    def on_update(self, delta_time: float):
        for player in self.players:
            player.tick(self.planet, delta_time)
        return super().on_update(delta_time)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.A:
            self.players[0].velocity = self.players[0].walking_speed * π/180.0
        elif symbol == arcade.key.D:
            self.players[0].velocity = -self.players[0].walking_speed * π/180.0
        elif symbol == arcade.key.SPACE:
            self.players[0].jump_velocity = self.players[0].jump_strength
        elif symbol == arcade.key.LEFT:
            self.players[1].velocity = self.players[1].walking_speed * π/180.0
        elif symbol == arcade.key.RIGHT:
            self.players[1].velocity = -self.players[1].walking_speed * π/180.0
        elif symbol == arcade.key.UP:
            self.players[1].jump_velocity = self.players[1].jump_strength
        return super().on_key_press(symbol, modifiers)

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.A:
            self.players[0].velocity = 0
        elif symbol == arcade.key.D:
            self.players[0].velocity = 0
        if symbol == arcade.key.LEFT:
            self.players[1].velocity = 0
        elif symbol == arcade.key.RIGHT:
            self.players[1].velocity = 0
        return super().on_key_release(symbol, modifiers)

def main():
    """Main method"""
    window = LittlePlanet()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()