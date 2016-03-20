# vim-cpp-fix-includes

## What it does

For now plugin does VERY simple thing:

* Finds C++ identifier under cursor (i.e. `std::sort`)
* Finds mapping in the internal dictionary from this identifier to appropriate include (i.e. `algorithm`)
* Inserts the include directive right after all include directives at the beginning of file

If you want to make some use of it just add necessary mappings via `g:fix_includes_additional_mappings` variable:

    let g:fix_includes_additional_mappings = "
      \REQUIRE \t path/to/exception.hpp \n
      \ASSERT  \t path/to/exception.hpp \n
      \DEBUG   \t path/to/logging.hpp   \n
      \WARN    \t path/to/logging.hpp   \n
      \ERROR   \t path/to/logging.hpp   \n
    \"

Plugin expects multiline string where each line corresponds to single tab-separated mapping. Spaces inside each mapping are ignored.

Also you may want to add some key mapping for the plugin command, like `nnoremap <Leader>m :FixCppInclude<CR>`.

## Requirements

`python` support in Vim is required as plugin is written in Python

## Installation

Use your plugin manager of choice.

- [Pathogen](https://github.com/tpope/vim-pathogen)
  - `git clone https://github.com/elricbk/vim-cpp-fix-includes ~/.vim/bundle/vim-cpp-fix-includes`
- [Vundle](https://github.com/gmarik/vundle)
  - Add `Bundle 'elricbk/vim-cpp-fix-includes'` to .vimrc
  - Run `:BundleInstall`
- [NeoBundle](https://github.com/Shougo/neobundle.vim)
  - Add `NeoBundle 'elricbk/vim-cpp-fix-includes'` to .vimrc
  - Run `:NeoBundleInstall`
- [vim-plug](https://github.com/junegunn/vim-plug)
  - Add `Plug 'elricbk/vim-cpp-fix-includes'` to .vimrc
  - Run `:PlugInstall`

## TODO

* Generate all the mappings for standard libraries (or at least more useful ones)
* Support for mapping search via tags file
* Add some tests as now tests from plugin generator are broken
