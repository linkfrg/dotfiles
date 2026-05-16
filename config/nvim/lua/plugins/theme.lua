vim.pack.add({ { src = "https://github.com/catppuccin/nvim", name = "catppuccin" } })

require("catppuccin").setup({
  flavour = "mocha",
})

vim.cmd.colorscheme("catppuccin-nvim")
