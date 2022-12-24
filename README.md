# **Jogo da vida**
O game da vida, feito por **Conway**
Caracterizado por ser um automato celular, originalmente
utilizado para usar um espaço bidimensional, embora existam também
versoes tridimensionais, em que cada elemento (celula) só pode ter
dois estados 0 e 1 (ativo, inativo. vivo, morto).  
A partir desse ponto, se entra a regra de vizinhança, onde
um automato pode-se ter 8 vizinhos, que seriam as 8 celulas que
estão ao seu redor. Essas são as celulas das quais se ira aplicar as
regras de transformação que é composta pelas seguintes condições:  
  
Dado uma celula na condição atual ativa, a celula permanece ativa se
possuir ao menos duas ou tres celulas vizinhas também ativas, caso contrario
a celula passará a estar inativa. O contrario para o mesmo caso.
  
  
  

## **Definições**
Elementos que o integra:  
Espaço: é uma area bidimensional ou um volume tridimensional em que se manifesta o automato celular.
O Automato celular é sempre feito de infinitos elemtentos que trabalham unissono(padronizados) 
e que devem ser bem organizados em um plano ou em um volume.
Cada uma dessas celulas se caracterizam por ter um valor.
  
Estado: é o conjunto de valores possiveis para cada elemento, podendo ser binarios por exemplo ou multiplos valores.  
  
Regra da vizinhança: determina quais elementos são considerados contíguos a cada elemento.
  
Regras de transformação: conjunto de regras que determinam o estado de cada elemento 
em função de seu estado anterior e dos elementos vizinhos.  
Isso faz com que ao longo do tempo, o estado dos elementos dependam dos seus vizinhos e também de si mesmo
causando uma interdependencia entre o estado de cada elemento e o estado do conjunto de elemento das coisas ao redor.  
  
Configuração inicial:  
É o estado inicial dos elementos que demonstram o comportamento inicial
antes da primeira iteração.
  
Fronteira:  
determina o estado dos elementos fora do espaço (elementos externos)  
  
  
  
  
## Simulação de ideia:  
  
geração = vetor(N) (N é o número de células)  
  
nova_geração = vetor(N)  
  
evolução = matriz(MAX, N) (MAX é o numero de gerações)  
  
inicializar geração (setar configuração inicial)  
  
para i = 1 até MAX  
    evolução[i,:] = geração  
    # percorre cada célula da geração atual  
    para j = 1 até N  
        aplicar regra de transição na célula j, gerando nova_geração  
    geração = nova_geração  
plot result  


