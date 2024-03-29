# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import subprocess

import psutil

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration

from libqtile import hook

mod = "mod4"
terminal = 'alacritty'
do_not_disturb = False


def clear_notifications(qtile):
    subprocess.run('notify-send.py a --hint boolean:deadd-notification-center:true string:type:clearInCenter', shell=True)

'''
    work in progress
'''
# def mute_notifications(qtile):
#     global do_not_disturb
#     if do_not_disturb:
#         subprocess.run('notify-send "do not disturb: enabled"', shell=True)
#         subprocess.run('notify-send.py a --hint boolean:deadd-notification-center:true string:type:unpausePopups', shell=True)
#         do_not_disturb = True
#     else: 
#         subprocess.run('notify-send.py a --hint boolean:deadd-notification-center:true string:type:pausePopups', shell=True)
#         subprocess.run('notify-send "do not disturb: disabled', shell=True)
#         do_not_disturb = False


def open_notification_center(qtile):
    subprocess.run('kill -s USR1 $(pidof deadd-notification-center)', shell=True) 

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
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
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, "control"], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # run software
    Key([], 'Print', lazy.spawn('flameshot gui')),
    Key([mod], 'r', lazy.spawn('rofi -show drun')),
    Key([mod], 'e', lazy.spawn('rofi -show window')),
    Key([mod], "t", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "n", lazy.function(open_notification_center)),
    # Key([mod], "m", lazy.function(mute_notifications)),
    Key([mod], "b", lazy.function(clear_notifications)),

    # lock screen 
    Key([mod], "comma", lazy.spawn('betterlockscreen -l'), desc="Lock screen"),

    # use next screen
    Key([mod], 'period', lazy.next_screen(), desc='Next monitor'),
]

groups = [
    Group('1', label=""),
    Group('2', label="", spawn="librewolf"),
    Group('3', label="", spawn="alacritty"),
    Group('4', label=""),
    Group('5', label=""),
    Group('6', label=""),
    Group('7', label=""),
    Group('8', label=""),
    Group('9', label="", spawn="obsidian")]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(
                    i.name),
            ),
        ]
    )

# colors 
base = '#24273a'
blue = '#8aadf4'
mauve = '#c6a0f6'
text = '#cad3f5'
subtext = '#8087a2'
pink = '#f5bde6'
flamingo = '#f0c6c6'
red='#ed8796'

layouts = [
    layout.Columns(border_focus=mauve, border_normal=flamingo, border_on_single=True, border_width=3,  
                   margin=10, fair=True, wrap_focus_stack=False),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # slayout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Slice()
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Open Sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

powerline = {
    "decorations": [
        PowerLineDecoration(path='rounded_right')
    ]
}

widgets = [
                widget.GroupBox(highlight_method='text', block_highlight_text_color='#c6f0fa', fontsize=12, active=flamingo, inactive=subtext),
                widget.Sep(foreground=text),
                widget.WindowTabs(foreground=text, **powerline),
                widget.Clock(padding=10, format="%d:%m:%Y %a %H:%M", background=blue, **powerline),
                widget.CurrentLayout(padding=10, background=mauve),
                
            ]


if psutil.sensors_battery() is not None:
    widgets.insert(3, widget.Battery(padding=10, background=mauve, **powerline))

screens = [
    Screen(
        wallpaper='~/dotfiles/wallpapers/wired.jpg', # wallpaper from my dotfiles repo 
        wallpaper_mode='stretch',
        top=bar.Bar(widgets,30,background=base),
    ),
    Screen(
        wallpaper='~/.config/wallpaper/wired.jpg',
        wallpaper_mode='stretch',
        top=bar.Bar(
            [
                widget.WindowTabs(foreground=text, **powerline),
                widget.Clock(padding=10, format="%d:%m:%Y %a %H:%M", background=blue, **powerline),
                widget.CurrentLayout(padding=10, background=mauve)
            ],
            30,
            background=base
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# for java apps to work
wmname = "LG3D"


@hook.subscribe.startup_once
def start_deadd():
    subprocess.Popen(["deadd-notification-center"])
