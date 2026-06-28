from pyngrok import conf, ngrok
import time

conf.get_default().auth_token = '3Fl4wlFTgMWouctyXGFWhRlHv67_2qRLNTcGL6oEzeaZBrREu'
url = ngrok.connect(8000)
print(f"Ngrok URL: {url}")
print("Ngrok is running press ctrl to close")
time.sleep(99999)