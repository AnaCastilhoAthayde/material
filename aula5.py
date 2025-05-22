nome = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a primeira nota do aluno: ")) #definimos a varial nota1 ela é do tipo float, e deve colocar input
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))

media = (nota1 + nota2 + nota3) /3 #estamos fzendo o calculo da media dos alunos

if media >= 7:
     print("APROVADO")
else:
  print("REPROVADO :(")







print (F"A média do aluno é {media:.2f} ")  #F significa fstring para eu conseguir colocar uma variavel entre aspas ""
#{media} coloca entre chaves porque colocamos a variavel na media na string
#:.2f significa quantas casas apos a virgula 