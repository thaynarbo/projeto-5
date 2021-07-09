from random import randint
from pessoa import Pessoa, humano
from time import sleep
from tempo import Tempo,tempo
import os
import sys


def validation(a):
    while a not in 'AB':
        a = input('Digite uma opção do menu [A / B]:  ')[0].upper()
    return a

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        sleep(0.044)

def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def option1():
    clean_screen()
    print(Tempo())
    print_slow(f'{humano.name} acorda cansada, não dormiu direito pois estava preocupada\ncomo iria honrar com as contas. João está chorando, com a fralda suja e\n{humano.name} está atrasada para ir ao trabalho.')
    print(
    f'''


            A){humano.name} vai cuidar do filho, toma um banho rápido
            ou prepara sua merenda e em seguida vai para o trabalho.

            B)Acorda Amando e pede que ele vá cuidar do filho e preparar
            a merenda do casal enquanto {humano.name} vai tomar banho.        
    '''   )
    
    choice = input('Digite uma opção do menu [A / B]:  ')[0].upper()
    answer = validation(choice)
    random_choice = randint(1, 2)
    
    if answer == 'A':
        if random_choice == 1:
            print(
                f'\n{humano.name} tem grandes chances de chegar atrasada no trabalho e poderá ser advertida pelo seu superior.')

            fam = 10
            rel_casal = 0
            bem_est = 0
            trab = -10
            estd = 0
            segur = 0
            saude = 10

            humano.update_scores(fam, rel_casal, bem_est, trab, estd, segur, saude)
            #print(humano.__str__())

            return f'\nPontos adquirido por {humano.name}:\nFamília: {fam} pontos\nTrabalho: {trab} pontos\n Saúde: {saude} pontos'

        elif random_choice == 2:
            print(f'\n{humano.name} cuida do filho e toma banho,mas está com fome por que não merendou')

            fam = 10
            rel_casal = 10
            bem_est = 0
            trab = 10
            estd = 0
            segur = 0
            saude = 20

            humano.update_scores(fam, rel_casal, bem_est, trab, estd, segur, saude)
            #print(humano.__str__())

            return f'\nPontos adquirido por {humano.name}:\nFamilia: {fam} pontos\nRelacionamento do Casal: {rel_casal} pontos\nTrabalho: {trab} pontos\n Saúde: {saude} pontos'

    elif answer == 'B':
        if random_choice == 1:
            print(
                f'\nAmando cuida do filho e faz a merenda do casal. {humano.name} chega à tempo no trabalho. ')

            fam = 10
            rel_casal = 10
            bem_est = 0
            trab = 10
            estd = 0
            segur = 0
            saude = 10

            humano.update_scores(fam, rel_casal, bem_est,trab, estd, segur, saude)
            #print(humano.__str__())

            return f'\nPontos adquirido por {humano.name}:\nFamilia: {fam} pontos\nRelacionamento do Casal: {rel_casal} pontos\nTrabalho: {trab} pontos\n Saúde: {saude}  pontos'

        elif random_choice == 2:
            print(
                f'\nAmando volta a dormir e não faz o que {humano.name} pediu. ')

            fam = -10
            rel_casal = -10
            bem_est = 0
            trab = 10
            estd = 0
            segur = 0
            saude = -10
    
            humano.update_scores(fam, rel_casal, bem_est, trab, estd, segur, saude)
            #print(humano.__str__())
    
            return f'\nPontos adquirido por {humano.name}:\nFamilia: {fam}/100\nRelacionamento do Casal: {rel_casal}/100\nTrabalho: {trab}/100\n Saúde: {saude}/100'
