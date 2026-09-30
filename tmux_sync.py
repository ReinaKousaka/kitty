# One place for all shortcuts: key -> (kitty action, tmux key after prefix or None)
# Loaded by kitty.conf via `geninclude tmux_sync.py`.
# Inside tmux, kitty sends `prefix + <tmux key>`, using tmux's default bindings,
# so the remote needs no config. (Typing `prefix :cmd` in one burst does not work.)
PREFIX = r"\x02"          # tmux prefix, Ctrl+b (use \x01 for Ctrl+a)
IN_TMUX = "title:^tmux"   # "tmux" (set by remote shell) or "tmux: ..." (tmux set-titles)

LEFT, RIGHT, UP, DOWN = r"\x1b[D", r"\x1b[C", r"\x1b[A", r"\x1b[B"

BINDINGS = {
    "ctrl+shift+9": ("launch --location=vsplit --cwd=current", "%"),   # side by side
    "ctrl+shift+0": ("launch --location=hsplit --cwd=current", '"'),   # top / bottom
    "ctrl+shift+z": ("toggle_layout stack",                    "z"),   # zoom pane
    "ctrl+shift+w": ("close_window",                           "x"),   # close pane (tmux asks y/n)
    "alt+left":     ("neighboring_window left",                LEFT),
    "alt+right":    ("neighboring_window right",               RIGHT),
    "alt+up":       ("neighboring_window up",                  UP),
    "alt+down":     ("neighboring_window down",                DOWN),
    "kitty_mod+t":  ("new_tab_with_cwd",                       "c"),   # new tmux window
    "ctrl+page_up":   ("previous_tab",                         "p"),   # previous tmux window
    "ctrl+page_down": ("next_tab",                             "n"),   # next tmux window
}

for key, (kitty_action, tmux_key) in BINDINGS.items():
    print(f"map {key} {kitty_action}")
    if tmux_key:
        print(f"map --when-focus-on {IN_TMUX} {key} send_text all {PREFIX}{tmux_key}")
