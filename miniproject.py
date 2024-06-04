import gradio as gr
from gradio.themes.base import Base
from gradio.themes.utils import colors, fonts, sizes
from typing import Iterable

class Seafoam(Base):
    def __init__(
        self,
        *,
        primary_hue: colors.Color | str = colors.emerald,
        secondary_hue: colors.Color | str = colors.blue,
        neutral_hue: colors.Color | str = colors.blue,
        spacing_size: sizes.Size | str = sizes.spacing_md,
        radius_size: sizes.Size | str = sizes.radius_md,
        text_size: sizes.Size | str = sizes.text_lg,
        font: fonts.Font | str | Iterable[fonts.Font | str] = (
            fonts.GoogleFont("Quicksand"),
            "ui-sans-serif",
            "sans-serif",
        ),
        font_mono: fonts.Font | str | Iterable[fonts.Font | str] = (
            fonts.GoogleFont("IBM Plex Mono"),
            "ui-monospace",
            "monospace",
        ),
    ):
        super().__init__(
            primary_hue=primary_hue,
            secondary_hue=secondary_hue,
            neutral_hue=neutral_hue,
            spacing_size=spacing_size,
            radius_size=radius_size,
            text_size=text_size,
            font=font,
            font_mono=font_mono,
        )
        super().set(
            body_background_fill="black",
            body_background_fill_dark="black",
            button_primary_background_fill="gold",
            button_primary_background_fill_hover="black",
            button_primary_text_color="gold",
            button_primary_background_fill_dark="black",
            slider_color="gold",
            slider_color_dark="gold",
            block_title_text_weight="600",
            block_border_width="3px",
            block_shadow="*shadow_drop_lg",
            button_shadow="*shadow_drop_lg",
            button_large_padding="32px",
        )

seafoam = Seafoam()

# Implementing Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Implementing Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Function to sort the array based on the selected algorithm
def sort_array(arr, algorithm):
    arr = list(map(int, arr.split()))  # Convert the input string to a list of integers
    if algorithm == 'Selection Sort':
        sorted_arr = selection_sort(arr)
    elif algorithm == 'Insertion Sort':
        sorted_arr = insertion_sort(arr)
    return ' '.join(map(str, sorted_arr))  # Convert the sorted list back to a string

# Define the Gradio interface with custom CSS
with gr.Blocks(theme=seafoam) as demo:
    gr.Markdown("## Mini Project")
    
    input_array = gr.Textbox(label="Enter an array of numbers (space-separated)", placeholder="e.g., 5 3 8 6 2")
    algorithm = gr.Radio(["Selection Sort", "Insertion Sort"], label="Select Sorting Algorithm")
    output_array = gr.Textbox(label="Sorted Array")
    
    sort_button = gr.Button("Sort")
    
    sort_button.click(fn=sort_array, inputs=[input_array, algorithm], outputs=output_array)

# Launch the Gradio interface
demo.launch()
