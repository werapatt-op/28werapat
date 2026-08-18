import tkinter as tk
from tkinter import ttk, messagebox
import random
import time
import math

# =========================================================
# SOLAR HYBRID DASHBOARD
# Python + Tkinter
# =========================================================

BG = "#F4F7F8"
DARK = "#082B4C"
DARK2 = "#123A5E"
GREEN = "#35B96B"
GREEN_LIGHT = "#EAF8EF"
BLUE = "#4D91E8"
PURPLE = "#9B7BE8"
ORANGE = "#F1A33B"
RED = "#E85D5D"
TEXT = "#1F3344"
GRAY = "#7D8B96"
WHITE = "#FFFFFF"

FONT = "Segoe UI"


# =========================================================
# MAIN WINDOW
# =========================================================

root = tk.Tk()
root.title("SolarHybrid Energy Management System")
root.geometry("1400x850")
root.minsize(1100, 700)
root.configure(bg=BG)


# =========================================================
# SYSTEM DATA
# =========================================================

system_data = {
    "solar": 18.7,
    "battery": 76.0,
    "consumption": 9.3,
    "grid": 1.2,
    "battery_kwh": 8.2,
}

update_interval = 2000
history = []

devices = {
    "Air Conditioner": True,
    "Water Heater": False,
    "EV Charger": False,
    "Pool Pump": True,
}


# =========================================================
# HELPER
# =========================================================

def clear_main():
    for widget in main.winfo_children():
        widget.destroy()


def create_title(parent, title, subtitle=""):
    frame = tk.Frame(parent, bg=BG)
    frame.pack(fill="x", padx=30, pady=(25, 10))

    tk.Label(
        frame,
        text=title,
        font=(FONT, 22, "bold"),
        bg=BG,
        fg=TEXT
    ).pack(anchor="w")

    if subtitle:
        tk.Label(
            frame,
            text=subtitle,
            font=(FONT, 9),
            bg=BG,
            fg=GRAY
        ).pack(anchor="w", pady=(4, 0))

    return frame


def create_card(parent, title, value, subtitle, color, icon):
    card = tk.Frame(
        parent,
        bg=WHITE,
        highlightbackground="#E5EAEE",
        highlightthickness=1
    )

    tk.Label(
        card,
        text=icon,
        font=(FONT, 20),
        bg=WHITE,
        fg=color
    ).pack(anchor="w", padx=18, pady=(15, 0))

    tk.Label(
        card,
        text=title,
        font=(FONT, 10),
        bg=WHITE,
        fg=GRAY
    ).pack(anchor="w", padx=18)

    value_label = tk.Label(
        card,
        text=value,
        font=(FONT, 22, "bold"),
        bg=WHITE,
        fg=TEXT
    )
    value_label.pack(anchor="w", padx=18, pady=(4, 0))

    subtitle_label = tk.Label(
        card,
        text=subtitle,
        font=(FONT, 9),
        bg=WHITE,
        fg=color
    )
    subtitle_label.pack(anchor="w", padx=18, pady=(0, 15))

    return card, value_label, subtitle_label


def create_section(parent, title):
    frame = tk.Frame(
        parent,
        bg=WHITE,
        highlightbackground="#E5EAEE",
        highlightthickness=1
    )

    tk.Label(
        frame,
        text=title,
        font=(FONT, 13, "bold"),
        bg=WHITE,
        fg=TEXT
    ).pack(anchor="w", padx=18, pady=(15, 5))

    return frame


# =========================================================
# SIDEBAR
# =========================================================

sidebar = tk.Frame(
    root,
    bg=DARK,
    width=220
)

sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)


logo = tk.Frame(sidebar, bg=DARK)
logo.pack(fill="x", padx=20, pady=25)

tk.Label(
    logo,
    text="☀",
    font=(FONT, 28),
    bg=DARK,
    fg=GREEN
).pack(side="left")

tk.Label(
    logo,
    text="SolarHybrid",
    font=(FONT, 16, "bold"),
    bg=DARK,
    fg=WHITE
).pack(side="left", padx=8)


# =========================================================
# SIDEBAR BUTTONS
# =========================================================

menu_items = [
    ("⌂", "Overview"),
    ("⚡", "Energy Flow"),
    ("▦", "Dashboard"),
    ("▣", "Devices"),
    ("↗", "Analytics"),
    ("◷", "History"),
    ("!", "Alerts"),
    ("⚙", "Settings"),
]


