# palindrome checker

s1 = str(input('phrase: ')).strip()
s2 = ''
for c in s1:
    s2 = c + s2
s1s = s1.split()
s2s = s2.split()
s1j = ''.join(s1s).upper()
s2j = ''.join(s2s).upper()
print(s1j, s2j)
print('palindrome' if s2j == s1j else 'not palindrome')
