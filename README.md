'BoB9' is the Alias to 'Black or Blue 9' which is the game's name.

BoB9 is a turn based card game between 2 players developed in Python 2.7.12

The game rules and behaviors are followed below:

- the 'BoB9' is played by two players as a competitive game.
- the game start with a chosen color ('Black' or 'Blue') named 'Start color'.
- the 'Start color' is chosen by some kind of arbitrary decision like a random number, etc.
- each player get 9 cards as a 'Hand', sorted between two colors divided (maybe randomly).
- if the start color is blue, players starts with 5 blue and 4 black cards.
- if the start color is black, each starts with 5 black and 4 blue.
- each 'Card' has a 'Value' (1-9) and a 'Color' (Black or Blue).
- the game is a Best of '9 turns' and '9 roles'.
- the player who get 5 turns first 'Win the role'.
- the player who get 5 roles 'Win the Game'.
- the game have a board.
- the board have 4 slots of cards.
- there is a pile of 9 cards named 'Stack' on the board and the Values are (1-9)
- each turn one card is taken from the 'Stack', is showed and two copies are placed in the center of the 'Board', one 'Blue' and other 'Black.
- the original card taken from the pile is discarded and goes to the 'Trash'
- each player needs to choose one card between the two board cards and place a 'Taped down' card from your 'Hand' on your own slot of the board.
- if both players choose the same 'Board card', then both untap you own 'Taped card', if the cards are black, the player who gets higher sum Value between your untapped card and the 'Board card' win, if the cards are blue, the player who gets lesser sum Value between your untapped card and the 'Board card' win.
- if each player choose a different card in the board, the player who get the lesser 'Points' on turn win.
- for those who choose the black card, 'Points' = 20 - cards sum. the better case is 20 - (9+9) = 2.
- for those who choose the blue card, 'Points' = 0 + cards sum. the better case is 0 + (1+1) = 2.
- after each turn, players discard the chosen cards, putting the one which came from your own hand to his 'Trash' and the 'Board card' to the 'Board trash'.
- when one player wins the best of 9 turns, win one role in a best of 9 roles.
- when a role is over, the player who won take the rest of the board 'Stack' as additional hand cards to the next role, getting advantage every time that win a role.
