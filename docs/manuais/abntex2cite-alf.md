# O pacote abntex2cite: estilo alfabético (manual)

> Texto extraído de `abntex2/doc/abntex2cite-alf.pdf` (abnTeX2 v-1.9.7) com
> `pdftotext -layout`; numeração de página removida. Preserva a quebra de
> linha do PDF, então palavras podem aparecer hifenizadas no fim da linha.
> Para regenerar: `python3 scripts/pdf_to_md.py`.

O pacote abntex2cite:
       Tópicos específicos da ABNT NBR 10520:2002 e o
       estilo bibliográfico alfabético (sistema autor-data)

                               Lauro César Araujo
                          <http://www.abntex.net.br/>

                         24 de novembro de 2018, v-1.9.7

                                        Resumo
        Este manual é parte integrante da suíte abnTEX2 e aborda tópicos específicos
     da ABNT NBR 10520:2002 e o estilo bibliográfico alfabético (sistema autor-data).

Sumário
1 Escopo                                                                                 2

2 Créditos aos autores originais                                                         2

3 Considerações iniciais                                                                2
  3.1 Prefira o sistema numérico, se possível . . . . . . . . . . . . . . . . . . .     2
  3.2 Cuidado: normas nebulosas! . . . . . . . . . . . . . . . . . . . . . . . . .      3

4 Como usar a citação alfabética (sistema autor-data)                                    3
  4.1 Como chamar os pacotes e estilos . . . . . . . . . . . . . . . . . . . . . .       3
  4.2 Como usar a citação no sistema autor-data . . . . . . . . . . . . . . . .          3
      4.2.1 Referências explícitas (citeonline) . . . . . . . . . . . . . . . .          4
      4.2.2 Referências a organization . . . . . . . . . . . . . . . . . . . . .         5
      4.2.3 Citações com autoria dada pelo título . . . . . . . . . . . . . . .          5
      4.2.4 Referências implícitas (cite) . . . . . . . . . . . . . . . . . . . .        6
      4.2.5 Referências citadas por outra referência (apud) . . . . . . . . . .          6
      4.2.6 Citações em notas de rodapé . . . . . . . . . . . . . . . . . . . .          7
      4.2.7 Uso de idem, ibidem, opus citatum e outros . . . . . . . . . . . .           7
      4.2.8 Referências múltiplas . . . . . . . . . . . . . . . . . . . . . . . . .      8
      4.2.9 Múltiplas referências com mesmo autor-data . . . . . . . . . . .             8
      4.2.10 Mais de três autores e o uso de et al. . . . . . . . . . . . . . . . .      9
      4.2.11 Citações de partes da referência . . . . . . . . . . . . . . . . . . .      9

5 Formações do estilo alfabético                                                        10

6 Alteração do estilo alfabético citeoption                                             10

7 Problemas com a ‘norma’ 10520                                                         11
  7.1 Referências múltiplas . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   11

    7.2    et al. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   12

Referências                                                                                     12

Lista de Tabelas
    1      Opções de alteração dos estilos bibliográficos: composição . . . . . . . .           11

1       Escopo
O objetivo deste manual é abordar tópicos específicos da ABNT NBR 10520:2002 e o
estilo bibliográfico alfabético (sistema autor-data).
Este documento é parte integrante da suíte abnTEX2 e é um complemento do documento
Araujo (2015b).
Para referências à classe abntex2, consulte Araujo (2015a).

2       Créditos aos autores originais
Este documento é derivado do documento Estilo bibtex compatível com a ‘norma’ 6023
da ABNT: Questões específicas da ‘norma’ 10520, versão 1.29, escrito por G. Weber
e atualizado por Miguel V. S. Frasson em 23 de março de 2004 no âmbito do projeto
abnTEX hospedado originalmente em <http://codigolivre.org.br/projects/abntex> 1 .
A equipe do projeto abnTEX2, observando a LaTeX Project Public License, registra que
os créditos deste manual são dos autores originais.

3       Considerações iniciais
3.1       Prefira o sistema numérico, se possível
Se você está usando LATEX assumimos que está usando um computador. Nesse caso, a
citação no esquema autor-data é uma coisa tão arcaica e desnecessária quanto uma régua-
de-cálculo. A leitura de um texto com chamadas no sistema autor-data é desajeitada,
especialmente quando muitas referências são chamadas de uma só vez. Você não tem
absolutamente nenhum motivo para usar o sistema autor-data já que a ABNT “autorizou”
o uso do sistema citação numérico por um cochilo qualquer.
Por outro lado, há aqueles que se dão ao trabalho de te dar trabalho, de seguir regras
esdrúxulas na hora de escrever teses. Estes podem estar exigindo que você use o arcaico
sistema autor-data. Também pode acontecer que os examinadores da banca, seja por
que não leram a sua tese ou porque não entenderam nada realmente (ou ambos), acabem
se enroscando em picuinhas.
Aí mandam você colocar todas as suas referências numéricas em formato autor-data.
Comentamos isso porque tudo isso já aconteceu e continua acontecendo com outras
pessoas. Portanto, esteja preparado.
  1 O documento original pode ser lido em <https://github.com/abntex/abntex2-old-binary/blob/

