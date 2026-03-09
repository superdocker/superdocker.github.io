# vimrc

syntax enable
set background=light
set nocompatible
set hlsearch
highlight LineNr ctermfg=8
set ignorecase
imap <S-Tab> <Space><Space><Space><Space>
map 3 :norm<Space>i#<CR>
map , :norm<Space>1x<CR>
map > :norm<Space>i<Space><Space><Space><Space><CR>
map < :norm<Space>4x<CR>
map f <C-w>v
map <S-f> f<C-w>L:e<Space>%:p:h<CR>
nnoremap <leader>s :%s/\<<C-r><C-w>\>/

" Abbreviate
abbr cmt #============================ <Esc>i
abbr ifmain if __name__ == "__main__":<Esc>o
abbr set_args import argparse, textwrap<Enter>parser = argparse.ArgumentParser(description='')<Enter>parser.add_argument('',type=,default=,<Enter><S-Tab><S-Tab><S-Tab>help=textwrap.dedent('''\<Enter><S-Tab><S-Tab><S-Tab><Enter><S-Tab><S-Tab><S-Tab>'''))<Enter>args=parser.parse_args()
abbr set_error raise NotImplementedError
abbr set_pdb import pdb; pdb.set_trace()
iabbr <expr> __time strftime("%Y-%m-%d %H:%M:%S")
iabbr <expr> __file expand('%:p')
iabbr <expr> __name expand('%')
iabbr <expr> __pwd expand('%:p:h')

# .tmux.conf
unbind C-b
set-option -g prefix C-a
bind-key C-a send-prefix

# download hf
import argparse

from huggingface_hub import snapshot_download

parser = argparse.ArgumentParser()
parser.add_argument('--folder_path', type=str)
parser.add_argument('--repo_id', type=str)
parser.add_argument('--read_token', type=str)
"doesn't save to huggingface cache, only downloads in specified local directory"
if __name__ == "__main__":
    args = parser.parse_args()
    snapshot_download(repo_id=args.repo_id,
                      repo_type="model",
                      local_dir=args.folder_path,
                      local_dir_use_symlinks=False,
                      ignore_patterns=["*.msgpack", "*.h5"],
                      token=args.read_token)
