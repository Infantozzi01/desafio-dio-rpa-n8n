# Processo de RPA com n8n e Python: Assistente de Investimentos 🚀

Repositório contendo a resolução do Desafio de Projeto da DIO, que implementa um pipeline híbrido unindo RPA (Robotic Process Automation) via Python e orquestração de fluxos automatizados no n8n.

## 🧠 Arquitetura da Solução

O sistema foi estruturado para atuar em três camadas complementares:

1. **Extração e RPA (Python + BeautifulSoup)**
   - Um script que emula a navegação humana acessando uma página estática.
   - Extrai de forma inteligente os dados de uma tabela HTML contendo clientes, saldo e perfil de investidor.
   - Formata a carga de dados em JSON e dispara via requisição HTTP `POST` para o motor de orquestração.

2. **Orquestração e Tratamento (n8n Workflow)**
   - O fluxo é acionado instantaneamente através de um **Webhook** nativo.
   - Um nó `HTTP Request` consome de forma dinâmica uma base em formato CSV contendo os produtos de investimento.
   - Um nó `Code` (JavaScript) consolida as regras de negócio, cruzando o perfil do investidor com o tipo de ativo adequado.

3. **Output (Mensageria Personalizada)**
   - O resultado final é um payload JSON estruturado contendo uma sugestão de briefing financeiro personalizado, pronto para ser encaminhado via Gmail, Slack ou processado por um Agente de Inteligência Artificial.

## 🛠️ Como reproduzir o projeto

1. Execute o n8n no seu ambiente.
2. Importe o arquivo `n8n/workflow.json` na interface.
3. Ative o fluxo no modo de teste (Test Workflow).
4. Abra o notebook `src/extrair_clientes.ipynb` (ou o script `.py`), valide a URL do Webhook configurada no código e rode o script.
5. Acompanhe a mágica acontecer na interface do n8n recebendo os dados em tempo real!