def option2():
    clean_screen()
    tempo.pass_time(30)
    print(tempo)
    print_slow(f'{humano.name} ao tentar sair com o carro elétrico, que foi emprestado\npor seu irmão Fabio, nota dois suspeitos na frente da casa.')
    print(f'''


            A){humano.name} ignora os dois homens e abre o portão
            da garagem que não é automático.

            B){humano.name} chama Amando, que a orienta a chamar a policia
            e aguardar até que os dois homens saiam da frente da garagem.         
    ''')
    
    choice = input('Digite uma opção do menu [A / B]:  ')[0].upper()
    answer = validation(choice)
    random_choice = 2
    
    if answer == 'A':
        if random_choice == 1:
            print(
                f'\n{humano.name} foi muito imprudente, colocou sua vida e da sua família em risco.')

            fam = 0
            rel_casal = 0
            bem_est = 0
            trab = 10
            estd = 0
            segur = -10
            saude = 0

            humano.update_scores(fam, rel_casal, bem_est, trab, estd, segur, saude)
            print(humano.__str__())

            return f'\nPontos adquirido por {humano.name}:\nTrabalho: {trab}/100\n Saúde: {saude}/100'

        elif random_choice == 2:
            print(
                f'\nOs dois homens estavam hospedados na casa da frente, não ofereceram perigo. Eles esqueceram a chave e o celular dentro de casa . {humano.name} ligou para um chaveiro 24h para ajudar os dois rapazes e em seguida foi para o trabalho. ')
            tempo.pass_time(20)
            fam = 0
            rel_casal = 10
            bem_est = 0
            trab = -10
            estd = 0
            segur = 0
            saude = 0

            humano.update_scores(fam, rel_casal, bem_est, trab, estd, segur, saude)
            print(humano.__str__())

            return f'\nPontos adquirido por {humano.name}:\nRelacionamento do Casal: {rel_casal}/100\nTrabalho: {trab}/100'

    elif answer == 'B':
        if random_choice == 1:
            print(f'\n{humano.name} segue o conselho do Amando, chama a polícia e espera até que os dois homens saiam da frente da garagem.')
            tempo.pass_time(20)
            fam = 0
            rel_casal = 10
            bem_est = 5
            trab = -10
            estd = 0
            segur = 10
            saude = 10

            humano.update_scores(fam, rel_casal, bem_est, trab, estd, segur, saude)
            print(humano.__str__())

            return f'\nPontos adquirido por {humano.name}:\nRelacionamento do Casal: {rel_casal}/100\nBem estar: {bem_est}/100\nTrabalho: {trab}/100\nSegurança: {segur}/100\n Saúde: {saude}/100'

        elif random_choice == 2:
            print(f'\n{humano.name} briga com Amando, diz que ele é muito medroso, mas espera os dois homens irem embora e aciona a polícia. ')
            tempo.pass_time(15)
            fam = 0
            rel_casal = -10
            bem_est = 0
            trab = -10
            estd = 0
            segur = 10
            saude = 5

            humano.update_scores(fam, rel_casal, bem_est, trab, estd, segur, saude)
            print(humano.__str__())

            return f'\nPontos adquirido por {humano.name}:\nRelacionamento do Casal: {rel_casal}/100\nTrabalho: {trab}/100\nSegurança: {segur}/100\n Saúde: {saude}/100'

    #sleep(4)

