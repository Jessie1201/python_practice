'''
Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct.
However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

Your task is to write a function maskify, which will:

Mask all digits (0-9) with #, unless they are first or last four characters.
Never mask credit cards with less than 6 characters.
Never mask non-digit characters.

Examples
"4556364607935616"->"4###########5616"	
"4556-3646-0793-5616"->"4###-####-####-5616"	
"64607935616"->"6######5616"	
"ABCD-EFGH-IJKLM-NOPQ"->"ABCD-EFGH-IJKLM-NOPQ"
'''
def maskify(cc):
  if len(cc) < 6:
    return cc
  else:
    middle = cc[1:-4]
    middle_res = ''
    for ch in middle:
      if ch.isdigit():
        middle_res += '#'
      else:
        middle_res += ch
    return cc[0] + middle_res + cc[-4:]