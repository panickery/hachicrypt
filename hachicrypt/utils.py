import hashlib

def stable_str_to_num(s: str) -> int:
    # MD5 해시 생성
    md5_digest = hashlib.md5(s.encode()).digest()
    # 바이트를 큰 정수로 변환
    num = int.from_bytes(md5_digest, 'big')
    # 0~9999로 매핑
    return num % 10000

"""
1,114,111 유니코드의 마지막 10진수 숫자
이걸 표현하기 위한 
진수	필요 자릿수
2	21 -> 21을 2진수로 표현하려면 5자리
3	13 -> 13을 3진수로 표현하려면 3자리(111)
4	11 -> 11을 4진수로 표현하려면 2자리(23)
5	9 -> 2자리
6	8 -> 2자리
7	8 -> 2자리
8	7 -> 1자리
9	7 -> 1자리
10	7 -> 1자리
"""

_SIZE_INDICATOR = {"2" : 5, "3" : 3, "4" : 2, "5" : 2, "6" : 2, "7" : 2, "8" : 1, "9" : 1, "10" : 1}

def put_indicator(n, base) :
    len_indicator = _SIZE_INDICATOR.get(str(base))
    idc = int_to_base(len(n), base)
    zeros_to_add = len_indicator - len(idc)
    return zeros_to_add * "0" + idc + str(n)

def int_to_base(n, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n == 0:
        return '0'
    result = ""
    negative = n < 0
    n = abs(n)
    while n:
        result = digits[n % base] + result
        n //= base
    return '-' + result if negative else result

def base_to_int(s, base):
    return int(s, base)

def dec_to_baseX(num, base):
    """10진수 정수를 X진수 문자열로 변환"""
    if num == 0:
        return '0'
    digits = []
    while num > 0:
        num, remainder = divmod(num, base)
        digits.append(str(remainder))
    return ''.join(reversed(digits))

def baseX_to_dec(s, base):
    """X진수 문자열을 10진수 정수로 변환"""
    return int(s, base)

def nums_to_char(concat_nums, ingredients):
    return [ingredients[int(i)] for i in concat_nums]

def chars_to_num(encoded_str_list, ingredients):
    return [ingredients.index(i) for i in encoded_str_list]

def split_bitstring_by_prefix(s, base):
    i = 0
    result = []
    split_num = _SIZE_INDICATOR.get(str(base))
    while i + split_num <= len(s):
        length_bits = s[i:i+split_num]
        i += split_num
        length = int(length_bits, base)  # 2진수 -> 10진수
        if i + length > len(s):
            # 길이 초과시 데이터 부족, break
            break
        data_bits = s[i:i+length]
        i += length
        result.append((length, data_bits))
    return result

def read_from_section(section):
    import configparser
    import os
    config_file_path = os.path.join(os.path.dirname(__file__), 'config.ini')
    config = configparser.ConfigParser()
    config.read(config_file_path, encoding='utf-8')  # 파일 읽기
    ingredients = config[section]['ingredients']
    print(ingredients)

def get_ingredients_from_section(section):
    import configparser
    import os
    config_file_path = os.path.join(os.path.dirname(__file__), 'config.ini')
    config = configparser.ConfigParser()
    config.read(config_file_path, encoding='utf-8')  # 파일 읽기
    ingredients = config[section]['ingredients']
    return ingredients

def check_section():
    import configparser
    import os
    config_file_path = os.path.join(os.path.dirname(__file__), 'config.ini')
    config = configparser.ConfigParser()
    config.read(config_file_path, encoding='utf-8')  # 파일 읽기
    print(config.sections())

def print_debug(msg, show_debug) :
    if show_debug :
        print("{}".format(msg))

if __name__ == '__main__' :
    pass
