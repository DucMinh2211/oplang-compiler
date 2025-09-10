# Generated from /Users/nongthithuykieu/projects/oplang-compiler/src/grammar/OPLang.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,73,454,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,114,8,1,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,3,1,3,1,3,3,3,126,8,3,1,4,1,4,1,4,1,4,3,4,132,8,4,1,5,1,5,
        1,5,1,5,3,5,138,8,5,1,6,1,6,3,6,142,8,6,1,7,1,7,1,7,1,7,1,7,1,8,
        1,8,1,8,1,8,1,8,3,8,154,8,8,1,9,1,9,3,9,158,8,9,1,10,1,10,1,10,1,
        10,3,10,164,8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,
        12,3,12,176,8,12,1,13,1,13,1,13,1,13,1,13,3,13,183,8,13,1,14,1,14,
        1,14,1,14,1,15,1,15,1,15,1,15,3,15,193,8,15,1,16,1,16,3,16,197,8,
        16,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,
        19,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,
        21,1,21,1,21,1,21,3,21,228,8,21,1,22,1,22,1,22,1,22,1,22,3,22,235,
        8,22,1,23,1,23,1,23,1,23,1,23,1,23,5,23,243,8,23,10,23,12,23,246,
        9,23,1,24,1,24,1,24,1,24,1,24,1,24,5,24,254,8,24,10,24,12,24,257,
        9,24,1,25,1,25,1,25,1,25,1,25,1,25,5,25,265,8,25,10,25,12,25,268,
        9,25,1,26,1,26,1,26,1,26,1,26,1,26,5,26,276,8,26,10,26,12,26,279,
        9,26,1,27,1,27,1,27,3,27,284,8,27,1,28,1,28,1,28,3,28,289,8,28,1,
        29,1,29,1,29,1,29,1,29,5,29,296,8,29,10,29,12,29,299,9,29,1,30,1,
        30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,31,1,31,3,31,312,8,31,5,
        31,314,8,31,10,31,12,31,317,9,31,1,32,1,32,1,32,1,32,1,32,1,32,1,
        32,1,32,1,32,1,32,1,32,3,32,330,8,32,1,33,1,33,1,33,1,33,1,33,1,
        33,1,34,1,34,3,34,340,8,34,1,35,1,35,1,35,1,35,1,35,3,35,347,8,35,
        1,36,1,36,1,36,1,36,1,36,1,37,1,37,1,37,1,37,1,37,1,38,1,38,1,38,
        1,38,3,38,363,8,38,1,39,1,39,1,39,1,39,3,39,369,8,39,1,40,1,40,1,
        40,1,40,1,40,1,41,1,41,1,41,1,41,1,41,1,41,1,41,1,41,1,41,1,41,3,
        41,386,8,41,1,42,1,42,1,42,1,42,1,42,1,43,1,43,1,43,3,43,396,8,43,
        1,44,1,44,1,44,1,44,1,44,1,44,1,44,3,44,405,8,44,1,45,1,45,1,45,
        1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,46,1,46,1,46,1,47,1,47,
        1,47,1,48,1,48,1,48,1,48,1,48,1,48,3,48,430,8,48,1,49,1,49,1,49,
        3,49,435,8,49,1,50,1,50,1,51,1,51,1,51,1,51,5,51,443,8,51,10,51,
        12,51,446,9,51,3,51,448,8,51,1,51,1,51,1,52,1,52,1,52,0,6,46,48,
        50,52,58,62,53,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,
        80,82,84,86,88,90,92,94,96,98,100,102,104,0,3,2,0,12,12,32,32,1,
        0,35,36,1,0,67,70,448,0,106,1,0,0,0,2,113,1,0,0,0,4,115,1,0,0,0,
        6,125,1,0,0,0,8,131,1,0,0,0,10,137,1,0,0,0,12,141,1,0,0,0,14,143,
        1,0,0,0,16,153,1,0,0,0,18,157,1,0,0,0,20,163,1,0,0,0,22,165,1,0,
        0,0,24,175,1,0,0,0,26,182,1,0,0,0,28,184,1,0,0,0,30,192,1,0,0,0,
        32,196,1,0,0,0,34,198,1,0,0,0,36,203,1,0,0,0,38,210,1,0,0,0,40,216,
        1,0,0,0,42,227,1,0,0,0,44,234,1,0,0,0,46,236,1,0,0,0,48,247,1,0,
        0,0,50,258,1,0,0,0,52,269,1,0,0,0,54,283,1,0,0,0,56,288,1,0,0,0,
        58,290,1,0,0,0,60,300,1,0,0,0,62,304,1,0,0,0,64,329,1,0,0,0,66,331,
        1,0,0,0,68,339,1,0,0,0,70,346,1,0,0,0,72,348,1,0,0,0,74,353,1,0,
        0,0,76,362,1,0,0,0,78,368,1,0,0,0,80,370,1,0,0,0,82,385,1,0,0,0,
        84,387,1,0,0,0,86,395,1,0,0,0,88,397,1,0,0,0,90,406,1,0,0,0,92,417,
        1,0,0,0,94,420,1,0,0,0,96,429,1,0,0,0,98,434,1,0,0,0,100,436,1,0,
        0,0,102,438,1,0,0,0,104,451,1,0,0,0,106,107,3,2,1,0,107,108,5,0,
        0,1,108,1,1,0,0,0,109,110,3,4,2,0,110,111,3,2,1,0,111,114,1,0,0,
        0,112,114,3,4,2,0,113,109,1,0,0,0,113,112,1,0,0,0,114,3,1,0,0,0,
        115,116,5,15,0,0,116,117,5,12,0,0,117,118,3,6,3,0,118,119,5,59,0,
        0,119,120,3,8,4,0,120,121,5,60,0,0,121,5,1,0,0,0,122,123,5,19,0,
        0,123,126,5,12,0,0,124,126,1,0,0,0,125,122,1,0,0,0,125,124,1,0,0,
        0,126,7,1,0,0,0,127,128,3,10,5,0,128,129,3,8,4,0,129,132,1,0,0,0,
        130,132,1,0,0,0,131,127,1,0,0,0,131,130,1,0,0,0,132,9,1,0,0,0,133,
        134,3,12,6,0,134,135,3,14,7,0,135,138,1,0,0,0,136,138,3,22,11,0,
        137,133,1,0,0,0,137,136,1,0,0,0,138,11,1,0,0,0,139,142,5,34,0,0,
        140,142,1,0,0,0,141,139,1,0,0,0,141,140,1,0,0,0,142,13,1,0,0,0,143,
        144,3,18,9,0,144,145,3,98,49,0,145,146,3,16,8,0,146,147,5,61,0,0,
        147,15,1,0,0,0,148,149,3,20,10,0,149,150,5,64,0,0,150,151,3,16,8,
        0,151,154,1,0,0,0,152,154,3,20,10,0,153,148,1,0,0,0,153,152,1,0,
        0,0,154,17,1,0,0,0,155,158,5,33,0,0,156,158,1,0,0,0,157,155,1,0,
        0,0,157,156,1,0,0,0,158,19,1,0,0,0,159,160,5,12,0,0,160,161,5,50,
        0,0,161,164,3,104,52,0,162,164,5,12,0,0,163,159,1,0,0,0,163,162,
        1,0,0,0,164,21,1,0,0,0,165,166,3,98,49,0,166,167,3,32,16,0,167,168,
        5,12,0,0,168,169,5,57,0,0,169,170,3,24,12,0,170,171,5,58,0,0,171,
        172,3,74,37,0,172,23,1,0,0,0,173,176,3,26,13,0,174,176,1,0,0,0,175,
        173,1,0,0,0,175,174,1,0,0,0,176,25,1,0,0,0,177,178,3,28,14,0,178,
        179,5,61,0,0,179,180,3,26,13,0,180,183,1,0,0,0,181,183,1,0,0,0,182,
        177,1,0,0,0,182,181,1,0,0,0,183,27,1,0,0,0,184,185,3,98,49,0,185,
        186,3,32,16,0,186,187,3,30,15,0,187,29,1,0,0,0,188,189,5,12,0,0,
        189,190,5,64,0,0,190,193,3,30,15,0,191,193,5,12,0,0,192,188,1,0,
        0,0,192,191,1,0,0,0,193,31,1,0,0,0,194,197,5,66,0,0,195,197,1,0,
        0,0,196,194,1,0,0,0,196,195,1,0,0,0,197,33,1,0,0,0,198,199,5,12,
        0,0,199,200,5,57,0,0,200,201,5,58,0,0,201,202,3,74,37,0,202,35,1,
        0,0,0,203,204,5,12,0,0,204,205,5,57,0,0,205,206,5,12,0,0,206,207,
        5,1,0,0,207,208,5,58,0,0,208,209,3,74,37,0,209,37,1,0,0,0,210,211,
        5,12,0,0,211,212,5,57,0,0,212,213,3,24,12,0,213,214,5,58,0,0,214,
        215,3,74,37,0,215,39,1,0,0,0,216,217,5,65,0,0,217,218,5,12,0,0,218,
        219,5,57,0,0,219,220,5,58,0,0,220,221,3,74,37,0,221,41,1,0,0,0,222,
        223,3,44,22,0,223,224,5,2,0,0,224,225,3,44,22,0,225,228,1,0,0,0,
        226,228,3,44,22,0,227,222,1,0,0,0,227,226,1,0,0,0,228,43,1,0,0,0,
        229,230,3,46,23,0,230,231,5,3,0,0,231,232,3,46,23,0,232,235,1,0,
        0,0,233,235,3,46,23,0,234,229,1,0,0,0,234,233,1,0,0,0,235,45,1,0,
        0,0,236,237,6,23,-1,0,237,238,3,48,24,0,238,244,1,0,0,0,239,240,
        10,2,0,0,240,241,5,4,0,0,241,243,3,48,24,0,242,239,1,0,0,0,243,246,
        1,0,0,0,244,242,1,0,0,0,244,245,1,0,0,0,245,47,1,0,0,0,246,244,1,
        0,0,0,247,248,6,24,-1,0,248,249,3,50,25,0,249,255,1,0,0,0,250,251,
        10,2,0,0,251,252,5,5,0,0,252,254,3,50,25,0,253,250,1,0,0,0,254,257,
        1,0,0,0,255,253,1,0,0,0,255,256,1,0,0,0,256,49,1,0,0,0,257,255,1,
        0,0,0,258,259,6,25,-1,0,259,260,3,52,26,0,260,266,1,0,0,0,261,262,
        10,2,0,0,262,263,5,6,0,0,263,265,3,52,26,0,264,261,1,0,0,0,265,268,
        1,0,0,0,266,264,1,0,0,0,266,267,1,0,0,0,267,51,1,0,0,0,268,266,1,
        0,0,0,269,270,6,26,-1,0,270,271,3,54,27,0,271,277,1,0,0,0,272,273,
        10,2,0,0,273,274,5,7,0,0,274,276,3,54,27,0,275,272,1,0,0,0,276,279,
        1,0,0,0,277,275,1,0,0,0,277,278,1,0,0,0,278,53,1,0,0,0,279,277,1,
        0,0,0,280,281,5,53,0,0,281,284,3,54,27,0,282,284,3,56,28,0,283,280,
        1,0,0,0,283,282,1,0,0,0,284,55,1,0,0,0,285,286,5,8,0,0,286,289,3,
        56,28,0,287,289,3,58,29,0,288,285,1,0,0,0,288,287,1,0,0,0,289,57,
        1,0,0,0,290,291,6,29,-1,0,291,292,3,62,31,0,292,297,1,0,0,0,293,
        294,10,2,0,0,294,296,3,60,30,0,295,293,1,0,0,0,296,299,1,0,0,0,297,
        295,1,0,0,0,297,298,1,0,0,0,298,59,1,0,0,0,299,297,1,0,0,0,300,301,
        5,55,0,0,301,302,3,42,21,0,302,303,5,56,0,0,303,61,1,0,0,0,304,305,
        6,31,-1,0,305,306,3,64,32,0,306,315,1,0,0,0,307,308,10,2,0,0,308,
        311,5,63,0,0,309,312,3,72,36,0,310,312,5,12,0,0,311,309,1,0,0,0,
        311,310,1,0,0,0,312,314,1,0,0,0,313,307,1,0,0,0,314,317,1,0,0,0,
        315,313,1,0,0,0,315,316,1,0,0,0,316,63,1,0,0,0,317,315,1,0,0,0,318,
        330,3,100,50,0,319,330,5,12,0,0,320,330,5,32,0,0,321,330,5,31,0,
        0,322,330,3,72,36,0,323,330,3,66,33,0,324,330,5,32,0,0,325,326,5,
        57,0,0,326,327,3,42,21,0,327,328,5,58,0,0,328,330,1,0,0,0,329,318,
        1,0,0,0,329,319,1,0,0,0,329,320,1,0,0,0,329,321,1,0,0,0,329,322,
        1,0,0,0,329,323,1,0,0,0,329,324,1,0,0,0,329,325,1,0,0,0,330,65,1,
        0,0,0,331,332,5,23,0,0,332,333,5,12,0,0,333,334,5,57,0,0,334,335,
        3,68,34,0,335,336,5,58,0,0,336,67,1,0,0,0,337,340,3,70,35,0,338,
        340,1,0,0,0,339,337,1,0,0,0,339,338,1,0,0,0,340,69,1,0,0,0,341,342,
        3,42,21,0,342,343,5,64,0,0,343,344,3,70,35,0,344,347,1,0,0,0,345,
        347,3,42,21,0,346,341,1,0,0,0,346,345,1,0,0,0,347,71,1,0,0,0,348,
        349,7,0,0,0,349,350,5,57,0,0,350,351,3,68,34,0,351,352,5,58,0,0,
        352,73,1,0,0,0,353,354,5,59,0,0,354,355,3,78,39,0,355,356,3,76,38,
        0,356,357,5,60,0,0,357,75,1,0,0,0,358,359,3,82,41,0,359,360,3,76,
        38,0,360,363,1,0,0,0,361,363,1,0,0,0,362,358,1,0,0,0,362,361,1,0,
        0,0,363,77,1,0,0,0,364,365,3,80,40,0,365,366,3,78,39,0,366,369,1,
        0,0,0,367,369,1,0,0,0,368,364,1,0,0,0,368,367,1,0,0,0,369,79,1,0,
        0,0,370,371,3,18,9,0,371,372,3,98,49,0,372,373,3,30,15,0,373,374,
        5,61,0,0,374,81,1,0,0,0,375,386,3,84,42,0,376,386,3,88,44,0,377,
        386,3,90,45,0,378,386,3,92,46,0,379,386,3,94,47,0,380,386,3,96,48,
        0,381,382,3,72,36,0,382,383,5,61,0,0,383,386,1,0,0,0,384,386,3,74,
        37,0,385,375,1,0,0,0,385,376,1,0,0,0,385,377,1,0,0,0,385,378,1,0,
        0,0,385,379,1,0,0,0,385,380,1,0,0,0,385,381,1,0,0,0,385,384,1,0,
        0,0,386,83,1,0,0,0,387,388,3,86,43,0,388,389,5,49,0,0,389,390,3,
        42,21,0,390,391,5,61,0,0,391,85,1,0,0,0,392,396,5,12,0,0,393,394,
        5,12,0,0,394,396,3,60,30,0,395,392,1,0,0,0,395,393,1,0,0,0,396,87,
        1,0,0,0,397,398,5,21,0,0,398,399,3,42,21,0,399,400,5,25,0,0,400,
        404,3,82,41,0,401,402,5,18,0,0,402,405,3,82,41,0,403,405,1,0,0,0,
        404,401,1,0,0,0,404,403,1,0,0,0,405,89,1,0,0,0,406,407,5,26,0,0,
        407,408,5,12,0,0,408,409,5,49,0,0,409,410,3,42,21,0,410,411,5,57,
        0,0,411,412,7,1,0,0,412,413,3,42,21,0,413,414,5,58,0,0,414,415,5,
        17,0,0,415,416,3,82,41,0,416,91,1,0,0,0,417,418,5,14,0,0,418,419,
        5,61,0,0,419,93,1,0,0,0,420,421,5,16,0,0,421,422,5,61,0,0,422,95,
        1,0,0,0,423,424,5,27,0,0,424,425,3,42,21,0,425,426,5,61,0,0,426,
        430,1,0,0,0,427,428,5,27,0,0,428,430,5,61,0,0,429,423,1,0,0,0,429,
        427,1,0,0,0,430,97,1,0,0,0,431,435,3,100,50,0,432,435,5,12,0,0,433,
        435,5,30,0,0,434,431,1,0,0,0,434,432,1,0,0,0,434,433,1,0,0,0,435,
        99,1,0,0,0,436,437,7,2,0,0,437,101,1,0,0,0,438,447,5,59,0,0,439,
        444,3,104,52,0,440,441,5,64,0,0,441,443,3,104,52,0,442,440,1,0,0,
        0,443,446,1,0,0,0,444,442,1,0,0,0,444,445,1,0,0,0,445,448,1,0,0,
        0,446,444,1,0,0,0,447,439,1,0,0,0,447,448,1,0,0,0,448,449,1,0,0,
        0,449,450,5,60,0,0,450,103,1,0,0,0,451,452,7,2,0,0,452,105,1,0,0,
        0,35,113,125,131,137,141,153,157,163,175,182,192,196,227,234,244,
        255,266,277,283,288,297,311,315,329,339,346,362,368,385,395,404,
        429,434,444,447
    ]

