import getch
from art import *
from colorama import init
init(autoreset=True)
from colorama import Fore, Back, Style

#большая приветственная надпись
aprint("sword7", number=3, space=3)
print("\n")
tprint("IgLyuYar", font="epic")
aprint("sword1", number=3, space=3)
print("\n\n")

#функция вызова главного меню
def main_menu():
	aprint("sword8")
	print(Fore.GREEN + 'Главное меню')
	aprint("sword9")
	print(Fore.YELLOW + '\n[ 1 ] Начать игру')
	print(Fore.YELLOW + '[ 2 ] Об авторе')
	print(Fore.YELLOW + '[ 3 ] Выйти из игры\n')
	choise_main_menu()
	return

#функция вызова меню об авторе
def about_author_menu():
  aprint("sword8")
  print(Fore.GREEN + 'Об авторе')
  aprint("sword9")
  print(Fore.YELLOW + '\nИгру для Вас разработал Тинчурин Ярослав Искандерович\nСпасибо моей любимой жене и сыну за вдохновение и поддержку!\n')
  print(Fore.MAGENTA + "Нажмите 1 для возвращения в главное меню\n")
  choise_about_author_menu()
  return

#функция вызова меню "начать игру"
def start_game_menu():
    aprint("sword8")
    print(Fore.GREEN + 'Стартовое меню')
    aprint("sword9")
    print(Fore.YELLOW + '\n[ 1 ] Создать нового персонажа')
    print(Fore.YELLOW + '[ 2 ] Выбрать персонажа')
    print(Fore.YELLOW + '[ 3 ] Удалить персонажа')
    print(Fore.YELLOW + '[ 4 ] Список персонажей')
    print(Fore.YELLOW + '[ 5 ] Вернуться в главное меню\n')
    choise_start_game_menu()
    return

#функция обработки выбора в стартовом меню
def choise_start_game_menu():
    match getch.getch():
        case "5": main_menu()
        case _: wrong_choise_sgm()
    return

#функция обработки выбора меню об авторе
def choise_about_author_menu():
  match getch.getch():
    case "1": main_menu()
    case _: wrong_choise_aam()
  return

#функция неверного ввода в стартовом меню
def wrong_choise_sgm():
    print(Back.RED + "\nВыберите действие из предоставленного списка\n")
    start_game_menu()
    return

#функция неверного ввода в меню об авторе
def wrong_choise_aam():
  print(Back.RED + "\nНажмите 1 для возвращения в главное меню\n")
  about_author_menu()
  return

#функция обработки выбора главного меню
def choise_main_menu():
	match getch.getch():
	    case "1": start_game_menu()
	    case "2": about_author_menu()
	    case "3": exit()
	    case _: wrong_choise_mm()
	return

#функция неверного ввода в главном меню
def wrong_choise_mm():
	print(Back.RED + "\nВыберите действие из предоставленного списка\n")
	main_menu()
	return

main_menu()
