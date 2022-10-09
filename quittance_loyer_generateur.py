#launch commandline %python3 quittance_loyer_generateur.py


import string
from turtle import color
from fpdf import FPDF
debut = "01/10/2022"
fin = "31/10/2022"

annee = int (debut[6]+debut[7]+debut[8]+debut[9])
mois = int (debut[3]+debut[4])
calcul = (annee - 2022)*12 + mois 
numerobis = str(calcul)
class PDF(FPDF):
    def header(self):
        # Logo
        self.image('kiatou.png', 163, 10,28)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        # Title
        self.cell(0, 0, 'XXXXX')
        self.set_font('Arial', '', 10)
        self.ln(8)
        self.cell(0,0,'XXXXXX')
        self.ln(4)
        self.cell(0,0,'XXXXXXXX')
        self.ln(4)
        self.cell(0,0,'XXXXXXXX')
        self.ln(4)
        self.cell(0,0,'Portable: XXXXXXXX  XXXXXXXX')
        self.ln(4)
        self.cell(0,0,'Mail: XXXXXXXX')
        # Line break
        self.ln(10)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

# Instanciation des paramètres généraux
pdf = PDF('P','mm','A4')
pdf.set_margins(20,15, 20)
pdf.alias_nb_pages()
pdf.add_page()

#Pour l'entête du contrat
pdf.set_font('Arial','', 10)
pdf.cell(139,4,'Contrat:     C'+ debut[6]+debut[7]+debut[8]+debut[9]+debut[3]+debut[4]+debut[0]+debut[1],0,0)
pdf.cell(31,4,'Quittance de loyer',1,1)
pdf.cell(139,4,'Locataire:  XXXXXXXX',0,0)
pdf.cell(31,4,'Contrat N° '+numerobis,1,1)
pdf.cell(139,4,'Période:     '+debut,0,0)
pdf.cell(31,4,debut,1,1)
pdf.ln(4)
pdf.cell(0,4,'XXXXXXXX',0,1)
pdf.cell(0,4,'XXXXXXXX ',0,1)
pdf.cell(0,4,'XXXXXXXX',0,1)
pdf.cell(0,4,'XXXXXXXX',0,1)
pdf.ln(4)

#Le corps du contrat
#pdf.set_draw_color(0,180,180) #border = blue
#pdf.set_fill_color(230,230,0) #fill with yellow color
#pdf.set_text_color(220,50,50) #text color = red

pdf.set_fill_color(0,180,180) #fill with yellow color
pdf.cell(0,4,'AVIS D\'ECHEANCE',1,1,"C",fill=1)
pdf.cell(0,26,"Période du "+ debut + " au " + fin,1,0)
pdf.cell(-30,26,"750.00 euros",1,0,"C")
pdf.ln(8)
pdf.cell(0,2,"LOCATION MEUBLEE",0,1)
pdf.ln(5)
pdf.cell(0,4,"Adresse :XXXXXXXX",0,1)
pdf.ln(7)
pdf.cell(0,26,"Charges Comprises",1,0)
pdf.cell(-30,26,"200.00 euros",1,1,"C")
pdf.ln(7)
pdf.set_font('Arial','I', 10)
pdf.cell(0,4,"XXXXXXXX",0,1)
pdf.cell(0,4,"XXXXXXXX",0,1)
pdf.cell(0,4,"Au titre du paiement du loyer et des charges du logement/local sis:",0,1)
pdf.cell(0,4,"XXXXXXXX",0,1)
pdf.cell(0,4,"Pour la période de location du "+debut +" au " + fin +"",0,1)



pdf.ln(40)
pdf.set_font('Arial','B', 10)
pdf.cell(40,4,"Mode de Paiement:",0,0)
pdf.set_font('Arial','', 10)
pdf.cell(80,4,"XXXXXXXX",0,0)
pdf.set_fill_color(0,180,180) #fill with yellow colorv
pdf.set_font('Arial','B', 10)
pdf.cell(30,4,"Montant à régler",1,0,fill =1)
pdf.cell(23,4,"950.00 euros",1,1,fill =1)
pdf.cell(40,4,"",0,0)
pdf.set_font('Arial','', 10)
pdf.cell(40,4,"XXXXXXXX",0,1)
pdf.cell(63,4,"",0,0)
pdf.set_fill_color(220,50,50)
pdf.cell(110,4,"950 euros payé le "+ debut + " par VIREMENT à XXXXXXXX",1,1, fill =1)
pdf.ln(2)
pdf.cell(40,4,"Le non paiement à échéance entrainera la",0,1)
pdf.cell(40,4,"facturation d'une indemnité égale à 40 euros",0,1)
#ajout de signature pour la fin
#pdf.image('signature.jpg', 35, 230,28)

pdf.ln(40)
#for i in range(1, 41):
#    pdf.cell(0, 10, 'Printing line number ' + str(i), 0, 1)
pdf.output("quittance_loyer.pdf", 'F')
