-- [[ Setting options ]]
-- See `:help vim.o`
-- NOTE: You can change these options as you wish!

-- Set highlight on search
vim.o.hlsearch = true

-- Make line numbers default
vim.wo.number = true

-- Enable mouse mode
vim.o.mouse = 'a' -- this option let user use mouse in all modes 

-- Sync clipboard between OS and Neovim.
vim.o.clipboard = 'unnamedplus'

-- Enable break indent; smart wrap (i think?)
vim.o.breakindent = true

-- Save undo history
vim.o.undofile = true

-- Case-insensitive searching 
vim.o.ignorecase = true
-- UNLESS \C or capital in search
vim.o.smartcase = true

-- this column next to the line number column
vim.wo.signcolumn = 'yes'

-- saves buffer to swap after given time
vim.o.updatetime = 250
-- set amount of time to wait for a key code sequence to complete 
vim.o.timeoutlen = 300

-- changes completion experience
vim.o.completeopt = 'menuone,noselect'

-- checks host termina's capability and enables 24-bit RGB color
-- NOTE: You should make sure your terminal supports this
vim.o.termguicolors = true

