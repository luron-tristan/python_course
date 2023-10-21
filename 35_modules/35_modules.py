# module = file containing python code. May contain function, classes, etc
# used with modular programming, which is to separate a program into parts

from messages import hello, bye
import messages as msg
# from messages import * # not recommended => naming conflicts

msg.hello()
msg.bye()

hello()
bye()

help('modules')
