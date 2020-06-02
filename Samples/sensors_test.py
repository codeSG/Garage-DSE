from adafruit_clue import clue
from adafruit_bitmap_font import bitmap_font

clue.sea_level_pressure = 1020

clue_data = clue.simple_text_display(title="CLUE SENSOR DATA!", text_scale=2)

while True:
    clue_data[0].text = "Acceleration: {:.2f} {:.2f} {:.2f} m/s^2".format(
        *clue.acceleration
    )
    clue_data[1].text = "Gyro: {:.2f} {:.2f} {:.2f} dps".format(*clue.gyro)
    clue_data[2].text = "Magnetic: {:.3f} {:.3f} {:.3f} uTesla".format(*clue.magnetic)
    clue_data[3].text = "Pressure: {:.3f} hPa".format(clue.pressure)
    clue_data[4].text = "Altitude: {:.1f} m".format(clue.altitude)
    clue_data[5].text = "Temperature: {:.1f} C".format(clue.temperature)
    clue_data[9].text = "Color: R: {} G: {} B: {} C: {}".format(*clue.color)
    clue_data[10].text = "Button A: {}".format(clue.button_a)
    clue_data[11].text = "Button B: {}".format(clue.button_b)
    clue_data.show()
