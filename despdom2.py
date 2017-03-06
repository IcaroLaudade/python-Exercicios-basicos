print 'Balanco de despesas domesticas'
ana = raw_input('Quanto gastou Ana? ')
bia = raw_input('Quanto gastou Bia? ')
total = float(ana) + float(bia)
print 'Total de gastos = R$ %s.' % total
media = total/2
print 'Gastos por pessoa = R$ %s.' % media
if(float(ana)!= float(bia)):
    if(float(ana)> float(bia)):
        deve=media-float(bia)
        print 'Bia deve %.2f para ana' % deve
    else:
        deve=media-float(ana)
        print 'Ana deve %.2f para Bia' %   deve
else:
    print 'Ambas gastaram a mesma quantia'
