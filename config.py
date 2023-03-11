# Qtile dot
#
# Pretty stuff is caused by pywal, feh[-blur], and jonaburg-picom.


from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

import os


#  Keys

mod = "mod4"
terminal = guess_terminal()

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

    # Other keybinds that may prove useful
    Key([mod], "a", lazy.spawn("rofi -config ~/.cache/wal/colors-rofi-dark.rasi -show run &"), desc="Launch rofi in run mode"),
]


#  Colors

colors = []

def init_colors():
    cache='/home/ursa/.cache/wal/colors'
    with open(cache, 'r') as file:
        for i in file.readlines():
            colors.append(i.strip())
init_colors()


#  Workstations

def init_group_names():
    return [
     (" ", {'layout': 'floating'}),
     (" ", {'layout': 'monadtall'}),
     (" ", {'layout': 'monadtall'}),
     (" ", {'layout': 'monadtall'}),
     (" ", {'layout': 'stack'}),
     (" ", {'layout': 'monadwide'}),
     (" ", {'layout': 'stack'}),
     (" ", {'layout': 'monadwide'})]

def init_groups():
    return [Group(name, **kwargs) for name, kwargs in group_names]

if __name__ in ["config", "__main__"]:
    group_names = init_group_names()
    groups = init_groups()

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen())) # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group


#  Layouts

layouts = [
    layout.Columns(border_focus_stack=[colors[7], colors[0]], border_width=1),
    layout.MonadTall(
        border_focus = colors[7],
        border_normal = colors[0],
        border_width = 1,
        margin = 30,
        min_ratio = 0.7,
        ratio = 0.7,
        single_margin = 30),
    layout.MonadWide(
        border_focus = colors[7],
        border_normal = colors[0],
        border_width = 1,
        margin = 30,
        min_ratio = 0.7,
        ratio = 0.7,
        single_margin = 30),
    layout.Stack(
        border_focus = colors[7],
        border_normal = colors[0],
        margin = 30,
        num_stacks = 1),
    layout.Floating(
        border_focus = colors[7],
        border_normal = colors[0]),
]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()


# ⎚ Screens

screens = [
    Screen(
        top=bar.Bar(
            [
            widget.Sep(
                linewidth = 0, 
                padding = 50),
            widget.GroupBox(
                font = "FiraCode Nerd Font", 
                block_highlight_text_color = colors[0],
                highlight_method = "block",
                this_screen_border = colors[7],
                this_current_screen_border = colors[7],
                urgent_alert_method = "block",
                urgent_border = colors[4],
                urgent_text = colors[0],
                fontsize = 15, 
                margin_y = 3, 
                margin_x = 5, 
                padding_y = 5, 
                padding_x = 5, 
                borderwidth = 4, 
                active = colors[7], 
                inactive = colors[1], 
                foreground = colors[7]),
            widget.Sep(
                linewidth = 0,
                padding = 50),
            widget.Spacer(length = bar.STRETCH),
            widget.Battery(
                format = "{char} {percent:2.0%}",
                battery = "BAT0",
                charge_char = "",
                discharge_char = "",
                empty_char = "",
                font = "FiraCode Nerd Font",
                fontsize = 15,
                foreground = colors[7],
                full_char = "",
                low_foreground = colors[1],
                low_percentage = 0.15,
                notify_below = 0.15,
                unknown_char = ""),
            widget.Sep(
                linewidth = 0,
                padding = 50),
            widget.TextBox(text = "", fontsize = "25", foreground = colors[7]),
            widget.Wlan(
                disconnected_message = "✗",
                font = "FiraCode Nerd Font",
                fontsize = 15,
                foreground = colors[7],
                format = "{essid} {percent:2.0%}"),
            widget.Sep(
                linewidth = 0,
                padding = 50),
            widget.TextBox(text = "", fontsize = "25", foreground = colors[7]),
            widget.Clock(
                format = '%H:%M', 
                font = "FiraCode Nerd Font",
                fontsize = 15,
                foreground = colors[7]),
            widget.Sep(
                linewidth = 0,
                padding = 50)
            ],
            24,
            background = colors[0],
            margin = [15, 30, -15, 30]
        ),
    ),
]


#  Mouse

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True


#  Misc

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
