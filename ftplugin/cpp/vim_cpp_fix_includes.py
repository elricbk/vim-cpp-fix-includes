vim = None

INCLUDE_MARKER = '#include'

_NAME_TO_INCLUDE = {
    'std::string': 'string',
    'std::vector': 'vector',
    'std::map': 'map',
    'std::set': 'set',
    'std::make_pair': 'utility',
    'std::shared_ptr': 'memory',
    'std::make_shared': 'memory',
    'std::unique_ptr': 'memory',
    'size_t': 'ctddef',
    'uint8_t': 'cstdint',
    'uint16_t': 'cstdint',
    'uint32_t': 'cstdint',
    'uint64_t': 'cstdint',
    'int8_t': 'cstdint',
    'int16_t': 'cstdint',
    'int32_t': 'cstdint',
    'int64_t': 'cstdint',
    'std::sort': 'algorithm',
    'std::cout': 'iostream',
    'std::endl': 'iostream',

    'boost::optional': 'boost/optional/optional.hpp',
    'boost::none': 'boost/none.hpp',
    'boost::lexical_cast': 'boost/lexical_cast.hpp',
}

def _get_visual_selection():
    b = vim.current.buffer
    (lnum1, col1) = b.mark('<')
    (lnum2, col2) = b.mark('>')
    if lnum1 != lnum2:
        return None
    return b[lnum1 - 1][col1:col2 + 1]

def extract_cpp_identifier(l, col):
    is_name_part = lambda c: c == ':' or c == '_' or c.isalnum()
    if col < 0 or col > len(l) - 1 or not is_name_part(l[col]):
        return None
    i = col - 1
    while i >= 0 and is_name_part(l[i]):
        i -= 1
    j = col + 1
    while j < len(l) and is_name_part(l[j]):
        j += 1
    return l[i + 1:j]

def find_include_range(buf):
    start = None
    end = None
    is_empty = lambda s: len(s.strip()) == 0
    is_include = lambda s: s.strip().startswith(INCLUDE_MARKER)
    for i, l in enumerate(buf):
        if is_empty(l): continue
        if start is None and is_include(l):
            start = i
        if not is_include(l) and start is not None:
            end = i
            break
    if start is not None and end is None:
        end = i + 1
    while end > start and len(buf[end - 1].strip()) == 0:
        end -= 1
    return (start, end)


# These are just functions to test buffer creation (if suggesting from tags
# will be implemented)

def _create_new_buffer(file_name, file_type, contents):
    vim.command('rightbelow split {0}'.format(file_name))
    vim.command('setlocal modifiable')
    vim.command('normal! ggdG')
    vim.command('setlocal filetype={0}'.format(file_type))
    vim.command('setlocal buftype=nowrite')
    vim.command('resize 10')
    vim.command('setlocal colorcolumn=')
    vim.command('setlocal cursorline')

    vim.current.buffer[:] = contents

    vim.command('setlocal nomodifiable')

def _make_example_python_buffer():
    contents = [
        "boost::geometry::Point    #include <boost/geometry/point.hpp>",
        "QPoint #include <QtCore/QPoint>"
    ]
    _create_new_buffer("Example_buffer", "cpp", contents)

def _load_additional_mappings():
    ADDITIONAL_MAPPINGS_KEY = "g:fix_includes_additional_mappings"
    eval_value = int(vim.eval('exists("%s")' % ADDITIONAL_MAPPINGS_KEY))
    if not eval_value: return {}
    actual_value = vim.eval(ADDITIONAL_MAPPINGS_KEY)
    mapping_list = [l.strip().split('\t') for l in actual_value.split('\n')]
    return dict(map(str.strip, t) for t in mapping_list if len(t) == 2)

def initialize(vim_ext):
    global vim
    vim = vim_ext

def fix_include_for_word_under_cursor():
    _NAME_TO_INCLUDE.update(_load_additional_mappings())

    b = vim.current.buffer
    (row, col) = vim.current.window.cursor
    word = extract_cpp_identifier(b[row - 1], col)

    if word is None:
        print "Can't find identifier under cursor"
        return

    if word in _NAME_TO_INCLUDE:
        start, end = find_include_range(b)
        insert_point = end if end is not None else 0
        line = '#include <{}>'.format(_NAME_TO_INCLUDE[word])
        vim.command('call append(%d, "%s") | redraw' % (insert_point, line))
        print "<{}> included".format(_NAME_TO_INCLUDE[word])
    else:
        print "No mapping for '{}'".format(word)
