# Exon Finder

Se você trabalha (ou trabalhou) com biologia molecular ou bioinformática, sabe o quão difícil (e até mesmo chato) é encontrar os 12 exons de um gene com 180 mil letras. Encontrar a sequência no NCBI, tratar a informação em um documento Word, ver onde começa e termina o primeiro de 12 exons e fazer isso para os exons restantes...uma tarefa que (para mim) levava cerca de 15 minutos para cada gene! Um tempo razoável para uma tarefa teoricamente simples. Sabendo disso (e também uma preguiça minha), resolvi desenvolver um software que fizesse essa tarefa para mim.

### Mas afinal de contas, o que é o *Exon Finder*?

O *Exon Finder* é um *software* de bioinformática desenvolvido para auxiliar na procura de exons em genes, independente do tamanho e da quantidade de exons. Ou seja, o tempo para a procura de exons que levavá cerca de 15 minutos caiu para um pouco mais de 15 segundos!

### E como o *Exon Finder* funciona?

O Exon Finder precisa basicamente de duas coisas: um ID da sequência de DNA do banco de dados do NCBI e o local para salvar o arquivo .docx com os exons marcados. A interface gráfica é bem simples:

![foto_1](https://user-images.githubusercontent.com/91161693/154067797-e0a33b72-4913-4d9a-a7c5-637a8e16358f.png)

O campo **ID Sequência** serve para informar o ID da sequência de DNA do banco de dados do NCBI (a identificação que está na linha *VERSION* na página do gene). O botão que contém a imagem da pasta é liberado somente depois que o botão Pesquisar for clicado e a identificação do gene estiver correta. Quando o botão com a pasta for clicado, abrirá um nova janela para selecionar o destino do arquivo **.docx**. E sim, o arquivo já será salvo nessa extensão, não precisando digitá-la quando for nomear o arquivo. Depois de feito isso, o botão **Salvar** será habilitado para salvar a sequência editada no local informado e com o nome desejado.

### Vantagens do *Exon Finder*

Como esse repositório contém a segunda versão do *software*, darei uma breve explicação do que continha na primeira versão. Na versão 1 do programa, era necessário baixar a sequência de DNA em um arquivo no formato **.fasta** ou **.txt**, tratar esse arquivo para que o programa conseguisse lê-lo e depois de tudo isso, ainda informar as posições iniciais e finais de cada exon do gene. Ou seja, a única parte automática era a criação do documento **.docx**; que era feita em menos de 10 segundos dependendo do tamanho da sequência de DNA. Porém, levavá mais de 5 minutos para fazer o processo antes da criação do documento Word. E por isso que a segunda versão do *Exon Finder* foi criada.

Na versão 2 do programa, tirando o fato de que não é mais necessário baixar a sequência de DNA, o tempo de execução da tarefa diminui drasticamente. O tempo para editar o arquivo **.docx** continua sendo semelhante, uma vez que isso depende do tamanho da sequência. Porém, como não é mais necessário informar onde começa e termina cada exon, o tempo de execução completa da tarefa depende somente do processador do computador.

Vejamos dois exemplos:

  1. O gene HBB (o menor gene funcional humano) possui 10.106 pares de base e 3 exons. Com a primeira versão do Exon Finder, o tempo para editar o arquivo .docx é de 0,220 segundos. Na senda versão do software esse tempo é de 0,8 segundos, isto é: 4 vezes mais "lento" em comparação com a primeira versão. Mas neste caso não foi necessário baixar nenhum documento nem escrever as posições iniciais e finais dos exons.
  2. O gene ALB1 possui 180.975 pares de base e 12 exons. Usando a primeira versão do software, o tempo para editar o arquivo .docx é de 10,109 segundos. Com a segunda versão do Exon Finder, o tempo para editar o arquivo .docx é de 11,7 segundos. O tempo da primeira versão é um pouco menor, mas na segunda versão não foi necessário baixar nenhum arquivo nem informar manualmente as posições dos exons.

Usar a primeira versão até que possui uma "pequena" vantagem na edição do arquivo .docx, mas antes disso é preciso tratar o arquivo para ser lido e informar as posições dos exons. Fato esse que dependendo da quantidade de exons, o tempo de execução da tarefa passa dos 5 minutos.

### Conclusão

Caso você queira saber o motivo da criação do *Exon Finder*, recomendo que leia este [artigo](https://www.linkedin.com/pulse/exon-finder-uma-ferramenta-simples-para-tarefa-chata-guilherme), lá explico direitinho o por quê. E o motivo da versão 2 (leia este [artigo](url) para maiores explicações)ter sido criada é que eu ainda tinha que fazer a maior parte do trabalho de modo manual, o que levavá um tempo considerável para genes grandes, além de aprender tecnologias novas na área da programação!
