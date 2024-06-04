#! /bin/bash

# for this to work base base-devel git linux linux-firmware linux-headers must be installed 
echo "This configuration uses dependencies from aur. If you want to avoid using software from AUR, reconsider changing this configuration for your needs :3"
read -p "Do you still want to continue? (y/n): " answer

if [ "$answer" -ne "y" ]; then 
    exit 1
fi

sudo pacman -Syyu
sudo pacman -S rsync gvim alacritty bluez bluez-utils flameshot man-db nemo obsidian obs-studio qtile rofi signal-desktop syncthing ttf-jetbrains-mono-nerd ufw zip unzip wget noto-fonts noto-fonts-cjk noto-fonts-emoji noto-fonts-extra virtualbox lightdm lightdm-gtk-greeter pipewire pipewire-audio pipewire-alsa pipewire-pulse dosfstools efibootmgr gimp github-cli htop inkscape libreoffice-still mtools neovim nodejs npm p7zip python-dbus-next python-pip python-pipx python-psutil ripgrep rofi signal-desktop skanlite syncthing sysfsutils tree lutris xclip   
echo "packages from official arch repo installed"

amd=`cat /proc/cpuinfo | grep -i amd`
intel=`cat /proc/cpuinfo | grep -i intel`
if [ ${#amd} > 0 ]; then
    sudo pacman -S amd-ucode
    echo "amd-ucode installed"
elif [ ${#intel} > 0 ]; then
    sudo pacman -S intel-ucode
    echo "intel-ucode installed"
else 
    echo "Couldn't detect machine's cpu information. Install manually amd-ucode, intel-ucode or resolve your problem in other way"
fi 

git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
cd ..
rm -rf yay
echo "yay built"

yay -S activitywatch-bin betterlockscreen deadd-notification-center-bin freetube librewolf-bin qtile-extras ungoogled-chromium-bin vesktop-bin 
echo "packages from AUR installed"

sudo systemctl enable lightdm
sudo systemctl enable bluetooth

pwd=`pwd`

mv ~/.config/alacritty ~/.config/_alacritty
mv ~/.config/nvim/  ~/.config/_nvim/
mv ~/.config/qtile ~/.config/_qtile
mv ~/.config/rofi/config.rasi  ~/.config/rofi/_config.rasi
mv ~/.config/deadd ~/.config/_dead
echo "backed up config files"

ln -s ${pwd}/alacritty ~/.config/alacritty
mkdir ~/.config/deadd/
ln -s ${pwd}/deadd ~/.config/deadd
ln -s ${pwd}/nvim ~/.config/nvim
ln -s ${pwd}/qtile ~/.config/qtile
mkdir ~/.config/rofi/
ln -s ${pwd}/rofi/config.rasi ~/.config/rofi/config.rasi
mkdir -p ~/.local/share/rofi/themes/
ln -s ${pwd}/rofi/catppuccin-frappe.rasi ~/.local/share/rofi/themes/catppuccin-frappe.rasi
echo "created symbolic links for config files"

echo "now your OS will reboot"
sudo reboot
