import sys
sys.path.insert(0, '/home/pi/Desktop')
import buzzer_helpers

from bluedot import BlueDot
from signal import pause
from gpiozero import LED
from time import sleep


led17 = LED(17)
led27 = LED(27)
melody = buzzer_helpers.star_wars_melody
#tempo = buzzer_helpers.tempo
tempo = buzzer_helpers.star_wars_tempo
time = buzzer_helpers.time.sleep(2)
#play_super = buzzer_helpers.play(melody, tempo, 1.3, 0.800)
#play_sw = buzzer_helpers.play(melody, tempo, 0.5, 1.0)
#destroy_here = buzzer_helpers.destroy()

def up():
	bd.color = "green"
	print("up LED17 Blink")
	led17.blink(.0625,.0625)
	
def down():
	bd.color = "red"
	bd.square = True
	print("down LED17 Off")
	led17.off()

def upl():
        bd.color = "green"
        buzzer_helpers.setup()
        print("Upper Left Button - Star Wars Imprerial March")
        buzzer_helpers.play(melody, tempo, 0.5, 1.0)

def upr():
        bd.color = "green"
        buzzer_helpers.setup()
        print("Upper Right Button - Super Mario Theme")
        buzzer_helpers.play(melody, tempo, 1.3, 0.800)

def left():
        bd.color = "green"
        print("left LED27 on")
        led27.on()
		
def right():
        bd.color = "red"
        bd.square = True
        print("right LED27 off")
        led27.off()
	
bd = BlueDot(cols=3, rows=3)


#bd[0,0].visible = False
#bd[2,0].visible = False
bd[0,2].visible = False
bd[2,2].visible = False
bd[1,1].visible = False

bd[0,0].when_pressed = upl
bd[2,0].when_pressed = upr
bd[1,0].when_pressed = up
bd[1,2].when_pressed = down
bd[0,1].when_pressed = left
bd[2,1].when_pressed = right

pause()
