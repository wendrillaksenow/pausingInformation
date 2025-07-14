# Complemento "Informação Pausada" para NVDA

## Descrição

O complemento "Informação Pausada" para NVDA é uma extensão que fornece uma leitura mais detalhada e pausada das informações de controle e estado quando o foco muda entre os elementos da interface.

Essa funcionalidade foi inspirada no leitor de tela brasileiro "Virtual Vision", conhecido por sua forma lenta de anunciar informações, melhorando a compreensão do usuário.

Este complemento geralmente deveria ser usado com o [sintetizador DeltaTalk](https://intervox.nce.ufrj.br/~wendrill/progs/sintets/DeltaTalk%20TTS.exe) para garantir uma experiência de leitura completa semelhante à do Virtual Vision, mas é perfeitamente compatível com qualquer outro sintetizador usado pelo NVDA.

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

No entanto, as seguintes opções de configuração, que permitem ajustar a operação do complemento ao seu gosto ou necessidades, estão disponíveis na categoria "Informação Pausada" na caixa de diálogo de configurações do NVDA:

* Habilitar leitura pausada de tipos e estados de controle: Ao desmarcar esta opção, o complemento será completamente desabilitado e todas as outras opções de configuração ficarão indisponíveis. Você também pode ativar/desativar o complemento usando o atalho NVDA+Shift+P. Este atalho pode ser modificado na caixa de diálogo "Definir Comandos" do NVDA, categoria "Informação Pausada".
* Permitir que o complemento traduza os nomes dos tipos e estados de controle: Se esta opção estiver marcada, o complemento usará um dicionário interno para traduzir os nomes dos tipos e estados de controle. Caso contrário, serão utilizadas as traduções internas do NVDA.
* Extensão de mensagens: Este grupo de botões de opção controla a quantidade de informações a serem faladas.
    * Curtas: Somente informações essenciais de navegação do NVDA serão faladas.
    * Médias: Além das informações essenciais de navegação do NVDA, mais algumas informações serão adicionadas pelo complemento. Por exemplo, quando um objeto possui uma tecla de atalho associada, você ouvirá "atalho" antes que a tecla de atalho seja anunciada. Você também ouvirá a informação "valor" antes de anunciar o valor dos controles deslizantes e das barras de rolagem.
    * Longas: O complemento adicionará outro conjunto de informações além dos anteriores. Ao navegar pelos itens de uma lista, itens da árvore ou itens de menu, você ouvirá as informações correspondentes de acordo com o tipo de item. O complemento também irá notificá-lo sempre que uma janela for ativada. Esta é a configuração padrão.
    * Personalizadas: Com esta opção você pode controlar individualmente todas as informações anunciadas pelo complemento.

#### Configurações para o nível personalizado

Ao definir o nível de extensão de mensagens como "Personalizadas", você pode ajustar individualmente todas as informações anunciadas pelo complemento, por exemplo, pode desabilitar informações que não deseja ou não precisa que sejam anunciadas. Você pode fazer isso usando o botão "Configurar". Este botão só está disponível quando o nível de extensão de mensagens personalizado é selecionado. Clicar neste botão abre uma caixa de diálogo de configuração para o nível personalizado, com as seguintes opções:

* Selecione os controles a serem anunciados: Nesta lista é possível ativar ou desativar todos os tipos de controles suportados pelo complemento. Para controles desativados, apenas o nome e o estado (se aplicável) serão anunciados.

* Outras mensagens adicionais: Este grupo de controles contém as seguintes opções:
    * Anunciar janelas ativas: Anuncia sempre que uma janela é ativada.
    * Anunciar "atalho" antes das teclas de atalho dos objetos: Quando um objeto possui uma tecla de atalho associada, o complemento anuncia a informação "atalho" antes que a tecla de atalho correspondente seja anunciada.
    * Anunciar "valor" antes dos valores do controle deslizante e da barra de rolagem: ao focar em um controle deslizante ou barra de rolagem, o complemento anuncia a informação "valor" antes que o valor seja anunciado.

## Problemas conhecidos

* Nas páginas da web, o comportamento do complemento pode ser imprevisível. Por enquanto, a leitura pausada nem sempre funciona conforme o esperado e os objetos são lidos repetidamente.
* Em alguns casos, o anúncio do estado pode falhar ou estar incorreto.
    * Quando uma caixa de seleção está marcada, desmarcá-la faz com que o estado "marcado" seja anunciado incorretamente.
    * Quando um botão de alternância é pressionado ou um item da lista é selecionado, desativar o botão ou desmarcar o item não os anuncia.
    * Essa falha ocorre apenas na primeira vez que uma caixa de seleção é desmarcada, um botão de alternância  é desativado ou um item da lista  é desmarcado com a Barra de espaço ou Control+Barra de espaço.
    * Para ter certeza, você pode usar o atalho NVDA+Tab para que a informação seja repetida pelo NVDA. Neste caso, o estado será anunciado corretamente.
* Em alguns tipos de menus, como os do Thunderbird, a leitura fica um pouco estranha. As informações "submenu" e "Indisponível" são anunciadas diversas vezes, mesmo quando não é necessário. Nestes casos, até que seja encontrada uma solução para este problema, é recomendado desativar temporariamente o complemento através da tecla de atalho ao navegar nos menus do Thunderbird e outros menus semelhantes.
* Em alguns tipos de caixas de diálogo que não possuem um título associado, seu conteúdo não é lido automaticamente pelo complemento.
* O anúncio de janelas ativas faz com que essa informação seja anunciada incorretamente em certos casos, por exemplo, ao abrir uma caixa de combinação com o atalho Alt+Seta para baixo ou ao abrir um menu de contexto como o do Google Chrome.

## Integração com o Deltatalk

O sintetizador DeltaTalk em formato dedicado para o NVDA já está completamente desenvolvido, portanto a funcionalidade deste complemento foi integrada ao sintetizador como um módulo chamado "Modo Virtual Vision". Assim, esta será a última versão independente deste complemento.

Agradecimentos especiais ao Chat GPT pela exaustiva colaboração no desenvolvimento deste complemento como um protótipo inicial, e também ao Claude pela ajuda nos ajustes adicionais que melhoraram muito o seu funcionamento, e ao Groc por sua ajuda na correção dos últimos bugs antes do lançamento da versão mais recente.

Agradecimentos especiais também a todas as pessoas que experimentaram este protótipo e contribuíram com relatórios de bugs e sugestões muito valiosas.

## Histórico de alterações

### Versão 1.5

* O estado "internal_link" (que identifica links para a mesma página) foi adicionado à lista de estados a serem anunciados.
* Mais alguns controles também foram adicionados à lista de tipos de controle a serem anunciados.
* Uma lógica foi criada para verificar a presença da versão antiga do complemento e removê-la antes de instalar esta nova versão.
* O complemento agora está disponível na loja de complementos do NVDA. Basta procurar por "Informação Pausada".
* Corrigido um problema em que as Configurações para o nível de extensão de mensagem personalizada eram perdidas quando o NVDA era reiniciado ou quando seu idioma era alterado.
* O código do complemento foi simplificado e partes desnecessárias e repetidas foram removidas para facilitar a manutenção.
* A funcionalidade do complemento foi integrada ao DeltaTalk como "Modo Virtual Vision", portanto, esta será a última versão autônoma.

### Versão 1.4

* Corrigido um erro com o anúncio de janelas ativas em que ao focar na barra de tarefas ou alternar entre tarefas com o atalho Alt+Tab, o primeiro item não era anunciado. Esse problema também afetava alguns itens das janelas normais, que eram ignorados.

### Versão 1.3

* Primeira versão oficial de lançamento.
* Foi implementado um nível de extensão de mensagem personalizado, que permite controlar individualmente todas as informações anunciadas pelo complemento.
* Uma nova opção de configuração foi criada para desabilitar completamente o complemento.
* Uma tecla de atalho para ativar/desativar também foi implementada, o que é especialmente útil para desativar temporariamente o complemento em certos casos.

### Versão 1.2

* Versão de teste privada, lançada inicialmente como 1.1 e posteriormente atualizada para 1.2.
* Foi criada uma nova opção de configuração que permite escolher se o complemento deve ou não traduzir os nomes dos tipos e estados de controle.
* Foi implementada uma lógica de níveis de extensão de mensagens - longas, médias e curtas. No nível longo (padrão), todas as informações possíveis serão faladas. No nível médio, algumas informações serão suprimidas e no nível curto, apenas as informações essenciais serão faladas.

### Versão 1.1

* Novos métodos de leitura de estados de controle foram criados para corrigir um problema em que determinados estados não eram lidos.
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