master/abntex1-manuais/abnt-bibtex-alf-doc.pdf>

                              Antes de começar a escrever recomendamos verificar quais são as regras de fato da sua
                              universidade ou instituição.

                              3.2      Cuidado: normas nebulosas!
                              Nós elaboramos os estilos debruçados diretamente sobre os originais da ABNT e as
                              seguimos escrupulosamente. Mas não se iluda! O que a sua coordenação de pós-
                              graduação, ou orientador, ou chefe etc., entendem por ‘normas ABNT’ pode não ter
                              qualquer vínculo com a realidade. Por isso não garantimos que ao usar os estilos do
                              abnTEX você esteja em conformidade com as normas da sua instituição ou empresa.
                              Um exemplo clássico é o sistema de chamada numérico2 . Embora todas as ‘normas’
                              da ABNT (ABNT, 1988; ABNT, 2000; ABNT, 2002b, 2002b; ABNT, 2001; ABNT,
                              2002a) ‘autorizem’ seu uso, a maioria das instituições, orientadores, membros de banca,
                              revisores de artigo. . . dirão que isso não é ABNT. Acredite se quiser.

                              4      Como usar a citação alfabética (sistema autor-
                                     data)
                              4.1      Como chamar os pacotes e estilos
\usepackage[alf]abntex2cite   Para usar o estilo de citação alfabético (seção 9.2 em 6023/2000 (ABNT, 2000)) utilize
                              no preâmbulo:

                              \usepackage[alf]{abntex2cite}

        \bibliographystyle    Você não precisa selecionar o comando \bibliographystyle, porque isso é realizado
                              automaticamente. Do mesmo modo, a base bibliográfica abntex2-options.bib também
                              estará automaticamente incluída.
                              Se você quiser usar apenas o estilo bibliográfico, e não utilizar o esquema de citações,
                              selecione com o comando:

                              \bibliographystyle{abntex2-alf}

                              mas esteja avisado que nesse caso as chamadas no texto não estarão em conformidade
                              com a ‘norma’.
                              Dessa forma, as citações no texto não estarão em conformidade com as normas brasileiras,
                              porém a bibliografia será formatada corretamente.

                              4.2      Como usar a citação no sistema autor-data
                              Este sistema de citação é descrito em ABNT (2002a). Note que essa ‘norma’ entrou em
                              vigor em agosto de 2002, apenas um ano depois da ABNT (2001).
                              Esse sistema aceita basicamente duas formatações para a citação, dependendo da
                              maneira como ocorre a citação no texto.
                                  2 Descrito em Araujo (2015b).

              4.2.1   Referências explícitas (citeonline)
\citeonline   É o caso em que você menciona explicitamente o autor da referência na sentença. Algo
              como “Fulano (1900)". Para isso use o comando \citeonline.
              Exemplos apresentadas em ABNT (2001):

                                                              A ironia será assim uma . . . proposta
              A ironia será assim uma \ldots\ proposta
                                                              por Authler-Reiriz (1982).
              por \citeonline{10520:2000:4.1-1}.

                                                               Oliveira e Leonardos (1943, p. 146) di-
              \citeonline[p.~146]{10520:2000:4.2-2}
                                                               zem que . . .
              dizem que \ldots\

                                                               Segundo Sá (1995, p. 27) . . .
              Segundo
                  \citeonline[p.~27]{10520:2000:4.2-3}
              \ldots\

                                                              Aqui vai um texto qualquer só para po-
              Aqui vai um texto qualquer só para\\
                                                              der citar alguém (LOPES, 2000, p. 225).
              poder citar alguém
              \cite[p.~225]{10520-2002:6.3-1}.

                                                               Bobbio (1995, p. 35) apresenta uma série
              \citeonline[p.~35]{10520-2002:6.3-2}
                                                               de coisas incompreensíveis.
              apresenta uma série
              de coisas incompreensíveis.

                                                               Mais um exemplo articifial mas necessá-
              Mais um exemplo articifial
                                                               rio de citação (JOSSUA; METZ, 1976,
              mas necessário de citação
                                                               p. 3).
              \cite[p.~3]{10520-2002:6.3-3}.

                                                               Merriam e Caffarella (1991) são mais
              \citeonline{10520-2002:6.3-4}
                                                               um exemplo de citação bem bacana.
              são mais um exemplo de citação
              bem bacana.

                                                                 Exemplo que mostra alguma coisa tam-
               Exemplo que mostra alguma
                                                                 bém (COMISSÃO DAS COMUNIDA-
               coisa também
                                                                 DES EUROPÉIAS, 1992, p. 34).
               \cite[p.~34]{10520-2002:6.3-5}.

               4.2.2   Referências a organization