def menu_click(name):
    if name == "Overview":
        show_overview()

    elif name == "Energy Flow":
        show_energy_flow()

    elif name == "Dashboard":
        show_dashboard()

    elif name == "Devices":
        show_devices()

    elif name == "Analytics":
        show_analytics()

    elif name == "History":
        show_history()

    elif name == "Alerts":
        show_alerts()

    elif name == "Settings":
        show_settings()


for icon, name in menu_items:

    tk.Button(
        sidebar,
        text=f"  {icon}   {name}",
        anchor="w",
        font=(FONT, 10),
        bg=DARK,
        fg=WHITE,
        activebackground=DARK2,
        activeforeground=WHITE,
        bd=0,
        relief="flat",
        padx=15,
        pady=10,
        command=lambda n=name: menu_click(n)
    ).pack(
        fill="x",
        padx=10,
        pady=2
    )


# =========================================================
# ECO IMPACT
# =========================================================

eco = tk.Frame(
    sidebar,
    bg=DARK2
)

eco.pack(
    side="bottom",
    fill="x",
    padx=15,
    pady=20
)

tk.Label(
    eco,
    text="🌱",
    font=(FONT, 30),
    bg=DARK2
).pack(pady=(15, 0))

tk.Label(
    eco,
    text="ECO IMPACT",
    font=(FONT, 9, "bold"),
    bg=DARK2,
    fg=GREEN
).pack()

eco_label = tk.Label(
    eco,
    text="CO₂ saved\n1.2 tons",
    font=(FONT, 9),
    bg=DARK2,
    fg=WHITE
)

eco_label.pack(pady=8)

tk.Button(
    eco,
    text="View Impact",
    bg=GREEN,
    fg=WHITE,
    activebackground="#2A9D59",
    bd=0,
    padx=15,
    pady=7,
    command=lambda: messagebox.showinfo(
        "Eco Impact",
        "This system has reduced approximately\n"
        "1.2 tons of CO₂ emissions this month."
    )
).pack(pady=(0, 15))


# =========================================================
# MAIN
# =========================================================

main = tk.Frame(
    root,
    bg=BG
)

main.pack(
    side="left",
    fill="both",
    expand=True
)


# =========================================================
# LIVE DASHBOARD
# =========================================================

