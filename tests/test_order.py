import algorithme.modules.order as ord

ouvrier = 1
champ = 1
legume = "TOMATE"
tracteur = 1
somme = 20000


def test_acheter_champ():
    assert ord.acheter_champ() == "0 ACHETER_CHAMP"


def test_arroser():
    assert ord.arroser(ouvrier, champ) == str(ouvrier) + " ARROSER " + str(
        champ
    )


def test_semer():
    assert ord.semer(ouvrier, legume, champ) == str(
        ouvrier
    ) + " SEMER " + legume + " " + str(champ)


def test_vendre():
    assert ord.vendre(champ) == "0 VENDRE " + str(champ)


def test_acheter_tracteur():
    assert ord.acheter_tracteur() == "0 ACHETER_TRACTEUR"


def test_stocker():
    assert ord.stocker(ouvrier, champ, tracteur) == str(
        ouvrier
    ) + " STOCKER " + str(champ) + " " + str(tracteur)


def test_cuisiner():
    assert ord.cuisiner(ouvrier) == str(ouvrier) + " CUISINER"


def test_employer():
    assert ord.employer() == "0 EMPLOYER"


def test_licencier():
    assert ord.licencier(ouvrier) == "0 LICENCIER " + str(ouvrier)


def test_emprunter():
    assert ord.emprunter(somme) == "0 EMPRUNTER " + str(somme)
