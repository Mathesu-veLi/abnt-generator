# A classe abntex2 (manual)

> Texto extraído de `abntex2/doc/abntex2.pdf` (abnTeX2 v-1.9.7) com
> `pdftotext -layout`; numeração de página removida. Preserva a quebra de
> linha do PDF, então palavras podem aparecer hifenizadas no fim da linha.
> Para regenerar: `python3 scripts/pdf_to_md.py`.

A classe abntex2:
         Documentos técnicos e científicos brasileiros
             compatíveis com as normas ABNT

                           Lauro César Araujo
                      <http://www.abntex.net.br/>

                     24 de novembro de 2018, v-1.9.7

                                    Resumo
         Este é o manual de uso da classe abntex2. Trata-se de um conjunto de
     customizações da classe memoir para elaboração de documentos técnicos e
     científicos condizentes com as normas da Associação Brasileira de Normas
     Técnicas, especialmente a ABNT NBR 6022:2018, ABNT NBR 10719:2015,
     ABNT NBR 14724:2011 e a ABNT NBR 6024:2012, além de outras referentes
     a “Informação e documentação”.

Sumário
1 Escopo                                                                        3

2 Considerações iniciais                                                         3
  2.1 Introdução . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
  2.2 Histórico do projeto . . . . . . . . . . . . . . . . . . . . . . . . . .   5
  2.3 O que o abnTEX2 traz de novo em relação ao abnTEX1? . . . . . .            5
  2.4 Compatibilidade entre as versões 1 e 2 do abnTEX . . . . . . . . .         6
  2.5 Licença de uso e customizações para universidades e outras instituições 6

3 Estrutura geral de documentos técnicos e científicos brasileiros              7

4 Configurações gerais                                                          8
  4.1 Codificação dos arquivos: UTF8 . . . . . . . . . . . . . . . . . . .      8
  4.2 A classe abntex2 como extensão de memoir . . . . . . . . . . . . . .      9
      4.2.1 O tamanho do papel . . . . . . . . . . . . . . . . . . . . . .      9
      4.2.2 Impressão em anverso e verso . . . . . . . . . . . . . . . . .      9
      4.2.3 Opção article . . . . . . . . . . . . . . . . . . . . . . . . .     9
      4.2.4 As opções de tamanho de fonte e o tamanho “menor e uniforme” 10
      4.2.5 Opções específicas da classe abntex2: títulos de divisões em
             letras maiúsculas . . . . . . . . . . . . . . . . . . . . . . . . 10
      4.2.6 Opções específicas da classe abntex2: alternativas de sumário 11
  4.3 Espaçamentos entre parágrafos e linhas . . . . . . . . . . . . . . . 11
      4.3.1 Tamanho do parágrafo . . . . . . . . . . . . . . . . . . . . . 11
      4.3.2 Tamanho do primeiro parágrafo . . . . . . . . . . . . . . . . 11

        4.3.3 Espaçamento entre parágrafos . . . . . . . . . . . . . . . . .        11
        4.3.4 Espaçamento entre linhas . . . . . . . . . . . . . . . . . . .        11
   4.4 Margens . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    12
   4.5 Numeração contínua de figuras e tabelas . . . . . . . . . . . . . . .        12
   4.6 Índice do PDF com pacote bookmark . . . . . . . . . . . . . . . . .          12
   4.7 Fontes de texto . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    13
        4.7.1 Fontes com XeLATEX . . . . . . . . . . . . . . . . . . . . . .        13
   4.8 Internacionalização . . . . . . . . . . . . . . . . . . . . . . . . . . .    14
        4.8.1 Hifenização e diferentes idiomas . . . . . . . . . . . . . . . .      14
        4.8.2 Alterações de nomes padronizados por babel . . . . . . . . .          15
        4.8.3 Documentos em diferentes idiomas . . . . . . . . . . . . . .          16
   4.9 Macros de dados do documento . . . . . . . . . . . . . . . . . . . .         17
        4.9.1 Título . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    17
        4.9.2 Título estrangeiro . . . . . . . . . . . . . . . . . . . . . . .      18
        4.9.3 Autor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     18
        4.9.4 Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    18
        4.9.5 Instituição . . . . . . . . . . . . . . . . . . . . . . . . . . . .   18
        4.9.6 Localidade . . . . . . . . . . . . . . . . . . . . . . . . . . .      18
        4.9.7 Preâmbulo . . . . . . . . . . . . . . . . . . . . . . . . . . .       18
        4.9.8 Tipo de trabalho . . . . . . . . . . . . . . . . . . . . . . . .      19
        4.9.9 Orientador . . . . . . . . . . . . . . . . . . . . . . . . . . .      19
        4.9.10 Coorientador . . . . . . . . . . . . . . . . . . . . . . . . . .     19
        4.9.11 Exemplo de uso hyperref com dados do documento . . . . .             19
   4.10 Configurações para remissões internas com autoref . . . . . . . .           20
   4.11 Finalização de partes com phantompart . . . . . . . . . . . . . . .         20

5 Elementos pré-textuais e Parte externa                                         21
  5.1 Capa (obrigatório) . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
  5.2 Folha de rosto (obrigatório) . . . . . . . . . . . . . . . . . . . . . . 22
  5.3 Ficha Catalográfica (Dados de catalogação-na-publicação) (obrigatório) 23
  5.4 Errata (opcional) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
  5.5 Folha de aprovação (obrigatório) . . . . . . . . . . . . . . . . . . . 25
  5.6 Dedicatória (opcional) . . . . . . . . . . . . . . . . . . . . . . . . . 26
  5.7 Agradecimentos (opcional) . . . . . . . . . . . . . . . . . . . . . . . 27
  5.8 Epígrafe (opcional) . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
  5.9 Resumos em língua vernácula e estrangeira (obrigatório) . . . . . . 28
  5.10 Lista de ilustrações (opcional) . . . . . . . . . . . . . . . . . . . . . 30
  5.11 Lista de tabelas (opcional) . . . . . . . . . . . . . . . . . . . . . . . 30
  5.12 Lista de abreviaturas e siglas (opcional) . . . . . . . . . . . . . . . 30
  5.13 Lista de símbolos (opcional) . . . . . . . . . . . . . . . . . . . . . . 31
  5.14 Sumário (obrigatório) . . . . . . . . . . . . . . . . . . . . . . . . . 32

6 Elementos textuais                                                                33
  6.1 Formatação dos títulos: partes, capítulos, seções, subseções e sub-
      subseções . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     35
      6.1.1 Estilos adicionais de capítulos . . . . . . . . . . . . . . . . .       35
      6.1.2 Cabeçalhos de capítulos com * . . . . . . . . . . . . . . . .           36
      6.1.3 Espaçamento entre os capítulos e o texto . . . . . . . . . .            36
  6.2 Citações diretas com mais de três linhas . . . . . . . . . . . . . . .        37
  6.3 Alíneas e Subalíneas . . . . . . . . . . . . . . . . . . . . . . . . . .      38

    6.4    Rótulos e legendas . . . . . . . . . . . . . . . . . . . . . . . . . . .   39
    6.5    Tabelas em conformidade com padrões do IBGE . . . . . . . . . .            39
    6.6    Quadros no modelo de trabalho acadêmico . . . . . . . . . . . . . .        40

7 Elementos pós-textuais                                                              41
  7.1 Referências (obrigatório) . . . . . . . . . . . . . . . . . . . . . . . .       41
  7.2 Glossário (opcional) . . . . . . . . . . . . . . . . . . . . . . . . . .        42
  7.3 Apêndices (opcional) . . . . . . . . . . . . . . . . . . . . . . . . . .        43
  7.4 Anexos (opcional) . . . . . . . . . . . . . . . . . . . . . . . . . . .         43
  7.5 Índice (opcional) . . . . . . . . . . . . . . . . . . . . . . . . . . . .       43

8 Mais informações                                                                    44

Referências                                                                           44

Lista de tabelas
    1      Alterações no pacote babel . . . . . . . . . . . . . . . . . . . . . . .   16
    2      Macros de formatação de fonte de divisões do texto . . . . . . . . .       35

1       Escopo
O objetivo deste manual é descrever a classe abntex2, responsável pelo layout dos
elementos de estruturação de documentos técnicos e científicos — como trabalhos
acadêmicos, artigos, relatórios técnicos, livros e folhetos —, especialmente aqueles
definidos pela ABNT NBR 6022:2018, ABNT NBR 10719:2015, ABNT NBR
14724:2011 e pela ABNT NBR 6024:2012. A subseção 2.1 contém a lista completa
de normas observadas pela classe.
Pelo fato de a norma ABNT NBR 14724:2011 e a ABNT NBR 6024:2012 englobarem
os requisitos das demais normas, estas são utilizadas como base de referência para
este manual. De todo modo, a seção 3 descreve as diferentes e similaridades
entre elas e em que medida a classe abntex2 atende a todas as normas listadas no
parágrafo anterior.
Este manual faz parte da suíte abnTEX2. Para referências ao pacote de citações
abntex2cite, consulte Araujo (2015f) e Araujo (2015g).
Exemplos de uso da classe descrita neste manual podem ser consultados em Araujo
(2015e), Araujo (2015b), Araujo (2015d), Araujo (2015c), Araujo (2015a), Cherem
(2015). Os documentos indicados tratam-se de “Modelos Canônicos”, ou seja,
de modelos que não são específicos a nenhuma universidade ou instituição, mas
que implementam exclusivamente os requisitos das normas da ABNT, Associação
Brasileira de Normas Técnicas.

2       Considerações iniciais
2.1       Introdução
Dentre as características de qualidade de trabalhos acadêmicos (teses, dissertações e
outros do gênero), de artigos científicos, de relatórios técnicos e de livros e folhetos,

ao lado da pertinência do tema e dos aspectos relativos ao conteúdo abordado no
trabalho, consta também o resultado da editoração final e as características de
forma e de estruturação dos documentos. Desse modo, a existência de um modelo
e de ferramentas que atendam às normas brasileiras de elaboração de trabalhos
acadêmicos, artigos científicos e relatórios técnicos propostas pela Associação
Brasileira de Normas Técnicas (ABNT) são recursos básicos para o aprimoramento
da qualidade geral dos trabalhos acadêmicos nacionais.
É com esse intuito que o abnTEX2 é apresentado à comunidade acadêmica brasileira:
o de ser um instrumento de aperfeiçoamento da qualidade dos textos produzidos.
O abnTEX2 surge para se somar ao já vasto universo de ferramentas LATEX, porém
que é escasso em utilitários específicos para trabalhos brasileiros. Nesse sentido,
abnTEX2 é proposto como uma evolução do abnTEX1 original1 e como facilitador
na elaboração de documentos técnicos e científicos condizentes com as normas
ABNT.
O abnTEX2 foi desenvolvido com base nos requisitos das seguintes normas ABNT:
ABNT NBR 6022:2018 Informação e documentação - Artigo em publicação
   periódica científica - Apresentação
ABNT NBR 6023:2002 Informação e documentação - Referência - Elaboração2
ABNT NBR 6024:2012 Informação e documentação - Numeração progressiva
   das seções de um documento - Apresentação
ABNT NBR 6027:2012 Informação e documentação - Sumário - Apresentação
ABNT NBR 6028:2003 Informação e documentação - Resumo - Apresentação
ABNT NBR 6029:2006 Informação e documentação - Livros e folhetos - Apre-
   sentação
ABNT NBR 6034:2004 Informação e documentação - Índice - Apresentação
ABNT NBR 10520:2002 Informação e documentação - Citações
ABNT NBR 10719:2015 Informação e documentação - Relatório técnico e-ou
   científico - Apresentação
ABNT NBR 14724:2011 Informação e documentação - Trabalhos acadêmicos -
   Apresentação
ABNT NBR 15287:2011 Informação e documentação - Projeto de pesquisa -
   Apresentação
Este manual de uso não foi escrito sob o modelo do abnTEX2, nem segue os padrões
da ABNT.
Este texto deve ser utilizado como complemento do manual do memoir3 (WILSON;
MADSEN, 2010).
   1 Ver subseção 2.2, Histórico do projeto.
   2 O abnTeX2 é compatível com a versão corrente da norma ABNT NBR 6023:2002. Porém, até

este momento, os manuais Araujo (2015f) e Araujo (2015g) estão atualizados com informações
referentes à versão anterior da referida norma, ou seja, com informações sobre a versão 2000.
A atualização do manual é uma das atividades em execução do projeto. Consulte <https:
//github.com/abntex/abntex2/issues> para outras informações.
   3 <https://www.ctan.org/pkg/memoir>

