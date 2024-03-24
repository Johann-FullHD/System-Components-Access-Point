import psutil
import platform
import subprocess
import tkinter as tk
import ctypes as ct

def get_system_info():
    system_info = {}

    # Betriebssystem
    system_info['Betriebssystem'] = platform.system()
    system_info['Betriebssystem-Version'] = platform.version()

    # CPU-Informationen
    cpu_info = subprocess.check_output("wmic cpu get name", shell=True).decode().strip().split('\n')[1]
    system_info['CPU'] = cpu_info

    # GPU-Informationen (Nvidia)
    try:
        gpu_info = subprocess.check_output("wmic path win32_videocontroller get name", shell=True).decode().strip().split('\n')[1]
        system_info['GPU'] = gpu_info
    except:
        system_info['GPU'] = "N/A"

    # RAM-Geschwindigkeit
    try:
        ram_speed = subprocess.check_output("wmic memorychip get speed", shell=True).decode().strip().split('\n')[1]
        system_info['RAM-Geschwindigkeit (MHz)'] = ram_speed
    except:
        system_info['RAM-Geschwindigkeit (MHz)'] = "N/A"

    # Speicherinformationen
    memory = psutil.virtual_memory()
    mem_info = {
        'Gesamtspeicher (MB)': memory.total / (1024 * 1024),
        'Verfügbarer Speicher (MB)': memory.available / (1024 * 1024),
        'Auslastung (%)': memory.percent,
        'Genutzter Speicher (MB)': memory.used / (1024 * 1024),
        'Freier Speicher (MB)': memory.free / (1024 * 1024)
    }
    system_info['Speicher'] = mem_info

    # Plattform-Informationen
    system_info['Plattform'] = platform.platform()
    system_info['Rechner-Name'] = platform.node()

    # Python-Version
    system_info['Python-Version'] = platform.python_version()

    return system_info

def update_layout(event, labels):
    for label in labels:
        label.grid_configure(sticky="w")


def create_window(system_info):
    window = tk.Tk()
    window.update()
    window.title("Systeminformationen")
    window.minsize(450, 550)
    window.maxsize(450, 550)
    window.configure(bg="black")
    DWMWA_USE_IMMERSIVE_DARK_MODE = 20
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())
    rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
    value = 2
    value = ct.c_int(value)
    set_window_attribute(hwnd, rendering_policy, ct.byref(value), ct.sizeof(value))
 
    labels = []
    row = 0

    label_header = tk.Label(window, text="Systeminformationen", font=("Helvetica", 18), fg="green", bg="black")
    label_header.grid(row=row, column=0, columnspan=2, pady=10, sticky="nsew")
    labels.append(label_header)
    row += 1

    for category, info in system_info.items():
        if isinstance(info, dict):
            category_label = tk.Label(window, text=f"{category}:", font=("Helvetica", 12), fg="green", bg="black")
            category_label.grid(row=row, column=0, padx=10, pady=5, sticky="nsew")
            labels.append(category_label)
            row += 1

            for key, value in info.items():
                if isinstance(value, list):
                    value = ', '.join(map(str, value))
                data_label = tk.Label(window, text=f"{key}: {value}", font=("Helvetica", 10), fg="green", bg="black")
                data_label.grid(row=row, column=1, padx=10, pady=5, sticky="nsew")
                labels.append(data_label)
                row += 1
        else:
            info_label = tk.Label(window, text=f"{category}: {info}", font=("Helvetica", 12), fg="green", bg="black")
            info_label.grid(row=row, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
            labels.append(info_label)
            row += 1

    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)
    window.bind("<Configure>", lambda event, labels=labels: update_layout(event, labels))
    window.mainloop()

if __name__ == "__main__":
    system_info = get_system_info()
    create_window(system_info)


## Made by Johann Kramer 2024