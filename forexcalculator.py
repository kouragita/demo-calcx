#forex calculator
p = input('enter the value of pips p')
L = input('emter the value of lot size L')
c = input('enter the value of contract size c')

#note modification for float is coming
p = int(p)
L = int(L)
c = int(c)

#profit and loss calculator. dollar sign always at the end $
pnl = (p * L * c)

print(pnl)