from collections.abc import Callable
import pytest
import hachicrypt.utils as utils
import hachicrypt.core as core

# from hachicrypt.core import encrypt, decrypt

def test_str_hash() :
    # pass
    hash1 = utils.stable_str_to_num("hachicrypt")  # 항상 같은 값
    hash2 = utils.stable_str_to_num("password123")
    print(hash1)
    print(hash2)
    #
    assert hash1 != hash2

def test_read_config() :
    ingredients = utils.read_from_section("botchi")
    print(ingredients)

def test_check_sections() :
    print("\nis good?")
    utils.check_section()

def test_encrypt_decrypt() :
    plaintext = "안녕 나는 하치야"
    encrypted = core.encrypt(plaintext, 5, "poorin")
    print("encrypted :: {}".format(encrypted))
    decrypted = core.decrypt(encrypted, 5, "poorin")
    print("decrypted :: {}".format(decrypted))

    assert plaintext != encrypted, "암호화된 문자열은 원본과 달라야 합니다. - 통과"
    assert encrypted != decrypted, "암호화와 복호화된 문자열이 달라야 합니다. - 통과"
    assert plaintext == decrypted, "원본과 복호화된 문자열이 같음 - 통과"

def test_encrypt() :
    plaintext = "안녕 나는 하치야"
    encrypted = core.encrypt(plaintext, 5, "pikachu")
    print("encrypted :: {}".format(encrypted))

# def test_encrypt_decrypt():
#     original = "Hello, Hachicrypt!"
#     key = "secretkey"
#
#     encrypted = encrypt(original, key)
#     assert encrypted != original, "암호화된 문자열은 원본과 달라야 합니다."
#
#     decrypted = decrypt(encrypted, key)
#     assert decrypted == original, "복호화된 문자열은 원본과 동일해야 합니다."