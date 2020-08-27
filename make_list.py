import os
import json

path = './movies' # 動画が入っているディレクトリを指定。


output = {'wide':[],'vertical':[]} # wideのほうにwideデータのファイル名を、vertiのほうにvertiデータのファイル名を保存する。
all_tmp = os.listdir(path)
all = []
for name in all_tmp:
    if not name.startswith(','):
        all.append(name)
for name in all:
    # ファイル名の中にwideが含まれていたらwideに、vertiが含まれていたらvertiに振り分けるようにしている。
    if 'wide' in name:
        output['wide'].append(name)
    elif 'vertical' in name:
        output['vertical'].append(name)

# movie_list.jsonというファイルに保存する。
with open('movie_list.json', 'w') as f:
    json.dump(output, f, indent=4)

