"""
Leet spek generator. Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras, como números por exemplo. A própria palavra leet admite muitas variações, como l33t ou 1337. O uso do leet reflete uma subcultura relacionada ao mundo dos jogos de computador e internet, sendo muito usada para confundir os iniciantes e afirmar-se como parte de um grupo. Pesquise sobre as principais formas de traduzir as letras. Depois, faça um programa que peça uma texto e transforme-o para a grafia leet speak.


Minha pesquisa principal
Carta	Possíveis contrapartes
A	4 , @ , /\ , /-\ , ? , ^ , is , 2
B	8 , |3 , ist , l³ , 13 , I3 , J3
C	( , [ , < , © , ¢
D	|) , |] , ⁇ , is , 1)
E	3 , € , & , £ , ál
F	|= , PH |, |*|-| , ²" , ⁇ , l
G	6 & 9
H	# , 4 , |-| , }{ , ]-[ , /-/ , )-(
EU	! , 1 , | , ][ , ⁇
J	_| , ¿
K	|< , |{ , |(, X
L	1 , |_ , £ , | , ][_
M	/\/\ , /v\ , |V| , ]V[ , |\/| , AA []V[] , |11 , /|\ , ^^ , (V) , |Y| , !!\/!
N	|\| , /\/ , /V , |V , /\\/ , |1 , 2 , ? , (\) , 11 , r , !\!
O	0 , 9 , () , [] , * , ° , <> , {[]}
P	9 , |° , p , |> , |* []D , ][D , |² , |? |, D
Q	0_ 0, 0
R	2 , |2 , 1² , ® , ? , √ , 12 , .
S	5 , $ , § , ? , 2 , s
T	7 , + , † '][' , |
U	|_| , ist [_] , v
V	\/ , |/ , \| , \'
W	\/\/ , VV , \A/ , \\' , uu , \^/ , \|/ , uJ
X	>< , )( , }{ , % , ? , × , ][
Y	`/ , °/ , ¥
Z	z, 2, "/_

Irei utilizar apenas a primeira contraparte

"""

def CoversorLeetSpeak(palavra):
    alfabetoLeet = ["4", "8", "(", "|)", "3", "|=", "6", "#", "!", "_|", "|<", "1", "/\/\\", "|\|",
                    "0", "9", "	0_ 0", "2", "5", "7", "|_|", "\/", "\/\/", "><", "`/", "z"]
    
    palavraEmLeet = ""

    for i in palavra:
        aux = ord(i)-65
        palavraEmLeet += alfabetoLeet[aux]

    return palavraEmLeet

    

def main():
    palavra = input("Insira uma palavra para a conversão em leetspeek: ").upper()
    print(CoversorLeetSpeak(palavra))

    return


if __name__ == "__main__":
    main()