def option3():
    clean_screen()
    tempo.pass_time(30)
    print(tempo)
    print_slow(f'{humano.name} está no início do  percurso em direção ao seu trabalho,\ndentro do limite de velocidade permitido pela via. Ela tem duas rotas para escolha: ')
    print(f'''


            A){humano.name} escolhe o caminho mais rápido.

            B){humano.name} pega a rota normal.      
    ''')
    
    choice = input('Digite uma opção do menu [A / B]:  ')[0].upper()
    answer = validation(choice)
    random_choice = randint(1, 2)
    
    if answer == 'A':
        if random_choice == 1:
            print(f'\nNo caminho mais rápido uma pessoa entra na frente do carro, mas ela não foi atropelada, não teve danos materiais, só o susto.')

            fam = 0
            rel_casal = 0
            bem_est = 10
            trab = 0
            estd = 0
            segur = 10
            saude = 10

            humano.update_scores(fam, rel_casal, bem_est, trab, estd, segur, saude)
            print(humano.__str__())

            return f'\nPontos adquirido por {humano.name}:\nBem estar: {bem_est}/100\nSegurança: {segur}/100\n Saúde: {saude}/100'

        elif random_choice == 2:
            print(
                f'\nNo caminho mais rápido uma pessoa entra na frente do carro. Ao jogar o carro para a calçada {humano.name} bateu no meio fio e furou o pneu se atrasou. ')
            tempo.pass_time(30)
            fam = 0
            rel_casal = 0
            bem_est = -5
            trab = -10
            estd = 0
            segur = -10
            saude = -10

            humano.update_scores(fam, rel_casal, bem_est, trab, estd, segur, saude)
            print(humano.__str__())

            return f'\nPontos adquirido por {humano.name}:\nBem estar: {bem_est}/100\nTrabalho: {trab}/100\nSegurança: {segur}/100\n Saúde: {saude}/100'

    elif answer == 'B':
        if random_choice == 1:
            print(f'\nO trânsito esta normal, ela chega no trabalho cedo.')

            fam = 0
            rel_casal = 0
            bem_est = 5
            trab = 10
            estd = 0
            segur = 0
            saude = 5

            humano.update_scores(fam, rel_casal, bem_est, trab, estd, segur, saude)
            print(humano.__str__())

            return f'\nPontos adquirido por {humano.name}:\nBem estar: {bem_est}/100\nTrabalho: {trab}/100\n Saúde: {saude}/100'

        elif random_choice == 2:
            print(
                f'\n{humano.name} pega um engarrafamento devido um acidente e chega atrasada no trabalho.')

            fam = 0
            rel_casal = 0
            bem_est = -5
            trab = -10
            estd = 0
            segur = 0
            saude = -5

            humano.update_scores(fam, rel_casal, bem_est, trab, estd, segur, saude)
            print(humano.__str__())

            return f'\nPontos adquirido por {humano.name}:\nBem estar: {bem_est}/100\nTrabalho: {trab}/100\nSaúde: {saude}/100'

    #sleep(4)

def option4():
    clean_screen()
    tempo.pass_time(60*2)
    print(tempo)
    print_slow(f'O chefe de {humano.name} pede que ela seja realocada de função durante 7\ndias, para uma função de gestão de planejamentos de dados da escola. Caso {humano.name}\naceite essa pequena mudança ela terá que levar trabalho para casa e fazer pela\nmadrugada adentro, já que não dispõe de outro horário. ')
    print(f'''


            A){humano.name} vê esse desafio como uma oportunidade de evolução
            pessoal e profissional mesmo que ela abdique de algumas horas do seu sono.

            B){humano.name} recusa educadamente o pedido do chefe já que não tem tempo
            disponível. Mas fica triste em dar a recusa, pois o seu superior é muito
            compreensível com ela, até autorizou a sua saída uma hora mais cedo, 
            para que ela chegue a tempo na faculdade.        
    ''')
    
    choice = input('Digite uma opção do menu  [A / B]:  ')[0].upper()
    answer = validation(choice)
    random_choice = randint(1, 2)
    
    if answer == 'A':
        if random_choice == 1:
            print(f'\nDevido ao esforço de {humano.name} ela é promovida a um cargo temporário de confiança que lhe permite ganhar mais, ela fica mais contente por dar mais conforto para sua família através do aumento que vai ter.')

            fam = 10
            rel_casal = 0
            bem_est = 10
            trab = 10
            estd = 0
            segur = 10
            saude = 10

            humano.update_scores(fam, rel_casal, bem_est, trab, estd, segur, saude)
            print(humano.__str__())

            return f'\nPontos adquirido por {humano.name}:\nFamília: {fam}/100\nBem estar: {bem_est}/100\nTrabalho: {trab}/100\nSegurança: {segur}/100\n Saúde: {saude}/100'

        elif random_choice == 2:
            print(f'\n{humano.name} fica muito estressada e sobrecarregada com a quantidade de trabalho e o tempo disponível que tem. Acaba não dando atenção ao João e desconta seu estresse em Amando.')

            fam = 10
            rel_casal = -10
            bem_est = -10
            trab = 0
            estd = 0
            segur = 0
            saude = 10

            humano.update_scores(fam, rel_casal, bem_est, trab, estd, segur, saude)
            print(humano.__str__())

            return f'\nPontos adquirido por {humano.name}:\nFamília: {fam}/100\nRelacionamento do Casal: {rel_casal}/100\nBem estar: {bem_est}/100\n Saúde: {saude}/100'

    elif answer == 'B':
        if random_choice == 1:
            print(f'\nSeu chefe ficou chateado, já que ele sempre procura ajudar humano de todas as formas possíveis.')

            fam = 0
            rel_casal = 0
            bem_est = -10
            trab = -10
            estd = 0
            segur = 0
            saude = -5

            humano.update_scores(fam, rel_casal, bem_est, trab, estd, segur, saude)
            print(humano.__str__())


            return f'\nPontos adquirido por {humano.name}:\nBem estar: {bem_est}/100\nTrabalho: {trab}/100\n Saúde: {saude}/100'

        elif random_choice == 2:
            print(
                f'\n{humano.name} perdeu a oportunidade de ter um aumento. Ficou mais tempo com o seu filho.  ')

            fam = 10
            rel_casal = 0
            bem_est = 0
            trab = 0
            estd = 0
            segur = 0
            saude = 5

            humano.update_scores(fam, rel_casal, bem_est, trab, estd, segur, saude)
            print(humano.__str__())

            return f'\nPontos adquirido por {humano.name}:\nFamília: {fam}/100\n Saúde: {saude}/100'

    #sleep(4)


