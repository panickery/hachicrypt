import hashlib

def stable_str_to_num(s: str) -> int:
    # MD5 해시 생성
    md5_digest = hashlib.md5(s.encode()).digest()
    # 바이트를 큰 정수로 변환
    num = int.from_bytes(md5_digest, 'big')
    # 0~9999로 매핑
    return num % 10000

_PLAIN_TEXT = """
여름 장이란 애시당초에 글러서, 해는 아직 중천에 있건만 장판은 벌써 쓸쓸하고 더운 햇발이 벌여놓은 전 휘장 밑으로 등줄기를 훅훅 볶는다.마을 사람들은 거지반 돌아간 뒤요, 팔리지 못한 나뭇군패가 길거리에 궁싯거리고들 있으나 석윳병이나 받고 고깃마리나 사면 족할 이 축들을 바라고 언제까지든지 버티고 있을 법은 없다. 춥춥스럽게 날아드는 파리떼도 장난군 각다귀들도 귀치않다. 얽둑배기요 왼손잡이인 드팀전의 허생원은 기어코 동업의 조선달에게 낚아보았다.
그다지 마음이 당기지 않는 것을 쫓아갔다. 허생원은 계집과는 연분이 멀었다. 얽둑배기 상판을 쳐들고 대어 설 숫기도 없었으나 계집 편에서 정을 보낸 적도 없었고, 쓸쓸하고 뒤틀린 반생이었다. 충줏집을 생각만 하여도 철없이 얼굴이 붉어지고 발밑이 떨리고 그 자리에 소스라쳐버린다. 충줏집 문을 들어서서 술좌석에서 짜장 동이를 만났을 때에는 어찌 된 서슬엔지 발끈 화가 나버렸다. 상위에 붉은 얼굴을 쳐들고 제법 계집과 농탕치는 것을 보고서야 견딜 수 없었던 것이다. 녀석이 제법 난질군인데 꼴사납다. 머리에 피도 안 마른 녀석이 낮부터 술 처먹고 계집과 농탕이야. 장돌뱅이 망신만 시키고 돌아다니누나. 그 꼴에 우리들과 한몫 보자는 셈이지. 동이 앞에 막아서면서부터 책망이었다. 걱정두 팔자요 하는 듯이 빤히 쳐다보는 상기된 눈망울에 부딪칠 때, 얼결김에 따귀를 하나 갈겨주지 않고는 배길 수 없었다. 동이도 화를 쓰고 팩하고 일어서기는 하였으나, 허생원은 조금도 동색하는 법없이 마음먹은 대로는 다 지껄였다--어디서 주워먹은 선머슴인지는 모르겠으나, 네게도 아비 어미 있겠지. 그 사나운 꼴 보면 맘 좋겠다. 장사란 탐탁하게 해야 돼지, 계집이 다 무어야. 나가거라, 냉큼 꼴 치워.
그러나 한마디도 대거리하지 않고 하염없이 나가는 꼴을 보려니, 도리어 측은히 여겨졌다. 아직두 서름서름한 사인데 너무 과하지 않았을까 하고 마음이 섬짓해졌다. 주제도 넘지, 같은 술손님이면서두 아무리 젊다구 자식 낳게 된 것을 붙들고 치고 닦아 셀 것은 무어야 원. 충줏집은 입술을 쭝긋하고 술 붓는 솜씨도 거칠었으나, 젊은 애들한테는 그것이 약이 된다나 하고 그 자리는 조선달이 얼버무려 넘겼다. 너 녀석한테 반했지? 애숭이를 빨면 죄된다. 한참 법석을 친 후이다. 담도 생긴데다가 웬일인지 흠뻑 취해보고 싶은 생각도 있어서 허생원은 주는 술잔이면 거의 다 들이켰다. 거나해짐을 따라 계집 생각보다도 동이의 뒷일이 한결같이 궁금해졌다. 내 꼴에 계집을 가로채서는 어떡헐 작정이었누 하고 어리석은 꼬락서니를 모질게 책망하는 마음도 한편에 있었다. 그렇기 때문에 얼마나 지난 뒤인지 동이가 헐레벌떡거리며 황급히 부르러 왔을 때에는, 마시던 잔을 그 자리에 던지고 정신없이 허덕이며 충줏집을 뛰어나간 것이다.
"""
# _INGREDIENTS = ["아", "에", "이", "오", "우"]
_INGREDIENTS = ["으", "에", "어", ".", "!"]
# _INGREDIENTS = [".", ",", "ㅋ", "!", "?"]
# _INGREDIENTS = [".", "ㅋ", "?"]
# _INGREDIENTS = ["안", "녕"]
# _INGREDIENTS = ["피", "카", "츄"]
_INGREDIENTS = list("0123456789")
_BASE = len(_INGREDIENTS)

print("{}진수 사용".format(_BASE))
print("{}글자 사용".format(len(_PLAIN_TEXT)))

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

def main() :
    pass

def test() :
    result = int_to_base(11, 4)
    print(result)

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
