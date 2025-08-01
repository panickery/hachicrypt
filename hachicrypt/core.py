import hachicrypt.utils as utils

def encrypt(plaintext, key, section, show_debug=False) :
    ingredients = utils.get_ingredients_from_section(section)
    utils.print_debug(ingredients, show_debug)
    ingredients = list(ingredients)
    base = len(ingredients)
    dec_numbers = [int(ord(ch)) for ch in plaintext]
    utils.print_debug("10진수 변환 :: {}, 적용 진법 :: {}".format(dec_numbers, base), show_debug)
    baseX_chars = [utils.dec_to_baseX(dn, base) for dn in dec_numbers]
    utils.print_debug(baseX_chars, show_debug)
    baseX_chars_with_indicator = [utils.put_indicator(ch, base) for ch in baseX_chars]
    utils.print_debug(baseX_chars_with_indicator, show_debug)
    concat_nums = ''.join(baseX_chars_with_indicator)
    utils.print_debug(concat_nums, show_debug)
    encoded_str_list = utils.nums_to_char(concat_nums, ingredients)
    utils.print_debug(encoded_str_list, show_debug)
    encoded_str = ''.join(encoded_str_list)
    utils.print_debug(encoded_str, show_debug)
    return encoded_str

def decrypt(ciphertext, key, section, show_debug=False) :
    ingredients = utils.get_ingredients_from_section(section)
    utils.print_debug(ingredients, show_debug)
    ingredients = list(ingredients)
    base = len(ingredients)
    encoded_str_list = list(ciphertext)
    utils.print_debug(encoded_str_list, show_debug)
    concat_nums = utils.chars_to_num(encoded_str_list, ingredients)
    utils.print_debug(concat_nums, show_debug)
    concat_nums = ''.join([str(i) for i in concat_nums])
    utils.print_debug(concat_nums, show_debug)
    split_prefix_num = utils.split_bitstring_by_prefix(concat_nums, base)
    utils.print_debug(split_prefix_num, show_debug)
    nums_list = [i[1] for i in split_prefix_num]
    utils.print_debug(nums_list, show_debug)
    nums_list = [int(i, base) for i in nums_list]
    utils.print_debug(nums_list, show_debug)
    utils.print_debug(''.join([chr(i) for i in nums_list]), show_debug)
    return ''.join([chr(i) for i in nums_list])

if __name__ == '__main__' :
    pass