def show_overview():

    clear_main()

    create_title(
        main,
        "Good morning, Alex! ☀",
        "Here's your solar hybrid system overview."
    )

    # -----------------------------------------------------
    # STATUS
    # -----------------------------------------------------

    status_frame = tk.Frame(main, bg=BG)
    status_frame.pack(fill="x", padx=30)

    tk.Label(
        status_frame,
        text="● SYSTEM ONLINE",
        font=(FONT, 9, "bold"),
        bg=BG,
        fg=GREEN
    ).pack(side="left")

    clock_label = tk.Label(
        status_frame,
        text="",
        font=(FONT, 9),
        bg=BG,
        fg=GRAY
    )

    clock_label.pack(side="right")

    def update_clock():
        if clock_label.winfo_exists():
            clock_label.config(
                text=time.strftime("%d/%m/%Y   %H:%M:%S")
            )
            clock_label.after(1000, update_clock)

    update_clock()

    # -----------------------------------------------------
    # CARDS
    # -----------------------------------------------------

    cards = tk.Frame(main, bg=BG)
    cards.pack(fill="x", padx=30, pady=20)

    card1, solar_label, solar_sub = create_card(
        cards,
        "Solar Production",
        "0 kWh",
        "Live",
        GREEN,
        "☀"
    )

    card2, battery_label, battery_sub = create_card(
        cards,
        "Battery Level",
        "0%",
        "Remaining",
        GREEN,
        "🔋"
    )

    card3, consumption_label, consumption_sub = create_card(
        cards,
        "Home Consumption",
        "0 kWh",
        "Live",
        BLUE,
        "⌂"
    )

    card4, grid_label, grid_sub = create_card(
        cards,
        "Grid Status",
        "0 kWh",
        "Importing",
        ORANGE,
        "⚡"
    )

    card1.pack(side="left", fill="both", expand=True, padx=(0, 7))
    card2.pack(side="left", fill="both", expand=True, padx=7)
    card3.pack(side="left", fill="both", expand=True, padx=7)
    card4.pack(side="left", fill="both", expand=True, padx=(7, 0))

    # -----------------------------------------------------
    # ENERGY FLOW
    # -----------------------------------------------------

    flow = create_section(
        main,
        "Energy Flow   ● LIVE"
    )

    flow.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=(0, 15)
    )

    flow_content = tk.Frame(
        flow,
        bg=WHITE
    )

    flow_content.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )

    # Solar
    solar_box = tk.Frame(flow_content, bg=WHITE)
    solar_box.pack(side="left", expand=True)

    tk.Label(
        solar_box,
        text="☀",
        font=(FONT, 38),
        fg=GREEN,
        bg=WHITE
    ).pack()

    tk.Label(
        solar_box,
        text="SOLAR",
        font=(FONT, 9, "bold"),
        fg=GRAY,
        bg=WHITE
    ).pack()

    solar_flow_label = tk.Label(
        solar_box,
        text="0 kWh",
        font=(FONT, 15, "bold"),
        fg=TEXT,
        bg=WHITE
    )

    solar_flow_label.pack()

    # Arrow
    tk.Label(
        flow_content,
        text="→",
        font=(FONT, 30, "bold"),
        fg=GREEN,
        bg=WHITE
    ).pack(side="left")

    # Battery
    battery_box = tk.Frame(
        flow_content,
        bg=GREEN_LIGHT
    )

    battery_box.pack(
        side="left",
        expand=True,
        padx=30,
        pady=20
    )

    tk.Label(
        battery_box,
        text="🔋",
        font=(FONT, 38),
        bg=GREEN_LIGHT
    ).pack()

    tk.Label(
        battery_box,
        text="BATTERY",
        font=(FONT, 9, "bold"),
        fg=GRAY,
        bg=GREEN_LIGHT
    ).pack()

    battery_flow_label = tk.Label(
        battery_box,
        text="0 kWh",
        font=(FONT, 15, "bold"),
        fg=TEXT,
        bg=GREEN_LIGHT
    )

    battery_flow_label.pack()

    # Arrow
    tk.Label(
        flow_content,
        text="→",
        font=(FONT, 30, "bold"),
        fg=BLUE,
        bg=WHITE
    ).pack(side="left")

    # Home
    home_box = tk.Frame(flow_content, bg=WHITE)
    home_box.pack(side="left", expand=True)

    tk.Label(
        home_box,
        text="⌂",
        font=(FONT, 38),
        fg=BLUE,
        bg=WHITE
    ).pack()

    tk.Label(
        home_box,
        text="HOME",
        font=(FONT, 9, "bold"),
        fg=GRAY,
        bg=WHITE
    ).pack()

    home_flow_label = tk.Label(
        home_box,
        text="0 kWh",
        font=(FONT, 15, "bold"),
        fg=TEXT,
        bg=WHITE
    )

    home_flow_label.pack()

    # -----------------------------------------------------
    # LIVE UPDATE
    # -----------------------------------------------------

    def update_view():

        if not main.winfo_exists():
            return

        solar = system_data["solar"]
        battery = system_data["battery"]
        consumption = system_data["consumption"]
        grid = system_data["grid"]

        solar_label.config(
            text=f"{solar:.1f} kWh"
        )

        battery_label.config(
            text=f"{battery:.0f}%"
        )

        consumption_label.config(
            text=f"{consumption:.1f} kWh"
        )

        grid_label.config(
            text=f"{grid:.1f} kWh"
        )

        solar_flow_label.config(
            text=f"{solar:.1f} kWh"
        )

        battery_flow_label.config(
            text=f"{system_data['battery_kwh']:.1f} kWh"
        )

        home_flow_label.config(
            text=f"{consumption:.1f} kWh"
        )

        if grid > 0:
            grid_sub.config(
                text="Importing from grid",
                fg=ORANGE
            )
        else:
            grid_sub.config(
                text="Exporting to grid",
                fg=GREEN
            )

        main.after(
            update_interval,
            update_view
        )

    update_view()


# =========================================================
# ENERGY FLOW PAGE
# =========================================================

