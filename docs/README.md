# Documentação (leitura para agentes)

Os manuais oficiais do abnTeX2 v-1.9.7 em PDF foram convertidos para Markdown
para leitura e busca por `grep`. O conteúdo é o mesmo dos PDFs em `abntex2/doc/`.

- `referencia-rapida.md` — comece por aqui: preâmbulo, macros de dados, elementos
  pré/textuais/pós-textuais e comandos mais usados, com trechos verificados nos
  exemplos oficiais.
- `manuais/abntex2.md` — manual da classe: opções, estrutura ABNT, capa, folha de
  rosto, aprovação, resumos, sumário, fontes, margens, internacionalização.
- `manuais/abntex2cite.md` — manual de citações e referências (NBR 10520 e 6023):
  `\cite`, `\citeonline`, `\apud`, `\footcite`, opções do pacote e formato `.bib`.
- `manuais/abntex2cite-alf.md` — detalhes do estilo autor-data (alfabético).

Para regenerar os `.md` a partir dos PDFs: `python3 scripts/pdf_to_md.py`.
Os manuais convertidos preservam a quebra de linha e a hifenização do PDF; ao citar
um trecho, confira no `.tex` de exemplo correspondente se o comando é aquele mesmo.

A fonte de verdade para **estrutura de documento** continua sendo o `.tex` do
exemplo adequado em `abntex2/doc/examples/`. Os manuais servem para tirar dúvida
de comando/opção, não para copiar estrutura.
