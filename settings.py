import button
# Pygame constants
WIDTH = 800
HEIGHT = 600

# Game constants
MAX_TIME = 5000

# Assets
PLAY_ICON_PATH = 'assets/images/play_button.png'
PAUSE_ICON_PATH = 'assets/images/pause_button.png'
PLAY_BUTTON = button.Button((255, 0, 0), (WIDTH // 2, HEIGHT // 2), 50, PLAY_ICON_PATH)

