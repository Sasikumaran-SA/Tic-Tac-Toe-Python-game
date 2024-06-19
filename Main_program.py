import pygame


# 'Board_Template.png' and 'FREESCPT.ttf' are the necessary file
# Follow the instruction in the screen


pygame.init()

WIDTH, HEIGHT = 600, 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))                                                     # Setting pygame window
pygame.display.set_caption("TIC TAC TOE")

font = 'FREESCPT.ttf'                                                                                 # Font for output text

def check_winner(x_o_list,x_o,position):                                                              # To check the winning possibility

    li = ['123','456','789','147','258','369','159','357']
    l1 = []

    for i in range(1,10):
        if position == str(i):
            for seq in li:
                if position in seq:
                    l2=[]
                    for pos in seq:
                        l2.append(x_o_list[int(pos)-1])
                    l1.append(set(l2))

    for set_ in l1:
        if len(set_) == 1:
            for ele in set_:
                if ele == x_o:
                    return True
                else:
                    return False


def start():                                                                                          # Starting page of screen

    font1 = pygame.font.Font(font, 70)
    font2 = pygame.font.Font(font, 30)
    font3 = pygame.font.Font(font, 50)

    while True:

        screen.fill((255,165,0))

        text1 = font1.render("Tic Tac Toe", True, (255,0,120))
        screen.blit(text1, (160, 10))

        text2 = font2.render("Player 1 : X", True, (220,0,0))
        screen.blit(text2, (460,100))
        text3 = font2.render("Player 2 : O", True, (0,0,255))
        screen.blit(text3, (460,150))

        text2 = font3.render("Choose the match mode :", True, (0,0,0))
        screen.blit(text2, (20,150))
        text3 = font2.render("Best of 1", True, (0,0,0))
        text4 = font2.render("Best of 3", True, (0,0,0))
        text5 = font2.render("Best of 5", True, (0,0,0))
        screen.blit(text3, (150,200))
        screen.blit(text4, (150,240))
        screen.blit(text5, (150,280))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            
            if event.type == pygame.KEYDOWN:                                                          # For choosing match mode
                if event.key == pygame.K_KP1:
                    return 1
                if event.key == pygame.K_KP3:
                    return 3
                if event.key == pygame.K_KP5:
                    return 5

        pygame.display.update()

