# Referência rápida — abnTeX2 v-1.9.7

Trechos verificados nos exemplos de `abntex2/doc/examples/` e nos manuais em
`docs/manuais/`. Para estrutura completa, leia o `.tex` do modelo escolhido.

## Como escolher o modelo

Interprete o pedido e escolha pelo tipo de documento; na dúvida, use
`trabalho-academico`.

| O pedido parece... | Modelo |
| --- | --- |
| "trabalho", "pesquisa", "seminário", TCC, monografia; capa, introdução, desenvolvimento, conclusão | `abntex2-modelo-trabalho-academico.tex` (NBR 14724) |
| artigo científico, paper, resumo com palavras-chave, publicado em periódico | `abntex2-modelo-artigo.tex` (NBR 6022) |
| projeto de pesquisa: justificativa, objetivos, metodologia, cronograma | `abntex2-modelo-projeto-pesquisa.tex` (NBR 15287) |
| relatório de atividade, experimento, visita técnica, estágio | `abntex2-modelo-relatorio-tecnico.tex` (NBR 10719) |
| apresentação de slides | `abntex2-modelo-slides.tex` (beamer) |
| livro, folheto, glossário | só quando pedido explicitamente |

Diferenças que mudam a estrutura (o resto do preâmbulo é igual):

| Item | trabalho acadêmico | artigo | projeto de pesquisa | relatório técnico |
| --- | --- | --- | --- | --- |
| Opções da classe | `12pt,oneside,a4paper,brazil` (sem `openright`) | `article,11pt,oneside,a4paper,brazil,sumario=tradicional` | `12pt,oneside,a4paper,brazil` (sem `openright`) | igual ao acadêmico |
| Abertura | `\imprimircapa` + `\imprimirfolhaderosto*` | `\maketitle` | `\imprimircapa` + `\imprimirfolhaderosto` (sem `*`) | `\imprimircapa` + `\imprimirfolhaderosto*` |
| Resumo | `resumo` + `resumo[Abstract]` (e outros idiomas) | `resumoumacoluna` (abstract opcional) | não tem | só `resumo` em português |
| Folha de aprovação | **não usar** | **não usar** | **não usar** | **não usar** |
| Sumário | `\tableofcontents*` | não | `\tableofcontents*` | `\tableofcontents*` |
| Divisão do texto | `\chapter`/`\section` | `\section` (sem `\chapter`) | `\chapter`/`\section` | `\chapter`/`\section` |
| Extra obrigatório | — | data de submissão/aprovação | — | formulário de identificação nos anexos |

## Preâmbulo

Base do trabalho acadêmico, projeto e relatório (**oneside**, sem `openright`):

```latex
\documentclass[12pt,oneside,a4paper,brazil]{abntex2}
\usepackage{lmodern}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{indentfirst}
\usepackage{graphicx}
\usepackage{microtype}
\usepackage[alf]{abntex2cite}   % autor-data; use [num] para numérico
```

No artigo, troque a primeira linha por:

```latex
\documentclass[article,11pt,oneside,a4paper,brazil,sumario=tradicional]{abntex2}
```

Texto todo em preto, inclusive hyperlinks (os exemplos oficiais usam azul):

```latex
\hypersetup{
    colorlinks=true,
    linkcolor=black,          % links internos (sumário, figuras, tabelas)
    citecolor=black,          % citações no texto
    filecolor=black,          % links para arquivos
    urlcolor=black            % URLs e e-mails
}
```

## Fonte uniforme (12pt em tudo)

O padrão da classe usa tamanhos maiores nos títulos (`\Huge`, `\Large`, `\large`) e
menores em legendas/notas (`\footnotesize`). Para deixar todo o texto em 12pt,
inclua no preâmbulo:

```latex
% Títulos e textos reduzidos em 12pt
\renewcommand{\ABNTEXchapterfontsize}{\normalsize}
\renewcommand{\ABNTEXsectionfontsize}{\normalsize}
\renewcommand{\ABNTEXsubsectionfontsize}{\normalsize}
\renewcommand{\ABNTEXsubsubsectionfontsize}{\normalsize}
\renewcommand{\ABNTEXsubsubsubsectionfontsize}{\normalsize}
\renewcommand{\ABNTEXfontereduzida}{\normalsize}

% Capa e folha de rosto têm tamanhos fixos na classe; troque por \normalsize
\usepackage{etoolbox}
\patchcmd{\imprimircapa}{\large}{\normalsize}{}{}
\patchcmd{\imprimircapa}{\large}{\normalsize}{}{}
\patchcmd{\imprimircapa}{\large}{\normalsize}{}{}
\patchcmd{\imprimircapa}{\LARGE}{\normalsize}{}{}
\patchcmd{\folhaderostocontent}{\large}{\normalsize}{}{}
\patchcmd{\folhaderostocontent}{\large}{\normalsize}{}{}
\patchcmd{\folhaderostocontent}{\large}{\normalsize}{}{}
\patchcmd{\folhaderostocontent}{\large}{\normalsize}{}{}
\patchcmd{\folhaderostocontent}{\large}{\normalsize}{}{}
\patchcmd{\folhaderostocontent}{\Large}{\normalsize}{}{}
```