organization   Se a autoria do texto for do tipo organization, você pode usar as citações normalmente.
               No entanto, é recomendado que, para organizações com descrição longa, você controle o
               que aparece no texto com o campo org-short do arquivo .bib. No exemplo seguinte
               temos:

               organization={Comiss\~ao das Comunidades Europ\’eias},

                                                                 Exemplo que mostra alguma coisa tam-
               Exemplo que mostra alguma
                                                                 bém (COMISSÃO DAS COMUNIDA-
               coisa também
                                                                 DES EUROPÉIAS, 1992, p. 34).
               \cite[p.~34]{10520-2002:6.3-5}.

               Já neste exemplo:

               organization={Brasil. {Ministério da Administração Federal
               e da Reforma do Estado}},
               org-short ={Brasil},

                                                                 E a pátria não poderia faltar (BRASIL,
               E a pátria não poderia faltar
                                                                 1995).
               \cite{10520-2002:6.3-6}.

               4.2.3   Citações com autoria dada pelo título

                                                                 Uma lei anônima (ANTEPROJETO. . . ,
               Uma lei anônima
                                                                 1987, p. 55).
               \cite[p.~55]{10520-2002:6.3-7}.

                                                                 Uma artigo anônimo (A FLOR. . . , 1995,
               Uma artigo anônimo
                                                                 p. 4).
               \cite[p.~4]{10520-2002:6.3-8}.

                                                                  Outro artigo anônimo (NOS CANAVI-
               Outro artigo anônimo
                                                                  AIS. . . , 1995, p. 12).
               \cite[p.~12]{10520-2002:6.3-9}.

               4.2.4   Referências implícitas (cite)
      \cite    São aquelas referências que não fazem parte do texto. Use com \cite.
               Exemplos:

                                                                  para que . . . à sociedade (SOUTO, 1916,
               para que \ldots\ àsociedade
                                                                  p. 46, grifo nosso) . . .
               \cite[p.~46, grifo nosso]{10520:2000:4.8}
               \ldots\

                                                                  b) desejo de . . . passado colonial (CAN-
               b) desejo de \ldots\ passado colonial
                                                                  DIDO, 1993, v. 2, p. 12, grifo do autor)
               \cite[v.~2, p.~12, grifo do autor]%
                                                                  ...
               {10520:2000:4.8.1} \ldots\

                                                                  “Apesar das . . . da filosofia” (DER-
               ‘‘Apesar das \ldots\ da filosofia’’
                                                                  RIDA, 1967, p. 293).
               \cite[p.~293]{10520:2000:4.1-2}.

                                                                  Depois, . . .   que prefiro (DEPOI-
               Depois, \ldots\ que prefiro
                                                                  MENTO. . . , 1978, p. 101–114).
               \cite[p.~101--114]{10520:2000:4.1-3}.

                                                                  A produção de . . . em 1928 (MUM-
               A produção de \ldots\ em 1928
                                                                  FORD, 1949, p. 513) .
               \cite[p.~513]{10520:2000:4.2-1} .

               4.2.5   Referências citadas por outra referência (apud)
       \apud   Para citar uma referência que é citada dentro de outra referência, pode-se usar as macros
\apudeonline   \apud e \apudonline, como nos exemplos abaixo.

                                                                  (SAGE, 1992 apud EVANS, 1987, p. 2–
               \apud[p.~2--3]{Sage1992}{Evans1987}
                                                                  3)

                                                                    Segundo Silva (1992 apud ABREU,
               Segundo
                                                                    1999, p. 3)
                   \apudonline[p.~3]{Silva1992}{Abreu1999}

               Nesses casos, todas as referências aparecerão na lista de referências, exceto aquelas
               definidas como entrada @hidden. Ou seja, se você não quiser que uma entrada apareça
               na lista de referências, você deve defini-la como @hidden na sua base bibliográfica.

               4.2.6   Citações em notas de rodapé
               A seção 7 da ABNT (2002a) apresenta as regras para referências em notas de rodapé.
               A seção 7.1.1 estabelece que “A primeira citação de uma obra, em nota de rodapé, deve
               ter sua referência completa.” As regras para as demais citações são estabelecidas pela
               seção 7.1.2, e podem ser atendidas pelos comandos detalhados pela Subsubseção 4.2.7.
\footciteref   Para inserir referências no rodapé da página, use:
                                                                    No rodapé1
                                                                       1 FARIA, J. E. (Org.).   Direitos huma-
               No rodapé\footciteref{10520-2002:7.1.1}              nos, direitos sociais e justiça. São Paulo:
                                                                    Malheiros, 1994.

               Atenção: comando \footciteref não se encontra totalmente funcional, e limitações
               são conhecidas. Por exemplo, veja <https://github.com/abntex/abntex2/issues/167>
               (acesso de 12.jun.2018).

               4.2.7   Uso de idem, ibidem, opus citatum e outros
               Implementamos comandos específicos para idem (mesmo autor), ibidem (mesma obra),
               opus citatum (obra citada), passim (aqui e alí), loco citato (no lugar citado), confira e
               et sequentia (e sequência) que atendem as orientações da seção seção 7.1.2 da ABNT
               (2002a). Veja uso desses tipos de citações nos exemplos abaixo.
       \Idem

                                                                    Id., 2000, p. 2
               \Idem[p.~2]{NBR6023:2000}

     \Ibidem

                                                                    Ibid., p. 2
               \Ibidem[p.~2]{NBR6023:2000}

      \opcit

                                                                    ABNT, op. cit., p. 2
               \opcit[p.~2]{NBR6023:2000}

     \passim

                                                                    ABNT, 2000, passim
               \passim{NBR6023:2000}

     \loccit

                                                                    ABNT, 2000, loc. cit.
               \loccit{NBR6023:2000}

   \cfcite

                                                                 Cf. ABNT, 2000, p. 2
              \cfcite[p.~2]{NBR6023:2000}

     \etseq

                                                                 ABNT, 2000, p. 2, et seq.
              \etseq[p.~2]{NBR6023:2000}

              Note que esses comandos só fazem sentido para citações a uma única referência por vez.
              Segundo o ítem 7.1.2 da ‘norma’ (ABNT, 2002a), essas expressões só devem ser usadas
              em notas de rodapé, não no texto. Apenas a expressão apud poderia ser usada no texto.
              As citações em notas de rodapé são detalhadas pela Subsubseção 4.2.6.

              4.2.8   Referências múltiplas
      \cite   Frequentemente queremos citar diversas referências de uma vez. Para isso, use
