"""
Author: Vaasudevan Srinivasan
Author Email: vaasuceg.96@gmail.com
Created on: May 08, 2017
Last Modified on: Dec 08, 2020
Description: Python package - cowsay
"""

from __future__ import print_function
import re
import sys

__version__ = '3.0'
__name__ = 'cowsay'

flg = []

Beavis = r'''
             _------~~-,
          ,'            ,
          /               \\
         /                :
        |                  '
        |                  |
        |                  |
         |   _--           |
         _| =-.     .-.   ||
         o|/o/       _.   |
         /  ~          \\ |
       (____\@)  ___~    |
          |_===~~~.`    |
       _______.--~     |
       \\________       |
                \\      |
              __/-___-- -__
             /            _ \\

            '''

Cheese = ''' 

     /     \\_/         |
    |                 ||
    |                 ||
   |    ###\\  /###   | |
   |     0  \\/  0    | |
  /|                 | |
 / |        <        |\\ \\
| /|                 | | |
| |     \\_______/   |  | |
| |                 | / /
/||                 /|||
   ----------------|
        | |    | |
        ***    ***
       /___\\  /___\\

       '''

Daemon = ''' 
            /- _  `-/  '
           (/\\/ \\ \\   /\\
           / /   | `    \\
           O O   ) /    |
           `-^--'`<     '
          (_.)  _  )   /
           `.___/`    /
             `-----' /
<----.     __ / __   \\
<----|====O)))==) \\) /====
<----'    `--' `.__,' \\
             |        |
              \\       /
        ______( (_  / \\______
      ,'  ,-----'   |        \\
      `--{__________)        \\/

       '''

Cow = r'''

   ^__^                             
   (oo)\_______                   
   (__)\       )\/\             
       ||----w |           
       ||     ||  

       '''

Dragon = r''' 

                           / \\  //\\
            |\\___/|      /   \\//  \\\\
            /0  0  \\__  /    //  | \\ \\    
           /     /  \\/_/    //   |  \\  \\  
           \@_^_\@'/   \\/_   //    |   \\   \\ 
           //_^_/     \\/_ //     |    \\    \\
        ( //) |        \\///      |     \\     \\
      ( / /) _|_ /   )  //       |      \\     _\\
    ( // /) '/,_ _ _/  ( ; -.    |    _ _\\.-~        .-~~~^-.
  (( / / )) ,-{        _      `-.|.-~-.           .~         `.
 (( // / ))  '/\\      /                 ~-. _ .-~      .-~^-.  \\
 (( /// ))      `.   {            }                   /      \\  \\
  (( / ))     .----~-.\\        \\-'                 .~         \\  `. \\^-.
             ///.----..>        \\             _ -~             `.  ^-`  ^-_
               ///-._ _ _ _ _ _ _}^ - - - - ~                     ~-- ,.-~
                                                                  /.-~

         '''

Ghostbusters = ''' 
                       __---__
                    _-       /--______
               __--( /     \\ )XXXXXXXXXXX\\v.
             .-XXX(   O   O  )XXXXXXXXXXXXXXX-
            /XXX(       U     )        XXXXXXX\\
          /XXXXX(              )--_  XXXXXXXXXXX\\
         /XXXXX/ (      O     )   XXXXXX   \\XXXXX\\
         XXXXX/   /            XXXXXX   \\__ \\XXXXX
         XXXXXX__/          XXXXXX         \\__---->
 ---___  XXX__/          XXXXXX      \\__         /
   \\-  --__/   ___/\\  XXXXXX            /  ___--/=
    \\-\\    ___/    XXXXXX              '--- XXXXXX
       \\-\\/XXX\\ XXXXXX                      /XXXXX
         \\XXXXXXXXX   \\                    /XXXXX/
          \\XXXXXX      >                 _/XXXXX/
            \\XXXXX--__/              __-- XXXX/
             -XXXXXXXX---------------  XXXXXX-
                \\XXXXXXXXXXXXXXXXXXXXXXXXXX/
                  ""VXXXXXXXXXXXXXXXXXXV""

            '''

Kitty = ''' 

     ("`-'  '-/") .___..--' ' "`-._
         ` *_ *  )    `-.   (      ) .`-.__. `)
         (_Y_.) ' ._   )   `._` ;  `` -. .-'
      _.. `--'_..-_/   /--' _ .' ,4
   ( i l ),-''  ( l i),'  ( ( ! .-'  

        '''