def Game_page(winner_list, no_of_match, match_no):                                                    # For game screen

    font1 = pygame.font.Font(font, 70)
    font2 = pygame.font.Font(font, 30)
    font3 = pygame.font.Font(font, 100)
    font4 = pygame.font.Font(font, 130)

    for _ in range(5000):

        screen.fill((255,165,0))

        text1 = font1.render("Tic Tac Toe", True, (255,0,120))
        screen.blit(text1, (160, 10))

        text2 = font2.render("Player 1 : X", True, (220,0,0))
        screen.blit(text2, (460,100))
        text3 = font2.render("Player 2 : O", True, (0,0,255))
        screen.blit(text3, (460,150))

        text4 = font3.render("Let's START!",True, (100,90,200))                                       # Screen before begining each match
        screen.blit(text4, (20,200))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0

        pygame.display.update()

    board_dic = {1:[False,'_',(35,350),pygame.K_KP1],                                                 # Game board values
                 2:[False,'_',(170,350),pygame.K_KP2],
                 3:[False,'_',(300,350),pygame.K_KP3],
                 4:[False,'_',(35,225),pygame.K_KP4],
                 5:[False,'_',(170,225),pygame.K_KP5],
                 6:[False,'_',(300,225),pygame.K_KP6],
                 7:[False,'_',(35,100),pygame.K_KP7],
                 8:[False,'_',(170,100),pygame.K_KP8],
                 9:[False,'_',(300,100),pygame.K_KP9]}
    
    circle_position_list = [(520,15),
                            (490,15),
                            (550,15),
                            (460,15),
                            (580,15)]
    
    if no_of_match == 1:
        circle_order = '0'
    elif no_of_match == 3:
        circle_order = '102'
    elif no_of_match == 5:
        circle_order = '31024'

    position_changer = 0

    tic_tac_toe_list = ['','','','','','','','','']

    last_wait_screen_li = [False, 300]                                                                # To increase the last screen time

    while True:
        
        screen.fill((255,165,0))

        text1 = font1.render("Tic Tac Toe", True, (255,0,120))
        screen.blit(text1, (160, 10))

        text2 = font2.render("Player 1 : X", True, (220,0,0))
        screen.blit(text2, (460,100))
        text3 = font2.render("Player 2 : O", True, (0,0,255))
        screen.blit(text3, (460,150))

        pygame.draw.rect(screen, (140,0,0), pygame.Rect(10,100,390,390),7)                            # To display board

        pygame.draw.line(screen, (140,0,0), (10,230),(399,230), 3)
        pygame.draw.line(screen, (140,0,0), (10,360),(399,360), 3)
        pygame.draw.line(screen, (140,0,0), (140,100),(140,489), 3)
        pygame.draw.line(screen, (140,0,0), (270,100),(270,489), 3)

        for _ in range(len(winner_list)):                                                             # To show the winning person in each match
            position = circle_position_list[_]
            pygame.draw.circle(screen, (0,0,0), position, 10, 2)
            if winner_list[_] != '':
                order = circle_order[_]
                position_ = circle_position_list[int(order)]
                if winner_list[_] == 'x':
                    pygame.draw.circle(screen, (220,0,0), position_, 8)
                elif winner_list[_] == 'o':
                    pygame.draw.circle(screen, (0,0,255), position_, 8)
                elif winner_list[_] == 'x_o':
                    pygame.draw.circle(screen, (220,0,255), position_, 8)


        board = pygame.transform.scale(pygame.image.load("Board_Template.png"), (380,390))
        boardRect = board.get_rect()
        boardRect.x, boardRect.y = 10,100
        screen.blit(board,boardRect)

        text4 = font2.render("Replay - Enter 'r'", True, (0,0,0))
        screen.blit(text4, (447,420))
        text5 = font2.render("Restart - Enter 'x'", True, (0,0,0))
        screen.blit(text5, (440,450))

        text6 = font2.render("Use NumberPad to Play", True, (0,0,0))
        screen.blit(text6, (405,350))

        x = font4.render('X', True, (220,0,0))                                                        # To present X or O in screen board
        o = font4.render('O', True, (0,0,255))
        for i in range(1,10):    
            if board_dic[i][0]:
                if board_dic[i][1] == 'x':
                    screen.blit(x, board_dic[i][2])
                elif board_dic[i][1] == 'o':
                    screen.blit(o, board_dic[i][2])
        
        if position_changer%2 == 0:                                                                   # To change the participate each time
            x_o_str = 'x'
            pygame.draw.circle(screen, (0,255,0), (440,115), 8)
        else:
            x_o_str = 'o'
            pygame.draw.circle(screen, (0,255,0), (440,165), 8)

        for event in pygame.event.get():                                                              # To get the input from keyboard
            if event.type == pygame.QUIT:
                return 0

            if event.type == pygame.KEYDOWN:
                for position in range(1,10):
                    if not board_dic[position][0] and not last_wait_screen_li[0]:
                        if event.key == board_dic[position][3]:                                       # To the get input for the number in the board
                            tic_tac_toe_list[position-1] = x_o_str
                            board_dic[position][0] = True
                            board_dic[position][1] = x_o_str
                            position_changer += 1
                            if check_winner(tic_tac_toe_list,x_o_str,str(position)):
                                winner_list[match_no] = x_o_str
                                last_wait_screen_li[0] = True
                            break
                        if event.key == pygame.K_r:                                                   # For replay the current match
                            return 'r',winner_list
                        if event.key == pygame.K_x:                                                   # For rematch
                            return 'x'
        
        for position in range(1,10):
            if not board_dic[position][0]:
                break
        else:
            if not last_wait_screen_li[0]:                                                            # To stop when match is draw
                winner_list[match_no] = 'x_o'
                last_wait_screen_li[0] = True
        
        if last_wait_screen_li[0]:
            last_wait_screen_li[1] -= 1
            if last_wait_screen_li[1] <= 0:
                return winner_list

        pygame.display.update()

