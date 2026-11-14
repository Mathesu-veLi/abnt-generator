# O pacote abntex2cite (manual)

> Texto extraído de `abntex2/doc/abntex2cite.pdf` (abnTeX2 v-1.9.7) com
> `pdftotext -layout`; numeração de página removida. Preserva a quebra de
> linha do PDF, então palavras podem aparecer hifenizadas no fim da linha.
> Para regenerar: `python3 scripts/pdf_to_md.py`.

O pacote abntex2cite:
   Estilos bibliográficos compatíveis com a ABNT NBR
                            6023

                             Lauro César Araujo
                        <http://www.abntex.net.br/>
                       24 de novembro de 2018, v-1.9.7

                                        Resumo
         Este manual é parte integrante da suíte abnTEX2 e descreve os estilos
     bibliográficos abntex-alf.bst e abntex-num.bst, responsáveis pelos estilos bibtex
     compatíveis com a ABNT NBR 6023.

Sumário
1 Escopo                                                                                  3

2 Créditos aos autores originais                                                          3

3 O novo pacote biblatex-abnt                                                             3

4 Considerações iniciais                                                                  4
  4.1 Se puder, evite a ‘norma’ ANBT NBR 6023 . . . . . . . . . . . . .                   4
  4.2 Cuidado: normas nebulosas! . . . . . . . . . . . . . . . . . . . . . .              4
  4.3 Até que ponto este estilo bibtex cumpre a ‘norma’ 6023? . . . . . .                 4
  4.4 O abntex2cite está em conformidade com a ABNT NBR 6023:2002?                        5
  4.5 Em que ambiente foram desenvolvidos os estilos? . . . . . . . . . .                 5

5 Uso de abntex2cite                                                                      6
  5.1 Seleção dos estilos . . . . . . . . . . . . . . . . . . . . . . . . . . .           6
      5.1.1 Citação numérica [num] . . . . . . . . . . . . . . . . . . . .                6
      5.1.2 A citação no texto . . . . . . . . . . . . . . . . . . . . . . .              6
      5.1.3 Conteúdo da referência bibliográfica . . . . . . . . . . . . .                7
      5.1.4 Alteração do estilo de chamada [num] . . . . . . . . . . . .                  7
      5.1.5 Citação alfabética por autor-data [alf] . . . . . . . . . . .                 8
  5.2 Cuidados com a acentuação . . . . . . . . . . . . . . . . . . . . . .               8
  5.3 Siglas e letras maiúsculas nos títulos das referências . . . . . . . .              8
  5.4 Autor com sobrenome composto . . . . . . . . . . . . . . . . . . .                  9
  5.5 URLs longas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .             9

6 Utilização da citação por sistema autor-data [alf]                                     10

7 Alteração dinâmica das opções do estilo [citeoption]                             10
  7.1 Como proceder . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      11
      7.1.1 Usando abntex2cite e citeoption . . . . . . . . . . . . . . .          11
      7.1.2 Sem usar abntex2cite nem citeoption . . . . . . . . . . . .            11
      7.1.3 Como agrupar várias opções . . . . . . . . . . . . . . . . . .         11
      7.1.4 Cuidados a serem tomados com opções . . . . . . . . . . . .            12
  7.2 Quando começa a valer a opção? . . . . . . . . . . . . . . . . . . .         12
      7.2.1 Sistema numérico [num] . . . . . . . . . . . . . . . . . . . .         12
      7.2.2 Sistema alfabético por autor-data [alf] . . . . . . . . . . .          12
  7.3 Comandos controlados por citeoption . . . . . . . . . . . . . . .            12
  7.4 Opções agrupadas . . . . . . . . . . . . . . . . . . . . . . . . . . .       18

8 Novos campos                                                                     19
  8.1 Endereços de internet (url) . . . . . . . . . . . . . . . . . . . . . .      19

9 Novas entradas .bib                                                              19
  9.1 @ABNT-option — Mudança no estilo ABNT . . . . . . . . . . . . .              23
  9.2 @hidden — Entrada escondida . . . . . . . . . . . . . . . . . . . .          23
  9.3 @ISO-option — Mudança de estilo ISO . . . . . . . . . . . . . . .            23
  9.4 @journalpart — Partes de periódicos . . . . . . . . . . . . . . . .          23
  9.5 @monography — Monografias . . . . . . . . . . . . . . . . . . . . .          23
  9.6 @patent — Patentes . . . . . . . . . . . . . . . . . . . . . . . . . .       23
  9.7 @thesis — Teses de modo geral . . . . . . . . . . . . . . . . . . .          23

Referências                                                                        23

A Questões específicas da ‘norma’ 6023 e sua implementação                         91
  A.1 A ‘norma’ em contradição com ela mesma . . . . . . . . . . . . . .           91
  A.2 Elementos essenciais e complementares . . . . . . . . . . . . . . . .        92
  A.3 Partes de coletâneas [incollection] e livros [inbook] . . . . . . .          92
  A.4 Eventos, Anais, Proceedings . . . . . . . . . . . . . . . . . . . . . .      92
  A.5 Nomes pessoais [author] . . . . . . . . . . . . . . . . . . . . . . . .      93
      A.5.1 Comentário: . . . . . . . . . . . . . . . . . . . . . . . . . . .      93
  A.6 Título (title) e subtítulo (subtitle) . . . . . . . . . . . . . . . .        93
      A.6.1 Comentário: . . . . . . . . . . . . . . . . . . . . . . . . . . .      94
  A.7 Ausência de local (address) e editora (publisher) . . . . . . . . .          94
      A.7.1 Comentário: . . . . . . . . . . . . . . . . . . . . . . . . . . .      94
  A.8 Teses, Dissertações, Monografias . . . . . . . . . . . . . . . . . . .       94
      A.8.1 Comentário . . . . . . . . . . . . . . . . . . . . . . . . . . .       94

B Referências segundo o tipo de entrada bibtex                                     95

Lista de Tabelas
   1    Tabela de conversão de acentuação. . . . . . . . . . . . . . . . . . .      8
   2    Opções de alteração dos estilos bibliográficos: formatação . . . . .       13
   3    Opções de alteração dos estilos bibliográficos: et al. . . . . . . . . .   14
   4    Opções de alteração dos estilos bibliográficos: composição . . . . .       15
   5    Opções de alteração dos estilos bibliográficos: funcionamento . . .        16
   6    Opções de alteração dos estilos bibliográficos: url . . . . . . . . . .    17

    7    Subestilos de diversas instituições . . . . . . . . . . . . . . . . . . .     18
    8    Versão das ‘normas’ a ser usada . . . . . . . . . . . . . . . . . . . .       18
    9    Campos relativos a sites de Internet e documentos eletrônicos . . .           19
    10   Campos relativos a ISBN e ISSN. . . . . . . . . . . . . . . . . . . .         20
    11   Campos relativos a subtítulos e seções de revistas. . . . . . . . . .         20
    12   Campos relativos a autoria. . . . . . . . . . . . . . . . . . . . . . .       21
    13   Campos relativos a descrição física do documento. . . . . . . . . .           22
    14   Campos relativos a descrição de uma conferência para entradas do
         tipo proceedings, inproceedings e conference. . . . . . . . . .               22
    15   Campos relativos teses e monografias. . . . . . . . . . . . . . . . .         22
    16   Citações bibliográficas usadas neste documento ordenadas segundo
         o tipo de entrada. . . . . . . . . . . . . . . . . . . . . . . . . . . . .    95

1     Escopo
O objetivo deste manual é descrever os estilos bibliográficos abntex-alf.bst e abntex-
num.bst, responsáveis pelos estilos bibtex compatíveis com a ABNT NBR 6023.
   Este documento é parte integrante da suíte abnTEX2 e é complementado pelo
documento 221.
   Para referências à classe abntex2, consulte 222.

2     Créditos aos autores originais
Este documento é derivado do documento Estilo bibtex compatível com a ‘norma’
6023 da ABNT - Versão 1.44 escrito por G. Weber e atualizado por Miguel V.
S. Frasson em 23 de julho de 2003 no âmbito do projeto abnTEX hospedado
originalmente em <http://codigolivre.org.br/projects/abntex> 1 .
    A equipe do projeto abnTEX2, observando a LaTeX Project Public License,
registra que os créditos deste manual são dos autores originais.

3     O novo pacote biblatex-abnt
O biblatex-abnt2 (223) é um projeto em andamento que define em BibLATEX3 as
regras de formatação bibliográfica da ABNT NBR 6023 e de citação da ABNT
NBR 10520. Sendo totalmente implementado em LATEX, ele substitui os arquivos
de estilo bibtex abntex2-alf.bst, abntex2-num.bst e o pacote abntex2cite.sty descrito
neste manual. Com isso, o biblatex-abnt deve aposentar os estilos de formatação
do abntex2cite e utilizar exclusivamente o biblatex-abnt e as macros padrões do
BibLATEX.
   1 O documento original pode ser lido em <https://github.com/abntex/abntex2-old-binary/

blob/master/abntex1-manuais/abnt-bibtex-doc.pdf>
   2 Ver <https://ctan.org/pkg/biblatex-abnt> e <https://github.com/abntex/biblatex-abnt>.
   3 Ver <https://ctan.org/pkg/biblatex>

4     Considerações iniciais
4.1    Se puder, evite a ‘norma’ ANBT NBR 6023
A primeira equipe do abnTeX usou a ABNT NBR 6023:2000 e outras normas da
ABNT vigentes, em média, até 2004. Naquela época as normas eram confusas,
inconsistentes e repletas de exemplos incoerentes. Atualmente a situação não é
muito diferente. Porém, percebe-se que houve uma tentativa mínima dos comitês
da ABNT em tornar o labor de interpretar as normas menos árduo. De toda forma,
acompanhamos os autores originais do abnTeX e recomendamos: “Se puder não
use e não peça para ninguém usar.”
    Existem centenas de estilos bibliográficos mundo a fora. Use o próprio bibtex
para experimentar. Se você quiser entender porque não se deveria usar, em nenhuma
circunstância, a ‘norma’ 6023, então leia o restante do texto. Porém se você estiver
sendo forçado a usar a ‘norma’ da ABNT então vá em frente e boa sorte!
    Porque então fizemos o estilo bibliográfico razoavelmente compatível com a
‘norma’? Nós queremos incentivar o uso do LATEX e queremos ajudar os pobres-
coitados, alguns dos quais nós mesmos, que são ou serão forçados, por estupidez
burocrática, a usar ‘normas’ da ABNT.
    A Subseção 4.4 descreve a compatibilidade do abnTEX2 com as normas mais
recentes e vigentes da ABNT.

4.2    Cuidado: normas nebulosas!
Nós elaboramos os estilos debruçados diretamente sobre os originais da ABNT
e as seguimos escrupulosamente. Mas não se iluda! O que a sua coordenação de
pós-graduação, ou orientador, ou chefe etc., entendem por ‘normas ABNT’ pode
não ter qualquer vínculo com a realidade. Por isso não garantimos que ao usar os
estilos do abnTEX você esteja em conformidade com as normas da sua instituição
ou empresa.
    Por que isso acontece? Em geral porque os originais das ‘normas’ da ABNT
não são gratuitas e as pessoas acabam se orientando na base do ‘ouvir falar’, ou
livros que supostamente se baseiam nessas ‘normas’. Acredite: nenhum material
que encontramos (livros, roteiros de biblioteca, normas de pós-graduação, material
encontrado na internet) implementa as ‘normas’ da ABNT corretamente.
    Um exemplo clássico é o sistema de chamada numérico (citação numérica, usada
neste documento). Embora todas as ‘normas’ da ABNT(2, 224, 3, 4) ‘autorizem’
seu uso a maioria das instituições, orientadores, membros de banca, revisores do
seu artigo. . . irão dizer que isso não é ABNT. Acredite se quiser.
    As regras particulares de algumas instituições foram acomodadas em termos de
subestilos. Consulte a Tabela 7 e avise-nos se houver regras particulares de sua
instituição para que possam ser disponibilizadas para outras pessoas.

4.3    Até que ponto este estilo bibtex cumpre a ‘norma’ 6023?
O estilo ainda está em fase final de desenvolvimento. Praticamente todos os tipos
de entrada funcionam bem.
   Tanto o estilo numérico (abnt-num.bst ou [num]) quanto o alfabético
(abnt-alf.bst ou [alf]) funcionam razoavelmente bem e devem gerar uma lista
bibliográfica bastante compatível. O uso deste estilo lhe dará um resultado muito

 superior a uma lista formatada à mão, principalmente se você não tiver acesso a
‘norma’ original (2).
     Fuja das ‘interpretações’ dessa norma que proliferam na Internet. Nenhuma
 delas faz muito sentido. Mesmo os tais livros de “Metodologia do Trabalho Científico”
 contém interpretações muito peculiares das ‘normas’ da ABNT. Se você está para
 entregar sua tese, já tem uma base bibtex formada, o abntex2cite vai resolver seu
 problema, com toda certeza.
     Até o momento 173 exemplos estão sendo reproduzidos corretamente e 12
 parcialmente. Alguns (3) não puderam ser reproduzidos por questões diversas.
Todos os exemplos que tentamos reproduzir estão inseridos neste documento.
     Sempre que possível colocamos um comentário em notas de rodapé com ex-
 plicações do problema dos exemplos que não conseguimos reproduzir de forma
 completa. Alguns exemplos jamais serão reproduzidos corretamente ou por serem
 estranhos demais ou porque estão em desacordo com a própria ‘norma’. As teses
 são um exemplo notório desse último caso.
     A ‘norma’ 6023:2000 (2) é complicada e cheia de inconsistências. Jamais será
 possível gerar um estilo bibtex totalmente consistente com a ‘norma’, até porque
 nem a ‘norma’ é compatível com ela mesma. Um bom estilo bibliográfico deve
 ter uma linha lógica para formatação de referências. Assim, com alguns poucos
 exemplos, qualquer pessoa poderia deduzir os casos omissos. Nesse sentido, a
‘norma’ 6023 trafega pela contra-mão. É quase impossível deduzir sua linha lógica.
 O problema mais grave, no entanto, fica pela maneira de organizar nomes. A ABNT
 quebrou o sobrenome em duas partes. Normalmente se fala apenas em “last name”,
 mas agora temos o “last last name” graças à ABNT. Isso não apenas é problemático,
 pelo menos do ponto de vista do bibtex, mas é também um desrespeito ao autor
 citado.

4.4    O abntex2cite está em conformidade com a ABNT NBR
       6023:2002?
Esta versão do manual dos estilos bibliográficos do abnTEX2 contém os exemplos
da versão anterior da norma ABNT NBR 6023, ou seja, da versão 2000. A norma
vigente é a 6023:2002. Porém, as alterações na forma de referenciamento bibliográfico
na nova versão da norma já foram incorporados ao código do abnTEX2.
    A atualização deste documento é uma tarefa em andamento4 . De todo modo,
este manual pode ser usado como referência de uso dos estilos providos pelo
abnTEX2 até que os exemplos sejam completamente atualizados.

4.5    Em que ambiente foram desenvolvidos os estilos?
Os estilos foram desenvolvidos em Conectiva Linux 8, e a implementação TEX é o
tetex versão 1.0.7.
    O abnTEX2 foi desenvolvido em um Mac OS X, testado em Linux Ubuntu versão
14.04 e em Windows XP SP 2, 7, 8 e 10, nas distribuições MikTeX e TeXLive.
   4 <https://github.com/abntex/abntex2/issues/29>

                              5       Uso de abntex2cite
                              5.1     Seleção dos estilos
                              5.1.1     Citação numérica [num]
\usepackage[num]abntex2cite   Diferente do que muita gente imagina, o sistema numérico é ‘permitido’ pela
                              ‘norma’(2) em sua seção 9.1.5 Se você quiser usar este estilo de citação utilize a
                              opção [num] (arquivo abnt-num.bst). Selecione-o com o comando usepackage no
                              preâmbulo:

                              \usepackage[num]{abntex2cite}

                               Com isso as chamadas no texto serão compatíveis com os exemplos 9.1 da
                           ‘norma’(2).
        \bibliographystyle     Alternativamente, você pode não selecionar o pacote e só colocar o estilo
                            bibliográfico:

                              \bibliographystyle{abnt-num}

                                 Dessa forma, as citações no texto seguirão o padrão do LATEX, porém a biblio-
                              grafia será formatada conforme o padrão brasileiro.

                              5.1.2     A citação no texto
                     \cite    No texto você deve inserir as citações com os comandos \cite e \citeonline.
               \citeonline    Veja os exemplos abaixo.

                                                                                     Elétrons podem relaxar via interação
                              Elétrons podem relaxar via interação
                                                                                     elétron-fônon(225).
                              elétron-fônon\cite{Tsen86}.

                                                                                     Segundo a referência 117 entende-se que
                              Segundo a referência \citeonline{8.1.1.2}
                                                                                     ...
                              entende-se que \ldots\

                 \citeyear        O estilo abntex2cite ainda disponibiliza os comandos \citeyear, \citeauthor
               \citeauthor    e citeauthoronline. O uso de \citeyear e citeauthoronline é igual ao do
         \citeauthoronline    estilo autor-data ([alf]) como mostrado nos seguintes exemplos:

                                                                                             Em 1986 Tsen e Morkoç mostra-
                              Em \citeyear{Tsen86} \citeauthoronline{Tsen86}
                                                                                             ram que elétrons podem relaxar
                              mostraram que elétrons podem relaxar via
                                                                                             via interação elétron-fônon(225).
                              interação elétron-fônon\cite{Tsen86}.

                                  5 Você não faz ideia do número de pessoas (especialmente funcionários de pós-graduação,

                               orientadores e membros de banca) que simplesmente não acreditam que o sistema numérico seja
                              ‘permitido’ pela ‘norma’. E não adianta ‘esfregar’ o original da ‘norma’ na cara deles.

                     O uso de citeauthor é modificado em relação ao estilo autor-data ([alf])
                  como se vê no exemplo:

                                                                    Em 1986 Tsen e Morkoç(225) mostra-
                  Em \citeyear{Tsen86} \citeauthor{Tsen86}
                                                                    ram que elétrons podem relaxar via in-
                  mostraram que elétrons podem relaxar via
                                                                    teração elétron-fônon.
                  interação elétron-fônon.

                  5.1.3   Conteúdo da referência bibliográfica
     \citetext    Você pode imprimir o conteúdo da referência bibliográfica de uma citação com a
                  macro \citetext{hlista de keysi}, como no exemplo:
                                          TSEN, K. T.; MORKOÇ, H. Population relaxation time of none-
                                          quilibrium LO phonons and electron-phonon interactions in GaAs–
                  \citetext{Tsen86}       Alx Ga1−x As multiple-quantum-well structures. Phys. Rev. B, v. 34,
                                          p. 4412–4414, 1986.

                  5.1.4   Alteração do estilo de chamada [num]
                  A norma NBR 10520:2002 (226) cita dois estilos de chamada numérica: entre
                  parênteses, no texto (padrão no abntex2cite) ou como sobrescrito, sem parênteses
                  ou colchetes:

                    1. para que . . . à sociedade[10]
                    2. para que . . . à sociedade10

\citebrackets[]
\citebrackets()      Para a opção 1, utilize:
\citebrackets{}

                  \usepackage[num,overcite]{abntex2cite}
                  \citebrackets()

                     Para a opção 2, utilize:

                  \usepackage[num,overcite]{abntex2cite}
                  \citebrackets{}

                      Como o segundo estilo entra em conflito com a numeração das notas de rodapé,
                  recomenda-se não utilizar notas de rodapé com citações numéricas. Também no
                  estilo sobrescrito não se deve deixar espaço entre o texto e a citação.
                      Para usar colchetes (citação padrão no LATEX), coloque no preâmbulo do seu
                  texto:

                  \citebrackets[]

                              5.1.5   Citação alfabética por autor-data [alf]
\usepackage[alf]abntex2cite   Se você quiser usar o estilo de citação alfabético (seção 9.2 da ABNT NBR
                              6023:2000(2)), utilize [alf] (que utilizará o arquivo abnt-alf.bst).

                              \usepackage[alf]{abntex2cite}

                                  É possível utilizar o estilo de formatação de bibliografias sem, no entanto, utilizar
                              a formatação das citações no texto. Nesse caso, não inclua o pacote abntex2cite no
                              preâmbulo, mas inclua \bibliographystyle{abnt-alf} imediatamente antes do
                              comando \bibliography{harquivo-de-referencias-bibi}:

                              \bibliographystyle{abnt-alf}
                              \bibliography{arquivo-de-referencias-bib}

                                 O uso do estilo de formatação sem o uso do pacote de citação anbtex2cite
                              pode trazer resultados inesperados. Analise se o resultado é adequado as suas
                              necessidades.
                                 Mais informações sobre o uso do estilo bibliográfico autor-ano estão disponíveis
                              no documento 221.

                              5.2     Cuidados com a acentuação
                              Normalmente não há problemas em usar caracteres acentuados em arquivos bibli-
                              ográficos (*.bib). Como mostrado em (54), não há problema algum em escrever
                              o título, tipo ou local de publicação com os caracteres acentuados normalmente.
                              Porém, como as regras da ABNT exigem a conversão do autor ou organização para
                              letras maiúsculas, é preciso observar o modo como se escrevem os nomes dos autores.
                              Na Tabela 1 você encontra alguns exemplos das conversões mais importantes.
                              Preste atenção especial para ‘ç’ e ‘í’ que devem estar envoltos em chaves. A regra
                              geral é sempre usar a acentuação neste modo quando houver conversão para letras
                              maiúsculas (ou seja, nos autores).

                                                 Tabela 1: Tabela de conversão de acentuação.

                                                              acento    bibtex
                                                              àáã       \‘a \’a \~a
                                                              í         {\’\i}
                                                              ç         {\c c}

                              5.3     Siglas e letras maiúsculas nos títulos das referências
                              A norma ABNT NBR 6023:2002 não determina que os títulos das referências
                              estejam ou não em letras maiúsculas. Na versão anterior, se houvesse alguma

referência com uma letra ou conjunto de letras que precisasse necessariamente
ficar em letras maiúsculas, era necessário colocar os elementos entre chaves, por
exemplo: {{C}onstituiçãoo da {R}epública {F}ederativa do {B}rasil}.
    Esta é uma característica de muitos estilos bibliográficos para bibtex que colo-
cam em maiúscula somente a primeira palavra do título. No entanto, é inconveniente
e trabalhoso para aqueles que lidam com bibliografias cujo títulos incluem siglas ou
substantivos próprios. Desta forma, nesta versão dos estilos abntex2-cite-alf e
abntex2-cite-num, pode-se simplesmente escrever em maiúsculas o que se desejar
nos títulos, por exemplo em (54):

 title    ={Constituição da República Federativa do Brasil}

    Notar que os autores continuam sendo transpostos em maiúsculas, como pre-
coniza a ABNT NBR 6023:2002. Se, no entanto, não desejar seguir esta regra,
crie um novo arquivo .bst (por exemplo, novoestilo.bst)a partir do estilo
usado (abntex2-cite-alf ou abntex2-cite-num) e retire todas as expressões
"u" change.case$, lembrando-se de indicar o novo arquivo como estilo, por exem-
plo, \bibliographystyle{novoestilo}, e colocar o arquivo criado na mesma
pasta em que está compilando o documento.

5.4      Autor com sobrenome composto
Para compor entradas bibliográficas para autores com sobrenome composto (Filho,
Jr.,Neto, Sobrinho etc.) pode-se proceder segundo o seguinte exemplo. Para inserir
uma referência cujo autor seja impresso como BARBOSA NETO, J. F., que é o
padrão estabelecido pelas normas da ABNT, use:

   @ARTICLE{FerraoKaizoAll2001,
   ...
   author = {José Francisco Barbosa{ }Neto},
   ...
   }

   Note que há um espaço entre as chaves: { }.
   Ou então:

   @ARTICLE{FerraoKaizoAll2001,
   ...
   author = {Barbosa, Neto, José Francisco},
   ...
   }

