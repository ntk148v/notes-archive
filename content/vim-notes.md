---
title: Vim notes
---

- Vim already has built-in key commands for insert mode to shift the current line left or right one `&shiftwidth`. They are (in insert mode):
    - `Ctrl-t` : shift right (mnemonic "tab").
    - `Ctrl-d` : shift left (mnemonic "de-tab").
    - Change to shift-tab and tab (just like VSCode):

    ```vim
    " Remap shift left-right
    " for command mode
    nnoremap <Tab> >>
    nnoremap <S-Tab> <<

    " for insert mode
    inoremap <Tab> <C-t>
    inoremap <S-Tab> <C-d>
    ```
    
 - Map Ctrl-S to save file: <https://vim.fandom.com/wiki/Map_Ctrl-S_to_save_current_or_new_files>
