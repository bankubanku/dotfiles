# alacritty config 
It is just copy-paste config from [catppuccin](https://github.com/catppuccin) profile. I included it in my own repo to keep everything in one place and leave myself the ability to customize it in the future, but for now I recomend checking the [original repo](https://github.com/catppuccin/alacritty). 

# installation 
## prerequisites 
- [alacritty](https://alacritty.org/)

## symbolic links 
change the name of your current config if you want to keep it 
```shell
mv ~/.config/alacritty/alacritty.yml  ~/.config/alacritty/_alacritty.yml
```
or just delete it (I wouldn't do that, tho)
```shell
rm -rf ~/.config/alacritty/alacritty.yml
``` 
create symbolic links 
```shell
ln -s ~/dotfiles/alacritty/alacritty.yml ~/.config/alacritty/alacritty.yml
ln -s ~/dotfiles/alacritty/catppuccin-macchiato.yml ~/.config/alacritty/catppuccin-macchiato.yml
```

## copying 
change the name of your current config if you want to keep it 
```shell
mv ~/.config/alacritty/alacritty.yml  ~/.config/alacritty/_alacritty.yml
```
copy the config files 
```shell
cp ~/dotfiles/alacritty/*.yml ~/.config/alacritty/
```