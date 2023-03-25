
import b64

content='dadefefefaefweerhthyt中国'

en_content=content.encode()
en_content=base64.b64encode(en_content).decode()
print(en_content)