Meow = r"""

                  _ ___.--'''`--''//-,-_--_.
      \\`"' ` || \\\\ \\ \\\\/ / // / ,-\\\\`,_
     /'`  \\ \\ || Y  | \\|/ / // / - |__ `-,
    /\@"\\  ` \\ `\\ |  | ||/ // | \\/  \\  `-._`-,_.,
   /  _.-. `.-\\,___/\\ _/|_/_\\_\\/|_/ |     `-._._)
   `-'``/  /  |  // \\__/\\__  /  \\__/ \\
        `-'  /-\\/  | -|   \\__ \\   |-' |
          __/\\ / _/ \\/ __,-'   ) ,' _|'
         (((__/(((_.' ((___..-'((__,'

        """

Milk = ''' 

       ____________ 
       |__________|
      /           /\\
     /           /  \\
    /___________/___/|
    |          |     |
    |  ==\\ /== |     |
    |   O   O  | \\ \\ |
    |     <    |  \\ \\|
   /|          |   \\ \\
  / |  \\_____/ |   / /
 / /|          |  / /|
/||\\|          | /||\\/
    -------------|   
        | |    | | 
       <__/    \\__>

       '''

Pig = r'''
             ,.
            (_|,.
            ,' /, )_______   _
        __j o``-'        `.'-)'
        (")                 \'
        `-j                |
            `-._(           /
                |_\  |--^.  /
            /_]'|_| /_)_/
                /_]'  /_]'

      '''

Stegosaurus = '''                    
                                     / `.   .' " 
                             .---.  <    > <    >  .---.
                             |    \\  \\ - ~ ~ - /  /    |
         _____          ..-~             ~-..-~
        |     |   \\~~~\\.'                    `./~~~/
       ---------   \\__/                        \\__/
      .'  O    \\     /               /       \\  " 
     (_____,    `._.'               |         }  \\/~~~/
      `----.          /       }     |        /    \\__/
            `-.      |       /      |       /      `. ,~~|
                ~-.__|      /_ - ~ ^|      /- _      `..-'   
                     |     /        |     /     ~-.     `-. _  _  _
                     |_____|        |_____|         ~ - . _ _ _ _ _>

              '''

Stimpy = ''' 
        .    _  .    
       |\\_|/__/|    
       / / \\/ \\  \\  
      /__|O||O|__ \\ 
     |/_ \\_/\\_/ _\\ |  
     | | (____) | ||  
     \\/\\___/\\__/  // 
     (_/         ||
      |          ||
      |          ||\\   
       \\        //_/  
        \\______//
       __ || __||
      (____(____)

        '''

Turkey = r'''

                                             ,+*^^*+___+++_
                                       ,*^^^^              )
                                    _+*                     ^**+_
                                  +^       _ _++*+_+++_,         )
              _+^^*+_    (     ,+*^ ^          \\+_        )
             {       )  (    ,(    ,_+--+--,      ^)      ^\\
            { (\@)    } f   ,(  ,+-^ __*_*_  ^^\\_   ^\\       )
           {:;-/    (_+*-+^^^^^+*+*<_ _++_)_    )    )      /
          ( /  (    (        ,___    ^*+_+* )   <    <      \\
           U _/     )    *--<  ) ^\\-----++__)   )    )       )
            (      )  _(^)^^))  )  )\\^^^^^))^*+/    /       /
          (      /  (_))_^)) )  )  ))^^^^^))^^^)__/     +^^
         (     ,/    (^))^))  )  ) ))^^^^^^^))^^)       _)
          *+__+*       (_))^)  ) ) ))^^^^^^))^^^^^)____*^
          \\             \\_)^)_)) ))^^^^^^^^^^))^^^^)
           (_             ^\\__^^^^^^^^^^^^))^^^^^^^)
             ^\\___            ^\\__^^^^^^))^^^^^^^^)\\\\
                  ^^^^^\\uuu/^^\\uuu/^^^^\\^\\^\\^\\^\\^\\^\\^\\
                     ___) >____) >___   ^\\_\\_\\_\\_\\_\\_\\)
                    ^^^//\\\\_^^//\\\\_^       ^(\\_\\_\\_\\)
                      ^^^ ^^ ^^^ ^

           '''

