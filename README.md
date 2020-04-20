[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![Python 3.6](https://img.shields.io/badge/python-3.6-green.svg)](https://www.python.org/downloads/release/python-360/) [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE) 

# Home_controlling
An IOT project that lets an user control and monitor their home from anywhere even withput strong internet connection

It uses several python modeules:

-**Tkinter**

-**socket**

-**pickle**

-**RPI**

**Tkinter** is used to make the application that can help the user control their home. **socket** and **pickle** libraries are used for data communication between the user and their home.**RPI** module is used to take data from various sensors(i.e home appliances)connected to the raspberry pi micro-controller. 

## Cloning
```bash
$ git clone https://github.com/Shaashwat05/home_controlling
```

## Dependencies
```bash
$ pip3 install -r requirements.txt
```

## Instructions
```bash
$ python3 home.py
$ python3 user.py
```
Run the home.py file on your raspberry pi only, the dependencies are rpi specific. Run the user.py file on your system. Give the rpi's IPV4 adress to user.py(it is preferred if rpi has a static IPV4, it is recommended to host it therfore on a cloud computing pltform)



## Author
[![LinkedIn-profile](https://img.shields.io/badge/LinkedIn-Profile-teal.svg)](https://www.linkedin.com/in/shaashwat-agrawal-1904a117a/)

* [**Shaashwat Agrawal**](https://github.com/Shaashwat05)

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details


