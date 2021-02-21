from core.menu import menu
from game.settings import __version__

BANNER = f'''
.------.
|M.--. | The vacuum cleaner world
| (\/) | version:    {__version__}
| :\/: |
| '--'M|
`------'
'''

if __name__ == '__main__':
    print(BANNER)

    while True:
        menu()
        repeat = input('Wanna play again? s/n\n>\t').lower()

        if repeat == 'n':
            break
