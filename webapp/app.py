import os
import pygame
from flask import Flask, render_template, redirect, url_for, flash
from waitress import serve

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Flask Application
app = Flask(__name__)
app.secret_key = os.urandom(24)

class Doorbell:
    def __init__(self, sound_file='static/sounds/doorbell.wav'):
        self.sound_file = sound_file     
        # Load sound
        try:
            self.sound = pygame.mixer.Sound(self.sound_file)
        except Exception as e:
            raise ValueError(f"Cannot load sound file: {e}")

    def ring(self):
        try:
            self.sound.play()
            # Wait for sound to complete
            pygame.time.wait(int(self.sound.get_length() * 1000))
            return True
        except Exception:
            return False

# Create doorbell instance
doorbell = Doorbell()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ring')
def ring():
    try:
        # Play sound
        if doorbell.ring():
            flash("Doorbell rang!", "success")
        else:
            flash("Doorbell sound failed", "warning")
    except Exception as e:
        flash(f"Error: {str(e)}", "error")
    
    return redirect(url_for('index'))

def main():
    try:
        serve(app, host='0.0.0.0', port=5001)
    except Exception as e:
        print(f"Failed to start server: {e}")

if __name__ == '__main__':
    main()