\citeonline   \cite{hkey1,key2,. . . ,keyN i} ou \citeonline{hkey1,key2,. . . ,keyN i}, separando cada
              chave por uma vírgula sem espaços e sem mudança de linha.

                                                            (CRUZ; CORREA; COSTA, 1998;
              \cite{10520:2000:5.1.4-98,10520:2000:5.1.4-99,%
                                                             CRUZ; CORREA; COSTA, 1999;
              10520:2000:5.1.4-00}
                                                             CRUZ; CORREA; COSTA, 2000)

                                                                 Cruz, Correa e Costa (1998), Cruz, Cor-
              \citeonline{10520:2000:5.1.4-98,%
                                                                 rea e Costa (1999), Cruz, Correa e Costa
              10520:2000:5.1.4-99,10520:2000:5.1.4-00}
                                                                 (2000)

                                                                 (ABNT, 1988; ABNT, 2000; ABNT,
              \cite{NBR10520:1988,NBR6023:2000,%
                                                                 2001)
              NBR10520:2001}

                                                                 ABNT (1988), ABNT (2000), ABNT
              \citeonline{NBR10520:1988,NBR6023:2000,%
                                                                 (2001)
              NBR10520:2001}

              4.2.9   Múltiplas referências com mesmo autor-data
              Quando há várias referências com o mesmo autor-data, abntex2cite.sty gera auto-
              maticamente um ‘a’, ‘b’, etc., adicional. Isto atende ao ítem 5.1.3 da ‘norma’ (ABNT,
              2001).

                                                                     (REESIDE, 1927a; REESIDE, 1927b)
                    \cite{10520:2000:5.1.3a,10520:2000:5.1.3b}

                                                                   Reeside (1927a), Reeside (1927b)
                    \citeonline{10520:2000:5.1.3a,10520:2000:5.1.3b}

                    4.2.10   Mais de três autores e o uso de et al.
                    A ‘norma’ (ABNT, 2001) é omissa sobre o caso de chamadas a obras com mais de três
                    autores. Mesmo entre os 204 exemplos da ‘norma’ (ABNT, 2000), ocorre apenas um
                    único caso, usado nos exemplos a seguir.

                                                                      Segundo Urani et al. (1994) entende-se
                    Segundo \citeonline{urani1994}
                                                                      que . . .
                    entende-se que \ldots\

                                                                      Em recente estudo (DENG et al., 2000)
                    Em recente estudo \cite{Deng00}
                                                                      foram investigados estados em fios quân-
                    foram investigados estados em
                                                                      ticos.
                    fios quânticos.

                    Você pode altera esse comportamento usando as opções abnt-etal-cite, abnt-etal-list
                    e abnt-etal-text. Veja mais informacões na Tabela 1 e em (ARAUJO, 2015b).

                    4.2.11   Citações de partes da referência
                    Às vezes pode ser necessário citar apenas uma parte da referência, como apenas o autor
                    ou apenas o ano. Para isso, foram implementados os comandos \citeauthoronline,
                    \citeauthor e \citeyear, exemplificados do seguinte modo:
\citeauthoronline   A macro \citeauthoronline deve ser utilizada para citar apenas o autor de forma
                    explícita:

                                                                     A produção de . . . em 1928 mencionada
                    A produção de \ldots\ em 1928
                                                                     por Mumford.
                    mencionada por
                    \citeauthoronline{10520:2000:4.2-1}.

      \citeauthor   A macro \citeauthor deve ser utilizada para citar apenas o autor de forma implícita:

                                                                      A produção de . . .   em 1928 (MUM-
                  A produção de \ldots\ em 1928
                                                                      FORD 1928).
                  (\citeauthor{10520:2000:4.2-1} 1928).

      \citeyear   A macro \citeyear deve ser utilizada para citar apenas o ano da publicação:

                                                                      Em 1982 a ironia será assim uma . . .
                  Em \citeyear{10520:2000:4.1-1} a ironia
                                                                      proposta por.
                  será assim uma \ldots\ proposta por.

                  5    Formações do estilo alfabético
      versalete   A opção versalete imprime os nomes dos autores das citações em versalete (small
                  caps, ou seja, letras maiúsculas com corpo do tamanho das minúsculas), ao invés de
                  maiúscula. Usar versalete era o comportamento padrão do abnTeX e do abnTeX2 até a
                  versão 1.4. Porém, os exemplos da norma ABNT NBR 10520 são em letras maiúsculas.
                  Por isso, à partir da versão 1.5, o abnTeX2 traz como padrão as citações em letras
                  maiúsculas e a opção versalete como compatibilidade com as versões anteriores. Para
                  usar o modelo antigo, ou seja, em versalete, use:

                  \usepackage[alf,versalete]{abntex2cite}

