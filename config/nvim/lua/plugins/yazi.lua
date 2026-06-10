vim.pack.add({
  "https://github.com/mikavilpas/yazi.nvim",
  "https://github.com/nvim-lua/plenary.nvim",
})

require("yazi").setup({
  open_for_directories = true,
  keymaps = {
    show_help = "<f1>",
  },
})

vim.g.loaded_netrwPlugin = 1

vim.keymap.set("n", "<leader>yf", "<cmd>Yazi<cr>", { desc = "Open [Y]azi at the current [F]ile" })
vim.keymap.set("n", "<leader>yd", "<cmd>Yazi cwd<cr>", { desc = "Open the file manager in nvim's working directory" })
