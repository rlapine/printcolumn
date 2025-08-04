"""
core.py

Public-facing functions for printing wrapped text, styled columns to the console using ColumnPrinter class.
Supports custom column widths, bold, italic, and foreground/background color names.

Features:
- prints text in wrapped columns to the console
- supports text color and background color for over 140 HTML safe named colors

Usage:
Use individual print_* functions for simple formatting, or print_formatted() for multiple styles.
Create reusable, styled print calls for terminal output, logs, or CLI utilities.

Author: Ryan LaPine  
Version: 0.1.0  
Date: 2025-08-03
"""
from typing import List
from .column_printer import ColumnPrinter

_column_printer = None

def _check_printer_obj():
    global _column_printer
    if _column_printer is None:
        _column_printer = ColumnPrinter()
    return _column_printer


"""
Print Column Function

Supports:
- custom column widths
- custom column divider
- custom row divider
- column text color
- column background color
- column bold
- column italic
"""

def print_column_row(*args,
        col_widths: List[int] = None,
        col_text_colors: List[str] = None,
        col_back_colors: List[str] = None,
        col_bold: List[bool] = None,
        col_italic: List[bool] = None,
        col_divider_char: str = None,
        row_divider_char: str = None,
        width: int = None,
        bold: bool = None,
        italic: bool = None,
        text_color: str = None,
        back_color: str = None,
    ) -> None:
    column_printer = _check_printer_obj()
    column_printer.print_column_row(*args,
                                    col_widths=col_widths,
                                    col_text_colors=col_text_colors,
                                    col_back_colors=col_back_colors,
                                    col_bold=col_bold,
                                    col_italic=col_italic,
                                    col_divider_char=col_divider_char,
                                    row_divider_char=row_divider_char,
                                    width=width,
                                    bold=bold,
                                    italic=italic,
                                    text_color=text_color,
                                    back_color=back_color
                                    )
    
# initialize column printer if you want to save format info
# for subsequent calls to print_column_row. 
# This is done by initializing the ColumnPrinter object with
# format info.
def initialize_column_printer(*args,
        col_widths: List[int] = None,
        col_text_colors: List[str] = None,
        col_back_colors: List[str] = None,
        col_bold: List[bool] = None,
        col_italic: List[bool] = None,
        col_divider_char: str = None,
        row_divider_char: str = None,
        width: int = None,
        bold: bool = None,
        italic: bool = None,
        text_color: str = None,
        back_color: str = None,
    ) -> None:
    global _column_printer
    _column_printer = ColumnPrinter(*args,
                                        col_widths=col_widths,
                                        col_text_colors=col_text_colors,
                                        col_back_colors=col_back_colors,
                                        col_bold=col_bold,
                                        col_italic=col_italic,
                                        col_divider_char=col_divider_char,
                                        row_divider_char=row_divider_char,
                                        width=width,
                                        bold=bold,
                                        italic=italic,
                                        text_color=text_color,
                                        back_color=back_color
                                        )

"""
Console testing script entry point.

"""

def main():
    # basic output
    print("PrintColumn - for printing wrapped text columns to the console.")
    basic_columns = []
    basic_columns.append("PrintColumn is great for displaying wrapped text in columns of a specified width.")
    basic_columns.append("Often, when printing to the console, text can become too long and unreadable."
                        "It is much clearer to wrap the text in fixed width columns.")
    basic_columns.append("PrintColumn can also stylize the columns with text colors, "
                        "and background colors, in bold or italic.")
    basic_text_colors = ['','','Blue']
    basic_background_colors = ['','','Orange']
    basic_bold = [False,False,True]
    basic_italic = [False,False,True]
    print()
    ColumnPrinter().print_column_row(*basic_columns,
                                     col_text_colors=basic_text_colors,
                                     col_back_colors=basic_background_colors,
                                     col_bold=basic_bold,
                                     col_italic=basic_italic)
    print()

    print("PrintColumn - Custom test")
    col_count = int(input("How many columns do you want?:"))
    col_text =[]
    col_widths = []
    col_text_colors = []
    col_back_colors = []
    col_bold = []
    col_italic = []
    reset = False
    for i in range(col_count):
        print(f"Enter values for column {i + 1}")
        col_text.append(input(f"\tEnter text for column {i + 1}:"))
        col_widths.append(int(input(f"\tEnter width of column {i+1}:")))
        col_text_colors.append(input(f"\tEnter text color for column {i + 1}:"))
        col_back_colors.append(input(f"\tEnter background color for column {i + 1}:"))
        col_bold.append(input(f"\tBold column {i + 1}? (y/n):").strip().lower()=='y')
        col_italic.append(input(f"\tItalic column {i + 1}? (y/n):").strip().lower()=='y')
    div_char = input("Enter a char to divide the columns:")
    row_div_char = input("Enter a char to divide rows:")
    
    ColumnPrinter().print_column_row(*col_text,
                                     col_widths = col_widths,
                                     col_text_colors=col_text_colors,
                                     col_back_colors=col_back_colors,
                                     col_bold=col_bold,
                                     col_italic=col_italic,
                                     col_divider_char=div_char,
                                     row_divider_char=row_div_char)
    print()
    

if __name__ == "__main__":
    main()