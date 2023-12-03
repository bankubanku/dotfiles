# rofi config 
It is just copy-paste config from [catppuccin](https://github.com/catppuccin) profile. I included it in my own repo to keep everything in one place and leave myself the ability to customize it in the future, but for now I recommend checking the [original repo](https://github.com/catppuccin/rofi).

# installation 
## prerequisites 
- [rofi](https://github.com/davatorium/rofi)

## symbolic links
change the name of your current config if you want to keep it 
```shell
mv ~/.config/rofi/config.rasi  ~/.config/rofi/_config.rasi
```
or just delete it (I wouldn't do that, tho)
```shell
rm -rf ~/.config/rofi/config.rasi 
``` 
create a symbolic links 
```shell
ln -s ~/dotfiles/rofi/config.rasi ~/.config/rofi/config.rasi
ln -s ~/dotfiles/rofi/catppuccin-frappe.rasi ~/.local/share/rofi/themes/catppuccin-frappe.rasi
```

## copying 
change the name of your current config if you want to keep it 
```shell
mv ~/.config/rofi/config.rasi  ~/.config/rofi/_config.rasi
```
copy the config files 
```shell
cp ~/dotfiles/rofi/config.rasi ~/.config/rofi/config.rasi
cp ~/dotfiles/rofi/catppuccin-frappe.rasi ~/.local/share/rofi/themes/catppuccin-frappe.rasi
```