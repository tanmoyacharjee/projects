import pygame
import random
import WordList

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
green = (0,255,0)
yellow = (255,255,0)
red = (255 , 0 , 0)
WIDTH = 500
HEIGHT = 700
screen = pygame.display.set_mode([WIDTH , HEIGHT])
pygame.display.set_caption('Wordle')
huge_font = pygame.font.Font('freesansbold.ttf' , 56)
turns  = 0
letters = 0
turn_active = True
game_over = False
secretWord = WordList.words[random.randint(0, len(WordList.words) -1)]
board = [[" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "]]


def draw_board():
    global board
    for col in range(0,5):
        for row in range(0,6):
            pygame.draw.rect(screen , white , [col * 100 + 12 , row * 100 + 12, 75 , 75] ,3 , 5)
            piece_text = huge_font.render(board[row][col],True ,white)
            screen.blit(piece_text ,(col*100+30 , row*100+25))

def checkguess():
    global turns
    global board
    global secretWord
    for col in range(0,5):
        for row in range(0,6):
            if secretWord[col] == board[row][col] and turns>row:
                pygame.draw.rect(screen ,green ,[col * 100 + 12 ,row * 100 + 12, 75, 75], 0, 5)
            elif board[row][col] in secretWord and turns>row:
                pygame.draw.rect(screen , yellow , [col * 100 + 12 ,row * 100 + 12, 75, 75], 0, 5)

fps = 60
timer = pygame.time.Clock()

running = True

while running :
    timer.tick(fps)
    screen.fill(black)
    checkguess()
    draw_board()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE and letters > 0:
                board[turns][letters - 1] = ' '
                letters -= 1
            if event.key == pygame.K_SPACE and not game_over:
                turns += 1
                letters = 0
            if event.key == pygame.K_SPACE and game_over:
                turns = 0
                letters = -1
                game_over = False
                secretWord = WordList.words[random.randint(0, len(WordList.words) -1)]
                board = [[" ", " ", " ", " ", " "],
                        [" ", " ", " ", " ", " "],
                        [" ", " ", " ", " ", " "],
                        [" ", " ", " ", " ", " "],
                        [" ", " ", " ", " ", " "],
                        [" ", " ", " ", " ", " "]]

                
        if event.type == pygame.TEXTINPUT and turn_active and not game_over:
            entry = event.__getattribute__('text')
            board[turns][letters] = entry
            letters += 1
    for row in range(0,6):
        guess = board[row][0] + board[row][1] + board[row][2] + board[row][3] + board[row][4]
        if guess == secretWord and turns > row:
            game_over = True
            
            
    if letters == 5:
        turn_active = False
    if letters < 5:
        turn_active = True
    
    
        
    if turns == 6:
        game_over = True
        loser_text = huge_font.render((secretWord + ' is correct') , True , red)
        screen.blit(loser_text , (25 , 625))
    
    if game_over and turns < 6:
        winner_text = huge_font.render('Winner',True,green)
        screen.blit(winner_text , (150,625))
        
        
            
            
    pygame.display.flip()
pygame.quit()


