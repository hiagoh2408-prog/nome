from pynput import mouse, keyboard
import pyautogui
import time



# ==============================
# VARIÁVEIS GLOBAIS
# ==============================
eventos = []
gravando = True
inicio = time.time()

mouse_listener = None


# ==============================
# FUNÇÕES DE CAPTURA
# ==============================
def on_click(x, y, button, pressed):
    global eventos, inicio

    if pressed and gravando:
        tempo = time.time() - inicio

        eventos.append({
            "x": x,
            "y": y,
            "button": button.name,
            "tempo": tempo
        })

        print(f"Gravado: {button.name} em ({x},{y}) após {round(tempo, 2)}s")


def on_press(key):
    global gravando, mouse_listener

    if key == keyboard.Key.esc:
        print("\nParando gravação...")
        gravando = False
        mouse_listener.stop()
        return False


# ==============================
# FUNÇÃO DE REPLAY
# ==============================
def replay():
    print("\nIniciando replay em 3 segundos...")
    time.sleep(3)

    tempo_anterior = 0

    for evento in eventos:
        espera = evento["tempo"] - tempo_anterior
        time.sleep(espera)

        pyautogui.moveTo(evento["x"], evento["y"])
        pyautogui.click(button=evento["button"])

        print(
            f"Reproduzido: {evento['button']} em ({evento['x']},{evento['y']})"
        )

        tempo_anterior = evento["tempo"]


# ==============================
# FUNÇÃO PRINCIPAL
# ==============================
def main():
    global mouse_listener

    print("Gravando cliques... (Pressione ESC para parar)")

    mouse_listener = mouse.Listener(on_click=on_click)
    keyboard_listener = keyboard.Listener(on_press=on_press)

    mouse_listener.start()
    keyboard_listener.start()

    mouse_listener.join()
    keyboard_listener.join()

    replay()


# ==============================
# ENTRY POINT
# ==============================
if __name__ == "__main__":
    main()
