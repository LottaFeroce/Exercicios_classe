#def buibivi(nome,id):
    #print("Bingus",nome,'\nMU lançará em:',id,"anos")
#for a in range(2):
   # buibivi("Floppa",28)
   #buibivi("Sangus",39)
    #buibivi("Tingus")
def calcp(qtd_h,valor_h):
    horas = float(qtd_h)
    taxa = float(valor_h)
    if horas <= 40:
        sal=horas*taxa
    else:
        h_excd = horas - 40
        sal = 40*taxa+(h_excd*(1.5*taxa))
    print(sal)
calcp(10,50)