Turtle = ''' 

                                               ___-------___
                                           _-~~             ~~-_
                                        _-~                    /~-_
             /^\\__/^\\         /~  \\                   /    \\
           /|  O|| O|        /      \\_______________/        \\
          | |___||__|      /       /                \\          \\
          |          \\    /      /                    \\          \\
          |   (_______) /______/                        \\_________ \\
          |         / /         \\                      /            \\
           \\         \\^\\\\         \\                  /               \\     /
             \\         ||           \\______________/      _-_       //\\__//
               \\       ||------_-~~-_ ------------- \\ --/~   ~\\    || __/
                 ~-----||====/~     |==================|       |/~~~~~
                  (_(__/  ./     /                    \\_\\      \\.
                         (_(___/                         \\_____)_)


        '''

Tux = ''' 

        .--.
       |o_o |
       |:_/ |
      //   \\ \\
     (|     | )
    /'\\_   _/`\\
    \\___)=(___/

    '''


# %%

def string_processing(args):
    return_string = "```"
    args = str(args)
    lines = args.split("\n")
    lines = [i.strip() for i in lines]
    lines = [i for i in lines if len(i) != 0]
    length = len(lines)

    if length == 1:

        flag = len(lines[0])
        if flag < 50:
            return_string = return_string +  ("  " + "_" * flag) + "\n"
            return_string = return_string + ("< " + lines[0] + " " * (flag - len(lines[0]) + 1) + ">") + "\n"
            return_string  = return_string + ("  " + "=" * flag) + "\n"
            flg.append(flag)
        else:
            args = list("".join(lines[0]))
            for j, i in enumerate(args):
                if j % 50 == 0:
                    args.insert(j, "\n")
            string_processing("".join(args))

    else:
        flag = len(max(lines, key=len))
        if all(len(i) < 50 for i in lines):
            return_string = return_string + ("  " + "_" * flag) + "\n"
            return_string = return_string + (" /" + " " * flag + "\\") + "\n"
            for i in lines:
                return_string = return_string + ("| " + i + " " * (flag - len(i) + 1) + "|") + "\n"
            return_string = return_string + (" \\" + " " * flag + "/") + "\n"
            return_string = return_string + ("  " + "=" * flag) + "\n"
            flg.append(flag)
        else:
            new_lines = []
            for i in lines:
                if len(i) > 50:
                    args = list("".join(i))
                    for j, i in enumerate(args):
                        if j % 50 == 0:
                            args.insert(j, "\n")
                    new_lines.append("".join(args))
                else:
                    new_lines.append(i + "\n")
            return_string = return_string +  string_processing("".join(new_lines)) + "\n"
    return return_string


# %% Character specific functions with minor tweaks

def beavis(args):
    str = ""
    try:

        str = str + string_processing(args) + "\n"
        flag = flg[-1]

        str = str + (' ' * (flag + 5) + '\\') + "\n"
        str = str + (' ' * (flag + 6) + '\\') + "\n"
        str = str + (' ' * (flag + 7) + '\\') + "\n"

        char_lines = Beavis.split('\n')
        char_lines = [i for i in char_lines if len(i) != 0]

        for i in char_lines:
            str = str + (' ' * flag + i) + "\n"

    except:
        str = ("```Can't Say...!! Give something much more easier to Mr.Beavis...")
    return str + "```"


def cheese(args):
    str = ""
    try:

        str = str + string_processing(args) + "\n"
        flag = flg[-1]

        str = str + (' ' * (flag + 5) + '\\') + "\n"
        str = str + (' ' * (flag + 6) + '\\') + "\n"
        str = str + (' ' * (flag + 7) + '\\') + "\n"
        str = str + (' ' * (flag + 8) + '\\') + "\n"

        char_lines = Cheese.split('\n')
        char_lines = [i for i in char_lines if len(i) != 0]

        for i in char_lines:
            str = str + (' ' * (flag + 5) + i) + "\n"

    except:
        str = ("```Can't Say...!! Give something much more easier to Mr.Cheese...")
    return str + "```"


def daemon(args):
    str = ""
    try:

        str = str + (string_processing(args)) + "\n"
        flag = flg[-1]

        str = str + (' ' * (flag + 5) + '\\') + "\n"
        str = str + (' ' * (flag + 6) + '\\') + "\n"
        str = str + (' ' * (flag + 7) + '\\') + "\n"
        str = str + (' ' * (flag + 8) + '\\') + "\n"

        char_lines = Daemon.split('\n')
        char_lines = [i for i in char_lines if len(i) != 0]

        for i in char_lines:
            str = str + (' ' * (flag - 3) + i) + "\n"

    except:
        str = ("```Can't Say...!! Give something much more easier to Mr.Daemon...")
    return str + "```"


