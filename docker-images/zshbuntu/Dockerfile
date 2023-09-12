ARG UBUNTU_VERSION=23.04
FROM ubuntu:${UBUNTU_VERSION}

RUN apt update
RUN apt install -y zsh sudo systemd vim iputils-ping curl && \
    # apt install -y python3 pip && \
    apt install -y git tig

# Creating user
RUN useradd -rm -d /home/sandbox -s /usr/bin/zsh -g root -G root -u 1001 sandbox && \
    echo "sandbox ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/sudoers

USER sandbox
WORKDIR /home/sandbox

RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
RUN git clone --depth=1 https://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions && \
    git clone --depth=1 https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting && \
    git clone --depth=1 https://github.com/akarzim/zsh-docker-aliases.git  ~/.oh-my-zsh/custom/plugins/zsh-docker-aliases && \
    sed -i 's/plugins=(git)/plugins=(git zsh-autosuggestions zsh-syntax-highlighting zsh-docker-aliases)/' .zshrc && \
    git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/.oh-my-zsh/custom/themes/powerlevel10k && \
    sed -i 's|ZSH_THEME=.*|ZSH_THEME="powerlevel10k/powerlevel10k"|' .zshrc

RUN git config --global init.defaultBranch main && \
    git config --global user.name "Ubuntu Sandbox" && \
    git config --global user.email "sandbox@ubuntu.sanbdox.com"

CMD ["zsh"]