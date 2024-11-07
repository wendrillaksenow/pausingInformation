# Extra “Informação Pausada” para NVDA

## Descrição

O extra “Informação Pausada” para NVDA é uma extensão que proporciona uma leitura mais detalhada e pausada das informações dos controlos e estados quando o foco muda entre elementos da interface.

Esta funcionalidade foi inspirada no leitor de ecrã brasileiro “Virtual Vision”, conhecido pela sua forma pausada de anunciar a informação, melhorando a compreensão do utilizador.

## Funcionalidades

* Anúncio dos tipos e estados de controlo: O extra anuncia o tipo de controlo (por exemplo “caixa de verificação”, “botão de opção”, “menu”, “caixa de edição”) e o seu estado (por exemplo “marcado”, “pressionado”, “indisponível”, “ocupado”).
* O anúncio é feito de forma pausada, à semelhança do que era feito pelo leitor de ecrã Virtual Vision.

## Utilização

Após a instalação, o extra funciona automaticamente, permitindo uma leitura mais detalhada e pausada das informações sobre os tipos e os estados dos controlos. Não é necessária qualquer configuração adicional.

## Notas

* A leitura do texto selecionado não é totalmente funcional e pode falhar em alguns casos. No entanto, foram efetuados ajustes para melhorar o funcionamento.
* Em alguns casos, o estado do controlo não é anunciado, por exemplo, quando uma caixa de verificação não está marcada ou um botão de comutação não está pressionado. Serão efetuados mais alguns ajustes para tentar corrigir este problema.
* Nas páginas Web, o comportamento do extra pode ser imprevisível. por agora, a leitura pausada nem sempre funciona como esperado e os objetos são lidos repetidamente.
* A leitura pausada baseia-se exclusivamente no nível de pontuação, uma vez que os hífenes são adicionados para pausar a leitura da informação. Se o nível de pontuação estiver definido para algo acima de "alguns", os hífenes serão lidos em voz alta.
* Da mesma forma, se os símbolos (especificamente o hífen) não estiverem corretamente ajustados no diálogo de pronúncia da pontuação/símbolo, as pausas podem não ocorrer.
* Para garantir que as pausas funcionam como esperado, vá ao diálogo de pronúncia da pontuação/símbolo e certifique-se de que o hífen está definido para ser enviado para o sintetizador quando está abaixo do nível de símbolos.
* Para utilizadores muito avançados: Se não quiser ouvir a expressão "item de lista", "item da vista em árvore" e "item de menu" quando percorrer os respectivos itens, basta abrir o código do extra em "globalPlugins\pausingInfo.py" e modificar as linhas para "ListItem", "TreeViewItem" e "MenuItem", substituindo as frases entre aspas por um espaço e reiniciar o NVDA após guardar o ficheiro. Tenha em atenção que isto só deve ser feito por utilizadores muito experientes! Está a ser considerada a possibilidade de implementar, no futuro, um diálogo de configurações, que permitirá ao utilizador personalizar o extra de acordo com os seus gostos ou necessidades.

## Desenvolvimento Futuro

Este extra foi criado como um protótipo. Quando o extra do sintetizador DeltaTalk para o NVDA estiver totalmente desenvolvido, a funcionalidade deste protótipo será incluída como parte do extra.

Um agradecimento especial ao Chat GPT pela sua colaboração exaustiva no desenvolvimento deste protótipo, e também ao Claude pela sua ajuda nos ajustes adicionais que melhoraram muito o funcionamento.

## Histórico de alterações

### Versão 1.0

* Versão completamente reescrita a partir do protótipo inicial, com várias correções de erros.
* Foi criado um dicionário completo com os nomes dos tipos e estados de controlo, com as respetivas traduções, que será atualizado conforme necessário.
* A documentação foi reescrita e será atualizada regularmente.

### Versão 0.1

* Protótipo inicial, criado com muito poucos recursos e ainda não muito funcional.
* Criação da documentação inicial.