class OPLangParser ( Parser ):

    grammarFileName = "OPLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'other'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'boolean'", "'break'", "'class'", "'continue'", "'do'", 
                     "'else'", "'extends'", "'float'", "'if'", "'int'", 
                     "'new'", "'string'", "'then'", "'for'", "'return'", 
                     "'true'", "'false'", "'void'", "'nil'", "'this'", "'final'", 
                     "'static'", "'to'", "'downto'", "'+'", "'-'", "'*'", 
                     "'/'", "'\\'", "'%'", "'!='", "'=='", "'<'", "'>'", 
                     "'<='", "'>='", "':='", "'='", "'||'", "'&&'", "'!'", 
                     "'^'", "'['", "']'", "'('", "')'", "'{'", "'}'", "';'", 
                     "':'", "'.'", "','", "'~'", "'&'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "CMP_WITH_OP", "CMP_OP", 
                      "AND_OR_OP", "ADD_SUB_BINOP", "MUL_DIV_MOD_OP", "STR_CONCAT_OP", 
                      "ADD_SUB_UNOP", "WS", "COMMENT_LINE", "COMMENT_BLOCK", 
                      "ID", "BOOLEAN", "BREAK", "CLASS", "CONTINUE", "DO", 
                      "ELSE", "EXTENDS", "FLOAT", "IF", "INT", "NEW", "STRING", 
                      "THEN", "FOR", "RETURN", "TRUE", "FALSE", "VOID", 
                      "NIL", "THIS", "FINAL", "STATIC", "TO", "DOWNTO", 
                      "PLUS", "MINUS", "MULTIPLY", "FLOAT_DIVISION", "INTEGER_DIVISION", 
                      "MODULO", "NOT_EQUAL", "EQUAL", "LESS_THAN", "GREATER_THAN", 
                      "LESS_THAN_OR_EQUAL", "GREATER_THAN_OR_EQUAL", "ASSIGN", 
                      "MEMBER_ASSIGN", "LOGICAL_OR", "LOGICAL_AND", "NOT", 
                      "STR_CONCAT", "LBRACKET", "RBRACKET", "LPAREN", "RPAREN", 
                      "LBRACE", "RBRACE", "SEMI", "COLON", "DOT", "COMMA", 
                      "TILDE", "AMPERSAND", "INTEGER_LITERAL", "FLOAT_LITERAL", 
                      "BOOLEAN_LITERAL", "STRING_LITERAL", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_class_decl_list = 1
    RULE_class_decl = 2
    RULE_class_extends = 3
    RULE_member_nulist = 4
    RULE_member = 5
    RULE_is_static = 6
    RULE_attribute_decl = 7
    RULE_attribute_name_list = 8
    RULE_is_final = 9
    RULE_attribute_name = 10
    RULE_method_decl = 11
    RULE_param_nulist = 12
    RULE_param_prime = 13
    RULE_param = 14
    RULE_id_list = 15
    RULE_is_ref = 16
    RULE_def_constructor = 17
    RULE_copy_constructor = 18
    RULE_custom_constructor = 19
    RULE_destructor = 20
    RULE_expr0 = 21
    RULE_expr1 = 22
    RULE_expr2 = 23
    RULE_expr3 = 24
    RULE_expr4 = 25
    RULE_expr5 = 26
    RULE_expr6 = 27
    RULE_expr7 = 28
    RULE_expr8 = 29
    RULE_array_access = 30
    RULE_expr9 = 31
    RULE_fact = 32
    RULE_obj_creation = 33
    RULE_expr_nulist = 34
    RULE_expr_prime = 35
    RULE_method_invocation = 36
    RULE_block_statement = 37
    RULE_stmt_nulist = 38
    RULE_var_decl_nulist = 39
    RULE_var_decl = 40
    RULE_stmt = 41
    RULE_assign_stmt = 42
    RULE_lhs = 43
    RULE_if_stmt = 44
    RULE_for_stmt = 45
    RULE_break_stmt = 46
    RULE_continue_stmt = 47
    RULE_return_stmt = 48
    RULE_type = 49
    RULE_literals = 50
    RULE_array_literal = 51
    RULE_value = 52

    ruleNames =  [ "program", "class_decl_list", "class_decl", "class_extends", 
                   "member_nulist", "member", "is_static", "attribute_decl", 
                   "attribute_name_list", "is_final", "attribute_name", 
                   "method_decl", "param_nulist", "param_prime", "param", 
                   "id_list", "is_ref", "def_constructor", "copy_constructor", 
                   "custom_constructor", "destructor", "expr0", "expr1", 
                   "expr2", "expr3", "expr4", "expr5", "expr6", "expr7", 
                   "expr8", "array_access", "expr9", "fact", "obj_creation", 
                   "expr_nulist", "expr_prime", "method_invocation", "block_statement", 
                   "stmt_nulist", "var_decl_nulist", "var_decl", "stmt", 
                   "assign_stmt", "lhs", "if_stmt", "for_stmt", "break_stmt", 
                   "continue_stmt", "return_stmt", "type", "literals", "array_literal", 
                   "value" ]

    EOF = Token.EOF
    T__0=1
    CMP_WITH_OP=2
    CMP_OP=3
    AND_OR_OP=4
    ADD_SUB_BINOP=5
    MUL_DIV_MOD_OP=6
    STR_CONCAT_OP=7
    ADD_SUB_UNOP=8
    WS=9
    COMMENT_LINE=10
    COMMENT_BLOCK=11
    ID=12
    BOOLEAN=13
    BREAK=14
    CLASS=15
    CONTINUE=16
    DO=17
    ELSE=18
    EXTENDS=19
    FLOAT=20
    IF=21
    INT=22
    NEW=23
    STRING=24
    THEN=25
    FOR=26
    RETURN=27
    TRUE=28
    FALSE=29
    VOID=30
    NIL=31
    THIS=32
    FINAL=33
    STATIC=34
    TO=35
    DOWNTO=36
    PLUS=37
    MINUS=38
    MULTIPLY=39
    FLOAT_DIVISION=40
    INTEGER_DIVISION=41
    MODULO=42
    NOT_EQUAL=43
    EQUAL=44
    LESS_THAN=45
    GREATER_THAN=46
    LESS_THAN_OR_EQUAL=47
    GREATER_THAN_OR_EQUAL=48
    ASSIGN=49
    MEMBER_ASSIGN=50
    LOGICAL_OR=51
    LOGICAL_AND=52
    NOT=53
    STR_CONCAT=54
    LBRACKET=55
    RBRACKET=56
    LPAREN=57
    RPAREN=58
    LBRACE=59
    RBRACE=60
    SEMI=61
    COLON=62
    DOT=63
    COMMA=64
    TILDE=65
    AMPERSAND=66
    INTEGER_LITERAL=67
    FLOAT_LITERAL=68
    BOOLEAN_LITERAL=69
    STRING_LITERAL=70
    ILLEGAL_ESCAPE=71
    UNCLOSE_STRING=72
    ERROR_CHAR=73

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_decl_list(self):
            return self.getTypedRuleContext(OPLangParser.Class_decl_listContext,0)


        def EOF(self):
            return self.getToken(OPLangParser.EOF, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_program




    def program(self):

        localctx = OPLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.class_decl_list()
            self.state = 107
            self.match(OPLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_decl(self):
            return self.getTypedRuleContext(OPLangParser.Class_declContext,0)


        def class_decl_list(self):
            return self.getTypedRuleContext(OPLangParser.Class_decl_listContext,0)


        def getRuleIndex(self):
            return OPLangParser.RULE_class_decl_list




    def class_decl_list(self):

        localctx = OPLangParser.Class_decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_decl_list)
        try:
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.class_decl()
                self.state = 110
                self.class_decl_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                self.class_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(OPLangParser.CLASS, 0)

        def ID(self):
            return self.getToken(OPLangParser.ID, 0)

        def class_extends(self):
            return self.getTypedRuleContext(OPLangParser.Class_extendsContext,0)


        def LBRACE(self):
            return self.getToken(OPLangParser.LBRACE, 0)

        def member_nulist(self):
            return self.getTypedRuleContext(OPLangParser.Member_nulistContext,0)


        def RBRACE(self):
            return self.getToken(OPLangParser.RBRACE, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_class_decl




    def class_decl(self):

        localctx = OPLangParser.Class_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(OPLangParser.CLASS)
            self.state = 116
            self.match(OPLangParser.ID)
            self.state = 117
            self.class_extends()
            self.state = 118
            self.match(OPLangParser.LBRACE)
            self.state = 119
            self.member_nulist()
            self.state = 120
            self.match(OPLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_extendsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXTENDS(self):
            return self.getToken(OPLangParser.EXTENDS, 0)

        def ID(self):
            return self.getToken(OPLangParser.ID, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_class_extends




    def class_extends(self):

        localctx = OPLangParser.Class_extendsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_class_extends)
        try:
            self.state = 125
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self.match(OPLangParser.EXTENDS)
                self.state = 123
                self.match(OPLangParser.ID)
                pass
            elif token in [59]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_nulistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member(self):
            return self.getTypedRuleContext(OPLangParser.MemberContext,0)


        def member_nulist(self):
            return self.getTypedRuleContext(OPLangParser.Member_nulistContext,0)


        def getRuleIndex(self):
            return OPLangParser.RULE_member_nulist




    def member_nulist(self):

        localctx = OPLangParser.Member_nulistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_member_nulist)
        try:
            self.state = 131
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12, 30, 33, 34, 67, 68, 69, 70]:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.member()
                self.state = 128
                self.member_nulist()
                pass
            elif token in [60]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def is_static(self):
            return self.getTypedRuleContext(OPLangParser.Is_staticContext,0)


        def attribute_decl(self):
            return self.getTypedRuleContext(OPLangParser.Attribute_declContext,0)


        def method_decl(self):
            return self.getTypedRuleContext(OPLangParser.Method_declContext,0)


        def getRuleIndex(self):
            return OPLangParser.RULE_member




    def member(self):

        localctx = OPLangParser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_member)
        try:
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.is_static()
                self.state = 134
                self.attribute_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.method_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Is_staticContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATIC(self):
            return self.getToken(OPLangParser.STATIC, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_is_static




    def is_static(self):

        localctx = OPLangParser.Is_staticContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_is_static)
        try:
            self.state = 141
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.match(OPLangParser.STATIC)
                pass
            elif token in [12, 30, 33, 67, 68, 69, 70]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def is_final(self):
            return self.getTypedRuleContext(OPLangParser.Is_finalContext,0)


        def type_(self):
            return self.getTypedRuleContext(OPLangParser.TypeContext,0)


        def attribute_name_list(self):
            return self.getTypedRuleContext(OPLangParser.Attribute_name_listContext,0)


        def SEMI(self):
            return self.getToken(OPLangParser.SEMI, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_attribute_decl




    def attribute_decl(self):

        localctx = OPLangParser.Attribute_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attribute_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.is_final()
            self.state = 144
            self.type_()
            self.state = 145
            self.attribute_name_list()
            self.state = 146
            self.match(OPLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_name_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_name(self):
            return self.getTypedRuleContext(OPLangParser.Attribute_nameContext,0)


        def COMMA(self):
            return self.getToken(OPLangParser.COMMA, 0)

        def attribute_name_list(self):
            return self.getTypedRuleContext(OPLangParser.Attribute_name_listContext,0)


        def getRuleIndex(self):
            return OPLangParser.RULE_attribute_name_list




    def attribute_name_list(self):

        localctx = OPLangParser.Attribute_name_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attribute_name_list)
        try:
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.attribute_name()
                self.state = 149
                self.match(OPLangParser.COMMA)
                self.state = 150
                self.attribute_name_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.attribute_name()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Is_finalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FINAL(self):
            return self.getToken(OPLangParser.FINAL, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_is_final




    def is_final(self):

        localctx = OPLangParser.Is_finalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_is_final)
        try:
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.match(OPLangParser.FINAL)
                pass
            elif token in [12, 30, 67, 68, 69, 70]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(OPLangParser.ID, 0)

        def MEMBER_ASSIGN(self):
            return self.getToken(OPLangParser.MEMBER_ASSIGN, 0)

        def value(self):
            return self.getTypedRuleContext(OPLangParser.ValueContext,0)


        def getRuleIndex(self):
            return OPLangParser.RULE_attribute_name




    def attribute_name(self):

        localctx = OPLangParser.Attribute_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_attribute_name)
        try:
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.match(OPLangParser.ID)
                self.state = 160
                self.match(OPLangParser.MEMBER_ASSIGN)
                self.state = 161
                self.value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.match(OPLangParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(OPLangParser.TypeContext,0)


        def is_ref(self):
            return self.getTypedRuleContext(OPLangParser.Is_refContext,0)


        def ID(self):
            return self.getToken(OPLangParser.ID, 0)

        def LPAREN(self):
            return self.getToken(OPLangParser.LPAREN, 0)

        def param_nulist(self):
            return self.getTypedRuleContext(OPLangParser.Param_nulistContext,0)


        def RPAREN(self):
            return self.getToken(OPLangParser.RPAREN, 0)

        def block_statement(self):
            return self.getTypedRuleContext(OPLangParser.Block_statementContext,0)


        def getRuleIndex(self):
            return OPLangParser.RULE_method_decl




    def method_decl(self):

        localctx = OPLangParser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_method_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.type_()
            self.state = 166
            self.is_ref()
            self.state = 167
            self.match(OPLangParser.ID)
            self.state = 168
            self.match(OPLangParser.LPAREN)
            self.state = 169
            self.param_nulist()
            self.state = 170
            self.match(OPLangParser.RPAREN)
            self.state = 171
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_nulistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_prime(self):
            return self.getTypedRuleContext(OPLangParser.Param_primeContext,0)


        def getRuleIndex(self):
            return OPLangParser.RULE_param_nulist




    def param_nulist(self):

        localctx = OPLangParser.Param_nulistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_param_nulist)
        try:
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.param_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(OPLangParser.ParamContext,0)


        def SEMI(self):
            return self.getToken(OPLangParser.SEMI, 0)

        def param_prime(self):
            return self.getTypedRuleContext(OPLangParser.Param_primeContext,0)


        def getRuleIndex(self):
            return OPLangParser.RULE_param_prime




    def param_prime(self):

        localctx = OPLangParser.Param_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_param_prime)
        try:
            self.state = 182
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12, 30, 67, 68, 69, 70]:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.param()
                self.state = 178
                self.match(OPLangParser.SEMI)
                self.state = 179
                self.param_prime()
                pass
            elif token in [58]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(OPLangParser.TypeContext,0)


        def is_ref(self):
            return self.getTypedRuleContext(OPLangParser.Is_refContext,0)


        def id_list(self):
            return self.getTypedRuleContext(OPLangParser.Id_listContext,0)


        def getRuleIndex(self):
            return OPLangParser.RULE_param




    def param(self):

        localctx = OPLangParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.type_()
            self.state = 185
            self.is_ref()
            self.state = 186
            self.id_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(OPLangParser.ID, 0)

        def COMMA(self):
            return self.getToken(OPLangParser.COMMA, 0)

        def id_list(self):
            return self.getTypedRuleContext(OPLangParser.Id_listContext,0)


        def getRuleIndex(self):
            return OPLangParser.RULE_id_list




    def id_list(self):

        localctx = OPLangParser.Id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_id_list)
        try:
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.match(OPLangParser.ID)
                self.state = 189
                self.match(OPLangParser.COMMA)
                self.state = 190
                self.id_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self.match(OPLangParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Is_refContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AMPERSAND(self):
            return self.getToken(OPLangParser.AMPERSAND, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_is_ref




    def is_ref(self):

        localctx = OPLangParser.Is_refContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_is_ref)
        try:
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [66]:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.match(OPLangParser.AMPERSAND)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Def_constructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(OPLangParser.ID, 0)

        def LPAREN(self):
            return self.getToken(OPLangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(OPLangParser.RPAREN, 0)

        def block_statement(self):
            return self.getTypedRuleContext(OPLangParser.Block_statementContext,0)


        def getRuleIndex(self):
            return OPLangParser.RULE_def_constructor




    def def_constructor(self):

        localctx = OPLangParser.Def_constructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_def_constructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(OPLangParser.ID)
            self.state = 199
            self.match(OPLangParser.LPAREN)
            self.state = 200
            self.match(OPLangParser.RPAREN)
            self.state = 201
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Copy_constructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(OPLangParser.ID)
            else:
                return self.getToken(OPLangParser.ID, i)

        def LPAREN(self):
            return self.getToken(OPLangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(OPLangParser.RPAREN, 0)

        def block_statement(self):
            return self.getTypedRuleContext(OPLangParser.Block_statementContext,0)


        def getRuleIndex(self):
            return OPLangParser.RULE_copy_constructor




    def copy_constructor(self):

        localctx = OPLangParser.Copy_constructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_copy_constructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(OPLangParser.ID)
            self.state = 204
            self.match(OPLangParser.LPAREN)
            self.state = 205
            self.match(OPLangParser.ID)
            self.state = 206
            self.match(OPLangParser.T__0)
            self.state = 207
            self.match(OPLangParser.RPAREN)
            self.state = 208
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Custom_constructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(OPLangParser.ID, 0)

        def LPAREN(self):
            return self.getToken(OPLangParser.LPAREN, 0)

        def param_nulist(self):
            return self.getTypedRuleContext(OPLangParser.Param_nulistContext,0)


        def RPAREN(self):
            return self.getToken(OPLangParser.RPAREN, 0)

        def block_statement(self):
            return self.getTypedRuleContext(OPLangParser.Block_statementContext,0)


        def getRuleIndex(self):
            return OPLangParser.RULE_custom_constructor




    def custom_constructor(self):

        localctx = OPLangParser.Custom_constructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_custom_constructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(OPLangParser.ID)
            self.state = 211
            self.match(OPLangParser.LPAREN)
            self.state = 212
            self.param_nulist()
            self.state = 213
            self.match(OPLangParser.RPAREN)
            self.state = 214
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DestructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TILDE(self):
            return self.getToken(OPLangParser.TILDE, 0)

        def ID(self):
            return self.getToken(OPLangParser.ID, 0)

        def LPAREN(self):
            return self.getToken(OPLangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(OPLangParser.RPAREN, 0)

        def block_statement(self):
            return self.getTypedRuleContext(OPLangParser.Block_statementContext,0)


        def getRuleIndex(self):
            return OPLangParser.RULE_destructor




    def destructor(self):

        localctx = OPLangParser.DestructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_destructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(OPLangParser.TILDE)
            self.state = 217
            self.match(OPLangParser.ID)
            self.state = 218
            self.match(OPLangParser.LPAREN)
            self.state = 219
            self.match(OPLangParser.RPAREN)
            self.state = 220
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr0Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OPLangParser.Expr1Context)
            else:
                return self.getTypedRuleContext(OPLangParser.Expr1Context,i)


        def CMP_WITH_OP(self):
            return self.getToken(OPLangParser.CMP_WITH_OP, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_expr0




    def expr0(self):

        localctx = OPLangParser.Expr0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expr0)
        try:
            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                self.expr1()
                self.state = 223
                self.match(OPLangParser.CMP_WITH_OP)
                self.state = 224
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OPLangParser.Expr2Context)
            else:
                return self.getTypedRuleContext(OPLangParser.Expr2Context,i)


        def CMP_OP(self):
            return self.getToken(OPLangParser.CMP_OP, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_expr1




    def expr1(self):

        localctx = OPLangParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_expr1)
        try:
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.expr2(0)
                self.state = 230
                self.match(OPLangParser.CMP_OP)
                self.state = 231
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(OPLangParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(OPLangParser.Expr2Context,0)


        def AND_OR_OP(self):
            return self.getToken(OPLangParser.AND_OR_OP, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_expr2



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OPLangParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 244
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OPLangParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 239
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 240
                    self.match(OPLangParser.AND_OR_OP)
                    self.state = 241
                    self.expr3(0) 
                self.state = 246
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(OPLangParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(OPLangParser.Expr3Context,0)


        def ADD_SUB_BINOP(self):
            return self.getToken(OPLangParser.ADD_SUB_BINOP, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_expr3



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OPLangParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_expr3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 255
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OPLangParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 250
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 251
                    self.match(OPLangParser.ADD_SUB_BINOP)
                    self.state = 252
                    self.expr4(0) 
                self.state = 257
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(OPLangParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(OPLangParser.Expr4Context,0)


        def MUL_DIV_MOD_OP(self):
            return self.getToken(OPLangParser.MUL_DIV_MOD_OP, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_expr4



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OPLangParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_expr4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.expr5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 266
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OPLangParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 261
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 262
                    self.match(OPLangParser.MUL_DIV_MOD_OP)
                    self.state = 263
                    self.expr5(0) 
                self.state = 268
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr6(self):
            return self.getTypedRuleContext(OPLangParser.Expr6Context,0)


        def expr5(self):
            return self.getTypedRuleContext(OPLangParser.Expr5Context,0)


        def STR_CONCAT_OP(self):
            return self.getToken(OPLangParser.STR_CONCAT_OP, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_expr5



    def expr5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OPLangParser.Expr5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_expr5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.expr6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 277
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OPLangParser.Expr5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr5)
                    self.state = 272
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 273
                    self.match(OPLangParser.STR_CONCAT_OP)
                    self.state = 274
                    self.expr6() 
                self.state = 279
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(OPLangParser.NOT, 0)

        def expr6(self):
            return self.getTypedRuleContext(OPLangParser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(OPLangParser.Expr7Context,0)


        def getRuleIndex(self):
            return OPLangParser.RULE_expr6




    def expr6(self):

        localctx = OPLangParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expr6)
        try:
            self.state = 283
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [53]:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                self.match(OPLangParser.NOT)
                self.state = 281
                self.expr6()
                pass
            elif token in [8, 12, 23, 31, 32, 57, 67, 68, 69, 70]:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
                self.expr7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD_SUB_UNOP(self):
            return self.getToken(OPLangParser.ADD_SUB_UNOP, 0)

        def expr7(self):
            return self.getTypedRuleContext(OPLangParser.Expr7Context,0)


        def expr8(self):
            return self.getTypedRuleContext(OPLangParser.Expr8Context,0)


        def getRuleIndex(self):
            return OPLangParser.RULE_expr7




    def expr7(self):

        localctx = OPLangParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expr7)
        try:
            self.state = 288
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.match(OPLangParser.ADD_SUB_UNOP)
                self.state = 286
                self.expr7()
                pass
            elif token in [12, 23, 31, 32, 57, 67, 68, 69, 70]:
                self.enterOuterAlt(localctx, 2)
                self.state = 287
                self.expr8(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr9(self):
            return self.getTypedRuleContext(OPLangParser.Expr9Context,0)


        def expr8(self):
            return self.getTypedRuleContext(OPLangParser.Expr8Context,0)


        def array_access(self):
            return self.getTypedRuleContext(OPLangParser.Array_accessContext,0)


        def getRuleIndex(self):
            return OPLangParser.RULE_expr8



    def expr8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OPLangParser.Expr8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_expr8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.expr9(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 297
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OPLangParser.Expr8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                    self.state = 293
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 294
                    self.array_access() 
                self.state = 299
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Array_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(OPLangParser.LBRACKET, 0)

        def expr0(self):
            return self.getTypedRuleContext(OPLangParser.Expr0Context,0)


        def RBRACKET(self):
            return self.getToken(OPLangParser.RBRACKET, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_array_access




    def array_access(self):

        localctx = OPLangParser.Array_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_array_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(OPLangParser.LBRACKET)
            self.state = 301
            self.expr0()
            self.state = 302
            self.match(OPLangParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fact(self):
            return self.getTypedRuleContext(OPLangParser.FactContext,0)


        def expr9(self):
            return self.getTypedRuleContext(OPLangParser.Expr9Context,0)


        def DOT(self):
            return self.getToken(OPLangParser.DOT, 0)

        def method_invocation(self):
            return self.getTypedRuleContext(OPLangParser.Method_invocationContext,0)


        def ID(self):
            return self.getToken(OPLangParser.ID, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_expr9



    def expr9(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OPLangParser.Expr9Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_expr9, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.fact()
            self._ctx.stop = self._input.LT(-1)
            self.state = 315
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OPLangParser.Expr9Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr9)
                    self.state = 307
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 308
                    self.match(OPLangParser.DOT)
                    self.state = 311
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                    if la_ == 1:
                        self.state = 309
                        self.method_invocation()
                        pass

                    elif la_ == 2:
                        self.state = 310
                        self.match(OPLangParser.ID)
                        pass

             
                self.state = 317
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literals(self):
            return self.getTypedRuleContext(OPLangParser.LiteralsContext,0)


        def ID(self):
            return self.getToken(OPLangParser.ID, 0)

        def THIS(self):
            return self.getToken(OPLangParser.THIS, 0)

        def NIL(self):
            return self.getToken(OPLangParser.NIL, 0)

        def method_invocation(self):
            return self.getTypedRuleContext(OPLangParser.Method_invocationContext,0)


        def obj_creation(self):
            return self.getTypedRuleContext(OPLangParser.Obj_creationContext,0)


        def LPAREN(self):
            return self.getToken(OPLangParser.LPAREN, 0)

        def expr0(self):
            return self.getTypedRuleContext(OPLangParser.Expr0Context,0)


        def RPAREN(self):
            return self.getToken(OPLangParser.RPAREN, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_fact




    def fact(self):

        localctx = OPLangParser.FactContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_fact)
        try:
            self.state = 329
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.literals()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 319
                self.match(OPLangParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 320
                self.match(OPLangParser.THIS)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 321
                self.match(OPLangParser.NIL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 322
                self.method_invocation()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 323
                self.obj_creation()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 324
                self.match(OPLangParser.THIS)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 325
                self.match(OPLangParser.LPAREN)
                self.state = 326
                self.expr0()
                self.state = 327
                self.match(OPLangParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Obj_creationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(OPLangParser.NEW, 0)

        def ID(self):
            return self.getToken(OPLangParser.ID, 0)

        def LPAREN(self):
            return self.getToken(OPLangParser.LPAREN, 0)

        def expr_nulist(self):
            return self.getTypedRuleContext(OPLangParser.Expr_nulistContext,0)


        def RPAREN(self):
            return self.getToken(OPLangParser.RPAREN, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_obj_creation




    def obj_creation(self):

        localctx = OPLangParser.Obj_creationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_obj_creation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(OPLangParser.NEW)
            self.state = 332
            self.match(OPLangParser.ID)
            self.state = 333
            self.match(OPLangParser.LPAREN)
            self.state = 334
            self.expr_nulist()
            self.state = 335
            self.match(OPLangParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_nulistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_prime(self):
            return self.getTypedRuleContext(OPLangParser.Expr_primeContext,0)


        def getRuleIndex(self):
            return OPLangParser.RULE_expr_nulist




    def expr_nulist(self):

        localctx = OPLangParser.Expr_nulistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_expr_nulist)
        try:
            self.state = 339
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 12, 23, 31, 32, 53, 57, 67, 68, 69, 70]:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.expr_prime()
                pass
            elif token in [58]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr0(self):
            return self.getTypedRuleContext(OPLangParser.Expr0Context,0)


        def COMMA(self):
            return self.getToken(OPLangParser.COMMA, 0)

        def expr_prime(self):
            return self.getTypedRuleContext(OPLangParser.Expr_primeContext,0)


        def getRuleIndex(self):
            return OPLangParser.RULE_expr_prime




    def expr_prime(self):

        localctx = OPLangParser.Expr_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_expr_prime)
        try:
            self.state = 346
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 341
                self.expr0()
                self.state = 342
                self.match(OPLangParser.COMMA)
                self.state = 343
                self.expr_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 345
                self.expr0()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invocationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(OPLangParser.LPAREN, 0)

        def expr_nulist(self):
            return self.getTypedRuleContext(OPLangParser.Expr_nulistContext,0)


        def RPAREN(self):
            return self.getToken(OPLangParser.RPAREN, 0)

        def ID(self):
            return self.getToken(OPLangParser.ID, 0)

        def THIS(self):
            return self.getToken(OPLangParser.THIS, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_method_invocation




    def method_invocation(self):

        localctx = OPLangParser.Method_invocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_method_invocation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            _la = self._input.LA(1)
            if not(_la==12 or _la==32):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 349
            self.match(OPLangParser.LPAREN)
            self.state = 350
            self.expr_nulist()
            self.state = 351
            self.match(OPLangParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(OPLangParser.LBRACE, 0)

        def var_decl_nulist(self):
            return self.getTypedRuleContext(OPLangParser.Var_decl_nulistContext,0)


        def stmt_nulist(self):
            return self.getTypedRuleContext(OPLangParser.Stmt_nulistContext,0)


        def RBRACE(self):
            return self.getToken(OPLangParser.RBRACE, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_block_statement




    def block_statement(self):

        localctx = OPLangParser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_block_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.match(OPLangParser.LBRACE)
            self.state = 354
            self.var_decl_nulist()
            self.state = 355
            self.stmt_nulist()
            self.state = 356
            self.match(OPLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_nulistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(OPLangParser.StmtContext,0)


        def stmt_nulist(self):
            return self.getTypedRuleContext(OPLangParser.Stmt_nulistContext,0)


        def getRuleIndex(self):
            return OPLangParser.RULE_stmt_nulist




    def stmt_nulist(self):

        localctx = OPLangParser.Stmt_nulistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_stmt_nulist)
        try:
            self.state = 362
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12, 14, 16, 21, 26, 27, 32, 59]:
                self.enterOuterAlt(localctx, 1)
                self.state = 358
                self.stmt()
                self.state = 359
                self.stmt_nulist()
                pass
            elif token in [60]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_nulistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(OPLangParser.Var_declContext,0)


        def var_decl_nulist(self):
            return self.getTypedRuleContext(OPLangParser.Var_decl_nulistContext,0)


        def getRuleIndex(self):
            return OPLangParser.RULE_var_decl_nulist




    def var_decl_nulist(self):

        localctx = OPLangParser.Var_decl_nulistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_var_decl_nulist)
        try:
            self.state = 368
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 364
                self.var_decl()
                self.state = 365
                self.var_decl_nulist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def is_final(self):
            return self.getTypedRuleContext(OPLangParser.Is_finalContext,0)


        def type_(self):
            return self.getTypedRuleContext(OPLangParser.TypeContext,0)


        def id_list(self):
            return self.getTypedRuleContext(OPLangParser.Id_listContext,0)


        def SEMI(self):
            return self.getToken(OPLangParser.SEMI, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_var_decl




    def var_decl(self):

        localctx = OPLangParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.is_final()
            self.state = 371
            self.type_()
            self.state = 372
            self.id_list()
            self.state = 373
            self.match(OPLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stmt(self):
            return self.getTypedRuleContext(OPLangParser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(OPLangParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(OPLangParser.For_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(OPLangParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(OPLangParser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(OPLangParser.Return_stmtContext,0)


        def method_invocation(self):
            return self.getTypedRuleContext(OPLangParser.Method_invocationContext,0)


        def SEMI(self):
            return self.getToken(OPLangParser.SEMI, 0)

        def block_statement(self):
            return self.getTypedRuleContext(OPLangParser.Block_statementContext,0)


        def getRuleIndex(self):
            return OPLangParser.RULE_stmt




    def stmt(self):

        localctx = OPLangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_stmt)
        try:
            self.state = 385
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 375
                self.assign_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 376
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 377
                self.for_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 378
                self.break_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 379
                self.continue_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 380
                self.return_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 381
                self.method_invocation()
                self.state = 382
                self.match(OPLangParser.SEMI)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 384
                self.block_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(OPLangParser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(OPLangParser.ASSIGN, 0)

        def expr0(self):
            return self.getTypedRuleContext(OPLangParser.Expr0Context,0)


        def SEMI(self):
            return self.getToken(OPLangParser.SEMI, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_assign_stmt




    def assign_stmt(self):

        localctx = OPLangParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.lhs()
            self.state = 388
            self.match(OPLangParser.ASSIGN)
            self.state = 389
            self.expr0()
            self.state = 390
            self.match(OPLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(OPLangParser.ID, 0)

        def array_access(self):
            return self.getTypedRuleContext(OPLangParser.Array_accessContext,0)


        def getRuleIndex(self):
            return OPLangParser.RULE_lhs




    def lhs(self):

        localctx = OPLangParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_lhs)
        try:
            self.state = 395
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 392
                self.match(OPLangParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 393
                self.match(OPLangParser.ID)
                self.state = 394
                self.array_access()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(OPLangParser.IF, 0)

        def expr0(self):
            return self.getTypedRuleContext(OPLangParser.Expr0Context,0)


        def THEN(self):
            return self.getToken(OPLangParser.THEN, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OPLangParser.StmtContext)
            else:
                return self.getTypedRuleContext(OPLangParser.StmtContext,i)


        def ELSE(self):
            return self.getToken(OPLangParser.ELSE, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_if_stmt




    def if_stmt(self):

        localctx = OPLangParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.match(OPLangParser.IF)
            self.state = 398
            self.expr0()
            self.state = 399
            self.match(OPLangParser.THEN)
            self.state = 400
            self.stmt()
            self.state = 404
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 401
                self.match(OPLangParser.ELSE)
                self.state = 402
                self.stmt()
                pass

            elif la_ == 2:
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(OPLangParser.FOR, 0)

        def ID(self):
            return self.getToken(OPLangParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(OPLangParser.ASSIGN, 0)

        def expr0(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OPLangParser.Expr0Context)
            else:
                return self.getTypedRuleContext(OPLangParser.Expr0Context,i)


        def LPAREN(self):
            return self.getToken(OPLangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(OPLangParser.RPAREN, 0)

        def DO(self):
            return self.getToken(OPLangParser.DO, 0)

        def stmt(self):
            return self.getTypedRuleContext(OPLangParser.StmtContext,0)


        def TO(self):
            return self.getToken(OPLangParser.TO, 0)

        def DOWNTO(self):
            return self.getToken(OPLangParser.DOWNTO, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_for_stmt




    def for_stmt(self):

        localctx = OPLangParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.match(OPLangParser.FOR)
            self.state = 407
            self.match(OPLangParser.ID)
            self.state = 408
            self.match(OPLangParser.ASSIGN)
            self.state = 409
            self.expr0()
            self.state = 410
            self.match(OPLangParser.LPAREN)
            self.state = 411
            _la = self._input.LA(1)
            if not(_la==35 or _la==36):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 412
            self.expr0()
            self.state = 413
            self.match(OPLangParser.RPAREN)
            self.state = 414
            self.match(OPLangParser.DO)
            self.state = 415
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(OPLangParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(OPLangParser.SEMI, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_break_stmt




    def break_stmt(self):

        localctx = OPLangParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self.match(OPLangParser.BREAK)
            self.state = 418
            self.match(OPLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(OPLangParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(OPLangParser.SEMI, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_continue_stmt




    def continue_stmt(self):

        localctx = OPLangParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.match(OPLangParser.CONTINUE)
            self.state = 421
            self.match(OPLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(OPLangParser.RETURN, 0)

        def expr0(self):
            return self.getTypedRuleContext(OPLangParser.Expr0Context,0)


        def SEMI(self):
            return self.getToken(OPLangParser.SEMI, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_return_stmt




    def return_stmt(self):

        localctx = OPLangParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_return_stmt)
        try:
            self.state = 429
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 423
                self.match(OPLangParser.RETURN)
                self.state = 424
                self.expr0()
                self.state = 425
                self.match(OPLangParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 427
                self.match(OPLangParser.RETURN)
                self.state = 428
                self.match(OPLangParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literals(self):
            return self.getTypedRuleContext(OPLangParser.LiteralsContext,0)


        def ID(self):
            return self.getToken(OPLangParser.ID, 0)

        def VOID(self):
            return self.getToken(OPLangParser.VOID, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_type




    def type_(self):

        localctx = OPLangParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_type)
        try:
            self.state = 434
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [67, 68, 69, 70]:
                self.enterOuterAlt(localctx, 1)
                self.state = 431
                self.literals()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 432
                self.match(OPLangParser.ID)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 433
                self.match(OPLangParser.VOID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL(self):
            return self.getToken(OPLangParser.INTEGER_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(OPLangParser.FLOAT_LITERAL, 0)

        def BOOLEAN_LITERAL(self):
            return self.getToken(OPLangParser.BOOLEAN_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(OPLangParser.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_literals




    def literals(self):

        localctx = OPLangParser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_literals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
            _la = self._input.LA(1)
            if not(((((_la - 67)) & ~0x3f) == 0 and ((1 << (_la - 67)) & 15) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(OPLangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(OPLangParser.RBRACE, 0)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OPLangParser.ValueContext)
            else:
                return self.getTypedRuleContext(OPLangParser.ValueContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(OPLangParser.COMMA)
            else:
                return self.getToken(OPLangParser.COMMA, i)

        def getRuleIndex(self):
            return OPLangParser.RULE_array_literal




    def array_literal(self):

        localctx = OPLangParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_array_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
            self.match(OPLangParser.LBRACE)
            self.state = 447
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 67)) & ~0x3f) == 0 and ((1 << (_la - 67)) & 15) != 0):
                self.state = 439
                self.value()
                self.state = 444
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==64:
                    self.state = 440
                    self.match(OPLangParser.COMMA)
                    self.state = 441
                    self.value()
                    self.state = 446
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 449
            self.match(OPLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL(self):
            return self.getToken(OPLangParser.INTEGER_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(OPLangParser.FLOAT_LITERAL, 0)

        def BOOLEAN_LITERAL(self):
            return self.getToken(OPLangParser.BOOLEAN_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(OPLangParser.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_value




    def value(self):

        localctx = OPLangParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            _la = self._input.LA(1)
            if not(((((_la - 67)) & ~0x3f) == 0 and ((1 << (_la - 67)) & 15) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[23] = self.expr2_sempred
        self._predicates[24] = self.expr3_sempred
        self._predicates[25] = self.expr4_sempred
        self._predicates[26] = self.expr5_sempred
        self._predicates[29] = self.expr8_sempred
        self._predicates[31] = self.expr9_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr5_sempred(self, localctx:Expr5Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr8_sempred(self, localctx:Expr8Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expr9_sempred(self, localctx:Expr9Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