def cow(args):
    try:
        str = (string_processing(args)) + "\n"
        flag = flg[-1]

        str = str + (' ' * (flag + 5) + '\\') + "\n"
        str = str + (' ' * (flag + 6) + '\\') + "\n"

        char_lines = Cow.split('\n')
        char_lines = [i for i in char_lines if len(i) != 0]

        for i in char_lines:
            str = str + (' ' * (flag + 5) + i) + "\n"
        str = str + "```"


    except:
        str = ("Can't Say...!! Give something much more easier to Mr.Cow...")

    return str


def dragon(args):
    str = ""
    try:

        str = str + string_processing(args) + "\n"
        flag = flg[-1]

        str = str + (' ' * (flag + 5) + '\\') + "\n"
        str = str + (' ' * (flag + 6) + '\\') + "\n"
        str = str + (' ' * (flag + 7) + '\\') + "\n"
        str = str + (' ' * (flag + 8) + '\\') + "\n"

        char_lines = Dragon.split('\n')
        char_lines = [i for i in char_lines if len(i) != 0]

        for i in char_lines:
            str = str + (' ' * (flag + 3) + i) + "\n"

    except:
        str = str + ("```Can't Say...!! Give something much more easier to Mr.Dragon...")
    return str + "```"


def ghostbusters(args):
    str = ""
    try:

        str = str + string_processing(args) + "\n"
        flag = flg[-1]

        str = str + (' ' * (flag + 5) + '\\') + "\n"
        str = str + (' ' * (flag + 6) + '\\') + "\n"
        str = str + (' ' * (flag + 7) + '\\') + "\n"
        str = str + (' ' * (flag + 8) + '\\') + "\n"

        char_lines = Ghostbusters.split('\n')
        char_lines = [i for i in char_lines if len(i) != 0]

        for i in char_lines:
            str = str + (' ' * (flag - 3) + i) + "\n"

    except:
        str = ("```Can't Say...!! Give something much more easier to"
              "Mr.Ghostbusters...")
    return str + "```"


def kitty(args):
    str = ""
    try:

        str = str + string_processing(args) + "\n"
        flag = flg[-1]

        str = str + (' ' * (flag + 5) + '\\') + "\n"
        str = str + (' ' * (flag + 6) + '\\') + "\n"
        str = str + (' ' * (flag + 7) + '\\') + "\n"
        str = str + (' ' * (flag + 8) + '\\') + "\n"

        char_lines = Kitty.split('\n')
        char_lines = [i for i in char_lines if len(i) != 0]

        for i in char_lines:
            str = str + (' ' * (flag + 3) + i) + "\n"

    except:
        str = ("```Can't Say...!! Give something much more easier to Ms.Kitty...")
    return str + "```"


def meow(args):
    str = ""
    try:

        str = str + string_processing(args) + "\n"
        flag = flg[-1]

        str = str + (' ' * (flag + 5) + '\\') + "\n"
        str = str + (' ' * (flag + 6) + '\\') + "\n"
        str = str + (' ' * (flag + 7) + '\\') + "\n"
        str = str + (' ' * (flag + 8) + '\\') + "\n"

        char_lines = Meow.split('\n')
        char_lines = [i for i in char_lines if len(i) != 0]

        for i in char_lines:
            str = str + (' ' * (flag + 5) + i) + "\n"

    except:
        str = str + ("```Can't Say...!! Give something much more easier to Mr.Meow...")
    return str + "```"


def milk(args):
    str = ""
    try:

        str = str + string_processing(args) + "\n"
        flag = flg[-1]

        str = str + (' ' * (flag + 5) + '\\') + "\n"
        str = str + (' ' * (flag + 6) + '\\') + "\n"
        str = str + (' ' * (flag + 7) + '\\') + "\n"
        str = str + (' ' * (flag + 8) + '\\') + "\n"

        char_lines = Milk.split('\n')
        char_lines = [i for i in char_lines if len(i) != 0]

        for i in char_lines:
            str = str + (' ' * (flag + 5) + i) + "\n"

    except:
        str = ("```Can't Say...!! Give something much more easier to Mr.Milk...")
    return str + "```"


def pig(args):
    str = ""
    try:

        str = str + string_processing(args) + "\n"
        flag = flg[-1]

        str = str +(' ' * (flag + 5) + '\\') + "\n"
        str = str + (' ' * (flag + 6) + '\\') + "\n"
        str = str + (' ' * (flag + 7) + '\\') + "\n"
        str = str + (' ' * (flag + 8) + '\\') + "\n"

        char_lines = Pig.split('\n')
        char_lines = [i for i in char_lines if len(i) != 0]

        for i in char_lines:
            str = str + (' ' * (flag + 5) + i) + "\n"

    except:
        str = ("```Can't Say...!! Give something much more easier to Mr.Pig...")
    return str + "```"


