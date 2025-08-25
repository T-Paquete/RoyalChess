# Board dimensions
COLS = 12
ROWS = 10 # 8 rows for the chess game + 2 extra rows
SQSIZE = 64

# Screen dimensions
MENU_WIDTH = 180
BOARD_PIXEL_WIDTH = COLS * SQSIZE
WIDTH = BOARD_PIXEL_WIDTH + MENU_WIDTH
HEIGHT = SQSIZE * ROWS

# Board colors
# Board square colors
LIGHT_COLOR = (234, 235, 200)    # Light squares on the board
DARK_COLOR = (119, 154, 88)      # Dark squares on the board

# Highlight and piece colors
WHITE = (255, 255, 255)          # White pieces or highlights
LIGHT_RED = (255, 102, 102, 120)  # Light red highlight (e.g., move indicator)
DARK_RED = (255, 102, 102, 120)   # Lighter red highlight (e.g., capture indicator)