def option5():
    clean_screen()
    tempo.pass_time(60*3)
    print(tempo)
    print_slow(f'{humano.name} está no seu horário de almoço e dispõe de 30 min para o\nalmoçar. Quando recebe uma ligação da escola do seu filho dizendo que o Amando não foi\nbuscar a criança.')
    print(f'''


            A){humano.name} não almoça e vai pegar João na escola e traz ele 
            para o seu local de trabalho.

            B)Tenta ligar para o Armando e saber o que houve.        
            ''')
    
    choice = input('Digite uma opção do menu [A / B]:  ')[0].upper()
    answer = validation(choice)
    random_choice = randint(1, 2)
    
    if answer == 'A':
        if random_choice == 1:
            print(
                f'\n{humano.name} brincou bastante de adivinhação com João no trajeto da escola para o seu trabalho. ')

            fam = 10
            rel_casal = -10
            bem_est = 5
            trab = 0
            estd = 0
            segur = 0
            saude = 0

            humano.update_scores(fam, rel_casal, bem_est, trab, estd, segur, saude)
            print(humano.__str__())

            return f'\nPontos adquirido por {humano.name}:\nFamília: {fam}/100\nRelacionamento do Casal: {rel_casal}/100\nBem estar: {bem_est}/100'

        elif random_choice == 2:
            print(
                f'\n{humano.name} falou mal do pai na frente do João quando voltava da escola para o seu trabalho. ')

            fam = -10
            rel_casal = -10
            bem_est = -5
            trab = 0
            estd = 0
            segur = 0
            saude = -5

            humano.update_scores(fam, rel_casal, bem_est, trab, estd, segur, saude)
            print(humano.__str__())

            return f'\nPontos adquirido por {humano.name}:\nFamília: {fam}/100\nRelacionamento do Casal: {rel_casal}/100\nBem estar: {bem_est}/100\n Saúde: {saude}/100'

    elif answer == 'B':
        if random_choice == 1:
            print(f'\nDescobre que Armando se atrasou por que ele voltou para casa para fechar a panela de pressão que esqueceu ligada.  Amando estava preparando o prato favorito do filho.')

            fam = 10
            rel_casal = 10
            bem_est = 0
            trab = 0
            estd = 0
            segur = 0
            saude = 10

            humano.update_scores(fam, rel_casal, bem_est, trab, estd, segur, saude)
            print(humano.__str__())

            return f'\nPontos adquirido por {humano.name}:\nFamília: {fam}/100\nRelacionamento do Casal: {rel_casal}/100\n Saúde: {saude}/100'

        elif random_choice == 2:
            print(f'\nDescobre que Amando não foi pegar o filho por que estava em um bar. ')

            fam = -10
            rel_casal = -10
            bem_est = -5
            trab = 0
            estd = 0
            segur = 0
            saude = -5

            humano.update_scores(fam, rel_casal, bem_est, trab, estd, segur, saude)
            print(humano.__str__())

            return f'\nPontos adquirido por {humano.name}:\nFamília: {fam}/100\nRelacionamento do Casal: {rel_casal}/100\nBem estar: {bem_est}/100\nSaúde: {saude}/100'

    #sleep(4)

