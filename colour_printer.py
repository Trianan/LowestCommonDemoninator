#                           COLOUR-PRINTER
#-------------------------------------------------------------------------------
#   A simple utility for outputting custom coloured text.
#
#     Uses ANSI-escape sequences to modify output text, and
#   supports RGB-values.
#-------------------------------------------------------------------------------
#     If this prints the sequences directly, run this command to
#   enable ANSI in Windows terminals:
#
#   reg add HKEY_CURRENT_USER\Console /v VirtualTerminalLevel /t REG_DWORD /d 1
#
#     To disable ANSI, run the same command with 0 replacing 1 as the
#   final argument.
#-------------------------------------------------------------------------------
#     Heavy help from:
#   https://replit.com/talk/learn/ANSI-Escape-Codes-in-Python/22803
#-------------------------------------------------------------------------------

import os

# Foreground colours:
class fg:
    BLACK = "\u001b[30m"
    RED = "\u001b[31m"
    GREEN = "\u001b[32m"
    YELLOW = "\u001b[33m"
    BLUE = "\u001b[34m"
    MAGENTA = "\u001b[35m"
    CYAN = "\u001b[36m"
    WHITE = "\u001b[37m"
    def rgb(r, g, b): return f"\u001b[38;2;{r};{g};{b}m"

# Background colours:
class bg:
    BLACK = "\u001b[40m"
    RED = "\u001b[41m"
    GREEN = "\u001b[42m"
    YELLOW = "\u001b[43m"
    BLUE = "\u001b[44m"
    MAGENTA = "\u001b[45m"
    CYAN = "\u001b[46m"
    WHITE = "\u001b[47m"
    def rgb(r, g, b): return f"\u001b[48;2;{r};{g};{b}m"

# Utilities and decorations:
class util:
    RESET = "\u001b[0m"
    BOLD = "\u001b[1m"
    UNDERLINE = "\u001b[4m"
    REVERSE = "\u001b[7m"

if __name__ == '__main__':
    print(f'''
        {   fg.RED + 'H' +
            fg.rgb(255,165,0) + 'E' +
            fg.YELLOW + 'L' +
            fg.GREEN + 'L' +
            fg.BLUE + 'O' +
            fg.rgb(75,0,130) + '!' +
            fg.rgb(138,43,226) + '!' +
            util.RESET
        }

        This module is {fg.GREEN}{bg.MAGENTA}working properly{util.RESET}.

        {util.BOLD}This should be bold.{util.RESET}

        {util.UNDERLINE}This should be underlined.{util.RESET}

        {util.REVERSE}This should be inverted.{util.RESET}

        {fg.BLACK}BLACK{util.RESET}
        {fg.RED}RED{util.RESET}
        {fg.GREEN}GREEN{util.RESET}
        {fg.YELLOW}YELLOW{util.RESET}
        {fg.BLUE}BLUE{util.RESET}
        {fg.MAGENTA}MAGENTA{util.RESET}
        {fg.CYAN}CYAN{util.RESET}
        {fg.WHITE}WHITE{util.RESET}

          If this prints the sequences directly, run this command to
        enable ANSI in Windows terminals:
        
        {fg.WHITE}reg add HKEY_CURRENT_USER\Console /v VirtualTerminalLevel /t REG_DWORD /d 1{util.RESET}
        
          To disable ANSI, run the same command with 0 replacing 1 as the
        final argument.
    ''')