5.5      URLs longas
O pacote lida com URLs longas carregando os pacotes url e breakurl onde
necessário (ou seja, carregando o último em compilação com LATEX, ou em “modo
dvi”). Estes pacotes, contudo, não inserem quebras de linha em URLs com hífens
por padrão.

   Caso sejam necessárias quebras de linha com URLs longas e hifenizadas, deve-
se passar as opções correspondentes para tais pacotes, chamando-os antes do
abntex2cite:

Compilação com latex (ou em “modo dvi”) Ao compilar o arquivo com
   latex, deve-se passar a opção hyphenbreak ao pacote breakurl:

       \usepackage{hyperref}
       \usepackage[hyphenbreaks]{breakurl}
       \usepackage{abntex2cite}

       Verifique a documentação do pacote breakurl.6
Compilação com pdflatex, lualatex ou xelatex Ao compilar com pdflatex,
   lualatex ou xelatex deve-se passar a opção hyphens ao pacote url:

          • Usando o pacote abntex2cite autonomamente (ou seja, sem a classe
            abntex2): Com outras classes (que não carregam o pacote hyperref) é
            preciso passar a opção carregando o pacote url antes do abntex2cite:

            \usepackage[hyphens]{url}
            \usepackage{abntex2cite}

          • Com a classe abntex2: A classe abntex2 carrega o pacote hyperref,
            que por usa vez carrega o url causando um erro do tipo “option clash” se
            o procedimento descrito acima for empregado. Para evitar isso, deve-se
            passar a opção hyphens ao url antes ou durante o carregamento da
            classe.

            \documentclass[hyphens]{abntex2}

6      Utilização da citação por sistema autor-data
       [alf]
Veja documento específico Ref. 221.

7      Alteração dinâmica das opções do estilo [citeoption]
Você pode alterar algumas maneiras do estilo bibliográfico sem ter de alterar o
arquivo em si7 . O método usado aqui permite até mesmo que se altere o estilo
de uma citação para outra. Isso está sendo usado neste documento que você está
lendo. Todas as opções estão apresentadas nas tabelas 2–5.
    6 <http://texdoc.net/pkg/breakurl>
  7 Até onde sabemos, os estilos bibliográficos do abnT X são os únicos que podem alterar o
                                                       E
comportamento do bibtex com comandos dentro do arquivo LATEX.

                7.1     Como proceder
                7.1.1   Usando abntex2cite e citeoption
  \citeoption   Você deve utilizar o comando \citeoption e incluir a base abnt-options em
                \bibliography, como no exemplo, que ativa a opção de usar primeiro o nome
                completo do autor:

                \citeoption{abnt-full-initials=yes}

                   Você também pode definir suas opções logo no carregamento do estilo, por
                exemplo:

                \usepackage[num,abnt-full-initials=yes]{abntex2cite}

                7.1.2   Sem usar abntex2cite nem citeoption
     \nocite    Você pode se valer das opções aqui apresentadas sem usar o pacote abntex2cite.
                Para isso você precisa usar o comando \nocite como no seguinte exemplo:

                \nocite{abnt-full-initials=yes}

                    O único inconveniente desse método (que funciona bem) é que você vai ter de con-
                viver constantemente com a mensagem de que a referência abnt-full-initials=yes
                não foi definida.

                7.1.3   Como agrupar várias opções
@ABNT-options   Você pode agrupar opções criando uma entrada do tipo ABNT-options em um
  \citeoption   arquivo de bibliografias (tipo .bib), por exemplo:

                @ABNT-options{minhasopcoes,
                  abnt-emphasize="\emph",
                  abnt-full-initials="no",
                  abnt-show-options="warn",
                  abnt-thesis-year="final",
                  key="x"}

                   Desse modo, deve deve chamar suas opções assim \citeoption{minhasopcoes}.
                   A Subseção 7.2 explica a função do campo key.
                   O comando \citeoption força o LATEX a gerar uma entrada de citação no
                arquivo auxiliar (.aux) que é processada pelo bibtex. Se você não quiser usar o
                arquivo abnt-options, você pode colocar uma entrada tipo ABNT-options no seu
                arquivo .bib. É essa entrada que você deve citar com \citeoption. Veja o arquivo
                abnt-bibtex-doc.bib para exemplos dessa entrada. As opções disponíveis estão
                descritas nas Tabela 2, na Tabela 4 e na Tabela 5.

                      7.1.4   Cuidados a serem tomados com opções
                      Note que o bibtex somente processa cada entrada bibliográfica uma única vez. Ou
                      seja, mesmo que exista mais de uma entrada \citeoption no texto, ela não será
                      processada novamente. Isso acontece porque o comando \citeoption nada mais é
                      do que um comando tipo \cite que é processado pelo bibtex como uma simples
                      entrada bibliográfica.

                      7.2     Quando começa a valer a opção?
                      O momento a partir do qual a opção selecionada por \citeoption começa a
                      funcionar depende do estilo bibliográfico usado. A Subsubseção 7.2.1 descreve o
                      uso no sistema numérico e a Subsubseção 7.2.2, no sistema alfa-numérico.

                      7.2.1   Sistema numérico [num]
                      As opções valem a partir do ponto do texto onde aparece o comando \citeoption.
                      Se você quiser que a opção esteja valendo para todas as entradas então use
                      \citeoption antes de qualquer uso de \cite ou \citeonline.

                      7.2.2   Sistema alfabético por autor-data [alf]
                      As opções valem a partir do ponto onde a entrada aparece na ordem alfabética,
                      independente do ponto no texto onde a citação foi feita. Isso é controlado por meio
                      do campo key. Se você quiser que as opções estejam valendo desde o início você
                      deve selecionar key de maneira a fazer a opção aparecer primeiro na ordenação
                      alfabética, como por exemplo key={a}. Ao usar \citeoption com [alf] esteja
                      atento aos seguintes fatos:

                        1. é muito difícil controlar a posição exata em que a opção começa a valer, a
                           menos que você escolha um key bem radical como ={aaaa}, que garante que
                           esta opção será processada antes de todas as outras entradas bibliográficas.
                           Este recurso é usado no arquivo abntex2-options.bib;
                        2. na prática, em geral você vai querer que uma opção esteja valendo para todas
                           as suas referências. Então você pode usar as opções predefinidas no arquivo
                           abntex2-options.bib;
                        3. você não pode usar \nocite{*} ou \cite{*} junto com o arquivo abntex2-options.bib,
                           pois isso chamaria todas as opções ao mesmo tempo.

                         O controle de onde a opção aparece é bem mais delicado no estilo [alf] do
                      que no estilo [num]. Sugerimos ficar atento ao posicionamento usando a opção
                      abnt-show-options=list e remover essa opção quando o documento estiver na
                      redação final.
                         Veja também outras opções de alteração no documento 221.

                      7.3     Comandos controlados por citeoption
\bibtextitlecommand    O comando \bibtextitlecommand{htipo de entradai}{hcampo a ser formatadoi}
                      permite que formatações adicionais da bibliografia sejam introduzidas. Veja o
                      resultado para a referência 19:

Tabela 2: Opções de alteração da formatação dos estilos bibliográficos. As opções
padrão (default) são sublinhadas ou indicadas. Também indicados as entradas que
já estão definidas em abntex2-options.bib.

 campo                          opções    descrição
 abnt-emphasize                           Seleciona o estilo de fonte do grifo. Po-
                                          dem ser usadas quaisquer combinações
                                          de comandos de fonte, mas apenas \bf
                                          (negrito) e \em (ênfase) são compatíveis
                                          com a ‘norma’ 6023.
 abnt-emphasize=em              \emph     opção padrão.
 abnt-emphasize=bf            \textbf
 abnt-ldots-type                          (somente [alf]) determina de que ma-
                                          neira deve ser composto as “. . .” nas
                                          chamadas.
 abnt-ldots-type=normal        normal     usar \ldots normal do LATEX.
 abnt-ldots-type=math            math     usar ambiente matemático, ou seja
                                          $\ldots$.
 abnt-ldots-type=none             none    não usa nada.
 abnt-ldots-type=text             text    simplesmente usa “...”, o espaçamento
                                          fica ruim mas pode ser útil na conversão
                                          para HTML.
 abnt-title-command                       Controla o uso do comando (veja se-
                                          ção 7.3) \bibtextitlecommand.
 abnt-title-command=no              no    não usa esse comando.
 abnt-title-command=yes            yes    usa esse comando.

Tabela 3: Opções de alteração da formatação de et al. na composição dos estilos
bibliográficos.

 campo                                     opções   descrição
 abnt-and-type                                      Opção específica do estilo [alf] veja
                                                    referência 221.
 abnt-dont-use-etal                                 Opção obsoleta veja abnt-etal-cite.
 abnt-etal-cite                                     Opção específica do estilo [alf] veja
                                                    referência 221.
 abnt-etal-list                                     controla como e quando os co-autores
                                                    são substituídos por et al. na lista bi-
                                                    bliográfica. Segundo o ítem 8.1.12(2) é
                                                    facultado indicar todos os autores se isto
                                                    for indispensável. Note que a substitui-
                                                    ção por et al. continua ocorrendo sempre
                                                    se os co-autores tiverem sido indicados
                                                    como others.
 abnt-etal-list=0                              0    não abrevia a lista de autores.
 abnt-etal-list=2                              2    abrevia com mais de 2 autores.
 abnt-etal-list=3                              3    abrevia com mais de 2 autores.
 ..                                            ..
  .                                             .
 abnt-etal-list=5                              5    abrevia com mais de 5 autores.
 abnt-etal-text                                     Texto a ser usado, tanto na chamada
                                                    quanto na bibliografia, quando a lista
                                                    de autores é abreviada.
 abnt-etal-text=none                    none        não usa qualquer texto.
 abnt-etal-text=default               et al.        usa ‘et al.’.
 abnt-etal-text=emph           \emph{et al.}        usa ênfase: ‘et al.’.
 abnt-etal-text=it           \textit{et al.}        usa itálico: ‘et al.’.

   Tabela 4: Opções de alteração da composição dos estilos bibliográficos.

campo                                opções     descrição
abnt-full-initials                              Seleciona se os prenomes são por extenso
                                                (quando disponível na base).
abnt-full-initials=no                      no   abreviado;
abnt-full-initials=yes                    yes   por extenso. Exemplos: 72, 113, 114,
                                                150.
abnt-last-names                                 Determina de que maneira devem ser
                                                tratados os sobrenomes. Para uma dis-
                                                cussão sobre esse aspecto veja Subse-
                                                ção A.5.
abnt-last-names=abnt                  abnt      Segue estritamente a ABNT.
abnt-last-names=bibtex              bibtex      Segue o modo usual do bibtex.
abnt-missing-year                               Determina de que maneira deve ser tra-
                                                tado um ano (campo year) ausente.
abnt-missing-year=void                 void     deixa em branco, é o padrão.
abnt-missing-year=sd                     sd     coloca a expressão “[s.d.]” (sem data).
                                                Note que a ‘norma’(2) não usa isso.

abnt-repeated-author-omit                       Permite suprimir o autor que aparece
                                                repetidas vezes na sequência. Exemplos:
                                                211, 212.
abnt-repeated-author-omit=no               no   Repete os autores.
                                                Nota: também coloca automaticamente
                                                abnt-repeated-title-omit=no.
abnt-repeated-author-omit=yes             yes   Substitui o autor repetido por      .

abnt-repeated-title-omit                        Permite suprimir o título que aparece
                                                repetidas vezes na seqüência quando o
                                                autor também está repetido. Exemplos:
                                                215, 216
abnt-repeated-title-omit=no                no   Repete os títulos.
abnt-repeated-title-omit=yes              yes   Substitui o título repetido por    .
                                                Nota: também coloca automaticamente
                                                abnt-repeated-author-omit=yes.

abnt-thesis-year                                Controla a posição do ano numa en-
                                                trada tipo mastersthesis, phdthesis
                                                e monography.
abnt-thesis-year=final                final     coloca o ano no final, ex. 191, 192;
abnt-thesis-year=title                title     logo após o título, ex. 194;
abnt-thesis-year=both                  both     em ambas as posições, ex. 196.

  Tabela 5: Opções de alteração do funcionamento dos estilos bibliográficos.

campo                         opções    descrição
abnt-refinfo                            Controla a utilização do comando
                                        \abntrefinfo usado pelo estilo abn-
                                        tex2cite
abnt-refinfo=yes                 yes    usa \abntrefinfo
abnt-refinfo=no                   no    não usa \abntrefinfo
abnt-show-options                       Controla como são mostradas as opções.
abnt-show-options=no             no     para não ver informação nenhuma;
abnt-show-options=warn         warn     para ter as informações mostradas como
                                        warnings durante a execução do bibtex;
abnt-show-options=list         list     para ter cada entrada listada na própria
                                        lista de referências. Exemplos: 1, 112,
                                        115, 193, 195, 197, 220.
abnt-verbatim-entry                     Permite mostrar na lista de referências
                                        toda a entrada em modo verbatim. Im-
                                        portante: este modo mostra as entrada
                                        já com a substituição das macros defini-
                                        das por @string.
abnt-verbatim-entry=no            no    não mostra a entrada.
abnt-verbatim-entry=yes          yes    mostra a entrada verbatim, é usado neste
                                        documento.

Tabela 6: Opções de alteração referntes a url (endereços de Internet). Veja também
a seção 8.1 para mais informações.

 campo                               opções   descrição
 abnt-doi                                     Determina como são tratadas url’s
                                              referentes a DOI (Digital Object
                                              Identifier)(218). Note que as opções se-
                                              guintes só terão efeito se a url iniciar
                                              por doi:.
 abnt-doi=expand                    expand    Expande um endereço iniciado com doi:
                                              para http://dx.doi.org/
 abnt-doi=link                         link   Deixa o endereço intacto e coloca uma
                                              hiperligação para a url correspondente
                                              em http:. A ligação só estará funcio-
                                              nando se algum pacote como hyperref
                                              tiver sido selecionado.
 abnt-doi=doi                           doi   Deixa o endereço intacto e coloca uma
                                              hiperligação também para um docu-
                                              mento do tipo doi:.
 abnt-url-package                             Opção obsoleta
                                              O valor padrão aqui é url; as demais
                                              opções são mantidas apenas para compa-
                                              tibilidade reversa.
                                              Identifica o pacote que é usado para tra-
                                              tar url’s.
                                              Nota: é necessário carregar esses pacotes
                                              para que estas opções tenham efeito.
 abnt-url-package=none                none    nenhum pacote.
 abnt-url-package=url                  url    usa o pacote url.
 abnt-url-package=hyperref        hyperref    usa o pacote hyperref.
 abnt-url-package=html                html    usa o pacote html.

\bibtextitlecommand{inbook}{A coloniza{\c c}\~ao da terra do {T}ucuj\’us}

   Por exemplo, para que todas as ocorrências de títulos sejam colocadas entre
aspas, voce pode usar o comando seguinte ainda no preâmbulo:

