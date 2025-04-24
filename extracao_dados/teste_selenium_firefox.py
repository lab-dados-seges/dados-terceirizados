from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import glob
import shutil

DOWNLOAD_DIR = os.path.join(os.getcwd(), "csv_paginas")
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

options = Options()
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.dir", os.path.expanduser("~/Downloads"))
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")
options.set_preference("pdfjs.disabled", True)

driver = webdriver.Firefox(service=Service(), options=options)
driver.get("https://contratos.comprasnet.gov.br/transparencia/terceirizados")

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "crudTable")))

# Ativa todas as colunas na primeira página
menu_visibilidade = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "buttons-collection")))
menu_visibilidade.click()
time.sleep(1)
opcoes = driver.find_elements(By.CSS_SELECTOR, "ul.dt-button-collection li")
for opcao in opcoes:
    if "active" not in opcao.get_attribute("class"):
        opcao.click()
        time.sleep(0.2)
menu_visibilidade.click()
print("✅ Todas as colunas ativadas.\n")

def baixar_csv(pagina, ultima_linha_texto):
    # Espera aparecer a tabela
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#crudTable tbody tr")))
    linha1 = driver.find_element(By.CSS_SELECTOR, "#crudTable tbody tr")
    texto_linha1 = linha1.text.strip()

    if texto_linha1 == ultima_linha_texto:
        print(f"⚠️ Página {pagina} não mudou (linhas idênticas). Pulando CSV.")
        return ultima_linha_texto

    # Exportar CSV
    botao_csv = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "buttons-csv")))
    botao_csv.click()

    # Espera o novo arquivo aparecer
    timeout = 10
    inicio = time.time()
    novo_csv = None

    while time.time() - inicio < timeout:
        arquivos = sorted(
            glob.glob(os.path.expanduser("~/Downloads/Consulta Terceirizados*.csv")),
            key=os.path.getmtime,
            reverse=True
        )
        if arquivos:
            novo_csv = arquivos[0]
            if time.time() - os.path.getmtime(novo_csv) < 5:
                break
        time.sleep(1)

    if not novo_csv or not os.path.exists(novo_csv):
        print(f"❌ CSV da página {pagina} não foi encontrado.")
        return texto_linha1

    destino = os.path.join(DOWNLOAD_DIR, f"pagina_{pagina}.csv")
    shutil.move(novo_csv, destino)
    print(f"📄 Página {pagina} | ✅ CSV exportado.")
    return texto_linha1

ultima_linha = ""
for pagina in range(1, 11):
    ultima_linha = baixar_csv(pagina, ultima_linha)

    try:
        botao_proxima = wait.until(EC.presence_of_element_located((By.ID, "crudTable_next")))
        if "disabled" in botao_proxima.get_attribute("class"):
            print("✅ Fim da paginação.")
            break
        # Clica via JavaScript para evitar erro de visibilidade
        driver.execute_script("arguments[0].click();", botao_proxima)
        time.sleep(3)
    except Exception as e:
        print(f"❌ Erro ao mudar para a página {pagina + 1}: {e}")
        break

driver.quit()