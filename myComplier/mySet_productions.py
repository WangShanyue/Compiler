from myComplier import Complier


# <prog> → program <id>；<block>
# <block> → [<condecl>][<vardecl>][<proc>]<body>
# <condecl> → const <const>{,<const>}
# <const> → <id>:=<integer>
# <vardecl> → var <id>{,<id>}
# <proc> → procedure <id>（[<id>{,<id>}]）;<block>{;<proc>}
# <body> → begin <statement>{;<statement>}end
# <statement> → <id> := <exp>               
# |if <lexp> then <statement>[else <statement>]
#                |while <lexp> do <statement>
#                |call <id>[（<exp>{,<exp>}）]
#                |<body>
#                |read (<id>{，<id>})
#                |write (<exp>{,<exp>})
# <lexp> → <exp> <lop> <exp>|odd <exp>
# <exp> → [+|-]<term>{<aop><term>}
# <term> → <factor>{<mop><factor>}
# <factor>→<id>|<integer>|(<exp>)
# <lop> → =|<>|<|<=|>|>=
# <aop> → +|-
# <mop> → *|/
# <id> → l{l|d}   （注：l表示字母）
# <integer> → d{d}


#这是什么数据类型？
productions = {
    'prog': [
        ['program','id',';','block'],
    ],
    'block': [
        ['body1'],
        ['condecl1','body1' ],
        ['condecl1','vardecl','body1'],
        ['vardecl','body1'],
        ['condecl1','vardecl','proc1','body1'],
        ['condecl1','proc1','body1'],
        ['proc1','body1'],
    ],
    'condecl1': [
        ['const','condecl2'],
    ],
    'condecl2': [
        ['const1',',','condecl2'],
        ['condecl3']
    ],
    'condecl3': [
        ['const1',';'],
    ],
    'const1': [
        ['id',':=' ,'integer'],
    ],
    'vardecl': [
        ['var','id',';'],
        ['var','id',',','id',';'],
        ['var','id',',','id',',','id',';'],
    ],
    'proc1': [
        ['procedure','id','(','proc2',')','M3','proc3' ],
        ['procedure','id','(',')','M3','proc3' ]
    ],
    'M3':[
        [';']
    ],
    'proc2': [
        ['id'],
        ['id',',','proc2' ],
    ],
    'proc3': [
        ['block'],
        ['block',';','proc1'],
    ],
    'body1': [
        ['begin','body2'],
    ],
    'body2': [
        ['body3'],
        ['statement',';','body2'],
    ],
    'body3': [
        ['statement','end'],
    ],
    'statement': [
        ['if','lexp','then','M1','statement'],
        ['if','lexp','then','M1','statement','N','else','M2','statement'],
        ['while','M1','lexp','do','M2','statement'],
        ['call','id','(',')'],
        ['call','id','(','exp1',')'],
        ['call','id','(','exp1',',','exp1',')'],
        ['call','id','(','exp1',',','exp1',',','exp1',')'],
        ['id',':=','exp1'],
        ['read','(','id',')'],
        ['write','(','exp1',')'],
        ['body1']
    ],
    'M1':[
        [':']
    ],
    'M2':[
        [':']
    ],
    'N':[
        [':']
    ],
    'lexp':[
        ['exp1', '<', 'exp1'],
        ['exp1', '>', 'exp1'],
        ['exp1', '<=', 'exp1'],
        ['exp1', '>=', 'exp1'],
        ['exp1', '==', 'exp1'],
        ['exp1', '!=', 'exp1'],
        ['exp1']
    ],
    'exp1': [
        ['exp1', '+', 'exp2'],
        ['exp1', '-', 'exp2'],
        ['exp2']
    ],
    'exp2':[
        ['exp2','*','exp3'],
        ['exp2','/','exp3'],
        ['exp3']
    ],
    'exp3':[
        ['(','exp1',')'],
        ['integer', ],
        ['id', ],
    ]
}
start = 'prog'
Complier.write_productions_to_file(start, productions)