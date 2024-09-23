from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Variabel yang berisi link-link lagu YouTube Music beserta durasinya
links = {
    "https://music.youtube.com/watch?v=V6ESLuloku0": "0:20",
    "https://music.youtube.com/watch?v=OZ4nHj3meHQ": "0:18",
    "https://music.youtube.com/watch?v=p6HEmjLC28Y": "0:27",
}




# Path ke Edge WebDriver
edge_service = Service(executable_path="C:/Users/KnowRise/Downloads/Compressed/edgedriver_win64/msedgedriver.exe")

options = webdriver.EdgeOptions()
adguard_extension_path = "C:/Users/KnowRise/Downloads/AdGuard-AdBlocker.crx"
options.add_extension(adguard_extension_path)

# Inisialisasi browser menggunakan Edge
driver = webdriver.Edge(service=edge_service, options=options)

# Buka halaman YouTube Music
driver.get("https://music.youtube.com")
time.sleep(15)  # Tunggu untuk instalasi AdGuard
driver.maximize_window()

# Tutup tab AdGuard jika ada
if len(driver.window_handles) > 1:
    driver.switch_to.window(driver.window_handles[1])
    driver.close()

# Kembali ke tab YouTube Music
driver.switch_to.window(driver.window_handles[0])

# Main process: putar setiap lagu sesuai durasi
try:
    for url, duration in links.items():
        # Buka link lagu
        driver.get(url)
        time.sleep(10)  # Tunggu agar lagu termuat
        driver.minimize_window()

        # Tunggu hingga tombol play terlihat dan bisa diklik
        # wait = WebDriverWait(driver, 20)
        # play_button = wait.until(EC.element_to_be_clickable((By.ID, 'play-pause-button')))
        # play_button.click()

        # Mengubah durasi dari format 'MM:SS' menjadi detik
        minutes, seconds = map(int, duration.split(':'))
        total_seconds = minutes * 60 + seconds - 10

        # Tunggu selama durasi lagu
        time.sleep(total_seconds)

except Exception as e:
    print(f"Terjadi kesalahan: {e}")
finally:
    driver.get("https://music.youtube.com/watch?v=MeLO_vuwenQ")
    input("Tekan Enter untuk menutup browser...")
    driver.quit()
