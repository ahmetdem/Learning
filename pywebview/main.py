import webview

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

    webview.create_window('TEST!', html=content)
    webview.start()