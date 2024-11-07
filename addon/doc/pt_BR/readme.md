# Complemento "Informações pausadas" para NVDA

## Descrição

O complemento "Informações pausadas" para NVDA é uma extensão que fornece uma leitura mais detalhada e pausada das informações de controle e estado quando o foco muda entre os elementos da interface. Essa funcionalidade foi inspirada no leitor de tela brasileiro “Virtual Vision”, conhecido por sua forma lenta de anunciar informações, melhorando a compreensão do usuário.

## Características

* Anúncio de tipos e estados de controle: O complemento anuncia o tipo de controle (por exemplo, "caixa de seleção", "botão de opção", "menu", "caixa de edição") e o seu estado (por exemplo, "marcado", "pressionado" , "indisponível", "ocupado").
* O anúncio é feito de forma pausada, semelhante ao que era feito pelo leitor de tela Virtual Vision.

## Uso

Após a instalação, o complemento funciona automaticamente, proporcionando uma leitura mais detalhada e pausada das informações dos tipos e status dos controles. Nenhuma configuração adicional é necessária.

## Notas

* A leitura do texto selecionado não é totalmente funcional e pode falhar em alguns casos. No entanto, ajustes foram feitos para melhorar a operação.
* Em alguns casos, o status do controle não é anunciado, por exemplo, quando uma caixa de seleção não está marcada ou um botão de alternância não está pressionado. Mais alguns ajustes serão feitos para tentar corrigir esse problema.
* Nas páginas da web, o comportamento do complemento pode ser imprevisível. Por enquanto, a leitura pausada nem sempre funciona conforme o esperado e os objetos são lidos repetidamente.
* A leitura pausada é baseada apenas no nível de pontuação, pois hifens são adicionados para pausar entre as informações de leitura. Se o grau de símbolos for definido acima de "pouco", os hifens serão lidos em voz alta.
* Da mesma forma, se os símbolos (especificamente o hífen) não forem ajustados corretamente na caixa de diálogo de pronúncia de pontuação / símbolos, as pausas poderão não ocorrer.
* Para garantir que as pausas funcionem conforme o esperado, vá para a caixa de diálogo de pronúncia da pontuação/símbolos e certifique-se de que o hífen esteja configurado para ser enviado ao sintetizador quando estiver abaixo do nível do símbolo.
* Para usuários muito avançados: Se você não quiser ouvir as expressões "item de lista", "item da árvore" e "item de menu" ao navegar pelos respectivos itens, basta abrir o código do complemento em "globalPlugins\pausingInfo .py " e modificar as linhas para "ListItem", "TreeViewItem" e "MenuItem", substituindo as frases entre aspas por um espaço, e reiniciar o NVDA após salvar o arquivo. Observe que isso só deve ser feito por usuários muito experientes! Está sendo considerada a possibilidade de implementar uma caixa de diálogo de configurações no futuro, o que permitirá ao usuário personalizar o complemento de acordo com seus gostos ou necessidades.

## Desenvolvimento Futuro

Este complemento foi criado como um protótipo. Quando o complemento do sintetizador DeltaTalk para o NVDA estiver totalmente desenvolvido, a funcionalidade deste protótipo será incluída como parte do complemento.

Agradecimentos especiais ao Chat GPT pela exaustiva colaboração no desenvolvimento deste protótipo, e também ao Claude pela ajuda nos ajustes adicionais que melhoraram muito o seu funcionamento.

## Histórico de alterações

### Versão 1.0

* Versão completamente reescrita do protótipo inicial, com diversas correções de bugs.
* Foi criado um dicionário completo com os nomes dos tipos de controle e estados, com suas respectivas traduções, que serão atualizadas conforme necessário.
* A documentação foi reescrita e será atualizada regularmente.

### Versão 0.1

* Protótipo inicial, criado com poucos recursos e ainda pouco funcional.
* Criação de documentação inicial.