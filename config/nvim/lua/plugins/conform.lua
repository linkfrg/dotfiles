vim.pack.add({ { src = "https://github.com/stevearc/conform.nvim", name = "conform" } })
require("conform").setup({
  notify_on_error = true,
  formatters_by_ft = {
    lua = { "stylua" },
    python = { "ruff" },
  },
})

vim.keymap.set("n", "<leader>f", function()
  require("conform").format({ async = true, lsp_format = "fallback" })
end, { desc = "[F]ormat buffer" })
