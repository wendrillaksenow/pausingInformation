# Extra “Informação Pausada” para NVDA

## Descrição

O extra “Informação Pausada” para NVDA é uma extensão que proporciona uma leitura mais detalhada e pausada das informações dos controlos e estados quando o foco muda entre elementos da interface.

Esta funcionalidade foi inspirada no leitor de ecrã brasileiro “Virtual Vision”, conhecido pela sua forma pausada de anunciar a informação, melhorando a compreensão do utilizador.

Este extra é suposto ser utilizado com o [sintetizador DeltaTalk](https://intervox.nce.ufrj.br/~wendrill/progs/sintets/DeltaTalk%20TTS.exe) para garantir uma experiência de leitura completa semelhante à do Virtual Vision, mas é perfeitamente compatível com qualquer outro sintetizador que esteja a ser utilizado pelo NVDA.

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

No entanto, as seguintes opções de configuração, que lhe permitem ajustar o funcionamento do extra ao seu gosto ou às suas necessidades, estão disponíveis a partir da categoria “Informação Pausada” no diálogo de configurações do NVDA:

* Ativar a leitura pausada dos tipos e estados de controlo: Se desmarcar esta opção, o extra será completamente desativado e todas as outras opções de configuração ficarão indisponíveis. Também pode ativar/desativar o extra utilizando o atalho NVDA+Shift+P. Este atalho pode ser modificado a partir do diálogo “Definir comandos” do NVDA, categoria “Informação Pausada”.
* Permitir que o extra traduza os nomes dos tipos e estados dos controlos: Se esta opção estiver marcada, o Extra utilizará um dicionário interno para traduzir os nomes dos tipos e estados dos controlos. Caso contrário, serão utilizadas as traduções internas do NVDA.
* Extensão da mensagem: Este grupo de botões de opção controla a quantidade de informação a ser falada.
    * Curta: Apenas as informações de navegação essenciais do NVDA serão faladas.
    * Média: Para além das informações de navegação essenciais do NVDA, serão adicionadas mais algumas informações pelo extra. Por exemplo, quando um objeto tem uma tecla de atalho associada, ouvirá a informação “atalho” antes de a tecla de atalho ser anunciada. Também ouvirá a informação “valor” antes de anunciar o valor dos controlos de deslize e das barras de deslocamento.
    * Longa: O extra adicionará outro conjunto de informações para além das anteriores. Ao navegar pelos itens de uma lista, vista de árvore ou menus, ouvirá a informação correspondente de acordo com o tipo de item. O extra também o avisará sempre que uma janela for ativada. Esta é a configuração predefinida.
    * Personalizada: Com esta opção, pode controlar individualmente todas as informações anunciadas pelo extra.

#### Configurações para o nível personalizado

Ao definir o nível de extensão da mensagem como “Personalizado”, pode ajustar individualmente todas as informações anunciadas pelo extra, por exemplo, pode desativar as informações que não quer ou não precisa que sejam anunciadas. Pode fazê-lo através do botão “Configurar”. Este botão só está disponível quando o nível de extensão da mensagem personalizada está selecionado. Ao clicar neste botão, abre-se um diálogo de configuração para o nível personalizado, com as seguintes opções:

* Selecionar os controlos a anunciar: Nesta lista, é possível ativar ou desativar todos os tipos de controlo suportados pelo extra. Para os controlos desativados, apenas serão anunciados o nome e o estado (se aplicável).

* Outras mensagens adicionais: Este grupo de controlos contém as seguintes opções:
    * Anunciar janelas ativas: Anuncia sempre que uma janela é ativada.
    * Anunciar “atalho” antes das teclas de atalho dos objetos: Quando um objeto tem uma tecla de atalho associada, anuncia a informação “atalho” antes de a tecla de atalho correspondente ser anunciada.
    * Anunciar “valor” antes dos valores do controlo de deslize e da barra de deslocamento: Quando focar numa barra deslizante ou de deslocamento, anuncia a informação “valor” antes de o valor ser anunciado.

## Problemas conhecidos

* Nas páginas Web, o comportamento do extra pode ser imprevisível. por agora, a leitura pausada nem sempre funciona como esperado e os objetos são lidos repetidamente.
* Em alguns casos, o anúncio dos estados pode falhar ou ser incorreto.
    * Quando uma caixa de verificação está marcada, desmarcá-la faz com que o estado “marcado” seja anunciado incorretamente.
    * Quando um botão de alternância é premido ou um item de lista é selecionado, a desativação do botão ou a anulação da seleção do item não os anuncia.
    * Esta falha só ocorre na primeira vez que se desmarca uma caixa de verificação, se desativa um botão de alternância ou se anula a seleção de um item de lista com a Barra de Espaço ou Control+Barra de Espaço.
    * Para ter a certeza, pode utilizar o atalho NVDA+Tab para que a informação seja repetida pelo NVDA. Neste caso, o estado será anunciado corretamente.
* Em alguns tipos de menus, como os do Thunderbird, a leitura é um pouco estranha. As informações “submenu” e “indisponível” são anunciadas várias vezes, mesmo quando não é necessário. Nestes casos, até que seja encontrada uma solução para este problema, recomenda-se desativar temporariamente o extra através da tecla de atalho ao navegar pelos menus do Thunderbird e outros menus semelhantes.
* Em alguns tipos de caixas de diálogo que não têm um título associado, o seu conteúdo não é lido automaticamente pelo extra.
* O anúncio de janelas ativas, em certos casos, faz com que esta informação seja anunciada incorretamente, por exemplo, ao abrir uma caixa combinada com o atalho Alt+Seta para baixo ou ao abrir um menu de contexto como o do Google Chrome.

## Integração com o DeltaTalk

O sintetizador DeltaTalk em formato dedicado para o NVDA já está totalmente desenvolvido, portanto, a funcionalidade deste extra foi integrada ao sintetizador como um módulo chamado “Modo Virtual Vision”. Por isso, esta será a última versão independente deste extra.

Um agradecimento especial ao Chat GPT pela sua colaboração exaustiva no desenvolvimento deste extra como um protótipo inicial, e também ao Claude pela sua ajuda nos ajustes adicionais que melhoraram muito o funcionamento, e ao Groc pela sua ajuda na correção dos últimos erros antes do lançamento da última versão.

Um agradecimento especial também a todas as pessoas que experimentaram este protótipo e contribuíram com relatórios de erros e sugestões muito valiosas.

## Histórico de alterações

### Versão 1.5

* O estado “internal_link” (que identifica os links para a mesma página) foi acrescentado à lista dos estados a anunciar.
* Foram também acrescentados mais alguns controlos à lista de tipos de controlo a anunciar.
* Foi criada uma lógica que verifica a presença da versão antiga do extra e remove-a antes de instalar esta nova versão.
* O extra está agora disponível na loja de extras do NVDA. Basta procurar por “Informação Pausada”.
* Foi corrigido um problema em que as configurações para o nível de extensão da mensagem personalizada se perdiam quando o NVDA era reiniciado ou quando o seu idioma era alterado.
* O código do extra foi simplificado e as partes desnecessárias e repetidas foram eliminadas para facilitar a manutenção.
* A funcionalidade do extra foi integrada no DeltaTalk como o “Modo Virtual Vision”, pelo que esta será a última versão autónoma.

### Versão 1.4

* Foi corrigido um erro com o anúncio de janelas ativas que fazia com que, ao focar a barra de tarefas ou alternar entre tarefas com o atalho Alt+Tab, o primeiro item não fosse anunciado. Este problema também afectava alguns itens em janelas normais, que eram ignorados.

### Versão 1.3

* Primeira versão de lançamento oficial.
* Foi implementado um nível de extensão de mensagem personalizado, que permite controlar individualmente todas as informações anunciadas pelo extra.
* Foi criada uma nova opção de configuração para desativar completamente o extra.
* Também foi implementada uma tecla de atalho para ativar/desativar, que é especialmente útil para desativar temporariamente o extra em determinados casos.

### Versão 1.2

* Versão de teste privada, inicialmente lançada como 1.1 e posteriormente atualizada para 1.2.
* Foi criada uma nova opção de configuração que lhe permite escolher se o extra deve ou não traduzir os nomes dos tipos e estados dos controlos.
* Foi implementada uma lógica de níveis de extensão da mensagem - longa, média e curta. No nível longo (predefinição), todas as informações possíveis serão faladas. No nível médio, algumas informações serão suprimidas e no nível curto, apenas as informações essenciais serão faladas.

### Versão 1.1

* Foram criados novos métodos de leitura dos estados de controlo para corrigir um problema em que certos estados não eram lidos.
* Foi criada uma nova interface para o extra, com o primeiro conceito de opções de configuração.
* Foi corrigido um erro em que a descrição de determinados objetos e o conteúdo de algumas caixas de diálogo não eram lidos.
* Foi corrigido um erro em que o valor das barras de progresso não era lido automaticamente.
* Foi corrigido um erro em que não era possível focar corretamente os links contidos em mensagens de e-mail e páginas Web.
* Foi corrigido um problema com a leitura de células do Excel.
* Foi criada uma lógica para verificar se o estado só de leitura é relevante, a fim de evitar anúncios desnecessários.

### Versão 1.0

* Versão completamente reescrita a partir do protótipo inicial, com várias correções de erros.
* Foi criado um dicionário completo com os nomes dos tipos e estados de controlo, com as respetivas traduções.
* A documentação foi reescrita e atualizada.

### Versão 0.1

* Protótipo inicial, criado com muito poucos recursos e ainda não muito funcional.
* Criação da documentação inicial.