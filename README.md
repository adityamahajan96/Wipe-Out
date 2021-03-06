# WipeOut: A Social Media Data Eraser Tool

## 1. WipeOut for Facebook

### Geckodriver for Firefox:
- Install **geckodriver** and other required packages for **Selenium Webdriver** in Python.
- Add the relative path of **geckodriver** w.r.t. the *fb_eraser.py* script on the following line inside the script: 
	- `driver = webdriver.Firefox(executable_path = 'geckodriver_relative_path/geckodriver.exe')`

### XAMPP Server Installation and Configuration:
- Install the latest version of **XAMPP Server** on your PC.
- By default, XAMPP server doesn't support *Python scripts*. So, we need to configure the `Apache httpd.conf` configuration file. 
- Go to the end of the configuration file and add these two lines:
	- `AddHandler cgi-script .py`
	- `ScriptInterpreterSource Registry-Strict`
	
### Running the application:
- Clone this repository inside the following path:
	- `C:/.../xampp/htdocs/`
- Start XAMPP. Run the *Apache Server* by clicking on `Run`. Wait for a few seconds for the Apache icon to turn Green.
- Now open a new tab on your Firefox browser and type `localhost/Wipeout/`.
- Finally, get started with the application.