def option6():
    clean_screen()
    tempo.pass_time(60*7)
    print(tempo)
    print_slow(
        f'Durante o trajeto para a faculdade, o gps informa de um grande engarrafamento mais\nà frente. {humano.name} tem um trabalho para apresentar em grupo:')
    print(f'''


            A)Pega um desvio mais longo que não tem engarrafamento.

            B)Fica na mesma via, supondo que o engarrafamento já terminou.        
    ''')
    
    choice = input('Digite uma opção do menu  [A / B]:  ')[0].upper()
    answer = validation(choice)
    random_choice = randint(1, 2)
    
    if answer == 'A':
        if random_choice == 1:
            print(
                f'\nO desvio que {humano.name} fez apesar de ser mais longo não houve engarrafamento durante o trajeto, {humano.name} chegou na faculdade no horário correto.')

            fam = 0
            rel_casal = 0
            bem_est = 5
            trab = 0
            estd = 10
            segur = 0
            saude = 5

            humano.update_scores(fam, rel_casal, bem_est, trab, estd, segur, saude)
            print(humano.__str__())

            return f'\nPontos adquirido por {humano.name}:\nBem estar: {bem_est}/100\nEstudo: {estd}/100\n Saúde: {saude}/100'
            
        elif random_choice == 2:
            print(
                f'\nDurante o desvio houve engarrafamento e {humano.name} chegou atrasada na faculdade.')

            fam = 0
            rel_casal = 0
            bem_est = -5
            trab = 0
            estd = -10
            segur = 0
            saude = -5

            humano.update_scores(fam, rel_casal, bem_est, trab, estd, segur, saude)
            print(humano.__str__())

            return f'\nPontos adquirido por {humano.name}:\nBem estar: {bem_est}/100\nEstudo: {estd}/100\n Saúde: {saude}/100'

    elif answer == 'B':
        if random_choice == 1:
            print(f'\n{humano.name} não seguiu o conselho de desvio do gps e chegou na faculdade adiantada, aproveitou para lanchar e ligar para o filho.')

            fam = 10
            rel_casal = 0
            bem_est = 0
            trab = 0
            estd = 10
            segur = 0
            saude = 10

            humano.update_scores(fam, rel_casal, bem_est, trab, estd, segur, saude)
            print(humano.__str__())

            return f'\nPontos adquirido por {humano.name}:\nFamília: {fam}/100\nEstudo: {estd}/100\n Saúde: {saude}/100'

        elif random_choice == 2:
            print(f'\n{humano.name} ficou presa no engarrafamento, ficou estressada, chegou atrasada na faculdade, e levou uma advertência do professor. ')

            fam = 0
            rel_casal = 0
            bem_est = -10
            trab = 0
            estd = -10
            segur = 0
            saude = -10

            humano.update_scores(fam, rel_casal, bem_est, trab, estd, segur, saude)
            print(humano.__str__())

            return f'\nPontos adquirido por {humano.name}:\nBem estar: {bem_est}/100\nEstudo: {estd}/100\n Saúde: {saude}/100'

    #sleep(4)

