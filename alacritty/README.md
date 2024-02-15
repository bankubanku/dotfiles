# alacritty config 
It is just copy-paste config from [catppuccin](https://github.com/catppuccin) profile. I included it in my own repo to keep everything in one place and leave myself the ability to customize it in the future, but for now I recomend checking the [original repo](https://github.com/catppuccin/alacritty). 

# installation 
## prerequisites 
- [alacritty](https://alacritty.org/)

## backup 
change the name of your current config if you want to keep it 
```shell
mv ~/.config/alacritty ~/.config/_alacritty
```
or just delete it (I wouldn't do that, tho)
```shell
rm -rf ~/.config/alacritty
```

## symbolic links 
```shell
ln -s ~/dotfiles/alacritty ~/.config/alacritty
```

## copying 
```shell
cp ~/dotfiles/alacritty ~/.config/alacritty
```