def show_energy_flow():

    clear_main()

    create_title(
        main,
        "Energy Flow",
        "Real-time energy movement through your system."
    )

    frame = create_section(
        main,
        "Live Energy Distribution"
    )

    frame.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=20
    )

    canvas = tk.Canvas(
        frame,
        bg=WHITE,
        highlightthickness=0
    )

    canvas.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )

    def draw():

        canvas.delete("all")

        w = canvas.winfo_width()
        h = canvas.winfo_height()

        if w < 100:
            return

        center_y = h // 2

        # Solar
        canvas.create_oval(
            70,
            center_y - 60,
            190,
            center_y + 60,
            fill=GREEN_LIGHT,
            outline=GREEN,
            width=2
        )

        canvas.create_text(
            130,
            center_y - 15,
            text="☀",
            font=(FONT, 35),
            fill=GREEN
        )

        canvas.create_text(
            130,
            center_y + 30,
            text=f"{system_data['solar']:.1f} kWh",
            font=(FONT, 12, "bold"),
            fill=TEXT
        )

        # Battery
        canvas.create_oval(
            w // 2 - 70,
            center_y - 60,
            w // 2 + 70,
            center_y + 60,
            fill=GREEN_LIGHT,
            outline=GREEN,
            width=2
        )

        canvas.create_text(
            w // 2,
            center_y - 15,
            text="🔋",
            font=(FONT, 30)
        )

        canvas.create_text(
            w // 2,
            center_y + 30,
            text=f"{system_data['battery']:.0f}%",
            font=(FONT, 12, "bold"),
            fill=TEXT
        )

        # Home
        canvas.create_oval(
            w - 190,
            center_y - 60,
            w - 70,
            center_y + 60,
            fill="#EAF2FF",
            outline=BLUE,
            width=2
        )

        canvas.create_text(
            w - 130,
            center_y - 15,
            text="⌂",
            font=(FONT, 35),
            fill=BLUE
        )

        canvas.create_text(
            w - 130,
            center_y + 30,
            text=f"{system_data['consumption']:.1f} kWh",
            font=(FONT, 12, "bold"),
            fill=TEXT
        )

        # arrows
        canvas.create_line(
            190,
            center_y,
            w // 2 - 70,
            center_y,
            fill=GREEN,
            width=5,
            arrow=tk.LAST
        )

        canvas.create_line(
            w // 2 + 70,
            center_y,
            w - 190,
            center_y,
            fill=BLUE,
            width=5,
            arrow=tk.LAST
        )

        canvas.after(1000, draw)

    draw()


# =========================================================
# DASHBOARD PAGE
# =========================================================

def show_dashboard():

    clear_main()

    create_title(
        main,
        "Dashboard",
        "System performance summary."
    )

    frame = tk.Frame(main, bg=BG)
    frame.pack(fill="both", expand=True, padx=30)

    items = [
        ("Solar Today", "18.7 kWh", GREEN),
        ("Solar This Week", "142.8 kWh", GREEN),
        ("Battery Efficiency", "94%", PURPLE),
        ("Grid Savings", "$18.42", BLUE),
        ("CO₂ Avoided", "36.5 kg", GREEN),
        ("System Efficiency", "91%", ORANGE),
    ]

    for i, (name, value, color) in enumerate(items):

        box = tk.Frame(
            frame,
            bg=WHITE,
            highlightbackground="#E5EAEE",
            highlightthickness=1
        )

        row = i // 2
        col = i % 2

        box.grid(
            row=row,
            column=col,
            sticky="nsew",
            padx=8,
            pady=8
        )

        tk.Label(
            box,
            text=name,
            font=(FONT, 10),
            fg=GRAY,
            bg=WHITE
        ).pack(
            anchor="w",
            padx=20,
            pady=(20, 5)
        )

        tk.Label(
            box,
            text=value,
            font=(FONT, 25, "bold"),
            fg=color,
            bg=WHITE
        ).pack(
            anchor="w",
            padx=20,
            pady=(0, 20)
        )

    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)

    for i in range(3):
        frame.grid_rowconfigure(i, weight=1)


# =========================================================
# DEVICES
# =========================================================

def show_devices():

    clear_main()

    create_title(
        main,
        "Devices",
        "Control connected home devices."
    )

    frame = tk.Frame(main, bg=BG)
    frame.pack(fill="both", expand=True, padx=30)

    for i, (name, state) in enumerate(devices.items()):

        card = tk.Frame(
            frame,
            bg=WHITE,
            highlightbackground="#E5EAEE",
            highlightthickness=1
        )

        card.pack(
            fill="x",
            pady=7
        )

        tk.Label(
            card,
            text=name,
            font=(FONT, 12, "bold"),
            bg=WHITE,
            fg=TEXT
        ).pack(
            side="left",
            padx=20,
            pady=18
        )

        status = tk.Label(
            card,
            text="ON" if state else "OFF",
            font=(FONT, 10, "bold"),
            bg=WHITE,
            fg=GREEN if state else RED
        )

        status.pack(side="right", padx=15)

        def toggle(device=name, label=status):

            devices[device] = not devices[device]

            label.config(
                text="ON" if devices[device] else "OFF",
                fg=GREEN if devices[device] else RED
            )

        tk.Button(
            card,
            text="Toggle",
            command=toggle,
            bg=DARK,
            fg=WHITE,
            bd=0,
            padx=15,
            pady=6
        ).pack(
            side="right",
            padx=10
        )


