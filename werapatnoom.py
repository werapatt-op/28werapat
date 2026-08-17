import tkinter as tk
from tkinter import ttk
import math
import random

# =========================================================
# SETTINGS
# =========================================================

BG = "#F4F7F8"
DARK = "#082B4C"
DARK2 = "#123A5E"
GREEN = "#35B96B"
GREEN_LIGHT = "#EAF8EF"
BLUE = "#4D91E8"
PURPLE = "#9B7BE8"
ORANGE = "#F1A33B"
TEXT = "#1F3344"
GRAY = "#7D8B96"
WHITE = "#FFFFFF"

FONT = "Segoe UI"


# =========================================================
# MAIN WINDOW
# =========================================================

root = tk.Tk()
root.title("SolarHybrid Dashboard")
root.geometry("1400x850")
root.minsize(1100, 700)
root.configure(bg=BG)


# =========================================================
# HELPER FUNCTIONS
# =========================================================

def create_card(parent, title, value, subtitle, color, icon):
    card = tk.Frame(
        parent,
        bg=WHITE,
        highlightbackground="#E5EAEE",
        highlightthickness=1
    )

    icon_label = tk.Label(
        card,
        text=icon,
        font=(FONT, 18),
        bg=WHITE,
        fg=color
    )
    icon_label.pack(anchor="w", padx=18, pady=(15, 0))

    tk.Label(
        card,
        text=title,
        font=(FONT, 10),
        bg=WHITE,
        fg=GRAY
    ).pack(anchor="w", padx=18)

    tk.Label(
        card,
        text=value,
        font=(FONT, 22, "bold"),
        bg=WHITE,
        fg=TEXT
    ).pack(anchor="w", padx=18, pady=(4, 0))

    tk.Label(
        card,
        text=subtitle,
        font=(FONT, 9),
        bg=WHITE,
        fg=color
    ).pack(anchor="w", padx=18, pady=(0, 15))

    return card


def section(parent, title):
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


# Logo
logo_frame = tk.Frame(sidebar, bg=DARK)
logo_frame.pack(fill="x", padx=20, pady=25)

tk.Label(
    logo_frame,
    text="🌱",
    font=(FONT, 26),
    bg=DARK,
    fg=GREEN
).pack(side="left")

tk.Label(
    logo_frame,
    text="SolarHybrid",
    font=(FONT, 16, "bold"),
    bg=DARK,
    fg=GREEN
).pack(side="left", padx=8)


# Menu
menu_items = [
    ("⌂", "Overview"),
    ("⚡", "Energy Flow"),
    ("▦", "Dashboard"),
    ("▣", "Devices"),
    ("↗", "Analytics"),
    ("◷", "History"),
    ("!", "Alerts"),
    ("⚙", "Settings"),
    ("?", "Support")
]


def menu_click(name):
    title_label.config(text=name)


for icon, name in menu_items:

    button = tk.Button(
        sidebar,
        text=f"  {icon}   {name}",
        anchor="w",
        font=(FONT, 10),
        bg=DARK,
        fg="white",
        activebackground="#17486D",
        activeforeground="white",
        bd=0,
        relief="flat",
        padx=15,
        pady=10,
        command=lambda n=name: menu_click(n)
    )

    button.pack(fill="x", padx=10, pady=2)


# Eco Impact
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
    font=(FONT, 32),
    bg=DARK2
).pack(pady=(15, 0))

tk.Label(
    eco,
    text="ECO IMPACT",
    font=(FONT, 9, "bold"),
    bg=DARK2,
    fg=GREEN
).pack()

tk.Label(
    eco,
    text="You've reduced\n1.2 tons of CO₂\nthis month.",
    font=(FONT, 8),
    bg=DARK2,
    fg="white",
    justify="center"
).pack(pady=8)

tk.Button(
    eco,
    text="View Impact",
    bg=GREEN,
    fg="white",
    activebackground="#2A9D59",
    bd=0,
    padx=15,
    pady=7
).pack(pady=(0, 15))


# =========================================================
# MAIN AREA
# =========================================================

main = tk.Frame(root, bg=BG)
main.pack(side="left", fill="both", expand=True)


# =========================================================
# HEADER
# =========================================================

header = tk.Frame(main, bg=BG)
header.pack(fill="x", padx=30, pady=(25, 10))

