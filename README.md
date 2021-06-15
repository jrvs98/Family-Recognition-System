# Family-Recognition-System

![Picture1](https://user-images.githubusercontent.com/58365714/122114386-a403bc80-ce3c-11eb-8a99-ba0803924aed.jpg)


For Backend purpose, after going through several documentations and reports we decided to work on Local Binary Pattern Histogram(LBPH) as it’s the modified version of Local Binary Pattern (LBP) as in LBP we only use distance vectors to recognize the pattern of image as major flaw in LBP was it will not give efficient answers to color picture through the technique og using distance vector is great. So in order to preserve that technique yet making this algorithm benificery programmers decided to alter the Algorithm in such way so it can give correct answer. They use technique of (HOG) to change the LBP to LBPH in such way image was first transformed in grayscale image and then Algorithm Trains the data moreover it change the Pixel size which help us a lot in using distance vector in more efficient way that’s the reason we can provide you confidence level upto 80% in our code.
	Lets talk about implementation through Code. In our project Code of Backend was changed in 3 phases. In First Phase We only Take sample pictures of person using library Python-OpenCv. As it help us a lot in turning vedio of a face into frames on run time following is the code snippet for this purpose. 
 
For Face detection we can use the following code as it extract information regarding facr through haarcascade-frontalface-default.xml file. As we only need to train data on basis of image in each frame.For that purpose followinf Code snippet is used.
 

Now Comes the Second Phase of Code in which we will train our data and assign label to each picture so in future on testing the label that matches most will be selected.For that purpose we first change the image in gray scale and then use the built-in functionality in Python-OpenCv to use LBPH. As it the purpose of selecting LBPH is that it’s easy to use (as built in function) and secondly have high number of confidence level. Following is code snippet of Training the data.
 

Now comes the Last part of Backend procedure in which we will use the test our data and on basis of certain confidence level we will give the answer. Following is the Code-snippet for testing the data on basis of labels we get through tarining data.
 

Secondly comes the Frontend where we use Library Tkinter as it’s the GUI toolkit which can provide efficient work with minimum effort. As following is the code-snippet for our GUI. According to this snippet the color and labels of GUI can be easily represented. Moreover Tkinter is easy to use as all we need to assign the label to the message and provide x axis and y axis which can help us placing that specific button or meesage on screen on thoses axis. A sample of such working is attach below:
	 

Functionalities:
1-	Add Member:
In this function we can add a new member to the family as webcam opens and take frames of the user which want to be enroll. Moreover, later ths data will be train automatically.



2-Browse an image:
In this function if we want to know a person is part of family or not we can simply add his/her photo later our program will tell either the picture we browse is part of family or not.
3-	WebCam detection:
In this function person have to show his face in real time and program will tell us that the person currently viewing is a member or not.
4-	Search Folder:
In this function one will help us to search the user folder by just simply entering his/her name. As we can see the image of the person that we want to see by simply searching his/her name.




Results:
	Our project provide us 3 types of results as you can see below:
	1-No Face Detection:
		In this Case no when no face is visible to camera we can see the Alert message as shown in image.
		 

	
2- Face Not match:
		If the person data is not stored in database it will give answer of Not a Family member as following. As I am using a beard person because its common in many face recognizer that they accept the info if any one have same face looking features.
 

3- Face Matched:
	In this case person data matches the info of the person stored in data base. In this case it will give answer of Family Member.
 
Conclusion:
	In this Project we usually looking to learn the technique of Face detection and the Face Recognization. Which we done in quite a great way. As we use libraries like Python-OpenCv and Python-contrib-OpenCv which helps in face detection and face recognization for GUI we used Tkinter. So in short at end of this project we are familiar with a lot of Machine Learning Aspects and being a semester project it help us a lot in digging a lot of things regarding ML. And how in history a lot of work is done in specific field of Face Recognization. Moreover, in future we can look after in modifing the current Algorithms so it can five us accuracy of more than 95%+. 
