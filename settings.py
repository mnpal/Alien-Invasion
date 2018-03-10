class Settings():
    """A class to store all settings for Alien Inasion."""
    def __init__(self):
        """Initialize game's static settings."""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (221, 200, 250)

        # Ship settings.
        self.ships_limit = 3

        # Bullet settings.
        self.bullet_width = 15
        self.bullet_height = 15
        self.bullet_color = (220, 150, 20)
        self.bullets_allowed = 6

        # Alien settings.
        self.fleet_drop_speed = 25

        # How quickly the game speeds up.
        self.speedup_scale = 1.1
        # How quickly the alien point values increase.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.3
        self.bullet_speed_factor = 2
        self.alien_speed_factor = 1.2

        # Fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
