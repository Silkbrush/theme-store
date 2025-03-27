import os
import sys
import json
import uuid
import time

with open('/home/runner/issue-parser-result.json', 'r') as file:
    data = json.load(file)

if not data['repo'].startswith('https://github.com/'):
    sys.exit(1)

if not data['name']:
    data['name'] = 'Untited Theme'

if not data['description']:
    data['description'] = 'No description provided.'

if not data['version']:
    data['version'] = '1.0.0'

if not data['author']:
    data['author'] = sys.argv[1]

if data['copy_file']:
    data['copy_file'] = data['copy_file'].split('\n')

if data['copy_folder']:
    data['copy_folder'] = data['copy_folder'].split('\n')

if data['load_chrome']:
    data['load_chrome'] = data['load_chrome'].split('\n')

if data['load_content']:
    data['load_content'] = data['load_content'].split('\n')

if data['domains']:
    data['domains'] = data['domains'].split('\n')

theme_type = 0
data['submission_type'] = 'Bundle'

if data['load_chrome'] and not data['load_content']:
    theme_type = 1
    data['submission_type'] = 'Theme'

if data['load_content'] and not data['load_chrome']:
    theme_type = 2
    data['submission_type'] = 'Page'

if not data['copy_file'] and not data['copy_folder']:
    print('ERROR: No files to copy.')
    print('Please provide a file or folder to copy.')
    sys.exit(1)

if not data['load_chrome'] and not data['load_content']:
    print('ERROR: No load points.')
    print('Please provide a load point for either userChrome or userContent.')
    sys.exit(1)

if theme_type == 0 and not (data['load_chrome'] and data['load_content']):
    print('ERROR: Theme type mismatch.')
    print('Your theme is a Bundle, but you did not provide load points for both userChrome and userContent.')
    print('Please provide load points for both or use a different type (Theme/Page).')
    sys.exit(1)

gh_username = data['repo'].replace('https://github.com/', '', 1).split('/')[0]
if not gh_username == sys.argv[1]:
    print('ERROR: Repository owner mismatch.')
    print('You don\'t own this repository.')
    sys.exit(1)

os.system(f'git clone {data["repo"]} theme-repo')
theme_id = str(uuid.uuid4())
theme_dir = f'themes/{theme_id}'
os.makedirs(theme_dir)

if data['readme']:
    with open(f'{theme_dir}/README.md', 'w+') as file:
        file.write(data['readme'])

for file in data['copy_file']:
    os.system(f'cp theme-repo/{file} {theme_dir}')

for folder in data['copy_folder']:
    os.system(f'cp -r theme-repo/{folder} {theme_dir}')

os.system(f'rm -rf theme-repo')

if data['load_chrome']:
    for load_point in data['load_chrome']:
        if not os.path.isfile(theme_dir + '/' + load_point):
            print(f'ERROR: Invalid userChrome load point {load_point}.')
            print('Please provide a valid file path.')
            sys.exit(1)

if data['load_content']:
    for load_point in data['load_content']:
        if not os.path.isfile(theme_dir + '/' + load_point):
            print(f'ERROR: Invalid userContent load point {load_point}.')
            print('Please provide a valid file path.')
            sys.exit(1)

theme_data = {
    "type": theme_type,
    "name": data['name'],
    "description": data['description'],
    "author": data['author'],
    "authorUrl": f"https://github.com/{sys.argv[1]}",
    "homepage": data['repo'],
    "version": data['version'],
    "createdAt": round(time.time()),
    "updatedAt": round(time.time()),
    "tags": [],
    "domains": data['domains']
}

theme_install_data = {
    "files": data['copy_file'],
    "folders": data['copy_folder'],
    "uclChromeTarget": data['load_chrome'],
    "uclContentTarget": data['load_content']
}

with open('themes.json', 'r') as file:
    themes = json.load(file)

with open(f'{theme_dir}/theme.json', 'w+') as file:
    # noinspection PyTypeChecker
    json.dump(theme_install_data, file, indent=4)

for theme in themes:
    if themes[theme]['homepage'] == theme_data['homepage']:
        print('ERROR: Theme already exists.')
        print('A theme with the same repository already exists.')
        sys.exit(1)

themes.update({theme_id: theme_data})

with open('themes.json', 'w+') as file:
    # noinspection PyTypeChecker
    json.dump(themes, file, indent=4)

print('SUCCESS: Files have been written to folder.')
