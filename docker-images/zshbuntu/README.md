Welcome to ZSHbuntu – Your Ultimate Ubuntu Image with Zsh Magic!

Discover a world of command-line sophistication with our ZSHbuntu Docker image. We've curated the perfect Ubuntu environment enhanced with the power of Zsh, Oh-My-Zsh. Elevate your terminal experience with this feature-packed image, designed to boost your productivity and style.

Whether you're a developer, system administrator, or terminal enthusiast, ZSHbuntu empowers you with a captivating, efficient, and fun command-line experience. Download now and unlock the full potential of your Ubuntu-based containers.

## Key Features:

- Ubuntu base with [Zsh](https://en.wikipedia.org/wiki/Z_shell) magic.
- [Oh-My-Zsh](https://ohmyz.sh) for enhanced shell capabilities.
- [Powerlevel10k](https://github.com/romkatv/powerlevel10k) for eye-catching, customizable prompts.
- [Syntax highlighting](https://github.com/zsh-users/zsh-syntax-highlighting) for code clarity.
- Vibrant [auto-suggestions](https://github.com/zsh-users/zsh-autosuggestions) for faster typing.
- [Zsh Docker Aliases](https://github.com/akarzim/zsh-docker-aliases) for streamlined container management.

## Modules Installed
zsh, sudo, systemd, vim, iputils-ping, curl, git, tig

## How to Use ZSHbuntu

### Create a Docker Volume:
- Create a Docker volume named "zshbuntu-sandbox" by running the following command:
```shell
docker volume create zshbuntu-sandbox
```
- This volume will be used to store and reuse your configuration and setups.

### Run the ZSHbuntu Docker Sandbox:
- To run the Docker image with the previously created volume mounted to `/home/sandbox` for the user **"sandbox"**, use the following command:
```shell
docker run --name sandbox -v zshbuntu-sandbox:/home/sandbox --rm -it macabrequinox/zshbuntu:23.04
```
- This command starts the ZSHbuntu Docker container, providing you with a secure and permission-free environment to run commands and experiment.

Now you're ready to enjoy your ZSHbuntu Docker Sandbox, where you can safely execute commands without worrying about permissions or security issues. Feel free to customize your environment and configurations within the sandbox, and any changes will be stored in the "zshbuntu-sandbox" volume for future use.

## Contribute
On [github](https://github.com/snigdhasjg/playground/tree/main/docker-images/zshbuntu)

---
Tags: #Ubuntu #Zsh #OhMyZsh #Powerlevel10k #SyntaxHighlighting #AutoSuggestions #DockerImage #CommandLine #DeveloperTools #Productivity