\authorcapstyle   O estilo usado na impressão dos nomes dos autores nas citações pode ser alterado com:
   \authorstyle

                  \renewcommand{\authorcapstyle}{\small}
                  \newcommand{\authorstyle}{\relax}

    \yearstyle    O estilo usado na impressão do ano nas citações pode ser alterado com:

                  \renewcommand{\yearstyle}{\bf}

                  6    Alteração do estilo alfabético citeoption
    \citeoption   Com o comando \citeoption ou \usepackage você pode alterar alguns comportamen-
                  tos do estilo bibliográfico. Na Tabela 1, listamos as opções que são específicas do estilo
                  abnt-alf.
                  Por exemplo, para desativar a substituição dos autores por ‘et al.’, você incluir o pacote
                  com a seguinte opção:

                  \usepackage[alf,abnt-etal-cite=0]{abntex2cite}

ou, em qualquer ponto do texto,

\citeoption{abnt-etal-cite=0}

Para ver as demais opções e o modo de uso veja o documento (ARAUJO, 2015b).

         Tabela 1: Opções de alteração da composição dos estilos bibliográficos.
       campo              opções descrição
       abnt-and-type                determina de que maneira é formatado o and.
       abnt-and-type=e          e Usa ‘e’ como em ‘Fonseca e Paiva’.
      abnt-and-type=&           & Usa ‘&’ como em ‘Fonseca & Paiva’.
       abnt-etal-cite               controla como e quando os co-autores são subs-
                                    tituídos por et al.. Note que a substituição
                                    por et al. continua ocorrendo sempre se os co-
                                    autores tiverem sido indicados como others.
      abnt-etal-cite=0          0 não abrevia a lista de autores.
      abnt-etal-cite=2          2 abrevia com mais de 2 autores.
      abnt-etal-cite=3          3 abrevia com mais de 2 autores.
      ..                         ..
       .                          .
      abnt-etal-cite=5               5   abrevia com mais de 5 autores.

7      Problemas com a ‘norma’ 10520
Como já foi dito, a ‘norma’ 10520 (ABNT, 2001) é incompleta e inconsistente. Aqui apre-
sentamos uma descrição dos principais problemas encontrados e como foram resolvidos,
quando foi possível.

7.1      Referências múltiplas
As referências a vários autores simultaneamente, ou várias obras de um mesmo autor,
são um verdadeiro mistério na “norma” (ABNT, 2001). No exemplo da seção 5.1.4, diz
a “norma”’
       As citações de diversos documentos de um mesmo autor, publicados em anos
       diferentes e mencionados simultaneamente, têm as suas datas separadas por
       vírgula.
       Exemplo: (CRUZ; CORREA; COSTA; 1998, 1999, 2000)3
Podemos então entender que Cruz, Correa e Costa são os três autores e 1998, 1999 e
2000 são os três anos de publicação referindo-se a três documentos separados?
Antes de responder sim, veja o que diz a seção seguinte, 5.1.5:
       As citações de diversos documentos de vários autores, mencionados simulta-
       neamente, devem ser separadas por ponto e vírgula.
       Exemplo: (FONSECA; PAIVA; SILVA, 1997)4
    3 Transcrição exata. Esta chamada não foi gerada automaticamente.
    4 Transcrição exata. Esta chamada não foi gerada automaticamente.

E agora? Trata-se de três autores separados, Fonseca, Paiva, Silva? Ou um autor
Fonseca e outro documento com dois autores, Paiva e Silva? Ou um documento com
dois autores Fonseca e Paiva seguido de um autor Silva? Quem não lê a descrição
da seção 5.1.5, pode-se inclusive achar que trata-se de um único documento. Ou o
exemplo da seção 5.1.5 está errado: faltam datas aos outros autores, ou foi uma tentativa
desastrada de agrupar três documentos com o mesmo ano de publicação. Já exemplo
anterior, da seção 5.1.4, há problemas também com um ponto-e-vírgula após o COSTA,
quando deveria haver apenas uma vírgula.
Veja na Subsubseção 4.2.8 como fica a nossa solução.
Exemplo da seção 5.1.5:

                                                         (FONSECA, 1997; PAIVA, 1997; SILVA,
\cite{10520:2000:5.1.5a,10520:2000:5.1.5b,%
                                                         1997)
10520:2000:5.1.5c}

                                               Fonseca (1997), Paiva (1997), Silva
\citeonline{10520:2000:5.1.5a,10520:2000:5.1.5b,%
                                              (1997)
10520:2000:5.1.5c}

ou, supondo que Fonseca e Paiva sejam co-autores,

                                                         (FONSECA; PAIVA, 1997;            SILVA,
\cite{10520:2000:5.1.5ab,10520:2000:5.1.5c}
                                                         1997)

                                               Fonseca e Paiva (1997), Silva (1997)
\citeonline{10520:2000:5.1.5ab,10520:2000:5.1.5c}

