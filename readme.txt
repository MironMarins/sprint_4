Nome: Fernando Paparelli Aracena RM: 551022

Nome: Filipe de Oliveira Mendes RM: 98959

Nome: Miron Gonçalves Martins RM: 551801

Nome: Paulo Henrique de Andrade Juniro RM: 99714

Nome: Vinícius Pedro de Souza RM: 550907

O programa foi feito para manipular(criar,atualizar,checar e eliminar dados) de nosso banco de dados.
o program irá criar diverços dicionarios, cujas informações neles colocas serão importadas para suas 
respectivas tabelas atraves das funções nos arquivos dentro da pasta ressources para nosso banco de dados.
o programa tambem conta com os arquivo auxilio.py que contará com dicionarios contendo valores equivalentes aos valores 
de tabelas em nosso banco de dados que foram feita para a manipulação do cliente, mas seus dados serviram
para constriuir um "resumo de chamada" ao final de uma chamada realizada, o arquivo codigo gerará um codigo numerico de oito 
digitos, o qual o cliente ultilizará para verificar ou manipular seus dados. main.py será o programa principal do cliente, será
atrave´z dele que o cliente interatividade com o programa total.

Programa "menu.py"

Conta com a função que criará o menu principal em main.py. A partir desse menu o usurio poderá decidir suas ações
sendo elas: " 1 Criar cadastro", onde o usuarario deverá colocar suas informações e as informações de seu veiculo para serem
quardadas no dicinario "cliente", que será quardado na lista "usuario". vale resaltar que o cliente tambem deverá colocar 
as informações de seu veiculo logo em seguida. Os veiculos estarão em uma lista "veiculos" no artributo "veiculos" do dicionario
cliente. Cada veiculo corresponde a um dicionario "V"
"2 cadastrar outro veiculo", onde o cliente podera adicionar outro veiculo (dicionario) à sua lista "veiculos"
"3 alterar informações", onde o cliente poderá arterar as informações apenas de seu veiculo, sendo as informações
de cliente são em grande parte imutaveis (id, cpf), não achamos que haveria necessidade de implementar um opção
para alterá-las
"4 consutar dados", onde o cliente podará ver seus dados pessoais e os dados de todos os seus veiculos, assim como
os dados de suas chamadas de modal CONTATO QUE ELE TENHA O CODIGO DA CHAMADA!!!
"5 - solicitação de modal", onde o cliente informará seu id e a placa do veiculo nessecitado, alem se esta carregando
alguma carga externa e qual dos problema mostrados no menu melhor definem seu situação, para poder chamar o auxilio mais
indicado. Pois as informações forem preenchidas o cliente receberá um codigo de chamada e escolherá se quiser ver o resumo 
de chamada
"6 - deletar impormações", onde o cliente deverá passar seu id para ou apagar sua conta completamente ou apenas apagar um 
veiculo de sua conta
"7 - sair", finaliza o programa

e a função seuVeiculo, que mostrará ao cliente atributos de veiculo correspondente aos dados de veiculos inseridos em nosso banco
de dados

Programa "codigo.py"

Conta apenas com uma função que criará um codigo de 8 digitos que servirá como codigo do cliente, codigo de chamada de modal e codigo de
carga de veiculo

Programa "auxilio.py"

Conta com seis funções que auxiliaram na indetentifaicação de um problema durante uma chamada de modal e na escolha de uma ajuda
apropriada, alem de criar uma lista com o resumo dos dados dessa chamada.
A função "auxilio", conta com o tipo de ajuda que será madanda para o cliente.
A função "problema", conta com um dicionarios de atributos numerados, cujos valores são referentes a tipos de problemas genricos que o cliente
pode estar tendo
A função "expecificacao", conta com valores numerados onde para onde o cliente poderá afunilar ainda mais o problema que o cliente
pode estar tendo.
A função "veiculoTotal", pega as informações do veiculo (peso,altura,comprimento,largura) e as junta com as informações de uma carga externa(se ouver)
de modo que os pesos e comprimetos serão somados e a maior altura e largura serão colocadas no dicionario veiculoTotal e essas informações
serão usadas para a excolha do melhor modal para essa chamada
A função "escolhaModal", usara as informações de pesoTotal da função veiculoTotal para selecionar o modal generico mais apropriado para o tipo
de veiculo necessitado
A função "resumoChamada", ela recebe as informações de problemas e de veiculo e as coloca no dicionerio resumoChamada, para em seguida
a colocalo na lista "chamada"
A lista "listaIdChamada" foi feita apenas para os ids chamadas sejão depositadas, para que se no caso de o usuario digitar um id inexiste
ele recebeba a menssagem "esse codigo não consta em nosso banco de dados" 

programa "cadastra.py"

Conta com duas listas e tres funções
as listas "listaPlacas" e "listaIdCliente", seriram apenas para guardar essas informações unicas de modo que no 
caso de o usuario digitar um id inexistente ou placa que não consta em seu cadastro recebeba a menssagem 
"esse codigo não consta em nosso banco de dados"
A função "cadastraCliente" pedirá informações ao usuario e as guardará no dicionario cliente, para que em seguida quarde essas informações
dentro da lista usuraio em main.py.
A função "cadastraV" pedirá informações sobre o veiculo do cliente para em seguida guarda-las no dicionario "V" que será em seguida
guardado na lista "veiculos" que esta no atribulo "veiculos" do dicionario "cliente" da função "cadastraCliente"

programa "main.py"

O programa central do nosso projeto, para seu funcinamento importações serão feitas por todos os outros programas.
Ele conta com a lista "cliente" que á qual o usurio podera colocar, alterar, ver ou deletar informações contanto que ele
tenha as chaves nessecitadas pelo programa para faze-lo (ids e numero de placas)
A varialvel "escolha" é referente as opçoes em "menu.py" enquanto a varialvel opcao será mais usada para navenar nos menus mais 
adentro do programa. 

É indicado que o usuario crie uma conta na opcao "1 - gostaria de realizar meu cadastro" antes de começar qualquer operação ou
poderá cair num looping que só será solucionado com a reinicilização do programa.

Obs: para não colocar muitas linhas repetidas com o loopins while esse comando foi usado apenas nas quatro primeiras opções
do menu principal, apenas para demonstrar uma solução para looping, estamos confiantes na habilidades de nossos usuarios de escreverem
seus codigos de forma correta quando forem pedidos    

Lembrando de SEMPRE GUARDAR O CÓDIGO DADO AO USOARIO AO FINAL DA REALIZAÇÃO DE SEU CADASTRO, ASSIM COMO A PLACA CADASTRADA DE SEU
VEICULO e CODIGO DE CHAMADA AO FINAL DE UMA CHAMADA pois é com esses codigos que o usoario poderá usar as funcionalidades desse programa

Vale resaltar que toda vez que um código for digitado de forma errada uma lista de opções aparecerá na tela
e o usoario poderá tentar digitar o código denovo




   

 