def option7():
    clean_screen()
    print_slow(
        f'Ao ir em direção a vaga de estacionamento, {humano.name} aguarda o carro sair da\n vaga para poder estacionar, quando de repente um motorista\nentra de uma vez e pega a vaga. ')
    print(f'''


            A)Procura por outra vaga

            B)Tenta dialogar com o motorista para que ele dê a vaga para ela,
            já que ela estava esperando o motorista da vaga sair para ela poder entrar
    ''')
    
    choice = input('Digite uma opção do menu  [A / B]:  ')[0].upper()
    answer = validation(choice)
    random_choice = randint(1, 2)
    
    if answer == 'A':
        if random_choice == 1:
            print(f'\nEncontra uma vaga e consegue chegar à tempo na faculdade ')

            fam = 0
            rel_casal = 0
            bem_est = -5
            trab = 0
            estd = 10
            segur = 0
            saude = 5

            humano.update_scores(fam, rel_casal, bem_est, trab, estd, segur, saude)
            print(humano.__str__())

            return f'\nPontos adquirido por {humano.name}:\nBem estar: {bem_est}/100\nEstudo: {estd}/100\n Saúde: {saude}/100'

        elif random_choice == 2:
            print(f'\nChega atrasada na classe de aula')
            tempo.pass_time(15)
            fam = 0
            rel_casal = 0
            bem_est = -5
            trab = 0
            estd = -10
            segur = 0
            saude = -5

            humano.update_scores(fam, rel_casal, bem_est, trab, estd, segur, saude)
            print(humano.__str__())

            return f'\nPontos adquiridos por {humano.name}:\nBem estar: {bem_est}/100\nEstudo: {estd}/100\n Saúde: {saude}/100'

    elif answer == 'B':
        if random_choice == 1:
            print(
                f'\nO motorista que furou a frente da {humano.name} pede desculpas e tira o\ncarro da vaga. {humano.name} chega no horário na sala de aula.')

            fam = 0
            rel_casal = 0
            bem_est = 10
            trab = 0
            estd = 10
            segur = 0
            saude = 10

            humano.update_scores(fam, rel_casal, bem_est, trab, estd, segur, saude)
            print(humano.__str__())

            return f'\nPontos adquirido por {humano.name}:\nBem estar: {bem_est}/100\nEstudo: {estd}/100\n Saúde: {saude}/100'

        elif random_choice == 2:
            print(f'\nO motorista não tira o carro da vaga, {humano.name} xinga o motorista\né chega atrasada na sala de aula.  ')

            fam = 0
            rel_casal = 0
            bem_est = -10
            trab = 0
            estd = -5
            segur = 0
            saude = -5

            humano.update_scores(fam, rel_casal, bem_est, trab, estd, segur, saude)
            print(humano.__str__())

            return f'\nPontos adquirido por {humano.name}:\nBem estar: {bem_est}/100\nEstudo: {estd}/100\n Saúde: {saude}/100'

    #sleep(4)

