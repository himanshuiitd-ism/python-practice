import tkinter as tk
import threading
import time

def show_overlay_message(message, duration=4, position="bottom-right"):
    """Displays a translucent floating overlay message (Jarvis style)."""
    
    def create_window():
        root = tk.Tk()
        root.overrideredirect(True)        # Removes title bar
        root.attributes('-topmost', True)  # Always on top
        root.attributes('-alpha', 0.88)    # Transparency level (0-1)
        root.config(bg="#101010")          # Dark background

        # Add text label
        label = tk.Label(
            root,
            text=f"🤖 Jarvis: {message}",
            fg="white",
            bg="#8A8A8A",
            font=("Segoe UI", 11, "bold"),
            padx=15, pady=10,
            justify="left",
            wraplength=350
        )
        label.pack()

        # Get screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Set position based on user choice
        x, y = 20, 20
        if position == "bottom-right":
            x = screen_width - 400
            y = screen_height - 150
        elif position == "bottom-left":
            x = 20
            y = screen_height - 150
        elif position == "top-right":
            x = screen_width - 400
            y = 40
        elif position == "top-left":
            x = 20
            y = 40

        root.geometry(f"380x80+{x}+{y}")

        # Auto-close after duration
        root.after(duration * 1000, root.destroy)

        # Fade-in effect
        for i in range(0, 10):
            root.attributes('-alpha', 0.7 + i * 0.03)
            time.sleep(0.02)

        root.mainloop()

    # Run in a separate thread so it doesn’t freeze your main code
    t = threading.Thread(target=create_window)
    t.start()
