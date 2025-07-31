from collections.abc import Callable
import pytest
import hachicrypt.utils as utils

# from hachicrypt.core import encrypt, decrypt

def test_str_hash() :
    pass
    # hash1 = utils.stable_str_to_num("hachicrypt")  # 항상 같은 값
    # hash2 = utils.stable_str_to_num("password123")
    #
    # assert hash1 != hash2

# def test_encrypt_decrypt():
#     original = "Hello, Hachicrypt!"
#     key = "secretkey"
#
#     encrypted = encrypt(original, key)
#     assert encrypted != original, "암호화된 문자열은 원본과 달라야 합니다."
#
#     decrypted = decrypt(encrypted, key)
#     assert decrypted == original, "복호화된 문자열은 원본과 동일해야 합니다."