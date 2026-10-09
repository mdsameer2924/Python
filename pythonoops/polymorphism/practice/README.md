# NVIM CHEAT SHEET

[Mode Switch](README.md#Mode)

## Mode Switch

- `i` -> to insert Mode
- `a` -> append mode **better replacement of `i`**
- `<leader> + e`   -> toggle on/off file explorer and for focus as well
- `<leader> + f + t` -> toggle on/off terminal
- `<leader> + f + T` -> toggle terminal on current file's path

## File explorer

- `a` -> to create file or folder

> for folder start end of the name use `/` like folder/

- `d` -> to delete the file and folder

## Navigation

nvim navigation is very crucial in nvim most the time except writing actual code we navigate a lot

### Text editor

- `k` -> up
- `j` -> down
- `h` -> left
- `l` -> right

### File explorer

- `k` -> up to folder
- `j` -> down to folder/file Navigation
- `h` -> minimize the folder
- `l` -> extend the folder/ or open file act like enter

### File Switching

- `l` -> on file  via file explorer then it's add into tab do with multiple file add into tab
- `shift l` and `shitf + h` to change the file tab l for right and h for left
- `<leader> + bd` to remove the file from tab

## Focus with toggle off

- `ctrl + w` then `ctrl + k` -> to focus on text editor from terminal
- `ctrl + w` then `ctrl + j` -> to focus on terminal from text editor **first press `ESC` to exit `INSERT` mode then work shortcut
- `ctrl + w` then `ctrl + h` -> focus on explorer from text editor
- `ctrl + w`  then `ctrl + l` -> focus on editor from explorer

## Text Manipulation

### Copy text
>
> all command start with `y` stand for **yank**

- in **nm** `yy` -> to copy current line
- in nm `yiw` -> only copy word where cursor keep
- in **nm** `y$` -> copy cursor to end line
- in **nm** `y0` -> copy cursor to beginning of line

### Delete Text
>
> all command start with `d` and  stand for **delete**
