# Setup on a new machine

Branches: `macos` (cmd-based shortcuts) and `main` (Debian/Linux, ctrl+shift-based).

## macOS laptop

```sh
brew install --cask kitty
brew install tmux fzf
git clone -b macos git@github.com:ReinaKousaka/kitty.git ~/.config/kitty
ln -sf ~/.config/kitty/tmux.conf ~/.tmux.conf
git clone https://github.com/nordtheme/tmux ~/.tmux/themes/nord-tmux
# optional: TPM plugins (tmux-sensible), then prefix + I inside tmux
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
```

Restart kitty (or cmd+ctrl+, to reload). The font `consolas` must be installed;
the Nord status bar needs a Powerline/Nerd font for its separators.

## Remote (SSH) machine

Only tmux is needed there; kitty translates cmd shortcuts into tmux prefix keys.

```sh
scp ~/.config/kitty/tmux.conf <host>:~/.tmux.conf
ssh <host> 'git clone https://github.com/nordtheme/tmux ~/.tmux/themes/nord-tmux'
```

Inside an already running tmux server: `tmux source ~/.tmux.conf`.

## How the kitty <-> tmux shortcuts work

kitty maps keys with `--when-focus-on=title:tmux$`. tmux.conf sets the window
title to `<host>:<session> tmux`, so when tmux is focused kitty sends the
tmux prefix (ctrl+b, `\x02`) plus the tmux key instead of acting itself:

| key            | kitty (no tmux)        | tmux         |
|----------------|------------------------|--------------|
| cmd+t          | new tab                | new window   |
| cmd+shift+9/0  | vsplit / hsplit        | `%` / `"`    |
| cmd+shift+z    | zoom split             | `z`          |
| cmd+shift+w    | close split            | kill pane    |
| cmd+arrows     | move between splits    | select pane  |
| cmd+page_up/dn | previous / next tab    | `p` / `n`    |

If a shortcut acts on kitty instead of tmux, check the tab title ends in
`tmux` (`tmux show -g set-titles` must be `on`).
