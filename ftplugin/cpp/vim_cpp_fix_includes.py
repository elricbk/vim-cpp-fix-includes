vim = None

INCLUDE_MARKER = '#include'

_HEADER_TO_IDENTIFIER = {
'algorithm': [
    'all_of', 'any_of', 'none_of', 'find_if_not', 'copy_if', 'is_sorted',
    'is_heap', 'adjacent_find', 'binary_search', 'copy', 'copy_backward',
    'count', 'count_if', 'equal', 'equal_range', 'fill', 'find', 'find_end',
     'find_first_of', 'find_if', 'for_each', 'generate', 'generate_n',
    'includes', 'inplace_merge', 'is_heap', 'is_sorted', 'iter_swap',
    'lexicographical_compare', 'lexicographical_compare_3way', 'lower_bound',
    'make_heap', 'max', 'max_element', 'merge', 'min', 'min_element',
    'mismatch', 'next_permutation', 'nth_element', 'partial_sort',
    'partial_sort_copy', 'partition', 'pop_heap', 'prev_permutation',
    'push_heap', 'random_sample', 'random_sample_n', 'random_shuffle', 'remove',
    'remove_copy', 'remove_copy_if', 'remove_if', 'replace', 'replace_copy',
    'replace_copy_if', 'replace_if', 'reverse', 'reverse_copy', 'rotate',
    'rotate_copy', 'search', 'search_n', 'set_difference', 'set_intersection',
    'set_symmetric_difference', 'set_union', 'sort', 'sort_heap',
    'stable_partition', 'stable_sort', 'swap', 'swap_ranges', 'transform',
    'unique', 'unique_copy', 'upper_bound'
],
'bitset': [ 'bitset' ],
'cmath': [ 'fmod' ],
'cstdio': [
    'fflush', 'freopen', 'setbuf', 'setvbuf', 'fprintf', 'fscanf', 'printf',
    'scanf', 'sprintf', 'sscanf', 'vfprintf', 'vprintf', 'vsprintf', 'fgetc',
    'fgets', 'fputc', 'fputs', 'getc', 'getchar', 'gets', 'putc', 'putchar',
    'puts', 'ungetc', 'fread', 'fwrite', 'fseek', 'ftell', 'rewind', 'feof',
    'perror', 'EOF', 'FILE', 'fpos_t'
],
'cstdlib': [
    'atof', 'atoi', 'atol', 'strtod', 'strtol', 'strtoul', 'rand', 'srand',
    'abort', 'exit', 'qsort', 'abs', 'atexit', 'calloc', 'bsearch', 'div',
    'free', 'malloc', 'getenv', 'labs', 'ldiv', 'system'
],
'cstring': [
    'memcpy', 'memmove', 'strcpy', 'strncpy', 'strcat', 'strncat', 'memcmp',
    'strcmp', 'strcoll', 'strncmp', 'strxfrm', 'memchr', 'strchr', 'strcspn',
    'strpbrk', 'strrchr', 'strspn', 'strstr', 'strtok', 'memset', 'strerror',
    'strlen'
],
'cstdint': [
    'int8_t', 'int16_t', 'int32_t', 'int64_t', 'uint8_t', 'uint16_t',
    'uint32_t', 'uint64_t'
],
'deque': [ 'deque' ],
'exception': [
    'exception', 'bad_exception', 'unexpected', 'uncaught_exception',
    'terminate', 'set_unexpected', 'set_terminate', 'terminate_handler',
    'unexpected_handler'
],
'fstream': [ 'ifstream', 'ofstream', 'fstream' ],
'functional': [
    'plus', 'minus', 'multiplies', 'hash', 'divides', 'modulus', 'negate',
    'equal_to', 'not_equal_to', 'less', 'greater', 'less_equal',
    'greater_equal', 'logical_and', 'logical_or', 'logical_not', 'binder1st',
    'bind1st', 'binder2nd', 'bind2nd', 'ptr_fun', 'pointer_to_unary_function',
    'pointer_to_binary_function', 'not1', 'unary_negate', 'binary_negate', 'not2',
    'mem_fun', 'mem_fun_ref', 'mem_fun1', 'mem_fun1_ref'
],
'iomanip': [ 'setw', 'setfill', 'hex', 'setprecision' ],
'iostream': [ 'cin', 'cerr', 'cout', 'istream', 'ostream', 'endl', 'flush' ],
'iterator': [
    'advance', 'distance', 'ostream_iterator', 'istream_iterator',
    'front_insert_iterator', 'back_insert_iterator', 'front_inserter',
    'back_inserter', 'insert_iterator', 'inserter', 'reverse_iterator',
    'reverse_bidirectional_iterator'
],
'list': [ 'list' ],
'map': [ 'map', 'multimap' ],
'memory': [ 'unique_ptr', 'shared_ptr', 'weak_ptr', 'auto_ptr', 'make_shared' ],
'numeric': [
    'accumulate', 'adjacent_difference', 'inner_product', 'partial_sum', 'power'
],
'queue': [ 'queue', 'priority_queue' ],
'set': [ 'set', 'multiset' ],
'sstream': [ 'istringstream', 'ostringstream', 'stringstream' ],
'stack': [ 'stack' ],
'stdexcept': [
    'domain_error', 'invaid_argument', 'length_error', 'out_of_range',
    'overflow_error', 'range_error', 'underflow_error', 'runtime_error'
],
'string': [ 'string', 'basic_string', 'char_traits', 'getline' ],
'tuple': [ 'make_tuple', 'tie', 'tuple', 'get' ],
'utility': [ 'pair', 'make_pair', 'move', 'forward' ],
'vector': [ 'vector', 'bit_vector' ],
'unordered_map': [ 'unordered_map' ],
'unordered_set': [ 'unordered_set' ],
}

_NAME_TO_INCLUDE = {
    'boost::optional': 'boost/optional/optional.hpp',
    'boost::none': 'boost/none.hpp',
    'boost::lexical_cast': 'boost/lexical_cast.hpp',
    'BOOST_AUTO_TEST_SUITE': 'boost/test/unit_test.hpp',
    'BOOST_AUTO_TEST_CASE': 'boost/test/unit_test.hpp',
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

def fix_include_for_word_under_cursor(notify):
    for header, identifier_list in _HEADER_TO_IDENTIFIER.iteritems():
        for i in identifier_list:
            _NAME_TO_INCLUDE[i] = header
            _NAME_TO_INCLUDE['std::' + i] = header
    _NAME_TO_INCLUDE.update(_load_additional_mappings())

    b = vim.current.buffer
    (row, col) = vim.current.window.cursor
    word = extract_cpp_identifier(b[row - 1], col)

    if word is None:
        notify("Can't find identifier under cursor")
        return

    if word in _NAME_TO_INCLUDE:
        start, end = find_include_range(b)
        insert_point = end if end is not None else 0
        line = '#include <{}>'.format(_NAME_TO_INCLUDE[word])
        vim.command('call append(%d, "%s") | redraw' % (insert_point, line))
        notify("<{}> included".format(_NAME_TO_INCLUDE[word]))
    else:
        notify("No mapping for '{}'".format(word))
