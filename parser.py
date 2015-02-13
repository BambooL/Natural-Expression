from lexer import my_lexer
from rply import ParserGenerator

pg = ParserGenerator(["NUMBER", "LET", "BE", "EVAL"],
        precedence=[("left", ['PLUS', 'MINUS'])], cache_id="myparser")

