"""
Les fonctions à tester sont les méthodes 'encrypt' et 'decrypt'
des classes contenues dans les fichiers dont le nom se termine
par 'algo.py'. À noter que certaines classes n'ont pas de méthode
decrypt, ou uniquement une méthode vide.

Pour lancer tous les tests contenus dans ce fichier, déplacez ce
fichier dans le dossier du projet puis utilisez 
la commande pytest <nom de ce script>
"""


# Les fichiers où se trouvent les fonctions à tester sont déjà importés
from crypto_app.enigmam3_algo import EnigmaM3
from crypto_app.aes_algo import AdvancedEncryptionStandard
from crypto_app.blowfish_algo import Blowfish
from crypto_app.caesarcipher_algo import CaesarCipher
from crypto_app.des_algo import DES
from crypto_app.md5_algo import MD5
from crypto_app.rsa_algo import RSAAlgo
from crypto_app.sha_algo import SHA
from crypto_app.vigenerecipher_algo import VigenereCipher




def test_enigma():
    """
    Premier exemple de test (vous n'avez rien à faire ici !)
    Lisez BIEN les commentaires ci-dessous, ils vous expliquent
    comment réaliser un test unitaire avec les fonctions de ce
    projet. Toutes les fonctions à tester suivent un schéma commun.
    """

    # D'abord, on instancie la classe qui contient les fonctions,
    # dans notre cas la classe EnigmaM3. Pour rappel, instancier
    # une classe c'est créer un objet de cette classe.
    enigma = EnigmaM3()

    # On crée un message qui nous servira à faire le test
    msg = "Message"

    # On définit la clé de cryptage. Enigma utilise des paramètres
    # plutôt complexes par rapport aux autres algorithmes, donc
    # ici je vous les fournis
    key = [
        ('A', 'C', 'N'),
        (2, 4, 1),
        ('F', 'H', 'K'),
        [('A', 'K')]
    ]

    # On crypte le message, puis on vérifie que le message crypté correspond 
    # au résultat attendu avec le mot clé 'assert'
    encrypted = enigma.encrypt(msg, key)
    assert encrypted == "FUTALDK"

    # Ensuite, on décrypte le message et on vérifie que l'on retrouve bien
    # notre message de base
    decrypted = enigma.decrypt(encrypted, key)
    assert decrypted == "MESSAGE"

    # Lors de l'exécution, ce test échouera si l'une des égalités testées
    # par les 'assert' est fausse.



#############################################################################
# À vous de jouer maintenant ! Complétez les tests suivants :
#############################################################################

def test_aes():

    aes = AdvancedEncryptionStandard()
    msg = "Message"
    key = "16 caracteres !!"
    expected_encryption = "5e10b9901384af"

    #####################################
    # Rajoutez les 'assert' ci-dessous !!
    #####################################

    encrypted = aes.encrypt(msg, key)
    assert encrypted == "5e10b9901384af"
    decrypted = aes.decrypt(encrypted, key)
    assert decrypted == "Message"

def test_blowfish():

    blowfish = Blowfish()
    msg = "message"
    key = "ma clé privée"
    expected_encryption = ""

    # À vous ! Ne testez que la valeur du message décrypté cette fois !
    encrypted = blowfish.encrypt(msg, key)
    assert encrypted == ""

def test_caesar():

    caesar = CaesarCipher()
    msg = "message"
    key = 3
    expected_encryption = "phvvdjh"

    # À vous !
    encrypted = caesar.encrypt(msg, key)
    assert encrypted == "phvvdjh"
    decrypted = caesar.decrypt(encrypted, key)
    assert decrypted == "message"

#######################################################################
# À vous d'écrire entièrement les tests restants. Quelques conseils :
#   - Vous pouvez lancer l'application et tester les différents cryptages
# par vous-mêmes pour voir comment ils fonctionnent. Les encadrés à droite
# donnent aussi quelques infos.
#   - Ce n'est pas grave si vous n'avez pas le temps de coder tous les tests.
# L'important est de comprendre le fonctionnent de pytest et des assert.
#   - Google is your friend, like always.
#   - Demandez au formateur si vous calez.

# Bon codage !
#######################################################################
