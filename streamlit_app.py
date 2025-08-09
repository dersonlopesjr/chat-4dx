# streamlit_app.py
import streamlit as st
from groq import Groq

# --- Conteúdo do seu arquivo 4d.txt ---
CONTEUDO_4D = """
As 4 Disciplinas da Execução: Transformando Estratégia em Resultados Concretos

Em muitas organizações, a distância entre o que se planeja e o que realmente se entrega é significativa. Estratégias bem formuladas frequentemente esbarram em obstáculos quando chegam à fase de execução, seja por falta de foco, excesso de prioridades, ausência de indicadores claros ou dificuldade em manter a equipe engajada ao longo do tempo.
O modelo As 4 Disciplinas da Execução (4DX), desenvolvido por Chris McChesney, Sean Covey e Jim Huling, oferece um método comprovado para fechar essa lacuna, transformando planos em resultados tangíveis.

As 4DX são construídas sobre um princípio central: a execução eficaz exige disciplina, clareza e ritmo. No Brasil, as quatro disciplinas são popularmente apresentadas assim:

1ª Disciplina – Foco na Meta Crucialmente Importante (MCI)
A primeira disciplina começa com a definição de uma Meta Crucialmente Importante (MCI), equivalente ao Wildly Important Goal (WIG) na versão original.
O conceito é simples, mas poderoso: “Quando tudo é prioridade, nada é prioridade.”

Organizações e equipes tendem a dispersar energia tentando avançar em várias direções ao mesmo tempo. O resultado é um progresso lento e difuso. A 1ª disciplina propõe concentrar esforços em um número extremamente reduzido de metas — muitas vezes apenas uma por equipe — cuja conquista gerará o maior impacto possível.

Aplicações práticas:
- Na liderança: escolher metas que mudam o jogo, evitando objetivos genéricos ou amplos demais.
- No time de vendas: em vez de buscar “crescer em todas as regiões”, definir “aumentar em 20% as vendas no segmento X até dezembro”.
- Na educação corporativa: focar no aumento da taxa de conclusão de treinamentos críticos antes de expandir para novos programas.

Pergunta-chave: Se falharmos em tudo o mais, mas alcançarmos esta meta, teremos vencido o jogo?

2ª Disciplina – Agir nas Medidas de Direção
No Brasil, também chamadas de “indicadores de direção” ou “indicadores preditivos”, são ações ou comportamentos que influenciam diretamente a MCI e que podem ser controlados pela equipe.
A diferença fundamental em relação aos indicadores de resultado é que estes últimos mostram apenas o que já aconteceu (passado), enquanto as medidas de direção permitem atuar sobre o presente para mudar o futuro.

Aplicações práticas:
- Na saúde: se a meta é perder 5 kg em 3 meses (resultado), as medidas de direção podem ser “realizar 4 treinos de 45 minutos por semana” e “manter ingestão calórica diária abaixo de 2.000 kcal”.
- No atendimento ao cliente: se a meta é reduzir cancelamentos, a medida de direção pode ser “ligar para todos os novos clientes nas primeiras 48 horas após a compra”.
- Em projetos: substituir “entregar o projeto no prazo” por medidas como “realizar reuniões semanais de alinhamento” e “concluir entregáveis parciais nas datas definidas”.

3ª Disciplina – Manter um Placar Visível
No Brasil, a 3ª disciplina costuma ser chamada de “placar visível” ou “placar de acompanhamento”. É um painel simples, atualizado e acessível a todos, que mostra de forma clara se a equipe está vencendo ou perdendo em relação à MCI.

Características de um bom placar:
1. Simples: qualquer pessoa entende rapidamente a situação.
2. Atualizado: dados sempre recentes, preferencialmente semanais ou diários.
3. Motivador: gera senso de urgência e de conquista.

Aplicações práticas:
- Equipes comerciais: mural físico ou painel digital mostrando meta semanal, vendas realizadas e diferença a ser alcançada.
- Times de projetos: quadro kanban com status atualizado das tarefas-chave ligadas à MCI.
- Escolas e universidades: painel que mostra avanço de alunos em trilhas de aprendizagem estratégicas.

4ª Disciplina – Criar uma Cadência de Prestação de Contas
Também chamada de “ritmo de responsabilidade” no Brasil, esta disciplina estabelece encontros regulares, curtos e objetivos, nos quais cada integrante da equipe presta contas do que fez e assume novos compromissos para a próxima semana.

A reunião, conhecida como “Sessão da MCI”, segue três passos:
1. Revisar os compromissos assumidos na semana anterior.
2. Avaliar os resultados obtidos (placar).
3. Assumir novos compromissos ligados às medidas de direção.

Aplicações práticas:
- Times ágeis: integrar a sessão da MCI às reuniões semanais, mantendo foco no avanço da meta.
- Áreas administrativas: reuniões de 15 a 30 minutos com registro claro de compromissos individuais.
- Educação: encontros curtos para acompanhar a implantação de novas metodologias ou programas.

Integração das 4 Disciplinas
Isoladamente, cada disciplina já é útil, mas a aplicação combinada e sequencial maximiza o impacto:
1. Definir a MCI certa (foco estratégico);
2. Determinar medidas de direção eficazes (ação controlável);
3. Acompanhar num placar visível (motivação constante);
4. Reunir-se regularmente para prestação de contas (ritmo disciplinado).

Essa abordagem é eficaz porque protege as ações estratégicas do atropelo das urgências do dia a dia, garantindo que o que realmente importa avance de forma consistente.

Conclusão
No Brasil, a adaptação das 4DX com termos como MCI, medidas de direção, placar visível e cadência de prestação de contas torna o método mais prático e próximo da realidade das empresas e equipes locais. Aplicar essas disciplinas de forma rigorosa não apenas gera resultados mensuráveis, mas também cria uma cultura organizacional de execução focada, colaborativa e disciplinada.

A chave é lembrar: estratégia sem execução é ilusão, e execução sem disciplina é desperdício de energia. As 4 Disciplinas da Execução são o elo que transforma metas em conquistas concretas.

A lacuna entre o que uma organização se propõe a fazer e o que ela de fato faz é conhecida como a "falha de execução". Não importa quão brilhante seja o plano estratégico, se a execução falha, os resultados serão, na melhor das hipóteses, medíocres. A equipe de liderança passa semanas, ou até meses, em retiros estratégicos, dedicando tempo e recursos valiosos para criar um plano robusto e inspirador. As metas são ambiciosas, os objetivos são claros e a visão é nobre. O plano é então apresentado em uma reunião grandiosa, muitas vezes com apresentações de slides impressionantes e palavras de encorajamento.No entanto, o que acontece a seguir é um fenômeno previsível e destrutivo: a rotina diária. A equipe de linha de frente, sobrecarregada com as urgências e o volume de trabalho existente, simplesmente não consegue absorver a nova estratégia. A prioridade de hoje, que era "aumentar a participação de mercado", se perde em meio à crise urgente da manhã, aos e-mails não lidos e às reuniões intermináveis. Essa rotina, que os autores do método 4DX chamam de "redemoinho" (whirlwind), é o verdadeiro inimigo da execução. Ele não é malicioso, mas é implacável. Ele representa a energia e o tempo que a organização precisa para sobreviver, mas, ironicamente, é também a força que sufoca qualquer nova iniciativa.O que as organizações precisam não é de mais planejamento, mas de um sistema de execução para operar dentro e, mais importante, apesar do redemoinho. É aqui que entram as 4 Disciplinas da Execução (4DX). Desenvolvido por Chris McChesney, Sean Covey e Jim Huling, o método 4DX é um conjunto de práticas simples, mas contraintuitivas, que criam um sistema operacional para que equipes e indivíduos traduzam a estratégia em ações diárias e atinjam suas metas mais importantes de forma consistente. As 4DX são uma ponte robusta entre o planejamento estratégico de alto nível e as ações cotidianas da equipe, garantindo que o que é crucialmente importante seja alcançado.Este guia aprofundado irá detalhar cada uma das quatro disciplinas, apresentando seus princípios fundamentais, casos de sucesso, e como elas se integram com o planejamento estratégico e as metodologias ágeis, criando uma cultura de alto desempenho e resultados.A Arquitetura da Execução: As 4 DisciplinasAs 4 Disciplinas da Execução operam como um sistema coeso. O sucesso de cada disciplina é a base para o sucesso da próxima. Ignorar ou negligenciar qualquer uma delas compromete o sistema inteiro. As disciplinas são:Disciplina 1: Foque no Crucialmente ImportanteDisciplina 2: Atue nas Medidas de DireçãoDisciplina 3: Mantenha um Placar EnvolventeDisciplina 4: Crie uma Cadência de ResponsabilidadeVamos explorar cada uma delas em detalhes.Disciplina 1: Foque no Crucialmente ImportanteA primeira e mais desafiadora disciplina é a do foco. Na maioria das organizações, há uma tendência natural de assumir múltiplas metas. Os líderes, por serem visionários e ambiciosos, não querem dizer não a uma boa ideia. O resultado é uma lista de "prioridades", onde tudo é rotulado como "Prioridade #1". Infelizmente, quando tudo é importante, nada é importante. A energia da equipe, que deveria ser direcionada para uma única meta, é dispersa em várias direções, e o resultado é uma performance medíocre ou nula em todas elas.A Lei dos Retornos Decrescentes mostra que, se uma equipe foca em duas a três metas, tem alta chance de alcançá-las com excelência. Se tentar focar em quatro a dez, terá sorte se atingir uma ou duas. Com mais de dez metas, o resultado é quase sempre zero.A solução da Disciplina 1 é ir contra a sua intuição e focar em uma única Meta Crucialmente Importante (MCI) por vez, ou no máximo duas. Uma MCI é a meta que, se for alcançada, fará toda a diferença para o sucesso da sua equipe ou organização. Se ela falhar, todas as outras conquistas serão irrelevantes.Como definir uma MCI?A formulação de uma MCI deve ser clara, concisa e, acima de tudo, mensurável. Para remover qualquer ambiguidade, use o seguinte formato:De X para Y até quando.X: Onde você está hoje, o ponto de partida atual.Y: Onde você quer chegar, o objetivo específico.Quando: O prazo final para a realização da meta.Este formato transforma uma intenção vaga em uma declaração clara de sucesso.Exemplo Prático:Incorreto (vago): "Melhorar a experiência do cliente."Correto (MCI): "Aumentar o Net Promoter Score (NPS) de 40 para 65 até o final do ano fiscal."A MCI não é apenas um número, é um grito de guerra para a equipe. Ela cria um jogo que todos podem entender.Estudo de Caso: O Foco que Levou o Homem à LuaO caso mais famoso de uma MCI bem-sucedida é o do Projeto Apollo. Na década de 1950, a NASA tinha metas amplas e pouco inspiradoras. No entanto, em 1961, o Presidente John F. Kennedy estabeleceu uma Meta Crucialmente Importante para a nação: "pousar um homem na Lua e trazê-lo de volta em segurança antes do final desta década." Esta MCI funcionou por três razões principais:Clareza Total: A meta era simples, inequívoca e compreendida por todos, desde os cientistas mais graduados até os trabalhadores da linha de montagem.Inspiradora: A meta era tão grandiosa que mobilizou a imaginação e a energia de toda uma nação.Foco Exclusivo: A meta forçou a NASA a dizer "não" para outras boas ideias e projetos, canalizando toda a sua energia para um único objetivo.4DX e o Planejamento Estratégico:A Disciplina 1 preenche a lacuna crítica no planejamento estratégico. O plano estratégico da alta liderança define a visão e a direção, mas a MCI traduz essa direção em uma meta tática e executável para cada equipe. Ela assegura que a estratégia não seja apenas um documento, mas uma diretriz diária para a ação, alinhando toda a organização em torno de um objetivo comum. É a disciplina que força a organização a fazer as escolhas difíceis e a manter o foco, mesmo quando a concorrência e as oportunidades tentam desviá-la.Disciplina 2: Atue nas Medidas de DireçãoA Disciplina 2 é a disciplina da "alavancagem" e é a essência do "como" da execução. Uma vez que a MCI é definida, a pergunta passa a ser: "Que ações de alto impacto nossa equipe pode fazer para mover a agulha?" A resposta não está em focar no resultado final (a MCI), mas sim nas ações que levam a ele.O método 4DX faz uma distinção crucial entre dois tipos de medidas:Medidas Históricas (Lag Measures): São os resultados que você está tentando alcançar. Elas estão sempre no passado, são o "placar" final. Exemplos incluem: Receita, Lucro, NPS, Taxa de Acidentes, etc. Você não tem controle direto sobre elas. Você só pode medi-las e esperar que mudem.Medidas de Direção (Lead Measures): São as ações e comportamentos que você pode controlar e que, de forma preditiva, levam ao resultado desejado. Elas são a sua alavanca.Uma boa medida de direção deve ter duas características essenciais:Preditiva: Se a medida de direção mudar, você pode prever que a medida histórica também mudará. Por exemplo, "Fazer 30 minutos de exercício por dia" é preditivo para a perda de peso.Influenciável: A equipe tem controle direto sobre a ação. Ninguém de fora da equipe pode impedi-la de ser executá-la. "O índice de chuvas" não é uma boa medida de direção para uma fazenda, pois não pode ser influenciado.Exemplo: Equipe de Vendas:MCI (Medida Histórica): "Aumentar a receita trimestral de $1M para $1.2M até 30 de setembro."Medidas de Direção (Ações controláveis):"Fazer 15 ligações de prospecção por dia.""Enviar 5 propostas a novos clientes por semana.""Participar de um evento de networking por mês."A Disciplina 2 é o segredo da execução porque traduz um objetivo distante em comportamentos diários. Em vez de se preocupar com um número que só será visível no final do trimestre, a equipe foca em ações diárias e semanais que estão sob seu total controle.Estudo de Caso: Towne Park e a Alavancagem do ServiçoA Towne Park, a maior empresa de manobristas de alto padrão, definiu uma MCI para aumentar a satisfação do cliente. A equipe descobriu que a medida histórica de satisfação não se movia. Após uma análise aprofundada, eles identificaram a medida de direção mais poderosa e contraintuitiva: "reduzir o tempo de espera do carro." Através das reuniões da MCI (a ser explicada na Disciplina 4), a equipe de manobristas começou a se comprometer com ações como: "avisar aos clientes que ligassem 10 minutos antes de saírem para que o carro já estivesse pronto." Essa simples medida de direção, que era controlável pela equipe, revolucionou a satisfação dos clientes. Em Miami, uma equipe de manobristas chegou a se comprometer a derrubar uma parede de concreto (com a autorização do hotel, é claro!) que atrapalhava o fluxo, uma ação que nenhum líder de forma tradicional teria imaginado. A equipe estava tão engajada em "vencer o jogo" que a inovação e a criatividade fluíram naturalmente.4DX e Metodologias Ágeis:Esta disciplina se alinha perfeitamente com os princípios ágeis de trabalho iterativo e incremental. As medidas de direção são análogas às tarefas e objetivos de um sprint. Em vez de planejar um ano inteiro de uma vez, a equipe foca em um conjunto de medidas de direção por semana ou por sprint, obtendo feedback rápido e ajustando o curso conforme necessário. Isso garante que o progresso seja constante e que a equipe esteja sempre se movendo na direção certa, em vez de se perder em um plano estático.Disciplina 3: Mantenha um Placar EnvolventeAs pessoas jogam de forma diferente quando mantêm um placar. E mais importante, as pessoas jogam de forma diferente quando elas mantêm o placar. Sem um placar claro, a MCI se perde no redemoinho. A Disciplina 3 é a disciplina do engajamento. Seu propósito é criar um placar que não apenas mostre o progresso, mas que motive e envolva a equipe a vencer.Um placar das 4DX não é o mesmo que um dashboard de gestão complexo. Ele deve ser um Placar do Jogador, projetado para os membros da equipe que estão na linha de frente, respondendo instantaneamente à pergunta: "Estamos ganhando ou perdendo?"As quatro regras de um Placar do Jogador:É Simples? O placar deve ser tão simples que qualquer membro da equipe possa entender o status do jogo em menos de cinco segundos. Ele não pode ser uma planilha complexa.É Visível? Deve ser colocado em um local de alta visibilidade, onde a equipe possa vê-lo e consultá-lo facilmente.Mostra as Medidas de Direção e Históricas? Ele deve exibir ambas as medidas. A equipe precisa ver o que está fazendo (medidas de direção) e o que está conquistando (medida histórica/MCI) para sentir a conexão entre esforço e resultado.Posso Dizer se Estou Vencendo? O placar deve comparar o desempenho atual (o "Real") com o desempenho desejado (o "Meta"), mostrando de forma clara se a equipe está à frente ou atrás.Exemplo de Placar:Um gráfico simples que mostra a meta (uma linha horizontal) e o desempenho real da equipe (uma linha em crescimento). Se o desempenho está acima da meta, a equipe está vencendo.Estudo de Caso: Younger Brothers Construction e a Cultura de SegurançaUma construtora chamada Younger Brothers Construction enfrentava um alto índice de acidentes. Eles estabeleceram uma MCI para reduzir os incidentes e escolheram "aumentar a conformidade com 8 normas de segurança" como medida de direção. A equipe então criou um placar simples em um quadro físico, mostrando o percentual de conformidade de cada equipe versus a meta de 100%. A visibilidade do placar e a competição saudável entre as equipes levaram a um engajamento total. Os membros da equipe passaram a se policiar mutuamente para garantir que todos estivessem usando os equipamentos de segurança. A taxa de acidentes caiu dramaticamente, e o placar se tornou o coração da cultura de segurança da empresa.O placar é o coração da motivação. Ele transforma uma meta abstrata em um jogo real, do qual a equipe quer participar ativamente. A visibilidade do progresso é o principal motor do engajamento, pois as pessoas sentem que suas contribuições individuais fazem a diferença.Disciplina 4: Crie uma Cadência de ResponsabilidadeAs três primeiras disciplinas estabelecem o jogo. A Disciplina 4 é o "motor" que garante que a equipe esteja jogando para vencer, não apenas para não perder. Esta é a disciplina da responsabilidade e da execução diária.A Cadência de Responsabilidade é um ritmo de reuniões curtas e frequentes, dedicadas exclusivamente à MCI. Elas são chamadas de Reuniões da MCI (WIG Sessions) e não duram mais de 20 a 30 minutos. Estas reuniões são sagradas; o "redemoinho" é estritamente proibido. Se surgem problemas operacionais, eles são anotados para serem tratados em outra reunião, fora da WIG Session.Agenda da Reunião da MCI (WIG Session):Prestar contas: Cada membro da equipe relata o que fez na última semana para cumprir os compromissos assumidos na reunião anterior.Revisar o placar: A equipe analisa o placar para ver se os esforços da última semana geraram o progresso esperado.Planejar e comprometer-se: Cada membro se compromete com uma ou duas ações específicas de alto impacto para a próxima semana, visando impulsionar as medidas de direção.O verdadeiro poder desta disciplina reside na responsabilidade mútua entre os pares. Em vez de o líder ser o único a cobrar resultados, os membros da equipe se cobram mutuamente, criando um ambiente de suporte e alta performance.Estudo de Caso: A Escalada do Monte EverestUma ilustração poderosa da importância dessa disciplina vem da história de dois grupos que tentaram escalar o Monte Everest. Um grupo, liderado pelo famoso autor Jon Krakauer, falhou em manter a disciplina e o senso de responsabilidade, resultando na morte de oito alpinistas. Um outro grupo, que incluía um alpinista cego, Erik Weihenmayer, obteve sucesso. A grande diferença foi que a equipe de Weihenmayer realizava "reuniões de tenda" diárias, uma versão das WIG Sessions, para compartilhar o que haviam aprendido, ajustar o plano e se comprometer com as ações do dia seguinte. Essa cadência de responsabilidade manteve a equipe unida e focada em seu objetivo, permitindo que Weihenmayer se tornasse a primeira pessoa cega a chegar ao topo do Everest.4DX e Metodologias Ágeis:As WIG Sessions de 4DX são a versão de alto desempenho de cerimônias ágeis como o Daily Stand-up e a Reunião de Revisão da Sprint. Elas garantem que a equipe se mantenha focada, responsável e adaptável em ciclos curtos e contínuos de trabalho. A cadência semanal da WIG Session cria um plano de execução "just-in-time", permitindo que a equipe se adapte rapidamente aos desafios e oportunidades que surgem, sem se perder no redemoinho.O Ciclo de Execução: Superando os Estágios de MudançaA implementação das 4DX não é um evento único, mas um processo de mudança de comportamento que passa por cinco estágios previsíveis. O líder deve estar ciente desses estágios para guiar a equipe com sucesso:Clareza: A equipe compreende e concorda com a MCI, as medidas e o placar.Lançamento: O processo começa. Nesta fase, o líder precisa de energia extra para garantir que a equipe saia da inércia.Adoção: A equipe começa a internalizar as novas práticas, superando a resistência inicial. O foco aqui é seguir o processo, mais do que focar nos resultados imediatos.Otimização: A equipe já domina o processo e começa a inovar por conta própria, gerando ideias criativas para impulsionar as medidas de direção.Hábito: A execução da MCI se torna uma prática natural da equipe, o novo "normal". O sucesso gera engajamento e a equipe está pronta para uma nova MCI.Conexões Poderosas com o Planejamento Estratégico e Metodologias ÁgeisAs 4 Disciplinas da Execução não substituem o planejamento estratégico ou as metodologias ágeis; elas são a camada de execução que os torna eficazes.4DX e Planejamento Estratégico: Enquanto o planejamento estratégico define o "onde vamos", a Disciplina 1 de 4DX define o "o que vamos fazer primeiro". A MCI é o elo mais forte entre a visão de longo prazo e a realidade da ação.4DX e Metodologias Ágeis: As 4DX são uma metodologia ágil de alto nível para a execução. A MCI pode ser vista como o objetivo do produto, enquanto as medidas de direção são as tarefas do backlog ou do sprint que impulsionam o progresso. A WIG Session é a versão corporativa do Daily Stand-up, garantindo o alinhamento e a responsabilidade em ciclos curtos e contínuos.Em resumo, o planejamento estratégico define o destino, as metodologias ágeis criam o veículo, e as 4DX são o sistema de navegação e o motor que garantem que o veículo chegue ao destino, superando os obstáculos da estrada.Ao implementar as 4 Disciplinas, as organizações conseguem, de fato, executar suas estratégias mais importantes de forma consistente. O resultado é não apenas o alcance de metas, mas a construção de uma cultura de execução, onde o sucesso se torna o principal motivador para a equipe e a organização como um todo.
"""

