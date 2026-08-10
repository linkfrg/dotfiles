vim.pack.add({ { src = "https://github.com/folke/which-key.nvim", name = "which-key" } })

require("which-key").setup({
  delay = 0,
  icons = { mappings = vim.g.have_nerd_font },

  spec = {
    { "<leader>s", group = "[S]earch", mode = { "n", "v" } },
    { "<leader>y", group = "[Y]azi", mode = { "n", "v" } },
    { "<leader>a", group = "LSP [A]ctions", mode = { "n" } },
  },
})
