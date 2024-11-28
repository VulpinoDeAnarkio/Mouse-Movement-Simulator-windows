import pyautogui
import time

def run_simulation():
    try:
        # Określ odległość i czas ruchu
        distance = 200  # Przesunięcie w pikselach
        duration = 1000  # Czas trwania ruchu w milisekundach

        # Pobierz aktualne położenie myszki
        startX, startY = pyautogui.position()

        # Czas trwania symulacji w sekundach (np. 1 godzina)
        simulation_duration = 3600

        start_time = time.time()
        while time.time() - start_time < simulation_duration:
            # Symuluj ruch myszką w górę
            for i in range(distance):
                pyautogui.moveTo(startX, startY - i)
                time.sleep(duration / distance / 1000)

            # Symuluj ruch myszką w dół
            for i in range(distance):
                pyautogui.moveTo(startX, startY - distance + i)
                time.sleep(duration / distance / 1000)

    except Exception as e:
        print(f"Error: {e}")

def main():
    while True:
        run_simulation()
        response = input("Czy chcesz uruchomić symulację ponownie? (T/N): ").strip().lower()
        if response != 't':
            break

    print("Mam nadzieję, że symulator był przydatny.")
    print("\nTo rzekła Anarchy Foxy")

if __name__ == "__main__":
    main()
