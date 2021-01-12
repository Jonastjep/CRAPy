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
- Trip back to Maastricht, delays in both flight and trains.
- Continued tutorial for a longer app with Flask

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


#### Sushant:


## Progress: Saturday 09 January, 2021

#### Adjaye:


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


#### Sushant:


## Progress: Sunday 10 January, 2021

#### Adjaye:


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


#### Sushant:


## Progress: Monday 11 January, 2021

#### Adjaye:


#### Francesco:
- I have been working on the second part in the creation of a web app, trying to form a quary. However, I have been stuck all day on the same problem, the storing table does not get recognised by the gueryTableBMP280.py programme and I can't figure out why!
- Just menaged to make the query work, it was due to a spelling mistake!!!
- Later I menaged to create a webserver and flask app where to display the data collected from the BMP280 sensor. I haven't uploaded the code because jonas has already a similar code onto git.
- Discussed with jonas the possible next steps in the creation of a self driving autonamous rover, next steps involved working with Genetic AI for movement and with the communication between rover and us through radio waves. I had the idea to attach on part of the module (transmitter) on the rover and place the reciver onto a raspberry-pi which we connect to through wi-fi. Still need to figure out how to do it.

#### Jonas:
- Printed more wheel parts in PLA and tested using PrusaSlicer instead of Cura: excellent results, I'm converted!
- Reassembled the rover almost fully, the shafts are still a pain to install, but PETG seems promising. Some older parts look on the verge of collapse, but planning on tying to add some epoxy for structural integrity.
- Helped a little bit around with Flask and the ROS installation, when needed.

#### Juliette:
- Went over the GPS files in the github to understand what has been done and how (defining line by line how the python files are written, which also helps to learn python structure, the different functions, and what it is possible to do)

#### Marco:
- succesfully downloaded and istalled the neccesary ROS onto a secondary raspberryPi to test if it worked. Did not. had to wipe the microSD and reinstall the software with little success. Now trying to retrace steps and redo all with extra attention to see if steps were overlooked. If the ROS and other software neccesary to run lidar on a raspberryPi can be succesfully downloaded in the following days then there should be no probelem implementing on actual rover. 

#### Timon:


#### Sushant:


## Progress: Tuesday 12 January, 2021

#### Adjaye:


#### Francesco:
- Investegated in the morning the uses of radiofrequency nrf24 module andobserved the SGVHAK_Rover git hub, from which we could take some inspiration (https://github.com/Roger-random/SGVHAK_Rover)

#### Jonas:


#### Juliette:


#### Marco:


#### Timon:


#### Sushant:


## Progress: Wednesday 13 January, 2021

#### Adjaye:


#### Francesco:


#### Jonas:


#### Juliette:


#### Marco:


#### Timon:


#### Sushant:


## Progress: Thursday 14 January, 2021

#### Adjaye:


#### Francesco:


#### Jonas:


#### Juliette:


#### Marco:


#### Timon:


#### Sushant:


## Progress: Friday 15 January, 2021

#### Adjaye:


#### Francesco:


#### Jonas:


#### Juliette:


#### Marco:


#### Timon:


#### Sushant:


## Progress: Saturday 16 January, 2021

#### Adjaye:


#### Francesco:


#### Jonas:


#### Juliette:


#### Marco:


#### Timon:


#### Sushant:


## Progress: Sunday 17 January, 2021

#### Adjaye:


#### Francesco:


#### Jonas:


#### Juliette:


#### Marco:


#### Timon:


#### Sushant:


## Progress: Monday 18 January, 2021

#### Adjaye:


#### Francesco:


#### Jonas:


#### Juliette:


#### Marco:


#### Timon:


#### Sushant:


## Progress: Tuesday 19 January, 2021

#### Adjaye:


#### Francesco:


#### Jonas:


#### Juliette:


#### Marco:


#### Timon:


#### Sushant:


## Progress: Wednesday 20 January, 2021

#### Adjaye:


#### Francesco:


#### Jonas:


#### Juliette:


#### Marco:


#### Timon:


#### Sushant:


## Progress: Thursday 21 January, 2021

#### Adjaye:


#### Francesco:


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
