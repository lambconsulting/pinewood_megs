import sys
sys.path.extend(['/home/pi/Desktop/Pinewood'])
import buzzer_helpers

from bluedot import BlueDot
from signal import pause
from gpiozero import LED
from time import sleep

print("Meghan, start up your Pinewood Derby Engines!!!")

led17 = LED(17)
led27 = LED(27)

melody_ul = buzzer_helpers.star_wars_melody
tempo_ul = buzzer_helpers.star_wars_tempo

melody_ur = buzzer_helpers.cat_melody
tempo_ur = buzzer_helpers.cat_tempo



#buzzer_helpers.play(melody_ur, tempo_ur, 0.1, 1.5)


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
        buzzer_helpers.play(melody_ul, tempo_ul, 0.5, 1.0)

def upr():
        bd.color = "green"
        buzzer_helpers.setup()
        print("Upper Right Button - Cat Meow Theme")
        buzzer_helpers.play(melody_ur, tempo_ur, 0.1, 1.5)

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
