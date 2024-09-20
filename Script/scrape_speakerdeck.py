import requests
from bs4 import BeautifulSoup

speakerdeck_account_id = 'akidon0000'

# WebページのURLを指定
url = 'https://speakerdeck.com/' + speakerdeck_account_id
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
links = soup.find_all('a', class_='deck-preview-link')


# ReadMeファイルのプレースホルダーを探して置換
readme_file = 'README.md'
placeholder = '<!--START_SECTION:speakerdeck-->'

# READMEファイルの内容を読み込む
with open(readme_file, 'r') as file:
    content = file.read()

# プレースホルダーの前に追加する新しいリンクのリストを作成
new_lines = ""
for link in links:
    href = link['href']  # リンクのURL
    title = link['title']  # タイトル
    new_link = f"[{title}]({href})\n"

    # すでにREADMEに同じリンクが存在するか確認
    if href not in content:
        new_lines += new_link  # 存在しない場合のみ追加

# 新しいリンクがある場合、プレースホルダーの前に追加
if new_lines and placeholder in content:
    # プレースホルダーの直前にリンクを追加する
    content = content.replace(placeholder, placeholder + "\n" + new_lines)

    # 上書き保存
    with open(readme_file, 'w') as file:
        file.write(content)
    print("新しいリンクが追加されました。")
else:
    print("新しいリンクはありませんでした、またはプレースホルダーが見つかりませんでした。")
