set nocompatible
filetype off
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'
Plugin 'tmhedberg/SimpylFold'
Plugin 'Valloric/YouCompleteMe'
Plugin 'vim-scripts/indentpython.vim'
Plugin 'francoiscabrol/ranger.vim'
Plugin 'junegunn/goyo.vim'
Plugin 'LukeSmithxyz/vimling'
Plugin 'vimwiki/vimwiki'
call vundle#end()

filetype plugin indent on

" Basics
set foldmethod=indent
set foldlevel=99
nnoremap <space> za

let mapleader =" "
set encoding=utf-8
set number relativenumber
syntax on

" Autocomplete
    set wildmode=longest,list,full
" Disables autocomment on newline
    autocmd FileType * setlocal formatoptions-=c formatoptions-=r formatoptions-=o
" Readable goyo for prose
    map <leader>g :Goyo \| set linebreak<CR>
" Spell-check
    map <leader>o :setlocal spell! spelllang=en_us<CR>
" Split open at bottom right
    set splitbelow splitright
" Split navigation
    map <C-h> <C-w>h
    map <C-j> <C-w>j
    map <C-k> <C-w>k
    map <C-l> <C-w>l
" Check file in shellcheck
    map <leader>s :!clear && shellcheck %<CR>
" Replace all alias
    nnoremap S :%s//g<Left><Left>
" Open Bibliography in split
    map <leader>b :vsp<space>$BIB<CR>
" Compile document
    map <leader>c :!pdflatex %<CR><CR>
"   map <leader>c :w! \| !compiler <c-r>%<CR><CR>
" Open pdf,html, or preview
    map <leader>v :!mupdf $(echo % \| sed 's/tex$/pdf/') & disown<CR><CR>
"   map <leader>v :!opout <c-r>%<CR><CR>
" Autoclear tex build files
    autocmd VimLeave *.tex !texclear %
" Ensure proper files are read
    let g:vimwiki_ext2syntax = {'.Rmd': 'markdown', '.rmd': 'markdown', '.md': 'markdown', '.markdown': 'markdown', '.mdown': 'markdown'}
    autocmd BufRead,BufNewFile /tmp/calcurse*,~/.calcurse/notes/* set filetype=markdown
    autocmd BufRead,BufNewFile *.ms,*.me,*.mom,*.man set filetype=groff
    autocmd BufRead,BufNewFile *.tex set filetype=tex
" Open url
    :noremap <leader>u :w<Home>silent <End> !urlscan<CR>
    :noremap ,, :w<Home>silent <End> !urlscan<CR>
" Copy selected text to system clipboard
    vnoremap <C-c> "*Y :let @+=@*<CR>
    map <C-p> "+P
" Autodelete all trailing whitespace on save
    autocmd BufWritePre * %s/\s\+$//e
" Renew sh and ranger configs with new material
    autocmd BufWritePost ~/.bm* !shortcuts
" Navigate with guides
    inoremap <Space><Tab> <Esc>/<++><Enter>"_c4l
    vnoremap <Space><Tab> <Esc>/<++><Enter>"_c4l
    map <Space><Tab> <Esc>/<++><Enter>"_c4l

" PEP-8 indentation
au BufNewFile,BufRead *.py
    set tabstop=4
    set softtabstop=4
    set shiftwidth=4
    set textwidth=79
    set expandtab
    set autoindent
    set fileformat=unix

" Mark Unnecessary whitespace in python and C files
au BufRead,BufNewFile *.py,*.pyw,*.c,*.h match BadWhitespace /\s\+$/

set tabstop=4
set autoindent
set expandtab
set softtabstop=4

