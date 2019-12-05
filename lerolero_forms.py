import random
from selenium import webdriver
from joblib import Parallel, delayed

# Selenium options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=800,800')
chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-proxy-server')
# chrome_options.add_argument("--proxy-server='direct://'");
# chrome_options.add_argument("--proxy-bypass-list=*");


def gerar_resposta():
    tab0 = [
        'Por outro lado, ',
        'Assim mesmo, ',
        'No entanto, não podemos esquecer que ',
        'Do mesmo modo, ',
        'A prática cotidiana prova que ',
        'Nunca é demais lembrar o peso e o significado destes problemas, uma vez que ',
        'As experiências acumuladas demonstram que ',
        'Acima de tudo, é fundamental ressaltar que ',
        'O incentivo ao avanço tecnológico, assim como ',
        'Não obstante, ',
        'Todas estas questões, devidamente ponderadas, levantam dúvidas sobre se ',
        'Pensando mais a longo prazo, ',
        'O que temos que ter sempre em mente é que ',
        'Ainda assim, existem dúvidas a respeito de como ',
        'Gostaria de enfatizar que ',
        'Todavia, ',
        'A nível organizacional, ',
        'O empenho em analisar ',
        'Percebemos, cada vez mais, que ',
        'No mundo atual, ',
        'É importante questionar o quanto ',
        'Neste sentido, ',
        'Evidentemente, ',
        'Por conseguinte, ',
        'É claro que ',
        'Podemos já vislumbrar o modo pelo qual ',
        'Desta maneira, ',
        'O cuidado em identificar pontos críticos n',
        'A certificação de metodologias que nos auxiliam a lidar com ']

    tab1 = [
        '',
        'a execução dos pontos do programa ',
        'a complexidade dos estudos efetuados ',
        'a contínua expansão de nossa atividade ',
        'a estrutura atual da organização ',
        'o novo modelo estrutural aqui preconizado ',
        'o desenvolvimento contínuo de distintas formas de atuação ',
        'a constante divulgação das informações ',
        'a consolidação das estruturas ',
        'a consulta aos diversos militantes ',
        'o início da atividade geral de formação de atitudes ',
        'o desafiador cenário globalizado ',
        'a mobilidade dos capitais internacionais ',
        'o fenômeno da Internet ',
        'a hegemonia do ambiente político ',
        'a expansão dos mercados mundiais ',
        'o aumento do diálogo entre os diferentes setores produtivos ',
        'a crescente influência da mídia ',
        'a necessidade de renovação processual ',
        'a competitividade nas transações comerciais ',
        'o surgimento do comércio virtual ',
        'a revolução dos costumes ',
        'o acompanhamento das preferências de consumo ',
        'o comprometimento entre as equipes ',
        'a determinação clara de objetivos ',
        'a adoção de políticas descentralizadoras ',
        'a valorização de fatores subjetivos ',
        'a percepção das dificuldades ',
        'o entendimento das metas propostas ',
        'o consenso sobre a necessidade de qualificação ',
        'o julgamento imparcial das eventualidades ',
        'O método De Rose de aprendizado ',
        'o método De Rose de ensino ']

    tab2 = [
        'nos obriga à análise ',
        'cumpre um papel essencial na formulação ',
        'exige a precisão e a definição ',
        'auxilia a preparação e a composição ',
        'garante a contribuição de um grupo importante na determinação ',
        'assume importantes posições no estabelecimento ',
        'facilita a criação ',
        'obstaculiza a apreciação da importância ',
        'oferece uma interessante oportunidade para verificação ',
        'acarreta um processo de reformulação e modernização ',
        'pode nos levar a considerar a reestruturação ',
        'representa uma abertura para a melhoria ',
        'ainda não demonstrou convincentemente que vai participar na mudança ',
        'talvez venha a ressaltar a relatividade ',
        'prepara-nos para enfrentar situações atípicas decorrentes ',
        'maximiza as possibilidades por conta ',
        'desafia a capacidade de equalização ',
        'agrega valor ao estabelecimento ',
        'é uma das consequências ',
        'promove a alavancagem ',
        'não pode mais se dissociar ',
        'possibilita uma melhor visão global ',
        'estimula a padronização ',
        'aponta para a melhoria ',
        'faz parte de um processo de gerenciamento ',
        'causa impacto indireto na reavaliação ',
        'apresenta tendências no sentido de aprovar a manutenção ',
        'estende o alcance e a importância ',
        'deve passar por modificações independentemente ',
        'afeta positivamente a correta previsão ',
        'afeta positivamente a hiperventilação ', ]

    tab3 = [
        'das condições financeiras e administrativas exigidas.',
        'das diretrizes de desenvolvimento para o futuro.',
        'do sistema de participação geral.',
        'das posturas dos órgãos dirigentes com relação às suas atribuições.',
        'das novas proposições.',
        'das direções preferenciais no sentido do progresso.',
        'do sistema de formação de quadros que corresponde às necessidades.',
        'das condições inegavelmente apropriadas.',
        'dos índices pretendidos.',
        'das formas de ação.',
        'dos paradigmas corporativos.',
        'dos relacionamentos verticais entre as hierarquias.',
        'do processo de comunicação como um todo.',
        'dos métodos utilizados na avaliação de resultados.',
        'de todos os recursos funcionais envolvidos.',
        'dos níveis de motivação departamental.',
        'da gestão inovadora da qual fazemos parte.',
        'dos modos de operação convencionais.',
        'de alternativas às soluções ortodoxas.',
        'dos procedimentos normalmente adotados.',
        'dos conhecimentos estratégicos para atingir a excelência.',
        'do fluxo de informações.',
        'do levantamento das variáveis envolvidas.',
        'das diversas correntes de pensamento.',
        'do impacto na agilidade decisória.',
        'das regras de conduta normativas.',
        'do orçamento setorial.',
        'do retorno esperado a longo prazo.',
        'do investimento em reciclagem técnica.',
        'do remanejamento dos quadros funcionais.']

    nomes = ["Helena", "Miguel", "Alice", "Arthur", "Laura", "Heitor", "Manuela", "Bernardo", "Valentina", "Davi",
             "Sophia", "Théo", "Isabella", "Lorenzo", "Heloísa", "Gabriel", "Luiza", "Pedro", "Júlia", "Benjamin",
             "Lorena", "Matheus", "Lívia", "Lucas", "Maria Luiza", "Nicolas", "Cecília", "Joaquim", "Eloá", "Samuel",
             "Giovanna", "Henrique", "Maria Clara", "Rafael", "Maria Eduarda", "Guilherme", "Mariana", "Enzo", "Lara",
             "Murilo", "Beatriz", "Benício", "Antonella", "Gustavo", "MariaJúlia", "Isaac", "Emanuelly", "João Miguel",
             "Isadora", "Lucca", "AnaClara", "Enzo Gabriel", "Melissa", "Pedro Henrique", "Ana Luiza", "Felipe",
             "Ana Júlia",
             "João Pedro", "Esther", "Pietro", "Lavínia", "Anthony", "Maitê", "Daniel", "Maria Cecília", "Bryan",
             "Maria Alice",
             "Davi Lucca", "Sarah", "Leonardo", "Elisa", "Vicente", "Liz", "Eduardo", "Yasmin", "Gael", "Isabelly",
             "Antônio",
             "Alícia", "Vitor", "Clara", "Noah", "Isis", "Caio", "Rebeca", "João", "Rafaela", "Emanuel", "Marina", "Cauã",
             "AnaLaura",
             "João Lucas", "Maria Helena", "Calebe", "Agatha", "Enrico", "Gabriela", "Vinícius", "Catarina", "Bento"]

    cargos = ["gerente",
              "gerente de vendas",
              "gerente de marketing",
              "gerente financeiro",
              "gestor(a)",
              "estagiário(a)",
              "analista",
              "vendedor(a)",
              "RH",
              "contador(a)",
              "empresário(a)",
              "consultor(a)"]

    inicios = ["Pela minha experiência com os métodos, ",
               "Em relação às aulas, ",
               "No que diz respeito às  aulas, ",
               "Quanto aos pontos positivos e negativos, ",
               "Quanto às aulas, ",
               "Quanto a minha visão dos momentos, ",
               "Em relação ao método de aprendizado, ",
               "Em relação à experiência vivida, ",
               "No que diz respeito às experiências, ",
               "Quanto à experiência, "]

    def lerolero(flag):
        p0 = tab0[random.randint(0, len(tab0) - 1)]
        p1 = tab1[random.randint(0, len(tab1) - 1)].lower()
        p2 = tab2[random.randint(0, len(tab2) - 1)].lower()
        p3 = tab3[random.randint(0, len(tab3) - 1)].lower()
        if flag == True:
            p0 = p0.lower()

        return str(p0 + p1 + p2 + p3 + " ")

    nome = nomes[random.randint(0, len(nomes) - 1)]
    idade = random.randint(19, 67)
    cargo = cargos[random.randint(0, len(cargos) - 1)]
    inicio = inicios[random.randint(0, len(inicios) - 1)]

    resposta = nome + ", " + str(idade) + ", " + cargo + ". " + inicio

    for i in range(random.randint(3,100)):
	    
        if i == 0:
	        flag = True
        else:
	        flag = False

        bullshit = lerolero(flag)
        resposta = resposta + bullshit
    
    return resposta

def enviar_resposta(resposta):
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.implicitly_wait(0)
    browser.get('https://forms.gle/3VjnatasVvxQhwSd6')
    campo = browser.find_element_by_xpath('//textarea[@name="entry.722894842"]')
    campo.send_keys(resposta)
    botao = browser.find_element_by_xpath("//*[contains(text(), 'Enviar')]")
    botao.click()
    browser.close()

def main():
    resposta = gerar_resposta()
    enviar_resposta(resposta)   
    
if __name__ == '__main__':
 Parallel(n_jobs=-1)(main() for i in range(100))