def Result_page(winner_list, no_of_match):                                                            # For display the result page

    font1 = pygame.font.Font(font, 70)
    font2 = pygame.font.Font(font, 30)
    font3 = pygame.font.Font(font, 50)

    circle_position_list = [(240,250),
                            (180,250),
                            (300,250),
                            (120,250),
                            (360,250)]
    
    if no_of_match == 1:
        circle_order = '0'
    elif no_of_match == 3:
        circle_order = '102'
    elif no_of_match == 5:
        circle_order = '31024'

    if winner_list[no_of_match-1] == '':                                                              # To check whether the match has finished or not
        is_end = 0
    else:
        no_of_x, no_of_o = 0, 0
        for winner_ in winner_list:
            if winner_ == 'x':
                no_of_x += 1
            elif winner_ == 'o':
                no_of_o += 1
        if no_of_x > no_of_o:
            winner = 'player 1'
        elif no_of_x < no_of_o:
            winner = 'player 2'
        elif no_of_x == no_of_o:
            winner = 0
        if winner:
            is_end = winner
        else:
            is_end = 1

    while True:

        screen.fill((255,165,0))

        text1 = font1.render("Tic Tac Toe", True, (255,0,120))
        screen.blit(text1, (160, 10))

        text2 = font2.render("Player 1 : X", True, (220,0,0))
        screen.blit(text2, (460,100))
        text3 = font2.render("Player 2 : O", True, (0,0,255))
        screen.blit(text3, (460,150))
        text4 = font2.render("Draw", True, (220,0,255))
        screen.blit(text4, (460,200))

        text5 = font3.render("Result", True, (0,0,0))
        screen.blit(text5, (200,160))
        
        for _ in range(len(winner_list)):                                                             # To show the winning person in each match
            position = circle_position_list[_]
            pygame.draw.circle(screen, (0,0,0), position, 20, 2)
            if winner_list[_] != '':
                order = circle_order[_]
                position_ = circle_position_list[int(order)]
                if winner_list[_] == 'x':
                    pygame.draw.circle(screen, (220,0,0), position_, 18)
                elif winner_list[_] == 'o':
                    pygame.draw.circle(screen, (0,0,255), position_, 18)
                elif winner_list[_] == 'x_o':
                    pygame.draw.circle(screen, (220,0,255), position_, 18)
        
        text6 = font2.render("Quit - Enter 'q'", True, (0,0,0))
        screen.blit(text6, (468,420))
        text7 = font2.render("Restart - Enter 'x'", True, (0,0,0))
        screen.blit(text7, (440,450))

        for event in pygame.event.get():                                                              # To get the input from keyboard
            if event.type == pygame.QUIT:
                return 0
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER:                                                    # To continue the game
                    return 1
                if event.key == pygame.K_q:                                                           # To exit from the game
                    return 0
                if event.key == pygame.K_x:                                                           # To restart the current game
                    return 'x'

        if is_end:
            if is_end == 1:
                text8 = font1.render("Match is Draw!", True, (0,0,0))
                screen.blit(text8, (100,300))
            elif is_end:
                text8 = font1.render(f"{is_end} is Winner!", True, (0,0,0))
                screen.blit(text8, (50,300))
        else:
            text8 = font2.render("Select 'Keypad Enter' to continue...", True, (0,0,0))
            screen.blit(text8, (20,450))

        pygame.display.update()

def main():

    match_mode = start()                                                                              # To get the mode of the match
    if match_mode == 0:
        return 0
    
    winner_list = ['' for _ in range(match_mode)]

    for match_no in range(match_mode):
        while True:
            restart = False
            winner_list = Game_page(winner_list, match_mode, match_no)                                # To get result from the game window
            if winner_list == 0:
                return 0
            elif winner_list == 'x':
                restart = True
                break
            elif winner_list[0] == 'r':
                winner_list = winner_list[1]
            else:
                break
        if restart:
            break

        next_page = Result_page(winner_list, match_mode)                                              # To show the rusult page and get the input
        if next_page == 0:
            return 0
        elif next_page == 'x':
            break
    main()                                                                                            # To restart the match

if __name__ == "__main__":

    main()                                                                                            # start<<

    font1 = pygame.font.Font(font, 70)                                                                # For ThankYou note
    for _ in range(4000):

        screen.fill((255,165,0))

        text1 = font1.render("Tic Tac Toe", True, (255,0,120))
        screen.blit(text1, (160, 10))
        text2 = font1.render("THANK YOU...", True, (0,0,0))
        screen.blit(text2, (50,200))
        text3 = font1.render("VISIT AGAIN!", True, (0,0,0))
        screen.blit(text3, (50,280))

        pygame.display.update()

    pygame.quit()                                                                                     # End<<