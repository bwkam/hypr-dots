#!/usr/bin/bash

# vars
config=$HOME/.config/hypr
scripts=$HOME/.config/hypr/scripts

# notification
dunst &

# waybar
$scripts/launch_waybar &
# $scripts/tools/dynamic &


# wallpaper
sh $scripts/background-changer &

# other
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP &
