local opts = { noremap = true, silent = true }

-- Move to previous/next
vim.keymap.set('n', '<A-,>', '<Cmd>BufferPrevious<CR>', opts)
vim.keymap.set('n', '<A-.>', '<Cmd>BufferNext<CR>', opts)
-- Re-order to previous/next
vim.keymap.set('n', '<A-<>', '<Cmd>BufferMovePrevious<CR>', opts)
vim.keymap.set('n', '<A->>', '<Cmd>BufferMoveNext<CR>', opts)

-- go to buffer in position
for i = 1, 9, 1 do
 vim.keymap.set('n', string.format('<A-%s>', i), string.format('<Cmd>BufferGoto %s<CR>', i), opts) 
end
vim.keymap.set('n', '<A-0>', '<Cmd>BufferLast<CR>', opts)

-- pin/unpin buffer 
vim.keymap.set('n', '<A-p>', '<Cmd>BufferPin<CR>', opts)

-- close buffer 
vim.keymap.set('n', '<A-c>', '<Cmd>BufferClose<CR>', opts)

-- close cmds
vim.keymap.set('n', '<A-a>', '<Cmd>BufferCloseAllButCurrentOrPinned<CR>', opts)

-- sorting 
vim.keymap.set('n', '<A-b>', '<Cmd>BufferOrderByBufferNumber<CR>', opts)
vim.keymap.set('n', '<A-d>', '<Cmd>BufferOrderByDirectory<CR>', opts)
vim.keymap.set('n', '<A-l>', '<Cmd>BufferOrderByLanguage<CR>', opts)
vim.keymap.set('n', '<A-w>', '<Cmd>BufferOrderByWindowNumber<CR>', opts)
