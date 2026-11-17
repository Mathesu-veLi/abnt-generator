# AGENTS.md

## Objetivo
Produzir trabalhos escolares completos e formatados em ABNT, em LaTeX com a suíte
abnTeX2, a partir de um pedido curto do usuário ("faça um trabalho sobre X; orientador
é Y; matéria é Z"). A entrega é o `.tex` (mais o PDF compilado), não um framework.

Este repositório reúne apenas documentação e ferramentas de apoio: não há código
de geração. `abntex2/` é a cópia de referência da suíte v-1.9.7, com os manuais e
os exemplos oficiais.

## Perfil fixo dos trabalhos
- Instituição: Colégio Estadual de Educação Profissional Newton Sucupira (Salvador/BA)
- Curso: Informática (técnico) — turma **2VINF09**
- Autor: **Matheus Levi Fernandes da Silva**
- Trabalhos em equipe: inserir os integrantes em **ordem alfabética**, junto do autor.
- **Só criar o trabalho depois que o usuário informar a matéria** (disciplina) à qual
  ele pertence. Se a matéria não vier no pedido, perguntar antes de gerar qualquer
  arquivo.

## Estilo de escrita (obrigatório)
- Português muito simples e didático, sem enrolação. Tom dostoievskiano e humanizado;
  viés marxista-leninista apenas quando couber ao tema (não citar o Manifesto ou
  fontes do tipo em trabalhos que não têm relação com isso).
- Evitar marcas de texto gerado por IA:
  - fechar com "Em resumo..."/"Em suma..." ou oferta de ajuda;
  - listas e tópicos para tudo, quando prosa resolver;
  - títulos e negrito em respostas curtas;
  - tríades ("rápido, eficiente e confiável");
  - "não é apenas X, é Y", travessão (—) em excesso, frases de efeito isoladas,
    pergunta retórica seguida da própria resposta;
  - vocabulário: mergulhar, desvendar, jornada, ecossistema, panorama, robusto,
    fundamental, crucial, "vale ressaltar", "é importante destacar", "em um mundo
    cada vez mais...";
  - adjetivos grandiosos para coisas banais, hedge excessivo, entusiasmo artificial,
    simetria forçada ("por um lado... por outro"), generalidades sem posição concreta.

## Modelos e documentação (ler antes de escrever)
Antes de escrever, entenda a proposta do trabalho e use o exemplo que combina com
ela; a estrutura do novo documento deve seguir a do exemplo escolhido (ordem dos
elementos, preâmbulo e comandos). A seção **Como escolher o modelo** de
`docs/referencia-rapida.md` traz os sinais de decisão e uma tabela com as diferenças
de estrutura entre trabalho acadêmico, artigo, projeto e relatório.
- Comece por `docs/referencia-rapida.md`: preâmbulo, macros de dados, elementos
  pré/textuais/pós-textuais, figuras/quadros, citações e armadilhas, tudo verificado
  nos exemplos.
- Manuais em Markdown (conversão fiel dos PDFs, mesma versão) em `docs/manuais/`:
  `abntex2.md` (classe), `abntex2cite.md` (citações/referências) e
  `abntex2cite-alf.md` (estilo autor-data). Use `grep` para localizar a seção em vez
  de ler o arquivo inteiro; a conversão mantém quebras de linha do PDF.
- Os PDFs originais ficam em `abntex2/doc/` (use só se precisar da paginação).
  Para regenerar o Markdown: `python3 scripts/pdf_to_md.py`.
- Exemplos em `abntex2/doc/examples/`:
  - `abntex2-modelo-trabalho-academico.tex` — trabalho escolar, monografia, TCC,
    dissertação ou tese (NBR 14724). **Padrão quando o tipo não for especificado.**
  - `abntex2-modelo-artigo.tex` — artigo científico (NBR 6022).
  - `abntex2-modelo-projeto-pesquisa.tex` — projeto de pesquisa (NBR 15287).
  - `abntex2-modelo-relatorio-tecnico.tex` — relatório técnico/científico (NBR 10719).
  - `abntex2-modelo-slides.tex` — apresentação em beamer; `abntex2-modelo-livro.tex`
    e `abntex2-modelo-glossarios.tex` só quando pedidos explicitamente.
- `abntex2-modelo-include-comandos.tex` explica comandos e o processo de compilação;
  `abntex2-modelo-references.bib` serve de modelo de `.bib`.
- Os exemplos são material de leitura: copie a estrutura para o novo `main.tex` e
  compile fora de `abntex2/`, sem editar os arquivos originais.

## Estrutura do documento
- Preâmbulo: `\documentclass[12pt,oneside,a4paper,brazil]{abntex2}` (**oneside, sem
  `openright`** — os exemplos oficiais usam `openright,twoside`, mas os trabalhos
  gerados aqui não), `lmodern`, `fontenc[T1]`, `inputenc[utf8]`, `indentfirst`,
  `graphicx`, `microtype` e `\usepackage[alf]{abntex2cite}`.
- Ordem: pré-textuais (`\pretextual`: capa, folha de rosto, folha de aprovação,
  resumo, abstract, sumário), textuais (`\textual`: introdução, desenvolvimento,
  conclusão) e pós-textuais (`\postextual`: referências, apêndices/anexos).
- Citações e referências via `.bib` + `\cite`/`\citeonline` (padrão autor-data).
  Usar apenas fontes reais; se o usuário não indicar obras, escolher referências
  verificáveis sobre o tema.
- Todo o texto deve ser **preto, inclusive hyperlinks**. Substitua as cores azuis do
  exemplo por `\hypersetup{colorlinks=true, linkcolor=black, citecolor=black,
  filecolor=black, urlcolor=black}`.
- Limite de **6 referências** por trabalho, e **todas em português** (não incluir
  obras em outro idioma, nem traduções citadas pelo título original).
- Em livros, o `year` do `.bib` é o ano da **edição específica da editora
  escolhida**, não o ano original da obra. Ex.: uma obra de Lênin publicada pela
  Editora X em 2024 entra como `year = {2024}`, com `publisher = {Editora X}`.

## Ambiente e compilação
- abnTeX2 v-1.9.7 já está instalado no sistema (`kpsewhich abntex2.cls` aponta para
  `/usr/share/texmf-dist/...`). A cópia em `abntex2/` é referência: **não editar**
  (é o upstream, licença LPPL) nem duplicar `.cls`/`.sty`/`.bst` no projeto.
- Compilar com `latexmk -pdf -interaction=nonstopmode arquivo.tex` — ele já encadeia
  pdflatex e bibtex. Verificado com o modelo de trabalho acadêmico.
- Manter cada trabalho em sua própria pasta, com `main.tex` e `referencias.bib`,
  para evitar `.aux`/`.bbl` misturados.
