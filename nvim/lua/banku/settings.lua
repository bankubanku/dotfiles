-- Set highlight on search
vim.opt.hlsearch = false

-- shows the matches for the current search pattern as you type it 
vim.opt.incsearch = true

-- Enable mouse mode
vim.opt.mouse = 'a'

-- Sync clipboard between OS and Neovim.
vim.opt.clipboard = 'unnamedplus'

-- Save undo history
vim.opt.undofile = true

-- Case-insensitive searching 
vim.opt.ignorecase = true
vim.opt.smartcase = true

-- this column next to the line number column
vim.opt.signcolumn = 'yes'

-- saves buffer to swap after given time
vim.opt.updatetime = 250

-- set amount of time to wait for a key code sequence to complete 
vim.opt.timeoutlen = 300

-- changes completion experience
vim.opt.completeopt = 'menuone,noselect'

-- checks host terminal's capability and enables 24-bit RGB color
-- NOTE: You should make sure your terminal supports this
vim.opt.termguicolors = true

-- enabling the column of number on the left 
vim.opt.number = true
vim.opt.relativenumber = true

-- highlight the line where cursor is currently positioned 
vim.opt.cursorline = true
vim.opt.cursorlineopt = 'number,line'

-- sets up number of lines to keep above and below the cursor when scrolling 
vim.opt.scrolloff = 10

-- neovim analyzes the code and controls indentation based on the syntax 
vim.opt.smartindent = true

-- size of indentation
vim.opt.tabstop = 4
vim.opt.shiftwidth = 4
vim.opt.softtabstop = 4

-- automaticaly indents the indentation level of current line when you start a new line 
vim.opt.autoindent = true

-- maintains the indentation level, even if the new line is wrapped 
vim.opt.breakindent = true

-- wraps line when it is no longer visible in neovim window 
vim.opt.wrap = true

-- controls wrapping based on breakat option (only specified character) 
vim.opt.linebreak = true
