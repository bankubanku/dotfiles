require "nvchad.options"

local options = {
  hlsearch = false, -- Set highlight on search
  incsearch = true, -- shows the matches for the current search pattern as you type it 
  mouse = 'a', -- Enable mouse mode
  clipboard = 'unnamedplus', -- Sync clipboard between OS and Neovim.
  undofile = true, -- Save undo history
  ignorecase = true,  -- Case-insensitive searching 
  smartcase = true, -- case-sensitive searching when capital letter typed 
  signcolumn = 'yes', -- this column next to the line number column
  updatetime = 250, -- saves buffer to swap after given time
  timeoutlen = 300, -- set amount of time to wait for a key code sequence to complete 
  completeopt = 'menuone,noselect', -- changes completion experience
  termguicolors = true, -- checks host terminal's capability and enables 24-bit RGB color
  number = true, -- adds number column on the left 
  relativenumber = true, -- makes number column relative
  cursorline = true,   -- highlight the line where cursor is currently positioned 
  cursorlineopt = 'number,line', -- what to highlight
  scrolloff = 10,   -- sets up number of lines to keep above and below the cursor when scrolling 
  smartindent = true,   -- neovim analyzes the code and controls indentation based on the syntax 
  expandtab = true, -- spaces instead of tab character
  tabstop = 4, -- width of the tab character 
  shiftwidth = 4, -- determines the size of indentation when using `<<`, `>>' or automatic features like autoindent or smartindent
  softtabstop = 4, -- controls the bahavior of the tab key in insert mode when 'expandtab' is enabled 
  autoindent = true,  -- automaticaly indents the indentation level of current line when you start a new line 
  breakindent = true,  -- maintains the indentation level, even if the new line is wrapped 
  wrap = true,  -- wraps line when it is no longer visible in neovim window 
  linebreak = true,  -- controls wrapping based on breakat option (only specified character) 
}

for k, v in pairs(options) do
  vim.opt[k] = v
end
