import os
import re
import shutil
from datetime import date
import time
import json


class SortFiles:
    def __init__(self, base_dir):
        self.number_of_files_moved = 0
        self.base_dir = base_dir
        self.patterns, self.default_dir, self.end_dirs = self.get_config()
        new_list = []
        for x in self.end_dirs:
            new_list.append(0)

        self.to_move_file = dict(zip(self.end_dirs, new_list))

    def move_file(self, pattern, filename, end_dir):
        base_dir = self.base_dir
        print(f'file for {end_dir} detected....')
        print(f'moving file to {end_dir}...')
        final_destination = ''


        if pattern == 'tt.pdf':
            final_destination = os.path.join(base_dir, end_dir, date.today().strftime('%d-%m-%Y') + f'_{filename}')
            print(final_destination)
            shutil.move(base_dir + f'/{filename}',
                        final_destination)


        elif pattern == '2021-23.pdf':
            final_destination = os.path.join(base_dir, end_dir, date.today().strftime('%d-%m-%Y') + f'_{filename}')
            shutil.move(base_dir + f'/{filename}', final_destination)

        elif pattern == '.deb':
            final_destination = os.path.join(base_dir, end_dir, f'{filename}')
            shutil.move(base_dir + f'/{filename}', final_destination)


        elif pattern == '.AppImage' or pattern == '.appimage':
            final_destination = os.path.join(base_dir, end_dir, f'{filename}')
            shutil.move(base_dir + f'/{filename}', final_destination)

        end_dir = end_dir.replace('/', '')
        self.to_move_file[end_dir] += 1

        print(final_destination)
        print(f'file moved to {end_dir} !')

    def get_pattern_matches(self, directories):
        for src_path in directories:
            index = 0
            for pattern in self.patterns:
                start_str, end_str = pattern
                if start_str is not None:
                    matches = re.search(f'^{start_str}.*{end_str}$', src_path)
                    if matches:
                        end_dir = self.end_dirs[index] + '/'
                        self.move_file(end_str, src_path, end_dir)
                        self.number_of_files_moved += 1
                else:
                    matches = re.search(f' *{end_str}$', src_path)
                    if matches:
                        end_dir = self.end_dirs[index] + '/'
                        self.move_file(end_str, src_path, end_dir)
                        self.number_of_files_moved += 1
                index += 1

    def get_config(self):
        config_file = open('config.json', 'r')
        config_json = json.load(config_file)
        return config_json['patterns'], config_json['default_dir'], config_json['end_dirs']


start_time = time.time()
parent_dir = os.path.dirname(os.getcwd())
base_dir = os.path.join(parent_dir, 'Downloads')

files_sorter = SortFiles(base_dir)
directories = os.listdir(base_dir)
files_sorter.get_pattern_matches(directories=directories)

print(f'\n\nnumber of files moved: {files_sorter.number_of_files_moved}\n')
time_taken = time.time() - start_time

for dirs in files_sorter.to_move_file.keys():
    dirs = dirs.replace('/', '')
    n = files_sorter.to_move_file[dirs]
    print(f'files moved in {dirs}: {n}')

print(f'\nfinished in {time_taken} seconds')