Não use `\small`/`\footnotesize` em quadros, tabelas ou qualquer trecho do texto.

## Dados do documento (usados na capa, folha de rosto etc.)

```latex
\titulo{Título}
\autor{Nome do autor}
\local{Salvador}
\data{2026}
\orientador{Nome}
\coorientador{Nome}          % opcional
\instituicao{Colégio ... \\ Curso ... \\ Turma ...}
\tipotrabalho{Relatório (Ensino Médio Técnico)}
\preambulo{Trabalho apresentado à disciplina ...}
```

## Pré-textuais do trabalho acadêmico

```latex
\pretextual
\imprimircapa
\imprimirfolhaderosto*        % o * inclui a ficha catalográfica
```

Ambientes: `fichacatalografica`, `errata`, `dedicatoria`, `agradecimentos`,
`epigrafe`, `resumo` (e `\begin{resumo}[Abstract]` para outro idioma), `siglas`,
`simbolos`. **Não usar `folhadeaprovacao` em nenhum modelo.**

Listas e sumário:

```latex
\pdfbookmark[0]{\listfigurename}{lof}
\listoffigures*
\cleardoublepage
% idem para \listoftables* e \tableofcontents*
```

## Artigo (NBR 6022)

- Abre com `\maketitle`; resumo no ambiente `resumoumacoluna` (com
  `\textbf{Palavras-chave}:`), abstract opcional repetindo o ambiente com
  `\renewcommand{\resumoname}{Abstract}`.
- Use `\section`, não `\chapter`.
- Inclua a data de submissão e aprovação; não há capa, folha de rosto nem sumário.

## Projeto de pesquisa (NBR 15287)

- `\imprimircapa` e `\imprimirfolhaderosto` sem `*`.
- Sem resumo e abstract (e sem folha de aprovação, como em todos os modelos).
- Listas e sumário como no trabalho acadêmico; texto dividido em capítulos
  (introdução, objetivos, justificativa, metodologia, cronograma).

## Relatório técnico (NBR 10719)

- Capa e folha de rosto com `*`; resumo só em português (sem abstract).
- Listas e sumário como no trabalho acadêmico.
- O modelo traz um formulário de identificação como anexo, referenciado por
  `\nameref{formulado-identificacao}` / `\autopageref{formulado-identificacao}`.

## Textuais e pós-textuais

```latex
\textual
\chapter{Introdução}
\section{...}
\chapter{Conclusão}

\postextual
\bibliography{referencias}

\begin{apendicesenv}
\partapendices
\chapter{Apêndice}
\end{apendicesenv}

\begin{anexosenv}
\partanexos
\chapter{Anexo}
\end{anexosenv}
```

## Figuras, tabelas e quadros

```latex
\begin{figure}[htb]
  \caption{\label{fig_exemplo}Legenda}
  \includegraphics[width=\textwidth]{imagem}
  \fonte{Autor.}
\end{figure}

\begin{quadro}[htb]
  \caption{\label{quadro_exemplo}Legenda}
  \begin{tabular}{|c|c|}
    \hline
    ... \\ \hline
  \end{tabular}
  \fonte{Autor.}
\end{quadro}
```

Referência no texto: `\autoref{fig_exemplo}` ou `Figura \ref{fig_exemplo}`.
O ambiente `quadro` e a lista de quadros já vêm configurados no modelo de trabalho
acadêmico.

## Citações e referências

- `\cite{chave}` / `\citeonline{chave}` — chamada no texto com ou sem o autor
  integrado à frase.
- Argumento opcional é o trecho/página: `\citeonline[3.1-3.2]{chave}`.
- `\citeyear`, `\citeauthor`, `\citeauthoronline`, `\citetext{chave}`.
- `\apud{chave1}{chave2}` e `\apudonline` para citação de citação; exigem entradas
  `@hidden` no `.bib` para as obras não citadas diretamente.
- Citação longa (mais de 3 linhas, recuo de 4 cm):

```latex
\begin{citacao}
Texto da citação longa.
\end{citacao}
```

- `\bibliography{referencias}` usa `abntex2-alf.bst` (opção `[alf]`) ou
  `abntex2-num.bst` (opção `[num]`). O `.bib` fica em UTF-8.
- **Máximo de 6 referências por trabalho, todas em português.**
- Em livros, o `year` é o da edição da editora escolhida, não o da obra original.
  Uma obra de Lênin da Editora X (2024) fica `year = {2024}` e
  `publisher = {Editora X}`.

## Armadilhas

- `\imprimirfolhaderosto*` (com asterisco) inclui a ficha catalográfica; sem o
  asterisco, não. Projeto de pesquisa usa sem asterisco.
- Os exemplos oficiais usam `openright,twoside` (geram páginas em branco). Aqui use
  sempre `oneside` e **não** use `openright`.
- `inputenc`/`fontenc` são para pdflatex; com XeLaTeX/LuaLaTeX, não use `inputenc`.
- `abntex2` é extensão de `memoir`: opções como `oneside`, `a4paper` e `article`
  vêm do memoir.
