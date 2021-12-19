with open ('highscore.txt') as file_object:
    highscore = file_object.read()

class Gamestats():
    """Track statistics for alien invasion."""

    def __init__(self, ai_settings, highscore):
        """Initialise statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Start alien invasion in an inactive state.
        self.game_active = False
        # High score should never be reset.
        self.high_score = highscore

    def reset_stats(self):
        """Initialise statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
