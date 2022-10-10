from flask import Flask, Response
import cv2
import socket

h_name = socket.gethostname()
IP_address = socket.gethostbyname(h_name)
webcontent = open('index.html').read()
css = open('main.css').read()
	
print(r"""

  ______             __        __  _______                           __            __  __         ______    ______    ______   __                               
 /      \           |  \      |  \|       \                         |  \          |  \|  \       /      \  /      \  /      \ |  \                              
|  $$$$$$\  ______  | $$  ____| $$| $$$$$$$\  ______   ______ ____   \$$ _______   \$$| $$   __ |  $$$$$$\|  $$$$$$\|  $$$$$$\| $$_______                       
| $$ __\$$ /      \ | $$ /      $$| $$  | $$ /      \ |      \    \ |  \|       \ |  \| $$  /  \| $$__/ $$| $$__/ $$ \$$__| $$ \$/       \                      
| $$|    \|  $$$$$$\| $$|  $$$$$$$| $$  | $$|  $$$$$$\| $$$$$$\$$$$\| $$| $$$$$$$\| $$| $$_/  $$ >$$    $$ \$$    $$  |     $$  |  $$$$$$$                      
| $$ \$$$$| $$  | $$| $$| $$  | $$| $$  | $$| $$  | $$| $$ | $$ | $$| $$| $$  | $$| $$| $$   $$ |  $$$$$$  _\$$$$$$$ __\$$$$$\   \$$    \                       
| $$__| $$| $$__/ $$| $$| $$__| $$| $$__/ $$| $$__/ $$| $$ | $$ | $$| $$| $$  | $$| $$| $$$$$$\ | $$__/ $$|  \__/ $$|  \__| $$   _\$$$$$$\                      
 \$$    $$ \$$    $$| $$ \$$    $$| $$    $$ \$$    $$| $$ | $$ | $$| $$| $$  | $$| $$| $$  \$$\ \$$    $$ \$$    $$ \$$    $$  |       $$                      
  \$$$$$$   \$$$$$$  \$$  \$$$$$$$ \$$$$$$$   \$$$$$$  \$$  \$$  \$$ \$$ \$$   \$$ \$$ \$$   \$$  \$$$$$$   \$$$$$$   \$$$$$$    \$$$$$$$                       
                                                                                                                                                                
                                                                                                                                                                
                                                                                                                                                                
                         __                                          ______                                                              __                     
                        |  \                                        /      \                                                            |  \                    
 __   __   __   ______  | $$____    _______  ______   ______ ____  |  $$$$$$\ ______    ______   __   __   __   ______    ______    ____| $$  ______    ______  
|  \ |  \ |  \ /      \ | $$    \  /       \|      \ |      \    \ | $$_  \$$/      \  /      \ |  \ |  \ |  \ |      \  /      \  /      $$ /      \  /      \ 
| $$ | $$ | $$|  $$$$$$\| $$$$$$$\|  $$$$$$$ \$$$$$$\| $$$$$$\$$$$\| $$ \   |  $$$$$$\|  $$$$$$\| $$ | $$ | $$  \$$$$$$\|  $$$$$$\|  $$$$$$$|  $$$$$$\|  $$$$$$\
| $$ | $$ | $$| $$    $$| $$  | $$| $$      /      $$| $$ | $$ | $$| $$$$   | $$  | $$| $$   \$$| $$ | $$ | $$ /      $$| $$   \$$| $$  | $$| $$    $$| $$   \$$
| $$_/ $$_/ $$| $$$$$$$$| $$__/ $$| $$_____|  $$$$$$$| $$ | $$ | $$| $$     | $$__/ $$| $$      | $$_/ $$_/ $$|  $$$$$$$| $$      | $$__| $$| $$$$$$$$| $$      
 \$$   $$   $$ \$$     \| $$    $$ \$$     \\$$    $$| $$ | $$ | $$| $$      \$$    $$| $$       \$$   $$   $$ \$$    $$| $$       \$$    $$ \$$     \| $$      
  \$$$$$\$$$$   \$$$$$$$ \$$$$$$$   \$$$$$$$ \$$$$$$$ \$$  \$$  \$$ \$$       \$$$$$$  \$$        \$$$$$\$$$$   \$$$$$$$ \$$        \$$$$$$$  \$$$$$$$ \$$      
                                                                                                                                                                
                                                                                                                                                                
                                                                                                                                                                

""")

usercam = int(input('Choose camera output (0-5): '))
if usercam == 0:
    camera = cv2.VideoCapture(0)
elif usercam == 1:
    camera = cv2.VideoCapture(1)
elif usercam == 2:
    camera = cv2.VideoCapture(2)
elif usercam == 3:
    camera = cv2.VideoCapture(3)
elif usercam == 4:
    camera = cv2.VideoCapture(4)
elif usercam == 5:
    camera = cv2.VideoCapture(5)

wm = ("On another device please go to your computer's ip address (http://" + IP_address + ":5000)")
print(wm)



app = Flask(__name__)

def gen_frames(): 
    while True:

        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpeg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """live image"""
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    """webcam live view"""
    return webcontent

@app.route('/main.css')
def cssdoc():
    """css"""
    return css

if __name__ == '__main__':
    app.run(host='0.0.0.0')