from lexer import *
from parser import Parser
from simulator import Simulator


def main():
    filename = 'test/test_if.pas'
    token_list = Lexer(filename).scan()
    # print(token_list) # test and shoe the result
    instruction_list = Parser(token_list).start_parser()
    # print(instruction_list)  #test and show the result
    Simulator(instruction_list).simulator()


main()
