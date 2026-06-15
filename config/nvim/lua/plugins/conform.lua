vim.pack.add({ { src = "https://github.com/stevearc/conform.nvim", name = "conform" } })
require("conform").setup({
  notify_on_error = true,
  format_on_save = {
    timeout_ms = 500,
    lsp_format = "fallback",
  },
  formatters_by_ft = {
    lua = { "stylua" },
    python = {
      -- To fix auto-fixable lint errors.
      "ruff_fix",
      -- To run the Ruff formatter.
      "ruff_format",
      -- To organize the imports.
      "ruff_organize_imports",
    },
    markdown = { "prettier", "cbfmt" },
    nix = { "alejandra" },
  },
})

vim.keymap.set("n", "<leader>f", function()
  require("conform").format({ async = true, lsp_format = "fallback" })
end, { desc = "[F]ormat buffer" })
