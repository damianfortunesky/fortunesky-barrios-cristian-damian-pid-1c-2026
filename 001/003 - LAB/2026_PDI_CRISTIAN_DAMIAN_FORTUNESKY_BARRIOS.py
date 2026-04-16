"""TP n1 pizarra - versión optimizada"""

# Ejecutar -> python "001\003 - LAB\2026_PDI_CRISTIAN_DAMIAN_FORTUNESKY_BARRIOS.py"

from dataclasses import dataclass, field
import py5


# =========================
# Configuración general
# =========================
WIDTH = 900
HEIGHT = 600
PALETTE_HEIGHT = 90

DEFAULT_BRUSH_SIZE = 8
MIN_BRUSH_SIZE = 1
MAX_BRUSH_SIZE = 50

BACKGROUND_COLOR = (245, 245, 245)
PALETTE_BG_COLOR = (225, 225, 225)

TOOL_PENCIL = "Pencil"
TOOL_ERASER = "Eraser"

PALETTE_COLORS = [
    (0, 0, 0),        # Negro
    (30, 90, 220),    # Azul
    (30, 170, 60),    # Verde
    (220, 30, 30),    # Rojo
    (255, 170, 0),    # Amarillo
    (180, 0, 220),    # Violeta
    (255, 100, 0),    # Naranja
    (0, 200, 210),    # Celeste
]


# =========================
# Modelos
# =========================
@dataclass(frozen=True)
class Button:
    x: int
    y: int
    size: int

    def contains(self, mx: int, my: int) -> bool:
        return self.x <= mx <= self.x + self.size and self.y <= my <= self.y + self.size


@dataclass(frozen=True)
class ColorButton(Button):
    color: tuple[int, int, int]


@dataclass
class BoardState:
    selected_color: tuple[int, int, int] = PALETTE_COLORS[0]
    active_tool: str = TOOL_PENCIL
    brush_size: int = DEFAULT_BRUSH_SIZE
    color_buttons: list[ColorButton] = field(default_factory=list)
    pencil_button: Button | None = None
    eraser_button: Button | None = None


state = BoardState()


# =========================
# Utilidades
# =========================
def set_tool(tool: str) -> None:
    if state.active_tool != tool:
        state.active_tool = tool
        draw_palette()


def set_color(color: tuple[int, int, int]) -> None:
    changed = state.selected_color != color or state.active_tool != TOOL_PENCIL
    state.selected_color = color
    state.active_tool = TOOL_PENCIL
    if changed:
        draw_palette()


def change_brush_size(delta: int) -> None:
    state.brush_size = max(MIN_BRUSH_SIZE, min(MAX_BRUSH_SIZE, state.brush_size + delta))


def current_stroke_color() -> tuple[int, int, int]:
    return state.selected_color if state.active_tool == TOOL_PENCIL else BACKGROUND_COLOR


def is_drawing_area(y: int) -> bool:
    return y >= PALETTE_HEIGHT


# =========================
# Render de herramientas
# =========================
def draw_button_base(button: Button, fill_color: tuple[int, int, int], active: bool, active_stroke: tuple[int, int, int]) -> None:
    py5.fill(*fill_color)
    py5.stroke(*(active_stroke if active else (50, 50, 50)))
    py5.stroke_weight(2 if active else 1)
    py5.rect(button.x, button.y, button.size, button.size, 6)

    if active:
        py5.no_fill()
        py5.stroke(*active_stroke)
        py5.stroke_weight(3)
        py5.rect(button.x - 3, button.y - 3, button.size + 6, button.size + 6, 8)


def draw_tool_icon_pencil(button: Button, active: bool) -> None:
    draw_button_base(button, (220, 235, 255) if active else (255, 255, 255), active, (30, 100, 255))

    cx = button.x + button.size // 2
    cy = button.y + button.size // 2

    py5.fill(255, 220, 80)
    py5.stroke(80)
    py5.stroke_weight(1)
    py5.begin_shape()
    py5.vertex(cx - 5, cy - 14)
    py5.vertex(cx + 5, cy - 14)
    py5.vertex(cx + 5, cy + 8)
    py5.vertex(cx - 5, cy + 8)
    py5.end_shape(py5.CLOSE)

    py5.fill(255, 200, 150)
    py5.begin_shape()
    py5.vertex(cx - 5, cy + 8)
    py5.vertex(cx + 5, cy + 8)
    py5.vertex(cx, cy + 16)
    py5.end_shape(py5.CLOSE)

    py5.fill(255, 150, 150)
    py5.rect(cx - 5, cy - 18, 10, 6, 2)

    py5.stroke(120)
    py5.stroke_weight(1)
    py5.line(cx - 5, cy - 12, cx + 5, cy - 12)


