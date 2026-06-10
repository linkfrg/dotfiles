vim.api.nvim_create_autocmd("FileType", {
  pattern = "markdown",
  once = true,
    callback = function()
    vim.pack.add({
      "https://github.com/MeanderingProgrammer/render-markdown.nvim",
      "https://github.com/dhruvasagar/vim-table-mode",
    })

    require("render-markdown").setup({})
  end,
})
