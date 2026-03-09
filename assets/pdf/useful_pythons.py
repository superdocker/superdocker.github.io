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

# UV guide
# pip install uv
uv venv gpt-oss --python 3.11 && source gpt-oss/bin/activate && uv pip install --upgrade pip
# Later
# source ~/gpt-oss/bin/activate
# source ~/jhlee/gpt-oss/bin/activate
uv pip install torch==2.8.0 torchvision torchaudio --index-url https://download.pytorch.org/whl/test/cu128
uv pip install git+https://github.com/triton-lang/triton.git@main#subdirectory=python/triton_kernels

# Dockerfile
FROM nvcr.io/nvidia/cuda:11.8.0-devel-ubuntu22.04
# apt packages
RUN apt-get update
RUN apt-get install git pip vim tmux htop libxml2 kmod systemctl lsof python3.10 -y
RUN pip install --upgrade pip
RUN ln -s /usr/bin/python3 /usr/bin/python
# tmux.conf           
RUN echo "unbind C-b"  >> ~/.tmux.conf
RUN echo "set-option -g prefix C-a" >> ~/.tmux.conf
RUN echo "bind-key C-a send-prefix" >> ~/.tmux.conf
# vimrc               
RUN echo "abbr set_pdb import pdb; pdb.set_trace()" >> ~/.vimrc
RUN echo "abbr cmt #============================ <Esc>i" >> ~/.vimrc
RUN echo "syntax enable" >> ~/.vimrc
RUN echo "set background=light" >> ~/.vimrc
RUN echo "set nocompatible" >> ~/.vimrc
RUN echo "set hlsearch" >> ~/.vimrc
RUN echo "highlight LineNr ctermfg=8" >> ~/.vimrc
RUN echo "set ignorecase" >> ~/.vimrc
RUN echo "imap <S-Tab> <Space><Space><Space><Space>" >> ~/.vimrc
RUN echo "map 3 :norm<Space>i#<CR>" >> ~/.vimrc
RUN echo "map , :norm<Space>1x<CR>" >> ~/.vimrc
RUN echo "map > :norm<Space>i<Space><Space><Space><Space><CR>" >> ~/.vimrc
RUN echo "map < :norm<Space>4x<CR>" >> ~/.vimrc
RUN echo "map f <C-w>v" >> ~/.vimrc
RUN echo "map <S-f> f<C-w>L:e<Space>%:p:h<CR>" >> ~/.vimrc
RUN echo "nnoremap <leader>s :%s/\<<C-r><C-w>\>/" >> ~/.vimrc
WORKDIR /root
# Python library
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
RUN pip install transformers accelerate sentencepiece tokenizers texttable toml attributedict protobuf cchardet
RUN pip install matplotlib scikit-learn pandas
RUN git clone https://github.com/EleutherAI/lm-evaluation-harness
RUN cd lm-evaluation-harness && pip install -e .
# Flush
RUN rm -rf /root/.cache/pip
