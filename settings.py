import button
# Pygame constants
WIDTH = 800
HEIGHT = 600

# Game constants
MAX_TIME = 5000

# Assets
PLAY_ICON_PATH = 'assets/images/play_button.png'
PAUSE_ICON_PATH = 'assets/images/pause_button.png'
FONT_COLOR = (255, 255, 255)
HIGHLIGHT_COLOR = (255, 0, 0)
PLAY_BUTTON = button.Button(HIGHLIGHT_COLOR, (3*WIDTH // 4, HEIGHT // 4), 20, PLAY_ICON_PATH)