# =========================================================
# ANALYTICS
# =========================================================

def show_analytics():

    clear_main()

    create_title(
        main,
        "Analytics",
        "Solar production and consumption."
    )

    frame = create_section(
        main,
        "7 Day Energy Performance"
    )

    frame.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=20
    )

    canvas = tk.Canvas(
        frame,
        bg=WHITE,
        highlightthickness=0
    )

    canvas.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )

    def draw():

        canvas.delete("all")

        w = canvas.winfo_width()
        h = canvas.winfo_height()

        if w < 200:
            return

        solar = [18, 22, 25, 20, 27, 23, 21]
        consumption = [13, 15, 17, 14, 16, 18, 15]

        days = [
            "Mon",
            "Tue",
            "Wed",
            "Thu",
            "Fri",
            "Sat",
            "Sun"
        ]

        chart_height = h - 80
        chart_width = w - 80

        for i in range(7):

            x = 50 + i * chart_width / 6

            y1 = h - 40 - (
                solar[i] / 30 * chart_height
            )

            y2 = h - 40 - (
                consumption[i] / 30 * chart_height
            )

            canvas.create_oval(
                x - 5,
                y1 - 5,
                x + 5,
                y1 + 5,
                fill=GREEN,
                outline=""
            )

            canvas.create_oval(
                x - 5,
                y2 - 5,
                x + 5,
                y2 + 5,
                fill=BLUE,
                outline=""
            )

            if i > 0:

                px = 50 + (i - 1) * chart_width / 6

                py1 = h - 40 - (
                    solar[i - 1] / 30 * chart_height
                )

                py2 = h - 40 - (
                    consumption[i - 1] / 30 * chart_height
                )

                canvas.create_line(
                    px,
                    py1,
                    x,
                    y1,
                    fill=GREEN,
                    width=3
                )

                canvas.create_line(
                    px,
                    py2,
                    x,
                    y2,
                    fill=BLUE,
                    width=3
                )

            canvas.create_text(
                x,
                h - 20,
                text=days[i],
                fill=GRAY
            )

    canvas.bind(
        "<Configure>",
        lambda e: draw()
    )

    draw()


# =========================================================
# HISTORY
# =========================================================

def show_history():

    clear_main()

    create_title(
        main,
        "History",
        "Recent system measurements."
    )

    frame = tk.Frame(main, bg=WHITE)
    frame.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=20
    )

    columns = (
        "time",
        "solar",
        "consumption",
        "battery",
        "grid"
    )

    tree = ttk.Treeview(
        frame,
        columns=columns,
        show="headings"
    )

    tree.heading(
        "time",
        text="Time"
    )

    tree.heading(
        "solar",
        text="Solar"
    )

    tree.heading(
        "consumption",
        text="Consumption"
    )

    tree.heading(
        "battery",
        text="Battery"
    )

    tree.heading(
        "grid",
        text="Grid"
    )

    tree.column("time", width=150)
    tree.column("solar", width=150)
    tree.column("consumption", width=150)
    tree.column("battery", width=150)
    tree.column("grid", width=150)

    tree.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )

    for item in reversed(history):

        tree.insert(
            "",
            "end",
            values=(
                item["time"],
                f'{item["solar"]:.2f} kWh',
                f'{item["consumption"]:.2f} kWh',
                f'{item["battery"]:.0f}%',
                f'{item["grid"]:.2f} kWh'
            )
        )


# =========================================================
# ALERTS
# =========================================================

