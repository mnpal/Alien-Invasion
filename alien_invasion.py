import pygame
import pygame.mixer
import pygame.sprite as sprite
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from button import Button
import game_functions as gf
from game_stats import GameStats
from scorecard import Scoreboard


def run_game():

    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()


    background = pygame.image.load('417403_980.jpg')
    background_size = background.get_size()
    background_rect = background.get_rect()
    screen = pygame.display.set_mode(background_size)
    ai_settings.screen_width, ai_settings.screen_height = background_size

    x = 0
    y = 0

    x1 = 0
    y1 = -ai_settings.screen_height


    #screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #shooting_sound = pygame.mixer.Sound("music/Gun+1.wav")
    pygame.mixer.music.load("music/Action_Time.mp3")
    pygame.mixer.music.play(-1)

    # Make the play button
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)

    # Create a scoreboard.
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a ship.
    ship = Ship(ai_settings, screen)

    # Make a group to store bullets in.
    bullets = Group()

    # Make a group of aliens.
    aliens = Group()

    # Create a fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)

        y1 += 5
        y += 5
        screen.blit(background, (0, y))
        screen.blit(background, (0, y1))
        if y>ai_settings.screen_height:
            y = -ai_settings.screen_height
        if y1>ai_settings.screen_height:
            y1 = -ai_settings.screen_height

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()
