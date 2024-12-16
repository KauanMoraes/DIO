l_hashes= list(input().replace(" ","").split(";"))

def verificar_hashes(l_hashes):
    results=[]
    for par in l_hashes:        
        par1,par2=par.split(",")
        # while par1.startwith(" "): par1.
        # while par2.startwith(" "):
        if par2==par1:
            results.append("Correto")
        else: results.append("Inválido")
    for r in results: print(r)
verificar_hashes(l_hashes)