# Top Down dirigido por tabela
# Produções:
# Hipótese 1:
producoes1 = {
    "p1": {
        "esquerdo": 'Lista',
        "direito": ['PA', 'LCont']
    },
    "p2": {
        "esquerdo": 'LCont',
        "direito": ['PF']
    },
    "p3": {
        "esquerdo": 'LCont',
        "direito": ['Elems', 'PF']
    },
    "p4": {
        "esquerdo": 'Elems',
        "direito": ['Elem', 'ElemCont']
    },
    "p5": {
        "esquerdo": 'Elem',
        "direito": ['NUM']
    },
    "p6": {
        "esquerdo": 'ElemCont',
        "direito": ['VIRG', 'Elems']
    },
    "p7": {
        "esquerdo": 'ElemCont',
        "direito": []
    }
}

# Hipótese 2 (agrupadas por simb N):
producoes = {
    "Lista": [['PA', 'LCont']],
    "LCont": [['PF'],['Elems', 'PF']],
    "Elems": [['Elem', 'ElemCont']],
    "Elem": [['NUM']],
    "ElemCont": [['VIRG', 'Elems'],[]]
}
# Símbolos não terminais
NT = ['Lista', 'LCont', 'Elems', 'Elem', 'ElemCont']
# Símbolos terminais
T = ['NUM','PA','PF','VIRG']

# Cálculo de LookAheads
lookAheads = {}
for n in NT:
    lookAheads[n] = []
    for p in producoes[n]:
        encontrado = False
        i = 0
        while not encontrado and i < len(p):
            if p[i] in T:
                if p[i] not in 