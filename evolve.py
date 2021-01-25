from lexer import Lexer
from parse import Parse
from evaluator import Evaluator
import logging
import os
import json

logger = logging.getLogger('ghpl_interpreter')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='./ghpl_logs/ghpl_interpreter.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

try:
    os.mkdir("ghpl_cache")
except OSError:
    logger.debug("Creation of the directory ghpl_cache failed")
else:
    logger.debug("Successfully created the directory ghpl_cache")

def main():

    f = open ('project.json', "r") 
    json_data = json.loads(f.read())   
    logger.debug(json_data)
    f.close()

    filename = json_data['main_file'] + '.ghpl'
    file     = open(filename, "r")
    lexer    = Lexer(file)
    parser   = Parse(lexer.tokens)

    logger.debug(filename)
    logger.debug(file)
    logger.debug(lexer)
    logger.debug(parser)

    lexer.tokenizer()
    #print("TOKENS:")
    #print(lexer.tokens, "\n")
    logger.debug(lexer.tokens)

    parser.build_AST()
    #print("AST:")
    #print(parser.AST, "\n")
    logger.debug(parser.AST)

    evaluator = Evaluator(parser.AST)

    #print("OUTPUT:")
    evaluator.run(parser.AST)
    logger.debug(evaluator.run(parser.AST))

if __name__ == "__main__":
    main()
