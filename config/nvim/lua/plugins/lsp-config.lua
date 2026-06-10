vim.pack.add({
  "https://github.com/neovim/nvim-lspconfig",
  "https://github.com/j-hui/fidget.nvim",
})

require("fidget").setup({})

local servers = {
  pyright = {},
  rust_analyzer = {},
  nil_ls = {},
  mesonlsp = {},
  marksman = {},

  stylua = {},
  lua_ls = {
    on_init = function(client)
      client.server_capabilities.documentFormattingProvider = false -- Disable formatting (formatting is done by stylua)

      if client.workspace_folders then
        local path = client.workspace_folders[1].name
        if
          path ~= vim.fn.stdpath("config")
          and (vim.uv.fs_stat(path .. "/.luarc.json") or vim.uv.fs_stat(path .. "/.luarc.jsonc"))
        then
          return
        end
      end

      client.config.settings.Lua = vim.tbl_deep_extend("force", client.config.settings.Lua, {
        runtime = {
          version = "LuaJIT",
          path = { "lua/?.lua", "lua/?/init.lua" },
        },
        workspace = {
          checkThirdParty = false,
          -- NOTE: this is a lot slower and will cause issues when working on your own configuration.
          --  See https://github.com/neovim/nvim-lspconfig/issues/3189
          library = vim.tbl_extend("force", vim.api.nvim_get_runtime_file("", true), {
            "${3rd}/luv/library",
            "${3rd}/busted/library",
          }),
        },
      })
    end,

    settings = {
      Lua = {
        format = { enable = false }, -- Disable formatting (formatting is done by stylua)
      },
    },
  },
}

for name, server in pairs(servers) do
  vim.lsp.config(name, server)
  vim.lsp.enable(name)
end
