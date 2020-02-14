import requests, json, turtle


iss = turtle.Turtle()

def move_iss(lat, long):
    global iss

    iss.penup()
    iss.goto(long, lat)
    iss.pendown()
    

def setup(world):
    global iss
    
    world.setup(1000,500)
    world.bgpic('earth.gif')
    world.setworldcoordinates(-180, -90, 180, 90)

    turtle.register_shape("iss.gif")
    iss.shape("iss.gif")


def track_iss():
    url = 'http://api.open-notify.org/iss-now.json'
    response = requests.get(url)

    if response.status_code == 200:
        json_string = response.text
        response_dictionary = json.loads(json_string)
        position = response_dictionary['iss_position']
        print('International Space Station at ' + position['latitude'] + ', ' + position['longitude'])
        lat = float(position['latitude'])
        long = float(position['longitude'])
        move_iss(lat, long)

    else:
        print("Houston, we've had a problem:", response.status_code)

    widget = turtle.getcanvas()
    widget.after(5000, track_iss)

    
def main():
    global iss

    screen = turtle.Screen()
    setup(screen)
    track_iss()
    
if __name__ == '__main__':
    main()
    turtle.mainloop()
