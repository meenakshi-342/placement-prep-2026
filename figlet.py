import sys
from pyfiglet import Figlet 
import random

figlet = Figlet()
available_fonts = figlet.getFonts()
if len(sys.argv) == 1:
   
    chosen_font = random.choice(available_fonts)
    figlet.setFont(font=chosen_font)

elif len(sys.argv) == 3:
    # 2 extra args -> Check flag and font existence
    is_valid_flag = sys.argv[1] == "-f" or sys.argv[1] == "--font"
    is_valid_font = sys.argv[2] in available_fonts

    if is_valid_flag and is_valid_font:
        figlet.setFont(font=sys.argv[2])
    else:
        sys.exit("Invalid usage")

else:
    # Any other number of args -> Invalid
    sys.exit("Invalid usage")
text = input("Input: ")
  
text = input("Input: ")
print(figlet.renderText(text))

