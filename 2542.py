def vencedor(podermarcos,poderleonardo):
        if podermarcos > poderleonardo :
                return "Marcos"
        if podermarcos < poderleonardo :
                return "Leonardo"
        return "Empate"        
        
if __name__=="__main__":
        while True:
                try:
                        numatrib=map(int,raw_input())
                        qtdcartas=map(int,raw_input().split(" "))
                        matrizmarcos=[]
                        matrizleonardo=[]
                        for i in range (0,qtdcartas[0]):
                                carta=map(int,raw_input().split(" "))
                                matrizmarcos.append(carta)
                        for i in range (0,qtdcartas[1]):
                                carta=map(int,raw_input().split(" "))
                                matrizleonardo.append(carta)                
                        cartasescolhidas=map(int,raw_input().split(" "))
                        atributo=int(raw_input())
                        podermarcos=matrizmarcos[cartasescolhidas[0]-1][atributo-1]
                        poderleonardo=matrizleonardo[cartasescolhidas[1]-1][atributo-1]
                        print vencedor(podermarcos,poderleonardo)
                except :   
                        break    