def draw_tool_icon_eraser(button: Button, active: bool) -> None:
    draw_button_base(button, (255, 225, 225) if active else (255, 255, 255), active, (220, 50, 50))

    cx = button.x + button.size // 2
    cy = button.y + button.size // 2

    py5.fill(255, 180, 180)
    py5.stroke(180, 80, 80)
    py5.stroke_weight(1.5)
    py5.rect(cx - 14, cy - 8, 28, 16, 3)

    py5.fill(230, 100, 100)
    py5.no_stroke()
    py5.rect(cx - 14, cy + 2, 28, 6, 3)

    py5.stroke(255, 255, 255, 180)
    py5.stroke_weight(2)
    py5.line(cx - 8, cy - 4, cx + 2, cy + 6)


def draw_color_button(button: ColorButton) -> None:
    py5.fill(*button.color)
    py5.stroke(50)
    py5.stroke_weight(1)
    py5.rect(button.x, button.y, button.size, button.size, 6)

    is_selected = (
        state.active_tool == TOOL_PENCIL and
        button.color == state.selected_color
    )

    if is_selected:
        py5.no_fill()
        py5.stroke(255)
        py5.stroke_weight(3)
        py5.rect(button.x - 3, button.y - 3, button.size + 6, button.size + 6, 8)


def draw_palette() -> None:
    py5.no_stroke()
    py5.fill(*PALETTE_BG_COLOR)
    py5.rect(0, 0, WIDTH, PALETTE_HEIGHT)

    for button in state.color_buttons:
        draw_color_button(button)

    draw_tool_icon_pencil(state.pencil_button, state.active_tool == TOOL_PENCIL)
    draw_tool_icon_eraser(state.eraser_button, state.active_tool == TOOL_ERASER)

    draw_ui_text()


def draw_ui_text() -> None:
    py5.fill(40)
    py5.text_size(14)
    py5.text_align(py5.LEFT, py5.CENTER)
    py5.text(f"Herramienta: {state.active_tool}", 20, PALETTE_HEIGHT - 14)
    py5.text(f"Grosor: {state.brush_size}", 180, PALETTE_HEIGHT - 14)
    py5.text("Atajos: P lápiz | E goma | + / - grosor | C limpiar", 300, PALETTE_HEIGHT - 14)


def reset_canvas() -> None:
    py5.background(*BACKGROUND_COLOR)
    draw_palette()


# =========================
# Setup
# =========================
def build_ui() -> None:
    button_size = 42
    margin = 16
    start_x = 20
    y = (PALETTE_HEIGHT - button_size) // 2

    state.color_buttons.clear()

    for index, color in enumerate(PALETTE_COLORS):
        x = start_x + index * (button_size + margin)
        state.color_buttons.append(ColorButton(x, y, button_size, color))

    last_x = start_x + len(PALETTE_COLORS) * (button_size + margin) + 10
    state.pencil_button = Button(last_x, y, button_size)
    state.eraser_button = Button(last_x + button_size + margin, y, button_size)


def setup() -> None:
    py5.size(WIDTH, HEIGHT)
    py5.stroke_cap(py5.ROUND)
    py5.stroke_join(py5.ROUND)
    build_ui()
    reset_canvas()


# =========================
# Loop principal
# =========================
def draw() -> None:
    if py5.is_mouse_pressed and is_drawing_area(py5.mouse_y):
        py5.stroke(*current_stroke_color())
        py5.stroke_weight(state.brush_size)
        py5.line(py5.pmouse_x, py5.pmouse_y, py5.mouse_x, py5.mouse_y)


# =========================
# Eventos
# =========================
def mouse_pressed() -> None:
    mx, my = py5.mouse_x, py5.mouse_y

    if is_drawing_area(my):
        return

    if state.pencil_button.contains(mx, my):
        set_tool(TOOL_PENCIL)
        return

    if state.eraser_button.contains(mx, my):
        set_tool(TOOL_ERASER)
        return

    for button in state.color_buttons:
        if button.contains(mx, my):
            set_color(button.color)
            return


def key_pressed() -> None:
    key = py5.key.lower() if py5.key else ""

    if key == "p":
        set_tool(TOOL_PENCIL)
    elif key == "e":
        set_tool(TOOL_ERASER)
    elif py5.key == "+":
        change_brush_size(1)
        draw_palette()
    elif py5.key == "-":
        change_brush_size(-1)
        draw_palette()
    elif key == "c":
        reset_canvas()


py5.run_sketch()