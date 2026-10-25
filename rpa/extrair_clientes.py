import requests
from bs4 import BeautifulSoup

URL_CLIENTES = "https://digitalinnovationone.github.io/dio-lab-assistente-investimentos-rpa-n8n/"
WEBHOOK_URL = "http://localhost:5678/webhook/investimentos"
resp = requests.get(URL_CLIENTES, timeout=15)
resp.raise_for_status()
soup = BeautifulSoup(resp.text, "html.parser")
tabela = soup.find("table")
if not tabela:
    raise SystemExit("Tabela não encontrada na página de origem.")

clientes = []
for linha in tabela.find_all("tr")[1:]:
    c = [td.text.strip() for td in linha.find_all("td")]
    if len(c) >= 4:
        clientes.append({"nome": c[0], "email": c[1], "saldo": c[2], "perfil": c[3]})

for cliente in clientes:
    try:
        r = requests.post(WEBHOOK_URL, json=cliente, timeout=15)
        if r.ok:
            print(f"Sucesso: {cliente['nome']} enviado ao n8n.")
        else:
            print(f"Falha ({r.status_code}) em {cliente['nome']}: {r.text[:120]}")
    except requests.RequestException as e:
        print(f"Erro de conexão: {e}")
        break
