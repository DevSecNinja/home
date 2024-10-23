apt update
apt -y install git curl zsh
git clone https://github.com/DevSecNinja/dotfiles.git ~/.dotfiles
cd ~/.dotfiles
script/bootstrap