def option8():
    clean_screen()
    tempo.pass_time(60*4)
    print(tempo)
    print_slow(
        f'Ao chegar em casa, {humano.name} descobre que Amando estava bêbado e não cuidou do filho. João estava sujo, com fome e chorando. ')
    print(f'''


            A){humano.name} vai cuidar de João, toma banho e vai jantar e vai dormir.

            B){humano.name} vai cuidar do filho e do marido. Toma banho, vai jantar
            e depois faz os trabalhos da faculdade e da escola onde ensina.
    ''')
    
    choice = input('Digite uma opção do menu  [A / B]:  ')[0].upper()
    answer = validation(choice)
    random_choice = randint(1, 2)
    
    if answer == 'A':
        if random_choice == 1:
            print(
                f'\nMesmo estando exausta de uma longa jornada de trabalho, {humano.name} cuida do filho, prepara a sua janta, toma banho e vai dormir.')

            fam = 10
            rel_casal = -10
            bem_est = 5
            trab = 0
            estd = 0
            segur = 0
            saude = 0

            humano.update_scores(fam, rel_casal, bem_est, trab, estd, segur, saude)
            print(humano.__str__())

            return f'\nPontos adquirido por {humano.name}:\nFamília: {fam}\nRelacionamento do Casal: {rel_casal}/100\nBem estar: {bem_est}/100'


        elif random_choice == 2:
            print(f'\n{humano.name} cuida do filho e depois cai na cama de tanto cansaço. O sono foi mais forte que a fome e banho.')

            fam = 5
            rel_casal = -10
            bem_est = -5
            trab = 0
            estd = 0
            segur = 0
            saude = -10

            humano.update_scores(fam, rel_casal, bem_est, trab, estd, segur, saude)
            print(humano.__str__())

            return f'\nPontos adquirido por {humano.name}:\nFamília: {fam}/100\nRelacionamento do Casal: {rel_casal}/100\nBem estar: {bem_est}/100\nSaúde: {saude}/100'

    elif answer == 'B':
        if random_choice == 1:
            print(
                f'\nApesar do problema de alcoolismo do Marido, {humano.name} acredita que Amando vai superar essa fase. Ela priorizou o cuidado de todos os integrantes da família.')

            fam = 10
            rel_casal = 10
            bem_est = 10
            trab = 10
            estd = 10
            segur = 0
            saude = 20

            humano.update_scores(fam, rel_casal, bem_est, trab, estd, segur, saude)
            print(humano.__str__())

            return f'\nPontos adquiridos por {humano.name}:\nFamília: {fam}\nRelacionamento do Casal: {rel_casal}/100\nBem estar: {bem_est}/100\nTrabalho: {trab}/100\nEstudo: {estd}/100\n Saúde: {saude}/100'

        elif random_choice == 2:
            print(f'\n{humano.name} está pensando em se divorciar, mas apesar dos problemas que ela tem com o marido, João é muito apegado com o pai, ela teme que o João fique muito triste com a separação dos pais. {humano.name} vai dormir com uma forte dor de cabeça. ')

            fam = 0
            rel_casal = -5
            bem_est = 10
            trab = 10
            estd = 10
            segur = 0
            saude = 10

            humano.update_scores(fam, rel_casal, bem_est, trab, estd, segur, saude)
            print(humano.__str__())

            return f'\nPontos adquiridos por {humano.name}:\nRelacionamento do Casal: {rel_casal}/100\nBem estar: {bem_est}/100\nTrabalho: {trab}/100\nEstudo: {estd}/100\n Saúde: {saude}/100'

    #sleep(4)

def conclusao():
    clean_screen()
    if humano.health >= 90:
        print_slow(f'\nParabéns,a {humano.name} conseguiu alcançar seus obejtivos.\n\n\nDe acordo com o estudo feito pelo Instituto de Pesquisa Econômica Aplicada, as mulheres trabalham cerca de 7,5 horas a mais do que os homens.\nO percentual de domicílios brasileiros comandados por mulheres saltou de 25%, em 1995, para 45% em 2018.\n43% das mulheres que são chefes de domicílio no Brasil vive em casal – sendo que 30% têm filhos e 13% não. Já o restante das 34,4 milhões das reponsáveis pelo lar se dividem entre mulheres solteiras com filho (32%), mulheres que vivem sozinhas (18%) e mulheres que dividem a casa com amigos ou parentes (7%).')
    else:
        print_slow(f'Infelizmente, a {humano.name} não conseguiu alcançar seus objetivos.\n\n\nDe acordo com o estudo feito pelo Instituto de Pesquisa Econômica Aplicada, as mulheres trabalham cerca de 7,5 horas a mais do que os homens.\nO percentual de domicílios brasileiros comandados por mulheres saltou de 25%, em 1995, para 45% em 2018.\n43% das mulheres que são chefes de domicílio no Brasil vive em casal – sendo que 30% têm filhos e 13% não. Já o restante das 34,4 milhões das responsáveis pelo lar se dividem entre mulheres solteiras com filho (32%), mulheres que vivem sozinhas (18%) e mulheres que dividem a casa com amigos ou parentes (7%).')
