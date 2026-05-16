vim.pack.add({ { src = "https://github.com/folke/which-key.nvim", name = "which-key" } })

require("which-key").setup({
  delay = 0,
  icons = { mappings = vim.g.have_nerd_font },

  spec = {
    { "<leader>s", group = "[S]earch", mode = { "n", "v" } },
    { "gr", group = "LSP Actions", mode = { "n" } },
  },
})
