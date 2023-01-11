import types
from imp import reload
from reloadall import status, tryreload, tester

def transitive_reload(modules, visited):
    while modules:
        next = modules.pop()           #удалить элемент next в конце
        status(next)                   # перезагрузить это,затолкнуть атрибуты в стек
        tryreload(next)
        visited.add(next)
        modules.extend(x for x in next.__dict__.values()
                       if type(x) == types.ModuleType and x not in visited)

def reload_all(*modules):
    transitive_reload(list(modules), set())

if __name__ =='__main__':
    tester(reload_all, 'reloadall3')