def stegosaurus(args):
    str = ""
    try:

        str = string_processing(args) + "\n"
        flag = flg[-1]

        str = str + (' ' * (flag + 5) + '\\') + "\n"
        str = str + (' ' * (flag + 6) + '\\') + "\n"
        str = str + (' ' * (flag + 7) + '\\') + "\n"
        str = str + (' ' * (flag + 8) + '\\') + "\n"

        char_lines = Stegosaurus.split('\n')
        char_lines = [i for i in char_lines if len(i) != 0]

        for i in char_lines:
            str = str + (' ' * (flag - 3) + i) + "\n"

    except:
        str = ("```Can't Say...!! Give something much more easier to"
              "Mr.stegosaurus...")
    return str + "```"


def stimpy(args):
    str = ""
    try:

        str = str + string_processing(args) + "\n"
        flag = flg[-1]

        str = str + (' ' * (flag + 5) + '\\') + "\n"
        str = str + (' ' * (flag + 6) + '\\') + "\n"
        str = str + (' ' * (flag + 7) + '\\') + "\n"
        str = str + (' ' * (flag + 8) + '\\') + "\n"

        char_lines = Stimpy.split('\n')
        char_lines = [i for i in char_lines if len(i) != 0]

        for i in char_lines:
            str = str + (' ' * (flag + 4) + i) + "\n"

    except:
        str = ("```Can't Say...!! Give something much more easier to Mr.Stimpy...")
    return str + "```"


def turkey(args):
    str = ""
    try:

        str = str + string_processing(args) + "\n"
        flag = flg[-1]

        str = str + (' ' * (flag + 5) + '\\') + "\n"
        str = str + (' ' * (flag + 6) + '\\') + "\n"
        str = str + (' ' * (flag + 7) + '\\') + "\n"
        str = str + (' ' * (flag + 8) + '\\') + "\n"

        char_lines = Turkey.split('\n')
        char_lines = [i for i in char_lines if len(i) != 0]

        for i in char_lines:
            str = str + (' ' * (flag - 3) + i) + "\n"

    except:
        str = ("```Can't Say...!! Give something much more easier to Mr.Turkey...")
    return str + "```"


def turtle(args):
    str = ""
    try:
        str = str + string_processing(args) + "\n"
        flag = flg[-1]

        str = str + (' ' * (flag + 5) + '\\') + "\n"
        str = str + (' ' * (flag + 6) + '\\') + "\n"
        str = str + (' ' * (flag + 7) + '\\') + "\n"
        str = str + (' ' * (flag + 8) + '\\') + "\n"

        char_lines = Turtle.split('\n')
        char_lines = [i for i in char_lines if len(i) != 0]

        for i in char_lines:
            str = str + (' ' * (flag - 3) + i) + "\n"

    except:
        str = ("```Can't Say...!! Give something much more easier to Mr.Turtle...")
    return str + "```"


def tux(args):
    return_str = ""
    return_str = return_str + string_processing(args) + "\n"
    flag = flg[-1]

    return_str = return_str + (' ' * (flag + 5) + '\\') + "\n"
    return_str = return_str + (' ' * (flag + 6) + '\\') + "\n"
    return_str = return_str + (' ' * (flag + 7) + '\\') + "\n"
    # return_str = return_str + str(' ' * (flag + 7) + '\\', end='') + "\n"

    char_lines = Tux.split('\n')
    char_lines = [i for i in char_lines if len(i) != 0]

    for i in char_lines:
        return_str = return_str + (' ' * flag + i) + "\n"
    return return_str + "```"


# %%

chars = [beavis, cheese, daemon, cow, dragon, ghostbusters, kitty, meow, milk,
         pig, stegosaurus, stimpy, turkey, turtle, tux]

char_names = ['beavis', 'cheese', 'daemon', 'cow', 'dragon', 'ghostbusters',
              'kitty', 'meow', 'milk', 'pig', 'stegosaurus', 'stimpy',
              'turkey', 'turtle', 'tux']


def cli():
    if '--version' in sys.argv[1:]:
        print(__version__)
        exit(0)

    cow(' '.join(sys.argv[1:]))