title_label = tk.Label(
    header,
    text="Good morning, Alex! ☀",
    font=(FONT, 21, "bold"),
    bg=BG,
    fg=TEXT
)

title_label.pack(side="left")

weather = tk.Frame(header, bg=BG)
weather.pack(side="right")

tk.Label(
    weather,
    text="☀  28°C",
    font=(FONT, 12, "bold"),
    bg=BG,
    fg=ORANGE
).pack()

tk.Label(
    weather,
    text="San Diego, CA",
    font=(FONT, 8),
    bg=BG,
    fg=GRAY
).pack()


tk.Label(
    main,
    text="Here's your solar hybrid system overview.",
    font=(FONT, 9),
    bg=BG,
    fg=GRAY
).pack(anchor="w", padx=30)


# =========================================================
# TOP CARDS
# =========================================================

cards = tk.Frame(main, bg=BG)
cards.pack(fill="x", padx=30, pady=20)

card1 = create_card(
    cards,
    "Solar Production",
    "18.7 kWh",
    "↑ 12% vs yesterday",
    GREEN,
    "☀"
)

card2 = create_card(
    cards,
    "Battery Level",
    "76%",
    "Remaining",
    GREEN,
    "▣"
)

card3 = create_card(
    cards,
    "Home Consumption",
    "9.3 kWh",
    "Today",
    BLUE,
    "⌂"
)

card4 = create_card(
    cards,
    "Grid Status",
    "Importing",
    "1.2 kWh",
    ORANGE,
    "⚡"
)

card1.pack(side="left", fill="both", expand=True, padx=(0, 7))
card2.pack(side="left", fill="both", expand=True, padx=7)
card3.pack(side="left", fill="both", expand=True, padx=7)
card4.pack(side="left", fill="both", expand=True, padx=(7, 0))


# =========================================================
# MIDDLE AREA
# =========================================================

middle = tk.Frame(main, bg=BG)
middle.pack(fill="both", expand=True, padx=30)

# -------------------------
# Energy Flow
# -------------------------

flow = section(middle, "Energy Flow   ● Live")
flow.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(0, 8)
)


flow_area = tk.Frame(flow, bg=WHITE)
flow_area.pack(fill="both", expand=True, padx=15, pady=10)


def flow_item(parent, emoji, value, name):
    box = tk.Frame(parent, bg=WHITE)

    tk.Label(
        box,
        text=emoji,
        font=(FONT, 28),
        bg=WHITE
    ).pack()

    tk.Label(
        box,
        text=value,
        font=(FONT, 11, "bold"),
        bg=WHITE,
        fg=TEXT
    ).pack()

    tk.Label(
        box,
        text=name,
        font=(FONT, 9),
        bg=WHITE,
        fg=GRAY
    ).pack()

    return box


solar = flow_item(flow_area, "☀", "18.7 kWh", "Solar")
home = flow_item(flow_area, "⌂", "9.3 kWh", "Home")
grid = flow_item(flow_area, "⚡", "1.2 kWh", "Grid")

solar.grid(row=0, column=0, padx=15, pady=30)
home.grid(row=0, column=2, padx=15, pady=30)
grid.grid(row=0, column=4, padx=15, pady=30)

tk.Label(
    flow_area,
    text="→",
    font=(FONT, 25, "bold"),
    fg=GREEN,
    bg=WHITE
).grid(row=0, column=1)

tk.Label(
    flow_area,
    text="←",
    font=(FONT, 25, "bold"),
    fg=ORANGE,
    bg=WHITE
).grid(row=0, column=3)


# Battery
battery_frame = tk.Frame(flow_area, bg=WHITE)
battery_frame.grid(row=1, column=0, columnspan=5, pady=10)

tk.Label(
    battery_frame,
    text="🔋",
    font=(FONT, 35),
    bg=WHITE
).pack()

tk.Label(
    battery_frame,
    text="8.2 kWh",
    font=(FONT, 11, "bold"),
    bg=WHITE,
    fg=TEXT
).pack()

tk.Label(
    battery_frame,
    text="Battery",
    font=(FONT, 9),
    bg=WHITE,
    fg=GRAY
).pack()


# -------------------------
# Energy Overview
# -------------------------

overview = section(middle, "Energy Overview")
overview.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(8, 0)
)


# Canvas chart
chart = tk.Canvas(
    overview,
    bg=WHITE,
    highlightthickness=0
)

chart.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=10
)


