import requests
from bs4 import BeautifulSoup

url_clientes = "https://raw.githubusercontent.com/digitalinnovationone/dio-lab-assistente-investimentos-rpa-n8n/main/docs/index.html"
WEBHOOK_URL = "http://localhost:5678/webhook-test/investimentos"

response = requests.get(url_clientes)
soup = BeautifulSoup(response.text, 'html.parser')
tabela = soup.find('table')

clientes = []
if tabela:
    linhas = tabela.find_all('tr')[1:]
    for linha in linhas:
        colunas = linha.find_all('td')
        if len(colunas) >= 4:
            clientes.append({
                "nome": colunas[0].text.strip(),
                "email": colunas[1].text.strip(),
                "saldo": colunas[2].text.strip(),
                "perfil": colunas[3].text.strip()
            })
else:
    print("Tabela HTML indisponível na origem. Injetando dados padrão do desafio...")
    clientes = [
        {"nome": "João Silva", "email": "joao@email.com", "saldo": "R$ 10.000", "perfil": "Conservador"},
        {"nome": "Maria Souza", "email": "maria@email.com", "saldo": "R$ 25.000", "perfil": "Moderado"},
        {"nome": "Carlos Eduardo", "email": "carlos@email.com", "saldo": "R$ 80.000", "perfil": "Arrojado"}
    ]

for cliente in clientes:
    try:
        requests.post(WEBHOOK_URL, json=cliente)
        print(f"Sucesso: {cliente['nome']} enviado ao n8n.")
    except Exception:
        print("Erro de conexão. Verifique se o Docker está rodando e o Test Workflow está ativo.")
        break
