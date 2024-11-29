# Complemento "Informação pausada" para NVDA

## Descrição

O complemento "Informação pausada" para NVDA é uma extensão que fornece uma leitura mais detalhada e pausada das informações de controle e estado quando o foco muda entre os elementos da interface.

Essa funcionalidade foi inspirada no leitor de tela brasileiro “Virtual Vision”, conhecido por sua forma lenta de anunciar informações, melhorando a compreensão do usuário.

Este complemento geralmente deveria ser usado com o [sintetizador DeltaTalk](https://cld.pt/dl/download/2fbe0f2a-3a24-41f3-96f5-9ff9a5a88b07/DeltaTalk%20TTS.exe?dl=true) para garantir uma experiência de leitura completa semelhante ao Virtual Vision, mas é perfeitamente compatível com qualquer outro sintetizador usado pelo NVDA.

## Nota importante
A leitura pausada é baseada apenas no nível de pontuação. Hífens são adicionados para pausar a leitura das informações. Se o nível de pontuação for definido acima de "alguns", os hífens serão lidos em voz alta.

Da mesma forma, se os símbolos (especificamente o hífen) não forem ajustados corretamente na caixa de diálogo de pronúncia de pontuação/símbolos, as pausas poderão não ocorrer.

Para garantir que as pausas funcionem conforme o esperado, vá para a caixa de diálogo de pronúncia de pontuação/símbolos e certifique-se de que o hífen esteja configurado para ser enviado ao sintetizador quando estiver abaixo do nível do símbolo.

## Características

* Anúncio de tipos e estados de controle: O complemento anuncia o tipo de controle (por exemplo, "caixa de seleção", "botão de opção", "menu", "caixa de edição") e o seu estado (por exemplo, "marcado", "pressionado" , "indisponível", "ocupado").
* O anúncio é feito de forma pausada, semelhante ao que era feito pelo leitor de tela Virtual Vision.

## Uso

Após a instalação, o complemento funciona automaticamente, permitindo uma leitura mais detalhada e pausada das informações sobre os tipos e estados dos controles. Nenhuma configuração adicional é necessária.

### Opções de configuração

Conforme mencionado, nenhuma configuração adicional é necessária ao usar o complemento. As configurações padrão fornecem uma experiência de leitura de tela e navegação no Windows muito semelhante à do Virtual Vision, especialmente quando este complemento é usado com o sintetizador DeltaTalk.

No entanto, as seguintes opções de configuração, que permitem ajustar a operação do complemento ao seu gosto ou necessidades, estão disponíveis na categoria "Informação pausada" na caixa de diálogo de configurações do NVDA:

* Permitir que o complemento traduza os nomes dos tipos e estados de controle: Se esta opção estiver marcada, o complemento usará um dicionário interno para traduzir os nomes dos tipos e estados de controle. Caso contrário, serão utilizadas as traduções internas do NVDA.
* Extensão de mensagens: Este grupo de botões de opção controla a quantidade de informações a serem faladas.
    * Curtas: Somente informações essenciais de navegação do NVDA serão faladas.
    * Médias: Além das informações essenciais de navegação do NVDA, mais algumas informações serão adicionadas pelo complemento. Por exemplo, quando um objeto possui uma tecla de atalho associada, você ouvirá "atalho" antes que a tecla de atalho seja anunciada. Você também ouvirá a informação "valor" antes de anunciar o valor dos controles deslizantes e das barras de rolagem.
    * Longas: O complemento adicionará outro conjunto de informações além dos anteriores. Ao navegar pelos itens de uma lista, itens da árvore ou itens de menu, você ouvirá as informações correspondentes de acordo com o tipo de item. O complemento também irá notificá-lo sempre que uma janela for ativada. Esta é a configuração padrão.

## Problemas conhecidos

* Nas páginas da web, o comportamento do complemento pode ser imprevisível. Por enquanto, a leitura pausada nem sempre funciona conforme o esperado e os objetos são lidos repetidamente.
* Em alguns casos, o anúncio do estado pode falhar ou estar incorreto.
    * Quando uma caixa de seleção está marcada, desmarcá-la faz com que o estado “marcado” seja anunciado incorretamente.
    * Quando um botão de alternância é pressionado ou um item da lista é selecionado, desativar o botão ou desmarcar o item não os anuncia.
    * Essa falha ocorre apenas na primeira vez que uma caixa de seleção é desmarcada, um botão de alternância  é desativado ou um item da lista  é desmarcado com a Barra de espaço ou Control+Barra de espaço.
    * Para ter certeza, você pode usar o atalho NVDA+Tab para que a informação seja repetida pelo NVDA. Neste caso, o estado será anunciado corretamente.
* Em alguns tipos de menus, como os do Thunderbird, a leitura fica um pouco estranha. A informação "submenu" é anunciada diversas vezes, mesmo quando não é necessário.
* O anúncio de janelas ativas faz com que, ao focar em qualquer parte da barra de tarefas, o primeiro item não seja anunciado. Isso também se aplica ao alternador de tarefas, acessível com Alt+Tab.

## Desenvolvimento Futuro

Este complemento foi criado como um protótipo. Quando o complemento do sintetizador DeltaTalk para o NVDA estiver totalmente desenvolvido, a funcionalidade deste protótipo será incluída como parte do complemento.

Agradecimentos especiais ao Chat GPT pela exaustiva colaboração no desenvolvimento deste protótipo, e também ao Claude pela ajuda nos ajustes adicionais que melhoraram muito o seu funcionamento.

## Histórico de alterações

### Versão 1.2

* Versão de teste privada, lançada inicialmente como 1.1 e posteriormente atualizada para 1.2.
* Foi criada uma nova opção de configuração que permite escolher se o complemento deve ou não traduzir os nomes dos tipos e estados de controle.
* Foi implementada uma lógica de níveis de extensão de mensagens - longas, médias e curtas. No nível longo (padrão), todas as informações possíveis serão faladas. No nível médio, algumas informações serão suprimidas e no nível curto, apenas as informações essenciais serão faladas.

### Versão 1.1

* Foi criada uma nova interface para o complemento, com o primeiro conceito de opções de configuração.
* Corrigido um problema em que a descrição de determinados objetos e o conteúdo de algumas caixas de diálogo não eram lidos.
* Corrigido um problema em que o valor da barra de progresso não era lido automaticamente.
* Foi corrigido um erro onde não era possível focar corretamente nos links contidos em mensagens de e-mail e páginas da web.
* Corrigido um problema com a leitura de células do Excel.
* Foi criada uma lógica para verificar se o estado somente leitura é relevante para evitar anúncios desnecessários.

### Versão 1.0

* Versão completamente reescrita do protótipo inicial, com diversas correções de bugs.
* Foi criado um dicionário completo com os nomes dos tipos e estados de controle, com suas respectivas traduções.
* A documentação foi reescrita e atualizada.

### Versão 0.1

* Protótipo inicial, criado com poucos recursos e ainda pouco funcional.
* Criação de documentação inicial.