def show_alerts():

    clear_main()

    create_title(
        main,
        "Alerts",
        "System notifications and warnings."
    )

    battery = system_data["battery"]
    grid = system_data["grid"]

    alerts = []

    if battery < 20:
        alerts.append(
            ("LOW BATTERY",
             "Battery level is below 20%.",
             RED)
        )

    if grid > 5:
        alerts.append(
            ("HIGH GRID IMPORT",
             "Home is importing a large amount of energy.",
             ORANGE)
        )

    if not alerts:

        alerts.append(
            ("SYSTEM NORMAL",
             "No critical alerts detected.",
             GREEN)
        )

    for title, text, color in alerts:

        box = tk.Frame(
            main,
            bg=WHITE,
            highlightbackground="#E5EAEE",
            highlightthickness=1
        )

        box.pack(
            fill="x",
            padx=30,
            pady=8
        )

        tk.Label(
            box,
            text="●",
            font=(FONT, 18),
            fg=color,
            bg=WHITE
        ).pack(
            side="left",
            padx=20
        )

        content = tk.Frame(
            box,
            bg=WHITE
        )

        content.pack(
            side="left",
            pady=15
        )

        tk.Label(
            content,
            text=title,
            font=(FONT, 11, "bold"),
            fg=TEXT,
            bg=WHITE
        ).pack(anchor="w")

        tk.Label(
            content,
            text=text,
            font=(FONT, 9),
            fg=GRAY,
            bg=WHITE
        ).pack(anchor="w")


# =========================================================
# SETTINGS
# =========================================================

def show_settings():

    clear_main()

    create_title(
        main,
        "Settings",
        "Configure the SolarHybrid dashboard."
    )

    frame = tk.Frame(
        main,
        bg=WHITE,
        highlightbackground="#E5EAEE",
        highlightthickness=1
    )

    frame.pack(
        fill="x",
        padx=30,
        pady=20
    )

    tk.Label(
        frame,
        text="Update Interval",
        font=(FONT, 11, "bold"),
        bg=WHITE,
        fg=TEXT
    ).pack(
        anchor="w",
        padx=20,
        pady=(20, 5)
    )

    interval_var = tk.StringVar(
        value=str(update_interval)
    )

    combo = ttk.Combobox(
        frame,
        textvariable=interval_var,
        values=[
            "1000",
            "2000",
            "3000",
            "5000",
            "10000"
        ],
        state="readonly"
    )

    combo.pack(
        anchor="w",
        padx=20,
        pady=10
    )

    def save_settings():

        global update_interval

        update_interval = int(
            interval_var.get()
        )

        messagebox.showinfo(
            "Settings",
            "Settings saved successfully."
        )

    tk.Button(
        frame,
        text="Save Settings",
        command=save_settings,
        bg=GREEN,
        fg=WHITE,
        bd=0,
        padx=20,
        pady=8
    ).pack(
        anchor="w",
        padx=20,
        pady=(5, 20)
    )


# =========================================================
# SYSTEM SIMULATION
# =========================================================

def update_system():

    hour = time.localtime().tm_hour

    # Solar production
    if 6 <= hour <= 18:

        solar = (
            25 *
            math.sin(
                math.pi *
                (hour - 6) /
                12
            )
        )

        solar += random.uniform(
            -2,
            2
        )

        solar = max(
            0,
            solar
        )

    else:

        solar = random.uniform(
            0,
            0.5
        )

    # -----------------------------------------------------
    # HOME CONSUMPTION
    # -----------------------------------------------------

    consumption = 4

    if devices["Air Conditioner"]:
        consumption += 3

    if devices["Water Heater"]:
        consumption += 4

    if devices["EV Charger"]:
        consumption += 6

    if devices["Pool Pump"]:
        consumption += 2

    consumption += random.uniform(
        -0.8,
        0.8
    )

    consumption = max(
        1,
        consumption
    )

    # -----------------------------------------------------
    # BATTERY
    # -----------------------------------------------------

    difference = solar - consumption

    if difference > 0:

        system_data["battery"] += (
            difference * 0.20
        )

    else:

        system_data["battery"] += (
            difference * 0.10
        )

    system_data["battery"] = max(
        0,
        min(
            100,
            system_data["battery"]
        )
    )

    # -----------------------------------------------------
    # GRID
    # -----------------------------------------------------

    grid = max(
        0,
        consumption - solar
    )

    system_data["solar"] = solar
    system_data["consumption"] = consumption
    system_data["grid"] = grid

    system_data["battery_kwh"] = (
        system_data["battery"] / 100
    ) * 10.8

    # -----------------------------------------------------
    # HISTORY
    # -----------------------------------------------------

    history.append({
        "time": time.strftime("%H:%M:%S"),
        "solar": solar,
        "consumption": consumption,
        "battery": system_data["battery"],
        "grid": grid
    })

    if len(history) > 100:
        history.pop(0)

    # Update Eco Impact
    eco_label.config(
        text=f"CO₂ saved\n"
             f"{1.2 + len(history) * 0.001:.2f} tons"
    )

    root.after(
        update_interval,
        update_system
    )


# =========================================================
# START
# =========================================================

show_overview()

update_system()

root.mainloop()
