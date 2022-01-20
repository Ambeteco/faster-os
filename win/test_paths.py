norm_paths = [
    'C:\\hello\\world',
    'C:\\\\hello\\\\\\world',
    'C:\\\\hello\\\\\\world\\\\\\',
    'C:\\\\hello\\\\\\world\\',
    'C:hello\\\\\\world\\',
    'C:\\..\\..\\..\\',
    'C:\\..\\..\\..\\Hello\\world\\',
    'C:\\..\\..\\..\\Hello\\world\\\\',
    'C:\\..\\..\\..\\Hello\\..\\..\\world\\\\',
    '..\\..\\..\\..\\Hello\\..\\..\\world\\\\',
    '..\\Hello\\..\\..\\world\\\\',
    '\\..\\Hello\\..\\..\\world\\\\',
    '\\..\\..\\..\\..\\Hello\\..\\..\\world\\\\',
]

rel_paths = [
    ('C:\\123\\456\\789', 'C:\\123'),
    ('C:\\123\\456\\789', 'C:\\123\\456'),
    ('C:\\123\\456\\789\\121221\\121222ss', 'C:\\123\\456'),
    ('C:\\123\\456\\789\\121221\\121222ss', 'C:\\123\\456\\sksksksksk'),
    ('C:\\123\\456\\789\\121221\\121222ss',
     'C:\\123\\456\\sksksksksk\\121212122'),
    ('C:\\123\\456\\789', 'C:\\123\\smth'),
    ('C:\\sjsjsjsj\\456\\789', 'C:\\123\\smth'),
    ('C:\\123\\456\\789\\121221\\121222ss',
     'C:\\123\\456\\sksksksksk\\121212122\\121212\\121221'),
    ('C:\\123\\456\\789\\121221\\121222ss',
     'C:\\123\\456\\sksksksksk\\121212122\\121212\\121221121212122\\121212\\121221'
     ),
    ('C:\\123\\456\\sksksksksk\\121212122\\121212\\121221121212122\\121212\\121221',
     'C:\\123\\456\\789\\121221\\121222ss'),
    ('C:\\123\\1212212', 'C:'),
]

valid_list_paths = [
    [
        'C:\\HELLO WORLD\\SOME PATH',
        'C:\\HELLO WORLD\\SOME PATH\\',
    ],
    [
        'C:\\HELLO WORLD\\SOME PATH',
        'C:\\HELLO WORLD\\SOME',
    ],
    [
        'C:\\HELLO WORLD\\SOME PATH',
        'C:\\HELLO \\SOME',
    ],
    [
        'C:\\HELLO WORLD\\SOME PATH',
        'C:\\HELLO WORLD\\SOrME',
    ],
    [
        'C:\\HELLO WORLD\\SOME PATH',
        'C:\\HELLO WORLD\\SOME PATH\\',
    ],
    [
        '\\\\HOST-NAME\\SHARE-NAME\\FILE_PATH',
        '\\\\HOST-NAME\\SHARE-NAME\\SOME\\LONG\\FILE\\PATH',
    ],
    [
        'C:\\',
        'C:\\1\\123/123/123\\123',
        'C:\\hello world\\some path',
        'C:\\hello world\\some path\\',
    ],
    [
        'C:\\123.ext',
        'C:\\123.ext\\',
        'C:\\123.ext\\123',
        'C:\\123.ext\\123.ext',
    ],
    [
        'hello world\\123.ext',
        'hello world\\123.ext\\',
        'hello world\\123.ext\\123',
    ],
    [
        'C:\\123.ext',
        'C:\\123.ext\\',
        'C:\\123.ext\\123',
        'C:\\123.ext\\123.ext',
    ],
]
list_paths = [
    [
        'C:\\HELLO WORLD\\SOME PATH',
        'C:\\HELLO WORLD\\SOME PATH\\',
    ],
    [
        'C:\\HELLO WORLD\\SOME PATH',
        'C:\\HELLO WORLD\\SOME',
    ],
    [
        'C:\\HELLO WORLD\\SOME PATH',
        'C:\\HELLO \\SOME',
    ],
    [
        'C:\\HELLO WORLD\\SOME PATH',
        'C:\\HELLO WORLD\\SOrME',
    ],
    [
        'C:\\123//123/123/1221\\33',
        '\\\\HOST-NAME\\SHARE-NAME\\FILE_PATH',
        '\\\\HOST-NAME\\SHARE-NAME\\SOME\\LONG\\FILE\\PATH',
    ],
    [
        'C:\\',
        'C:\\1\\123/123/123\\123',
        'C:\\hello world\\some path',
        'C:\\hello world\\some path\\',
    ],
    [
        'C:\\123.ext',
        'C:\\123.ext\\',
        'C:\\123.ext\\123',
        'C:\\123.ext\\123.ext',
        'hello world\\123.ext',
        'hello world\\123.ext\\',
        'hello world\\123.ext\\123',
    ],
    [
        'hello world\\123.ext',
        'hello world\\123.ext\\',
        'hello world\\123.ext\\123',
    ],
    [
        'C:\\123.ext',
        'C:\\123.ext\\',
        'C:\\123.ext\\123',
        'C:\\123.ext\\123.ext',
    ],
]