7.2    et al.
A ‘norma’ 10520 (ABNT, 2001) nada diz sobre como devem ser tratadas as chamadas
a referências com mais de três autores. Supondo que exista uma relação lógica entre
as ‘normas’ 10520 (ABNT, 2001) e 6023 (ABNT, 2000), então faz sentido pensar que
deve-se usar ‘et al.’ na chamada exatamente nos mesmos casos em que ‘et al.’ é usado
na lista bibliográfica. No caso, a 6023 diz que se deve usar ‘et al.’ para mais de três
autores, ou seja, a partir de quatro autores.5
 Parece lógico, não é mesmo? Então veja o seguinte caso. Fomos informados que nas
‘normas’ da UFLA (que supostamente seguem as ‘normas’ da ABNT) exige-se o uso de
‘et al.’ na chamada já com três autores e não se use ‘et al.’ na lista bibliográfica. E
 agora? Cadê a lógica?
Por isso insistimos que você sempre verifique a ‘lógica’ da sua instituição bem antes de
entregar a sua tese.
  5 Muitas pessoas entendem isso errado e pensam que se usa ‘et al.’ já com três autores

Referências
A FLOR prometida. A Folha de S. Paulo, São Paulo, p. 4, 2 abr. 1995.

@article{10520-2002:6.3-8,
address={S\~ao Paulo},
journal={A Folha de S.~Paulo},
month={2 abr.},
pages={4},
title={A~flor prometida},
year={1995}}

ABREU, X. Y. Z. Exemplo de citação no texto. [S.l.: s.n.], 1999.

@book{Abreu1999,
author={X. Y. Z. Abreu},
title={Exemplo de cita{\c c}\~ao no texto},
year={1999}}

ANTEPROJETO de lei. Estudos e Debates, Brasília, DF, n. 13, p. 51–60, jan. 1987.

@article{10520-2002:6.3-7,
address={Brasília, DF},
journal={Estudos e Debates},
month={jan.},
number={13},
pages={51-60},
title={Anteprojeto de lei},
year={1987}}

ARAUJO, L. C. A classe abntex2: Modelo canônico de trabalhos acadêmicos brasileiros
compatível com as normas ABNT NBR 14724:2011, ABNT NBR 6024:2012 e outras.
[S.l.], 2015. Disponível em: <http://www.abntex.net.br/>.

