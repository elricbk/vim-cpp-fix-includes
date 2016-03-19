# vim-cpp-fix-includes

## Requirements

`python` support in Vim is required as plugin is written in Python

## Installation

Use your plugin manager of choice.

- [Pathogen](https://github.com/tpope/vim-pathogen)
  - `git clone https://github.com/elricbk/vim-cpp-fix-includes ~/.vim/bundle/vim-cpp-fix-includes`
- [Vundle](https://github.com/gmarik/vundle)
  - Add `Bundle 'https://github.com/elricbk/vim-cpp-fix-includes'` to .vimrc
  - Run `:BundleInstall`
- [NeoBundle](https://github.com/Shougo/neobundle.vim)
  - Add `NeoBundle 'https://github.com/elricbk/vim-cpp-fix-includes'` to .vimrc
  - Run `:NeoBundleInstall`
- [vim-plug](https://github.com/junegunn/vim-plug)
  - Add `Plug 'https://github.com/elricbk/vim-cpp-fix-includes'` to .vimrc
  - Run `:PlugInstall`

## What it does

For now plugin does one VERY simple thing:

* Finds C++ identifier under cursor (i.e. `std::sort`)
* Finds mapping in the internal dictionary from this identifier to appropriate include (i.e. `algorithm`)
* Inserts the include directive right after all include directives at the beginning of file

If you want to make some use of it just add necessary mappings to the plugin file.

And some mapping for the plugin command, like `nnoremap <Leader>m :FixCppInclude<CR>`.

## TODO

* Support more user-friendly additional mappings
* Generate all the mappings for standard libraries (or at least more useful ones)
* Support for mapping search via tags file
* Add some tests as now tests from plugin generator are broken
