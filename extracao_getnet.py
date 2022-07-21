from selenium import webdriver
from time import sleep
from getpass import getpass


class extract_getnet():
    def __init__(self, 
                start_date: str,
                end_date: str,
                user: str,
                password: str) -> None:
        """Método construtor da classe.

        Params:
            start_date: Data inicial das transações a serem exportadas do relatório.
            end_date: Data final das transações a serem exportadas do relatório.
            user: Usuário com acesso a Getnet.
            password: Senha do usuário informado"""
        self.start_date = start_date
        self.end_date = end_date
        self.user = user
        self.password = password
        self.url = 'https://minhaconta.getnet.com.br/login'

    def extrair(self) -> None:
        """Método para extrair efetivamente o relatório.

        Não recebe parametros.
        """
        nav = webdriver.Chrome()
        nav.get(url=self.url)
        sleep(3)
        email = nav.find_element(by='xpath', 
                                value='//*[@id="loginField"]')
        email.click()
        email.send_keys(self.user)
        senha_ = nav.find_element(by='xpath',
                                value='//*[@id="passField"]')
        senha_.click()
        senha_.send_keys(self.password)
        botton = nav.find_element(by='xpath',
                                value='//*[@id="btnEntrarContinuar"]')
        botton.click()
        sleep(5)
        nav.get(url=self.url)
        sleep(3)
        vendas = nav.find_element(by='xpath',
                                value='//*[@id="menu-1"]/span')
        vendas.click()
        sleep(3)
        calendario = nav.find_element(by='xpath', 
                                    value='//*[@id="body-index"]/app-root/main/app-que-vendi/main/section[1]/div[2]/div/div/div[3]/app-date-picker-line/div/button/span')
        calendario.click()
        sleep(3)
        de = nav.find_element(by='xpath',
                            value='//*[@id="dataDe"]')
        de.click()
        de.send_keys(self.start_date)
        sleep(1)
        ate = nav.find_element(by='xpath',
                            value='//*[@id="dataAte"]')
        ate.click()
        ate.send_keys(self.end_date)
        aplicar = nav.find_element(by='xpath', 
                                value='//*[@id="btnFiltrarPersonalizado"]')
        aplicar.click()
        sleep(2)
        exportar = nav.find_element(by='xpath', value='//*[@id="body-index"]/app-root/main/app-que-vendi/main/section[1]/div[2]/div/div/div[1]/button[1]')
        exportar.click()
        sleep(2)
        selecione_ecs = nav.find_element(by='xpath', value='//*[@id="modal-getnet"]/div/div[2]/div[1]/div[1]/div[1]/app-dropdown-matriz/button/span')
        selecione_ecs.click()
        sleep(2)
        adcionar_todos = nav.find_element(by='xpath', value='//*[@id="body-index"]/ngb-modal-window/div/div/div/div[1]/div/div/div/div[5]/div[1]/div[2]/button')
        adcionar_todos.click()
        ok = nav.find_element(by='xpath', value='//*[@id="body-index"]/ngb-modal-window/div/div/div/div[2]/button[2]')
        ok.click()
        sleep(2)
        tipo_apres = nav.find_element(by='xpath', value='//*[@id="visaoExtrato"]')
        tipo_apres.click()
        detalhamento = nav.find_element(by='xpath', value='//*[@id="visaoExtrato"]/option[4]')
        detalhamento.click()
        exportar1 = nav.find_element(by='xpath', value='//*[@id="btnExportar"]')
        exportar1.click()
        sleep(4)
        excel = nav.find_element(by='xpath', value='//*[@id="body-index"]/app-root/main/app-downloads/div/div/div[3]/table/tbody/tr[1]/td[7]/em')
        excel.click()
        sleep(3)


if __name__ == '__main__':
    data1 = input('Informe a data inicial: ').strip()
    data2 = input('Informe a data final: ')
    usuario = input('Informe seu usuário: ').strip().lower()
    senha = getpass('Informe a senha: ')
    chrome = extract_getnet(start_date=data1,
                            end_date=data2,
                            user=usuario,
                            password=senha)
    chrome.extrair()
