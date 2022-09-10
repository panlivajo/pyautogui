

import pyautogui
import time

# a automação consiste em através do controle de mouse, teclado e tela, fazer backup de um arquivo
# em uma area especifica, no caso a area de trabalho.

# passo 0 informar inicio de automação

pyautogui.alert('Inicio da automação, não mexa no computador apo´s dar ok')
# passo 1 abrir o navegador e entrar no google drive

pyautogui.PAUSE = 0.5
pyautogui.press('winleft')
pyautogui.write('crome')
pyautogui.press('enter')
time.sleep(3)
pyautogui.write('https://drive.google.com/drive/folders/1QBzzpJNYIYoJYQ-BFNv4p_z9zIbCSJzQ')
pyautogui.press('enter')
time.sleep(1)

# passo 2 voltar a area de trabalho, arrastar o arquivo com posição predefinida, para posição
# desejada, abrir a tela do google drive e soltar o arquivo

pyautogui.hotkey('winleft','d')
pyautogui.moveTo(1314, 50)
pyautogui.mouseDown()
pyautogui.moveTo(650, 530)
time.sleep(4)
pyautogui.hotkey('alt', 'tab')
time.sleep(1)
pyautogui.mouseUp()
time.sleep(5)
pyautogui.alert('automação encerrada')
