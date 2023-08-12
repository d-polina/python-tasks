# В текстовом файле находится цепочка из символов латинского алфавита A, B, C, D, E, F. Найдите длину самой длинной подцепочки, состоящей из символов А, С, D, F (в произвольном порядке)


# разбиением на кусочки:
s = open('24-1.txt').readline()
s = s.replace('B',' ').replace('E',' ')
print(max(len(c) for c in s.splite())) # конструкция len(c) for c in s.splite() - генератор списка, он превращает каждый кусочек в его длину

# перебором с длинным условием
s = open('24-1.txt').readline()
c = m = 0
for i in range(len(s)):
    if s[i]=='A' or s[i]=='C' or s[i]=='D' or s[i]=='F':
        c += 1
        m = max(m,c)
    else:
        c = 0
print(m)

# перебором с коротким условием
s = open('24-1.txt').readline()
c = m = 0
for i in range(len(s)):
    if s[i] in 'ACDF': # здесь проверяется один символ s[i] из A или С или D или F, короткая запись
        c += 1
        m = max(m,c)
    else: 
        c = 0
print(m)