@manual{abntex2classe,
author={Lauro C{\’e}sar Araujo},
organization={Equipe abnTeX2},
title={A classe abntex2: Modelo can{\^o}nico de trabalhos acad{\^e}micos
  brasileiros compat{\’\i}vel com as normas ABNT NBR 14724:2011, ABNT NBR
  6024:2012 e outras},
url={http://www.abntex.net.br/},
year={2015}}

        . O pacote abntex2cite: Estilos bibliográficos compatíveis com a ABNT NBR 6023.
[S.l.], 2015. Disponível em: <http://www.abntex.net.br/>.

@manual{abntex2cite,

author={Lauro C{\’e}sar Araujo},
organization={Equipe abnTeX2},
title={O pacote abntex2cite: Estilos bibliogr{\’a}ficos compat{\’\i}veis com a
  ABNT NBR 6023},
url={http://www.abntex.net.br/},
year={2015}}

ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. NBR 10520 : Apresentação
de citações em documentos — procedimentos. Rio de Janeiro, 1988. 3 p.

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

      . NBR 6023 : Informação e documentação — referências — elaboração. Rio de
Janeiro, 2000. 22 p.

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

     . NBR 10520 : Informação e documentação — apresentação de citações em
documentos. Rio de Janeiro, 2001. 4 p. Substitui a Ref. ABNT (1988).

@manual{NBR10520:2001,
address={Rio de Janeiro},
month={jul.},
note={Substitui a Ref.~\citeonline{NBR10520:1988}},
organization={Associa{\c c}\~ao Brasileira de Normas T\’ecnicas},
org-short={ABNT},
pages={4},
subtitle={Informa{\c c}\~ao e documenta{\c c}\~ao --- Apresenta{\c c}\~ao de
  cita{\c c}\~oes em documentos},
title={{NBR} 10520},
year={2001}}

      .      . Rio de Janeiro, 2002. 7 p. Substitui a Ref. ABNT (2001).

@manual{NBR10520:2002,
address={Rio de Janeiro},
month={ago.},
note={Substitui a Ref.~\citeonline{NBR10520:2001}},
organization={Associa{\c c}\~ao Brasileira de Normas T\’ecnicas},
org-short={ABNT},
pages={7},
subtitle={Informa{\c c}\~ao e documenta{\c c}\~ao --- Apresenta{\c c}\~ao de
  cita{\c c}\~oes em documentos},
title={{NBR} 10520},
year={2002}}

      . NBR 6023 : Informação e documentação — referências — elaboração. Rio de
Janeiro, 2002. 24 p. Substitui a Ref. ABNT (2000).

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

AUTHLER-REIRIZ, X. Y. Z. Exemplo de citação no texto. [S.l.: s.n.], 1982.

@book{10520:2000:4.1-1,
author={X. Y. Z. Authler-Reiriz},
title={Exemplo de cita{\c c}\~ao no texto},
year={1982}}

BOBBIO, N. O positivismo jurídico: lições de filosofia do direito. São Paulo: Ícone,
1995.

@book{10520-2002:6.3-2,
address={S\~ao Paulo},
author={Noberto Bobbio},
publisher={\’Icone},
subtitle={li{\c c}\~oes de Filosofia do Direito},
title={O positivismo jur{\’\i}dico},
year={1995}}

BRASIL. Ministério da Administração Federal e da Reforma do Estado. Plano diretor
da reforma do aparelho do estado. Brasília, DF, 1995.

@manual{10520-2002:6.3-6,
address={Brasília, DF},
organization={Brasil. {Ministério da Administra{\c c}\~ao Federal e da Reforma
  do Estado}},
org-short={Brasil},
title={Plano diretor da reforma do aparelho do estado},
year={1995}}

CANDIDO, X. Y. Z. Exemplo de citação no texto. [S.l.: s.n.], 1993.

@book{10520:2000:4.8.1,
author={X. Y. Z. Candido},
title={Exemplo de cita{\c c}\~ao no texto},
year={1993}}

COMISSÃO DAS COMUNIDADES EUROPÉIAS. A união européia. Luxemburgo:
Serviço das Publicações Oficiais das Comunidades Européias, 1992.

@book{10520-2002:6.3-5,
address={Luxemburgo},
organization={Comiss\~ao das Comunidades Europ\’eias},
publisher={Servi{\c c}o das Publica{\c c}\~oes Oficiais das Comunidades
  Europ\’eias},
title={A uni\~ao europ\’eia},
year={1992}}

CRUZ, X. Y. Z.; CORREA, X. Y. Z.; COSTA, X. Y. Z. Exemplo de citação no texto.
[S.l.: s.n.], 1998.

@book{10520:2000:5.1.4-98,
author={X. Y. Z. Cruz and X. Y. Z. Correa and X. Y. Z. Costa},
title={Exemplo de cita{\c c}\~ao no texto},
year={1998}}

     .       . [S.l.: s.n.], 1999.

@book{10520:2000:5.1.4-99,
author={X. Y. Z. Cruz and X. Y. Z. Correa and X. Y. Z. Costa},
title={Exemplo de cita{\c c}\~ao no texto},
year={1999}}

     .       . [S.l.: s.n.], 2000.

@book{10520:2000:5.1.4-00,
author={X. Y. Z. Cruz and X. Y. Z. Correa and X. Y. Z. Costa},
title={Exemplo de cita{\c c}\~ao no texto},
year={2000}}

DENG, Z.-Y. et al. Subband structures and exciton and impurity states in V-shaped
GaAs-Ga1−x Alx As quantum wires. Phys. Rev. B, v. 61, p. 15905–15913, 2000.

@article{Deng00,
author={Z-Y Deng and X Chen and T Ohji and T Kobayashi},
journal={Phys.\ Rev.\ B},
pages={15905-15913},
title={Subband structures and exciton and impurity states in {V}-shaped
  {GaAs-Ga$_{1-x}$Al$_x$As} quantum wires},
volume={61},
year={2000}}

DEPOIMENTO sobre qualquer coisa. [S.l.: s.n.], 1978. 101-114 p.

@book{10520:2000:4.1-3,
pages={101-114},
title={Depoimento sobre qualquer coisa},
year={1978}}

DERRIDA, X. Y. Z. Exemplo de citação no texto. [S.l.: s.n.], 1967. 293 p.

@book{10520:2000:4.1-2,
author={X. Y. Z. Derrida},
pages={293},
title={Exemplo de cita{\c c}\~ao no texto},
year={1967}}

EVANS, X. Y. Z. Exemplo de citação no texto. [S.l.: s.n.], 1987.

@book{Evans1987,
author={X. Y. Z. Evans},
title={Exemplo de cita{\c c}\~ao no texto},
year={1987}}

FARIA, J. E. (Org.). Direitos humanos, direitos sociais e justiça. São Paulo: Malheiros,
1994.

@book{10520-2002:7.1.1,
address={São Paulo},
editor={José Eduardo Faria},

editortype={Org.},
publisher={Malheiros},
title={Direitos humanos, direitos sociais e justiça},
year={1994}}

FONSECA, X. Y. Z. Exemplo de citação no texto. [S.l.: s.n.], 1997.

@book{10520:2000:5.1.5a,
author={X. Y. Z. Fonseca},
title={Exemplo de cita{\c c}\~ao no texto},
year={1997}}

FONSECA, X. Y. Z.; PAIVA, X. Y. Z. Exemplo de citação no texto. [S.l.: s.n.], 1997.

@book{10520:2000:5.1.5ab,
author={X. Y. Z. Fonseca and X. Y. Z. Paiva},
title={Exemplo de cita{\c c}\~ao no texto},
year={1997}}

JOSSUA, J. P.; METZ, J. B. Editorial: Teologia e literatura. Concilium, Petrópolis,
v. 115, n. 5, p. 2–5, 1976.

@article{10520-2002:6.3-3,
address={Petr\’opolis},
author={Jossua, Jean Pierre and Metz, Johann Baptist},
journal={Concilium},
number={5},
pages={2-5},
title={Editorial: Teologia e Literatura},
volume={115},
year={1976}}

LOPES, J. R. de L. O direito na história. São Paulo: Max Limonad, 2000.

@book{10520-2002:6.3-1,
address={S\~ao Paulo},
author={Jos\’e Reinaldo de Lima Lopes},
publisher={Max Limonad},
title={O direito na história},
year={2000}}

MAKAU, A. B. Esperanza de la educación hoy. Lisboa: J. Piaget, 1962. Separata de:
Moore (1960)

@book{makau1962,
address={Lisboa},

author={A. B. Makau},
publisher={J.~Piaget},
reprinted-from={wmoore1960},
title={Esperanza de la educaci\’on hoy},
year={1962}}

MERRIAM, S.; CAFFARELLA, R. Learning in adulthood: a comprehensive guide. San
Francisco: Jossey-Bass, 1991.

@book{10520-2002:6.3-4,
address={San Francisco},
author={S. Merriam and R. Caffarella},
publisher={Jossey-Bass},
subtitle={a comprehensive guide},
title={Learning in adulthood},
year={1991}}

MOORE, W. (Ed.). Construtivismo del movimiento educacional: soluciones. Córdoba,
AR: [s.n.], 1960. 309-340 p.6

@book{wmoore1960,
address={C\’ordoba, AR},
editor={W. Moore},
pages={309-340},
subtitle={soluciones},
title={Construtivismo del movimiento educacional},
year={1960}}

MUMFORD, X. Y. Z. Exemplo de citação no texto. [S.l.: s.n.], 1949.

@book{10520:2000:4.2-1,
author={X. Y. Z. Mumford},
title={Exemplo de cita{\c c}\~ao no texto},
year={1949}}

NOS CANAVIAIS, mutilação em vez de lazer e escola. O Globo — O País, Rio de
Janeiro, p. 12, 16 jul. 1995.7

@article{10520-2002:6.3-9,
address={Rio de Janeiro},
journal={O~Globo},
month={16 jul.},
pages={12},
section={O Pa{\’\i}s},
  6 Essa referência ainda traz importantes problemas de implementação. No original aparecem dois

campos address/publisher. A segunda ocorrência desses campos por enquanto é ignorada pelo estilo.
  7 Não sabemos porque no original a seção vem antes da página. Ainda estamos verificando isso.

title={Nos~canaviais, mutila{\c c}\~ao em vez de lazer e escola},
year={1995}}

OLIVEIRA, X. Y. Z.; LEONARDOS, X. Y. Z. Exemplo de citação no texto. [S.l.: s.n.],
1943.

@book{10520:2000:4.2-2,
author={X. Y. Z. Oliveira and X. Y. Z. Leonardos},
title={Exemplo de cita{\c c}\~ao no texto},
year={1943}}

PAIVA, X. Y. Z. Exemplo de citação no texto. [S.l.: s.n.], 1997.

@book{10520:2000:5.1.5b,
author={X. Y. Z. Paiva},
title={Exemplo de cita{\c c}\~ao no texto},
year={1997}}

REESIDE, X. Y. Z. Exemplo de citação no texto. [S.l.: s.n.], 1927.

@book{10520:2000:5.1.3a,
author={X. Y. Z. Reeside},
title={Exemplo de cita{\c c}\~ao no texto},
year={1927}}

      .      . [S.l.: s.n.], 1927.

@book{10520:2000:5.1.3b,
author={X. Y. Z. Reeside},
title={Exemplo de cita{\c c}\~ao no texto},
year={1927}}

SÃO PAULO (Estado). Secretaria do Meio Ambiente. Tratados e organizações ambientais
em matéria de meio ambiente. In:       . Entendendo o meio ambiente. São Paulo,
1999. v. 1. Disponível em: <http://www.bdt.org.br/sma/entendendo/atual.htm>.
Acesso em: 8 mar. 1999.

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

SÁ, X. Y. Z. P. de. Exemplo de citação no texto. [S.l.: s.n.], 1995.

@book{10520:2000:4.2-3,
author={X. Y. Z. Pereira~de~S\’a},
title={Exemplo de cita{\c c}\~ao no texto},
year={1995}}

@hidden{Sage1992,
author={X. Y. Z. Sage},
title={Exemplo de cita{\c c}\~ao no texto},
year={1992}}

SANTOS, F. R. dos. A colonização da terra do tucujús. In:              . História do Amapá,
1o grau. 2. ed. Macapá: Valcan, 1994. cap. 3, p. 15–24.

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

@hidden{Silva1992,
author={X. Y. Z. Silva},
year={1992}}

SILVA, X. Y. Z. Exemplo de citação no texto. [S.l.: s.n.], 1997.

@book{10520:2000:5.1.5c,
author={X. Y. Z. Silva},
title={Exemplo de cita{\c c}\~ao no texto},
year={1997}}

SIMPÓSIO BRASILEIRO DE REDES DE COMPUTADORES, 13., 1995, Belo
Horizonte. Anais... Belo Horizonte: UFMG, 1995. 655 p.

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

SOUTO, X. Y. Z. Exemplo de citação no texto. [S.l.: s.n.], 1916.

@book{10520:2000:4.8,
author={X. Y. Z. Souto},
title={Exemplo de cita{\c c}\~ao no texto},
year={1916}}

URANI, A. et al. Constituição de uma matriz de contabilidade social para o Brasil.
Brasília, DF: IPEA, 1994.

@book{urani1994,
address={Bras{\’\i}lia, DF},
author={Urani, A and others},
publisher={IPEA},
title={Constitui{\c c}\~ao de uma matriz de contabilidade social para o
  Brasil},
year={1994}}
