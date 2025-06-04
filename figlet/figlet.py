from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()

args = ["-f", "--font"]



if sys.argv[1] in args:
    if sys.argv[2] not in fonts:
        sys.exit("Invalid usage")

    elif len(sys.argv) == 3:
        font_name = sys.argv[2]
        figlet.setFont(font=font_name)

    user = input()
    if len(sys.argv) == 1:
        font_name = random.choice(fonts)
        figlet.setFont(font=font_name)


    print(figlet.renderText(user))
else:
    sys.exit("Invalid usage")
