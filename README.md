# dotfiles
My configuration files 

# installation 
Clone the repository
```shell
git clone https://github.com/bankubanku/dotfiles
```

Copy copy files accordingly:

- for desktop 
```shell
rsync -av --progress dotfiles/desktop/.local ~/.
rsync -av --progress dotfiles/desktop/.config ~/.
```

- for laptop 
```shell
rsync -av --progress dotfiles/laptop/.local ~/.
rsync -av --progress dotfiles/laptop/.config ~/.
```