import pyautogui
import time

print("Posicione o mouse na posição desejada em 5 segundos...")
time.sleep(5)

# Obter as coordenadas atuais do cursor do mouse
x, y = pyautogui.position()

# Exibir as coordenadas
print(f"A posição atual do mouse é: x = {x}, y = {y}")
