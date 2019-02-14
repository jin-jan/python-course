import pygame as pg
from snowman import SnowMan
from input_box import InputBox
from button import Button
from guess_word import GuessWord
from player import Player
from utils import SCREEN, PURPLE


def game(players):
    input_box = InputBox(440, 340, 480, 50)
    quit_button = Button(690, 520, 80, 50, 'QUIT', 'quit')
    start_button = Button(680, 440, 100, 50, 'START', 'start')
    player_text = Player(140, 160, 130, 50)
    play = GuessWord()
    snowman = SnowMan()
    rand_word = play.random_word()
    print_word = [False for i in range(len(rand_word))]
    in_letter = []
    out_letter = []

    done = False
    start_game = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
                pg.quit()
                quit()
            input_box.handle_event(event)
            quit_button.handle_event(event)
            start_game = start_button.handle_event(event)

        SCREEN.fill(PURPLE)
        quit_button.draw(SCREEN)

        if len(out_letter) == 14:
            start_button.draw(SCREEN)
        else:
            if in_letter == list(rand_word):
                if players:
                    won = (len(in_letter) + len(out_letter)) %2
                    if won:
                        player_text.text = 'Player 2!'
                    else:
                        player_text.text = 'Player 1!'
                    player_text.draw(SCREEN)
                start_button.draw(SCREEN)
            else:
                input_box.draw(SCREEN)
                if input_box.text in rand_word:
                    if input_box.text not in in_letter:
                        in_letter = play.check_in(input_box.text, print_word)
                else:
                    if input_box.text not in out_letter:
                        if len(out_letter) <= 14:
                            out_letter.append(input_box.text)
        play.draw_lines(SCREEN, print_word)
        if start_game:
            done = True
        snowman.wrong_letter = out_letter
        snowman.draw_snowman(SCREEN)

        pg.display.flip()


if __name__ == '__main__':
    end_game = False
    player1_button = Button(200, 440, 140, 50, '1 Player', '1')
    player2_button = Button(400, 440, 150, 50, '2 Players', '2')
    while not end_game:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                end_game = True
                pg.quit()
                quit()
            player1 = player1_button.handle_event(event)
            player2 = player2_button.handle_event(event)

        SCREEN.fill(PURPLE)
        player1_button.draw(SCREEN)
        player2_button.draw(SCREEN)

        if player1 == 1:
            game(False)
        if player2 == 2:
            game(True)
        pg.display.flip()
