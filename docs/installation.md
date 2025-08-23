# Installation

## Clone repository

```
git clone https://github.com/linkfrg/dotfiles.git --depth 1 --branch main
```

## Copy config files

```
cd dotfiles
mkdir -p ~/.local/share/themes
cp -R .config/* ~/.config/
cp -R ignis ~/.config/
cp -R Material ~/.local/share/themes
```

## Install dependencies

Firstly, you need to install AUR helper (e.g., paru).

```
paru -S --needed - < dependencies.txt
```

If using nvidia install also
```
paru -S --needed - < nvidia_deps.txt
```

## Install tide prompt

Install fisher.

```bash
paru -S fisher
```

Install tide.

```bash
fisher install IlanCosman/tide@v6
```

Configure tide prompt.

```bash
tide configure --auto --style=Rainbow --prompt_colors='16 colors' --show_time=No --rainbow_prompt_separators=Angled --powerline_prompt_heads=Sharp --powerline_prompt_tails=Round --powerline_prompt_style='Two lines, frame' --prompt_connection=Disconnected --powerline_right_prompt_frame=Yes --prompt_spacing=Sparse --icons='Many icons' --transient=No
```
