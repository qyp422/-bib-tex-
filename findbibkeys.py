import re

def get_bib_keys(bib_file):
    with open(bib_file, 'r', encoding='utf-8') as f:
        bib_content = f.read()

    pattern = re.compile(r'@.*?\{(.*?),', re.DOTALL)
    bib_keys = re.findall(pattern, bib_content)
    
    return set(bib_keys)

def get_tex_citations(tex_file):
    with open(tex_file, 'r', encoding='utf-8') as f:
        tex_content = f.read()

    pattern = re.compile(r'\\cite\{(.*?)\}')
    tex_citations = re.findall(pattern, tex_content)
    
    tex_keys = set()
    for citation in tex_citations:
        keys = citation.split(',')
        tex_keys.update(keys)
    
    return tex_keys

def find_unreferenced_keys(bib_keys, tex_keys):
    unreferenced_keys = bib_keys - tex_keys
    return unreferenced_keys

# 指定.bib文件和.tex文件的路径
bib_file_path = 'refback.bib'
tex_file_paths = [f'chapter{i}.tex' for i in range(1,6)]


# 获取.bib文件中的引用文献键
bib_keys = get_bib_keys(bib_file_path)

# 获取.tex文件中的引用文献键（使用集合）
tex_keys = set()
for tex_file_path in tex_file_paths:
    tex_keys.update(get_tex_citations(tex_file_path))

# 查找未引用的文献键
unreferenced_keys = find_unreferenced_keys(bib_keys, tex_keys)

# 打印未引用的文献键
print("未引用的文献键:")
for key in unreferenced_keys:
    print(key)