2.2     Histórico do projeto
Entre 2001 e 2002 nascia o projeto abnTEX original, cujo objetivo era o de
“prover um conjunto de macros para LATEX para formação de trabalhos acadê-
micos condizentes com as normas ABNT”. A última versão estável publicada
pelos integrantes originais4 é a versão 0.8.2 e data de 3.11.2004 (hospedada em
<http://abntex.codigolivre.org.br/>). Em 2006 uma versão não estável foi publi-
cada para testes, mas nunca foi evoluída.
Em maio de 2009 Leandro Salvador fez uma chamada no fórum Tex-BR5 clamando
por voluntários para a retomada do projeto. Embora tenha sido criado um novo
repositório para o projeto6 , nenhuma nova contribuição ao código do abnTEX foi
realizada desde 2006 até dezembro de 2012. No novo endereço há discussões um
pouco mais recentes sobre o projeto, porém datam de 2009. Há, inclusive, uma
sugestão de Gerald Weber, um dos criadores originais:
      “A sugestão que eu daria seria substituir a classe que o Miguel Frasson
      desenvolveu por pacotes padrão do LATEX. Há pacotes que imple-
      mentam praticamente tudo que a ABNT requer, basta mexer nas
      opções. Assim teria algo muito mais simples de manter e atualizar
      no longo prazo.” (<https://sourceforge.net/projects/abntex/forums/
      forum/947854/topic/3265973>)
Os problemas com instalação e distribuição do abnTEX original e as falhas nor-
mativas em relação às normas vigentes da ABNT – uma vez que tinham se
passado quase 10 anos desde a criação do abnTEX– foram motivadores adicionais
para que o novo projeto abnTEX2 se tornasse urgente. Então o novo projeto
foi iniciado oficialmente em maio de 2012 com o apoio dos integrantes do grupo
<http://groups.google.com/group/abntex2> e coordenado por Lauro César Araujo.
A ideia de Gerald e o software já construído do abnTEX original serviriam de ponto
de partida para o abnTEX2.
A primeira versão do abnTEX2 foi concluída em dezembro de 2012 e disponibilizada
ao público em janeiro de 2013. O portal do projeto atual é <http://www.abntex.
net.br/>. O abnTEX2 foi disponibilizado ao CTAN, The Comprehensive TEX
Archive Network, em 2 de janeiro de 2013 e pode ser consultado em <http:
//www.ctan.org/pkg/abntex2>. As principais distribuições LATEX7 são construídas
à partir de pacotes e classes do CTAN.
O software é mantido desde então pela comunidade de indivíduos e de organizações
que adotam e/ou investem em software livre.

2.3     O que o abnTEX2 traz de novo em relação ao abnTEX1?
A suíte abnTEX2 é composta por quatro elementos principais8 :
   • a classe de formação de documentos técnicos e científicos abntex2, descrita
     neste manual;
  4 Os integrantes originais do projeto são Miguel Frasson, Gerald Weber, Leslie H. Watter,

Bruno Parente Lima, Flávio de Vasconcellos Corrêa, Otavio Real Salvador e Renato Machnievscz.
  5 A mensagem pode ser lida neste link: <http://marc.info/?l=tex-br&m=124110883528962>
  6 O projeto de Salvador está hospedado em <https://sourceforge.net/projects/abntex/>.
  7 Como TeX Live, MiKTeX, MacTeX e proTeXt
  8 Somam-se a esses elementos a documentação da classe e do pacote citação.

   • o pacote de citações bibliográficas abntex2cite; e
   • as especificações de formatação de referências bibliográficas abntex2-num.bst
     e abntex2-alf.sty;
   • os modelos canônicos de uso do abnTEX2; (ARAUJO, 2015e; ARAUJO,
     2015b; ARAUJO, 2015d; ARAUJO, 2015c; ARAUJO, 2015a; CHEREM,
     2015)
Esta versão do abnTEX2 fornece uma classe para produção de um vasto número de
documentos técnicos e científicos, como trabalhos acadêmicos, artigos científicos,
relatórios técnicos, projetos de pesquisa, livros, folhetos e outros do gênero. A classe
utilizada por este projeto é completamente nova em relação à utilizada pelo projeto
anterior, que tinha a intenção de produzir um número menor de documentos. A
classe anterior, chamada abnt, não está mais disponível e não é distribuída nesta
versão.
Já o pacote de citações bibliográficas e as especificações de formatação de refe-
rências bibliográficas são uma evolução da versão anterior. Novas funcionalidades
foram incluídas, como a possibilidade de uso do pacote backref (subseção 7.1),
compatibilidade com o beamer9 , entre outros aperfeiçoamentos e ajustes de con-
formidade com a versão 2002 da ABNT NBR 6023. Para referência ao pacote de
citações abntex2cite, inclusive sobre conformidade com as normas, consulte Araujo
(2015f) e Araujo (2015g). O abnTeX2 também traz suporte nativo para produção
de documentos em diferentes idiomas, como inglês por exemplo (subseção 4.8).
Os modelos canônicos não estavam presentes no abnTeX original. Eles são exemplos
de uso do abnTEX2 e são distribuídos junto com a instalação padrão.

2.4     Compatibilidade entre as versões 1 e 2 do abnTEX
As duas versões do abnTEX são compatíveis entre si, ou seja, não há incompatibili-
dade mútua entre elas de tal modo que você pode ter as duas versões do abnTEX
instaladas simultaneamente no mesmo computador. Desse modo, documentos
escritos com a versão anterior do abnTEX continuarão a serem compilados com a
classe e os pacotes anteriores. Apenas documentos escritos conforme este manual
utilizarão a nova classe e os novos pacotes de citação e formatação de referências
bibliográficas.
Com base neste manual você provavelmente não terá dificuldades em converter os
trabalhos escritos em abnTEX1 para o novo abnTEX2.

2.5     Licença de uso e customizações para universidades e
        outras instituições
Sinta-se convidado a participar do projeto abnTEX2! Acesse o site do projeto em
<http://www.abntex.net.br/>. Também fique livre para conhecer, estudar, alterar
e redistribuir o trabalho do abnTEX2, desde que os arquivos modificados tenham
seus nomes alterados, até mesmo no seu computador, e que os créditos sejam dados
aos autores, nos termos da “The LATEXProject Public License”10 .
  9 <http://www.ctan.org/pkg/beamer>
  10 <http://www.latex-project.org/lppl.txt>

Encorajamos que customizações específicas para universidades sejam realizadas
— como capas, folha de aprovação, etc. Porém, recomendamos que ao invés de
se alterar diretamente os arquivos do abnTEX2, distribua-se arquivos com as
respectivas customizações. Isso permite que futuras versões do abnTEX2 não se
tornem automaticamente incompatíveis com as customizações promovidas.

3     Estrutura geral de documentos técnicos e cien-
      tíficos brasileiros
A seção 4 da ABNT NBR 14724:2011 estabelece que a estrutura de trabalhos
acadêmicos compreende duas partes: a externa e a interna, que aparecem no
texto na ordem que segue. Essa norma pode ser considerada uma norma geral de
estrutura de documentos técnicos e científicos porque compartilha com as demais
uma estrutura comum. Os demais parágrafos desta seção descrevem as semelhanças
e diferenças entre as outras normas.
Parte externa
     Capa (obrigatório)
     Lombada (opcional)
Parte Interna
      Elementos pré-textuais
          Folha de rosto (obrigatório) +
          Dados de catalogação-na-publicação11 (opcional)
          Errata (opcional)
          Folha de aprovação (obrigatório)
          Dedicatória (opcional)
          Agradecimentos (opcional)
          Epígrafe (opcional)
          Resumo em língua vernácula (obrigatório)
          Resumo em língua estrangeira (obrigatório)
          Lista de ilustrações (opcional)
          Lista de tabelas (opcional)
          Lista de abreviaturas e siglas (opcional)
          Lista de símbolos (opcional)
          Sumário (obrigatório)
      Elementos textuais 12
          Introdução
          Desenvolvimento
          Conclusão
      Elementos pós-textuais
          Referências (obrigatório)
          Glossário (opcional)
          Apêndice (opcional)
  11 O documento “Dados de catalogação-na-publicação” é chamado apenas como “Ficha catalo-

gráfica” neste texto.
  12 A nomenclatura dos títulos dos elementos textuais é a critério do autor.

            Anexo (opcional)
            Índice (opcional)
O abnTEX2 apresenta instrumentos para produzir todas as partes do documento,
exceto a Lombada e o Glossário, que podem ser produzidos por outros pacotes
adicionais. As seções seguintes descrevem como cada seção pode ser produzida.
A norma ABNT NBR 10719:2015 Informação e documentação - Relatório técnico
e-ou científico - Apresentação apresenta basicamente a mesma estrutura que a
norma de trabalhos acadêmicos, exceto que nesta norma a Capa é opcional, não
há Folha de aprovação, Dedicatória, Epígrafe nem Resumo em língua estrangeira e
acrescenta-se opcionalmente um formulário de identificação como último elemento
pós-textual. Um modelo desse formulário está incluído no modelo (ARAUJO,
2015d). Todos os demais elementos aparecem na mesma ordem e são regidos pelas
mesmas regras nas duas normas.
A norma ABNT NBR 15287:2011 Informação e documentação - Projeto de pesquisa
- Apresentação também apresenta a mesma estrutura básica da ABNT NBR
14724:2011. Porém, na ABNT NBR 15287:2011 a Capa é opcional, não há Errata,
Folha de aprovação, Dedicatória, Agradecimentos, Epígrafe nem Resumos. Todos
os demais elementos aparecem na mesma ordem e, a exemplo da ABNT NBR
10719:2015, são regidos pelas mesmas regras.
Dessa forma, a classe abntex2 pode ser utilizada para gerar os documentos previstos
tanto na ABNT NBR 10719:2015 quanto na ABNT NBR 15287:2011.
Adicionalmente, a classe abntex2 também é compatível com a norma ABNT NBR
6022:2018 Informação e documentação - Artigo em publicação periódica científica
- Apresentação. Porém, nesse caso, a estrutura apresentada nesta seção não é
aplicável. O modelo (ARAUJO, 2015b) é um exemplo de artigo científico elaborado
com a classe abntex2. O mesmo vale para norma ABNT NBR 6029:2006 Informação
e documentação - Livros e folhetos - Apresentação. Nesse caso, o modelo (CHEREM,
2015) é um exemplo de livro ou folheto produzido com a classe abntex2.

4     Configurações gerais
4.1     Codificação dos arquivos: UTF8
A codificação de todos os arquivos do abnTEX2 é UTF8. É necessário que você
utilize a mesma codificação nos documentos que escrever, inclusive nos arquivos de
base bibliográficas .bib.
No preâmbulo do seu documento você geralmente usará os pacotes inputenc13 (com
a opção [utf8]{inputenc}) e fontenc14 (com a opção [T1]{fontenc}) sempre que
xetex ou xelatex não são usados para compilar o documento, ou seja, os pacotes
geralmente devem ser incorporados ao seu documento quando se utiliza pdflatex,
por exemplo. Porém, a classe abntex2 não incorpora os pacotes automaticamente.
  13 O pacote inputenc é usado para que seja possível escrever textos acentuados em determinado

padrão de codificação. No caso, abnTEX2 utiliza a codificação UTF8. Consulte detalhes do
pacote em <http://www.ctan.org/pkg/inputenc>.
  14 O pacote fontenc controla a codificação das fontes usadas para impressão do documento.

Consulte detalhes do pacote em <http://www.ctan.org/pkg/fontenc>.

                  Veja detalhes sobre fontes com XeLATEX na subseção 4.7.1.

                  4.2     A classe abntex2 como extensão de memoir
 \documentclass   A classe abntex2 foi criada como um conjunto de configurações da classe memoir15
                  (WILSON; MADSEN, 2010). Desse modo, todas as opções do memoir estão disponí-
                  veis, como por exemplo, 12pt,openright,twoside,a4paper,article. Consulte
                  o manual do memoir para outras opções.
                  As opções mais comuns de inicialização do texto do documento são:

                  \documentclass[12pt,openright,twoside,a4paper,brazil]{abntex2}

                  Veja a subseção 5.14, a subseção 4.2.4 e a subseção 4.2.5 para outras opções.

                  4.2.1   O tamanho do papel
                  O tamanho do papel pode ser alterado modificando a opção a4paper para a5paper,
                  por exemplo. Porém, o tamanho definido pela ABNT NBR 14724:2011 é A4. A
                  lista completa de opções disponíveis pode ser consultada em Wilson e Madsen
                  (2010, p. 1).

                  4.2.2   Impressão em anverso e verso
                  É interessante observar que a ABNT NBR 14724:2011 (seção 5.1) recomenda que
                  os documentos sejam impressos no anverso e no verso das folhas. Isso é obtido com
                  a opção twoside.

                  4.2.3   Opção article
        article   A opção article é útil para produção de artigos com abnTEX2. Nesse caso, a
\counterwithout   maioria dos elementos pré-textuais descritos na seção 5 se tornam desnecessários.
                  Quando esta opção for utilizada, a classe abntex2 não forçará quebra de página para
                  os elementos pré-textuais, utilizará título estrangeiro (subseção 4.9.2) e definirá a
                  formatação do capítulo de forma idêntica à formatação das seções. Por padrão,
                  quando a opção article estiver presente, você deve iniciar as divisões do documento
                  com \section, e não \chapter, como é usual em trabalhos monográficos. Porém,
                  caso queira iniciar as divisões com \chapter ao invés de \section, adicione as
                  linhas abaixo no preâmbulo do documento para que a numeração dos capítulos,
                  seções, figuras e tabelas sejam corretamente sequenciados:

                  \counterwithout{section}{section}
                  \counterwithout{figure}{chapter}
                  \counterwithout{table}{chapter}

                  A macro \part também é permitida em article.
                   15 A versão anterior do abnT X era baseada na classe report.
                                               E

                       4.2.4     As opções de tamanho de fonte e o tamanho “menor e uniforme”
\ABNTEXfontereduzida   O terceiro parágrafo da seção 5.1 da ABNT NBR 14724:2011 estabelece que o
       \footnotesize   tamanho fonte seja 12 para todo o documento (obtida com a opção 12pt), “inclusive
                12pt   capa, excetuando-se citações com mais de três linhas, notas de rodapé, paginação,
                       dados internacionais de catalogação-na-publicação, legendas e fontes das ilustrações
                       e das tabelas, que devem ser em tamanho menor e uniforme”. Da mesma forma,
                       o terceiro parágrafo da seção 5.1 da ABNT NBR 10719:2015 possui orientação
                       semelhante, ao recomendar que “quando digitado, fonte tamanho 12 e tipo da fonte
                       padronizado para todo o documento. As citações com mais de três linhas, notas
                       de rodapé, paginação, dados internacionais de catalogação-na-publicação, legendas,
                       notas e fontes das ilustrações e tabelas devem ser em tamanho menor e uniforme.”
                       O tamanho “menor e uniforme” é estabelecido pela macro \ABNTEXfontereduzida
                       e o valor padrão utilizado é o mesmo da macro \footnotesize. Você pode alterar
                       o valor de \ABNTEXfontereduzida para \small, por exemplo, com o seguinte
                       comando:

                       \renewcommand{\footnotesize}{\small}

                       Caso deseje utilizar outro tamanho de fonte para o documento, substitua a opção
                       12pt pelo tamanho desejado, como por exemplo, 10pt, ou 14pt. A lista completa
                       de opções disponíveis pode ser consultada em Wilson e Madsen (2010, p. 2-3).

                       4.2.5     Opções específicas da classe abntex2: títulos de divisões em letras
                                 maiúsculas
                        chapter=TITLE
                               Altera para caixa alta (letras maiúsculas) os títulos dos capítulos e o títulos
                               de todos os elementos pré e pós textuais escritos com o mesmo nível que
                               capítulos.
                        section=TITLE, subsection=TITLE, subsubsection=TITLE, subsubsubsection=TITLE
                               Altera para caixa alta (letras maiúsculas) os títulos das seções, subseções,
                               subsubseções e subsubsubseções, respectivamente.
                       Essas opções não controlam o formato dos items no sumário, lista de ilustrações,
                       tabelas, etc., nem controlam o formato dos cabeçalhos de páginas que incluem
                       informações de capítulos ou de secionamento.
                       Exemplo de uso:

                       \documentclass[12pt,openright,twoside,a4paper,
                         chapter=TITLE, % títulos de capítulos convertidos em letras maiúsculas
                         section=TITLE, % títulos de seções convertidos em letras maiúsculas
                         subsection=TITLE, % títulos de subseções convertidos em letras maiúsculas
                         subsubsection=TITLE, % títulos de subsubseções em letras maiúsculas
                         subsubsubsection=TITLE, % títulos de subsubsubseções em letras maiúsculas
                         english,french,spanish,brazil]{abntex2}

4.2.6   Opções específicas da classe abntex2: alternativas de sumário
A subseção 5.14 contém opções adicionais de configuração do sumário.

4.3     Espaçamentos entre parágrafos e linhas
4.3.1   Tamanho do parágrafo
O tamanho do parágrafo, espaço entre a margem e o início da frase do parágrafo,
é definido por:

\setlength{\parindent}{1.3cm}

4.3.2   Tamanho do primeiro parágrafo
Por padrão, não há espaçamento no primeiro parágrafo de cada início de divisão
do documento. Porém, você pode definir que o primeiro parágrafo também seja
indentado. Para isso, apenas inclua o pacote indentfirst no preâmbulo do documento:

\usepackage{indentfirst} % Indenta o primeiro parágrafo de cada seção.

4.3.3   Espaçamento entre parágrafos
O espaçamento entre um parágrafo e outro pode ser controlado por meio do
comando:

\setlength{\parskip}{0.2cm} % tente também \onelineskip

4.3.4   Espaçamento entre linhas
O espaçamento entre linhas padrão é definido como \OnehalfSpacing, ou seja,
um espaço e meio, conforme estabelece a ABNT NBR 14724:2011. De todo modo,
os comando \SingleSpacing, \DoubleSpacing podem ser utilizados para obter
espaçamento simples e espaçamento duplo, respectivamente. Além dessas macros,
estão disponíveis:

\begin{SingleSpace} ...\end{SingleSpace}
\begin{Spacing}{hfactori} ... \end{Spacing}
\begin{OnehalfSpace} ... \end{OnehalfSpace}
\begin{OnehalfSpace*} ... \end{OnehalfSpace*}
\begin{DoubleSpace} ... \end{DoubleSpace}
\begin{DoubleSpace*} ... \end{DoubleSpace*}

Observe que a classe abntex2 utiliza o sistema de espaçamento padrão do memoir.
Nesse caso, o pacote setspace não é necessário.
Para mais informações, consulte Wilson e Madsen (2010, p. 47-52 e 135).

                  4.4    Margens
                  As margens são configuradas conforme a NBR 14724:2011, seção 5.1, e podem ser
                  alteradas do seguinte modo:

                  \setlrmarginsandblock{3cm}{2cm}{*}
                  \setulmarginsandblock{3cm}{2cm}{*}
                  \checkandfixthelayout

                  4.5    Numeração contínua de figuras e tabelas
 \counterwithin   A numeração de figuras e tabelas deve ser contínua em todo o documento (ABNT
                  NBR 14724:2011 seções 5.8 e 5.9). Porém, caso deseje alterar esse comportamento
                  para numeração por capítulos, por exemplo, use:

                  \counterwithin{figure}{section}
                  \counterwithin{table}{section}

                  4.6    Índice do PDF com pacote bookmark
                  O índice da estrutura do documento é automaticamente inserido no PDF final
                  do documento por meio do pacote bookmark16 . Neste documento este índice será
                  identificado como “bookmark do PDF”.
                  Com exceção da Ficha catalográfica (subseção 5.3), todos os elementos pré-
                  textuais descritos na seção 5 e as divisões dos documentos, como \part, \chapter,
                  \section, etc., são automaticamente inseridos tanto no Sumário (subseção 5.14)
                  quanto no bookmark do PDF.
   \pdfbookmark   A versão * dos comandos, como \part* e \chapter*, por exemplo, não inclui
                  a divisão no Sumário, nem no bookmark do PDF nem altera o cabeçalho da
                  página no caso de capítulos. Porém, você pode explicitamente incluir as divisões no
                  bookmark com o comando \pdfbookmark[hposiçãoi]{hTítulo no bookmarki}{htexto
                  de identificação única, sem espaçosi}:

                  \pdfbookmark[0]{Capítulo fora do Sumário, mas presente no
                   bookmark}{texto-qualquer}
                  \chapter*{Capítulo fora do Sumário, mas presente no bookmark}

                  Para alterar o cabeçalho da página automaticamente com o comando \chapter*,
                  consulte a subseção 6.1.2.
                  Para inserir uma divisão com * no sumário, consulte subseção 5.14.
\phantomsection   A macro \phantomsection pode ser útil imediatamente antes de \pdfbookmark,
                  quando o texto adicionado ao bookmark não estiver próxima a uma divisão do
                  documento. Nesse caso, o comando deve ser usado assim:
                   16 <http://www.ctan.org/pkg/bookmark>

                     \phantomsection\pdfbookmark[0]{Capítulo}{texto-qualquer2}
                     \chapter*{Capítulo}

                     Veja a sugestão de uso do bookmark do PDF na subseção 5.10, subseção 5.11,
                     subseção 5.12 e na subseção 5.14.
\pretextualchapter   A macro \pretextualchapter{htítulo do capítuloi} pode ser utilizada para criar
                     capítulos sem numeração, que não aparecem no Sumário, mas que são automatica-
                     mente adicionados ao bookmark do PDF e alteram o cabeçalho da página. Consulte
                     a subseção 6.1 para mais detalhes.
                     Informações adicionais sobre configuração dos bookmarks podem ser obtidas em
                     Oberdiek (2011).

                     4.7     Fontes de texto
                     A ABNT NBR 14724:2011 não determina o uso de alguma fonte específica. Apenas
                     o tamanho, que deve ser 12pt, é estabelecido.
                     Se nenhum pacote de fonte for encontrado, o abnTEX2 utiliza a fonte padrão do
                     LATEX, que é Computer Moderns 17 . Para os títulos das divisões, o abnTEX2 utiliza
                     uma versão sem serifa da fonte. Consulte a subseção 6.1 para mais informações
                     sobre a formatação das divisões.
                     Para escolher uma fonte compilando o documento com pdflatex, utilize um
                     dos pacotes de fontes nativos do LATEX: por exemplo, \usepackage{fourier},
                     para Adobe Utopia; ou, como nos documentos de exemplo do abnTEX2, use
                     \usepackage{lmodern} para a Latin Modern, que é uma versão aprimorada da
                     Computer Modern 18 . Há dezenas de outros pacotes de fontes. Muitos deles estão
                     disponíveis na maioria das distribuições LATEX19 .

                     4.7.1    Fontes com XeLATEX
                     Para utilizar as fontes de tipo .ttf ou .otf — como as presentes em seu sistema
                     operacional ou utilizadas por outros programas —, o arquivo deve estar em co-
                     dificação UTF8 e ser compilado com o comando xelatex (nomedoarquivo.tex).
                     XeTEX é um programa de diagramação derivado do TEX que utiliza Unicode e
                     possibilita o emprego de fontes tipográficas modernas, como OpenType e AAT
                     (Apple Advanced Typography). A classe abntex2 implementa opções para XeLATEX
                     por meio dos pacotes fontspec20 e polyglossia21 .
                     Quando um documento é compilado com xelatex, os pacotes inputenc e fontenc,
                     descritos na subseção 4.1, geralmente não devem ser incluídos ao preâmbulo do
                     documento. Ao invés desses pacotes, geralmente fontspec é usado. O seguinte
                      17 <http://www.tug.dk/FontCatalogue/cmr/>
                      18 Veja mais informações em <http://www.tug.dk/FontCatalogue/lmodern/>.
                       19 Você pode encontrá-las em <http://www.tug.dk/FontCatalogue/>. Há muitas fontes in-

                     teressantes, boas e legíveis, e todas elas podem ser utilizadas compilando o documento com o
                     comando: pdflatex (nome do documento).tex (ou direto no seu editor de texto favorito). Por
                     exemplo, temos as fontes: Charter, Palatino, Utopia, Century. . .
                       20 <http://ctan.org/pkg/fontspec>
                       21 <http://ctan.org/pkg/polyglossia>

exemplo de preâmbulo torna flexível a compilação do documento, que pode tanto
ser realizada da forma tradicional com pdflatex quanto com xelatex, uma vez
que inclui seletivamente os pacotes adequados para cada compilador:

\usepackage{ifxetex}
 \ifxetex
   \usepackage{fontspec}
   \defaultfontfeatures{Ligatures={TeX}}
  \else
   \usepackage[utf8]{inputenc}
   \usepackage[T1]{fontenc}
  \fi

Para fonte serifada, sem serifa (geralmente usada para títulos) e monoespaçada,
respectivamente:

\setromanfont{Minion Pro}
\setsansfont{Myriad Pro}
\setmonofont[Scale=MatchLowercase]{Consolas}

O usuário deve implementar esses comandos, substituindo o nome das fontes pelas
que preferir. É importante destacar que, caso as fontes não sejam embutidas
no PDF22 , o software que lerá o PDF deverá ter disponível a fonte utilizada.
Com o Adobe Acrobat Reader, por exemplo, as fontes gratuitas seguintes já
estão disponíveis: Minion Pro e Myriad Pro23 . Outra fonte de alta qualidade é
Gentium24 .
Para textos em outras línguas, deverão ser utilizados ambientes do pacote polyglossia.
Por exemplo:

\begin{english}
 Text in English...
\end{english}

Para mais informações, consulte <http://www.xelatex.org/>.

4.8     Internacionalização
4.8.1    Hifenização e diferentes idiomas
Para usar as diferentes hifenizações de cada idioma, inclua nas opções do documento
o nome dos idiomas usados no texto. Por exemplo:
  22 As fontes devem ser embutidas do PDF quando, por exemplo, deseja-se produzir documentos

em conformidade com o padrão PDF/A normatizado pela série ISO 19005. Para geração de
PDF/A em LATEX consulte <http://support.river-valley.com/wiki/index.php?title=Generating_
PDF/A_compliant_PDFs_from_pdftex>.
  23 Para Linux, faça o download de: <http://www.adobe.com/support/downloads/detail.jsp?

ftpID=4426>, extraia e instale. Para Windows, vá até a pasta onde instalou o Reader (Arquivos
de Programas), procure as fontes e instale.
  24 <http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=Gentium_download>.

                   \documentclass[12pt,openright,twoside,a4paper,english,french,
                   spanish,brazil]{abntex2}

                   O idioma português-brasileiro (brazil) é incluído automaticamente pela classe
                   abntex2. Porém, mesmo assim a opção brazil deve ser informada como a última
                   opção da classe para que todos os pacotes reconheçam o idioma, além de selecionar
                   o idioma após o preâmbulo (no início do documento). Vale ressaltar que a última
                   opção de idioma é a utilizada por padrão na hifenização do documento. Desse
                   modo, caso deseje escrever um texto em inglês que tenha citações em português e
                   em francês, você deveria usar o preâmbulo e o início do documento como abaixo:

                   \documentclass[12pt,openright,twoside,a4paper,french,brazil,english]{abntex2}
                   ...
                   \begin{document}
                   \selectlanguage{english}
                   ...
                   \end{document}

                   A lista completa de idiomas suportados, bem como outras opções de hifenização,
                   estão disponíveis na documentação do pacote babel25 Braams (2008, p. 5-6).
\foreignlanguage   A macro \foreignlanguage{hidiomai}{htexto a ser inseridoi} insere um texto
                   com a hifenização do idioma informado em {hidiomai}.
   otherlanguage   O ambiente otherlanguage*{hidiomai} pode ser usado para o mesmo propósito
  otherlanguage*   da macro \foreignlanguage. A versão com * indica que apenas o esquema
                   de hifenização do idioma selecionado deve ser utilizado. Nesse caso, as demais
                   configurações de idiomas, como nome da Lista de figuras, rótulos das seções, entre
                   outros, não são alterados. Exemplo de uso:

                   \begin{otherlanguage*}{french}
                    Texte en français.
                   \end{otherlanguage*}

\selectlanguage    A macro \selectlanguage{hidiomai} altera o idioma padrão do documento a
                   partir do ponto em que é informado.
                   Consulte a subseção 4.8.3 para obter detalhes sobre o uso de diferentes idiomas no
                   documento.
                   A subseção 6.2 descreve o ambiente citacao[hlanguagei] que pode receber como
                   parâmetro um idioma a ser usado na citação.

                   4.8.2   Alterações de nomes padronizados por babel
                   Algumas alterações foram realizadas nos nomes padronizados pelo pacote babel
                   para atender a requisitos da ABNT (2011) e da ABNT (2012), conforme Table 1.
                   Se desejar outro comportamento, use:
                    25 <https://www.ctan.org/pkg/babel>

                                    Tabela 1: Alterações no pacote babel
                   Macro                       Valor original                       Novo valor
                   \bibname                    “Referências Bibliográficas”         “Referências”
                   \indexname                  “Índice Remissivo”                   “Índice”
                   \listfigurename             “Lista de Figuras”                   “Lista de ilustrações”
                   \listtablename              “Lista de Tabelas”                   “Lista de tabelas”
                   \pageautorefname            “Página”                             “página”
                   \sectionautorefname         “Seção”                              “seção”
                   \subsectionautorefname      “Subseção”                           “subseção”
                   \subsubsectionautorefname “Subsubseção”                          “subseção”
                   \paragraphautorefname       “Parágrafo”                          “subseção”26

                  \addto\captionsbrazil{
                    %% ajusta nomes padroes do babel
                    \renewcommand{\bibname}{Refer\^encias}
                    \renewcommand{\indexname}{\’Indice}
                    \renewcommand{\listfigurename}{Lista de ilustra\c{c}\~{o}es}
                    \renewcommand{\listtablename}{Lista de tabelas}
                    %% ajusta nomes usados com a macro \autoref
                    \renewcommand{\pageautorefname}{p\’agina}
                    \renewcommand{\sectionautorefname}{se{\c c}\~ao}
                    \renewcommand{\subsectionautorefname}{subse{\c c}\~ao}
                    \renewcommand{\paragraphautorefname}{par\’agrafo}
                    \renewcommand{\subsubsectionautorefname}{subse{\c c}\~ao}
                  }

                  Veja observações sobre as alterações referentes à página, seção, subseção, subsubse-
                  ção e parágrafo na subseção 4.10.

                  4.8.3   Documentos em diferentes idiomas
\selectlanguage   Conforme descrito na subseção 4.8.1, o abnTEX2 já está adequado para produzir
                  documentos técnicos e científicos em português-brasil (padrão) e em inglês. Para
                  alterar o idioma padrão do documento use:

                  \selectlanguage{english}

                  A macro \selectlanguage{english} altera os valores padrões listados na Table 1,
                  bem como o conteúdo de todas as macros de dados listadas na subseção 4.9 para o
                  idioma inglês.
                  Para prover a tradução para outros idiomas, faça como no exemplo, sendo que
                  captionsenglish deve ser alterado para o idioma em questão, conforme descrito
                  no mamual do pacote babel (BRAAMS, 2008):

                  \addto\captionsenglish{% ingles

                      %% adjusts names from abnTeX2
                      \renewcommand{\folhaderostoname}{Title page}
                      \renewcommand{\epigraphname}{Epigraph}
                      \renewcommand{\dedicatorianame}{Dedication}
                      \renewcommand{\errataname}{Errata sheet}
                      \renewcommand{\agradecimentosname}{Acknowledgements}
                      \renewcommand{\anexoname}{ANNEX}
                      \renewcommand{\anexosname}{Annex}
                      \renewcommand{\apendicename}{APPENDIX}
                      \renewcommand{\apendicesname}{Appendix}
                      \renewcommand{\orientadorname}{Supervisor:}
                      \renewcommand{\coorientadorname}{Co-supervisor:}
                      \renewcommand{\folhadeaprovacaoname}{Approval}
                      \renewcommand{\resumoname}{Abstract}
                      \renewcommand{\listadesiglasname}{List of abbreviations and acronyms}
                      \renewcommand{\listadesimbolosname}{List of symbols}
                      \renewcommand{\fontename}{Source}
                      \renewcommand{\notaname}{Note}
                       %% adjusts names used by \autoref
                      \renewcommand{\pageautorefname}{page}
                      \renewcommand{\sectionautorefname}{section}
                      \renewcommand{\subsectionautorefname}{subsection}
                      \renewcommand{\subsubsectionautorefname}{subsubsection}
                      \renewcommand{\paragraphautorefname}{subsubsubsection}
                  }

                  4.9      Macros de dados do documento
                  As macros descritas nas próximas subseções são utilizadas para armazenar dados
                  do documento. Esses dados são utilizados na Capa (subseção 5.1), Folha de rosto
                  (subseção 5.2), Folha de aprovação (subseção 5.5) e Ficha catalográfica (subse-
                  ção 5.3). Recomenda-se que esses dados sejam preenchidos ainda no preâmbulo do
                  documento LATEX, de modo que possam ser úteis para configurações do PDF final
                  com a classe hyperref 27 , por exemplo. A subseção 4.9.11 ilustra um exemplo de
                  configuração do pacote hyperref.
                  As macros \titulo, \autor, \data e seus pares \imprimirtitulo, \imprimirautor
                  e \imprimirdata (subseção 4.9.1, subseção 4.9.3, subseção 4.9.4) são meras tra-
                  duções das macros padrões \title, \author, \date, \thetitle, \theauthor e
                  \thedate, respectivamente. As traduções servem para abstrair o uso do memoir e
                  para simplificar futuras adaptações para outras classes bases.
                  A subseção 4.8.3 descreve como prover traduções para outros idiomas dos nomes
                  descritos nas subseções seguintes.

                  4.9.1     Título
        \titulo   A macro \titulo{htexto do títuloi} é utilizada para armazenar o título do docu-
\imprimirtitulo   mento. O conteúdo armazenado é impresso por meio da macro \imprimirtitulo.
                  Esta macro também executa a macro padrão \title com o mesmo conteúdo
                  informado em \titulo.
                      27 <https://www.ctan.org/pkg/hyperref>

                             4.9.2   Título estrangeiro
        \tituloestrangeiro   A macro \tituloestrangeiro{htexto do títuloi} é utilizada para armazenar o
\imprimirtituloestrangeiro   título do documento em idioma diferente do corpo do texto. O conteúdo armazenado
                             é impresso por meio da macro \imprimirtituloestrangeiro.

                             4.9.3   Autor
                    \autor   A macro \autor{hnome do(s) autor(es)i} é utilizada para armazenar os nomes
            \imprimirautor   dos autores do documento. O conteúdo armazenado é impresso por meio da macro
                             \imprimirautor. Esta macro também executa a macro padrão \author com o
                             mesmo conteúdo informado em \autor.
                     \and    Para inserir múltiplos autores, use \and para que uma vírgula separe os autores
                       \\    no caso de a opção article não estar ativada, ou use \\ para que uma quebra de
                             linha seja inserida entre os autores.
                             No caso de a opção article estar ativada, \and imprime um espaço adicional
                             entre os nomes, de modo que fiquem visualmente em colunas separadas.

                             4.9.4   Data
                    \data    A macro \data{hmês e ano ou data em portuguêsi} é utilizada para armazenar o
            \imprimirdata    mês e ano ou a data do documento. O conteúdo armazenado é impresso por meio
                             da macro \imprimirdata. Esta macro também executa a macro padrão \date
                             com o mesmo conteúdo informado em \data.
                             Durante o desenvolvimento do documento, é possível utilizar \data{\today} para
                             que seja armazenada a data atual.

                             4.9.5   Instituição
             \instituicao    A macro \instituicao{hnome da instituiçãoi} é utilizada para armazenar o
     \imprimirinstituicao    nome da instituição. O conteúdo armazenado é impresso por meio da macro
                             \imprimirinstituicao.

                             4.9.6   Localidade
                   \local    A macro \local{hlocalidade de apresentação do documentoi} é utilizada para
           \imprimirlocal    armazenar a localidade de apresentação do documento, geralmente o nome da
                             cidade e a unidade federativa. O conteúdo armazenado é impresso por meio da
                             macro \imprimirlocal.

                             4.9.7   Preâmbulo
               \preambulo    A macro \preambulo{hpreâmbulo do documentoi} é utilizada para armazenar o
       \imprimirpreambulo    preâmbulo do documento. O preâmbulo é o texto impresso na Folha de rosto e na
                             Folha de aprovação. Ele deve conter o tipo do documento, o objetivo, o nome da
                             instituição e a área de concentração. O conteúdo armazenado é impresso por meio
                             da macro \imprimirpreambulo.

                              4.9.8    Tipo de trabalho
             \tipotrabalho    A macro \tipotrabalho{htipo do trabalhoi} é utilizada para armazenar o tipo de
     \imprimirtipotrabalho    trabalho. Geralmente os textos “Tese (doutorado)” ou “Dissertação (mestrado)”
                              são utilizados. O tipo de trabalho é utilizado na Ficha catalográfica (subseção 5.3).
                              O conteúdo armazenado é impresso por meio da macro \imprimirtipotrabalho.

                              4.9.9    Orientador
               \orientador    A macro \orientador[hrótuloi]{hnome do(s) orientador(es)i} é utilizada para
       \imprimirorientador    armazenar o nome do(s) orientador(es). O parâmetro opcional indica o rótulo a
 \imprimirorientadorRotulo    ser utilizado. O valor padrão do rótulo é “Orientador:”. O conteúdo armazenado é
                              impresso por meio da macro \imprimirorientador e o rótulo pode ser impresso
                              com o comando \imprimirorientadorRotulo.

                              4.9.10    Coorientador
              \coorientador   A macro \coorientador[hrótuloi]{hnome do(s) coorientador(es)i} é utilizada
      \imprimircoorientador   para armazenar o nome do(s) coorientador(es). O parâmetro opcional indica o
\imprimircoorientadorRotulo   rótulo a ser utilizado. O valor padrão do rótulo é “Coorientador:”. O conteúdo
                              armazenado é impresso por meio da macro \imprimircoorientador e o rótulo
                              pode ser impresso com o comando \imprimircoorientadorRotulo.

                              4.9.11    Exemplo de uso hyperref com dados do documento
                              O hyperref 28 é um pacote usado para construir remissões internas e hyper docu-
                              mento.
               \hypersetup    O hyperref pode inserir informações dos dados do documento nos metadados do
                              PDF final, conforme o exemplo, que também altera informações de cores dos links
                              internos do documento final:

                              \usepackage{hyperref}    % controla a formação do índice

                              \titulo{Modelo Canônico de\\ Trabalho Acadêmico com \abnTeX}
                              \autor{Equipe \abnTeX}
                              \local{Brasil}
                              \data{2012}
                              \orientador{Lauro César Araujo}
                              \coorientador{Equipe \abnTeX}
                              \instituicao{%
                                Universidade do Brasil -- UBr
                                \par
                                Faculdade de Arquitetura da Informação
                                \par
                                Programa de Pós-Graduação}
                              \tipotrabalho{Tese (Doutorado)}
                              \preambulo{Modelo canônico de trabalho monográfico acadêmico em
                                  conformidade
                              com as normas ABNT apresentado àcomunidade de usuários \LaTeX.}

                               28 <http://www.ctan.org/pkg/hyperref>.

                             \makeatletter
                             \hypersetup{
                                 pdftitle={\@title},
                                 pdfauthor={\@author},
                                 pdfsubject={\imprimirpreambulo},
                                 pdfkeywords={PALAVRAS}{CHAVE}{EM}{PORTUGUES},
                                 pdfcreator={LaTeX with abnTeX2},
                                 colorlinks=true,
                                 linkcolor=blue,
                                 citecolor=blue,
                                 urlcolor=blue
                             }
                             \makeatother

                             As macros \imprimirtitulo, e \imprimirautor não devem ser usadas no âmbito
                             da configuração de \hypersetup. Ao invés delas, use as macros internas \@title
                             e \@author, conforme o exemplo anterior.
\pdfstringdefDisableCommands Na configuração dos metadados do PDF, o abnTEX2 altera as macros \and e
                             \\, geralmente usadas nos campos de título e autor, para , e ;, respectivamente.
                             Porém, isso pode ser alterado como no exemplo seguinte:

                             \pdfstringdefDisableCommands{\def\\{, }\def\and{; }}

                             4.10     Configurações para remissões internas com autoref
                  \autoref   A macro \autoref{hlabeli} do pacote hyperref 29 é usada para realizar remissões
                             internas que, além do número do elemento, apresentam também o rótulo. Por
                             exemplo, se label é refere-se a uma figura, \autoref{label} imprime “Figura
                             X”, sendo “X” o número sequencial da figura.
                             Isso é especialmente útil ao se nomear divisões do documento, como capítulos,
                             seções, subseções, subsubseções, etc. Ocorre que em português não temos a
                             palavra “subsubseção”. Por isso o abnTEX2 traduz a referência a subsubseções para
                             “subseção”. Além disso, o padrão de nomeação em português provida pelo pacote
                             hyperref desses elementos é colocá-los com letras maiúsculas. Porém, a ABNT
                             (2012, p. 4) apresenta exemplos de remissões internas entre seções e parágrafos com
                             letras minúsculas. Veja a lista completa de alterações realizadas na subseção 4.8.2.
                             As remissões internas a capítulo, parte, figura, tabela e demais não foram alteradas,
                             e serão impressas com letras maiúsculas.

                             4.11     Finalização de partes com phantompart
              \phantompart   A classe abntex2 fornece a macro \phantompart, que simula a finalização de uma
                             parte criada com \part. A macro automaticamente faz com que o próximo capítulo
                             se inicie na raiz do índice do PDF (subseção 4.6), e caso a opção abnt-6027-2012
                             (subseção 5.14) esteja habilitada, também adiciona ao Sumário (subseção 5.14) um
                             espaço vertical equivalente ao espaço do início de um capítulo, ou de uma parte caso
                               29 <http://www.ctan.org/pkg/hyperref>.

                     contrário. A macro \phantompart deve ser usada sempre que um novo capítulo
                     não fizer parte do contexto da parte em que os capítulos anteriores estavam, mas
                     que não seja o caso de se criar uma nova parte para o novo capítulo. Desse modo,
                     não é necessário usar \phantompart no início de partes subsequentes. Exemplo
                     correto de uso:

                     \phantompart

                     \chapter*[Conclusão]{Conclusão}
                     \addcontentsline{toc}{chapter}{Conclusão}

                     \phantompart
                     \printindex

                     Exemplo INCORRETO de uso:

                     \phantompart
                     \part{Nova parte em que phantompart foi usado incorretamente}

                     A macro \phantompart é executado automaticamente em \postextual (seção 7).

                     5     Elementos pré-textuais e Parte externa
      \pretextual    O comando \pretextual identifica o início dos elementos pré-textuais. Esses
     \frontmatter    elementos não possuem numeração de páginas, nem em algarismos romanos, con-
                     forme estabelece a ABNT NBR 14724:2011. Porém, a contagem é iniciada logo
                     após a Capa. A classe abntex2 não faz separação entre “Parte externa” e “Parte
                     interna”, por isso, a macro \pretextual é acionado automaticamente no início de
                     \begin{document} e desse modo você não precisa explicitamente incluí-la em seu
                     documento. A título de coerência, a macro \frontmatter, padrão do memoir, é
                     reescrita para que tenha o mesmo comportamento que \pretextual.
\pretextualchapter   A macro \pretextualchapter{htitulo do capituloi} pode ser utilizado para adici-
                     onar um capítulo com a formatação estabelecida na seção 5.2.3 da ABNT NBR
                     14724:2011 e na seção 4.1 da ABNT NBR 6024:2012. Consulte a subseção 6.1
                     para obter informações sobre o comportamento do bookmark do PDF de capítulos
                     pré-textuais e a subseção 6.1 para ler detalhes adicionais sobre a formatação de
                     capítulos.
                     As subseções seguintes descrevem como cada elemento pré-textual pode ser cons-
                     truído com abnTEX2.

                     5.1   Capa (obrigatório)
    \imprimircapa    A macro \imprimircapa imprime um modelo básico de capa que atende aos
             capa    requisito da seção 4.1.1 da ABNT NBR 14724:2011. A capa é o único elemento
                     “externo” que abnTEX2 produz.
                     A capa não é incluída no bookmark do PDF.

                         Para criar uma capa diferente, você pode reescrever a macro \imprimircapa com
                         base no ambiente capa, conforme o exemplo:

                         \renewcommand{\imprimircapa}{%
                           \begin{capa}%
                             \center
                             \ABNTEXchapterfont\Large UNIVERSIDADE QUE TORNA OS DOCUMENTOS AINDA
                                 MAIS ESTRANHOS

                              \vspace*{1cm}

                              {\ABNTEXchapterfont\large\imprimirautor}

                              \vfill
                              \begin{center}
                              \ABNTEXchapterfont\bfseries\LARGE\imprimirtitulo
                              \end{center}
                              \vfill

                              \large\imprimirlocal

                              \large\imprimirdata

                               \vspace*{1cm}
                             \end{capa}
                         }

                         5.2     Folha de rosto (obrigatório)
\imprimirfolhaderosto    A macro \imprimirfolhaderosto[hnome da folha de rostoi] imprime um modelo
    \folhaderostoname    básico de folha de rosto que atende aos requisito da seção 4.2.1.1 da ABNT NBR
                         14724:2011. A folha de rosto é incluída automaticamente no bookmark do PDF
                         com o nome dado pelo valor do argumento opcional. Caso ele não seja informado,
                         o conteúdo de \folhaderostoname é utilizado (subseção 4.9).
\imprimirfolhaderosto*   A variante \imprimirfolhaderosto*[hnome da folha de rostoi] deve ser utilizada
                         quando se estiver utilizando a impressão frente e verso (twoside) e se desejar
                         incluir a “Ficha catalográfica” (Dados de catalogação-na-publicação, subseção 5.3),
                         que deve ser impressa no verso da Folha de rosto, conforme a seção 4.2.1.1.2 da
                         mesma norma. Observe que o uso de \imprimirfolhaderosto* sem o uso da
                         Ficha catalográfica poderá trazer comportamento não desejado à numeração das
                         páginas. Porém, se a opção \twoside não estiver sendo utilizada, as duas versões
                         da macro têm o mesmo comportamento.
                         Você pode criar uma folha de rosto diferente sem se preocupar com as diferenças
                         entre os comandos \imprimirfolhaderosto e \imprimirfolhaderosto*. Para
                         isso, reescreva a macro \folhaderostocontent, conforme o exemplo:

                         \makeatletter
                         \renewcommand{\folhaderostocontent}{

                       \begin{center}

                        {\ABNTEXchapterfont\large\imprimirautor}

                        \vspace*{\fill}\vspace*{\fill}
                        \begin{center}
                        \ABNTEXchapterfont\bfseries\Large\imprimirtitulo
                        \end{center}
                        \vspace*{\fill}

                        \abntex@ifnotempty{\imprimirpreambulo}{%
                          \hspace{.45\textwidth}
                          \begin{minipage}{.5\textwidth}
                            \SingleSpacing
                             \imprimirpreambulo
                           \end{minipage}%
                           \vspace*{\fill}
                        }%

                       {\abntex@ifnotempty{\imprimirinstituicao}{\imprimirinstituicao
                     \vspace*{\fill}}}

                        {\large\imprimirorientadorRotulo~\imprimirorientador\par}
                        \abntex@ifnotempty{\imprimircoorientador}{%
                           {\large\imprimircoorientadorRotulo~\imprimircoorientador}%
                        }%
                        \vspace*{\fill}

                        {\large\imprimirlocal}
                        \par
                        {\large\imprimirdata}
                        \vspace*{1cm}

                       \end{center}
                     }
                     \makeatother

                     5.3   Ficha Catalográfica (Dados de catalogação-na-publicação)
                           (obrigatório)
fichacatalografica   O ambiente fichacatalografica deve ser utilizado para impressão da Ficha
                     catalográfica, ou “Dados de catalogação-na-publicação”, conforme estabelece a
                     seção 4.2.1.1.2 da ABNT NBR 14724:2011.
                     Caso a impressão frente e verso seja acionada (opção twoside), é necessário que a
                     Folha de rosto (subseção 5.2) seja impressa com a versão estrelada (*) da macro
                     \imprimirfolhaderosto*, para que a Ficha catalográfica seja impressa no verso
                     da Folha de rosto.
                     Um exemplo de uso do comando é:

                     \begin{fichacatalografica}

                  \sffamily
                \vspace*{15cm}    % Posição vertical
                \hrule       % Linha horizontal
                \begin{center}    % Minipage Centralizado
                \begin{minipage}[c]{12.5cm} % Largura

                \imprimirautor

                \hspace{0.5cm} \imprimirtitulo / \imprimirautor. --
                \imprimirlocal, \imprimirdata-

                \hspace{0.5cm} \pageref{LastPage} p. : il.(alguma color.); 30 cm.\\

                \hspace{0.5cm} \imprimirorientadorRotulo \imprimirorientador\\

              \hspace{0.5cm}
              \parbox[t]{\textwidth}{\imprimirtipotrabalho~--~\imprimirinstituicao,
              \imprimirdata.}\\

                \hspace{0.5cm}
                  1. Palavra-chave1.
                  2. Palavra-chave2.
                  I. Orientador.
                  II. Universidade xxx.
                  III. Faculdade de xxx.
                  IV. Título\\

                \hspace{8.75cm} CDU 02:141:005.7\\

                \end{minipage}
                \end{center}
                \hrule
              \end{fichacatalografica}

              O exemplo apresentado necessita do pacote lastpage para que ele possa obter o
              número da última página do documento. Portanto, para usar o exemplo é preciso
              adicionar a linha abaixo ao preâmbulo do documento:

              % usado por abntex2-fichacatalografica.tex
              \usepackage{lastpage}

              A Ficha catalográfica não é incluída no bookmark do PDF (subseção 4.6).

              5.4   Errata (opcional)
     errata   A Errata é um elemento opcional da ABNT NBR 14724:2011, seção 4.2.1.2, que
\errataname   pode ser criada por meio do ambiente errata[hnome da erratai]. O valor do
              parâmetro opcional é utilizado como entrada no bookmark do PDF (subseção 4.6).
              Caso o parâmetro não seja informado, o conteúdo de \errataname é utilizado
              (subseção 4.9).
              Um exemplo de uso do ambiente é:

                        \begin{errata}

                        FERRIGNO, C. R. A. \textbf{Tratamento de neoplasias ósseas apendiculares
                            com
                        reimplantação de enxerto ósseo autólogo autoclavado associado ao plasma
                        rico em plaquetas}: estudo crítico na cirurgia de preservação de membro em
                        cães. 2011. 128 f. Tese (Livre-Docência) - Faculdade de Medicina
                            Veterinária
                        e Zootecnia, Universidade de São Paulo, São Paulo, 2011.

                        \begin{table}[htb]
                        \center
                        \footnotesize
                        \begin{tabular}{|p{1.4cm}|p{1cm}|p{3cm}|p{3cm}|}
                          \hline
                          \textbf{Folha} & \textbf{Linha} & \textbf{Onde se lê} &
                              \textbf{Leia-se}\\
                          \hline
                          1 & 10 & auto-conclavo & autoconclavo\\
                          \hline
                        \end{tabular}
                        \end{table}

                        \end{errata}

                        5.5    Folha de aprovação (obrigatório)
     folhadeaprovacao   O ambiente folhadeaprovacao[hnome da folha de aprovaçãoi] permite a criação
\folhadeaprovacaoname   de uma Folha de aprovação, elemento obrigatório da ABNT NBR 14724:2011
                        descrita na seção 4.2.1.3 da norma. O valor do parâmetro opcional é utilizado como
                        entrada no bookmark do PDF (subseção 4.6). Caso o parâmetro não seja informado,
                        o conteúdo de \folhadeaprovacaoname é utilizado (subseção 4.9). Conforme
                        estabelece a seção 5.2.4 da norma em tela, a Folha de aprovação não possui título
                        nem indicador numérico.
          \includepdf   Um modelo de Folha de aprovação não é oferecido pelo abnTEX2 porque ela varia
                        largamente entre instituições. E, além disso, provavelmente você incluirá uma
                        versão digitalizada com assinaturas dos membros da banca após a apresentação do
                        trabalho. Uma página digitalizada pode ser incluída no documento com o comando
                        abaixo, provido pelo pacote pdfpages:

                        \includepdf{folhadeaprovacao_final.pdf}

                        De todo modo, você pode utilizar o seguinte modelo de Folha de aprovação até a
                        aprovação final do trabalho:

                        \begin{folhadeaprovacao}

                        \begin{center}
                          {\ABNTEXchapterfont\large\imprimirautor}

                          \vspace*{\fill}\vspace*{\fill}
                          \begin{center}
                           \ABNTEXchapterfont\bfseries\Large\imprimirtitulo
                          \end{center}
                          \vspace*{\fill}

                          \hspace{.45\textwidth}
                          \begin{minipage}{.5\textwidth}
                              \imprimirpreambulo
                          \end{minipage}%
                          \vspace*{\fill}
                         \end{center}

                         Trabalho aprovado. \imprimirlocal, 24 de novembro de 2012:

                         \assinatura{\textbf{\imprimirorientador} \\ Orientador}
                         \assinatura{\textbf{Professor} \\ Convidado 1}
                         \assinatura{\textbf{Professor} \\ Convidado 2}
                         \assinatura{\textbf{Professor} \\ Convidado 3}
                         \assinatura{\textbf{Professor} \\ Convidado 4}

                         \begin{center}
                          \vspace*{0.5cm}
                          {\large\imprimirlocal}
                          \par
                          {\large\imprimirdata}
                          \vspace*{1cm}
                        \end{center}

                       \end{folhadeaprovacao}

        \assinatura    A macro \assinatura{htexto a ser impressoi} é um utilitário para impressão
                       de assinaturas da Folha de aprovação. Ela imprime o texto a ser impresso
                       centralizado abaixo de uma linha. A versão \assinatura* imprime a mesma
                       assinatura em uma box sem posição atribuída, o que é útil para impressão de
                       assinaturas lado a lado.
   \ABNTEXsignwidth    O comprimento da linha de assinatura é definido pela métrica \ABNTEXsignwidth.
                       O valor padrão é definido como: \setlength{\ABNTEXsignwidth}{8cm}.
\ABNTEXsignthickness   A largura da linha de assinatura é definida pela métrica \ABNTEXsignthickness.
                       O valor padrão é definido como: \setlength{\ABNTEXsignthickness}{1pt}.
    \ABNTEXsignskip    O espaçamento entre um comando \assinatura e outro é definido pela métrica
                       \ABNTEXsignskip. O valor padrão é definido como: \setlength{\ABNTEXsignskip}{0.7cm}.

                       5.6   Dedicatória (opcional)
        dedicatoria    A Dedicatória é um elemento opcional da ABNT NBR 14724:2011, seção 4.2.1.4,
   \dedicatorianame    que pode ser criada por meio do ambiente dedicatoria[hnome da dedicatóriai].

                      O valor do parâmetro opcional é utilizado como entrada no bookmark do PDF
                      (subseção 4.6) e como título da dedicatória, que é escrito como um título de capítulo
                      pré-textual, ou seja, não numerado e centralizado. Caso o parâmetro não seja
                      informado, o conteúdo de \dedicatorianame é utilizado apenas para entrada do
                      bookmark do PDF e a dedicatória é impressa sem título e sem indicador numérico,
                      conforme estabelece a seção 5.2.4 da norma em tela.
                      Um exemplo de uso do ambiente é:

                      \begin{dedicatoria}

                         \vspace*{\fill}
                         Este trabalho édedicado aos que acreditam...
                         \vspace*{\fill}

                      \end{dedicatoria}

                      5.7    Agradecimentos (opcional)
     agradecimentos   A seção Agradecimentos é um elemento opcional da ABNT NBR 14724:2011,
\agradecimentosname   4.2.1.5, que pode ser criada por meio do ambiente agradecimentos[hnome dos
                      agradecimentosi]. O valor do parâmetro opcional é utilizado como entrada no
                      bookmark do PDF (subseção 4.6). Caso o parâmetro não seja informado, o conteúdo
                      de \agradecimentosname é utilizado (subseção 4.9).
                      Um exemplo de uso do ambiente é:

                      \begin{agradecimentos}

                         Os agradecimentos...

                      \end{agradecimentos}

                      5.8    Epígrafe (opcional)
          epigrafe    A Epígrafe é um elemento opcional da ABNT NBR 14724:2011, seção 4.2.1.6, que
     \epigraphname    pode ser criada por meio do ambiente epigrafe[hnome da epígrafei]. O valor do
                      parâmetro opcional é utilizado como entrada no bookmark do PDF (subseção 4.6)
                      e como título da epígrafe, que é escrito como um título de capítulo pré-textual,
                      ou seja, não numerado e centralizado. Caso o parâmetro não seja informado, o
                      conteúdo de \epigraphname é utilizado apenas para entrada do bookmark do PDF
                      e a epígrafe é impressa sem título e sem indicador numérico, conforme estabelece a
                      seção 5.2.4 da norma em tela.
                      Um exemplo de uso do ambiente é:

                      \begin{epigrafe}

                    \vspace*{\fill}
                    \begin{flushright}
                       \textit{‘‘Não vos amoldeis às estruturas deste mundo, \\
                       mas transformai-vos pela renovação da mente, \\
                       a fim de distinguir qual éa vontade de Deus: \\
                       o que é bom, o que Lhe éagradável, o que éperfeito.\\
                       (Bíblia Sagrada, Romanos 12, 2)}
                     \end{flushright}

                  \end{epigrafe}

                  5.9    Resumos em língua vernácula e estrangeira (obrigató-
                         rio)
         resumo   Os resumos em língua vernácula e estrangeira são elementos obrigatórios da ABNT
         resumo   NBR 14724:2011, seção 4.2.1.7 e 4.2.1.8, e devem ser escritos conforme orientação
    \resumoname   da ABNT NBR 6028. Os elementos podem ser criados por meio do ambiente
                  resumo[hnome do resumoi]. O valor do parâmetro opcional é utilizado como
                  entrada no bookmark do PDF (subseção 4.6) e como título do resumo. Caso o
                  parâmetro não seja informado, o conteúdo de \resumoname é utilizado. O parâmetro
                  opcional é útil para criação de resumos em diversos idiomas estrangeiros.
                  Exemplos de uso do ambiente são:

                  % --- resumo em português ---
                  \begin{resumo}
                    Resumo em português
                    \vspace{\onelineskip}
                    \noindent
                    \textbf{Palavras-chave}: latex. abntex. editoração de texto.
                  \end{resumo}

                  % --- resumo em francês ---
                  \begin{resumo}[Résumé]
                   \begin{otherlanguage*}{french}
                      Il s’agit d’un résumé en français.
                      \vspace{\onelineskip}
                      \noindent
                      \textbf{Mots-clés}: latex. abntex. publication de textes.
                   \end{otherlanguage*}
                  \end{resumo}

resumoumacoluna   Em documentos que utilizam a opção twocolumn para produzir o texto em duas
    \resumoname   colunas — geralmente utilizado conjuntamente com article —, pode-se desejar
     \twocolumn   imprimir o resumo em uma única coluna e o restante do documento em duas. Nesse
                  caso, utilize o ambiente resumoumacoluna[hnome do resumoi].
                  Embora o parâmetro opcional nome do resumo esteja disponível, o ambiente
                  resumoumacolumna deve ser usado no contexto da macro \twocolumn, que por
                  sua vez não permite que nenhum ambiente ou macro possua outros parâmetros.
                  Desse modo, não é possível alterar o nome do resumo com o parâmetro opcional.

                    Felizmente, é possível fazê-lo redefinindo a macro \resumoname, conforme os
                    exemplos que seguem. A macro \twocolumn é usada para passar parâmetro à
                    opção twocolumn da classe abntex2.
                    Exemplos de uso do ambiente são:

                    \twocolumn[ % indica que inicia-se opção de twocolumn
                    % --- resumo em português ---
                    \begin{resumoumacoluna}
                      Resumo em português
                      \vspace{\onelineskip}
                      \noindent
                      \textbf{Palavras-chave}: latex. abntex. editoração de texto.
                    \end{resumoumacoluna}

                    % --- resumo em francês ---
                    \renewcommand{\resumoname}{Résumé}
                    \begin{resumoumacoluna}
                      \begin{otherlanguage*}{french}
                        Il s’agit d’un résumé en français.
                        \vspace{\onelineskip}
                        \noindent
                        \textbf{Mots-clés}: latex. abntex. publication de textes.
                      \end{otherlanguage*}
                    \end{resumoumacoluna}
                    ] fim de opção de twocolumn

  \absleftindent    As margens esquerda e direita, respectivamente, do ambiente resumo podem ser
 \absrightindent    customizadas com os comandos. Esta é a configuração padrão para documentos
                    que não sejam artigos:

                    \setlength\absleftindent{0cm}
                    \setlength\absrightindent{0cm}

\abstracttextfont   A fonte do ambiente resumo é automaticamente alterada para o caso de documentos
                    que não sejam artigos com:

                    \abstracttextfont{\normalfont\normalsize}

   \absparindent    A indentação e o espaçamento entre parágrafos do ambiente resumo podem ser
      \absparsep    alterados, respectivamente, com:

                    \setlength{\absparindent}{0pt}
                    \setlength{\absparsep}{18pt}

                    A indentação padrão utilizada no ambiente é 0pt. Já o separador de parágrafos
                    não é alterada pela classe abntex2.

                 Outras configurações do ambiente resumo estão disponíveis no manual do memoir
                 (WILSON; MADSEN, 2010, p. 69-71).
                 A subseção 4.8.1 aborda a macro otherlanguage*, responsável pela hifenização
                 em diferentes idiomas.

                 5.10    Lista de ilustrações (opcional)
\listoffigures   A Lista de ilustrações é um elemento opcional da ABNT NBR 14724:2011, seção
                 4.2.1.9, que pode ser criada por meio da macro padrão \listoffigures.
                 Nem a classe memoir, nem a classe abntex2 incluem automaticamente o capítulo
                 criado pela macro \listoffigures no bookmark do PDF (subseção 4.6).
                 O exemplo seguinte cria a Lista de ilustrações e já a adiciona ao bookmark:

                 \pdfbookmark[0]{\listfigurename}{lof}
                 \listoffigures*
                 \cleardoublepage

                 A seção 4.2.1.9 da norma ABNT NBR 14724:2011 recomenda que, quando necessá-
                 rio, seja produzido uma lista própria para cada tipo de ilustração, como desenhos,
                 esquemas, fluxogramas, fotografias, gráficos, mapas, organogramas, plantas, qua-
                 dros, retratos, e outros. Como essa necessidade é específica de cada trabalho, o
                 abnTEX2 não traz essa implementação automaticamente. Porém, diferentes tipos
                 de lista podem ser criadas por meio de macros do memoir. Para isso, consulte o
                 capítulo 9 do manual do memoir (WILSON; MADSEN, 2010).

                 5.11    Lista de tabelas (opcional)
\listoftables    A Lista de tabelas é um elemento opcional da ABNT NBR 14724:2011, seção
                 4.2.1.10, que pode ser criada por meio da macro padrão \listoftables.
                 Nem a classe memoir, nem a classe abntex2 incluem automaticamente o capítulo
                 criado pela macro \listoftables no bookmark do PDF (subseção 4.6).
                 O exemplo seguinte cria a Lista de tabelas e já a adiciona ao bookmark:

                 \pdfbookmark[0]{\listtablename}{lot}
                 \listoftables*
                 \cleardoublepage

                 5.12    Lista de abreviaturas e siglas (opcional)
       siglas    A Lista de abreviaturas e siglas é um elemento opcional da ABNT NBR 14724:2011,
                 seção 4.2.1.11 e pode ser criada com o ambiente siglas:

                   \begin{siglas}
                     \item[Fig.] Area of the $i^{th}$ component

                        \item[456] Isto éum número
                        \item[123] Isto éoutro número
                        \item[lauro cesar] este éo meu nome
                      \end{siglas}

\listadesiglasname   A macro \listadesiglasname contém o nome da lista de abreviaturas e siglas.
\printnomenclature   Opcionalmente, é possível usar o pacote nomencl30 , que oferece recursos adicionais
                     na composição de lista de siglas, símbolos e até glossários. Com esse pacote crie a
                     lista de abreviaturas e siglas seguindo o exemplo:
                     No preâmbulo:

                     \usepackage{nomencl}

                     \makenomenclature

                     No corpo do documento:

                     \nomenclature{Fig.}{Figura}
                     \nomenclature{$A_i$}{Area of the $i^{th}$ component}
                     \nomenclature{456}{Isto éum número}
                     \nomenclature{123}{Isto éoutro número}
                     \nomenclature{a}{primeira letra do alfabeto}
                     \nomenclature{lauro}{este émeu nome}

                     \renewcommand{\nomname}{\listadesiglasname}
                     \pdfbookmark[0]{\nomname}{las}
                     \printnomenclature
                     \cleardoublepage

                     Para usar o pacote nomencl, é necessário compilar o documento LATEX com makein-
                     dex:

                     makeindex ARQUIVO_PRINCIPAL.nlo -s nomencl.ist -o ARQUIVO_PRINCIPAL.nls

                     Após a compilação com makeindex, compile normalmente o documento com
                     pdflatex.
                     Geralmente os editores de documentos LATEX possuem formas de automatizar
                     essa compilação. Porém, caso você opte por usar o ambiente siglas, nenhuma
                     compilação adicional é necessária.

                     5.13    Lista de símbolos (opcional)
          simbolos   A lista de símbolos é um elemento opcional da ABNT NBR 14724:2011, seção
                     4.2.1.12 e pode ser criada com o ambiente simbolos:
                      30 <https://www.ctan.org/pkg/nomencl>

                         \begin{simbolos}
                           \item[$ \Gamma $] Letra grega Gama
                           \item[$ \Lambda $] Lambda
                           \item[$ \zeta $] Letra grega minúscula zeta
                           \item[$ \in $] Pertence
                         \end{simbolos}

  \listadesimbolosname   A macro \listadesimbolosname o nome da lista de símbolos.
                         Opcionalmente, use o pacote nomencl ou glossaries, que tanto podem construir a
                         Lista de símbolos, como Glossários. Consulte subseção 5.12 e a subseção 7.2 para
                         outras informações.

                         5.14    Sumário (obrigatório)
     \tableofcontents    O Sumário é um elemento obrigatório da ABNT NBR 14724:2011, seção 4.2.1.13,
                         que pode ser criada por meio da macro padrão \tableofcontents.
     \subsubsubsection   Conforme a referida norma, os itens do sumário são numerados até o quinto nível.
                         Por isso, adicionou-se ao abnTEX2 o comando \subsubsubsection{hdivisão de
                         quinto níveli}.
sumario=abnt-6027-2012   A classe abntex2 produz um sumário construído similar ao exemplo recomendado
   sumario=tradicional   pela ABNT NBR 6027:2012. O sumário customizado é ativado automaticamente,
                         mas pode ser controlado por meio da opção sumario= da declação \documentclass.
                         Desse modo, a opção
                         sumario=abnt-6027-2012 formata o sumário conforme as recomendações da
                              ABNT NBR 6027:2012. É a opção padrão, de modo que não é necessá-
                              rio informá-la;
                         sumario=tradicional usa o estilo tradicional de sumários do memoir. Recomenda-
                              se que se use esta opção no caso de customizações adicionais do sumário.
     \tableofcontents    Nem a classe memoir, nem a classe abntex2 incluem automaticamente o capítulo
         \pdfbookmark    criado pela macro \tableofcontents no bookmark do PDF. Caso deseje que o
                         título do capítulo seja incluído no bookmark (subseção 4.6), utilize o exemplo
                         abaixo:

                         \pdfbookmark[0]{\contentsname}{toc}
                         \tableofcontents*
                         \cleardoublepage

         \settocdepth    Você pode customizar o nível de divisões que o sumário pode listar com a macro
                         \settocdepth{hnome da subdivisãoi}, sendo nome da subdivisão um dos valores:
                         chapter, part, section, subsection, subsubsection.
                         A configuração padrão do abnTEX2 é \settocdepth{subsubsection}.
      \setsecnumdepth    Também é possível customizar se a numeração das divisões é exibida no sumário.
                         Para isso use \setsecnumdepth{hnome da subdivisãoi}, sendo nome da subdivisão
                         um dos mesmos valores utilizados em \settocdepth.

                   A configuração padrão do abnTEX2 é \setsecnumdepth{subsubsection}.
  \tocheadstart    É possível customizar a fonte das partes e dos capítulos no Sumário. Para isso,
                   redefina a macro \tocheadstart. O abnTEX2 a redefine por padrão para que
                   a fonte utilizada no Sumário seja a mesma defina para o capítulo, da seguinte
                   maneira:

                   \renewcommand{\tocheadstart}{\ABNTEXchapterfont}

\addcontentsline   O comando \addcontentsline{hsigla do sumarioi}{hnível da divisãoi}{htexto no
                   sumárioi} pode ser usado para incluir uma linha no Sumário. Use o comando, por
                   exemplo, após a criação de capítulo não numerado:

                   \chapter*{Introdução}
                   \addcontentsline{toc}{chapter}{Introdução}

                   É importante destacar que nenhum elemento pré-textual deve estar presente no
                   Sumário. Veja mais informações na seção 6.
                   Consulte a subseção 4.6 para obter informações sobre o bookmark, índice da
                   estrutura do documento no PDF.
  \addtocontents   O comando \addtocontents{toc}{\vspace{\cftbeforepartskip}} pode ser
                   usado para adicionar um espaço vertical no Sumário do mesmo tamanho do
                   espaço usado na separação de \part. Isso é útil, por exemplo, para indicar no
                   sumário que um novo capítulo não faz parte da parte anterior.
                   Consulte a subseção 4.11 para obter informações sobre a macro \phantompart.
     KeepFromToc   O ambiente KeepFromToc pode ser utilizada para que um divisão não seja in-
                   cluída no Sumário. Esse ambiente é equivalente à macro \ProximoForaDoSumario
                   utilizada pela versão anterior do abnTEX, e que não está mais presente nesta versão.
                   Use a macro como no exemplo:

                   \begin{KeepFromToc}
                      \chapter{Este capítulo não aparece no sumário}
                      \section{Nem esta seção}
                   \end{KeepFromToc}

                   O capítulo 9 do mamual do memoir detalha como o sumário pode ser customizado
                   (WILSON; MADSEN, 2010).

                   6    Elementos textuais
        \textual   O comando \textual identifica o início dos elementos textuais. As páginas desses
     \mainmatter   elementos são numeradas com algarismos arábicos no lado direito superior ou direi-
                   to/esquerdo superior caso a impressão frente e verso (opção twoside) seja acionada,
                   conforme estabelece a ABNT NBR 14724:2011. Geralmente a “Introdução” é o

            primeiro capítulo textual. A título de coerência, a macro \mainmatter, padrão do
            memoir, é reescrita para que tenha o mesmo comportamento que \textual. Por
            isso, fique livre em escolher qualquer das macros. Porém, o uso de uma delas é
            obrigatória, para que os cabeçalhos sejam montados corretamente.
            Segundo a ABNT NBR 14724:2011, seção 4.2.2, “o texto é composto de uma
            parte introdutória, que apresenta os objetivos do trabalho e as razões de sua
            elaboração; o desenvolvimento, que detalha a pesquisa ou estudo realizado; e
            uma parte conclusiva.” Os títulos dos capítulos textuais são à critério do autor
            e não há nenhuma normatização a respeito deles. No entanto, geralmente o
            capítulo “Introdução” e o capítulo “Conclusão” (ou “Considerações finais”) são,
            respectivamente, o primeiro e o último capítulo textual e normalmente não são
            numerados.
            É importante destacar que a norma em tela e a ABNT NBR 6024:2012 não são
            explícitas sobre a possibilidade de não numeração de capítulos textuais31 . Desse
            modo, sugere-se que se siga o modo de numeração desses capítulos utilizado pela
            instituição que você apresentará o trabalho.
\chapter*   Caso queira incluir capítulos sem numeração (como Introdução e Conclusão, por
            exemplo), utilize a macro \chapter*{hIntroduçãoi}. Porém, capítulos com * não
            são incluídos automaticamente no Sumário, nem no bookmark do PDF, nem alteram
            o cabeçalho das páginas.
            Consulte a subseção 5.14 para ver como incluir divisões com * ao sumário.
            Consulte a subseção 6.1 para obter outras informações sobre formatação de capítulos
            e, especialmente, consulte a subseção 6.1.2 para ver como alterar automaticamente
            os cabeçalhos das páginas com o comando \chapter*.
            Consulte a subseção 4.6 para ver como controlar o bookmark do PDF.
   \part    A macro \part{hnome da partei} pode ser utilizada para que uma página de
            divisão do trabalho seja incluída. A parte agrupa capítulos. Um exemplo é o uso
            do trabalho dividido em três partes:

            \part{Preparação da Pesquisa}
               (...)
               \chapter{Metodologia}
               (...)
            \part{Referenciais teóricos}
               (...)
               \chapter{O trabalho de Charles Darwin}
               (...)
            \part{Resultados}
               (...)

               31 Embora a seção 5.2.3 da ABNT NBR 14724:2011 seja clara a respeito dos capítulos pré e

            pós-textuais estabelecidos por ela: “Os títulos, sem indicativo numérico — errata, agradecimentos,
            lista de ilustrações, lista de abreviaturas e siglas, lista de símbolos, resumos, sumário, referências,
            glossário, apêndice(s), anexo(s) e índice(s) —- devem ser centralizados”.

                              6.1     Formatação dos títulos: partes, capítulos, seções, sub-
                                      seções e subsubseções
        \ABNTEXchapterfont    O memoir possui uma vasta lista de opções de estilos de capítulos (ver subse-
    \ABNTEXchapterfontsize    ção 6.1.1). A classe abntex2 adiciona a essa lista um estilo chamado abnt, que
                              atende aos requisitos na ABNT NBR 14724:2011 e da ABNT NBR 6024:2012. O
                              estilo abnt é carregado automaticamente e possui duas configurações adicionais:
                              \ABNTEXchapterfont é a fonte utilizada nos capítulos e \ABNTEXchapterfontsize
                              é o tamanho da fonte.
                              Por padrão, uma versão sem serifas da fonte corrente do documento é utilizada
                              para os títulos das divisões. Você pode customizar a fonte dos títulos dos capítulos
                              alterando os comandos como no exemplo a seguir, para que seja utilizada a fonte
                              Computer Modern com tamanho maior do que o utilizado por padrão:

                              \renewcommand{\ABNTEXchapterfont}{\fontfamily{cmr}\fontseries{b}\selectfont}
                              \renewcommand{\ABNTEXchapterfontsize}{\HUGE}

            \ABNTEXpartfont
        \ABNTEXpartfontsize
                             As fontes e o tamanho das fontes obtidas com as divisões \part{hnome da partei},
         \ABNTEXsectionfont
                             \chapter{hnome do capítuloi}, \section{hnome da seçãoi}, \subsection{hnome
     \ABNTEXsectionfontsize
                             da subseçãoi} e \subsubsection{hnome da subsubseçãoi} são definidas por pa-
      \ABNTEXsubsectionfont
                             drão, respectivamente, conforme a Table 2. Você pode alterá-las com o comando
  \ABNTEXsubsectionfontsize
                             \renewcommand.
   \ABNTEXsubsubsectionfont
\ABNTEXsubsubsectionfontsize
\ABNTEXsubsubsubsectionfont            Tabela 2: Macros de formatação de fonte de divisões do texto
\ABNTEXsubsubsubsectionfontsize      Macro                                  Valor padrão
                                      \ABNTEXchapterfont                       \sffamily32
                                      \ABNTEXchapterfontsize                   \Huge
                                      \ABNTEXpartfont                          \ABNTEXchapterfont
                                      \ABNTEXpartfontsize                      \ABNTEXchapterfontsize
                                      \ABNTEXsectionfont                       \ABNTEXchapterfont
                                      \ABNTEXsectionfontsize                   \Large
                                      \ABNTEXsubsectionfont                    \ABNTEXsectionfont
                                      \ABNTEXsubsectionfontsize                \large
                                      \ABNTEXsubsubsectionfont                 \ABNTEXsubsectionfont
                                      \ABNTEXsubsubsectionfontsize             \normalsize
                                      \ABNTEXsubsubsubsectionfont              \ABNTEXsubsectionfont
                                      \ABNTEXsubsubsubsectionfontsize          \normalsize

                              6.1.1   Estilos adicionais de capítulos
              \chapterstyle   O estilo de capítulo abnt provido pela classe abnTEX2 pode ser substituído por
                              outro estilo já fornecido pelo memoir ou mesmo por outro criado por você. Isso é
                              útil especialmente se estiver interessado em publicar seu trabalho como livro ou
                              não se importar em não seguir o padrão normativo. Para isso, utilize o comando:

            \chapterstyle{nome_do_estilo}

            Experimente lyhne ou dash. Você encontra alguns estilos no manual do
            memoir e outros neste documento: <https://www.ctan.org/tex-archive/info/
            MemoirChapStyles>. Ambos mostram como criar um novo estilo.

            6.1.2    Cabeçalhos de capítulos com *
\chapter*   Conforme descrito na subseção 4.6, os capítulos criados com \chapter* não alteram
            automaticamente o cabeçalho da página. Ou seja, o cabeçalho de um capítulo
            iniciado com o comando \chapter* é o mesmo do capítulo anterior, se houver.
            Para alterar esse comportamento, informe o parâmetro opcional: \chapter*[hnome
            do capítulo do cabeçalhoi]{hnome do capítulo na páginai}.
            Para mais detalhes, consulte o Wilson e Madsen (2010, p. 73).

            6.1.3    Espaçamento entre os capítulos e o texto
            Segundo a ABNT (2011, seção 5.2.2), os títulos das seções primárias (os capítulos)
            “devem começar em página ímpar (anverso)33 , na parte superior da mancha gráfica
            e ser separados do texto que os sucede por um espaço entre as linhas de 1,5”.
            Porém, propositalmente os modelos do abnTEXnão atendem a essa regra, uma
            vez que utiliza-se tamanhos diferentes de fontes para capítulos e, nesse caso, um
            espaçamento de 1,5 entre o capítulo e o início do texto não ficaria esteticamente
            elegante. Observe que a norma em questão nem as demais normas estabelece
            um tamanho de fonte para as seções, o que torna livre a opção de um tamanho
            diferente (e maior) de fonte para os capítulos do que o tamanho da fonte do corpo
            do texto.
            De toda forma, caso você queira seguir estritamente o requisito da norma referente
            ao espaçamento entre o capítulo e o início do texto, faça o seguinte.
            Utilize no preâmbulo do documento:

            \setlength\afterchapskip{\lineskip}

            Imediatamente após a declaração de um capítulo de apêndice ou de anexo:

            \chapter{Título de um anexo ou apêndice}
            \setlength{\afterchapskip}{-\baselineskip}

            O texto do apêndice ou do anexo...

            Caso o título do apêndice ou do anexo tenha mais de duas linhas, use o comando
            abaixo para ajustar um eventual problema de espaçamento:
              33 Esse requisito é atendido ao usar a opção openright.

                      \chapter{Título de um anexo ou apêndice muito longo, com mais de duas
                          linhas, que pode
                      ocasionar um problema de espaçamento}
                      \phantom{x}

                      O texto do apêndice ou do anexo...

                      6.2    Citações diretas com mais de três linhas
           citacao    A ABNT NBR 10520:2002, seção 5.3, descreve que citações diretas com mais de
                      três linhas devem ser destacadas com recuo de 4 cm da margem esquerda, com
                      letra menor que a do texto utilizado e sem as aspas. Para inserir citações longas,
                      utilize o ambiente citacao, conforme o exemplo:

                      \begin{citacao}
                      As citações diretas, no texto, com mais de três linhas, devem ser
                      destacadas com recuo de 4 cm da margem esquerda, com letra menor que
                      a do texto utilizado e sem as aspas. No caso de documentos datilografados,
                      deve-se observar apenas o recuo \cite[5.3]{NBR10520:2002}
                      \end{citacao}

                      O ambiente citacao[hlanguagei] pode receber como parâmetro opcional um nome
                      de idioma previamente carregado nas opções da classe (subseção 4.8.1). Nesse caso,
                      o texto da citação é automaticamente escrito em itálico e a hifenização é ajustada
                      para o idioma selecionado na opção do ambiente, conforme o exemplo:

                      \begin{citacao}[english]
                      Text in English language in italic with correct hyphenation.
                      \end{citacao}

                      A subseção 4.8.1 descreve o uso de diferentes idiomas no texto.
                      O tamanho da fonte utilizada no ambiente citacao é determinada pela macro
                      \ABNTEXfontereduzida, descrita na seção 4.
\ABNTEXcitacaorecuo   O recuo utilizado pelo ambiente citacao é definido pela métrica
                      \ABNTEXcitacaorecuo, que pode ser alterado com:

                      \setlength{\ABNTEXcitacaorecuo}{1.8cm}

                      Quando um documento é produzido com a opção twocolumn, a classe abntex2
                      automaticamente altera o recuo padrão definido pela ABNT NBR 10520:2002 para
                      1.8cm.

             6.3    Alíneas e Subalíneas
             A ABNT NBR 6024:2012, seção 4.2, descreve o uso das alíneas, que podem ser
             compreendias como subdivisões não nomeadas de uma seção.
             As alíneas são numeradas com letras minúsculas do alfabeto com recuo em relação
             à margem esquerda do documento. A norma prescreve que o texto que antecede
             as alíneas deve finalizar com dois pontos (:); as alíneas devem iniciar com letra
             minúscula e serem finalizadas com ponto e vírgula (;), exceto a última alínea,
             que deve ser finalizada com ponto final, e exceto as alíneas que precederem uma
             subalínea, caso em que devem ser finalizadas com dois pontos (:); a segunda e as
             seguintes linhas do texto da alínea começa sob a primeira letra do texto da própria
             alínea.
             Os ambientes descritos nesta seção são criados com o pacote enumitem. Consulte a
             documentação do pacote em Bezos (2011) para obter detalhes e opções adicionais
             de configuração.
  alineas    A classe abntex2 fornece o ambiente alineas, que cria listas conforme o padrão
             estipulado pela norma. Veja o exemplo:

             \begin{alineas}
               \item linha 1;
               \item linha 2;
               \item linha 3.
             \end{alineas}

subalineas   As alíneas podem ser aninhadas. Nesse caso, a numeração é substituída por
   incisos   um travessão. Você pode criar uma subalínea de três formas diferentes, todas
             equivalentes entre si: com outro ambiente alineas, com subalineas ou ainda
             com o ambiente incisos:

             \begin{alineas}

               \item linha 1:
               \begin{alineas}
                 \item subalinea 1;
                 \item subalinea 2;
               \end{alineas}

               \item linha 2:
               \begin{subalineas}
                 \item subalinea 1;
                 \item subalinea 2;
               \end{subalineas}

               \item linha 3:
               \begin{incisos}
                 \item subalinea 1;
                 \item subalinea 2;
               \end{incisos}

                        \item linha 4.
                      \end{alineas}

                      6.4    Rótulos e legendas
           \caption   Rótulos e legendas de ilustrações, tabelas e qualquer outro ambiente do tipo
            \legend   listing podem ser definidos pelos comandos \caption{hrotuloi} e \legend{hlegendai},
                      respectivamente.
                      Conforme a ABNT NBR 14724:2011, seção 5.8, o rótulo é atribuído acima do
                      elemento e a legenda abaixo, conforme no exemplo:

                      \begin{figure}[htb]
                        \caption{\label{fig_circulo}A delimitação do espaço}
                        \begin{center}
                          \includegraphics[scale=0.75]{myfig.pdf}
                        \end{center}
                        \legend{Fonte: os autores}
                      \end{figure}

\ABNTEXcaptiondelim   O comando \ABNTEXcaptiondelim representa a definição do separador padrão de
                      rótulos. O separador padrão é o travessão (–), conforme estabelecido pela norma
                      ABNT NBR 14724:2011. Você pode mudar o separador padrão seguindo este
                      exemplo:

                      \renewcommand{\ABNTEXcaptiondelim}{~\textendash~}
                      \captiondelim{\ABNTEXcaptiondelim}

  \includegraphics    A macro \includegraphics pode ser utilizada para inclusão de imagens.
                      Recomenda-se que imagens vetoriais, como imagens em PDF, sejam preferidas em
                      oposição a imagens baseadas em mapas de bits, uma vez que desse forma não há
                      perda de qualidade nas imagens. Porém, formatos como PNG, BMP, JPG e outros
                      são aceitos pelo LATEX.

                      6.5    Tabelas em conformidade com padrões do IBGE
           \IBGEtab   Conforme a ABNT NBR 14724:2011, seção 5.9, as tabelas “devem ser citadas no
           \ibgetab   texto, inseridas o mais próximo possível do trecho a que se referem e padronizadas
                      conforme o Instituto Brasileiro de Geografia e Estatística (IBGE)”. Para aten-
                      der a esse requisito, a classe abntex2 oferece a macro \IBGEtab{hNome e rótulo
                      da tabelai}{hConteúdo da tabelai}{hConteúdo da legendai}, criada para atender
                      requisitos descritos por IBGE (1993).
                      Nome e rótulo devem ser criados com \caption{hNome a ser impresso acima
                      do objetoi} e \label{hNome do rótuloi}, respectivamente. O rótulo é usado por
                      \autoref{hNome do rótuloi} para referenciar o elemento criado. O conteúdo da
                      tabela pode ser criado com os ambientes tabular, table, ou mesmo ser uma

                   figura importada no ambiente figure. O desenvolvimento do \IBGEtab prevê
                   o uso do longtable, mas não funciona com ele ainda. O conteúdo da legenda
                   pode ser criado com a macro \legend e \namedlegend, padrões do memoir, ou,
                   preferencialmente, com \fonte e \nota.
         \fonte    A macro \fonte[hRótulo da fonte. Padrão: “Fonte”i]{hDescrição da fonte da
                   tabela ou figurai} imprime o conteúdo do argumento antecedido da expressão
                   “Fonte: ”, ou do conteúdo do parâmetro opcional, alinhado conforme requisitos
                   do IBGE. A macro \fonte pode ser usada no interior de figuras ou de outros
                   ambientes.
           \nota   A macro \nota[hRótulo da nota. Padrão: “Nota”i]{hNota ou outra descriçãoi}
                   imprime o conteúdo do argumento antecedido da expressão “Nota: ”, ou do
                   conteúdo do parâmetro opcional, alinhado conforme requisitos do IBGE. A macro
                   \nota pode ser usada no interior de figuras ou de outros ambientes.
\IBGEtabfontsize   O conteúdo do material tabulado usado na macro \IBGEtab podem ser glo-
                   balmente ou localmente ajustado através da macro \IBGEtabfontsize. A
                   norma diz que o conteúdo de tabelas deve ser em fonte reduzida, assim, por
                   padrão, a classe faz \IBGEtabfontsize como \ABNTEXfontereduzida. Para
                   uma adequação às normas da instituição este tamanho pode ser modificado via
                   \renewcommand{\IBGEtabfontsize}{htamanho de fonte desejadai}.
                   Desse modo, um exemplo completo de uso das macros \IBGEtab, \fonte e \nota
                   é:

                   \begin{table}[htb]
                   \IBGEtab{%
                     \caption{Um Exemplo de tabela alinhada que pode ser longa ou curta,
                     conforme padrão IBGE.}%
                     \label{tabela-ibge}
                   }{%
                     \begin{tabular}{ccc}
                     \toprule
                      Nome & Nascimento & Documento \\
                     \midrule \midrule
                      Maria da Silva & 11/11/1111 & 111.111.111-11 \\
                     \bottomrule
                   \end{tabular}%
                   }{%
                     \fonte{Produzido pelos autores}%
                     \nota{Esta éuma nota, que diz que os dados são baseados na
                     regressão linear.}%
                     \nota[Anotações]{Uma anotação adicional, seguida de várias outras.}%
                   }
                   \end{table}

                   6.6   Quadros no modelo de trabalho acadêmico
        \quadro    A partir da versão XXX, o modelo de trabalho acadêmico dispobibilizado no
                   abnTEX trás pré-configurado a impressão da lista de quadros no pretextual e
                   disponibiliza o ambiente quadro para sua criação, veja um exemplo:

                \begin{quadro}[htb]
                \caption{\label{quadro_exemplo}Exemplo de quadro}
                \begin{tabular}{|c|c|c|c|}
                  \hline
                  \textbf{Pessoa} & \textbf{Idade} & \textbf{Peso} & \textbf{Altura} \\
                      \hline
                  Marcos & 26 & 68 & 178      \\ \hline
                  Ivone & 22   & 57 & 162     \\ \hline
                  ...    & ... & ... & ...    \\ \hline
                  Sueli & 40   & 65 & 153     \\ \hline
                \end{tabular}
                \fonte{Autor.}
                \end{quadro}

                Caso esteja utilizando um modelo anterior deseja incluir um quadro, você precisará
                configurar o seu modelo apropriadamente34 .

                7     Elementos pós-textuais
 \postextual    O comando \postextual identifica o início dos elementos pós-textuais. Na prática
 \backmatter    o único comportamento específico é a execução da macro \phantompart (subse-
                ção 4.11). Dessa forma, caso deseje atribuir algum comportamento diferenciado aos
                elementos pós-textuais, faça-o redefinindo a macro, mas não se esqueça de adicionar
                o comando \phantompart. A título de coerência, a macro \backmatter, padrão
                do memoir, é reescrita para que tenha o mesmo comportamento que \postextual.

                7.1    Referências (obrigatório)
\bibliography   A classe abntex2 é responsável pela estruturação e o aspecto geral dos documentos.
                Mais precisamente, ela é focada em atender os requisitos apresentados pela norma
                ABNT NBR 10719:2015, ABNT NBR 14724:2011, ABNT NBR 15287:2011 e
                normas correlatas. As referências bibliográficas são normatizadas pela norma
                ABNT NBR 10520:2002 e ABNT NBR 6023:2002. Os requisitos impostos por estas
                normas são atendidos pelo pacote abntex2cite.
                Esta seção apresenta apenas uma introdução ao uso de referências bibliográficas
                com abnTEX2. Para um detalhamento completo do tema, consulte os manuais
                Araujo (2015f) e Araujo (2015g).
                Para utilizar o padrão de bibliografias brasileiro implementado pelo pacote abn-
                tex2cite, declare no preâmbulo do documento:

                \usepackage[alf]{abntex2cite} % Citações padrão ABNT

                A opção alf indica que as referências serão alfanuméricas, no padrão autor-ano.
                Ela se opõe à opção num, que indica que as referências serão numéricas. Consulte
                o manual do pacote abntex2cite para informações detalhadas.
                 34 Para     configuração     consulte        <https://github.com/abntex/abntex2/wiki/
                HowToCriarNovoAmbienteListing>

          Para indicar o local de impressão da bibliografia, utilize:

          \bibliography{arquivo-de-referencias-bib}

          Você pode usar tanto a classe abntex2 quanto o pacote de citações abntex2cite
          de forma independente. Usar apenas o pacote de citações é útil quando se está
          escrevendo um documento baseado em outra classe fornecida. Uma instituição de
          ensino, por exemplo, pode se utilizar deste recurso caso se deseje manter apenas
          o padrão de citações. Por outro lado, também se pode optar por utilizar as
          customizações da classe abntex2 com outro padrão de referências bibliográficas.
backref   O abntex2cite é compatível com o pacote backref 35 , que permite que a bibliografia
          indique quantas vezes e em quais páginas a citação ocorreu. Para isso, adicione ao
          preâmbulo:

          \usepackage[brazilian,hyperpageref]{backref}

          Ainda no preâmbulo, você pode configurar como o pacote backref deverá imprimir
          as referências:

          % Configurações do pacote backref
          % Usado sem a opção hyperpageref de backref
          \renewcommand{\backrefpagesname}{Citado na(s) página(s):~}

          % Texto padrão antes do número das páginas
          \renewcommand{\backref}{}

          % Define os textos da citação
          \renewcommand*{\backrefalt}[4]{
              \ifcase #1 %
               Nenhuma citação no texto.%
              \or
               Citado na página #2.%
              \else
               Citado #1 vezes nas páginas #2.%
              \fi}%

          7.2    Glossário (opcional)
          O abnTEX2 não traz uma implementação própria para o Glossário, elemento
          opcional estabelecido pela ABNT NBR 14724:2011. Um dos motivos da não
          inclusão desse recurso é a existência de diversos pacotes que o fazem, cada um com
          uma característica diferente.
          Como sugestão, consulte o pacote glossaries36 , que tanto pode construir Glossários
          como a Lista de símbolos (subseção 5.13).
           35 <http://www.ctan.org/pkg/backref>
           36 <https://www.ctan.org/pkg/glossaries>

                 O portal LATEXCommunity (<http://www.latex-community.org>) possui um guia
                 de uso do pacote glossaries37 e também um excelente artigo38 que mostra como
                 criar um pacote próprio de gerenciamento de glossários que não necessita de
                 nenhum utilitário externo, uma vez que glossaries requer os aplicativos makeindex e
                 makeglossaries, este último escrito e dependente do Perl39 . Já o livro “LaTeX”40 da
                 WikiBooks possui um capítulo dedicado à construção de glossários com glossaries.
                 Como exemplo de uso do pacote glossaries, a partir da versão 1.6 o abnTEX2 inclui
                 o documento “Exemplo de uso de glossário com abnTeX2” (ARAUJO, 2015a), que
                 pode ser usado como referência para criação desse elemento pós textual.

                 7.3    Apêndices (opcional)
    \apendices   O início dos apêndices, elementos opcionais da ABNT NBR 14724:2011, seção
  apendicesenv   4.2.3.3, deve ser marcado com a macro \apendices, ou os apêndices devem estar
                 contidos no ambiente apendicesenv. Os apêndices devem preceder os anexos, caso
                 esses existam.
\apendicename    Os apêndices devem ser iniciados com a macro \chapter{hnome do apêndicei},
                 que imprime o nome do apêndice precedido do conteúdo da macro \apendicename,
                 cujo conteúdo padrão é AP\^ENDICE.
\apendicesname   No contexto dos apêndices, a macro \partpage e seu sinônimo \partapendices
     \partpage   imprimem o conteúdo da macro \apendicesname como se fosse uma divisão de
\partapendices   partes obtida com \part não numerada. A variante \partapendices* não inclui
                 divisão no Sumário nem no bookmark do PDF.

                 7.4    Anexos (opcional)
       \anexos   O início dos anexos, elementos opcionais da ABNT NBR 14724:2011, seção 4.2.3.4,
     anexosenv   deve ser marcado com a macro \anexos, ou os anexos devem estar contidos no
                 ambiente anexosenv. Os anexos devem vir dispostos após os apêndices, caso esses
                 existam.
   \anexoname    Os anexos devem ser iniciados com a macro \chapter{hnome do anexoi}, que
                 imprime o nome do anexo precedido do conteúdo da macro \anexoname, cujo
                 conteúdo padrão é ANEXO.
  \anexosname    No contexto dos anexos, a macro \partpage e seu sinônimo \partanexos imprimem
    \partpage    o conteúdo da macro \anexosname como se fosse uma divisão de partes obtida com
  \partanexos    \part não numerada. A variante \partanexos* não inclui a divisão no Sumário
                 nem no bookmark do PDF.

                 7.5    Índice (opcional)
   \printindex   O índice, elemento opcional da ABNT NBR 14724:2011, deve ser elabora con-
        \index   forme a ABNT NBR 6034 e pode ser produzido por meio da macro \printindex,
                   37 <http://www.latex-community.org/know-how/latex/55-latex-general/

                 263-glossaries-nomenclature-lists-of-symbols-and-acronyms>q
                   38 <http://www.latex-community.org/know-how/456-glossary-without-makeindex>
                   39 <http://www.perl.org/>
                   40 <http://en.wikibooks.org/wiki/LaTeX/Glossary>

que imprime as páginas nas quais as macros \index{hpalavra a ser indexadai}
apareceram.
Para que as macros \printindex e \index funcionem, é preciso utilizar o compi-
lador MakeIndex41 .

8     Mais informações
Para mais informações, consulte o site do projeto em <http://www.abntex.net.br/
>. Há dezenas de páginas de wiki que podem esclarecer suas dúvidas.
Faça parte também do fórum de discussão do abnTEX2 em <http://groups.google.
com/group/abntex2>.

Referências
ARAUJO, L. C. Exemplo de uso de glossário com abnTeX2. [S.l.], 2015. Disponível
em: <http://www.abntex.net.br/>.
ARAUJO, L. C. Modelo Canônico de Artigo científico com abnTeX2. [S.l.], 2015.
Disponível em: <http://www.abntex.net.br/>.
ARAUJO, L. C. Modelo Canônico de Projeto de pesquisa com abnTeX2. [S.l.],
2015. Disponível em: <http://www.abntex.net.br/>.
ARAUJO, L. C. Modelo Canônico de Relatório Técnico e/ou Científico com
abnTeX2. [S.l.], 2015. Disponível em: <http://www.abntex.net.br/>.
ARAUJO, L. C. Modelo Canônico de Trabalho Acadêmico com abnTeX2. [S.l.],
2015. Disponível em: <http://www.abntex.net.br/>.
ARAUJO, L. C. O pacote abntex2cite: Estilos bibliográficos compatíveis com a
ABNT NBR 6023. [S.l.], 2015. Disponível em: <http://www.abntex.net.br/>.
ARAUJO, L. C. O pacote abntex2cite: tópicos específicos da ABNT NBR
10520:2002 e o estilo bibliográfico alfabético (sistema autor-data. [S.l.], 2015.
Disponível em: <http://www.abntex.net.br/>.
ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. ABNT NBR
14724:2011 : Informação e documentação — trabalhos acadêmicos — apresentação.
Rio de Janeiro, 2011. 15 p.
ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. ABNT NBR 6024:
2012 : Informação e documentação - numeração progressiva das seções de um
documento - apresentação. Rio de Janeiro, 2012. 4 p.
BEZOS, J. Customizing lists with the enumitem package. [S.l.], 2011. Disponível em:
<http://linorg.usp.br/CTAN/macros/latex/contrib/enumitem/enumitem.pdf>.
Acesso em: 22.1.2013.
BRAAMS, J. Babel, a multilingual package for use with LATEX’s standard
document classes. [S.l.], 2008. Disponível em: <http://mirrors.ctan.org/info/
babel/babel.pdf>. Acesso em: 17.2.2013.
  41 <https://www.ctan.org/pkg/makeindex>

CHEREM, Y. Modelo de Livro produzido com abnTeX2. [S.l.], 2015. Disponível
em: <http://www.abntex.net.br/>.
IBGE. Normas de apresentação tabular. 3. ed. Rio de Janeiro: Centro de
Documentação e Disseminação de Informações. Fundação Intituto Brasileiro de
Geografia e Estatística, 1993. Acesso em: 21 ago 2013.
OBERDIEK, H. The bookmark package. [S.l.], 2011. Disponível em:
<https://www.ctan.org/pkg/bookmark>. Acesso em: 27.2.2015.
WILSON, P.; MADSEN, L. The Memoir Class for Configurable
Typesetting - User Guide. Normandy Park, WA, 2010. Disponível em:
<http://mirrors.ctan.org/macros/latex/contrib/memoir/memman.pdf>. Acesso
em: 19.12.2012.
