# Progress report of the CRAPy project


## Progress: Monday 04 January, 2021

#### Adjaye:

- Downloaded Fusion 360 and began brainstorming ideas for CAD design.

#### Francesco:
- Carried out first tutorials for processing so I can get some knowledge on the graphical part of the Genetic NN code
- Dowloaded Anaconda, Processing and Atom to work with python
- Read part of the script for creating the plaentary climate model. I have figured out the variables needed but my knowledge of python and physics isn't good enough yet to make sense of most part of the code. If you want to check it out you can find it on (https://github.com/Planet-Factory/claude/blob/master/CLAuDE%20NOM.pdf)

#### Jonas:
- Restructured the github repo for the new project (deleted unecessary files and changed directory struct) and created a [script](https://github.com/Jonastjep/CRAPy/blob/master/Tutorials/createProjStruc.py) to make this file. Also created a table of content for facilitating navigation for the readers.
- Improved the [Genetic NN code](https://github.com/Jonastjep/TinyProjects/tree/main/ObstacleAvoidance/ObstacleAvoidance_js/AI_version "Some cool stuff!") for automated obstacle avoidance ([click here to see the training in action](https://jonastjep.github.io/TinyProjects/)):
	- Changed the NN creation and setup code from homebuilt to TensorFlow.js (more ressource hungry but more efficient on many levels)
	- Tried to improve the fitness function a little (failure to notice any differences, need to rethink the architecture and verify any mistakes)
	- Added a slider change the speed of evolution of the algorithm. Allows for faster training as until now was difficult to see improvement because the training was so slow. We can now focus on the architecture of AI, optimizing the fitness function and seeing how efficient the mutation is (maybe switch from fully random to a Gaussian change). Also until now cross-over has not been implemented, so this should be a big priority.
- Debugged the [user game version](https://github.com/Jonastjep/TinyProjects/tree/main/ObstacleAvoidance/ObstacleAvoidance_js/Game_version) of the AI framework and changed the color palette.
- Looked a little around to see the capabilities of the thermal IR sensor and bicubic interpolation of 2D grid.

#### Juliette:
- Downloaded programs (Fusion 360, installed Python and Atom)
- Read through python textbook, created list of basic commands

#### Marco:
- started to create the environment in which the lidar software can be tested
- learnt how different pathfinding algorithms work in respect to lidar
	- looked over existing code to get an initial idea of how the software can be structured

#### Timon:
- Brainstorm ideas for arm redesign (different platform position, gearing and toolchanger)


#### Sushant:


## Progress: Tuesday 05 January, 2021

#### Adjaye:

- Listened in to the tutorial by Jonas and began testing/practicing making objects in Fusion 360.


#### Francesco:
- Learned the basic use of Arduino and RaspberryPi and how these can be connected to various sensors through flask. The level was very basic but I understood how the basic electronics and programming principles behind switching on and off a LED light connected to an Arduino through a potentiometer. Pretty useful tutorial to get a hang of how arduino's work in case you don't know it yet (https://www.youtube.com/watch?v=nL34zDTPkcs&ab_channel=Afrotechmods)
- Watched another series of tutorials on how to use Processing and how to programme interactive geometrical shapes and drawings
- Attended the amazing tutorial by jonas on how to work with Flask and GitHub
- Dowloaded Git and watched a couple of extra tutorials on how to use Git and the basic principles of Flask

#### Jonas:
- Gave a (very) long and hopefully interesting tutorial about the pleasures of SSH, VNC, Flask and Git/Github.
- Discussed with Sushant the ways he could implement a sensor graphic onto the Flask server and the advantages of JSON or SQLite. Not yet conclusive, so keep an eye on Sushants work.
- Struggled with the AMG8833 thermal sensing module. Got values out, so this is nice, but absolutely impossible to find a way to plot it and refused to use PyGame, which would have no feasible way of implementing to a flask app. Tried matplotlib, seaborn, plotly and openCV, best result to have come out was OpenCV but was not successful at animating it. Just realized that p5.js might be a good possibility, but have to see how to pass the data to the script... Positive side is that the sensor is working and it is possible to see from the values the wiggle of fingers.
	- The problems encountered is how do I create the 8x8 images, and simultaneously send them to the js script for reading
	- **Late night update, possibility using websocket. To be investigated further...**
- Also Started working on a cheat file for the Git/ssh commands. Will be available tomorrow probably

#### Juliette:
- Attended Jonas' tutorials on Git/GitHub, SSH, and Flask and began practicing/researching basic concepts.
- Downloaded and Installed Git and Flask
- Started practicing and brainstorming on Fusion 360 

#### Marco:
- succesfully created version one of the environment to test the lidar. Point clouds are now generated on command if objects are within range of the simulated lidar. Still need to fix so the lidar range is blocked by objects (currently there is clipping).
	- The simulated rover only moves up/down/left/right instead of forward/backwards/rotation -> this needs to be fixed to better simulate the rovers movements
	- the lidar also will need to be changed to simulate blockages


#### Timon:
- Optimize slicer profile for PETG filament and do test prints
- Develop more concrete ideas for the robotic arm and find out what the different available motors are capable of.


#### Sushant:


## Progress: Wednesday 06 January, 2021

#### Adjaye:

- Collaborating with Timon to decide which aspects of the design we will be in charge of and getting the basic run down of the parts needed in this iteration of the project and their importance from Marco and Jonas.

#### Francesco:
- Manged to set my git (baby steps for a bio students)
- Looking into using python to code  for the sensors' module. Still far away from what I need to know

#### Jonas:
- Wrote the Git/Github [tutorial](https://github.com/Jonastjep/CRAPy/blob/master/Tutorials/Setting_Git%26Github.md) for the team
- Managed to stream the thermal camera using Python websockets and processing!! :) This should be very low computing for the RPi and low latency as it's the host computer that does all the work. Nice video example. Still need to do the interpolation (we hope for bicubic) that might make it a bit heavier for the Rpi but not much. But this took some time...
- Had a look at the LiDAR and despaired on the discovery that it can only be controlled through ROS

#### Juliette:
- Began Flask tutorial from the official website
- Created first app with Flask that displays "Hello, world" when using the link of the ip adress.

#### Marco:
- Fixed lidar environment.
	- now only objects in rover fov are added to point cloud - as would be the case with real lidar. movement mechanic logic was changed to make smoother use. rover no longer clips through obstacles. point clouds still generated on command. personal computer broke so started using jonas' spare. files in branch Marco are by marco despite being pushed by different user - this valid until specified. 
- 3d design
	- discussed with adjaye and timon the way forward regarding design of components. outlined 6 reccesary practical aspects of the project; 5x ultrasound mounts for hardpoints onto rover body, robotic arm with manipluation attachment, solar panel/ material deposit tray, fix current defective pieces, camera/lidar mount, other small sensor housings.
	- work split as follows; timon - robotic arm, adjaye - solar panel and material deposit, marco - camera and lidar mount, whole team - fix current defective pieces,  ultrasound mounts and small sensor housings are trivial designs open to whoever wants.

#### Timon:
-3D model bracket that mounts to rover for arm
- discoss with adjaye how the arm and the solar panel can be operated on the rover
- start tallking about ideas of how to stop the axles from slipping


#### Sushant:


## Progress: Thursday 07 January, 2021

#### Adjaye: 
- Continuing to develop ideas for the rover's solar panel and sample box design.


#### Francesco:
- Menaged to connect to raspberry pi from Italy through ssh and VNC, controlled the temperature sensor.
- Next step is try to build a database with sqlite, store in it the data obtained from the temperature sensor and form a graph using Matplotlib. Then display the data using JustGage and then make the graphed data available through a web app made with flask. It's a work in progress
- To do all pf this with my little knowledge I have also been following some tutorials on how to programme with python, especially in the context of 

#### Jonas:
- Discovered the pressure sensor was not working (only after a loooong period of troubleshooting) so had to solder a new one together and conect it to the RPi to allow access through ssh for Francesco. Also had to figure out how to configure the I2P port address for the [Adafruit BMP280 libraries](https://github.com/adafruit/Adafruit_CircuitPython_BMP280/blob/f65303074498e07db883e73c067a8b9e491451a2/adafruit_bmp280.py#L399). Alot of issues due to the fact our sensor is not genuine. Also had to figure out if it was a BME280 or BMP280 (it's the latter). Alot of time went into just figuring out these things.
- Had a zoom conference with Italy to help with taking control of a remote server (a RPi) and using it to run some python software.
- Spent some time reflashing another RPi and updating it up. Issues with the headless connection through wifi but fixable.

#### Juliette:
- Continued tutorial for a longer app with Flask
- Trip back to Maastricht, delays in both flight and trains.

#### Marco:
- partially installed the neccesary ROS software needed to operate lidar (still proving to be tricky)
- began designing first iteration of the camera/lidar sensor mast
- reviewed current physical design flaws and neccesary improvements 
- reveiwed methods to export point cloud data from ROS into a more managable format for end-used consumption
- set up fusion 360 team and made accessible the previous design of the rover for design reference

#### Timon:
- Develop and 3D print (and improve it again) a snap on attachmet that can be used to attach all other sensors etc. to the rover.
- identify broken parts on the rover that need to be reprinted
- start printing replacement parts with reiforcememnt out of PETG for the rover
- experiment with drilling of the axles to aviod slipping
- retrieving a vice to hold the axles while drilling them
- drilling hoes into all axles to prevent slipping

#### Sushant:


## Progress: Friday 08 January, 2021

#### Adjaye:
- Collaborating with Timon on solar panel and sample box design
- Begin implementing the design into CAD


#### Francesco:
- Still working on the creation of a web app to store and display the data from the temperature and pressure sensor (BMP280). Until now I managed to build a database with sqlite, store in it the data obtained from the temperature sensor. The next step is to form a graph using Matplotlib and display the data using JustGage. Ultimately the app for display will be made with flask but to do so I think I will need to be in maastricht to get some assistance from more experienced prigrammers... Jonas has been very helpful!
- Menaged to create a working database and programme to store the data directly from the sensor. Next step is to create a query, to format the raw data into a readable form. Then a falask web app to visualise this form.

#### Jonas:
- Wrote the Raspberry [Pi setup/connection tutorial](https://github.com/Jonastjep/CRAPy/blob/master/Tutorials/Setting_Up_The_RPi.md) that explains how to setup a headless RPi and take control of it. 
- Also wrote the [ssh and remote control of system tutorial](https://github.com/Jonastjep/CRAPy/blob/master/Tutorials/RemoteConnection_tutorial.md), to explain how to remotely use a GNU/Linux system (specifically RPi) from afar.
- Helped Juliette a little bit with flask (Vorführeffekt) and gave some advice to Francesco.
- Disassembled the suspentions of the Rover with Timon to test out the new PETG part, but infill was too low and piece cracked when pushing it with a bearing. 
- Rethought the fitness function of the genetic AI: add negative fitness points to models that turn too much and that don't push on the forward button. This should take care of the ones that turn in a circle indefinitely as well as the ones that just stop down.
	- Added features that allow for death timer to be removed and added the choice to leave the forward motion to the rover (we can now force the rover to always have it's foot on the accelerator - it totally removes the problem of static cars and disfavours the rotating ones)

#### Juliette:
- Had issues with the Flask app and the virtual environment, solved now.
- Installed PUTTy for SSH and connected to Raspberry pi
- Making app with flask and SQLite for sensors from Raspberrypi

#### Marco:
- continued the design process for the sensor mast, worked through two iterations each using a different design to move camera and optical equiptment. finalised the orientation of equiptment on the mast, as lidar needs a 360 degree unimpeded view whereas if camera and optical equiptment has small blindspots it is not a big issue (given that default position is unimpeded).

#### Timon:
- Develop and test new slicing profile for increased strength PETG parts
- Start printing PETG replacement parts

#### Sushant:


## Progress: Saturday 09 January, 2021

#### Adjaye: 
- Implemented the first version of the sample collection box into Fusion 360 that utilizes a slider crank to open and close the box.


#### Francesco:
No progress due to trip from Italy to Maastrict! The car broke down.

#### Jonas:
- Worked on implementing the new fitness model to the genetic algorithm. The changes don't gives very different results, probably because the values are not well set... Need to sit down and think about the optimal aditions of fitness values to the score.
- Also looked into making the cross-over. I (or someone else from the team) should probably continue the python implementation, as python has many more tools for these tasks. It's just nice that p5.js can be run on the browser.

#### Juliette:
- Database creation using sqlite. Used commands in shell to create a table, insert data, and retrieve the table to ensure proper functioning of code.
- Learn to structure python scripts for database creation as well so commands don't need to be manually entered every time but instead it is better to just call in the python file with the commands included in it.

#### Marco:
- completed the design for the uper part sensor mast where optical sensors are located. now only need to design a secure method to fix bottom end of pvc pipe to rover body and sensor assembly will be complete. **visible in my branch if yous are curious**

#### Timon:
- Continued printing replacement parts

#### Sushant:


## Progress: Sunday 10 January, 2021

#### Adjaye: 

- Day off


#### Francesco:
- Arrived in Maastricht late due to journey delay (broken car)
- Menaged to set up another programme to log data automatically and have been working on a way to let the programme run continously but let it stop at a precise point, like once every single hour it should collect informations, feed them to the database and then stop, to start again in the next hour. Still need to define well how to do it.

#### Jonas:
- total day off :) (almost)

#### Juliette:
- Researched possible sensors that we would be using (still need to know what sensors we have to research how they work)
- Learned about DHT sensors and followed basic tutorials on it

#### Marco:
- nothing this was day off 

#### Timon:
- Continued printing replacement parts 
- Enjoyed the weekend

#### Sushant:


## Progress: Monday 11 January, 2021

#### Adjaye:
- Continuing to work on the sample box v1.

#### Francesco:
- I have been working on the second part in the creation of a web app, trying to form a quary. However, I have been stuck all day on the same problem, the storing table does not get recognised by the gueryTableBMP280.py programme and I can't figure out why!
- Just menaged to make the query work, it was due to a spelling mistake!!!

#### Jonas:
- Printed more wheel parts in PLA and tested using PrusaSlicer instead of Cura: excellent results, I'm converted!
- Reassembled the rover almost fully, the shafts are still a pain to install, but PETG seems promising. Some older parts look on the verge of collapse, but planning on tying to add some epoxy for structural integrity.
- Helped a little bit around with Flask and the ROS installation, when needed.

#### Juliette:
- Went over the GPS files in the github to understand what has been done and how (defining line by line how the python files are written, which also helps to learn python structure, the different functions, and what it is possible to do)
- Attempted to work with pressure/temp sensor to create database using sqlite (not quite successful yet)

#### Marco:
- succesfully downloaded and istalled the neccesary ROS onto a secondary raspberryPi to test if it worked. Did not. had to wipe the microSD and reinstall the software with little success. Now trying to retrace steps and redo all with extra attention to see if steps were overlooked. If the ROS and other software neccesary to run lidar on a raspberryPi can be succesfully downloaded in the following days then there should be no probelem implementing on actual rover. 

#### Timon:
- Made the bracket that attaches the arm to the chassis in fusion 360
- made the motor mount for rotation of the arm in F360
- Transferred bearings from old to new parts and hammered them in
- Assembled suspension and drivetrain related parts of the rover

#### Sushant:


## Progress: Tuesday 12 January, 2021

#### Adjaye:


#### Francesco:


#### Jonas:
- Started the prints for the camera and LiDAR attachement module, will probably have the module tomorrow
- Managed to finally make the LiDAR work with Marco, what a pleasure to see the point cloud delimiting my room! I just helped debugging a little the commands needed for the setting up
- Discussed sensor modules with Francesco and Juliette. Starting to figure out where we want to go, probably starting on the datacollection tomorrow or something. We'll see how well the nRF24 sensors work and how we can implement all this.
- Managed to create a mapping inteface for GPS data. Works super nicely, just waiting to have implemented many more features than simply all data or query a certain amount of latest data (for example, give two dates, and map the travel between; also centralize the map on the tracks first point, still to do). Will probably make pull request tomorrow. Had issues with cached json files in browser, but found solution.
- Wrote some demos for data conversion between CSV, SQLite database and JSON. Good for the people of the group interested.
-Also this mapping is proof of concept of how we will make all of the interactive plots etc on the webapp: This worked fabulously and leaves us with alot of control. Need to discuss this with the others tomorrow.

#### Juliette:
- Discussed sensors with Jonas and Francesco to figure out a plan (how to implement them together)
- Attempted with Francesco to establish communication between Arduino and Raspberry pi through rnf24l01 transceivers (searched for standard connection mappings between sensors and raspberry pi) - Had issues making this work.
- Found a tutorial for nrf24l01 communication from Arduino to Arduino (instead of Arduino to Raspberrypi) https://lastminuteengineers.com/nrf24l01-arduino-wireless-communication/ (will run this on wednesday with Francesco)

#### Marco:
- lidar now working (mainly thanks to jonas for troubleshooting with me). required several reflashing of sd card until we chose to use a disk image with ROS kinetic alreadz installed with ubuntu 16. this allowed us to bypass several installation steps that were previously problematic. running codes to activate and perate lidar are as follows. `roslaunch ydlidar_ros_driver X4.launch` hen in another windown run `rviz` to open the ROS software. then within the ROS software `file>open confi>ubuntu>ydlidar_ws>src>ydlidar_ros_driver/launch/lidar.rviz` to get real time lidar info on screen. 
	- looks cool and proves it works, does not yet actually create a map to then be stored. The next steps are as follows; implement SLAM to create a static point cloud that can then be exported to flask web app.this will alow the end user to view the map created by the rover in real time (hopefully). 
	- should it all work then the actual rasPi used on the rover will need to be reflashed with disk image used on test rasPi. everything will need to be redone on the actual rasPi, for this first i will make a tutorial/log of everything we did to get the current rasPi working, not only to make replication easier but also to ensure future groups are able to use the LiDAR module if they want to.


#### Timon:
- Discussed with Adjaye various ways of how the solar panel could be lifted (worm gear, regular gear reduction, linear actuator)
- discussed more concretely what areas of the front of the rover are available for which mechanisms
- Designed the base of the arm which holds the first link 
- Started with the first link of the arm.

#### Sushant:


## Progress: Wednesday 13 January, 2021

#### Adjaye:


#### Francesco:
- Have been working on the connection between raspberry pi and arduino using the radio frequencies. Following this tutorial https://medium.com/@anujdev11/communication-between-arduino-and-raspberry-pi-using-nrf24l01-818687f7f363
- The tutorial we were following didn't prove useful so we changed plan, with Juliette we will try to connect two arduinos, one attached to the rover's raspberry pi and one attached to the headquarters' raspberry pi.
- With jonas and juliette we menaged to make two NRF24L01 communicate, one reciver and one transmitter, but we fail to have a clear connection where we have a message being recieved aaandaa a message being sent back, to confirm the message being recieved.

#### Jonas:


#### Juliette:
- Worked with Francesco on nrf24l01 communication. Attempted again to follow a tutorial between Raspberry pi and Arduino (see Francesco's report for link) but it was unsuccesful. Decided to stick with Arduino to Arduino wireless communication.
- With the help of Jonas, Francesco and I finally made the two nrf24l01 communicate, following a simple code for two-way transmission (one code for the transmitter and one for the receiver) https://forum.arduino.cc/index.php?topic=421081
- Problems receiving an acknowledgement message back from the receiver so transmitter cannot confirm message has been successfully received.

#### Marco:
- wrote tutorial on how to set-up rasPi for lidar operation, starting from a new blank rasPi all the way to lidar operation. Visible under tutorials folder of master branch and titled Lidar_rPi_tutorial.md
- worked on initial  3d printed parts of the sensor mast design to prepare them for assembly.

#### Timon:
- Improved the base of the arm and other parts so that the first link can rotate down as far as possible. This is so that the arm can be as short as possible to make it more lighweight and easier to lift for the motors
- indentified broken hub parts that need to be replaced
- retrieved heat inserts and screws from broken parts
- searched together all screws neccesary for the wheel assembly
- put heat inserts and screws into new parts
- Partially assembled hubs and motors

#### Sushant:


## Progress: Thursday 14 January, 2021

#### Adjaye:


#### Francesco:
- Found this tutorial https://forum.arduino.cc/index.php?topic=623796.0 to conenct arduinos and send data. We are going to test the code and connection between our two NRF24L01 modules 
- With Juliette we menaged to make two antennas nRF24L01 communicate at long distance, sending messages and receving them. The confirmation of having recieved the message doesn't work from reciver to transmitter. Next step is to make that work, so that we can have the rover confirming a message has been recieved or sent. N.B. This was difficult (jonas agrees)
- We menaged to get the reciver to send a confirmation signal to the transmitter. The problem wasn't the code but rather the connection and the equipment we were using, probaby in relation to the cables and the way in which they connect

#### Jonas:


#### Juliette:
- Working with Francesco, still trying to make the nrf24l01 sensors work.
- Researching how to send data from sensors through transceivers.
- nrf24l01 worked!! at "long" distance! Acknowledgement message still missing, need to review code and find where it fails to send confirmation receipt.
- Managed to get 7 confirmation messages from the receiver! Possible problems with connections
- Placed a few screws here and there in the rover

#### Marco:


#### Timon:
- Realize that a few more hubs are broken
- Harvest heat inserts from old hubs and put into new hubs
- Shorten axles that were too long, using a plastic bag in the process
- mount wheel carriers onto the suspension assembly
- attach all 10 motors, by numbers to each position
- shorten screws because there weren´t enough of the right size
- attach wheels
FINALLY 10 WHEELS THAT DON´T SLIP!!! 

#### Sushant:


## Progress: Friday 15 January, 2021

#### Adjaye:


#### Francesco:
- With Juliette we have been trying to send the data directly from the arduino to the other through he nRF24L01 module underthe form of strings. This tutorial might be useful https://forum.arduino.cc/index.php?topic=436525.0. We should also start to think about the way to send a serial communication from the sensors to the raspberry pi and form a database there. But this is for future moment.
- We gave up on sending data between the two nRF24L01 modules because the connection is too unstable and continously brakes, which also makes it very difficult to test the code and the way in which data are sent. NOTE on future improvements: use more powerful antennas and to try to have a more stable connection

#### Jonas:


#### Juliette:
- Spent first hours working with each sensor (separately) to obtain individual codes as well as proper cable connections for each (that way we can be sure we can make them all work properly. Did this for mq2-gas sensor | hcsro4-ultra sound sensor | dht11 - temperature and humidity sensor)
- Worked on combining code of nrf24l01 transmitter sensor with one of the individual scripts (chose hcsro4 - ultra sound sensor for this because it was the one working best)
- Assembled the arduino connection with the two sensos (nrf24l01-transmitter and hcsro4)
- Ran into problems compiling the script due to type mismatch between the needed type for the transmitter (String) and the one established in the sensor (long)
- Worked with Francesco finding tutorials to send sensor data from one Arduino to the other as Strings
- With the help of jonas we used .concate() to adhere the data into a string, this solved the compiling problem
- Uploaded the script and attempted to send sensor data over the transceivers. The receiver did not get any message at all. Printed values in the code to make sure the data variable was indeed containing the data received from the ultra sound sensor, this was correct. 
- Attempted to run simple code again (which had work the day before and had even sent acknowledgement receipts). This connection failed as well. Thus, the problem was deemed to be within the connection of the trasnceivers. Gave up on sending data between the nrf24l01 modules.
- Focused on producing a combined code by adding one more sensor (the mq2- gas sensor)
- Managed to compile a code containing all the info for the nrf24l01 transmitter, the hcsro4 ultra sound sensor, and the mq2 gas sensor.
- Made all connection to the arduino, uploaded the script, ran it. Successful retrieval of data.

#### Marco:


#### Timon:
- experiment with rubber bands to determine what extensions they should operate at and what force they are able to provide
- Designed first link of the robotic arm


#### Sushant:


## Progress: Saturday 16 January, 2021

#### Adjaye:


#### Francesco:
- Have been working on two main things, the first one is to find a way to transform the data from the arduino into a json format to be sent over to the raspberry pi. The other is the creation of a programme to recive the data on the raspberry pi and serial it into different variables to store in arrays which will then be used to form sqlite database. I have menaged to get a bit further on this part, mainly due to the fact that today I didn't have any access to the arduino, so it was difficult to test the code.
- I still have to understand better how to sort out the data for the serial communication, but once that is done, the next step is create a flask app and display all the data collected into the sqlite database.
#### Jonas:


#### Juliette:
- Looked into JSON structure in arduino to send organized data from the code of the arduino to the Raspberry pi
- Cleaned up a bit the combined code of the arduino

#### Marco:


#### Timon:
- starting with printing of parts of the robotic arm

#### Sushant:


## Progress: Sunday 17 January, 2021

#### Adjaye:


#### Francesco:
- Scratched off part of yesterday's work because json is needed after the data has been stored in sqlite, not before. Menaged to write a code that takes the data from serial of arduino, stores them into a sqlite database.
- Through another programme I convert the sqlite data into the json type data, which will be then used in the flask app that I am currently writing.
- All these programs still need to be tested, but the main part of that will be simply trubleshooting
- We will also need to start to write a programme for the arm and the light sensors.

#### Jonas:


#### Juliette:
- Added dht11 sensor to the combined code in the arduino. (Now this code has nrf24l01, hcsro4, mq2, and dht11 implemented - Compiled successfully).
- Organized data in a variable that separates values with a ",". Need to figure out how to implement json structure. (jonas explained, json not needed from Arduino).
- Error when running as the data for dht11 sensor returns 0 and 0 for temperature and humidity.
- Ran sensor individually with script done on friday, it works. Currently trying to find the issue within the combined code as the logic and commands are the same.

#### Marco:


#### Timon:
- continue printing parts of the robotic arm
- testing fitment of pars
- changing parameters of the parts (e.g. bearing fitment) 


#### Sushant:


## Progress: Monday 18 January, 2021

#### Adjaye:


#### Francesco:
- Created the first part of the web app and tested it with a randomly populated set of data. Passed on the whole day trouble shooting, the code is very big.
- Worked with Chart.js and revisioned how to make graphs

#### Jonas:


#### Juliette:
- Found issue with dht11 sensor, fixed code (was missing a read command before retrieving the data). 
- Now working with bmp280 sensor. Having issues running examples and actually, any code ("sensor not detected").
- Problem solved with the help of Jonas: Edited library, used the SPI protocol instead of I2C, and added .begin() command. 
Now implemented individual script into combined code. 
- All 5 sensors (nrf24l01, hcsro4, mq2, dht11, and bmp280) are now in the script :) Everything runs correctly!
- Organized the data (small details such as no spaces, different headers, proper separators)
- Placed the connections in the Arduino Mega taking into account future needed pins (bmp280 changed to I2C since SPI is needed for nrf24l01).
- Need to add GPS sensor now. Running individual script, I get responses but no data. Might be due to our positioning not getting any data from satellites.
- Soldered cables, added some heat inserts, and used a hammer for apparently the first time!?

#### Marco:


#### Timon:
- designing second link of the robotic arm
- printing more parts of the arm
#### Sushant:


## Progress: Tuesday 19 January, 2021

#### Adjaye:


#### Francesco:
- Continued with yesterday's trouble shooting and have been working on some ideas for the video

#### Jonas:


#### Juliette:


#### Marco:


#### Timon:
-take all parts and assemble to a working arm! (longer than expected)
- print more hubs that don´t break (more perimeters jonas!)
#### Sushant:


## Progress: Wednesday 20 January, 2021

#### Adjaye:


#### Francesco:
- Adapted the web app code with the Arduino code from Juliette. I have also created two databases to store data from the GPS in one, and data from the sensor in the other.
- Also began to write the script for the video

#### Jonas:


#### Juliette:


#### Marco:


#### Timon:
- Construct part that pitches and rotates the toolhead
- adapt the grabber

#### Sushant:


## Progress: Thursday 21 January, 2021

#### Adjaye:


#### Francesco:
- Finished the script for the video this morning. I am waiting for a reply from the members of the team.

#### Jonas:


#### Juliette:


#### Marco:


#### Timon:


#### Sushant:


## Progress: Friday 22 January, 2021

#### Adjaye:


#### Francesco:


#### Jonas:


#### Juliette:


#### Marco:


#### Timon:


#### Sushant:


## Progress: Saturday 23 January, 2021

#### Adjaye:


#### Francesco:


#### Jonas:


#### Juliette:


#### Marco:


#### Timon:


#### Sushant:


## Progress: Sunday 24 January, 2021

#### Adjaye:


#### Francesco:


#### Jonas:


#### Juliette:


#### Marco:


#### Timon:


#### Sushant:


## Progress: Monday 25 January, 2021

#### Adjaye:


#### Francesco:


#### Jonas:


#### Juliette:


#### Marco:


#### Timon:


#### Sushant:


## Progress: Tuesday 26 January, 2021

#### Adjaye:


#### Francesco:


#### Jonas:


#### Juliette:


#### Marco:


#### Timon:


#### Sushant:


## Progress: Wednesday 27 January, 2021

#### Adjaye:


#### Francesco:


#### Jonas:


#### Juliette:


#### Marco:


#### Timon:


#### Sushant:


## Progress: Thursday 28 January, 2021

#### Adjaye:


#### Francesco:


#### Jonas:


#### Juliette:


#### Marco:


#### Timon:


#### Sushant:


## Progress: Friday 29 January, 2021

#### Adjaye:


#### Francesco:


#### Jonas:


#### Juliette:


#### Marco:


#### Timon:


#### Sushant:


## Progress: Saturday 30 January, 2021

#### Adjaye:


#### Francesco:


#### Jonas:


#### Juliette:


#### Marco:


#### Timon:


#### Sushant:


## Progress: Sunday 31 January, 2021

#### Adjaye:


#### Francesco:


#### Jonas:


#### Juliette:


#### Marco:


#### Timon:


#### Sushant:


## Progress: Monday 01 February, 2021

#### Adjaye:


#### Francesco:


#### Jonas:


#### Juliette:


#### Marco:


#### Timon:


#### Sushant:
