# -*- coding                                                                     : utf-8 -*-
from sys import argv
from random import randint
import os


class Bob9:
    def __init__(self, P1, P2):
        # Parametros iniciais
        self.P1 = P1
        self.P2 = P2

        # Constantes preliminares para gerar ambiente
        self.COLORS = ['BLACK', 'BLUE']
        self.START_COLOR = self.COLORS[randint(0, 1)]

        #
        # Variaveis iniciais vazias
        #
        self.__game_over__ = False
        self.__set_over__ = False
        self.__turn_over__ = False
        self.turn = 1
        self.set = 1
        self.board = [(self.P1, ' '), ('BLACK', ' '),
                      ('BLUE', ' '), (self.P2, ' ')]
        self.stack = []
        self.trash = []
        self.p1_hand = []
        self.p2_hand = []
        self.hands = {}
        self.p1_trash = []
        self.p2_trash = []

        # Pontuacao inicial. Para exibir informacoes bastar dar print em
        # 'game_bar' a qualquer momento
        self.p1_wins = 00
        self.p2_wins = 0
        self.p1_sets = 0
        self.p2_sets = 0
        self.score = 'TURNOS[%s %dX%d %s]sets[%s %dX%d %s]' % (
            self.P1, self.p1_wins, self.p2_wins, self.P2, self.P1, self.p1_sets, self.p2_sets, self.P2)
        self.game_bar = "Turno :%s-9set: %s-9Placar:%s" % (
            self.turn, self.set, self.score)

        return
    #
    # funcoes de criacao do jogo
    #

    # Atualiza Placar
    def score_update(self):
        self.score = 'TURNOS[%s %dX%d %s]sets[%s %dX%d %s]' % (
            self.P1, self.p1_wins, self.p2_wins, self.P2, self.P1, self.p1_sets, self.p2_sets, self.P2)
        self.game_bar = "Turno :%s de 9set: %s de 9Placar:%s" % (
            self.turn, self.set, self.score)
        return

    # Cria Mao de cartas inicial para jogador
    def hand_build(self, color):
        hand_built = []
        used_value = []

        for i in range(1, 10):
            value = randint(1, 9)

            while value in used_value:
                value = randint(1, 9)

            card = ['card %d' % i, value, color]
            used_value.append(value)

            if color == 'BLACK':
                color = 'BLUE'
            else:
                color = 'BLACK'

            hand_built.append(card)

        hand_built.insert(0, 9)

        return hand_built

    # Cria stack a partir de uma lista de valores
    def create_stack(self):
        new_stack = []
        used_value = []

        for i in range(0, 9):
            value = randint(1, 9)

            while value in used_value:
                value = randint(1, 9)

            new_stack.append(value)
            used_value.append(value)

        return new_stack

    # Prepara o jogo em seu estado de inicio/re-inicio do jogo
    def onStart(self):
        # Inicializacao do stack
        self.stack = self.create_stack()

        # Maos iniciais para os jogadores
        self.p1_hand = self.hand_build(self.START_COLOR)
        self.p2_hand = self.hand_build(self.START_COLOR)
        self.hands = {self.P1: self.p1_hand, self.P2: self.p2_hand}
        self.trash = []
        self.p1_trash = []
        self.p1_trash = []

        return True

    # Exibe mao de um jogador
    def show_hand(self, player):
        cards_to_show = []
        if player == self.P1:
            hand = self.p1_hand
        else:
            hand = self.p2_hand

        for i in range(1, len(hand)):
            cards_to_show.append('%d %s' % (hand[i][1], hand[i][2]))

        show = '%s cards: %s' % (hand[0], cards_to_show)
        print show.center(150)
        return cards_to_show

    # Jogador escolhe uma card a jogar
    def choose_card_from_hand(self, player):
        hand = []
        if player == self.P1:
            hand = self.p1_hand
        elif player == self.P2:
            hand = self.p2_hand

        self.show_hand(player)

        message = 'Choose your card by position[%d - %d]\n' % (
            1, len(hand) - 1)
        card_position = int(raw_input(message.center(150)))

        while card_position not in range(1, len(hand)):
            card_position = int(
                raw_input('Invalid position!' + message % (1, len(hand) - 1)))

        return hand[card_position]

    # Atualiza os 4 slots do board, passando a card retirada do stack e cards
    # dos jogadores
    def put_cards_on_board(self, taken_from_stack, p1_card, p2_card):
        self.board = (
            [(self.P1, p1_card), ('BLACK', taken_from_stack),
             ('BLUE', taken_from_stack), (self.P2, p2_card)]
        )
        return self.board

    # Incrementa a mao do vencedor da set com as sobras do stack

    # Nao descartar o stack ate gerar uma nova mao para cada jogador
    def new_set_winner_hand(self, player):
        if player == self.P1:
            hand = self.p1_hand
        else:
            hand = self.p2_hand

        if len(self.stack) > 0:
            stack_card_color = ''
            last_card_in_hand = hand[len(hand) - 1]

            if last_card_in_hand[2] == 'BLACK':
                stack_card_color = 'BLUE'
            else:
                stack_card_color = 'BLACK'

            new_hand = hand
            for card in self.stack:
                new_hand.append(
                    ('card %d' % (new_hand[0] + 1), card, stack_card_color))
                new_hand[0] += 1
        else:
            print "Stack vazio. Mao do vencedor continua a mesma.".center(150)

        return new_hand

    # Atualiza o jogo
    def onUpdate(self):
        self.__turn_over__ = False

        # Card retirada do topo do Stack e posta em duas cores no board
        taken_from_stack = self.stack.pop()

        # Informacoes do estado atual do jogo
        print 'BLACK or BLUE 9'.center(150)
        print self.game_bar.center(150)
        print 'BOARD %s'.center(150) % self.put_cards_on_board(taken_from_stack, '_', '_')

        # Opcoes do jogador 1
        print self.P1 + ' OPTION SELECTION'.center(150)
        print "1-Fazer Jogada".center(150)
        print "2-Ver seu Trash".center(150)
        print "3-Ver Trash adversario".center(150)
        print "4-Ver Stack Trash".center(150)

        option_message = "O que deseja fazer?(1-4)\n"

        p1_option = raw_input(option_message.center(150))
        while not p1_option.isdigit() or int(p1_option) not in list(range(1, 5)):
            p1_option = raw_input(("O que deseja fazer?(1-4)\n").center(150))

        while not int(p1_option) == 1:
            if int(p1_option) == 4:
                print ('%s ' % self.trash).center(150)
            if int(p1_option) == 3:
                print ('%s ' % self.p2_trash).center(150)
            if int(p1_option) == 2:
                print ('%s ' % self.p1_trash).center(150)

            p1_option = raw_input(option_message.center(150))

        # Fase de escolhas de cards dos jogadores
        else:
            print ('%s CARD SELECTION ' % self.P1).center(150)
            p1_card = self.choose_card_from_hand(self.P1)
            self.p1_hand.remove(p1_card)
            self.p1_hand[0] = self.p1_hand[0] - 1
            self.p1_trash.append(p1_card)

        os.system('cls')

        # Informacoes do estado atual do jogo
        print 'BLACK or BLUE 9'.center(150)
        print self.game_bar.center(150)
        print 'BOARD %s'.center(150) % self.put_cards_on_board(taken_from_stack, '_', '_')

        # Opcoes do jogador 2
        print self.P2 + ' OPTION SELECTION'.center(150)
        print "1-Fazer Jogada".center(150)
        print "2-Ver seu Trash".center(150)
        print "3-Ver Trash adversario".center(150)
        print "4-Ver Stack Trash".center(150)

        p2_option = raw_input(option_message.center(150))
        while not p2_option.isdigit() or orint(p2_option) not in list(range(1, 5)):
            p2_option = raw_input(option_message.center(150))

        while not int(p2_option) == 1:
            if int(p2_option) == 4:
                print ('%s ' % self.trash).center(150)
            if int(p2_option) == 3:
                print ('%s ' % self.p1_trash).center(150)
            if int(p2_option) == 2:
                print ('%s ' % self.p2_trash).center(150)

            p2_option = raw_input(option_message.center(150))

        # Fase de escolhas de cards dos jogadores
        else:
            print '%s CARD SELECTION '.center(150) % self.P2
            p2_card = self.choose_card_from_hand(self.P2)
            self.p2_hand.remove(p2_card)
            self.p2_hand[0] = self.p2_hand[0] - 1
            self.p2_trash.append(p2_card)

        os.system('cls')

        # Re-exibe o board com as escolhas dos jogadores
        print 'BOARD %s'.center(150) % self.put_cards_on_board(taken_from_stack, p1_card, p2_card)

        self.trash.append(taken_from_stack)

        # Calcula pontuacao para a jogada de cada jogador. Vence a menor pontuacao
        # P1
        if p1_card[2] == 'BLACK':
            # 20 - (jogador + stack)
            p1_point = 20 - (p1_card[1] + taken_from_stack)
        else:
            # 0 + (jogador + stack)
            p1_point = 0 + (p1_card[1] + taken_from_stack)

        # P2
        if p2_card[2] == 'BLACK':
            # 20 - (jogador + stack)
            p2_point = 20 - (p2_card[1] + taken_from_stack)
        else:
            # 0 + (jogador + stack)
            p2_point = 0 + (p2_card[1] + taken_from_stack)

        if p1_point == p2_point:
            self.turn = self.turn + 2
            self.p1_wins = self.p1_wins + 1
            self.p2_wins = self.p2_wins + 1
            print "Draw. 1 win to each player and um turn skipped.".center(150)

        if p1_point < p2_point:
            self.turn = self.turn + 1
            self.p1_wins = self.p1_wins + 1
            print self.P1 + " Won a turn.".center(150)

        if p2_point < p1_point:
            self.turn = self.turn + 1
            self.p2_wins = self.p2_wins + 1
            print self.P2 + " Won a turn.".center(150)

        self.__turn_over__ = True

        if self.p1_wins >= 5 and self.p1_wins > self.p2_wins:
            print self.P1 + " Won a set.".center(150)
            self.p1_sets = self.p1_sets + 1

            # Maos iniciais para os jogadores
            self.p1_hand = self.hand_build(self.START_COLOR)
            self.p2_hand = self.hand_build(self.START_COLOR)
            self.hands = {self.P1: self.p1_hand, self.P2: self.p2_hand}
            self.trash = []
            self.p1_trash = []
            self.p1_trash = []
            self.p1_hand = self.new_set_winner_hand(self.P1)

            # Inicializacao do stack
            self.stack = self.create_stack()
            self.p1_wins = 0
            self.p2_wins = 0
            self.__set_over__ = True

        if self.p1_wins < self.p2_wins >= 5:
            print self.P2 + " Won a set.".center(150)
            self.p2_sets = self.p2_sets + 1

            # Maos iniciais para os jogadores
            self.p1_hand = self.hand_build(self.START_COLOR)
            self.p2_hand = self.hand_build(self.START_COLOR)
            self.hands = {self.P1: self.p1_hand, self.P2: self.p2_hand}
            self.trash = []
            self.p1_trash = []
            self.p1_trash = []
            self.p2_hand = self.new_set_winner_hand(self.P2)

            # Inicializacao do stack
            self.stack = self.create_stack()
            self.p1_wins = 0
            self.p2_wins = 0
            self.__set_over__ = True

        if self.__set_over__:
            self.set = self.set + 1
            self.turn = 1
            self.__set_over__ = False

        if self.p2_sets < self.p1_sets >= 5:
            print self.P1 + " GANHOU A BEST OF 9 DAS BEST OF 9!!!!.".center(150)
            self.__game_over__ = True

        if self.p1_sets < self.p2_sets >= 5:
            print self.P2 + " GANHOU A BEST OF 9 DAS BEST OF 9!!!!.".center(150)
            self.__game_over__ = True

        self.score_update()

        stop_point = raw_input(
            "Pressione qualquer tecla para seguir para o proximo turno>".center(150))
        os.system("cls")

        return self.__game_over__


def main():
    print 'BLACK or BLUE 9'.center(150)
    print 'Game design and script by Icaro Torres: icaro.stuart@gmail.com'.center(150)
    print 'Github https://github.com/IcaroTorres/bob9'.center(150)

    P1 = raw_input(('What is your name Player 1?\n').center(150))
    P2 = raw_input(('What is your name Player 2?\n').center(150))
    os.system('cls')

    game = Bob9(P1, P2)
    game.onStart()
    while not game.__game_over__:  # != True:
        game.onUpdate()


if __name__ == '__main__':
    main()
