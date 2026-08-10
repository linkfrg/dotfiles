vim.pack.add({ "https://github.com/folke/todo-comments.nvim" })

require("todo-comments").setup({})

vim.keymap.set("n", "<leader>sc", "<cmd>TodoTelescope<CR>", { desc = "[S]earch [C]omments" })
