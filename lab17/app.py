# Stwórz pakiet wraz z subpakietami i modułami wg schematu jak na rysunku a dodatkowo:
# • w każdym module umieść definicję funkcji fun(),
# • wspomniana funkcja powinna wyświetlać informacje o funkcji, module oraz pakiecie z jakiego została wywołana,
# • skrypt app.py powinien wywoływać wszystkie funkcje.

import pack1.mod1 as mod1

mod1.fun()
print()

import pack1.subpack1.mod2 as mod2

mod2.fun()
print()

import pack1.subpack2.mod3 as mod3

mod3.fun()
