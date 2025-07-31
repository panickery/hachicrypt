import hashlib

def stable_str_to_num(s: str) -> int:
    # MD5 해시 생성
    md5_digest = hashlib.md5(s.encode()).digest()
    # 바이트를 큰 정수로 변환
    num = int.from_bytes(md5_digest, 'big')
    # 0~9999로 매핑
    return num % 10000