def draw_chart(event=None):

    chart.delete("all")

    width = chart.winfo_width()
    height = chart.winfo_height()

    if width < 100:
        return

    # Grid
    for i in range(5):

        y = 30 + i * 45

        chart.create_line(
            35,
            y,
            width - 15,
            y,
            fill="#E9EEF1"
        )

    # Labels
    labels = ["12 AM", "6 AM", "12 PM", "6 PM", "12 AM"]

    for i, label in enumerate(labels):

        x = 40 + i * ((width - 60) / 4)

        chart.create_text(
            x,
            height - 20,
            text=label,
            fill=GRAY,
            font=(FONT, 8)
        )

    data_sets = [
        ([10, 12, 25, 18, 8], GREEN),
        ([8, 10, 12, 17, 15], BLUE),
        ([12, 8, 4, 10, 13], PURPLE),
        ([7, 6, 2, 7, 9], ORANGE)
    ]

    for values, color in data_sets:

        points = []

        for i, value in enumerate(values):

            x = 40 + i * ((width - 60) / 4)

            y = height - 50 - value * 8

            points.extend([x, y])

        chart.create_line(
            points,
            fill=color,
            width=3,
            smooth=True
        )

        for i in range(5):

            x = 40 + i * ((width - 60) / 4)
            y = height - 50 - values[i] * 8

            chart.create_oval(
                x - 3,
                y - 3,
                x + 3,
                y + 3,
                fill=color,
                outline=color
            )


chart.bind("<Configure>", draw_chart)


# =========================================================
# BOTTOM AREA
# =========================================================

bottom = tk.Frame(main, bg=BG)
bottom.pack(fill="both", expand=True, padx=30, pady=15)


# -------------------------
# Production & Consumption
# -------------------------

production = section(
    bottom,
    "Production & Consumption"
)

production.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(0, 8)
)


bar_canvas = tk.Canvas(
    production,
    bg=WHITE,
    highlightthickness=0
)

bar_canvas.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=10
)


def draw_bars(event=None):

    bar_canvas.delete("all")

    width = bar_canvas.winfo_width()
    height = bar_canvas.winfo_height()

    if width < 100:
        return

    days = [
        "Mon",
        "Tue",
        "Wed",
        "Thu",
        "Fri",
        "Sat",
        "Sun"
    ]

    solar_data = [18, 22, 25, 20, 27, 23, 21]
    consume_data = [13, 15, 17, 14, 16, 18, 15]

    max_value = 30

    bar_width = 10
    spacing = width / 8

    for i, day in enumerate(days):

        x = spacing * (i + 1)

        h1 = solar_data[i] / max_value * (height - 70)
        h2 = consume_data[i] / max_value * (height - 70)

        # Solar
        bar_canvas.create_rectangle(
            x,
            height - 40 - h1,
            x + bar_width,
            height - 40,
            fill=GREEN,
            outline=""
        )

        # Consumption
        bar_canvas.create_rectangle(
            x + 13,
            height - 40 - h2,
            x + 13 + bar_width,
            height - 40,
            fill=BLUE,
            outline=""
        )

        bar_canvas.create_text(
            x + 8,
            height - 20,
            text=day,
            fill=GRAY,
            font=(FONT, 8)
        )


bar_canvas.bind("<Configure>", draw_bars)


# -------------------------
# Smart Insights
# -------------------------

insight = section(
    bottom,
    "🌱 Smart Insights"
)

insight.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(8, 0)
)


insight_box = tk.Frame(
    insight,
    bg=GREEN_LIGHT
)

insight_box.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=10
)

tk.Label(
    insight_box,
    text="Great job! 🎉",
    font=(FONT, 13, "bold"),
    bg=GREEN_LIGHT,
    fg=TEXT
).pack(
    anchor="w",
    padx=20,
    pady=(20, 5)
)

tk.Label(
    insight_box,
    text="Your solar production\n"
         "has exceeded consumption by\n"
         "35% this week.",
    font=(FONT, 10),
    bg=GREEN_LIGHT,
    fg=TEXT,
    justify="left"
).pack(
    anchor="w",
    padx=20
)

tk.Label(
    insight_box,
    text="🌱",
    font=(FONT, 55),
    bg=GREEN_LIGHT
).pack(
    side="right",
    padx=30,
    pady=20
)


# =========================================================
# RUN
# =========================================================

root.mainloop()