# Extra “Informação Pausada” para NVDA

## Descrição

O extra “Informação Pausada” para NVDA é uma extensão que proporciona uma leitura mais detalhada e pausada das informações dos controlos e estados quando o foco muda entre elementos da interface.

Esta funcionalidade foi inspirada no leitor de ecrã brasileiro “Virtual Vision”, conhecido pela sua forma pausada de anunciar a informação, melhorando a compreensão do utilizador.

Este extra é suposto ser utilizado com o [sintetizador DeltaTalk](https://cld.pt/dl/download/2fbe0f2a-3a24-41f3-96f5-9ff9a5a88b07/DeltaTalk%20TTS.exe?dl=true) para garantir uma experiência de leitura completa semelhante à do Virtual Vision, mas é perfeitamente compatível com qualquer outro sintetizador que esteja a ser utilizado pelo NVDA.

## Nota importante

A leitura pausada baseia-se exclusivamente no nível de pontuação. São adicionados hífenes para pausar a leitura da informação. Se o nível de pontuação estiver definido para algo acima de “alguns”, os hífenes serão lidos em voz alta.

Da mesma forma, se os símbolos (especificamente o hífen) não estiverem corretamente ajustados no diálogo de pronúncia da pontuação/símbolo, as pausas podem não ocorrer.

Para garantir que as pausas funcionam como esperado, vá ao diálogo de pronúncia da pontuação/símbolo e certifique-se de que o hífen está definido para ser enviado para o sintetizador quando está abaixo do nível de símbolos.

## Funcionalidades

* Anúncio dos tipos e estados de controlo: O extra anuncia o tipo de controlo (por exemplo “caixa de verificação”, “botão de opção”, “menu”, “caixa de edição”) e o seu estado (por exemplo “marcado”, “pressionado”, “indisponível”, “ocupado”).
* O anúncio é feito de forma pausada, à semelhança do que era feito pelo leitor de ecrã Virtual Vision.

## Utilização

Após a instalação, o extra funciona automaticamente, permitindo uma leitura mais detalhada e pausada das informações sobre os tipos e os estados dos controlos. Não é necessária qualquer configuração adicional.

### Opções de configuração

Como mencionado, não é necessária qualquer configuração adicional quando se utiliza o extra. As configurações predefinidas fornecem uma experiência de leitura de ecrã e de navegação no Windows muito semelhante à do Virtual Vision, especialmente quando este extra é usado com o sintetizador DeltaTalk.

No entanto, as seguintes opções de configuração, que lhe permitem ajustar o funcionamento do extra ao seu gosto ou às suas necessidades, estão disponíveis a partir da categoria “Informação pausada” no diálogo de configurações do NVDA:

* Anunciar itens de lista: Será notificado sempre que um item de lista for focado.
* Anunciar itens de vista em árvore: Será notificado sempre que um item de vista em árvore for focado.
* Anunciar itens de menu: Será notificado sempre que um item de menu for focado.
* Anunciar “valor” antes dos valores do controlo de deslize: Quando focar numa barra deslizante ou de deslocamento, anuncia a informação “valor” antes de o valor ser anunciado.
* Anunciar “atalho” antes dos atalhos de objetos: Quando um objeto tem uma tecla de atalho associada, anuncia a informação “atalho” antes de a tecla de atalho correspondente ser anunciada.

## Problemas conhecidos

* Nas páginas Web, o comportamento do extra pode ser imprevisível. por agora, a leitura pausada nem sempre funciona como esperado e os objetos são lidos repetidamente.
* Em alguns casos, o anúncio dos estados pode falhar ou ser incorreto.
    * Quando uma caixa de verificação está marcada, desmarcá-la faz com que o estado “marcado” seja anunciado incorretamente.
    * Quando um botão de alternância é premido ou um item de lista é selecionado, a desativação do botão ou a anulação da seleção do item não os anuncia.
    * Esta falha só ocorre na primeira vez que se desmarca uma caixa de verificação, se desativa um botão de alternância ou se anula a seleção de um item de lista com a Barra de Espaço ou Control+Barra de Espaço.
    * Para ter a certeza, pode utilizar o atalho NVDA+Tab para que a informação seja repetida pelo NVDA. Neste caso, o estado será anunciado corretamente.
* Em alguns tipos de menus, como os do Thunderbird, a leitura é um pouco estranha. A informação “submenu” é anunciada várias vezes, mesmo quando não é necessária.

## Desenvolvimento Futuro

Este extra foi criado como um protótipo. Quando o extra do sintetizador DeltaTalk para o NVDA estiver totalmente desenvolvido, a funcionalidade deste protótipo será incluída como parte do extra.

Um agradecimento especial ao Chat GPT pela sua colaboração exaustiva no desenvolvimento deste protótipo, e também ao Claude pela sua ajuda nos ajustes adicionais que melhoraram muito o funcionamento.

## Histórico de alterações

### Versão 1.1

* Foi criada uma nova interface para o extra, com o primeiro conceito de opções de configuração.
* Foi corrigido um erro em que a descrição de determinados objetos e o conteúdo de algumas caixas de diálogo não eram lidos.
* Foi corrigido um erro em que o valor das barras de progresso não era lido automaticamente.
* Foi corrigido um erro em que não era possível focar corretamente os links contidos em mensagens de e-mail e páginas Web.
* Foi corrigido um problema com a leitura de células do Excel.
* Foi criada uma lógica para verificar se o estado só de leitura é relevante, a fim de evitar anúncios desnecessários.

### Versão 1.0

* Versão completamente reescrita a partir do protótipo inicial, com várias correções de erros.
* Foi criado um dicionário completo com os nomes dos tipos e estados de controlo, com as respetivas traduções, que será atualizado conforme necessário.
* A documentação foi reescrita e será atualizada regularmente.

### Versão 0.1

* Protótipo inicial, criado com muito poucos recursos e ainda não muito funcional.
* Criação da documentação inicial.
