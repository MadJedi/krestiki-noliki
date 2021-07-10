#КРЕСТИКИ-НОЛИКИ
#глобальные константы
X = "X"
O = "O"
EMPTY = " "
TIE = "НИЧЬЯ"
NUM_SQUARES = 9

def display_instruct():
    """ ВЫВОДИТ НА ЭКРАН ИНСТРУКЦИЮ """
print(
 """
Добро пожаловать в игру крестики-нолики. Играют: ИИ и Игрок.
Чтобы сделать ход, введи число от 0 до 8. Числа соответствуют полям доски.
 -----------         
| 0 | 1 | 2 |       
|-----------|         
| 3 | 4 | 5 |         
|-----------|       
| 6 | 7 | 8 |        
 -----------            

Приготовься к бою!!!\n
 """
 )

def ask_yes_no(question):
    """ Задаёт вопрос с ответом 'ДА' или 'НЕТ'."""
    response = None
    if response not in ("y", "n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    """Просит ввести число диапазона"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def pieces():
    """Определяет принадлежность первого хода."""
    go_first = ask_yes_no("Хочешь оставить первый ход за собой?(y/n): ")
    if go_first == "y":
        print("\nНу что ж, ходи первым, играй крестиками.")
        human = X
        computer = O
    else:
        print("\nЯ хожу первым, играю крестиками.")
        computer = X
        human = O
        return computer, human
def new_board():
    """Создаёт новую доску."""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    """Отображает игровую доску."""
    print("\t", "----------")  
    print("\n\t", board[0], " | ", board[1], " | ", board[2])
    print("\t", "----------")
    print("\n\t", board[3], " | ", board[4], " | ", board[5])
    print("\t", "----------")
    print("\n\t", board[6], " | ", board[7], " | ", board[8])
    print("\t", "----------")

def legal_moves(board):
    """Создаёт список доступных ходов."""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):
    """Определяет победителя в игре."""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
    return None

def human_move(board, human):
    """Получает ход человека."""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Твой ход, выбери одно из полей(0 - 8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nПоле уже занято, выбери другое")
    return move

def computer_move(board,computer,human):
    """Делает ход за компьютерого противника."""
#рабочая копия доски, функция будет менять некоторые значения в списке
    board = board [:]
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("Я выберу поле номер", end = " ")
    for move in legal_moves(board):
        board[move] = computer
#если следующим ходом компьютер может победить делаем этот ход
        if winner(board) == computer:
            print(move)
            return move
#выполним проверку, отменим внесенные изменения
        board[move] = EMPTY
    for move in legal_moves(board):
        board[move] = human
#если следующим ходом выигрывает человек, блокируем ход
        if winner(board) == human:
            print(move)
        return move
#проверка и отмена внесенных изменений
        board[move] = EMPTY
#если селдующим ходом ни одна сторона не может победить, выбираем лучшее из доступных полей
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
        return move

def next_turn(turn):
    """Осуществляет переход хода"""
    if turn == X:
        return 0
    else:
        return X #функция для чередования ходов по мере совершения ходов

def congrat_winner(the_winner, computer, human):
    """Поздравляем победителя игры"""
    if the_winner != TIE:
        print("Три", the_winner, "в ряд!\n")
    else:
        print("Ничья!\n")
    if the_winner == computer:
        print("ПОБЕДА ЗА МНОЙ!!!")
    elif the_winner == human:
        print("ПОБЕДА ТВОЯ!!!\n")
    elif the_winner == TIE:
        print("ГОСПОДА, ЭТО НИЧЬЯ\n")

def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)
#запус программы
main()
input("\n\nPRESS ENTER FOR EXIT")

