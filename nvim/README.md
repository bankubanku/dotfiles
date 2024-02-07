# neovim config 
My personalized [neovim](https://neovim.io/) config that is based on [kickstart.nvim](https://github.com/nvim-lua/kickstart.nvim) and on which I'm currently working on. 

# installation
## prerequisites
- [neovim](https://neovim.io/)
## symbolic links 
change the name of your current config if you want to keep it 
```shell
mv ~/.config/nvim/  ~/.config/_nvim/
```
or just delete it (I wouldn't do that, tho)
```shell
rm -rf ~/.config/nvim/
``` 
create symbolic links 
```shell
ln -s ~/dotfiles/nvim/ ~/.config/nvim/
```

## copying 
change the name of your current config if you want to keep it 
```shell
mv ~/.config/nvim/  ~/.config/_nvim/
```
copy the config files 
```shell
cp ~/dotfiles/nvim/ ~/.config/nvim/
```