\newcommand{\bibtextitlecommand}[2]{‘‘#2’’}

   Você pode restringir esse comando apenas a entradas do tipo article, por
exemplo. Nesse caso, comando seria o seguinte:

\newcommand{\bibtextitlecommand}[2]{%
  \ifthenelse{\equal{#1}{article}}{‘‘#2’’}{}}

7.4    Opções agrupadas
O arquivo abntex2-options.bib define opções que agrupam outras opções defini-
das na Tabela 2 a na Tabela 5. A tabela Tabela 7 e a Tabela 8 mostram os grupos
de opções disponíveis. Consulte o próprio arquivo abntex2-options.bib para ver
as opções definidas8 .

Tabela 7: Subestilos locais usadas por algumas instituições. Estas alterações foram
identificadas por usuários. Se sua instituição tem regras particulares que poderiam
entrar aqui, por favor avise-nos.

  opção                       descrição
  abnt-substyle=COPPE         opções específicas para a COPPE/UFRJ.
  abnt-substyle=UFLA          opções específicas para a UFLA.

 Tabela 8: Grupos de opções que caraterizam as versões das diversas ‘normas’.

  opção                       descrição
  abnt-nbr10520=2001          (padrão) segue a ‘norma’ 10520/2001(4).
  abnt-nbr10520=1988          segue a ‘norma’ 10520/1988(3).

   8 Note que essas opções só podem ser usadas se for usado o arquivo abntex2-options.bib na

bibliografia.

8      Novos campos
Para conseguir atender a todas as peculiaridades da ‘norma’ 6023(2), foi necessário
criar um grande número de campos bibliográficos específicos. Esteja atento que
outros estilos bibtex simplesmente ignoraram esses campos. Se o campo também
for utilizado por outros estilos, indicamos esse fato (desde que seja do nosso
conhecimento), nas seções seguintes.

8.1    Endereços de internet (url)
O estilo bibliográfico junto com o pacote abntex2cite trata corretamente endereços
de internet, mais conhecidos como url. Veja a Tabela 9. Se o seu documento
carrega o pacote hyperref antes do pacote abntex2cite todas as url viram com
hyperligações (hyperlinks) que podem ser navegáveis. Note que ao utilizar pdflatex
o pacote hyperref é automaticamente carregado.
    Dependendo das opções escolhidas (veja a Tabela 6), a url pode aparecer como
hiperligação na sua lista bibliográfica. Para que isso ocorra é necessário que a url
esteja formatada de maneira válida, isto é, que inicie por http:, ftp:, mailto:,
file: ou doi:. A url será filtrada para a remoção de caracteres que atrapalham a
formatação LATEX, mas a url passada para o programa externo será sempre correta.
O estilo bibliográfico também insere marcações de hifenização que permite que a
url seja quebrada, já que elas tendem a ser muito longas.

Tabela 9: Campos relativos a sites de Internet e documentos eletrônicos. Exemplos:
21, 22, 36, 37, 38, 39, 40, 41, 48, 49, 50, 51, 52, 99, 101. O campo url é utilizado
em numerosos estilos bibtex.

 campo              entradas   descrição
 url                 todas     Universal Resource Locator, ou endereço de internet.
                               A url deve ser dada exatamente como seria usada num
                               browser. O estilo bibliográfico se encarrega de adaptar
                               a url para que possa ser formatada pelo LATEX e para
                               que possa servir como hiperligação em documentos
                               que usam o pacote hyperref ou pdflatex.
 urlaccessdate       todas     data em que foi acessado a url. É responsabilidade do
                               usuário colocar a data no formato correto.

9      Novas entradas .bib
Algumas novas entradas tiveram que ser criadas. Entradas são objetos de citação
bibliográficas como @book e @article que ficam no arquivo de bibliografias (arquivo
.bib). Note que outros estilos bibliográficos tratarão essas entradas como @misc.

Tabela 10: Campos relativos a ISBN e ISSN. Os campos isbn e issn são usados
nos estilos is-alpha, is-unsrt, dinat, jurabib, jureco, abbrvnat, plainnat,
unsrtnat

 campo     entradas               descrição
 isbn      book,    booklet, ISBN é a numeração internacional para livros. É res-
           inbook,           ponsabilidade do usuário colocar o ISBN no formato
           incollection,     correto. Ex. 6, 7, 148, 178, 202.
           inproceedings,
           proceedings
 issn      article,    book,      ISSN é a numeração internacional para publicações
           inproceedings,         periódicas: jornais, revistas, catálogos telefônicos etc.
           proceedings            É responsabilidade do usuário colocar o ISSN no for-
                                  mato correto. Ex. 23, 25.

           Tabela 11: Campos relativos a subtítulos e seções de revistas.

 campo             entradas                      descrição
 subtitle          todas                         subtítulo relativo ao title, não coloque
                                                 os dois pontos que são gerados automá-
                                                 ticamente. Ex. 2, 12, 14, 15, 16, 17, 37,
                                                 44, 82, 83, 99, 116, 126, 127, 134, 135,
                                                 152, 192
 booksubtitle      todas que tem o campo         subtítulo relatívo ao booktitle. Ex. 18,
                   booktitle                     52
 section           journal                       formata a seção de um article. Ex. 29,
                                                 31, 55, 57, 59, 61, 62

                 Tabela 12: Campos relativos a autoria.

campo         entradas                   descrição
editortype    todas onde cabe editor     altera o tipo de editor (padrão “Ed.”)
                                         para qualquer valor colocado no campo.
                                         Isto atende ao ítem 8.1.1.4(2). É res-
                                         ponsabilidade do usuário usar formato
                                         correto: “Org.", “Coord."etc. Ex. 18, 118,
                                         119, 121, 135, 172 e sem essa opção:
                                         12, 120.
furtherresp   book                       adiciona informações sobre responsabi-
                                         lidades adicionais de autoria, tradução,
                                         organização, ilustrações etc. Isto atende
                                         ao ítem 8.1.1.7(2). É responsabilidade
                                         do usuário colocar isso na forma correta,
                                         muito embora nenhuma prescrição para
                                         isso esteja dada(2) Ex. 12, 20, 60, 121,
                                         124, 125, 126, 135, 144, 177, 178, 185,
                                         186, 187, 188
org-short     todas                      este campo permite colocar uma abre-
                                         viatura ou sigla para o nome de uma
                                         organização (ex. ABNT). Isso permite
                                         que a chamada na citação use a forma
                                         abreviada. Somente para o estilo alfabé-
                                         tico.

         Tabela 13: Campos relativos a descrição física do documento.

  campo          entradas               descrição
  dimensions     book                   texto que mostra as dimensões do do-
                                        cumento. Isto atende ao ítem 8.9(2). É
                                        responsabilidade do usuário colocar as
                                        dimensões na forma correta. Ex. 6, 148,
                                        178, 179, 180, 181, 182, 183, 185, 187,
                                        204
  illustrated    book                   indica as ilustrações. Se for vazio,
                                        illustrated={}, será colocado automá-
                                        ticamente “il.”. Senão será colocado o
                                        que estiver neste campo. É responsabili-
                                        dade do usuário usar os formatos corre-
                                        tos: “il. color.”, “principalmente il. co-
                                        lor.”, “somente il.” etc. Ex. 13, 148, 175,
                                        176, 177, 178, 181, 187, 202
  pagename       todas                   define novo nome para página, alterando
                                         o padrão “p.”. Note que a única variação
                                         é usar “f.”, para designar folhas ao invés
                                         de páginas. Isto atende ao ítem 8.7.2(2).
                                         É responsabilidade do usuário usar for-
                                         mato correto: “f." Ex. 9, 146, 169, 78

Tabela 14: Campos relativos a descrição de uma conferência para entradas do tipo
proceedings, inproceedings e conference.

 campo                      descrição
 conference-number          número da conferência, adiciona um ponto automati-
                            camente, isto é, ‘13’ torna-se ‘13.’.
 conference-year            ano em que foi realizada a conferência.
 conference-location        localização onde foi realizada a conferência

                Tabela 15: Campos relativos teses e monografias.

    campo                descrição
    year-presented       ano em que um trabalho foi apresentado.

               9.1     @ABNT-option — Mudança no estilo ABNT
@ABNT-option   Com entrada a @ABNT-option você pode especificar as alterações no comportamento
               dos estilos bibliográficos. Veja a Seção 7, Página 10, para mais detalhes. Neste
               texto as alterações são mostradas na própria lista de referências: 1, 8, 10????, 112,
               115, 193, 195, 197

               9.2     @hidden — Entrada escondida
     @hidden   @hidden gera uma entrada que não aparece na lista de referências. Ela é útil para
       \apud   ser usada com os comandos \apud e \apudonline. Veja a Ref. 221 para mais
\apudeonline   detalhes. Os únicos campos considerados são de autoria (author, ou editor, ou
               organization, ou title) e de ano (year). Esse tipo de entrada só tem sentido no
               estilo autor-data [alf].

               9.3     @ISO-option — Mudança de estilo ISO
 @ISO-option   Tem a mesma função que entradas tipo @ABNT-option, só que altera opções
               específicas para ‘normas’ ISO.

               9.4     @journalpart — Partes de periódicos
@journalpart   Esta entrada formata partes de periódicos. Veja os exemplos 26, 27, 28, 136, 137,
               160, 161.

               9.5     @monography — Monografias
 @monography   Além de teses de mestrado9 e doutorado, a ABNT ainda definiu separadamente
               monografias em geral. Use exatamente da mesma maneira como @mastersthesis
               e @phdthesis. Exemplos: 191, 194, 196

               9.6     @patent — Patentes
     @patent   É uma entrada ainda bastante experimental para descrever patentes. Exemplo: 53

               9.7     @thesis — Teses de modo geral
     @thesis   Esta entrada funciona como @phdthesis com a diferença que o campo type deve
               conter toda a informação sobre o tipo de tese.
                  Por exemplo, se tivermos:

               type={Doutorado em f\’\i sica}

                  teremos como saída ‘Doutorado em física’ e não ‘Tese (Doutorado em física)’
               como em @phdthesis.
                  9 O trabalho escrito de mestrado no Brasil é chamado de dissertação, dando a entender que

               se trata de um trabalho de qualidade inferior ao de uma tese. No exterior, onde o trabalho das
               pessoas costuma ser mais respeitado, é chamado de tese de mestrado.

Referências
1 Mudança de estilo após este ponto com o comando
\citeoption{abnt-options0} . Opção selecionada abnt-show-options=list.

@abnt-options{abnt-options0,
key={a},
abnt-show-options={list}}

2 ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. NBR 6023 :
Informação e documentação — referências — elaboração. Rio de Janeiro, 2000.
22 p.

@manual{NBR6023:2000,
address={Rio de Janeiro},
month={ago.},
organization={Associa{\c c}\~ao Brasileira de Normas T\’ecnicas},
org-short={ABNT},
pages={22},
subtitle={Informa{\c c}\~ao e documenta{\c c}\~ao --- Refer\^encias ---
  Elabora{\c c}\~ao},
title={{NBR} 6023},
year={2000}}

3 ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. NBR 10520 :
Apresentação de citações em documentos — procedimentos. Rio de Janeiro, 1988.
3 p.

@manual{NBR10520:1988,
address={Rio de Janeiro},
month={out.},
organization={Associa{\c c}\~ao Brasileira de Normas T\’ecnicas},
org-short={ABNT},
pages={3},
subtitle={Apresenta{\c c}\~ao de cita{\c c}\~oes em documentos ---
  Procedimentos},
title={{NBR} 10520},
year={1988}}

4 ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. NBR 10520 :
Informação e documentação — apresentação de citações em documentos. Rio de
Janeiro, 2001. 4 p. Substitui a Ref. 3.

@manual{NBR10520:2001,
address={Rio de Janeiro},
month={jul.},
note={Substitui a Ref.~\citeonline{NBR10520:1988}},
organization={Associa{\c c}\~ao Brasileira de Normas T\’ecnicas},

org-short={ABNT},
pages={4},
subtitle={Informa{\c c}\~ao e documenta{\c c}\~ao --- Apresenta{\c c}\~ao
    de
  cita{\c c}\~oes em documentos},
title={{NBR} 10520},
year={2001}}

5 WEBER, G. Estilo bibtex compatível com a ‘norma’ 6023/2000 da ABNT :
Questões específicas da ‘norma’ 10520/2001. [S.l.], 2003. Disponível em:
<http://abntex.codigolivre.org.br>.

@manual{abnt-bibtex-alf-doc,
author={Gerald Weber},
organization={Grupo abnTeX},
subtitle={Quest\~oes espec{\’\i}ficas da ‘norma’ 10520/2001},
title={Estilo bibtex compat{\’\i}vel com a ‘norma’ 6023/2000 da {ABNT}},
url={http://abntex.codigolivre.org.br},
year={2003}}

6 GOMES, L. G. F. F. Novela e sociedade no Brasil. Niterói: EdUFF, 1998.
137 p., 21 cm. (Coleção Antropologia e Ciência Política, 15). Bibliografia: p.
131–132. ISBN 85-228-0268-8.

@book{gomes1998,
address={Niter\’oi},
author={Gomes, L. G. F. F},
dimensions={21~cm},
isbn={85-228-0268-8},
note={Bibliografia: p. 131--132},
number={15},
pages={137},
publisher={EdUFF},
series={Cole{\c c}\~ao Antropologia e Ci\^encia Pol{\’\i}tica},
title={Novela e sociedade no Brasil},
year={1998}}

7 PERFIL da administração pública paulista. 6. ed. São Paulo: FUNDAP, 1994.
317 p., 28 cm. Inclui índice. ISBN 85-7285-026-0.

@book{FUNDAP1994,
address={S\~ao Paulo},
edition={6},
dimensions={28~cm},
isbn={85-7285-026-0},
note={Inclui {\’\i}ndice},
pages={317},
publisher={FUNDAP},
title={Perfil da administra{\c c}\~ao p\’ublica paulista},
year={1994}}

8 Mudança de estilo após este ponto com o comando
\citeoption{ABNT-barcelos0} . Opção selecionada abnt-thesis-year=title.

@abnt-options{ABNT-barcelos0,
key={x},
abnt-thesis-year={title}}

9 BARCELOS, M. F. P. Ensaio tecnológico, bioquímico e sensorial de soja e
gandu enlatados no estágio verde e maturação de colheita. 1998. 160 f. Tese
(Doutorado em Nutrição) — Faculdade de Engenharia de Alimentos, Universidade
Estadual de Campinas, Campinas.

@phdthesis{barcelos1998,
address={Campinas},
author={M. F. P. Barcelos},
pages={160},
pagename={f.},
school={Faculdade de Engenharia de Alimentos, Universidade Estadual de
  Campinas},
title={Ensaio tecnol\’ogico, bioqu{\’\i}mico e sensorial de soja e gandu
  enlatados no est\’agio verde e matura{\c c}\~ao de colheita},
type={Doutorado em Nutri{\c c}\~ao},
year={1998}}

10 Mudança de estilo após este ponto com o comando
\citeoption{ABNT-barcelos1} . Opção selecionada abnt-thesis-year=final.

@abnt-options{ABNT-barcelos1,
key={x},
abnt-thesis-year={final}}

11 IBICT. Manual de normas de editoração do IBICT. 2. ed. Brasília, DF, 1993.
41 p.

@booklet{IBICT1993,
address={Bras{\’\i}lia, DF},
edition={2},
organization={IBICT},
pages={41},
title={Manual de normas de editora{\c c}\~ao do {IBICT}},
year={1993}}

12 HOUAISS, A. (Ed.). Novo dicionário Folha Webster’s: inglês/português,
português/inglês. Co-editor Ismael Cardim. São Paulo: Folha da Manhã, 1996.
Edição exclusiva para o assinante da Folha de S. Paulo.

@book{houaiss1996,
address={S\~ao Paulo},
editor={A. Houaiss},
furtherresp={Co-editor Ismael Cardim},
note={Edi{\c c}\~ao exclusiva para o assinante da Folha de S.\ Paulo},
publisher={Folha da Manh\~a},
subtitle={ingl\^es/portugu\^es, portugu\^es/ingl\^es},
title={Novo dicion\’ario {Folha Webster’s}},
year={1996}}

13 BRASIL: roteiros turísticos. São Paulo: Folha da Manhã, 1995. 319 p., il.
(Roteiros turísticos Fiat). Inclui mapa rodoviário.

@book{folha1995,
address={S\~ao Paulo},
illustrated={},
note={Inclui mapa rodovi\’ario},
pages={319},
publisher={Folha da Manh\~a},
series={Roteiros tur{\’\i}sticos Fiat},
title={Brasil: roteiros tur{\’\i}sticos},
year={1995}}

14 SÃO PAULO (Estado). Secretaria do Meio Ambiente. Coordenadoria de
Planejamento Ambiental. Estudo de impacto ambiental — EIA, Relatório de
Impacto Ambiental — RIMA: manual de orientação. São Paulo, 1989. 48 p. (Série
Manuais).

@manual{secretaria1989,
address={S\~ao Paulo},
organization={S\~ao Paulo {(Estado). Secretaria do Meio Ambiente.
    Coordenadoria
  de Planejamento Ambiental.}},
pages={48},
series={S\’erie Manuais},
subtitle={manual de orienta{\c c}\~ao},
title={Estudo de impacto ambiental --- EIA, Relat\’orio de Impacto
    Ambiental
  --- RIMA},
year={1989}}

15 MUSEU DA IMIGRAÇÃO (São Paulo, SP). Museu da Imigração — S. Paulo:
catálogo. São Paulo, 1997. 16 p.

@manual{museu1997,
address={S\~ao Paulo},
organization={Museu~da~Imigra{\c c}\~ao {(S\~ao Paulo, SP)}},
pages={16},

subtitle={cat\’alogo},
title={Museu da Imigra{\c c}\~ao --- S. Paulo},
year={1997}}

16 INSTITUTO MOREIRA SALLES. São Paulo de Vincenzo Pastore: fotografias:
de 26 de abril a 3 de agosto de 1997, Casa da cultura de Poços de Caldas, MG.
[S.l.], 1997. 1 folder. Apoio Ministério da Cultura: Lei Federal de Incentivo à
Cultura.

@manual{moreira1997,
note={1 folder. Apoio Minist\’erio da Cultura: Lei Federal de Incentivo \‘a
  Cultura},
organization={Instituto Moreira Salles},
subtitle={fotografias: de 26 de abril a 3 de agosto de 1997, {Casa da
    cultura
  de Po{\c c}os de Caldas, MG}},
title={S\~ao Paulo de Vincenzo Pastore},
year={1997}}

17 TORELLY, M. Almanaque para 1949 : primeiro semestre ou almanaque d’a
manhã. Ed. fac-sim. São Paulo: Studioma: Arquivo do Estado, 1991. (Coleção
Almanaques do Barão de Itararé). Contém iconografia e depoimentos sobre o
autor.

@book{torelly1991,
address={S\~ao Paulo},
author={M. Torelly},
edition={Ed. fac-sim},
note={Cont\’em iconografia e depoimentos sobre o autor},
publisher={Studioma: Arquivo do Estado},
series={Cole{\c c}\~ao Almanaques do Bar\~ao de Itarar\’e},
subtitle={primeiro semestre ou Almanaque d’A Manh\~a},
title={Almanaque para 1949},
year={1991}}

18 ROMANO, G. Imagens da juventude na era moderna. In: LEVI, G.;
SCHMIDT, J. (Org.). História dos jovens 2 : a época contemporânea. São Paulo:
Companhia das Letras, 1996. p. 7–16.

@incollection{romano1996,
address={S\~ao Paulo},
author={G. Romano},
booktitle={Hist\’oria dos jovens 2},
booksubtitle={a \’epoca contempor\^anea},
editor={G. Levi and J. Schmidt},
editortype={Org.},
pages={7-16},
publisher={Companhia das Letras},
title={Imagens da juventude na era moderna},
year={1996}}

19 SANTOS, F. R. dos. A colonização da terra do tucujús. In:        . História
do Amapá, 1o grau. 2. ed. Macapá: Valcan, 1994. cap. 3, p. 15–24.

@inbook{santos1994,
address={Macap\’a},
author={dos Santos, Fernando Rodrigues},
booktitle={Hist\’oria do Amap\’a, {1$^o$} grau},
chapter={3},
edition={2},
pages={15-24},
publisher={Valcan},
title={A coloniza{\c c}\~ao da terra do Tucuj\’us},
year={1994}}

20 KOOGAN, A.; HOUAISS, A. (Ed.). Enciclopédia e dicionário digital 98.
Direção geral de André Koogan Breikman. São Paulo: Delta: Estadão, 1998. 5
CD-ROM. Produzida por Videolar Multimídia.

@book{koogan1998,
address={S\~ao Paulo},
editor={A. Koogan and A. Houaiss},
furtherresp={Dire{\c c}\~ao geral de Andr\’e Koogan Breikman},
note={5 CD-ROM. Produzida por Videolar Multim{\’\i}dia},
publisher={Delta: Estad\~ao},
title={Enciclop\’edia e dicion\’ario digital 98},
year={1998}}

21 POLÍTICA. In: DICIONÁRIO da língua portuguesa. Lisboa: Priberam
Informática, 1998. Disponível em: <http://www.priberam.pt/dlDLPO>. Acesso
em: 8 mar. 1999.

@inbook{priberam1998,
address={Lisboa},
booktitle={Dicion\’ario da l{\’\i}ngua portuguesa},
publisher={Priberam Inform\’atica},
title={Pol{\’\i}tica},
url={http://www.priberam.pt/dlDLPO},
urlaccessdate={8 mar. 1999},
year={1998}}

22 SÃO PAULO (Estado). Secretaria do Meio Ambiente. Tratados
e organizações ambientais em matéria de meio ambiente. In:      .
Entendendo o meio ambiente. São Paulo, 1999. v. 1. Disponível em:
<http://www.bdt.org.br/sma/entendendo/atual.htm>. Acesso em: 8 mar. 1999.

@inbook{secretaria1999,
address={S\~ao Paulo},
booktitle={Entendendo o meio ambiente},

organization={S\~ao Paulo {(Estado). Secretaria do Meio Ambiente}},
title={Tratados e organiza{\c c}\~oes ambientais em mat\’eria de meio
  ambiente},
url={http://www.bdt.org.br/sma/entendendo/atual.htm},
urlaccessdate={8 mar. 1999},
volume={1},
year={1999}}

23 REVISTA BRASILEIRA DE GEOGRAFIA. Rio de Janeiro: IBGE, 1939–.
Trimestral. Absorveu Boletim Geográfico do IBGE. Índice acumulado. 1939–1983.
ISSN 0034-723X.

@book{brasileira1939,
address={Rio de Janeiro},
issn={0034-723X},
note={Trimestral. Absorveu Boletim Geogr\’afico do IBGE. \’Indice
    acumulado.
  1939--1983},
organization={Revista Brasileira de Geografia},
publisher={IBGE},
year={1939--}}

24 BOLETIM GEOGRÁFICO. Rio de Janeiro: IBGE, 1943–1978. Trimestral.

@book{geografico1943,
address={Rio de Janeiro},
note={Trimestral},
organization={Boletim Geogr\’afico},
publisher={IBGE},
year={1943-1978}}

25 SÃO PAULO MEDICAL JOURNAL=REVISTA PAULISTA DE MEDICINA.
São Paulo: Associação Paulista de Medicina, 1941–. Bimensal. ISSN 0035-0362.10

@book{paulista1941,
address={S\~ao Paulo},
issn={0035-0362},
note={Bimensal},
organization={S\~ao Paulo Medical Journal=Revista Paulista de Medicina},
publisher={Associa{\c c}\~ao Paulista de Medicina},
year={1941-}}

26 CONJUNTURA ECONÔMICA. As 500 maiores empresas do Brasil. Rio de
Janeiro: FGV, v. 38, n. 9, set. 1984. 135 p. Edição Especial.
 10 O sinal de igualdade é do jeito que está no exemplo da ‘norma’.

@journalpart{fgv1984,
address={Rio de Janeiro},
month={set.},
note={Edi{\c c}\~ao Especial},
number={9},
pages={135},
publisher={FGV},
title={Conjuntura Econ\^omica. As 500 maiores empresas do Brasil},
volume={38},
year={1984}}

27 PESQUISA NACIONAL POR AMOSTRA DE DOMICÍLIOS. Mão-de-obra e
previdência. Rio de Janeiro: IBGE, v. 7, 1983. Suplemento.

@journalpart{ibge1983,
address={Rio de Janeiro},
note={Suplemento},
publisher={IBGE},
title={Pesquisa Nacional por amostra de domic{\’\i}lios. M\~ao-de-obra e
  previd\^encia},
volume={7},
year={1983}}

28 DINHEIRO: revista semanal de negócios. São Paulo: Ed. Três, n. 148, 28 jun.
2000. 98 p.

@journalpart{tres2000,
address={S\~ao Paulo},
month={28 jun.},
number={148},
pages={98},
publisher={Ed.\ Tr\^es},
subtitle={revista semanal de neg\’ocios},
title={Dinheiro},
year={2000}}

29 COSTA, V. R. À margem da lei: o programa comunidade solidária. Em Pauta
— Revista da Faculdade de Serviço Social da UERJ, Rio de Janeiro, n. 12, p.
131–148, 1998.

@article{costa1998,
address={Rio de Janeiro},
author={V. R. Costa},
journal={Em Pauta},
number={12},
pages={131-148},
section={Revista da Faculdade de Servi{\c c}o Social da UERJ},
title={{\‘A} Margem da lei: o Programa Comunidade Solid\’aria},
year={1998}}

30 GURGEL, C. Reforma do estado e segurança pública. Política e administração,
Rio de Janeiro, v. 3, n. 2, p. 15–21, set. 1997.

@article{gurgel1997,
address={Rio de Janeiro},
author={C. Gurgel},
journal={Pol{\’\i}tica e administra{\c c}\~ao},
month={set.},
number={2},
pages={15-21},
title={Reforma do estado e seguran{\c c}a p\’ublica},
volume={3},
year={1997}}

31 TOURINHO NETO, F. C. Dano ambiental. Consulex — Revista Jurídica,
Brasília, DF, ano 1, n. 1, p. 18–23, fev. 1997.

@article{tourinho1997,
address={Bras{\’\i}lia, DF},
author={Tourinho, Neto, F. C.},
journal={Consulex},
month={fev.},
number={1},
pages={18-23},
section={Revista Jur{\’\i}dica},
title={Dano ambiental},
volume={ano~1},
year={1997}}

32 MANSILLA, H. C. F. La controversia entre universalismo y particularismo en
la filosofia de la cultura. Revista Latinoamericana de Filosofia, Buenos Aires, v. 24,
n. 2, primavera 1998.

@article{mansilla1998,
address={Buenos Aires},
author={H. C. F. Mansilla},
journal={Revista Latinoamericana de Filosofia},
month={primavera},
number={2},
title={La controversia entre universalismo y particularismo en la
    filosofia de
  la cultura},
volume={24},
year={1998}}

33 COSTURA × P. U. R. Aldus, São Paulo, ano 1, n. 1, nov. 1997. Encarte
técnico, p. 8.

@article{aldus1997,
address={S\~ao Paulo},
journal={Aldus},
month={nov.},
note={Encarte t\’ecnico, p.~8},
number={1},
title={Costura {$\times$} {P. U. R.}},
volume={ano 1},
year={1997}}

34 NAVES, P. Lagos andinos dão banho de belexa. Folha de S. Paulo, São Paulo,
28 jun. 1999. Folha Turismo, Caderno 8, p. 13.

@article{naves1999,
address={S\~ao Paulo},
author={P. Naves},
journal={Folha de S.\ Paulo},
month={28 jun.},
note={Folha Turismo, Caderno 8, p.~13},
title={Lagos andinos d\~ao banho de belexa},
year={1999}}

35 LEAL, L. N. MP fiscaliza com autonomia total. Jornal do Brasil, Rio de
Janeiro, p. 3, 25 abr. 1999.

@article{leal1999,
address={Rio de Janeiro},
author={L. N. Leal},
journal={Jornal do Brasil},
month={25 abr.},
pages={3},
title={{MP} fiscaliza com autonomia total},
year={1999}}

36 SILVA, M. M. L. Crimes da era digital. .Net, Rio de Janeiro, nov. 1998.
Seção Ponto de Vista. Disponível em: <http://www.brazilnet.com.br/contexts/
brasilrevistas.htm>. Acesso em: 28 nov. 1998.

@article{silva1998,
address={Rio de Janeiro},
author={M. M. L. Silva},
journal={.Net},
month={nov.},
note={Se{\c c}\~ao Ponto de Vista},
title={Crimes da era digital},
url={http://www.brazilnet.com.br/contexts/brasilrevistas.htm},
urlaccessdate={28 nov. 1998},
year={1998}}

37 RIBEIRO, P. S. G. Adoção à brasileira: uma análise sócio-jurídica.
Datavenia, São Paulo, ano 3, n. 18, ago. 1998. Disponível em: <http:
//www.datavenia.inf.br/frameartig.html>. Acesso em: 10 set. 1998.

@article{ribeiro1998,
address={S\~ao Paulo},
author={P. S. G. Ribeiro},
journal={Datavenia},
month={ago.},
number={18},
subtitle={uma an\’alise s\’ocio-jur{\’\i}dica},
title={Ado{\c c}\~ao \‘a brasileira},
url={http://www.datavenia.inf.br/frameartig.html},
urlaccessdate={10 set. 1998},
volume={ano~3},
year={1998}}

38 WINDOWS 98: o melhor caminho para atualização. PC World, São Paulo,
n. 75, set. 1998. Disponível em: <http://www.idg.com.br/abre.htm>. Acesso em:
10 set. 1998.

@article{pc1998,
address={S\~ao Paulo},
journal={PC World},
month={set.},
number={75},
title={Windows 98: o melhor caminho para atualiza{\c c}\~ao},
url={http://www.idg.com.br/abre.htm},
urlaccessdate={10 set. 1998},
year={1998}}

39 SILVA, I. G. Pena de morte para o nasciturno. O Estado de S. Paulo, São
Paulo, 19 set. 1998. Disponível em: <http://www.providafamilia.org/pena_
morte_nasciturno.htm>. Acesso em: 10 set. 1998.

@article{gsilva1998,
address={S\~ao Paulo},
author={I. G. Silva},
journal={O Estado de S.~Paulo},
month={19 set.},
title={Pena de morte para o nasciturno},
url={http://www.providafamilia.org/pena_morte_nasciturno.htm},
urlaccessdate={10 set. 1998},
year={1998}}

40 KELLY, R. Electronic publishing at APS: its not just online
journalism. APS News Online, Los Angeles, nov. 1996. Disponível em:
<http://www.aps.org/apsnews/1196/11965.html>. Acesso em: 25 nov. 1998.11
  11 No original está ‘Nov.’ em vez de ‘nov.’. Trata-se de um boletim informativo de sociedade

científica (APS) e não de um jornal científico como afirma a ‘norma’.

@article{kelly1996,
address={Los Angeles},
author={R. Kelly},
journal={APS News Online},
month={nov.},
title={Electronic publishing at {APS}: its not just online journalism},
url={http://www.aps.org/apsnews/1196/11965.html},
urlaccessdate={25 nov. 1998},
year={1996}}

41 ARRANJO tributário. Diário do Nordeste Online, Fortaleza, 27 nov. 1998.
Disponível em: <http://www.diariodonordeste.com.br>. Acesso em: 28 nov. 1998.

@article{nordeste1998,
address={Fortaleza},
journal={Di\’ario do Nordeste Online},
month={27 nov.},
title={Arranjo tribut\’ario},
url={http://www.diariodonordeste.com.br},
urlaccessdate={28 nov. 1998},
year={1998}}

42 SIMPÓSIO BRASILEIRO DE REDES DE COMPUTADORES, 13., 1995,
Belo Horizonte. Anais... Belo Horizonte: UFMG, 1995. 655 p.

@proceedings{redes1995,
address={Belo Horizonte},
conference-number={13},
conference-year={1995},
conference-location={Belo Horizonte},
organization={Simp\’osio Brasileiro de Redes de Computadores},
pages={655},
publisher={UFMG},
title={Anais...},
year={1995}}

43 IUFROST INTERNATIONAL SYMPOSIUM ON CHEMICAL CHANGES
DURING FOOD PROCESSING, 1984, Valencia. Proceedings... Valencia: Instituto
de Agroquimica y Tecnologia de Alimentos, 1984.

@proceedings{chemical1984,
address={Valencia},
conference-year={1984},
conference-location={Valencia},
organization={IUFROST International Symposium on Chemical Changes During
    Food
  Processing},
publisher={Instituto de Agroquimica y Tecnologia de Alimentos},

title={Proceedings...},
year={1984}}

44 REUNIÃO ANUAL DA SOCIEDADE BRASILEIRA DE QUÍMICA, 20.,
1997, Poços de Caldas. Química: academia, indústria, sociedade: livro de resumos.
São Paulo: Sociedade Brasileira de Química, 1997.

@proceedings{quimica1997,
address={S\~ao Paulo},
conference-number={20},
conference-year={1997},
conference-location={Po{\c c}os de Caldas},
organization={Reuni\~ao Anual da Sociedade Brasileira de Qu\’imica},
publisher={Sociedade Brasileira de Qu{\’\i}mica},
subtitle={academia, ind\’ustria, sociedade: livro de resumos},
title={Qu{\’\i}mica},
year={1997}}

45 MARTIN NETO, L.; BAYER, C.; MIELNICZUK, J. Alterações qualitativas
da matéria orgânica e os fatores determinantes da sua estabilidade num solo
podzólico vermelho-escuro em diferentes sistemas de manejo. In: CONGRESSO
BRASILEIRO DE CIÊNCIA DO SOLO, 26., 1997, Rio de Janeiro. Resumos... Rio
de Janeiro: Sociedade Brasileira de Ciência do Solo, 1997. p. 443. Ref. 6–141.12

@inproceedings{martin1997,
address={Rio de Janeiro},
author={Martin, Neto, L. and C. Bayer and J. Mielniczuk},
booktitle={Resumos...},
conference-number={26},
conference-year={1997},
conference-location={Rio de Janeiro},
note={ref. 6--141},
organization={Congresso Brasileiro de Ci\^encia do Solo},
pages={443},
publisher={Sociedade Brasileira de Ci\^encia do Solo},
title={Altera{\c c}\~oes qualitativas da mat\’eria org\^anica e os fatores
  determinantes da sua estabilidade num solo podz\’olico vermelho-escuro em
  diferentes sistemas de manejo},
year={1997}}

46 BRAYNER, A. R. A.; MEDEIROS, C. B. Incorporação do tempo em SGDB
orientado a objetos. In: SIMPÓSIO BRASILEIRO DE BANCO DE DADOS, 9.,
1994, São Paulo. Anais... São Paulo: USP, 1994. p. 16–29.

@inproceedings{brayner1994,
address={S\~ao Paulo},
author={A. R. A. Brayner and C. B. Medeiros},
 12 No original: ‘p. 443, ref. 6-141’ em vez de ‘p. 443. ref. 6-141’.

booktitle={Anais...},
conference-number={9},
conference-year={1994},
conference-location={S\~ao Paulo},
organization={Simp\’osio Brasileiro de Banco de Dados},
pages={16-29},
publisher={USP},
title={Incorpora{\c c}\~ao do tempo em {SGDB} orientado a objetos},
year={1994}}

47 SOUZA, L. S.; BORGES, A. L.; REZENDE, J. O. Influência da correção e
do preparo do solo sobre algumas propriedades químicas do solo cultivado com
bananeiras. In: REUNIÃO BRASILEIRA DE FERTILIDADE DO SOLO E
NUTRIÇÃO DE PLANTAS, 21., 1994, Petrolina. Anais... Petrolina: EMPRAPA,
CATSA, 1994. p. 3–4.

@inproceedings{souza1994,
address={Petrolina},
author={L. S. Souza and A. L. Borges and J. O. Rezende},
booktitle={Anais...},
conference-number={21},
conference-year={1994},
conference-location={Petrolina},
organization={Reuni\~ao Brasileira de Fertilidade do Solo e Nutri{\c
    c}\~ao de
  Plantas},
pages={3-4},
publisher={EMPRAPA, CATSA},
title={Influ\^encia da corre{\c c}\~ao e do preparo do solo sobre algumas
  propriedades qu{\’\i}micas do solo cultivado com bananeiras},
year={1994}}

48 CONGRESSO DE INICIAÇÃO CIENTÍFICA DA UFPe, 4.,
1996, Recife. Anais eletrônicos... Recife: UFPe, 1996. Disponível em:
<http://www.propesq.ufpe.br/anais/anais.htm>. Acesso em: 21 jan. 1997.

@proceedings{cientifica1996,
address={Recife},
conference-number={4},
conference-year={1996},
conference-location={Recife},
organization={Congresso de Inicia{\c c}\~ao Cient\’ifica da {UFPe}},
publisher={UFPe},
title={Anais eletr\^onicos...},
url={http://www.propesq.ufpe.br/anais/anais.htm},
urlaccessdate={21 jan. 1997},
year={1996}}

49 SILVA, R. N.; OLIVEIRA, R. Os limites pedagógicos do paradigma da
qualidade total na educação. In: CONGRESSO DE INICIAÇÃO CIENTÍFICA
DA UFPe, 4., 1996, Recife. Anais eletrônicos... Recife: UFPe, 1996. Disponível em:

<http://www.propesq.ufpe.br/anais/anais/educ/ce04.htm>. Acesso em: 21 jan.
1997.13

@inproceedings{oliveira1996,
address={Recife},
author={R. N. Silva and R. Oliveira},
booktitle={Anais eletr\^onicos...},
conference-number={4},
conference-year={1996},
conference-location={Recife},
organization={Congresso de Inicia{\c c}\~ao Cient\’ifica da {UFPe}},
publisher={UFPe},
title={Os limites pedag\’ogicos do paradigma da qualidade total na educa{\c
  c}\~ao},
url={http://www.propesq.ufpe.br/anais/anais/educ/ce04.htm},
urlaccessdate={21 jan. 1997},
year={1996}}

50 GUNCHO, M. R. A educação à distância e a biblioteca universitária. In:
SEMINÁRIO DE BIBLIOTECAS UNIVERSITÁRIAS, 10., 1998, Fortaleza.
Anais... Fortaleza: Tec Treina, 1998. 1 CD.

@inproceedings{guncho1998,
address={Fortaleza},
author={M. R. Guncho},
booktitle={Anais...},
conference-number={10},
conference-year={1998},
conference-location={Fortaleza},
note={1~CD},
organization={Semin\’ario de Bibliotecas Universit\’arias},
publisher={Tec Treina},
title={A educa{\c c}\~ao \‘a dist\^ancia e a biblioteca universit\’aria},
year={1998}}

51 SABROZA, P. C. Globalização e saúde: impacto nos perfis epidemiológicos
das populações. In: CONGRESSO BRASILEIRO DE EPIDEMIOLOGIA, 4.,
1998, Rio de Janeiro. Anais eletrônicos... Rio de Janeiro: ABRASCO, 1998.
Mesa-redonda. Disponível em: <http://www.abrasco.com.br/epirio98/>. Acesso
em: 17 jan. 1999.

@inproceedings{sabroza1998,
address={Rio de Janeiro},
author={P. C. Sabroza},
booktitle={Anais eletr\^onicos...},
conference-number={4},
conference-year={1998},
conference-location={Rio de Janeiro},
 13 A url no original é impossível.

note={Mesa-redonda},
organization={Congresso Brasileiro de Epidemiologia},
publisher={ABRASCO},
title={Globaliza{\c c}\~ao e sa\’ude: impacto nos perfis epidemiol\’ogicos
    das
  popula{\c c}\~oes},
url={http://www.abrasco.com.br/epirio98/},
urlaccessdate={17 jan. 1999},
year={1998}}

52 KRZYZANOWSKI, R. F. Valor agregado no mundo da informação: um
meio de criar novos espaços competitivos a partir da tecnologia da informação
e melhor satisfazer às necessidades dos clientes/usuários. In: CONGRESSO
REGIONAL DE INFORMAÇÃO EM CIÊNCIAS DA SAÚDE, 3., 1996, Rio de
Janeiro. Interligações da tecnologia da informação: um elo futuro. Disponível em:
<http://www.bireme.br/cgi-bin/crics3/texto?titulo=VALOR+AGREGADO+
NO+MUNDO>. Acesso em: 26 jan. 1999.

@inproceedings{krzyzanowski1996,
author={R. F. Krzyzanowski},
booktitle={Interliga{\c c}\~oes da tecnologia da informa{\c c}\~ao},
booksubtitle={um elo futuro},
conference-number={3},
conference-year={1996},
conference-location={Rio de Janeiro},
organization={Congresso Regional de Informa{\c c}\~ao em Ci\^encias da
  Sa\’ude},
title={Valor agregado no mundo da informa{\c c}\~ao: um meio de criar novos
  espa{\c c}os competitivos a partir da tecnologia da informa{\c c}\~ao e
  melhor satisfazer \‘as necessidades dos clientes/usu\’arios},
url={http://www.bireme.br/cgi-bin/crics3/texto?titulo=VALOR+AGREGADO+NO+MUNDO},
urlaccessdate={26 jan. 1999}}

53 EMBRAPA. Unidade de Apoio, Pesquisa e Desenvolvimento de Instrumentação
Agropecuária (São Carlos). Paulo Estevão Cruvinel. Medidor digital multisensorial
de temperatura para solos. BR n. PI 8903105-9, 26 jun. 1989, 30 maio 1995.

@patent{cruvinel1989,
author={Paulo Estev{\~a}o Cruvinel},
howpublished={26 jun. 1989, 30 maio 1995},
number={BR n. PI 8903105-9},
organization={Embrapa. {Unidade de Apoio, Pesquisa e Desenvolvimento de
  Instrumenta{\c c}\~ao Agropecu\’aria (S\~ao Carlos)}},
title={Medidor digital multisensorial de temperatura para solos}}

54 BRASIL. Constituição (1988). Constituição da República Federativa do Brasil.
Brasília, DF: Senado, 1988.

@book{brasil1988,
address={Brasília, DF},

organization={Brasil},
publisher={Senado},
title={Constituição da República Federativa do Brasil},
type={Constituição (1988)},
year={1988}}

55 BRASIL. Constituição (1988). emenda constitucional no 9, de 9 de novembro
de 1995. dá nova redação ao art. 177 da constituição federal, alterando e inserindo
parágrafos. Lex — Coletânea de Legislação e Jurisprudência: legislação federal e
marginália, São Paulo, v. 59, p. 1966, out./dez. 1995.

@article{brasil1966,
address={S\~ao Paulo},
journal={Lex},
month={out./dez.},
organization={Brasil},
pages={1966},
section={Colet\^anea de Legisla{\c c}\~ao e Jurisprud\^encia: legisla{\c
    c}\~ao
  federal e margin\’alia},
title={Constitui{\c c}\~ao (1988). Emenda constitucional n{$^o$}9, de 9 de
  novembro de 1995. D\’a nova reda{\c c}\~ao ao art.\ 177 da Constitui{\c
  c}\~ao Federal, alterando e inserindo par\’agrafos},
volume={59},
year={1995}}

56 BRASIL. Medida provisória no 1.569-9, de 11 de dezembro de 1997. estabelece
multa em operações de importação, e dá outras providências. Diário Oficial
[da] República Federativa do Brasil, Poder Executivo, Brasília, DF, 14 dez. 1997.
Seção 1, p. 29514.

@article{brasil1997,
address={Bras{\’\i}lia, DF},
journal={Di\’ario Oficial [da] Rep\’ublica Federativa do Brasil},
month={14 dez.},
note={Se{\c c}\~ao~1, p.~29514},
organization={Brasil},
publisher={Poder Executivo},
title={Medida provis\’oria n{$^o$} 1.569-9, de 11 de dezembro de 1997.
  Estabelece multa em opera{\c c}\~oes de importa{\c c}\~ao, e d\’a outras
  provid\^encias.},
year={1997}}

57 SÃO PAULO (Estado). Decreto no 42.822, de 20 de janeiro de 1998. dispõe
sobre a desativação de unidades administrativas de órgãos da administração direta
e das autarquias do eestado e dá providências correlatas. Lex — Coletânea de
Legislação e Jurisprudência, São Paulo, v. 62, n. 3, p. 217–220, 1998.

@article{lex1998,
address={S\~ao Paulo},

journal={Lex},
number={3},
organization={S\~ao Paulo {(Estado)}},
pages={217-220},
section={Colet\^anea de Legisla{\c c}\~ao e Jurisprud\^encia},
title={Decreto n{$^o$} 42.822, de 20 de janeiro de 1998. Disp\~oe sobre a
  desativa{\c c}\~ao de unidades administrativas de \’org\~aos da
      administra{\c
  c}\~ao direta e das autarquias do Eestado e d\’a provid\^encias
      correlatas},
volume={62},
year={1998}}

58 BRASIL. Congresso. Senado. Resolução no 17, de 1991. autoriza o desbloqueio
de letras financeiras do tesouro do estado do rio grande do sul, através de
revogação do parágrafo 2o , do artigo 1o da resolução no 72, de 1990. Coleção
de leis da República Federativa do Brasil, Brasília, DF, v. 183, p. 1156–1157,
maio/jun. 1991.

@article{leis1991,
address={Bras{\’\i}lia, DF},
journal={Cole{\c c}\~ao de leis da Rep\’ublica Federativa do Brasil},
month={maio/jun.},
organization={Brasil. {Congresso. Senado}},
pages={1156-1157},
title={Resolu{\c c}\~ao n{$^o$} 17, de 1991. Autoriza o desbloqueio de
    Letras
  Financeiras do Tesouro do Estado do Rio Grande do Sul, atrav\’es de
      revoga{\c
  c}\~ao do par\’agrafo 2{$^o$}, do artigo 1{$^o$} da Resolu{\c c}\~ao
      n{$^o$}
  72, de 1990},
volume={183},
year={1991}}

59 BRASIL. Consolidação das leis do trabalho. decreto-lei no 5.252 de 1 de
maio de 1943. aprova a consolidação das leis do trabalho. Lex — Coletânea de
Legislação: edição federal, São Paulo, v. 7, 1943. Suplemento.

@article{lex1943,
address={S\~ao Paulo},
journal={Lex},
note={Suplemento},
organization={Brasil},
section={Colet\^anea de Legisla{\c c}\~ao: edi{\c c}\~ao federal},
title={Consolida{\c c}\~ao das Leis do Trabalho. Decreto-lei n{$^o$}5.252
    de 1
  de maio de 1943. Aprova a consolida{\c c}\~ao das leis do trabalho},
volume={7},
year={1943}}

60 BRASIL. Código civil. Organização dos textos, notas remissivas e índices por
Juarez de Oliveira. 46. ed. São Paulo: Saraiva, 1995.

@book{brasil1995,
address={S\~ao Paulo},
edition={46},
furtherresp={Organiza{\c c}\~ao dos textos, notas remissivas e
    {\’\i}ndices por
  Juarez de Oliveira},
organization={Brasil},
publisher={Saraiva},
title={C\’odigo civil},
year={1995}}

61 BRASIL. Tribunal regional federal. região, 5. administrativo. escola técnica
federal. pagamento de diferenças referente a enquadramento de servidor decorrente
de implantação de plano Único de classificação e distribuição de cargos e empregos,
instituído pela lei no 8.270/91. predominância da lei sobre a portaria. apelação
cível no 42.441-PE (94.05.01629-6). apelante: Edilemos mamede dos santos e
outros. apelada: Escola técnica federal de pernambuco. relator: Juiz nereu santos.
recife, 4 de março de 1997. Lex — Jurisprudência do STJ e Tribunais Regionais
Federais, São Paulo, v. 10, n. 103, p. 558–562, mar. 1998.14

@article{brasillex1998,
address={S\~ao Paulo},
journal={Lex},
month={mar.},
number={103},
organization={Brasil},
pages={558-562},
section={Jurisprud\^encia do STJ e Tribunais Regionais Federais},
title={Tribunal Regional Federal. Regi\~ao, 5. Administrativo. Escola
    T\’ecnica
  Federal. Pagamento de diferen{\c c}as referente a enquadramento de
      servidor
  decorrente de implanta{\c c}\~ao de Plano {{\’U}}nico de Classifica{\c
      c}\~ao
  e Distribui{\c c}\~ao de Cargos e Empregos, institu{\’\i}do pela Lei
  n{$^o$}~8.270/91. Predomin\^ancia da lei sobre a portaria. Apela{\c
      c}\~ao
  c{\’\i}vel n{$^o$}~42.441-{PE} (94.05.01629-6). Apelante: Edilemos
      Mamede dos
  Santos e outros. Apelada: Escola T\’ecnica Federal de Pernambuco.
      Relator:
  Juiz Nereu Santos. Recife, 4 de mar{\c c}o de 1997},
volume={10},
year={1998}}

62 BRASIL. Superior Tribunal de Justiça. Processual penal. Habeas-corpus.
constrangimento ilegal. Habeas-corpus no 181.636-1, da 6a câmera cível do tribunal
 14 Na ‘norma’ a última parte, a partir do volume, encontra-se incorretamente em itálico.

de justiça do estado de são paulo, brasília, DF, 6 de dezembro de 1994. Lex —
Jurisprudência do STJ e Tribunais Regionais Federais, São Paulo, v. 10, n. 103, p.
236–240, mar. 1998.

@article{tribunal1998,
address={S\~ao Paulo},
journal={Lex},
month={mar.},
number={103},
organization={Brasil. {Superior Tribunal de Justi\c ca}},
pages={236-240},
section={Jurisprud\^encia do STJ e Tribunais Regionais Federais},
title={Processual Penal. \textit{Habeas-corpus}. Constrangimento ilegal.
  \textit{Habeas-corpus} n{$^o$}~181.636-1, da 6{$^a$} C\^amera C{\’\i}vel
      do
  Tribunal de Justi{\c c}a do Estado de S\~ao Paulo, Bras{\’\i}lia, {DF},
      6 de
  dezembro de 1994},
volume={10},
year={1998}}

63 BRASIL. Supremo Tribunal de Justiça. Súmula no 14. não é admissível por ato
administrativo restringir, em razão de idade, inscrição em concurso para cargo
público. In:      . Súmulas. São Paulo: Associação dos Advogados do Brasil,
1994. p. 16.

@inbook{brasil1994,
address={S\~ao Paulo},
booktitle={S\’umulas},
organization={Brasil. {Supremo Tribunal de Justi{\c c}a}},
pages={16},
publisher={Associa{\c c}\~ao dos Advogados do Brasil},
title={S\’umula n{$^o$}14. N\~ao \’e admiss{\’\i}vel por ato administrativo
  restringir, em raz\~ao de idade, inscri{\c c}\~ao em concurso para cargo
  p\’ublico},
year={1994}}

64 BARROS, R. G. de. Ministério público: sua legitimação frente ao código do
consumidor. Revista Trimestral de Jurisprudência dos Estados, São Paulo, v. 19,
n. 139, p. 53–72, ago. 1995.

@article{barros1995,
address={S\~ao Paulo},
author={R. G. de Barros},
journal={Revista Trimestral de Jurisprud\^encia dos Estados},
month={ago.},
number={139},
pages={53-72},
title={Minist\’erio P\’ublico: sua legitima{\c c}\~ao frente ao C\’odigo do
  Consumidor},

volume={19},
year={1995}}

65 BRASIL. Lei no 9.887, de 7 de dezembro de 1999. altera a legislação tributária
federal. Diário Oficial [da] República Federativa do Brasil, Brasília, DF, 8 dez. 1999.
Disponível em: <http://www.in.gov.br/mp_leis/leis_texto.aps?Id=Lei%209887>.
Acesso em: 22 dez. 1999.

@article{brasil1999,
address={Bras{\’\i}lia, DF},
journal={Di\’ario Oficial [da] Rep\’ublica Federativa do Brasil},
month={8 dez.},
organization={Brasil},
title={Lei n{$^o$} 9.887, de 7 de dezembro de 1999. Altera a legisla{\c
    c}\~ao
  tribut\’aria federal},
url={http://www.in.gov.br/mp_leis/leis_texto.aps?Id=Lei%209887},
urlaccessdate={22 dez. 1999},
year={1999}}

66 BRASIL. Supremo Tribunal Federal. Súmula no 14. Não é admissível por ato
administrativo restringir, em razão de idade, inscrição em concurso para cargo
público. Disponível em: <http://www.truenetm.com.br/jurisnet/sumusSTF.html>.
Acesso em: 29 nov. 1998.

@book{brasil1998,
note={N\~ao \’e admiss{\’\i}vel por ato administrativo restringir, em
    raz\~ao
  de idade, inscri{\c c}\~ao em concurso para cargo p\’ublico},
organization={Brasil. {Supremo Tribunal Federal}},
title={S\’umula n{$^o$}14},
url={http://www.truenetm.com.br/jurisnet/sumusSTF.html},
urlaccessdate={29 nov. 1998}}

67 BRASIL. Supremo Tribunal Federal. Súmula no 14. não é admissível
por ato administrativo restringir, em razão de idade, inscrição em
concurso para cargo público. julgamento: 1963/12/16. SUDIN vol. 0000-01
PG00037. Revista Experimental de Direito e Telemática. Disponível em:
<http://www.prodau-sc.com.br/ciberjur/stf.html>. Acesso em: 29 nov. 1998.

@article{supremo1998,
journal={Revista Experimental de Direito e Telem\’atica},
organization={Brasil. {Supremo Tribunal Federal}},
title={S\’umula n{$^o$}14. N\~ao \’e admiss{\’\i}vel por ato administrativo
  restringir, em raz\~ao de idade, inscri{\c c}\~ao em concurso para cargo
  p\’ublico. Julgamento: 1963/12/16. {SUDIN} vol. 0000-01 {PG}00037},
url={http://www.prodau-sc.com.br/ciberjur/stf.html},
urlaccessdate={29 nov. 1998}}

68 OS PERIGOS do uso de tóxicos. Produção de Jorge Ramos de Andrade.
Coordenação de Maria Izabel Azevedo. São Paulo: CERAVI, 1983. 1 fita de vídeo
(30 min), VHS, son., color.

@book{ceravi1983,
address={S\~ao Paulo},
furtherresp={Produ{\c c}\~ao de Jorge Ramos de Andrade. Coordena{\c c}\~ao
    de
  Maria Izabel Azevedo},
note={1 fita de v{\’\i}deo (30 min), VHS, son., color.},
publisher={CERAVI},
title={Os~perigos do uso de t\’oxicos},
year={1983}}

69 CENTRAL do Brasil. Direção: Walter Salles Júnior. Produção: Martire de
Clermont-Tonnerre e Artur Cohn. Roteiro: Marcos Bernstein, João Emanuel
Carneiro e Walter Salles Júnior. Intérpretes: Fernanda Montenegro; Marília Pera;
Vinicius de Oliveira; Sônia Lira; Othon Bastos; Matheus Nachtergaele e outros.
[S.l.]: Le Studio Canal; Riofilme; MACT Productions, 1998. 1 filme (106 min),
son., color., 35 mm.

@book{riofilme1998,
furtherresp={Dire{\c c}\~ao: Walter Salles J\’unior. Produ{\c c}\~ao:
    Martire
  de Clermont-Tonnerre e Artur Cohn. Roteiro: Marcos Bernstein, Jo\~ao
      Emanuel
  Carneiro e Walter Salles J\’unior. Int\’erpretes: Fernanda Montenegro;
  Mar{\’\i}lia Pera; Vinicius de Oliveira; S\^onia Lira; Othon Bastos;
      Matheus
  Nachtergaele e outros},
note={1 filme (106 min), son., color., 35 mm},
publisher={Le Studio Canal; Riofilme; MACT Productions},
title={Central do Brasil},
year={1998}}

70 BLADE Runner. Direção: Ridley Scott. Produção: Michael Deeley. Intérpretes:
Harrison Ford; Rutger Hauer; Sean Young; Edward James Olmos e outros. Roteiro:
Hampton Fancher e David Peoples. Música: Vangelis. Los Angeles: Warner
Brothers, c1991. 1 DVD (117 min), widescreen, color. Produzido por Warner
Video Home. Baseado na novela “Do androids dream of electric sheep?” de Philip
K. Dick.

@book{warner1991,
address={Los Angeles},
furtherresp={Dire{\c c}\~ao: Ridley Scott. Produ{\c c}\~ao: Michael Deeley.
  Int\’erpretes: Harrison Ford; Rutger Hauer; Sean Young; Edward James
      Olmos e
  outros. Roteiro: Hampton Fancher e David Peoples. M\’usica: Vangelis},
note={1 DVD (117 min), widescreen, color. Produzido por Warner Video Home.
  Baseado na novela ‘‘Do androids dream of electric sheep?’’ de Philip K.\
  Dick},

publisher={Warner Brothers},
title={Blade Runner},
year={c1991}}

71 KOBAYASHI, K. Doença dos xavantes. 1980. 1 fot., color. 16 cm×56 cm.

@misc{kobayashi1998,
author={K. Kobayashi},
note={1 fot., color. 16 cm$\times$56 cm},
title={Doen{\c c}a dos xavantes},
year={1980}}

72 FRAIPONT, E. A. I. O Estado de S. Paulo, São Paulo, 30 nov. 1998. Caderno
2, Visuais p. D2. 1 fot., p&b. Foto apresentada no Projeto ABRA/Coca-cola.15

@article{fraipont1998,
address={S\~ao Paulo},
author={Fraipont, E. Amiclar {II}},
journal={O Estado de S.\ Paulo},
month={30 nov.},
note={Caderno 2, Visuais p. D2. 1 fot., p\&b. Foto apresentada no Projeto
  ABRA/Coca-cola},
year={1998}}

73 O QUE acreditar em relação à maconha. São Paulo: CERAVI, 1985. 22
transparências, color., 25 cm×20 cm.

@misc{ceravi1985,
address={S\~ao Paulo},
howpublished={22 transpar\^encias, color., 25 cm$\times$20 cm},
publisher={CERAVI},
title={O~que acreditar em rela{\c c}\~ao \‘a maconha},
year={1985}}

74 O DESCOBRIMENTO do Brasil. Fotografia de Carmem Souza. Gravação
de Marcos Lourenço. São Paulo: CERAVI, 1985. 31 diapositivos: color. + 1 fita
cassete sonoro (15 min) mono.

@misc{souza1985,
address={S\~ao Paulo},
furtherresp={Fotografia de Carmem Souza. Grava{\c c}\~ao de Marcos
    Louren{\c
  c}o},
howpublished={31 diapositivos: color. + 1 fita cassete sonoro (15 min)
    mono},
publisher={CERAVI},
 15 Não é possível saber o que vem a ser o “II” (ou seria “Ll”?) no nome.

title={O~descobrimento do Brasil},
year={1985}}

75 SAMÚ, R. Vitória: 18:35 h. 1977. 1 grav., serigraf., color., 46 cm×63 cm.
Coleção Particular.

@misc{samu1977,
author={R. Sam\’u},
howpublished={1 grav., serigraf., color., 46 cm$\times$63 cm. Cole{\c
    c}\~ao
  Particular},
subtitle={18:35 h},
title={Vit\’oria},
year={1977}}

76 MATTOS, M. D. Paisagem — Quatro Barras. 1987. 1 original de arte, óleo
sobre tela, 40 cm×50 cm. Coleção particular.

@misc{mattos1987,
author={M. D. Mattos},
howpublished={1 original de arte, \’oleo sobre tela, 40~cm{$\times$}50~cm.
  Cole{\c c}\~ao particular.},
title={Paisagem --- Quatro Barras},
year={1987}}

77 VASO.TIFF. 1999. Altura: 1083 pixels. Largura: 827 pixels. 300 dpi. 32
BIT CMYK. 3.5 Mb. Formato TIFF bitmap. Compactado. Disponível em:
<C:\Carol\VASO.TIFF>. Acesso em: 28 out. 1999.16

@misc{vaso1999,
note={Altura: 1083 pixels. Largura: 827 pixels. 300 dpi. 32 BIT CMYK. 3.5
    Mb.
  Formato TIFF bitmap. Compactado},
title={VASO.TIFF},
url={C:\\Carol\\VASO.TIFF},
urlaccessdate={28 out. 1999},
year={1999}}

78 LEVI, R. Edifício Columbus de propriedade de Lamberto Ramengoni à Rua da
Paz, esquina da Avenida Brigadeiro Luiz Antonio: n. 1930-33. 1997. 108 f. Plantas
diversas. Originais em papel vegetal.

@misc{levi1997,
author={R. Levi},
howpublished={Plantas diversas. Originais em papel vegetal},
pages={108},
 16 Na ‘norma’ aparece o ano quando já tem a data de acesso.

pagename={f.},
subtitle={n. 1930-33.},
title={Edif{\’\i}cio Columbus de propriedade de Lamberto Ramengoni \‘a Rua
    da
  Paz, esquina da Avenida Brigadeiro Luiz Antonio},
year={1997}}

79 DATUM CONSULTORIA E PROJETOS. Hotel Porto do Sol São Paulo: ar
condicionado e ventilação mecânica: fluxograma hidráulico, central de água gelada.
1996. Projeto final. Desenhista: Pedro. N. da obra 1744/96/Folha 10.

@misc{datum1996,
howpublished={Projeto final. Desenhista: Pedro. N. da obra 1744/96/Folha
    10},
month={15 jul.},
organization={Datum Consultoria e Projetos},
subtitle={ar condicionado e ventila{\c c}\~ao mec\^anica: fluxograma
  hidr\’aulico, central de \’agua gelada},
title={Hotel Porto do Sol S\~ao Paulo},
year={1996}}

80 ATLAS Mirador Internacional. Rio de Janeiro: Enciclopédia Britânica do
Brasil, 1981.

@book{britanica1981,
address={Rio de Janeiro},
publisher={Enciclop\’edia Brit\^anica do Brasil},
title={Atlas Mirador Internacional},
year={1981}}

81 INSTITUTO GEOGRÁFICO E CARTOGRÁFICO (São Paulo, SP). Regiões
de governo do Estado de São Paulo. São Paulo, 1994. Plano Cartográfico do
Estado de São Paulo. Escala 1:2.000.

@manual{geografico1994,
address={S\~ao Paulo},
note={Plano Cartogr\’afico do Estado de S\~ao Paulo. Escala 1:2.000},
organization={Instituto Geogr\’afico e Cartogr\’afico {(S\~ao Paulo, SP)}},
title={Regi\~oes de governo do Estado de S\~ao Paulo},
year={1994}}

82 BRASIL e parte da América do Sul: mapa político, escolar, rodoviário,
turístico e regional. São Paulo: Michalany, 1981. 1 mapa, color., 79 cm×95 cm.
Escala 1:600.000.

@book{michalany1981,
address={S\~ao Paulo},
note={1 mapa, color., 79~cm$\times$95~cm. Escala 1:600.000},

publisher={Michalany},
subtitle={mapa pol\’itico, escolar, rodovi\’ario, tur{\’\i}stico e
    regional},
title={Brasil e parte da Am\’erica do Sul},
year={1981}}

83 INSTITUTO GEOGRÁFICO E CARTOGRÁFICO (São Paulo, SP). Projeto
Lins Tupã: foto aérea. São Paulo, 1986. Fx 28, n. 15. Escala 1:35.000.

@manual{geografico1986,
address={S\~ao Paulo},
note={Fx~28, n.~15. Escala 1:35.000},
organization={Instituto Geogr\’afico e Cartogr\’afico {(S\~ao Paulo, SP)}},
subtitle={foto a\’erea},
title={Projeto Lins Tup\~a},
year={1986}}

84 LANDSAT TM 5. São José dos Campos: Instituto Nacional de Pesquisas
Espaciais, 1987–1988. Canais 3, 4 e composição colorida 3, 4 e 5. Escala 1:100.000.

@misc{espaciais1987,
address={S\~ao Jos\’e dos Campos},
howpublished={Canais 3, 4 e composi{\c c}\~ao colorida 3, 4 e 5. Escala
  1:100.000},
publisher={Instituto Nacional de Pesquisas Espaciais},
title={Landsat {TM} 5},
year={1987--1988}}

85 ESTADOS UNIDOS. National Oceanic and Atmospheric Administration.
GOES-08: SE. 13 jul. 1999, 17:42Z. IR04. Itajaí: UNIVALI. Imagem de satélite:
1999071318.GIF: 557 Kb.17

@misc{univali1999,
address={Itaja{\’\i}},
howpublished={Imagem de sat\’elite: 1999071318.GIF: 557 Kb},
organization={Estados Unidos. {National Oceanic and Atmospheric
  Administration}},
publisher={UNIVALI},
title={GOES-08: SE. 13 jul. 1999, 17:42Z. IR04}}

86 MPB especial. [Rio de Janeiro]: Globo: Movieplay, c1995. 1 CD (50 min).
(Globo collection, 2).

@misc{globo1995,
address={[Rio de Janeiro]},
 17 Não dá para entender porque a ‘norma’ não coloca o título em negrito neste exemplo.

howpublished={1 CD (50 min)},
number={2},
publisher={Globo: Movieplay},
series={Globo collection},
title={{MPB} especial},
year={c1995}}

87 ALCIONE. Ouro e cobre. Direção artistica: Miguel Propschi. São Paulo: RCA
Victor, p1988. 1 disco sonoro (45 min), 33 1/3 rpm, estero, 12 pol.

@misc{alcione1988,
address={S\~ao Paulo},
author={Alcione},
furtherresp={Dire{\c c}\~ao artistica: Miguel Propschi},
howpublished={1~disco sonoro (45~min), 33~1/3 rpm, estero, 12~pol.},
publisher={RCA Victor},
title={Ouro e cobre},
year={p1988}}

88 SILVA, L. I. L. da. Luiz Inácio Lula da Silva: depoimento [abr. 1991].
Entrevistadores: V. Tremel e M. Garcia. São Paulo: SENAI-SP, 1991. 2 fitas
cassete (120 min), 3 3/4 pps, estero. Entrevista concedida ao Projeto Memória do
SENAI-SP.

@misc{silva1991,
address={S\~ao Paulo},
author={L. I. L. da Silva},
furtherresp={Entrevistadores: V. Tremel e M. Garcia},
howpublished={2~fitas cassete (120~min), 3~3/4 pps, estero. Entrevista
  concedida ao Projeto Mem\’oria do SENAI-SP},
publisher={SENAI-SP},
subtitle={depoimento [abr. 1991]},
title={Luiz In\’acio Lula da Silva},
year={1991}}

89 FAGNER, R. Revelação. Rio de Janeiro: CBS, 1988. 1 fita cassete (60 min),
3 3/4 pps., estereo.

@misc{fagner1988,
address={Rio de Janeiro},
author={R. Fagner},
howpublished={1~fita cassete (60~min), 3~3/4 pps., estereo},
publisher={CBS},
title={Revela{\c c}\~ao},
year={1988}}

90 SIMONE. Face a face. [S.l.]: Emi-Odeon Brasil, p1977. 1 CD (ca. 40 min).
Remasterizado em digital.

@misc{simone1977,
author={Simone},
howpublished={1~CD (ca. 40~min). Remasterizado em digital},
publisher={Emi-Odeon Brasil},
title={Face a face},
year={p1977}}

91 ALCIONE. Toque macio. A. Gino. [Compositor]. In:              . Ouro e cobre.
Direção Artística: Miguel Propschi. São Paulo: RCA Victor, p1988. 1 disco sonoro
(45 min), 33 1/3 rpm, estéreo, 12 pol. Lado A, faixa 1 (4 min 3 s).18

@inbook{alcionet1988,
address={S\~ao Paulo},
author={Alcione},
booktitle={Ouro e cobre},
furtherresp={Dire{\c c}\~ao Art{\’\i}stica: Miguel Propschi},
note={1~disco sonoro (45~min), 33~1/3 rpm, est\’ereo, 12~pol. Lado~A,
    faixa~1
  (4~min 3~s)},
publisher={RCA Victor},
title={Toque macio. {A. Gino. [Compositor]}},
year={p1988}}

92 SIMONE. Jura secreta. S. Costa, A. Silva. [Compositores]. In:        . Face a
face. [S.l.]: Emi-Odeon Brasil, p1977. 1 CD (ca. 40 min). Faixa 7 (4 min 22 s).
Remasterizado em digital.19

@inbook{simonej1977,
author={Simone},
booktitle={Face a face},
note={1 CD (ca. 40 min). Faixa 7 (4 min 22 s). Remasterizado em digital.},
publisher={Emi-Odeon Brasil},
title={Jura secreta. {S. Costa, A. Silva. [Compositores]}},
year={p1977}}

93 BARTÓK, B. O mandarim maravilhoso: op. 19. Wien: Universal, 1952. 1
partitura (73 p.). Orquestra.

@misc{bart1952,
address={Wien},
author={B. Bart\’ok},
howpublished={1 partitura (73 p.). Orquestra},
publisher={Universal},
subtitle={op. 19},
 18 O compositor foi acrescentado ao título. No original o campo "São Paulo: RCA Victor, p1988"

está repetido. Parece ser um erro de digitação assim como o ponto em "estéreo.".
  19 O compositor foi acrescentado ao título.

title={O mandarim maravilhoso},
year={1952}}

94 GALLET, L. (Org.). Canções populares brasileiras. Rio de Janeiro: Carlos
Wehns, 1851. 1 partitura (23 p.). Piano.

@misc{gallet1851,
address={Rio de Janeiro},
editor={L. Gallet},
editortype={Org.},
howpublished={1 partitura (23 p.). Piano},
publisher={Carlos Wehns},
title={Can{\c c}\~oes populares brasileiras},
year={1851}}

95 VILLA-LOBOS, H. Coleções de quartetos modernos: cordas. Rio de Janeiro:
[s.n.], 1916. 1 partitura (23 p.). Violoncelo.

@misc{villa1916,
address={Rio de Janeiro},
author={H. Villa-Lobos},
howpublished={1 partitura (23 p.). Violoncelo},
subtitle={cordas},
title={Cole{\c c}\~oes de quartetos modernos},
year={1916}}

96 DUCHAMP, M. Escultura para viajar. 1918. 1 escultura variável, borracha
colorida e cordel, dimensões ad lib. Original destruído. Cópia por Richard
Hamilton, feita por ocasião da retrospectiva de Duchamp na Tate Gallery
(Londres) em 1966. Coleção de Arturo Schwarz. Título original: Sculpture for
travelling.

@misc{duchamp1918,
author={M. Duchamp},
howpublished={1 escultura vari\’avel, borracha colorida e cordel,
    dimens\~oes
  \textit{ad lib.} Original destru{\’\i}do. C\’opia por Richard Hamilton,
      feita
  por ocasi\~ao da retrospectiva de Duchamp na Tate Gallery (Londres) em
      1966.
  Cole{\c c}\~ao de Arturo Schwarz. T{\’\i}tulo original: Sculpture for
  travelling},
title={Escultura para viajar},
year={1918}}

97 TAÇA de vidro à maneira de Veneza, com a imagem de Nossa Senhora e o
menino no fuste também decorado com detalhes azuis. Europa, séc. XVIII-XIX,
10,7 cm de diâm. × 24,5 cm de alt.

@misc{europa0000,
howpublished={Europa, s\’ec. XVIII-XIX, 10,7 cm de di\^am. $\times$ 24,5
    cm de
  alt.},
title={Ta{\c{c}}a de vidro \‘a maneira de Veneza, com a imagem de Nossa
    Senhora
  e o menino no fuste tamb\’em decorado com detalhes azuis}}

98 BULE de porcelana: família rosa, decorado com buquês e guirlandas de flores
sobre fundo branco, pegador de tampa em formato de fruto. Marca Companhia
das Índias. China, séc. XIX. 17 cm de alt.

@misc{indias0000,
howpublished={Marca Companhia das \’Indias. China, s\’ec. XIX. 17 cm de
    alt.},
title={Bule de porcelana: fam{\’\i}lia rosa, decorado com buqu\^es e
    guirlandas
  de flores sobre fundo branco, pegador de tampa em formato de fruto}}

99 BIRDS from Amapá: banco de dados. Disponível em: <http:
//www.bdt.org/bdt/avifauna/aves>. Acesso em: 25 nov. 1998.

@misc{birds1998,
subtitle={banco de dados},
title={Birds from Amap\’a},
url={http://www.bdt.org/bdt/avifauna/aves},
urlaccessdate={25 nov. 1998}}

100 FUNDAÇÃO TROPICAL DE PESQUISAS E TECNOLOGIA
"ANDRÉ TOSELLO". Ácaros no Estado de São Paulo (Enseius concordis).
Banco de dados preparado por Carlos H. W. Flechtmann. Disponível em:
<http://www.bdt.org/bdt/acarosp>. Acesso em: 28 nov. 1998.20

@misc{tropical1998,
furtherresp={Banco de dados preparado por Carlos H. W. Flechtmann},
organization={Funda{\c c}\~ao Tropical de Pesquisas e Tecnologia "Andr\’e
  Tosello"},
title={\’Acaros no Estado de S\~ao Paulo (\textit{Enseius concordis})},
url={http://www.bdt.org/bdt/acarosp},
urlaccessdate={28 nov. 1998}}

  20 Este exemplo dado na ‘norma’ parece estar todo equivocado. O exemplo mostra a citação

como se não tivesse um autor (daí a primeira palavra do título em maiúsculas. No entanto há
claramente um autor (a fundação). Veja como está na ‘norma’: ÁCAROS no Estado de São Paulo
(Enseius concordis): banco de dados preparado por Carlos H. W. Flechtmann. In: FUNDAÇÃO
TROPICAL DE PESQUISAS E TECNOLOGIA “ANDRÉ TOSELLO”’. Bases de Dados
Tropical: no ar desde 1985. Disponível em . . .

101 BIOLINE Discussion List. List maintained by the Bases de Dados Tropical,
BDT in Brasil. Disponível em: <http://lisserv@bdt.org.br>. Acesso em: 25 nov.
1998.

@misc{bioline1998,
title={Bioline Discussion List. List maintained by the Bases de Dados
    Tropical,
  BDT in Brasil},
url={http://lisserv@bdt.org.br},
urlaccessdate={25 nov. 1998}}

102 BOOK announcement 13 may 1997. Produced by J. Drummond. Disponível
em: <http://www.bdt.org.br/bioline/DBSearch?BIOLINE-L+READC+57>.
Acesso em: 25 nov. 1998.21

@misc{drummond1998,
furtherresp={Produced by J. Drummond},
title={Book announcement 13 may 1997},
url={http://www.bdt.org.br/bioline/DBSearch?BIOLINE-L+READC+57},
urlaccessdate={25 nov. 1998}}

103 CIVITAS. Coordenação de Simão Pedro P. Marinho. Desenvolvido pela
Pontifícia Universidade Católica de Minas Gerais. 1995–1998. Apresenta
textos sobre urbanismo e desenvolvimento de cidades. Disponível em:
<http://www.gcsnet.com/oamis/civitas>. Acesso em: 27 nov. 1998.22

@misc{coordena1995,
furtherresp={Coordena{\c c}\~ao de Sim\~ao Pedro P. Marinho. Desenvolvido
    pela
  Pontif{\’\i}cia Universidade Cat\’olica de Minas Gerais},
howpublished={Apresenta textos sobre urbanismo e desenvolvimento de
    cidades},
title={Civitas},
url={http://www.gcsnet.com/oamis/civitas},
urlaccessdate={27 nov. 1998},
year={1995-1998}}

104 MARINHO, S. P. P. (Coord.). Civitas. Pontifícia Universidade Católica de
Minas Gerais, 1995–1998. Apresenta textos sobre urbanismo e desenvolvimento de
cidades. Disponível em: <http://www.gcsnet.com/oamis/civitas>. Acesso em: 27
nov. 1998.23

   21 Não dá para entender porque na ‘norma’ todo título foi escrito em maiúsculas (BOOK

ANNOUNCEMENT 12 MAY 1998) e não apenas a primeira palavra. Será que confundiram o
título com o nome de organização?
   22 Claramente há aqui um nome que desempenha papel de editor, minha sugestão para esta

citação está em (104).
   23 Minha sugestão para a referência (103).

@misc{marinho1995,
editor={Marinho, Sim{\~a}o Pedro P.},
editortype={Coord.},
note={Apresenta textos sobre urbanismo e desenvolvimento de cidades},
publisher={Pontif{\’\i}cia Universidade Cat\’olica de Minas Gerais},
title={Civitas},
url={http://www.gcsnet.com/oamis/civitas},
urlaccessdate={27 nov. 1998},
year={1995-1998}}

105 GALERIA virtual de arte do Vale do Paraíba. São José dos Campos:
Fundação Cultural Cassiano Ricardo, 1998. Apresenta reproduções
virtuais de obras de artistas plásticos do Vale do Paraíba. Disponível em:
<http://www.virtualvale.com.br/galeria>. Acesso em: 27 nov. 1998.24

@misc{cassiano1998,
address={S\~ao Jos\’e dos Campos},
howpublished={Apresenta reprodu{\c c}\~oes virtuais de obras de artistas
  pl\’asticos do Vale do Para{\’\i}ba},
publisher={Funda{\c c}\~ao Cultural Cassiano Ricardo},
title={Galeria virtual de arte do Vale do Para{\’\i}ba},
url={http://www.virtualvale.com.br/galeria},
urlaccessdate={27 nov. 1998},
year={1998}}

106 UNIVERSIDADE FEDERAL DO PARANÁ. Biblioteca Central. Normas.doc:
normas para apresentação de trabalhos. Curitiba, 1998. 5 disquetes, 3 1/2 pol.
Word for Windows 7.0.25

@misc{parana1998,
address={Curitiba},
month={7 mar.},
note={5 disquetes, 3~$1/2$~pol. Word for Windows 7.0},
organization={Universidade Federal do Paran\’a. {Biblioteca Central}},
subtitle={normas para apresenta{\c c}\~ao de trabalhos},
title={Normas.doc},
year={1998}}

107 UNIVERSIDADE FEDERAL DO PARANÁ. Biblioteca de Ciência e
Tecnologia. Mapas. Curitiba, 1997. Base de Dados em Microisis, versão 3.7.

@misc{parana1997,
address={Curitiba},
howpublished={Base de Dados em Microisis, vers\~ao 3.7},
organization={Universidade Federal do Paran\’a. {Biblioteca de Ciência e
  24 Esse exemplo difere daquele mostrado na ‘norma’ pelo uso do ‘:’ entre o endereço e a editora.
  25 Na ‘norma’ aparece como “Normas.doc. normas para . . . ". Aqui a segunda parte foi colocada

como subtitle.

  Tecnologia}},
title={Mapas},
year={1997}}

108 MICROSOFT Project for Windows 95, version 4.1: project planning software.
[S.l.]: Microsoft Corporation, 1995. Conjunto de programas. 1 CD-ROM.26

@misc{microsoft1995,
howpublished={Conjunto de programas. 1 CD-ROM},
publisher={Microsoft Corporation},
subtitle={project planning software},
title={Microsoft Project for Windows 95, version 4.1},
year={1995}}

109 ALIE’S play house. Palo Alto, CA: MPC/Opcode Interactive, 1993. 1
CD-ROM. Windows 3.1.

@misc{mpc1993,
address={Palo Alto, CA},
howpublished={1 CD-ROM. Windows 3.1},
publisher={MPC/Opcode Interactive},
title={Alie’s play house},
year={1993}}

110 PAU no gato! Por quê? Rio de Janeiro: Sony Music Book Case Multimedia
Educational, [1990]. 1 CD-ROM. Windows 3.1.

@misc{sony1990,
address={Rio de Janeiro},
howpublished={1 CD-ROM. Windows 3.1},
publisher={Sony Music Book Case Multimedia Educational},
title={Pau no gato! Por qu\^e?},
year={[1990]}}

111 ACCIOLY, F. Publicação eletrônica [mensagem pessoal]. Mensagem recebida
por <mtmendes@uol.com.br> em 26 jan. 2000.

@misc{accioly2000,
author={F. Accioly},
howpublished={Mensagem recebida por $<$mtmendes@uol.com.br$>$ em 26 jan.
    2000},
title={Publica{\c c}\~ao eletr\^onica \normalfont [mensagem pessoal]}}

112 Mudança de estilo após este ponto com o comando
\citeoption{abnt-options1} . Opção selecionada abnt-full-initials=yes.
  26 Que vexame! A ABNT usa windows e word não sabe que a MS fica em Redmond? Ou será

que o soft era pirata e não tinha o certificado de licença com o endereço da MS?

@abnt-options{abnt-options1,
key={x},
abnt-full-initials={yes}}

113 ALVES, Roque de Brito. Ciência criminal. Rio de Janeiro: Forense, 1995.

@book{alves1995,
address={Rio de Janeiro},
author={Roque de Brito Alves},
publisher={Forense},
title={Ci\^encia criminal},
year={1995}}

114 DAMIÃO, Regina Toledo; HENRIQUES, Antonio. Curso de direito judrídico.
São Paulo: Atlas, 1995.

@book{dami1995,
address={S\~ao Paulo},
author={Toledo Dami{\~a}o, Regina and Antonio Henriques},
publisher={Atlas},
title={Curso de direito judr{\’\i}dico},
year={1995}}

115 Mudança de estilo após este ponto com o comando
\citeoption{abnt-options2} . Opção selecionada abnt-full-initials=no.

@abnt-options{abnt-options2,
key={x},
abnt-full-initials={no}}

116 PASSOS, L. M. M.; FONSECA, A.; CHAVES, M. Alegria de saber:
matemática, segunda série, 2, primeiro grau: livro do professor. São Paulo:
Scipione, 1995. 136 p.

@book{passos1995,
address={S\~ao Paulo},
author={Luciana M. M. Passos and Albani Fonseca and Marta Chaves},
pages={136},
publisher={Scipione},
subtitle={matem\’atica, segunda s\’erie, 2, primeiro grau: livro do
    professor},
title={Alegria de saber},
year={1995}}

117 URANI, A. et al. Constituição de uma matriz de contabilidade social para o
Brasil. Brasília, DF: IPEA, 1994.

@book{urani1994,
address={Bras{\’\i}lia, DF},
author={Urani, A and others},
publisher={IPEA},
title={Constitui{\c c}\~ao de uma matriz de contabilidade social para o
  Brasil},
year={1994}}

118 FERREIRA, L. P. (Org.). O fonoaudiólogo e a escola. São Paulo: Summus,
1991.

@book{ferreira1991,
address={S\~ao Paulo},
editor={Piccolotto Ferreira, Leslie},
editortype={Org.},
publisher={Summus},
title={O fonoaudi\’ologo e a escola},
year={1991}}

119 MARCONDES, E.; LIMA, I. N. de (Coord.). Dietas em pediatria clínica. 4.
ed. São Paulo: Sarvier, 1993.

@book{marcondes1993,
address={S\~ao Paulo},
edition={4},
editor={Eduardo Marcondes and de Lima, Ilda Nogueira},
editortype={Coord.},
publisher={Sarvier},
title={Dietas em pediatria cl{\’\i}nica},
year={1993}}

120 MOORE, W. (Ed.). Construtivismo del movimiento educacional: soluciones.
Córdoba, AR: [s.n.], 1960.

@book{moore1960,
address={C\’ordoba, AR},
editor={W. Moore},
subtitle={soluciones},
title={Construtivismo del movimiento educacional},
year={1960}}

121 LUJAN, R. P. (Comp.). Um presente especial. Tradução Sonia da Silva. 3. ed.
São Paulo: Aquariana, 1993. 167 p.

@book{lujan1993,
address={S\~ao Paulo},

edition={3},
editor={Lujan, Roger Patr{\’o}n},
editortype={Comp.},
furtherresp={Tradu{\c c}\~ao Sonia da Silva},
pages={167},
publisher={Aquariana},
title={Um presente especial},
year={1993}}

122 DIAGNÓSTICO do setor editorial brasileiro. São Paulo: Câmara Brasileira
do Livro, 1993. 64 p.

@book{brasileira1993,
address={S\~ao Paulo},
pages={64},
publisher={C\^amara Brasileira do Livro},
title={Diagn\’ostico do setor editorial brasileiro},
year={1993}}

123 DINIZ, J. As pupilas do senhor reitor. 15. ed. São Paulo: Ática, 1994. 263 p.
(Série Bom Livro).

@book{diniz1994,
address={S\~ao Paulo},
author={J{\’u}lio Diniz},
edition={15},
pages={263},
publisher={\’Atica},
series={S\’erie Bom Livro},
title={As pupilas do senhor reitor},
year={1994}}

124 DANTE ALIGHIERI. A divina comédia. Tradução, prefácio e notas: Hernâni
Donato. São Paulo: Círculo do Livro, [1983]. 344 p.27

@book{alighieri1983,
address={S\~ao Paulo},
author={Dante{\space}Alighieri},
furtherresp={Tradu{\c c}\~ao, pref\’acio e notas: Hern\^ani Donato},
pages={344},
publisher={C{\’\i}rculo do Livro},
title={A divina com\’edia},
year={[1983]}}

   27 Neste exemplo a ‘norma’ não explica porque não foi abreviado o nome do autor. Para forçar

 o bibtex a considerar os dois nomes como um só foi usado o comando space entre o ‘Dante’ e o
‘Alighieri’.

125 GOMES, O. O direito de família. Atualização e notas de Humberto Theodoro
Júnior. 11. ed. Rio de Janeiro: Forense, 1995. 562 p.

@book{gomes1995,
address={Rio de Janeiro},
author={O. Gomes},
edition={11},
furtherresp={Atualiza{\c c}\~ao e notas de Humberto Theodoro J\’unior},
pages={562},
publisher={Forense},
title={O direito de fam{\’\i}lia},
year={1995}}

126 ALBERGARIA, L. Cinco anos sem chover: história de lino albergaria.
Ilustrações de Paulo Lyra. 12. ed. São Paulo: FTD, 1994. 63 p.28

@book{albergaria1994,
address={S\~ao Paulo},
author={Lino Albergaria},
edition={12},
furtherresp={Ilustra{\c c}\~oes de Paulo Lyra},
pages={63},
publisher={FTD},
subtitle={hist\’oria de Lino Albergaria},
title={Cinco anos sem chover},
year={1994}}

127 ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. NBR 10520 :
apresentação de citações em documentos: procedimento. Rio de Janeiro, 1988.

@manual{brasileira1988,
address={Rio de Janeiro},
organization={Associa{\c c}\~ao Brasileira de Normas T\’ecnicas},
subtitle={apresenta{\c c}\~ao de cita{\c c}\~oes em documentos:
    procedimento},
title={{NBR} 10520},
year={1988}}

128 UNIVERSIDADE DE SÃO PAULO. Catálogo de teses da Universidade de
São Paulo, 1992. São Paulo, 1993. 467 p.

@manual{universidade1993,
address={S\~ao Paulo},
organization={Universidade de S\~ao Paulo},
pages={467},
title={Cat\’alogo de teses da Universidade de S\~ao Paulo, 1992},
year={1993}}

 28 Nome correto do autor é Lino de Albergaria

129 CONGRESSO BRASILEIRO DE BIBLIOTECONOMIA E DOCUMENTA-
ÇÃO, 10., 1979, Curitiba. Anais... Curitiba: Associação Bibliotecária do Paraná,
1979. 3 v.

@proceedings{biblioteconomia1979,
address={Curitiba},
conference-number={10},
conference-year={1979},
conference-location={Curitiba},
note={3~v.},
organization={Congresso Brasileiro de Biblioteconomia e Documenta{\c
    c}\~ao},
publisher={Associa{\c c}\~ao Bibliotec\’aria do Paran\’a},
title={Anais...},
year={1979}}

130 SÃO PAULO (Estado). Secretaria do Meio Ambiente. Diretrizes para a
politica ambiental do Estado de São Paulo. São Paulo, 1993. 35 p.

@manual{secretaria1993,
address={S\~ao Paulo},
organization={S\~ao Paulo {(Estado). Secretaria do Meio Ambiente.}},
pages={35},
title={Diretrizes para a politica ambiental do Estado de S\~ao Paulo},
year={1993}}

131 BRASIL. Ministério da Justiça. Relatório de atividades. Brasília, DF, 1993.
28 p.

@techreport{justica1993,
address={Bras{\’\i}lia, DF},
organization={Brasil. {Minist\’erio da Justi{\c c}a}},
pages={28},
title={Relat\’orio de atividades},
year={1993}}

132 BIBLIOTECA NACIONAL (Brasil). Relatório da diretoria-geral: 1984. Rio
de Janeiro, 1985. 40 p.

@techreport{biblioteca1985,
address={Rio de Janeiro},
organization={Biblioteca Nacional {(Brasil)}},
pages={40},
subtitle={1984},
title={Relat\’orio da diretoria-geral},
year={1985}}

133 BIBLIOTECA NACIONAL (Portugal). O 24 de julho de 1833 e a guerra
civil de 1829–1834. Lisboa, 1983. 95 p.

@techreport{biblioteca1983,
address={Lisboa},
organization={Biblioteca Nacional {(Portugal)}},
pages={95},
title={O 24 de julho de 1833 e a guerra civil de 1829--1834},
year={1983}}

134 PASTRO, C. Arte sacra: espaço sagrado hoje. São Paulo: Loyola, 1993. 343 p.

@book{pastro1993,
address={S\~ao Paulo},
author={C. Pastro},
pages={343},
publisher={Loyola},
subtitle={espa{\c c}o sagrado hoje},
title={Arte sacra},
year={1993}}

135 GONSALVES, P. E. (Org.). A criança: perguntas e respostas: médicos,
psicólogos, professores, técnicos, dentistas... Prefácio do prof. Dr. Carlos da Silva
Lacaz. São Paulo: Cultrix: Ed. da USP, 1971.29

@book{golsalves1971,
address={S\~ao Paulo},
editor={P. E. Gonsalves},
editortype={Org.},
furtherresp={Pref\’acio do prof. Dr. Carlos da Silva Lacaz},
publisher={Cultrix: Ed.\ da USP},
subtitle={perguntas e respostas: m\’edicos, psic\’ologos, professores,
  t\’ecnicos, dentistas...},
title={A crian{\c c}a},
year={1971}}

136 REVISTA BRASILEIRA DE BIBLIOTECNONOMIA E DOCUMENTAÇÃO.
São Paulo: FEBAB, 1973–1992.

@journalpart{febab1973,
address={S\~ao Paulo},
publisher={FEBAB},
title={Revista Brasileira de Bibliotecnonomia e documenta{\c c}\~ao},
year={1973--1992}}

 29 No original está ‘prof.’ em minúsculas.

137 BOLETIM ESTATÍSTICO [da] Rede Ferroviária Federal. Rio de Janeiro:
[s.n.], 1965–.30

@journalpart{boletim1965,
address={Rio de Janeiro},
howpublished={Trimestral},
title={Boletim Estat{\’\i}stico {[da] Rede Ferrovi\’aria Federal}},
year={1965--}}

138 LEITÃO, D. M. A informação como insumo estratégico. Ci. Inf., Brasília,
DF, v. 22, n. 2, p. 118–123, maio/ago. 1989.

@article{leitao1989,
address={Bras{\’\i}lia, DF},
author={D. M. Leit{\~a}o},
journal={Ci.\ Inf.},
month={maio/ago.},
number={2},
pages={118-123},
title={A informa{\c c}\~ao como insumo estrat\’egico},
volume={22},
year={1989}}

139 SCHAUM, D. Schaum’s outline of theory and problems. 5th. ed. New York:
Schaum Publishing, 1956. 204 p.31

@book{schaum1956,
address={New York},
author={D. Schaum},
edition={5th},
pages={204},
publisher={Schaum Publishing},
title={Schaum’s outline of theory and problems},
year={1956}}

140 PEDROSA, I. Da cor à cor inexistente. 6. ed. Rio de Janeiro: L. Cristiano,
1995. 219 p.

@book{pedrosa1995,
address={Rio de Janeiro},
author={I. Pedrosa},
edition={6},
  30 O ítem 8.2.5 da ‘norma’ trata de títulos ‘genéricos’. Infelizmente o bibtex não tem como

decidir se um título é genérico ou não. Este caso ainda precisa ser trabalhado.
   31 Na verdade a ‘norma’ está em contradição ao usar Publishing pois isso é equivalente a ‘Editor’.

Também o correto seria usar fifth e não 5th, que é o uso tradicional em bibliografias no exterior
(já que querem usar este campo em inglês, que o façam direito).

pages={219},
publisher={L.~Cristiano},
title={Da cor \‘a cor inexistente},
year={1995}}

141 FRANÇA, J. L. et al. Manual para normalização de publicações
técnico-científicas. 3. ed. rev. e aum. Belo Horizonte: Ed. da UFMG, 1996.32

@book{francca1996,
address={Belo Horizonte},
author={J. L. Fran{\c c}a and others},
edition={{3}. ed. rev. e aum.},
publisher={Ed. da UFMG},
title={Manual para normaliza{\c c}\~ao de publica{\c c}\~oes
  t\’ecnico-cient{\’\i}ficas},
year={1996}}

142 FRANÇA, J. L. et al. Manual para normalização de publicações
técnico-científicas. 3. ed. rev. e aum. Belo Horizonte, 1996.33

@manual{francco1996,
address={Belo Horizonte},
author={J. L. Fran{\c c}a and others},
edition={{3}. ed. rev. e aum.},
publisher={Ed. da UFMG},
title={Manual para normaliza{\c c}\~ao de publica{\c c}\~oes
  t\’ecnico-cient{\’\i}ficas},
year={1996}}

143 ZANI, R. Beleza, saúde e bem-estar. São Paulo: Saraiva, 1995. 173 p.

@book{zani1995,
address={S\~ao Paulo},
author={R. Zani},
pages={173},
publisher={Saraiva},
title={Beleza, sa\’ude e bem-estar},
year={1995}}

144 SWOKOWSKI, E. W.; FLORES, V. R. L. F.; MORENO, M. Q. Cálculo de
geometria analítica. Tradução de Alfredo Alves de Faria. Revisão técnica Antonio
Pertence Júnior. 2. ed. São Paulo: Makron Books do Brasil, 1994. 2 v.34
  32 Apesar de ser um manual esta entrada não foi formatada como manual e sim como book pois

não se enquadra na definição de manual do bibtex. Veja o que acontece se esta referência for
formatada como manual em 142. Note que ainda aparece um ‘ed.’ adicional que ainda precisa ser
acertado no estilo.
  33 Aqui a referência 141 foi formatada como manual para fins de comparação.
  34 O título deveria ser: Cálculo e geometria analítica e os últimos dois autores na verdade são

os tradutores.

@book{swokowski1994,
address={S\~ao Paulo},
author={Earl W. Swokowski and Vera Regina L. F. Flores and Quint{\~ao}
    Moreno,
  M{\’a}rcio},
edition={2},
furtherresp={Tradu{\c c}\~ao de Alfredo Alves de Faria. Revis\~ao t\’ecnica
  Antonio Pertence J\’unior},
note={2~v.\footnote{O t{\’\i}tulo deveria ser: C\’alculo {\em e} geometria
  anal{\’\i}tica e os \’ultimos dois autores na verdade s\~ao os
      tradutores.}},
publisher={Makron Books do Brasil},
title={C\’alculo de geometria anal{\’\i}tica},
year={1994}}

145 LAZZARINI NETO, S. Cria e recria. [São Paulo]: SDF Editores, 1994. 108 p.

@book{lazzarini1994,
address={[S\~ao Paulo]},
author={Lazzarini, Neto, S.},
pages={108},
publisher={SDF Editores},
title={Cria e recria},
year={1994}}

146 OS GRANDES clássicos das poesias líricas. [S.l.]: Ex Libris, 1981. 60 f.

@book{libris1981,
pages={60},
pagename={f.},
publisher={Ex Libris},
title={Os~grandes cl\’assicos das poesias l{\’\i}ricas},
year={1981}}

147 KRIEGER, G.; NOVAES, L. A.; FARIA, T. Todos os sócios do presidente. 3.
ed. [S.l.]: Scritta, 1992. 195 p.

@book{krieger1992,
author={G. Krieger and L. A. Novaes and T. Faria},
edition={3},
pages={195},
publisher={Scritta},
title={Todos os s\’ocios do presidente},
year={1992}}

148 DAGHLIAN, J. Lógica e álgebra de Boole. 4. ed. São Paulo: Atlas, 1995.
167 p., il., 21 cm. Bibliografia: p. 166–167. ISBN 85-224-1256-1.

@book{daghalian1995,
address={S\~ao Paulo},
author={J. Daghlian},
edition={4},
dimensions={21~cm},
illustrated={},
isbn={85-224-1256-1},
note={Bibliografia: p.~166--167},
pages={167},
publisher={Atlas},
title={L\’ogica e \’algebra de Boole},
year={1995}}

149 LIMA, M. Tem encontro com Deus: teologia para leigos. Rio de Janeiro:
J. Olympio, 1985.

@book{lima1985,
address={Rio de Janeiro},
author={M. Lima},
publisher={J.~Olympio},
subtitle={teologia para leigos},
title={Tem encontro com Deus},
year={1985}}

150 ALFONSO-GOLDFARB, A. M.; MAIA, C. A. (Coord.). História da ciência:
o mapa do conhecimento. Rio de Janeiro: Expressão e Cultura, 1995. 968 p.
(América 500 anos, 2).35

@book{maia1995,
address={Rio de Janeiro},
editor={Ana Maria Alfonso-Goldfarb and Carlos A. Maia},
editortype={Coord.},
number={2},
pages={968},
publisher={Express\~ao e Cultura},
series={Am\’erica 500 anos},
subtitle={o mapa do conhecimento},
title={Hist\’oria da ci\^encia},
year={1995}}

151 FIGUEIREDO, N. M. Metodologias para a promoção do uso da informação:
técnicas aplicadas particularmente em bibliotecas universitárias especializadas.
São Paulo: Nobel, 1990.

@book{figueiredo1990,
  35 Nesta referência ainda falta modificar o estilo para que seja acrescentado um segundo conjunto

address e publisher.

address={S\~ao Paulo},
author={N. M. Figueiredo},
publisher={Nobel},
subtitle={t\’ecnicas aplicadas particularmente em bibliotecas
    universit\’arias
  especializadas},
title={Metodologias para a promo{\c c}\~ao do uso da informa{\c c}\~ao},
year={1990}}

152 FRANCO, I. Discursos: de outubro de 1992 a agosto de 1993. Brasília, DF:
[s.n.], 1993. 107 p.

@book{franco1993,
address={Bras{\’\i}lia, DF},
author={Itamar Franco},
pages={107},
subtitle={de outubro de 1992 a agosto de 1993},
title={Discursos},
year={1993}}

153 GONÇALVES, F. B. A história de Mirador. [S.l.: s.n.], 1993.

@book{alves1993,
author={F. B. Gon{\c c}alves},
title={A hist\’oria de {Mirador}},
year={1993}}

154 UNIVERSIDADE FEDERAL DE VIÇOSA. Catálogo de graduação,
1994–1995. Viçosa, MG, 1994. 385 p.

@manual{vicosa1994,
address={Vi{\c c}osa, MG},
organization={Universidade Federal de Vi{\c c}osa},
pages={385},
title={Cat\’alogo de gradua{\c c}\~ao, 1994--1995},
year={1994}}

155 LEITE, C. B. O século do desempenho. São Paulo: LTr, 1994. 160 p.

@book{leite1994,
address={S\~ao Paulo},
author={C. B. Leite},
pages={160},
publisher={LTr},
title={O s\’eculo do desempenho},
year={1994}}

156 CIPOLLA, S. Eu e a escola 2a série. São Paulo: Paulinas, 1993. 63 p.

@book{cipolla1993,
address={S\~ao Paulo},
author={S. Cipolla},
pages={63},
publisher={Paulinas},
title={Eu e a escola 2{$^a$} s\’erie},
year={1993}}

157 FLORENZANO, E. Dicionário de idéias semelhantes. Rio de Janeiro:
Ediouro, [1993]. 383 p.

@book{florenzano1993,
address={Rio de Janeiro},
author={E. Florenzano},
pages={383},
publisher={Ediouro},
title={Dicion\’ario de id\’eias semelhantes},
year={[1993]}}

158 CHAVE bíblica. Brasília, DF: Sociedade Bíblica do Brasil, 1970 (impressão
1994). 511 p.

@book{biblica1970,
address={Bras{\’\i}lia, DF},
pages={511},
publisher={Sociedade B{\’\i}blica do Brasil},
title={Chave b{\’\i}blica},
year={1970 (impress\~ao 1994)}}

159 RUCH, G. História geral da civilização: da antigüidade ao XX século. Rio de
Janeiro: F. Briguiet, 1926–1940. 4 v., il., 19 cm.

@book{ruch1926,
address={Rio de Janeiro},
author={G. Ruch},
note={4~v., il., 19~cm},
publisher={F. Briguiet},
subtitle={da Antig\"uidade ao {XX} s\’eculo},
title={Hist\’oria geral da civiliza{\c c}\~ao},
year={1926-1940}}

160 GLOBO RURAL. São Paulo: Rio Gráfica, 1985– . Mensal.36
  36 Aqui o espaço após o ano foi forçado com o comando space para ficar igual ao original, muito

embora esse espaço não ocorra em outros exemplos.

@journalpart{grafica1985,
address={S\~ao Paulo},
note={Mensal},
publisher={Rio Gr\’afica},
title={Globo Rural},
year={1985--\space}}

161 DESENVOLVIMENTO & CONJUNTURA. Rio de Janeiro: Confederação
Nacional da Indústria, 1957–1968. Mensal.

@journalpart{industria1957,
address={Rio de Janeiro},
note={Mensal},
publisher={Confedera{\c c}\~ao Nacional da Ind\’ustria},
title={Desenvolvimento \& Conjuntura},
year={1957-1968}}

162 ALCARDE, J. C.; RODELLA, A. A. O equivalente em carbonato de cálcio
dos corretivos da acidez dos solos. Scientia Agricola, Piracicaba, v. 53, n. 2/3, p.
204–210, maio/dez. 1996.

@article{alcarde1996,
address={Piracicaba},
author={J. C. Alcarde and A. A. Rodella},
journal={Scientia Agricola},
month={maio/dez.},
number={2/3},
pages={204-210},
title={O equivalente em carbonato de c\’alcio dos corretivos da acidez dos
  solos},
volume={53},
year={1996}}

163 BENETTON, M. J. Terapia ocupacional e reabilitação psicossocial: uma
relação possível. Revista de Terapia Ocupacional da Universidade de São Paulo,
São Paulo, v. 4, n. 3, p. 11–16, mar. 1993.

@article{benetton1993,
address={S\~ao Paulo},
author={M. J. Benetton},
journal={Revista de Terapia Ocupacional da Universidade de S\~ao Paulo},
month={mar.},
number={3},
pages={11-16},
title={Terapia ocupacional e reabilita{\c c}\~ao psicossocial: uma rela{\c
  c}\~ao poss{\’\i}vel},
volume={4},
year={1993}}

164 FIGUEIREDO, E. Canadá e antilhas: línguas populares, oralidade e
literatura. Gragoatá, Niterói, n. 1, p. 127–136, 2. sem. 1996.

@article{figueirde1996,
address={Niter\’oi},
author={E. Figueiredo},
journal={Gragoat\’a},
month={2. sem.},
number={1},
pages={127-136},
title={Canad\’a e Antilhas: l{\’\i}nguas populares, oralidade e
    literatura},
year={1996}}

165 LUCCI, E. A. Viver e aprender: estudos sociais, 3: exemplar do professor. 3.
ed. São Paulo: Saraiva, 1994. 96, 7 p.37

@book{lucci1994,
address={S\~ao Paulo},
author={E. A. Lucci},
edition={3},
pages={96, 7},
publisher={Saraiva},
subtitle={estudos sociais, 3: exemplar do professor},
title={Viver e aprender},
year={1994}}

166 FELIPE, J. F. A. A Previdência social na prática forense. 4. ed. Rio de
Janeiro: Forense, 1994. viii, 236 p.38

@book{felipe1994,
address={Rio de Janeiro},
author={J. F. A. Felipe},
edition={4},
pages={viii, 236},
publisher={Forense},
title={A Previd\^encia social na pr\’atica forense},
year={1994}}

167 JAKUBOVIC, J.; LELLIS, M. Matemática na medida certa, 8. série: livro
do professor. 2. ed. São Paulo: Scipione, 1994. 208, xxi p.39
  37 A última parte (“96, 7”) foi colocada num campo pages, não sei exatamente o que quer dizer,

 mas atende ao ítem 8.7.1 da ‘norma’(2).
  38 A última parte (“viii, 236”) foi colocada num campo pages, para atender ao ítem 8.7.1 da

‘norma’(2).
  39 A última parte (“208, xxi”) foi colocada num campo pages, para atender ao ítem 8.7.1 da

‘norma’(2).

@book{lellis1994,
address={S\~ao Paulo},
author={J. Jakubovic and M. Lellis},
edition={2},
pages={208, xxi},
publisher={Scipione},
subtitle={livro do professor},
title={Matem\’atica na medida certa, 8. s\’erie},
year={1994}}

168 PIAGET, J. Para onde vai a educação. 7. ed. Rio de Janeiro: J. Olympio,
1980. 500 p.

@book{piaget1980,
address={Rio de Janeiro},
author={J. Piaget},
edition={7},
pages={500},
publisher={J.~Olympio},
title={Para onde vai a educa{\c c}\~ao},
year={1980}}

169 TABAK, F. A lei como instrumento de mudança social. Fortaleza: Fundação
Waldemar Alcântara, 1993. 17 f.

@book{tabak1993,
address={Fortaleza},
author={F. Tabak},
pages={17},
pagename={f.},
publisher={Funda{\c c}\~ao Waldemar Alc\^antara},
title={A lei como instrumento de mudan{\c c}a social},
year={1993}}

170 TOURINHO FILHO, F. C. Processo penal. 16. ed. rev. e atual. São Paulo:
Saraiva, 1994. 4 v.40

@book{tourinho1994,
address={S\~ao Paulo},
author={Tourinho, Filho, F. C.},
edition={{16.} ed. rev. e atual.},
howpublished={4~v.},
publisher={Saraiva},
title={Processo penal},
year={1994}}

 40 Aqui tivemos a necessidade de ‘enganar’ o estilo bibliográfico. Quando o campo edition inicia

por um número o estilo adiciona automáticamente um "ed.". Neste caso colocamos o número
entre chaves o que resolveu o problema.

171 SILVA, D. P. Vocabulário jurídico. 4. ed. Rio de Janeiro: Forense, 1996. 5 v.
em 3.

@book{silva1996,
address={Rio de Janeiro},
author={D. P. Silva},
edition={4},
note={5~v. em~3},
publisher={Forense},
title={Vocabul\’ario jur{\’\i}dico},
year={1996}}

172 REGO, L. L. B. O desenvolvimento cognitivo e a prontidão para alfabetização.
In: CARRARO, T. N. (Org.). Aprender pensando. 6. ed. Petrópolis: Vozes, 1991. p.
31–40.

@incollection{rego1991,
address={Petr\’opolis},
author={L. L. B. Rego},
booktitle={Aprender pensando},
edition={6},
editor={T. N. Carraro},
editortype={Org.},
pages={31-40},
publisher={Vozes},
title={O desenvolvimento cognitivo e a prontid\~ao para alfabetiza{\c
    c}\~ao},
year={1991}}

173 MARQUES, M. P.; LANZELOTTE, R. G. Banco de dados e hipermídia:
construindo um metamodelo para o projeto portinari. Rio de Janeiro: PUC,
Departamento de Informática, 1993. Paginação irregular.

@book{marques1993,
address={Rio de Janeiro},
author={M. P. Marques and R. G. Lanzelotte},
note={Pagina{\c c}\~ao irregular},
publisher={PUC, Departamento de Inform\’atica},
subtitle={construindo um metamodelo para o Projeto Portinari},
title={Banco de dados e hiperm{\’\i}dia},
year={1993}}

174 SISTEMA de ensino Tamandaré: sargentos do exército e da aeronáutica. [Rio
de Janeiro]: Colégio Curso Tamandaré, 1993. Não paginado.

@book{tamandare1993,
address={[Rio de Janeiro]},
note={N\~ao paginado},

publisher={Col\’egio Curso Tamandar\’e},
subtitle={sargentos do Ex\’ercito e da Aeron\’autica},
title={Sistema de ensino Tamandar\’e},
year={1993}}

175 CESAR, A. M. A bala e a mitra. Recife: Bagaço, 1994. 267 p., il.

@book{cesar1994,
address={Recife},
author={A. M. Cesar},
illustrated={},
pages={267},
publisher={Baga{\c c}o},
title={A bala e a mitra},
year={1994}}

176 AZEVEDO, M. R. de. Viva vida: estudos sociais, 4. São Paulo: FTD, 1994.
194 p., il. color.

@book{azevedo1994,
address={S\~ao Paulo},
author={M. R. de Azevedo},
illustrated={il. color.},
pages={194},
publisher={FTD},
subtitle={estudos sociais, 4.},
title={Viva vida},
year={1994}}

177 BATISTA, Z.; BATISTA, N. O foguete do Guido. Ilustrações de Marilda
Castanha. São Paulo: Ed. do Brasil, 1992. 15 p., principalmente il. color.

@book{batista1992,
address={S\~ao Paulo},
author={Z. Batista and N. Batista},
furtherresp={Ilustra{\c c}\~oes de Marilda Castanha},
illustrated={principalmente il. color.},
pages={15},
publisher={Ed. do Brasil},
title={O foguete do Guido},
year={1992}}

178 CHUEIRE, C. Marca angelical. Ilustração Luciane Fadel. Petrópolis: Vozes,
1994. 18 p., somente il., 20 cm. ISBN 85-326-1087-0.

@book{chueire1994,
address={Petr\’opolis},

author={C. Chueire},
dimensions={20~cm},
furtherresp={Ilustra{\c c}\~ao Luciane Fadel},
illustrated={somente il.},
isbn={85-326-1087-0},
pages={18},
publisher={Vozes},
title={Marca angelical},
year={1994}}

179 DURAN, J. J. Iluminação para vídeo e cinema. São Paulo: [s.n.], 1993.
126 p., 21 cm.

@book{duran1993,
address={S\~ao Paulo},
author={J. J. Duran},
dimensions={21~cm},
pages={126},
title={Ilumina{\c c}\~ao para v{\’\i}deo e cinema},
year={1993}}

180 CHEMELLO, T. Lãs, linhas e retalhos. 3. ed. São Paulo: Global, 1993. 61 p.,
il., 16 cm × 23 cm.

@book{chemello1993,
address={S\~ao Paulo},
author={T. Chemello},
edition={3},
dimensions={16~cm {$\times$}~23~cm},
illustrated={},
pages={61},
publisher={Global},
title={L\~as, linhas e retalhos},
year={1993}}

181 ARBEX JUNIOR, J. Nacionalismo: o desafio à nova ordem pós-socialista.
São Paulo: Scipione, 1993. 104 p., il., 23 cm. (História em aberto).

@book{arbex1993,
address={S\~ao Paulo},
author={Arbex, Junior, J.},
dimensions={23~cm},
illustrated={},
pages={104},
publisher={Scipione},
series={Hist\’oria em aberto},
subtitle={o desafio \‘a nova ordem p\’os-socialista},
title={Nacionalismo},
year={1993}}

182 CARVALHO, M. Guia prático do alfabetizador. São Paulo: Ática, 1994. 95 p.,
21 cm. (Princípios, 243).

@book{carvalho1994,
address={S\~ao Paulo},
author={M. Carvalho},
dimensions={21~cm},
number={243},
pages={95},
publisher={\’Atica},
series={Princ{\’\i}pios},
title={Guia pr\’atico do alfabetizador},
year={1994}}

183 MIGLORI, R. Paradigmas e educação. São Paulo: Aquariana, 1993. v. 1.
20 p., 23 cm. (Visão do futuro, v. 1).

@book{miglori1993,
address={S\~ao Paulo},
author={R. Miglori},
dimensions={23~cm},
pages={20},
publisher={Aquariana},
series={Vis\~ao do futuro},
title={Paradigmas e educa{\c c}\~ao},
volume={1},
year={1993}}

184 AMARAL SOBRINHO, J. Ensino fundamental: gastos das união e do MEC
em 1991: tendências. Brasília, DF: IPEA, 1994. 8 p. (Texto para discussão,
n. 31).41

@book{amaral1994,
address={Bras{\’\i}lia, DF},
author={Amaral, Sobrinho, J.},
number={n.~31},
pages={8},
publisher={IPEA},
series={Texto para discuss\~ao},
subtitle={gastos das Uni\~ao e do {MEC} em 1991: tend\^encias},
title={Ensino fundamental},
year={1994}}

185 RODRIGUES, A. Teatro completo. Organização geral e prefácio Sábato
Magaldi. Rio de Janeiro: Nova Aguilar, 1994. 1134 p., 19 cm. (Biblioteca
luso-brasileira. Serie brasileira).42
 41 O número em série não deveria de levar o ‘n.’, este exemplo é uma exceção. Não sabemos por

que.
  42 Falta mesmo o acento em Série no exemplo da norma.

@book{rodrigues1994,
address={Rio de Janeiro},
author={A. Rodrigues},
dimensions={19~cm},
furtherresp={Organiza{\c c}\~ao geral e pref\’acio S\’abato Magaldi},
pages={1134},
publisher={Nova Aguilar},
series={Biblioteca luso-brasileira. Serie brasileira},
title={Teatro completo},
year={1994}}

186 CARRUTH, J. A nova casa do Bebeto. Desenhos de Tony Hutchings.
Tradução Ruth Rocha. São Paulo: Círculo do Livro, 1993. 21 p. Título original:
Moving House.

@book{carruth1993,
address={S\~ao Paulo},
author={J. Carruth},
furtherresp={Desenhos de Tony Hutchings. Tradu{\c c}\~ao Ruth Rocha},
note={T{\’\i}tulo original: Moving House},
pages={21},
publisher={C{\’\i}rculo do Livro},
title={A nova casa do Bebeto},
year={1993}}

187 SAADI. O jardim das rosas... Tradução de Aurélio Buarque de Holanda. Rio
de Janeiro: J. Olympio, 1944. 124 p., il. (Coleção Rubaiyat). Versão francesa de:
Franz Toussaint. Original árabe.

@book{saadi1994,
address={Rio de Janeiro},
author={Saadi},
furtherresp={Tradu{\c c}\~ao de Aur\’elio Buarque de Holanda},
illustrated={},
note={Vers\~ao francesa de: Franz Toussaint. Original \’arabe},
pages={124},
publisher={J. Olympio},
series={Cole{\c c}\~ao Rubaiyat},
title={O jardim das rosas...},
year={1944}}

188 MANDINO, O. A universidade do sucesso. Tradução de Eugenia Loureiro. 6.
ed. Rio de Janeiro: Record, 1994. 562 p., 21 cm. Título original: The university of
success.

@book{mandino1994,
address={Rio de Janeiro},
author={O Mandino},

edition={6},
dimensions={21~cm},
furtherresp={Tradu{\c c}\~ao de Eugenia Loureiro},
note={T{\’\i}tulo original: The university of success},
pages={562},
publisher={Record},
title={A universidade do sucesso},
year={1994}}

189 MAKAU, A. B. Esperanza de la educación hoy. Lisboa: J. Piaget, 1962.
Separata de: 227

@book{makau1962,
address={Lisboa},
author={A. B. Makau},
publisher={J.~Piaget},
reprinted-from={wmoore1960},
title={Esperanza de la educaci\’on hoy},
year={1962}}

190 LION, M. F.; ANDRADE, J. Drogas cardiovasculares e gravidez. Separata
de: Arquivos Brasileiros de Cardiologia, São Paulo, v. 37, n. 2, p. 125–127, 1981.

@article{lion1981,
address={S\~ao Paulo},
author={M. F. Lion and J. Andrade},
journal={Arquivos Brasileiros de Cardiologia},
number={2},
pages={125-127},
reprinted-text={Separata de},
title={Drogas cardiovasculares e gravidez},
volume={37},
year={1981}}

191 MORGADO, M. L. C. Reimplante dentário. 51 f. Monografia (Especialização)
— Faculdade de Odontologia, Universidade Camilo Castelo Branco, São Paulo,
1990.

@monography{morgado1990,
address={S\~ao Paulo},
author={M. L. C. Morgado},
pages={51},
pagename={f.},
school={Faculdade de Odontologia, Universidade Camilo Castelo Branco},
title={Reimplante dent\’ario},
type={Especializa{\c c}\~ao},
year={1990}}

192 ARAÚJO, U. A. M. Máscaras inteiriças Tukúna: possibilidade de estudo
de artefatos de museu para o conhecimento do universo indígena. 1985. 102 f.
Dissertação (Mestrado em Ciências Sociais) — Fundação Escola de Sociologia
Política de São Paulo, São Paulo, 1986.43

@mastersthesis{araujo1986,
address={S\~ao Paulo},
author={U. A. M. Ara\’ujo},
pages={102},
pagename={f.},
school={Funda{\c c}\~ao Escola de Sociologia Pol{\’\i}tica de S\~ao Paulo},
subtitle={possibilidade de estudo de artefatos de museu para o
    conhecimento do
  universo ind{\’\i}gena},
title={M\’ascaras inteiri{\c c}as Tuk\’una},
type={Mestrado em Ci\^encias Sociais},
year={1986}}

193 Mudança de estilo após este ponto com o comando
\citeoption{abnt-options3} . Opção selecionada abnt-thesis-year=title.

@abnt-options{abnt-options3,
key={x},
abnt-thesis-year={title}}

194 MORGADO, M. L. C. Reimplante dentário. 1990. 51 f. Monografia
(Especialização) — Faculdade de Odontologia, Universidade Camilo Castelo
Branco, São Paulo.

@monography{morgadob1990,
address={S\~ao Paulo},
author={M. L. C. Morgado},
pages={51},
pagename={f.},
school={Faculdade de Odontologia, Universidade Camilo Castelo Branco},
title={Reimplante dent\’ario},
type={Especializa{\c c}\~ao},
year={1990}}

195 Mudança de estilo após este ponto com o comando
\citeoption{abnt-options4} . Opção selecionada abnt-thesis-year=both.

@abnt-options{abnt-options4,
key={x},
abnt-thesis-year={both}}

  43 No original: ‘São Paulo. 1985.’, ou seja um ponto após o endereço ao invés de uma vírgula

que aparentemente deveria ser o correto.

196 MORGADO, M. L. C. Reimplante dentário. 1990. 51 f. Monografia
(Especialização) — Faculdade de Odontologia, Universidade Camilo Castelo
Branco, São Paulo, 1990.

@monography{morgadoc1990,
address={S\~ao Paulo},
author={M. L. C. Morgado},
pages={51},
pagename={f.},
school={Faculdade de Odontologia, Universidade Camilo Castelo Branco},
title={Reimplante dent\’ario},
type={Especializa{\c c}\~ao},
year={1990}}

197 Mudança de estilo após este ponto com o comando
\citeoption{abnt-options5} . Opção selecionada abnt-thesis-year=final.

@abnt-options{abnt-options5,
key={x},
abnt-thesis-year={final}}

198 LAURENTI, R. Mortalidade pré-natal. São Paulo: Centro Brasileiro de
Classificação de Doenças, 1978. Mimeografado.

@book{laurenti1978,
address={S\~ao Paulo},
author={R. Laurenti},
note={Mimeografado},
publisher={Centro Brasileiro de Classifica{\c c}\~ao de Doen{\c c}as},
title={Mortalidade pr\’e-natal},
year={1978}}

199 MARINS, J. L. C. Massa calcificada da naso-faringe. Radiologia Brasileira,
São Paulo, n. 23, 1991. No prelo.

@article{marins1991,
address={S\~ao Paulo},
author={J. L. C. Marins},
journal={Radiologia Brasileira},
note={No prelo},
number={23},
title={Massa calcificada da naso-faringe},
year={1991}}

200 MALAGRINO, W. et al. Estudos preliminares sobre os efeitos de baixas
concentrações de detergentes amiônicos na formação do bisso em Branchidontas

solisianus. In: CONGRESSO BRASILEIRO DE ENGENHARIA SANITÁRIA E
AMBIENTAL, 13., 1985. [S.l.]. Não publicado.44

@inproceedings{malagrino1985,
author={W. Malagrino and others},
conference-number={13},
conference-year={1985},
note={N\~ao publicado},
organization={Congresso Brasileiro de Engenharia Sanit\’aria e Ambiental},
title={Estudos preliminares sobre os efeitos de baixas concentra{\c
    c}\~oes de
  detergentes ami\^onicos na forma{\c c}\~ao do bisso em
      \textit{Branchidontas
  solisianus}}}

201 ZILBERMAN, R. A leitura e o ensino da literatura. São Paulo: Contexto,
1988. Recensão de: 228

@book{zilberman1998,
address={S\~ao Paulo},
author={R. Zilberman},
publisher={Contexto},
reprinted-from={silva1988},
reprinted-text={Recens\~ao de},
title={A leitura e o ensino da literatura},
year={1988}}

202 HOLANDA, S. B. Caminhos e fronteiras. 3. ed. São Paulo: Companhia das
Letras, 1994. 301 p., il., 21 cm. Inclui índice. ISBN 85-7164-411-X.

@book{holanda1994,
address={S\~ao Paulo},
author={S. B. Holanda},
edition={3},
dimensions={21~cm},
illustrated={},
isbn={85-7164-411-X},
note={Inclui {\’\i}ndice},
pages={301},
publisher={Companhia das Letras},
title={Caminhos e fronteiras},
year={1994}}

203 PELOSI, T. O caminho das cordas. Rio de Janeiro: Anais, 1993. 158 p., il.,
21 cm. Bibliografia: p. 115–158.
 44 O original difere completamente, não ficou claro porque a ‘norma’ neste caso fugiu completa-

mente da formatação dos outros exemplos.

@book{pelosi1993,
address={Rio de Janeiro},
author={T. Pelosi},
dimensions={21~cm},
illustrated={},
note={Bibliografia: p. 115--158},
pages={158},
publisher={Anais},
title={O caminho das cordas},
year={1993}}

204 TRINGALI, D. Escolas literárias. São Paulo: Musa, 1994. 246 p., 21 cm.
Inclui bibliografias.

@book{tringali1994,
address={S\~ao Paulo},
author={D. Tringali},
dimensions={21~cm},
note={Inclui bibliografias},
pages={246},
publisher={Musa},
title={Escolas liter\’arias},
year={1994}}

205 RESPRIN: comprimidos. Responsável técnico Delosmar R. Bastos. São José
dos Campos: Johnson & Johnson, 1997. Bula de remédio.45

@misc{delosmar1997,
address={S\~ao Jos\’e dos Campos},
furtherresp={Respons\’avel t\’ecnico Delosmar R.\ Bastos},
note={Bula de rem\’edio},
publisher={Johnson \& Johnson},
subtitle={comprimidos},
title={Resprin},
year={1997}}

206 JOHNSON & JOHNSON. Resprin: comprimidos. Responsável técnico
Delosmar R. Bastos. São José dos Campos, 1997. Bula de remédio.46

@manual{resprinb1997,
address={S\~ao Jos\’e dos Campos},
furtherresp={Respons\’avel t\’ecnico Delosmar R.\ Bastos},
note={Bula de rem\’edio},
  45 Não sabemos porque na ‘norma’ foi formatado desse jeito. Seria mais sensato colocar a

empresa como autora e formatar como manual. Afinal o que é uma bula senão um manual? Veja
na referência 206 a nossa sugestão de formatação.
  46 Esta é a nossa sugestão de formatação para a referência 205.

organization={Johnson \& Johnson},
subtitle={comprimidos},
title={Resprin},
year={1997}}

207 CARDIM, M. S. Constitui o ensino de 2o grau regular noturno uma
verdadeira educação de adultos? Curitiba: Universidade Federal do Paraná, Setor
de Educação, 1984. 3 microfichas. Redução de 1:24.000.

@book{cardim1984,
address={Curitiba},
author={M. S. Cardim},
note={3 microfichas. Redu{\c c}\~ao de 1:24.000},
publisher={Universidade Federal do Paran\’a, Setor de Educa{\c c}\~ao},
title={Constitui o ensino de 2$^o$ grau regular noturno uma verdadeira
    educa{\c
  c}\~ao de adultos?},
year={1984}}

208 CRETELLA JÚNIOR, J. Do impeachment no direito brasileiro. [São Paulo]:
R. dos Tribunais, 1992. 107 p.47

@book{cretella1992,
address={[S\~ao Paulo]},
author={Cretella, J\’unior, J.},
pages={107},
publisher={R. dos Tribunais},
title={Do impeachment no direito brasileiro},
year={1992}}

209 BOLETIM ESTATÍSTICO [da] Rede Ferroviária Federal. Rio de Janeiro,
p. 20, 1965.48

@article{boletime1965,
address={Rio de Janeiro},
pages={20},
title={Boletim~estat{\’\i}stico [da] Rede Ferrovi\’aria Federal},
year={1965}}

210 Mudança de estilo após este ponto com o comando
\citeoption{abnt-repeated-author-omit=yes} . Opção selecionada
abnt-repeated-author-omit=yes.

@abnt-options{abnt-repeated-author-omit=yes,
key={aaaa},
abnt-repeated-author-omit={yes}}

 47 A paginação no exemplo da ‘norma’ está ‘p. 107’.
 48 A paginação no exemplo da ‘norma’ está ‘p. 20’.

211 FREYRE, G. Casa grande & senzala: formação da família brasileira sob
regime de economia patriarcal. Rio de Janeiro: J. Olympio, 1943. 2 v.

@book{freyre1943,
address={Rio de Janeiro},
author={G. Freyre},
howpublished={2~v.},
publisher={J.~Olympio},
subtitle={forma{\c c}\~ao da fam{\’\i}lia brasileira sob regime de economia
  patriarcal},
title={Casa grande \& senzala},
year={1943}}

212        . Sobrados e mocambos: decadência do patriarcado rural no brasil. São
Paulo: Ed. Nacional, 1936.49

@book{freyre1936,
address={S\~ao Paulo},
author={G. Freyre},
publisher={Ed.~Nacional},
subtitle={decad\^encia do patriarcado rural no Brasil},
title={Sobrados e mocambos},
year={1936}}

213 Mudança de estilo após este ponto com o comando
\citeoption{abnt-repeated-author-omit=no} . Opção sele-
cionada abnt-repeated-author-omit=no. Opção selecionada
abnt-repeated-title-omit=no.

@abnt-options{abnt-repeated-author-omit=no,
key={aaaa},
abnt-repeated-author-omit={no},
abnt-repeated-title-omit={no}}

214 Mudança de estilo após este ponto com o comando
\citeoption{abnt-repeated-title-omit=yes} . Opção sele-
cionada abnt-repeated-author-omit=yes. Opção selecionada
abnt-repeated-title-omit=yes.

@abnt-options{abnt-repeated-title-omit=yes,
key={aaaa},
abnt-repeated-author-omit={yes},
abnt-repeated-title-omit={yes}}

215 FREYRE, G. Sobrados e mocambos: decadência do patriarcado rural no
brasil. São Paulo: Ed. Nacional, 1936. 405 p.
 49 O certo deveria ser ‘Nacional’ e não ‘Ed. Nacional’.

@book{freyreg1936,
address={S\~ao Paulo},
author={G. Freyre},
pages={405},
publisher={Ed.~Nacional},
subtitle={decad\^encia do patriarcado rural no Brasil},
title={Sobrados e mocambos},
year={1936}}

216       .      . 2. ed. São Paulo: Ed. Nacional, 1938. 410 p.

@book{freyre1938,
address={S\~ao Paulo},
author={G. Freyre},
edition={2},
pages={410},
publisher={Ed.~Nacional},
subtitle={decad\^encia do patriarcado rural no Brasil},
title={Sobrados e mocambos},
year={1938}}

217 Mudança de estilo após este ponto com o comando
\citeoption{abnt-repeated-title-omit=no} . Opção selecionada
abnt-repeated-title-omit=no.

@abnt-options{abnt-repeated-title-omit=no,
key={aaaa},
abnt-repeated-title-omit={no}}

218 INTERNATIONAL DOI FOUNDATION. The DOI handbook. Oxford, 2003.
Disponível em: <doi:10.1000/182>.

@manual{DOI,
address={Oxford},
month={fev.},
organization={International DOI Foundation},
org-short={IDF},
title={The {DOI} handbook},
url={doi:10.1000/182},
year={2003}}

219 HAMADA, M. Constructive codes for classical and quantum wiretap
channels. In: ROLAND E. CHEN. Cryptography and Research Perspectives. Nova
York, Estados Unidos: Nova Science Publishers, 2008. p. 1–48.

@inbook{hamada2008,

address={Nova York, Estados Unidos},
author={Mitsuru Hamada},
booktitle={Cryptography and Research Perspectives},
organization={Roland E. Chen},
pages={1-48},
publisher={Nova Science Publishers},
title={Constructive Codes for Classical and Quantum Wiretap Channels},
year={2008}}

220 Mudança de estilo após este ponto com o comando \citeoption{ABNT-final}
. Opção selecionada abnt-show-options=list. Opção selecionada
abnt-emphasize=\textbf. Opção selecionada abnt-full-initials=no. Opção
selecionada abnt-thesis-year=final. Opção selecionada abnt-etal-list=3.

@abnt-options{ABNT-final,
key={x},
abnt-emphasize={\textbf},
abnt-full-initials={no},
abnt-show-options={list},
abnt-thesis-year={final}}

221 ARAUJO, L. C. O pacote abntex2cite: tópicos específicos da ABNT
NBR 10520:2002 e o estilo bibliográfico alfabético (sistema autor-data.
[S.l.], 2015. Disponível em: <http://www.abntex.net.br/>.

@manual{abntex2cite-alf,
author={Lauro C{\’e}sar Araujo},
organization={Equipe abnTeX2},
title={O pacote abntex2cite: t{\’o}picos espec{\’\i}ficos da ABNT NBR
  10520:2002 e o estilo bibliogr{\’a}fico alfab{\’e}tico (sistema
      autor-data},
url={http://www.abntex.net.br/},
year={2015}}

222       . A classe abntex2: Modelo canônico de trabalhos
acadêmicos brasileiros compatível com as normas ABNT NBR
14724:2011, ABNT NBR 6024:2012 e outras. [S.l.], 2015. Disponível em:
<http://www.abntex.net.br/>.

@manual{abntex2classe,
author={Lauro C{\’e}sar Araujo},
organization={Equipe abnTeX2},
title={A classe abntex2: Modelo can{\^o}nico de trabalhos acad{\^e}micos
  brasileiros compat{\’\i}vel com as normas ABNT NBR 14724:2011, ABNT NBR
  6024:2012 e outras},
url={http://www.abntex.net.br/},
year={2015}}

223 MARQUES, D. B. biblatex-abnt. [S.l.], 2018. Disponível em:
<http://www.abntex.net.br/>.

@manual{biblatex-abnt,
author={Daniel Ballester Marques},
organization={Equipe abnTeX},
title={biblatex-abnt},
url={http://www.abntex.net.br/},
year={2018}}

224 ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. NBR 6023:
Informação e documentação — referências — elaboração. Rio de Janeiro, 2002.
24 p. Substitui a Ref. 2.

@manual{NBR6023:2002,
address={Rio de Janeiro},
month={ago.},
note={Substitui a Ref.~\citeonline{NBR6023:2000}},
organization={Associa{\c c}\~ao Brasileira de Normas T\’ecnicas},
org-short={ABNT},
pages={24},
subtitle={Informa{\c c}\~ao e documenta{\c c}\~ao --- Refer\^encias ---
  Elabora{\c c}\~ao},
title={{NBR} 6023},
year={2002}}

225 TSEN, K. T.; MORKOÇ, H. Population relaxation time of nonequilibrium
LO phonons and electron-phonon interactions in GaAs–Alx Ga1−x As
multiple-quantum-well structures. Phys. Rev. B, v. 34, p. 4412–4414, 1986.

@article{Tsen86,
author={K T Tsen and H Morko{\c{c}}},
journal={Phys.\ Rev.~B},
pages={4412-4414},
title={Population relaxation time of nonequilibrium {LO} phonons and
  electron-phonon interactions in {GaAs--Al$_x$Ga$_{1-x}$As}
  multiple-quantum-well structures},
volume={34},
year={1986}}

226 ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. NBR 10520:
Informação e documentação — apresentação de citações em documentos. Rio de
Janeiro, 2002. 7 p. Substitui a Ref. 4.

@manual{NBR10520:2002,
address={Rio de Janeiro},
month={ago.},
note={Substitui a Ref.~\citeonline{NBR10520:2001}},
organization={Associa{\c c}\~ao Brasileira de Normas T\’ecnicas},
org-short={ABNT},
pages={7},

subtitle={Informa{\c c}\~ao e documenta{\c c}\~ao --- Apresenta{\c c}\~ao
    de
  cita{\c c}\~oes em documentos},
title={{NBR} 10520},
year={2002}}

227 MOORE, W. (Ed.). Construtivismo del movimiento educacional:
soluciones. Córdoba, AR: [s.n.], 1960. 309-340 p.50

@book{wmoore1960,
address={C\’ordoba, AR},
editor={W. Moore},
pages={309-340},
subtitle={soluciones},
title={Construtivismo del movimiento educacional},
year={1960}}

228 SILVA, E. T. Ci. Inf., Brasília, DF, v. 17, n. 2, jul./dez. 1988.

@article{silva1988,
address={Bras{\’\i}lia, DF},
author={E. T. Silva},
journal={Ci.\ Inf.},
month={jul./dez.},
number={2},
volume={17},
year={1988}}

229 SUN, H. Electronic states of V-shaped semiconductor quantum wires in
electric fields. Phys. Rev. B, v. 58, p. 15381–15384, 1999.

@article{Sun99,
author={H Sun},
journal={Phys.\ Rev.\ B},
pages={15381-15384},
title={Electronic states of {V}-shaped semiconductor quantum wires in
    electric
  fields},
volume={58},
year={1999}}

230 CRECI, G.; WEBER, G. Electron and hole states in V-groove quantum
wires: an effective potential calculation. Semicond. Sci. Technol., v. 14, p.
690–694, 1999.
  50 Essa referência ainda traz importantes problemas de implementação. No original aparecem

dois campos address/publisher. A segunda ocorrência desses campos por enquanto é ignorada
pelo estilo.

@article{Creci99,
author={Geraldo Creci and Gerald Weber},
journal={Semicond.\ Sci.\ Technol.},
pages={690-694},
title={Electron and hole states in {V}-groove quantum wires: an effective
  potential calculation},
volume={14},
year={1999}}

231 SUBRAMANIAM, V.; KIRSCH, A. K.; JOVIN, T. M. Cell biological
applications of scanning near-field optical microscopy (NSOM). Cell. Mol. Biol.,
v. 44, p. 689–700, 1998.

@article{Subramaniam98,
author={V Subramaniam and A K Kirsch and T M Jovin},
journal={Cell.\ Mol.\ Biol.},
pages={689-700},
title={Cell biological applications of scanning near-field optical
    microscopy
  {(NSOM)}},
volume={44},
year={1998}}

232 DENG, Z.-Y. et al. Subband structures and exciton and impurity states
in V-shaped GaAs-Ga1−x Alx As quantum wires. Phys. Rev. B, v. 61, p.
15905–15913, 2000.

@article{Deng00,
author={Z-Y Deng and X Chen and T Ohji and T Kobayashi},
journal={Phys.\ Rev.\ B},
pages={15905-15913},
title={Subband structures and exciton and impurity states in {V}-shaped
  {GaAs-Ga$_{1-x}$Al$_x$As} quantum wires},
volume={61},
year={2000}}

233 EITER, T. et al. Heterogeneous active agents, I: Semantics. Artificial
Intelligence, Elsevier, v. 108, p. 179–255, 1999.

@article{Eiter99:HAA,
author={Eiter, Thomas and others},
journal={Artificial Intelligence},
pages={179-255},
publisher={Elsevier},
title={Heterogeneous Active Agents, {I}: Semantics},
volume={108},
year={1999}}

234 D’INVERNO, M. et al. Formalisms for multi-agent systems. The
Knowledge Engeneering Review, v. 3, n. 12, 1997.

@article{Inverno97:Formalisms,
author={d’Inverno, Mark and Fisher, Michael and Lomuscio, Alessio and Luck,
  Michael and de Rijke, Maarten and Ryan, Mark and Wooldridge, Michael},
journal={The Knowledge Engeneering Review},
number={12},
title={Formalisms for Multi-Agent Systems},
volume={3},
year={1997}}

235 KONEMAN, E. W. et al. Diagnóstico Microbiológico. 5. ed. Buenos
Aires: Médica Panamericana, 1999.

@book{Koneman99,
address={Buenos Aires},
author={E W Koneman and S D Allen and W M Janda and P C Schreckenberger
    and W C
  Winn},
edition={5},
publisher={M{\’e}dica Panamericana},
title={Diagn{\’o}stico Microbiol{\’o}gico},
year={1999}}

236 FERBER, J. Les Systèmes Multi-Agent: Vers une Inteligence
Collective. Paris: InterEditions, 1995.

@book{Ferber95:SMA,
address={Paris},
author={Ferber, Jacques},
publisher={InterEditions},
title={Les Syst\‘emes Multi-Agent: Vers une Inteligence Collective},
year={1995}}

237 CARDONA, M.; GÜNTHERODT, G. (Ed.). Light Scattering in Solids.
Berlin: Springer, 1982. (Topics in applied physics, 51). ISBN 3-540-11513-7.

@book{Cardona82,
address={Berlin},
editor={M. Cardona and G. G{\"u}ntherodt},
isbn={3-540-11513-7},
number={51},
publisher={Springer},
series={Topics in applied physics},
title={Light Scattering in Solids},
year={1982}}

238 JENNINGS, N. R.; WOOLDRIDGE, M. J. Applications of intelligent agents.
In: JENNINGS, N. R.; WOOLDRIDGE, M. J. (Ed.). Agent Technology:
Foundations, Applications, and Markets. Heidelberg: Springer, 1998. p.
3–28.

@incollection{Jennings98:Applications,
address={Heidelberg},
author={Nicholas R. Jennings and Michael J. Wooldridge},
booktitle={Agent Technology: Foundations, Applications, and Markets},
editor={Nicholas R. Jennings and Michael J. Wooldridge},
pages={3--28},
publisher={Springer},
title={Applications of Intelligent Agents},
year={1998}}

239 VALIANT, L. G. Rationality. In: Proc. of the 8th Annual Conference
on Computer Learning Theory. Santa Cruz (CA): [s.n.], 1995.

@inproceedings{Valiant95:Rationality,
address={Santa Cruz (CA)},
author={Valiant, Leslie G.},
booktitle={Proc. of the 8th Annual Conference on Computer Learning Theory},
month={July 5-8},
title={Rationality},
year={1995}}

240 ELAMARAN, B. et al. A Beam-Steerer Using Reconfigurable PBG Ground
Plane. In: MICROWAVE SYMPOSIUM DIGEST, 67., 2000, Massachussets.
Proceedings... Piscataway, NJ: Institute of Electrical and Electronics Engineers,
Inc., 2000. v. 2, p. 835–838.

@inproceedings{Chiao00,
address={Piscataway, NJ},
author={B. Elamaran and Iao-Mak Chio and Liang-Yu Chen and Jung-Chih
    Chiao},
booktitle={Proceedings...},
organization={Microwave Symposium digest,{ 67., 2000, Massachussets}},
pages={835-838},
publisher={Institute of Electrical and Electronics Engineers, Inc.},
title={{A Beam-Steerer Using Reconfigurable PBG Ground Plane}},
volume={2},
year={2000}}

241 BUMGARDNER, J. Syd 1.0.5: User Manual. [S.l.], 1997.

@manual{Bumgardner97:Syd,
author={Bumgardner, Jim},
title={Syd 1.0.5: User Manual},
year={1997}}

242 GIRAFFA, L. M. M. Uma arquitetura de tutor utilizando estados
mentais. Tese (Doutorado) — Universidade Federal do Rio Grande do Sul, Porto
Alegre, 1999.

@phdthesis{Giraffa:1999,
address={Porto Alegre},
author={L{\’u}cia M. Martins Giraffa},
school={Universidade Federal do Rio Grande do Sul},
title={Uma arquitetura de tutor utilizando estados mentais},
year={1999}}

243 SINGH, M. P. Intentions for Multiagent Systems. [S.l.], 1991.

@techreport{Singh91:Intentions,
author={Munindar P. Singh},
institution={Unknown},
title={Intentions for Multiagent Systems},
year={1991}}

244 MCCARTHY, J. Elephant 2000: A programming language based on speech
acts. Artigo do McCarthy sobre a linguage de programação Elephant. 1992.

@unpublished{Mccarthy92:Elephant,
author={John McCarthy},
note={Artigo do McCarthy sobre a linguage de programa\c{c}\~ao Elephant},
title={Elephant 2000: A Programming Language Based on Speech Acts},
year={1992}}

A     Questões específicas da ‘norma’ 6023 e sua im-
      plementação
A.1    A ‘norma’ em contradição com ela mesma
A ‘norma’ diz que os exemplos que traz são normativos. Ocorre que muitos exemplos
não satisfazem a própria ‘norma’. Aqui nós tentamos reproduzir os exemplos de
modo a ter exatamente a mesma formatação. Com os exemplos errados, às vezes
ficamos na situação difícil de ter de reproduzir coisas inconsistentes.

Abreviação de nomes: a referência 124 deveria abreviar o “Dante” mas não é
isso o que é feito no exemplo da ‘norma’ 6023/2000(2). A solução para reproduzir
isso foi formatar o author do seguinte modo:

author ={Dante{\space}Alighieri},

A.2     Elementos essenciais e complementares
Do ítem 7.1.3(2):

      Os elementos complementares são: indicações de outros tipos de
      responsabilidade (ilustrador, tradutor, revisor, adaptador, compila-
      dor etc.); informações sobre características físicas do suporte mate-
      rial, páginas [pages] e/ou volumes [volume], ilustrações, dimensões
      [dimensions](6, 7), série editorial ou coleção [series], notas [notes] e
      ISBN [isbn](6, 7), entre outros.

   book (6, 7, 12, 13, 17); phdthesis (9); booklet (11); manual (14, 15, 16);

Comentário: Veja Tabela 10 sobre a descrição e uso do campo isbn.
   Veja comentário na Subseção A.8, página 94, sobre o posicionamento do ano
em 9.

A.3     Partes de coletâneas [incollection] e livros [inbook]
Do ítem 7.2.2(2):

      Os elementos essenciais são: autor(es) [author], título [subtitle], sub-
      título [subtitle] (se houver) da parte, seguidos da expressão “In:” (18),
      e da referência completa da monografia no todo. No final da referência,
      deve-se informar a paginação [pages] ou outra forma de individualizar
      a parte referenciada.

   incollection (18, 172); inbook (19).

O que ainda precisa ser feito:
  1. Formatar o tipo de editor em (18).

A.4     Eventos, Anais, Proceedings
Na seção 7.5.1(2) é discutido como se referencia artigos em proceedings e os
proceedings em si. É uma completa maluquice! Em nenhum lugar entra o editor dos
proceedings. Isso faz a ‘norma’ da ABNT divergir completamente de qualquer outro
estilo bibliográfico conhecido. Proceedings são sempre publicados e referenciados a
partir do nome dos editores. Significa que uma pessoa que for pegar a referência
formatada pelo estilo da ABNT corre o risco de nunca encontrar tal referência.
    Outro problema é que no lugar do editor a ABNT coloca o nome do evento, o
que normalmente viria no título. Em compensação o título foi quebrado em duas
partes (suspiro!). Assim um proceeding do tipo “Anais da V Reunião dos Usuários
Latex"tem no lugar do editor “REUNIÃO DOS USUÁRIOS LATEX, 5."e no lugar
do título “Anais. . .. Note ainda que o “V"vira “‘5."embora todo mundo diga “V
Reunião"e não “Reunião, 5.". Enfim, se podemos complicar, para que simplificar!?
    Resumindo, a ABNT desprezou a figura importante do editor, quebrou o título
em várias partes, introduziu informações sem importância e fugiu completamente
ao que é internacionalmente aceito para esses tipos de referências.

    Nós sinceramente não sabemos como elaborar um estilo bibtex coerente que
seja compatível com essa bobagem sem introduzir vários campos novos. Vide a
Tabela 14 para a descrição dos campos novos que foram introduzidos.
    Outra adaptação foi usar o campo organization para o nome do evento. Isso
normalmente não é usado em entradas to tipo proceedings e inproceedings, mas
foi a melhor solução encontrada. Novamente, esteja atento que ao usar outros estilos
bibtex suas bibliografias poderão ficar com uma cara muito estranha. Recomendamos
estudar os exemplos aqui apresentados para um resultado aceitável.
    Naturalmente, como é internacionalmente aceito, é usual se referenciar ao editor
e se você já tem entradas formatadas desse modo, o editor aparecerá no lugar de
organization. Existe aí o risco de alguém aborrecer você dizendo que você não
está cumprindo a ‘norma’, mas esse risco é pequeno porque o número de pessoas
que conhece a ‘norma’ a esse ponto é pequeno também.
    proceedings(42, 43, 44, 48, 129); inproceedings(45, 46, 47, 49, 50, 51, 52)

A.5     Nomes pessoais [author]
      8.1.1.1(2) Indica(m)-se o(s) autores [author, editor] pelo último so-
      brenome, em maiúsculas, seguido do(s) prenome(s) e outros sobrenomes
      abreviado(s) ou não. (113, 114) (113, 114, 116)

A.5.1    Comentário:
A ABNT conseguiu quebrar o sobrenome em duas partes. Com isso ficou difícil
gerar uma forma coerente de escrever nomes em bibtex. Bibtex assume que nomes
sejam da forma “First von Last Jr.”. A ABNT misturou o “Last” com o “First”.
O exemplo 113 deveria ser escrito assim: author={Roque de Brito Alves}, aqui
ficou “First=Roque”, “von=de”, e “Last=Brito Alves”. A formatação usual dos
estilos bibtex colocariam então “BRITO ALVES, Roque de”, mas isso não cumpre
a ‘norma’. O nosso estilo consegue contornar o problema e gerar “ALVES, Roque
de Brito”, mas existe a possibilidade de que o nosso mecanismo gere problemas.
Se você quiser reverter ao modo usual do bibtex, use a opção bibtex descrita na
Tabela 4.
    Outro problema é a questão de elementos tipo “Jr.” tais como “Filho”, “Neto”
etc. A ‘norma’ não diz nada explicitamente sobre o que fazer com isso. Pelos
exemplos fica aparente que esses elementos são agregados ao sobrenome. Embora
seja estranho, o estilo trata esses casos sem problema algum. Veja 145, 208, 45, 31, 51

A.6     Título (title) e subtítulo (subtitle)
Do ítem pastro1993(2):
      O título [title, booktitle] e subtítulo [subtitle, booksubtitle]
      devem ser reproduzidos tal como figuram no documento, separados por
      dois pontos.
   Exemplos: article(37) book (12, 17, 82, 116, 134, 152) incollection(18)
manual(2, 14, 15, 16, 83, 127) mastersthesis(192) misc(99).

A.6.1    Comentário:
O subtítulo foi implementado por meio dos novos campos subtitle e booksubtitle
que estão disponível para todas as entradas bibliográficas. A separação por dois
pontos é gerada automaticamente quando o estilo detecta a presença do campo
subtitle ou booksubtitle. Note que em outros estilos bibliográficos os campos
subtitle e booksubtitle serão ignorado. Veja também a Tabela 11.
   Não fica muito claro o que vem a ser um subtítulo nem qual seria a sua serventia.
Não conhecemos nenhum outro estilo bibliográfico que faça uso de subtítulos, daí
não recomendamos o seu uso.

A.7     Ausência de local (address) e editora (publisher)
Do ítem 8.4.5(2):
      Não sendo possível determinar o local [address], utiliza-se a expressão
      Sine loco, abreviada, entre colchetes [S.l.]
   Do ítem franco1993(2):
      Quando a editora [publisher] não é identificada, deve-se indicar a
      expressão sine nomine, abreviada, entre colchetes [s.n.].
   Do ítem alves1993(2):
      Quando o local [address] e o editor [publisher] não puderem ser
      identificados na publicação, utilizam-se ambas as expressões, abreviadas
      e entre colchetes [S.l.: s.n.]

A.7.1    Comentário:
Quando o bibtex encontrar uma entrada book sem campo publisher será feita a
substituição automática por [s.n.]. (152) Se encontrar sem address será colocada
[S.l.]. (146, 147) Se não tiver nenhuma das duas [S.l.: s.n.]. (153)

A.8     Teses, Dissertações, Monografias
Do ítem 8.11.4(2):
      Nas dissertações [mastersthesis], teses [phdthesis] e/ou outros tra-
      balhos acadêmicos [monography] devem ser indicados em nota o tipo
      do documento (monografia, dissertação, tese etc.), o grau [type], a vin-
      culação acadêmica [school], local [address] e a data [ year] da defesa,
      mencionada na folha de aprovação (se houver). (191, 192, 194, 196)

A.8.1    Comentário
Na ‘norma’ os exemplos 191, 192 apresentam alguns problemas. Ambos repetem o
ano duas vezes, a primeira logo após o título e a segunda no final. O exemplo 192
inclusive apresenta duas datas diferentes. Não foi fornecida nenhuma explicação
para essa discrepância. Como na descrição acima se diz “local e a data” optamos
no estilo colocar apenas a data no final logo após o local. É possível alterar o
comportamento do estilo via o campo abnt-thesis-year. Veja a Tabela 4 para
mais detalhes.

B       Referências segundo o tipo de entrada bibtex

Tabela 16: Citações bibliográficas usadas neste documento ordenadas segundo o
tipo de entrada.

 entrada          contribuídas      da referência 2
 article          229, 230, 231,    29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41,
                  232, 233, 234,    55, 56, 57, 58, 59, 61, 62, 64, 65, 67, 72, 138,
                  225               139, 162, 163, 164, 179, 180, 199.
 book             235, 236, 237     6, 7, 12, 13, 17, 20, 23, 24, 25, 54, 60, 68, 69,
                                    70, 80, 82, 113, 114, 116, 117, 118, 119, 120,
                                    121, 122, 123, 124, 125, 126, 134, 135, 140, 141,
                                    143, 144, 145, 146, 147, 148, 150, 149, 151, 152,
                                    153, 155, 156, 157, 158, 159, 165, 166, 167, 168,
                                    169, 170, 171, 173, 174, 175, 176, 177, 178, 181,
                                    182, 183, 184, 185, 186, 187, 188, 198, 202, 203,
                                    204, 207, 208, 211, 212, 215, 216
 booklet                            11, 209
 inbook                             19, 21, 63, 91, 92
 incollection     238               18, 172, 189, 190
 inproceedings    239, 240          45, 46, 47, 49, 50, 51, 52
 journalpart                        26, 27, 28, 136, 137, 160, 161
 manual           241               14, 15, 16, 81, 83, 127, 128, 130, 142, 154
 masterthesis                       192
 misc                               53, 71, 73, 74, 75, 76, 77, 78, 79, 84, 85, 86, 87,
                                    88, 89, 90, 93, 94, 95, 96, 97, 98, 99, 100, 101,
                                    102, 103, 104, 105, 106, 107, 108, 109, 110, 111
 proceedings                        42, 43, 44, 48, 129, 200
 phdthesis        242               9
 techreport       243               131, 132, 133
 unpublished      244
