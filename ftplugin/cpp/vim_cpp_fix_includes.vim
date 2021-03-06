" --------------------------------
" Add our plugin to the path
" --------------------------------
python import sys
python import vim
python sys.path.append(vim.eval('expand("<sfile>:h")'))

" --------------------------------
"  Function(s)
" --------------------------------
function! FixCppInclude()
python << endOfPython

import vim_cpp_fix_includes

def notify(s): print(s)

vim_cpp_fix_includes.initialize(vim)
vim_cpp_fix_includes.fix_include_for_word_under_cursor(notify)

endOfPython
endfunction

" --------------------------------
"  Expose our commands to the user
" --------------------------------
command! FixCppInclude call FixCppInclude()
