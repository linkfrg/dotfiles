export FZF_HEIGHT="40%"

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

install_fzf() {
    if command_exists fzf; then
        echo "fzf is already installed."
    else
        echo "fzf is not installed. Installing fzf..."

        # Clone fzf repository from GitHub
        sudo pacman -S fzf
    fi
}

install_figlet() {
    if command_exists figlet; then
        echo "figlet is already installed."
    else
        echo "figlet is not installed. Installing figlet..."
        # Install figlet
        sudo pacman -S figlet
    fi
}

install_git() {
    if command_exists git; then
        echo "git is already installed."
    else
        echo "git is not installed. Installing git..."
        # Install git
        sudo pacman -S git
    fi
}

# Function to install yay
install_yay() {
    if command_exists yay; then
        echo "yay is already installed."
    else
        echo "yay is not installed. Installing yay..."

        # Update system packages
        sudo pacman -Syu --noconfirm

        # Install base-devel and git if not already installed
        sudo pacman -S --needed --noconfirm base-devel git

        # Clone yay repository from the AUR
        git clone https://aur.archlinux.org/yay.git

        # Change directory to yay folder
        cd yay

        # Build and install yay
        makepkg -si --noconfirm

        # Go back to the original directory
        cd ..

        # Clean up by removing the yay directory
        rm -rf yay

        echo "yay has been successfully installed."
    fi
}


# Function to install paru
install_paru() {
    if command_exists paru; then
        echo "paru is already installed."
    else
        echo "paru is not installed. Installing paru..."

        # Update system packages
        sudo pacman -Syu --noconfirm

        # Install base-devel and git if not already installed
        sudo pacman -S --needed --noconfirm base-devel git

        # Clone paru repository from the AUR
        git clone https://aur.archlinux.org/paru.git

        # Change directory to paru folder
        cd paru

        # Build and install paru
        makepkg -si --noconfirm

        # Go back to the original directory
        cd ..

        # Clean up by removing the paru directory
        rm -rf paru

        echo "paru has been successfully installed."
    fi
}

# Function to remove certain packages
remove_packages() {
    # List of packages to remove (space-separated)
    packages_to_remove=("dunst") # Replace with actual package names

    # Check if packages are installed and remove them
    if pacman -Q "${packages_to_remove[@]}" &>/dev/null; then
        echo "Removing packages: ${packages_to_remove[*]}"
        killall ${packages_to_remove[@]} 2>/dev/null
        sudo pacman -Rns --noconfirm "${packages_to_remove[@]}"
    else
        echo "One or more packages are not installed."
    fi
}

continue_prompt() {
    # Color variables
    GREEN="\e[32m"
    RED="\e[31m"
    CYAN="\e[36m"
    BOLD="\e[1m"
    RESET="\e[0m"

    while true; do
        echo -e "${CYAN}${BOLD}$1${RESET} ${GREEN}[Y]${RESET}/${RED}[N]${RESET}: "
        read -p "" choice
        case "$choice" in
        [Yy]*)
            echo -e "${GREEN}Great! Continuing...${RESET}"
            $2
            break
            ;;
        [Nn]*)
            echo -e "${RED}Okay, exiting...${RESET}"
            break
            ;;
        *) echo -e "${RED}Please answer with Y or N.${RESET}" ;;
        esac
    done
}
