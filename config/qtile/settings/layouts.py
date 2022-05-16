# Modificador por Josué Romero
# Creador Antonio Sarosi
# https://twitter.com/josueromr
# https://github.com/josuerom/Install-ArchLinux

from libqtile import layout
from libqtile.config import Match
from .theme import colors

# Layouts and layout rules
layout_conf = {
    'border_focus': colors['focus'][0],
    'border_width': 1,
    'margin': 3
}

layouts = [
    layout.MonadTall(**layout_conf),
    layout.Max(),
    layout.Matrix(columns=2, **layout_conf),
    layout.MonadWide(**layout_conf),
    layout.Bsp(**layout_conf),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),
        Match(wm_class='makebranch'),
        Match(wm_class='maketag'),
        Match(wm_class='ssh-askpass'),
        Match(title='branchdialog'),
        Match(title='pinentry'),
    ],
    border_focus=colors["color4"][0]
)
