import pygame as pg
from snowman import SnowMan
from input_box import InputBox
from button import Button
from guess_word import GuessWord
from utils import SCREEN, PURPLE


def game():
    input_box = InputBox(440, 340, 480, 50)
    quit_button = Button(540, 440, 100, 50, 'QUIT', 'quit')
    start_button = Button(640, 440, 100, 50, 'START', 'start')
    play = GuessWord()
    snowman = SnowMan()
    rand_word = play.random_word()
    print_word = [False for i in range(len(rand_word))]
    in_letter = []
    out_letter = []
    print(rand_word)

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
        print(input_box.text)

        if len(out_letter) == 14:
            start_button.draw(SCREEN)
        else:
            if in_letter == list(rand_word):
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

        print(play.check_in(input_box.text, print_word))
        pg.display.flip()


if __name__ == '__main__':
    end_game = False
    while not end_game:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                end_game = True
                import pdb;pdb.set_trace()
                pg.quit()
                quit()
        game()
