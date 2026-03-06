import time
import threading
from pynput import mouse, keyboard

# Configurações
HOTKEY = keyboard.key.f6 # Tecla que liga/desliga
EXIT_KEY = keyboard.Key.esc               # Tecla para sair
CLICK_DELAY = 0.01                         # Intervalo entre cliques

mouse_controller = mouse.Controller()

clicando = False  # Estado do auto clicker


def auto_click():
    """Loop que executa os cliques continuamente."""
    global clicando

    while clicando:
        mouse_controller.click(mouse.Button.left, 1)
        time.sleep(CLICK_DELAY)


def on_press(key):
    """Detecta quando uma tecla é pressionada."""
    global clicando

    if key == HOTKEY:
        clicando = not clicando

        if clicando:
            print("[AUTOCLICK] Ativado")
            threading.Thread(target=auto_click).start()
        else:
            print("[AUTOCLICK] Desativado")

    elif key == EXIT_KEY:
        print("[INFO] Encerrando script")
        return False


print("Auto Clicker iniciado")
print("Pressione 'f6' para ligar/desligar")
print("Pressione 'ESC' para sair")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
