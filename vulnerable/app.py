from flask import Flask
import time
import threading

app = Flask(__name__)

# Funny Rickroll HTML
RICKROLL_PAGE = """
<!DOCTYPE html>
<html>
<head>
   
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
    return '<h1 style="color:red;text-align:center;font-size:60px">Open → <a href="/rick">/rick</a></h1>'

@app.route('/rick')
def rick():
    # Log for demo visibility
    print(f"Request received! Active threads: {threading.active_count()} (queue building...)")
    
    # Increased delay for stress test visibility (simulates heavy work)
    time.sleep(1.5)  # 1.5 seconds per request → easy to overload
    
    return RICKROLL_PAGE, 200, {'Content-Type': 'text/html'}

if __name__ == '__main__':
    print("="*60)
    print("VULNERABLE RICKROLL SERVER STARTED - READY FOR STRESS TEST")
    print("Browser: http://localhost:5000 → click /rick")
    print("During stress: Watch me slow down and freeze!")
    print("="*60)
    app.run(port=5000, threaded=False)  # Single-threaded = quick overload
