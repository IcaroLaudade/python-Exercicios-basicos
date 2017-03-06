
print 'Digite os valores a somar seguidos de [ENTER].'
print 'Para encerrar apenas [ENTER].'
total = 0
while 1:
    try:
        n = float(raw_input(':'))
        total = total + n
    except:
        break
print 'TOTAL: %s' % total
