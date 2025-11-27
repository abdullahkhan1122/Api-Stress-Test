from flask import Flask
import time
import threading
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(get_remote_address, app=app, default_limits=["10 per minute"])

# Same Funny Rickroll HTML (copied from vulnerable)
RICKROLL_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>You just got served</title>
    <style>
        body { margin:0; background:black; display:flex; justify-content:center; align-items:center; height:100vh; }
        img { width:90vw; max-width:800px; box-shadow: 0 0 50px cyan; }
        h1 { position:absolute; top:20px; width:100%; text-align:center; color:cyan; font-size:50px; 
             text-shadow: 0 0 20px cyan; font-family: Comic Sans MS; }
    </style>
</head>
<body>
   <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ3ppYXlycjZ0dGwzbWI0MnJtaWMweTk4bjQ1N3JicnZpZ3gyamUxaCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/GXiasDXfP0j8Q/giphy.gif" alt="Rick Astley dancing">
</body>
</html>
"""

@app.route('/')
def home():
    return '<h1 style="color:green;text-align:center;font-size:60px">Protected! Open → <a href="/rick">/rick</a></h1>'

@app.route('/rick')
@limiter.limit("5 per minute")  # Strict limit for clear demo
def rick():
    # Log for demo
    print(f"Allowed request! Active threads: {threading.active_count()}")
    
    time.sleep(1.5)  # Same delay, but limits prevent overload
    
    return RICKROLL_PAGE, 200, {'Content-Type': 'text/html'}

if __name__ == '__main__':
    print("="*60)
    print("PROTECTED RICKROLL SERVER STARTED - STRESS TEST PROOF")
    print("Browser: http://localhost:5000 → click /rick")
    print("During stress: I stay fast - excess get 429 error!")
    print("="*60)
    app.run(port=5000, threaded=False)