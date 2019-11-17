from bs4 import BeautifulSoup

lg = '''
  <script>
            window.X_Anti_Forge_Token = '59018a64-2982-4cd0-9788-3beb775a058a';
            window.X_Anti_Forge_Code = '86645652';
        </script>
'''

soup = BeautifulSoup(lg, "html.parser")

print(soup.script.string)