# --- Configuração da página ---
st.set_page_config(page_title="💬 Chat 4DX", page_icon="🎯")
st.title("💬 Chat 4DX: As 4 Disciplinas da Execução")

# --- Verificação da chave API ---
try:
    api_key = st.secrets["GROQ_API_KEY"]
except Exception as e:
    st.error("🔐 Erro ao carregar a chave API. Verifique os 'secrets'.")
    st.stop()

# --- Inicializa o histórico de mensagens ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Olá! Sou um especialista em As 4 Disciplinas da Execução. Como posso te ajudar hoje?"}
    ]

# --- Exibe as mensagens do chat ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- Campo de entrada do usuário ---
if prompt := st.chat_input("Digite sua pergunta sobre as 4DX..."):
    # Adiciona a mensagem do usuário
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Chama o modelo Groq
    try:
        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": f"Você é um especialista em 'As 4 Disciplinas da Execução'. Responda APENAS com base no texto abaixo. Se a informação não estiver aqui, diga 'Não encontrei isso no texto.'\n\n{CONTEUDO_4D}"},
                {"role": "user", "content": prompt}
            ],
            model="llama3-8b-8192",
            temperature=0.7,
            max_tokens=1024
        )
        resposta = response.choices[0].message.content
    except Exception as e:
        resposta = f"❌ Erro ao gerar resposta: {str(e)}"

    # Adiciona e exibe a resposta
    st.session_state.messages.append({"role": "assistant", "content": resposta})
    with st.chat_message("assistant"):
        st.markdown(resposta)
