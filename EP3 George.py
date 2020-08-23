
import time

def ClassMetodoSort(TAB):
    
    TAB.sort()

def ClassQuickRecursivo(TAB,inicio,fim):

    if inicio < fim:
        
        k = ParticionaRecursivo(TAB,inicio,fim)
        ClassQuickRecursivo(TAB,inicio,k-1)
        ClassQuickRecursivo(TAB,k+1,fim)


         
def ClassQuickNaoRecursivo(TAB,inicio,fim):

    pilha = [[inicio,fim]]
    a,b = 0,0
    
    while pilha != []:

        inicio,fim = pilha.pop()
        
        if inicio < fim:
            a += 1
            k = ParticionaRecursivo(TAB,inicio,fim)
            b += 1
            pilha.append([inicio,k-1])
            pilha.append([k+1,fim])
            
           
def ParticionaRecursivo(TAB,inicio,fim):
    
    i,j = inicio,fim
    pivo = TAB[fim]
    
    while True:

        #aumentando i
        while i < j and TAB[i] <= pivo: i = i +  1

        if i < j:
            TAB[i],TAB[j] = pivo,TAB[i]
        
        else: break
    
        #diminuindo j
        while i < j and TAB[j] >= pivo: j = j - 1
        
        if i < j:
            TAB[i],TAB[j] = TAB[j],pivo
            
        else: break
    
    return i



def TransformaData(data):

    #Muda o formato da data de 'dd/mm/aaaa' para 'aaaammaa'
    nova_data = data.split('/')
    nova_data[0],nova_data[2] = nova_data[2],nova_data[0]
    nova_data = ''.join(nova_data)
    
    return nova_data


def RetornaData(data):

    #Muda o formato da data de 'aaaammaa' para 'dd/mm/aaaa'
    
    return data[6:8]+'/'+data[4:6]+'/'+data[0:4]



def LeArquivo(arq):
    
    #Le o arquivo e separa cada linha em uma lista contendo nome, data e id
    arq_txt = open(arq,"r")
    
    tab = []
    
    for i in arq_txt:
        tab.append(i)
        
    for j in range(len(tab)):
        tab[j] = tab[j].split(',')
        tab[j][1] = TransformaData(tab[j][1])
        
    return tab


def SalvaArquivo(tab,arqdestino):

    #Salva o arquivo e usa a funcao que retorna a data
    arq = open(arqdestino,'w')
    
    for j in range(len(tab)):
        #retorna todas as informacoes da pessoa par auma unica string
        tab[j] = tab[j][0]+','+RetornaData(tab[j][1])+','+tab[j][2]
    
        #Escreve no arquivo
        arq.write(tab[j])

    arq.close()
    

        
        
def VerifClass(tab):

    #Verifica se a tabela esta classificada
    for i in range(len(tab)-1):
        if tab[i] > tab[i+1]:
            return False
    
    return True
        
            
def main():

    #Classifica uma tabela pelos seguintes metodos:
    #Quick Recursivo
    #Quick Nao Recursivo
    #Sort do Python

    while True:

        try:
            
            arq_origem = input('Entre com o nome do arquivo origem: ')
            if arq_origem == 'fim': break

            arq_destino = input('Entre com o nome do arquivo destino: ')
            if arq_destino == 'fim': break
            
            tab = LeArquivo(arq_origem)

            #Copia tabela
            tabNR = tab[:]
            tabR = tab[:]
            #tabs = tab[:]

            #Classifica pelos 3 metodos e calcula o tempo
            t0 = time.clock()
            ClassQuickNaoRecursivo(tabNR,0,len(tabNR)-1)
        
            t1 = time.clock()
            ClassQuickRecursivo(tabR,0,len(tabR)-1)
            
            t2 = time.clock()
            ClassMetodoSort(tab)

            t3 = time.clock()
            
            #Verifica se as tabelas estao classificadas e printa o tempo
            if VerifClass(tabNR) == True and VerifClass(tabR) == True and VerifClass(tab) == True:
                
                print('Tempo para classificar a tabela: ')
                print()
                print('Metodo Quick Recursivo: ',t2 - t1,'segundos')
                print('Metodo Quick Nao Recursivo: ',t1 - t0,'segundos')
                print('Metodo sort() do Python:  ',t3 - t2,'segundos')
                print()
                
                SalvaArquivo(tab,arq_destino)      
        
        
        except Exception as e:
                print(e)


main()
