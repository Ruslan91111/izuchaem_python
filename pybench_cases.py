"""
pybench_cases.ру:    запускает pybench на наборе версий Python и операторов.
Выбирайте режимы путем редактирования этого сценария либо использования
аргументов командной строки (в sys.argv): например, запускайте
C:\python27\python pybench_cases.ру, чтобы протестировать только одну
версию Python из перечисленных в stmts, pybench_cases.ру -а
для тестирования всех версий Python и ру -3 pybench_cases.ру -a -t
для трассировки командных строк.
"""

import pybench, sys
pythons = [
    (1,'D:\python33\python'),
    (0, 'D:\python27\python'),
    (0, 'D:\pypy\pypy-1.9\pypy')
]

stmts = [
    (0,0, "[x**2 for x in range(1000)]"),
    (0,0, "res=[]\nfor x in range(1000): res.append(x**2)"),
    (0, 0, "$listif3(map(lambda x: x**2, range(1000)))"),
    (0, 0, "list(x**2 for x in range(1000))"),
    (0,0, "s='spam'*2500\nx = [s[i] for i in range (10000)]"),
    (0,0,"s='?'\nfor i in range(10000):s += '?'"),
]
tracecmd = '-t' in sys.argv
pythons = pythons if '-a' in sys.argv else None   # -а: все версии Python
                                                  # -t: трассировать командные строки?
                                                  #  в спискеf  иначе одну?
pybench.runner(stmts, pythons, tracecmd)








