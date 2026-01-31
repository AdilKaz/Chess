import pygame
import os

# -------- CONFIG --------
WIDTH,HEIGHT=800,800
ROWS,COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

LIGHT = (230, 230, 232)
DARK = (70, 92, 106)

# -------- INIT --------
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

# Safe way to load images
BASE_DIR = os.path.dirname(__file__)
icon_path = os.path.join(BASE_DIR, "images", "chess_icon.png")
pygame.display.set_icon(pygame.image.load(icon_path))

clock = pygame.time.Clock()

# -------- FUNCTIONS --------
def draw_board(win):
    for row in range(ROWS):
        for col in range(COLS):
            color = LIGHT if (row + col) % 2 == 0 else DARK
            pygame.draw.rect(win, color, (col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def load_piece(filename):
    path = os.path.join(BASE_DIR, "images", filename)
    image = pygame.image.load(path)
    return pygame.transform.scale(image, (SQUARE_SIZE-10, SQUARE_SIZE-10))

# -------- LOAD PIECES --------
white_pawn = load_piece("white_pawn.png")
white_knight = load_piece("white_knight.png")
white_bishop = load_piece("white_bishop.png")
white_rook = load_piece("white_rook.png")
white_queen = load_piece("white_queen.png")
white_king = load_piece("white_king.png")

black_pawn = load_piece("black_pawn.png")
black_knight = load_piece("black_knight.png")
black_bishop = load_piece("black_bishop.png")
black_rook = load_piece("black_rook.png")
black_queen = load_piece("black_queen.png")
black_king = load_piece("black_king.png")
# Example position: row 6, col 0
pieces = [(white_pawn, 6, 0),(white_pawn, 6, 1),(white_pawn, 6, 2),(white_pawn, 6, 3),(white_pawn, 6, 4),(white_pawn, 6, 5),(white_pawn, 6, 6),(white_pawn, 6, 7),
          (black_pawn, 1, 0),(black_pawn, 1, 1),(black_pawn, 1, 2),(black_pawn, 1, 3),(black_pawn, 1, 4),(black_pawn, 1, 5),(black_pawn, 1, 6),(black_pawn, 1, 7),
          (white_knight, 7, 1),(white_knight, 7, 6),
          (black_knight, 0, 1),(black_knight, 0, 6),
          (white_bishop, 7, 2),(white_bishop, 7, 5),
          (black_bishop, 0, 2),(black_bishop, 0, 5),
          (white_rook, 7, 0),(white_rook, 7, 7),
          (black_rook, 0, 0),(black_rook, 0, 7),
          (white_queen, 7, 3),
          (black_queen, 0, 3),
          (white_king, 7, 4),
          (black_king, 0, 4)]

# -------- GAME LOOP --------
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_board(screen)

    # Draw all pieces
    for piece, row, col in pieces:
        screen.blit(piece, (col * SQUARE_SIZE+5, row * SQUARE_SIZE))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