paths = [
    'C:\\HELLO WORLD\\SOME PATH',
    'C:\\HELLO WORLD\\SOME PATH\\',
    'C',
    '~\\user',
    '%USERPROFILE%\\hi',
    '~user',
    '~user\\123',
    '~\\',
    '~\\ddd',
    'C:',
    'C:\\123//123/123/1221\\33',
    '\\\\HOST-NAME\\SHARE-NAME\\FILE_PATH',
    '\\\\HOST-NAME\\SHARE-NAME\\SOME\\LONG\\FILE\\PATH',
    'C:1',
    '\\\\MACHINE\\MOUNTPOINT\\DIRECTORY\\ETC\\',
    '',
    'C:\\',
    'C:\\1\\123/123/123\\123',
    'C:\\hello world\\some path',
    'C:\\hello world\\some path\\',
    'C',
    'C:',
    '\\\\host-name\\share-name\\file_path',
    '\\\\host-name\\share-name\\some\\long\\file\\path',
    'C:1',
    '\\\\machine\\mountpoint\\directory\\etc\\',
    '',
    'C:\\',
    'C:\\1\\123/123/123\\123',
    'C:\\hello world\\some path',
    'C:\\hello world\\some path\\',
    'C',
    'C:',
    'C:1',
    '',
    '\\\\machine\\mountpoint\\directory\\etc\\',
    'C:\\',
    'C:\\1\\123/123/123\\123',
    'C:\\123.ext',
    'C:\\123.ext\\',
    'C:\\123.ext\\123',
    'C:\\123.ext\\123.ext',
    'hello world\\123.ext',
    'hello world\\123.ext\\',
    'hello world\\123.ext\\123',
]

join_paths = [
    ('C:\\HELLO WORLD\\SOME PATH', '12121331'),
    ('C:\\HELLO WORLD\\SOME PATH\\', '12kdnwdnkjwd\\121212'),
    ('C', '1231313/121212\\1212'),
    ('C:', '123', '1341378317/j\\djd', '12sss//'),
    ('C:', '123', '1341378317djd', '12sss//'),
    ('C:', '123', '1341378317djd', '12sss'),
    ('\\\\machine\\mountpoint\\directory\\etc\\', '12121331'),
    ('\\\\machine\\mountpoint\\directory\\etc\\', '12kdnwdnkjwd\\121212'),
    ('\\\\machine\\mountpoint\\directory\\etc\\', '1231313/121212\\1212'),
    ('\\\\machine\\mountpoint\\directory\\etc\\', '123', "sqsqss", '12sss//'),
]