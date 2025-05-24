import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import requests
from threading import Thread


class IPInfoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("IP Information Finder")
        self.root.geometry("600x500")

        # Main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # IP input field
        ttk.Label(main_frame, text="Enter IP addresses (comma-separated):").grid(row=0, column=0, sticky=tk.W)
        self.ip_input = ttk.Entry(main_frame, width=50)
        self.ip_input.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)

        # Results area
        self.result_text = scrolledtext.ScrolledText(main_frame, width=60, height=20)
        self.result_text.grid(row=2, column=0, columnspan=2, pady=10)

        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=2)

        self.search_button = ttk.Button(button_frame, text="Search", command=self.start_search)
        self.search_button.grid(row=0, column=0, padx=5)

        ttk.Button(button_frame, text="Clear", command=self.clear_results).grid(row=0, column=1, padx=5)

    def get_ip_info(self, ip_addresses):
        self.result_text.delete(1.0, tk.END)
        self.search_button.config(state='disabled')

        for ip in ip_addresses:
            try:
                response = requests.get(f"http://ip-api.com/json/{ip.strip()}")
                data = response.json()

                if data['status'] == 'success':
                    info = (
                        f"🌍 IP: {ip}\n"
                        f"🗺️ Country: {data['country']}\n"
                        f"🏙️ City: {data['city']}\n"
                        f"🛰️ ISP: {data['isp']}\n"
                        f"🧭 Coordinates: {data['lat']}, {data['lon']}\n"
                        "------------------------------\n"
                    )
                else:
                    info = f"❌ Could not determine data for IP: {ip}\n------------------------------\n"
            except Exception as e:
                info = f"⚠️ Error for IP {ip}: {e}\n------------------------------\n"

            self.result_text.insert(tk.END, info)
            self.result_text.see(tk.END)

        self.search_button.config(state='normal')

    def start_search(self):
        ip_text = self.ip_input.get().strip()
        if not ip_text:
            messagebox.showwarning("Warning", "Please enter at least one IP address!")
            return

        ip_list = [ip.strip() for ip in ip_text.split(',')]
        Thread(target=self.get_ip_info, args=(ip_list,), daemon=True).start()

    def clear_results(self):
        self.ip_input.delete(0, tk.END)
        self.result_text.delete(1.0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = IPInfoGUI(root)
    root.mainloop()