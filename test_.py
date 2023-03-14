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


"""Fonctions de test"""

def test_equality():
    assert True

def test_2():
    assert 2 + 2 == 4
    


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


def test_md5():
    enigma_md5 = MD5()
    message = "Voiture qui roule, voiture qui marche"
    expected_hash = "2371e7e3cc3f124e66f695c92b13aca4"  # MD5 hash of the message
    ciphertext = enigma_md5.encrypt(message)    
    if ciphertext == expected_hash:
        print("MD5 Test: ok")

def test_sha():
    enigma_sha = SHA()
    message = "Quand il n'y a plus de nature, il n'y a plus rien"
    expected_hash = "6a1f0b34a2150aa8100e20aa1f5ca81ba10d1c424b5cbc3fa9b8cde834834cce54c29ea1c79b4a5a278d00c11473509b7c6a73d9ee133f64e048900d0cb5945c"  # SHA-512 hash of the message
    actual_hash = enigma_sha.encrypt(message)
    if actual_hash == expected_hash:
        print("SHA Test: ok")

def test_caesar_cipher():
    enigma_caesar = CaesarCipher()
    plaintext = "La plus belle pomme est surement la plus pourrie"
    key = 5
    ciphertext = enigma_caesar.encrypt(plaintext, key)
    decryptedtext = enigma_caesar.decrypt(ciphertext, key)
    print(ciphertext, decryptedtext)
    if plaintext == decryptedtext:
        print("CaesarCipher Test: ok")


if __name__ == "__main__":
    test_aes()
    test_md5()
    test_sha()
    test_caesar_cipher()