
def preveri(igrana, dobitna1, dobitna2, dobitna3, dobitna4, dobitna5):
    if igrana == "":
        barva = "prazna"
        return barva
    elif igrana == dobitna1 or igrana == dobitna2 or igrana == dobitna3 or igrana == dobitna4 or\
                    igrana == dobitna5:
        barva = "zadeta"
        return barva
    else:
        barva = "zgresena"
        return barva

def preverix(igrana, dobitnax1, dobitnax2):
    if igrana == "":
        barva = "prazna"
        return barva
    elif igrana == dobitnax1 or igrana == dobitnax2:
        barva = "zadeta"
        return barva
    else:
        barva = "zgresena"
        return barva

ena = "cifra"

dva = 1

cifra = "%s%s" % (ena, dva)
print cifra
dva += 1
cifra = "%s%s" % (ena, dva)
print cifra


dobitna1 = 1
dobitna2 = 2
dobitna3 = 3
dobitna4 = 4
dobitna5 = 5
igrana1 = 4
igrana2 = 6
igrana3 = 9

seznam = [igrana1, igrana2, igrana3]

params = {"dobitna1": dobitna1, "dobitna2": dobitna2, "dobitna3": dobitna3, "dobitna4": dobitna4, "dobitna5": dobitna5,
          "igrana1": igrana1, "igrana2": igrana2, "igrana3": igrana3}

ime = "barva"
st = 1

for cifra in seznam:
    igrana = "%s%s" % (ime, st)
    barva = preveri(cifra, dobitna1, dobitna2, dobitna3, dobitna4, dobitna5)
    params[igrana] = barva
    st += 1
    print barva

print(params)
