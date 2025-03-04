'''Cvičení: Truhlář - nábytkář vyrábí tyto druhy nábytku: stůl, židle, komoda,
policová skříň. Každý z těchto druhů nábytku má své vlastnosti: stůl (výška, šířka, hloubka), židle (výška, šířka, hloubka),
komoda (výška, šířka, hloubka, počet šuplíků), policová skříň (výška, šířka, hloubka, počet polic). Všechny druhy nábytku mají společnou vlastnost
 - materiál (např. buk, dub apod.) Vytvoř vhodnou strukturu stříd a implementuj návrhový vzor Factory pro vytváření objektů nábytku.'''
class factory:
    def __init__(self,material):
        self.material = material

    def table(self,vyska,sirka,hloubka):
            self.vyska = vyska
            self.sirka = sirka
            self.hloubka = hloubka
            return f"Vyska je {vyska}, sirka je {sirka}, hloubka je {hloubka},ze {self.material}"
    def chair(self,vyska,sirka,hloubka):
            self.vyska = vyska
            self.sirka = sirka
            self.hloubka = hloubka
            return f"Vyska je {vyska}, sirka je {sirka}, hloubka je {hloubka},ze {self.material}"
    def closet(self,vyska,sirka,hloubka,drawers):
            self.vyska = vyska
            self.sirka = sirka
            self.hloubka = hloubka
            self.drawers = drawers
            return f"Vyska je {vyska}, sirka je {sirka}, hloubka je {hloubka},ze {self.material}. Pocet supliku je {drawers}"
    def board_closet(self,vyska,sirka,hloubka):
            self.vyska = vyska
            self.sirka = sirka
            self.hloubka = hloubka
            return f"Vyska je {vyska}, sirka je {sirka}, hloubka je {hloubka},ze {self.material}"



x = factory("Dubu")
print(x.table(12,13,15))
print(x.closet(13,11,13,12))