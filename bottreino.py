import pyautogui
import time
from PIL import ImageGrab
import json

class Bot_Treino():
    def __init__(self):
        self.corMob = {1:(107,105,107),3:(148,146,148),6:(206,166,0),9:(140,113,0),
        25:(247,243,247),35:(57,190,255),45:(255,60,57),50:(189,150,0),55:(148,146,148),225:(231,89,49),
        75:(247,243,247),110:(255,0,0),120:(156,12,181),275:(140,44,49),"melle":(206,48,49)}


    def obter_cor_na_coordenada(self, x, y):
        # Captura a tela na coordenada especificada
        screenshot = ImageGrab.grab(bbox=(x, y, x + 1, y + 1))

        # Obtém o valor RGB do pixel capturado
        rgb_pixel = screenshot.getpixel((0, 0))
        #print(rgb_pixel)
        return rgb_pixel
    
    def verifica_img(self, x, y, i):
        # Obtém a cor na coordenada especificada
        cor_pixel = self.obter_cor_na_coordenada(x, y)
        print('ultimas cordenadas', x,y)

        # Compara a cor com as cores desejadas
        if i in self.corMob and cor_pixel == self.corMob[i]:
            return True
        else:
            
            print('Saida da cor',cor_pixel)
            return False
    
    def treino(self, x, y, x2, y2, i,x3,y3):
        print('pq nao que bater')
        if self.verifica_img(x2,y2,1):
            pyautogui.click(x=x3, y=y3)
            time.sleep(10)
        if self.verifica_img(x, y, i):
            pyautogui.click(x=x, y=y)
            time.sleep(10)

    def supertreino(self,x,y,x2,y2):
        if self.verifica_img(x2, y2, 1):
            for i in range(2):
                time.sleep(2)
                pyautogui.click(x=x, y=y)
            time.sleep(5)
    
    def coletarcoord(self,text):
        print(f"Posicione o mouse na posição do {text} desejada em 10 segundos...")
        time.sleep(10)
        # Obter as coordenadas atuais do cursor do mouse
        x, y = pyautogui.position()
        # Exibir as coordenadas
        print(f"A posição atual do mouse é: x = {x}, y = {y}")
        return x, y





class GerenciadorBot(Bot_Treino):  # Herda de Bot_Treino
    def __init__(self):
        super().__init__()  # Chama o construtor da classe pai
        self.tela = None
    
    def looptreinoafk(self,tipo):
        tela = self.tela
        if tipo != 1:
            while True:
                # Tela 1
                if super().verifica_img(tela['x'], tela['y'], tela['mob']):
                    print("Clique na imagem (cor predominante)")
                    super().treino(tela['x'], tela['y'], tela['x2'], tela['y2'], tela['mob'], tela['x3'], tela['y3'])
                if super().verifica_img(tela['x'], tela['y'], tela['mob2']):
                    print("Clique na imagem (cor predominante)")
                    super().treino(tela['x'], tela['y'], tela['x2'], tela['y2'], tela['mob2'], tela['x3'], tela['y3'])
                pyautogui.click(x=tela['x4'], y=tela['y4'])
                time.sleep(10)
        else:
            while True:
                melle = 'melle'
                # Tela 1
                if super().verifica_img(tela['x'], tela['y'], tela['mob']):
                    print("Clique na imagem (cor predominante)")
                    if super().verifica_img(tela['x5'], tela['y5'],melle):
                        print('ele já está treinando')
                    else:
                        super().treino(tela['x'], tela['y'], tela['x2'], tela['y2'], tela['mob2'], tela['x3'], tela['y3'])
                
                pyautogui.click(x=tela['x4'], y=tela['y4'])
                time.sleep(10)


    def switch(self,i,j): 
        match i:
            case 1:
                return self.looptreinoafk(j)
            case 2:
                return "Opção 2 selecionada"
            case _:
                return "Opção desconhecida"

    def start(self):
        print('Bem Vindo ao BotTreino \n [1] Treino Afk \n [2] Treino On \n [3] Treino Segunda Classe')
        opcao  = int(input('O Que Deseja:'))
        opcao2 = int(input('Utilizar as Últimas Coordenadas ? \n [0] Sim ou [1] Não\n:'))
        opcao3 = int(input('Qual classe vc ira treinar? \n [1] Melle \n [2] Distance \n [3] Magic\n:'))

        if opcao2 == 0:
            with open('coordenadas.json', 'r') as arquivo:
                 self.tela = json.load(arquivo)
    
        elif opcao2 == 1:
            tela = {}
            tela['x'], tela['y'] = super().coletarcoord('Monstro')
            tela['x2'], tela['y2'] = super().coletarcoord('Barra de Mana')
            tela['x3'], tela['y3'] = super().coletarcoord('Poção de Mana')
            tela['x4'], tela['y4'] = super().coletarcoord('Parede para o Jogo não deslogar')
            tela['x5'], tela['y5'] = super().coletarcoord('Linha Vermelha do Mob')
            # As chaves 'mob' e 'mob2' já têm valores definidos
            tela['mob'] = int(input('Nível para Mob de Treinamento :'))
            tela['mob2'] = int(input('2° Nível para Mob de Treinamento :'))
                    
            with open('coordenadas.json', 'w') as arquivo_json:
                 json.dump(tela, arquivo_json)
            self.tela=tela


        else:
            print(f'\nNão Foi Encontrado essa Opção {opcao2}\n')
            self.start()

        self.switch(opcao,opcao3)

    
  

gr = GerenciadorBot()

gr.start()




