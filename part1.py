from fpdf import FPDF
# to launch the process you have to wtrite %python3 part1.py
title = 'nique ta mere'

class PDF(FPDF):
    def header(self):
        #logo
        self.image('fox_face',10,80,25)
        #font
        self.set_font('helvetica','B',20)
        title_w = self.get_string_width(title) + 6
        doc_w = self.w
        self.set_x((doc_w - title_w/2))

        #colors of frame, background, and text
        self.set_draw_color(0,80,180) #border = blue
        self.set_fill_color(230,230,0)#background = yellow
        self.set_text_color(220,50,50)#text = red
        #Thickness of frame (border)
        self.set_line_width(1)
        #Title
        self.cell(title_w,10,title,border=1,ln=1,align='C',fill=1)
        #Padding
        self.cell(80)
        #Title
        self.cell(50,20,'Title',border = True, ln=1, align = 'C')
        #line break
        self.ln(20)
        
    def footer(self):
        #Set position of the footer
        self.set_y(-10)
        #set font
        self.set_font('helvetica','I',10)
        #Page number
        self.cell(0,10,f'Page {self.page_no()}/{{nb}}',align= 'C')    
    # Create FPDF object


# Layout ('P','L')
# Unit ('mm','cm','in')
# format ('A3','A4' (default),'A5','Letter','Legal',(100,150))
pdf = PDF('P','mm','Letter')


#add a page
pdf.add_page()
#get total page number
pdf.alias_nb_pages()

#Set auto page break
pdf.set_auto_page_break(auto=True, margin = 10)


#specify font
#fonts('times','courier','helvetica','symbol','zpdfingbats')
#'B'(bold), 'U' (underline), 'I' (italics), ''(regular), combination,(i.e.,('BU'))
pdf.set_font('helvetica','BI',16)
pdf.set_text_color(0,0,0)
#Add text
#w = width
#h = height
#ln (0 False;1 True - move cursor down to next line)
pdf.cell(120,1,'Hello world!', ln =True)
pdf.cell(80,10,"bye world")
pdf.cell(80,1,'Hello world!', ln =True)
pdf.cell(10,1,'Hello world!', ln =True)
# pdf.cell(ln=True)
# pdf.cell(40,10,'Hello world!')
for i in range (1,41):
    pdf.cell(15,10,f'bonjour',ln=1)

pdf.add_page()
pdf.output('pdf_1.pdf')