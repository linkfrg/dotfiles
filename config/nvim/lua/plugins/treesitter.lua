vim.pack.add({ "https://github.com/nvim-treesitter/nvim-treesitter" })

local parsers = {
  "diff",
  "markdown",
  "markdown_inline",
  "query",
  "vim",
  "vimdoc",
  "bash",
  "c",
  "lua",
  "luadoc",
  "python",
  "rust",
}
require("nvim-treesitter").install(parsers)

vim.api.nvim_create_autocmd("FileType", {
  callback = function(args)
    local buf, filetype = args.buf, args.match

    local language = vim.treesitter.language.get_lang(filetype)

    if language and vim.treesitter.language.add(language) then
      vim.treesitter.start(buf, language)
      vim.bo.indentexpr = "v:lua.require'nvim-treesitter'.indentexpr()"
    end
  end,
})
