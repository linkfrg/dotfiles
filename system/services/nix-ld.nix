{pkgs, ...}: {
  programs.nix-ld.enable = true;

  programs.nix-ld.libraries = with pkgs; [
    # Core runtime
    glibc
    stdenv.cc.cc
    zlib
    libgcc
    bash

    # Common system libs
    dbus
    expat
    libuuid
    libxcb
    libxkbcommon
    libdrm
    mesa

    # X11
    xorg.libX11
    xorg.libXcursor
    xorg.libXrandr
    xorg.libXinerama
    xorg.libXrender
    xorg.libXext
    xorg.libXi
    xorg.libXfixes
    xorg.libXdamage
    xorg.libXScrnSaver
    xorg.libXcomposite
    xorg.libXxf86vm

    # Wayland
    wayland
    wayland-protocols

    # Audio
    alsa-lib
    pipewire

    # Fonts / text
    freetype
    fontconfig
    harfbuzz
    pango
    cairo

    # Graphics & images
    libGL
    libGLU
    libpng
    libjpeg
    libwebp
    giflib
    gdk-pixbuf

    # Compression / archives
    bzip2
    xz
    zstd

    # Networking & crypto
    openssl
    curl
    libnghttp2
    krb5

    # GTK
    glib
    gtk3
    gtk4
    atk
    at-spi2-core
    at-spi2-atk

    # Misc
    nspr
    nss
    libnotify
    libsecret
    libcap
    libpulseaudio
    cups
  ];
}
