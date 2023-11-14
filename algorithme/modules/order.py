def acheter_champ():
    return "0 ACHETER_CHAMP"


def arroser(ouvrier, champ):
    return str(ouvrier) + " ARROSER " + str(champ)


def semer(ouvrier, legume, champ):
    return str(ouvrier) + " SEMER " + legume + " " + str(champ)


def vendre(champ):
    return "0 VENDRE " + str(champ)


def acheter_tracteur():
    return "0 ACHETER_TRACTEUR"


def stocker(ouvrier, champ, tracteur):
    return str(ouvrier) + " STOCKER " + str(champ) + " " + str(tracteur)


def cuisiner(ouvrier):
    return str(ouvrier) + " CUISINER"


def employer():
    return "0 EMPLOYER"


def licencier(ouvrier):
    return "0 LICENCIER " + str(ouvrier)


def emprunter(somme):
    return "0 EMPRUNTER " + str(somme)
