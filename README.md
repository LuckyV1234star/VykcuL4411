Automated Trash Separation, Data Collection and Analysis System   

This system is built based on Python 3.12.0 and the following modules are used:
- tkinter
- threading
- time 
- cv2 
- os  
- google.generativeai

*pre-requirement: 
1- since this program used Gemini as the Demo AI detector, user will require to use VPN to connect to location that support the use of Gemini
2- camara is needed 

Description:
When this program started, it will open the camara of the user PC. It will keep opening and the user may click on the button "recognize" to take a photo for computer to recognize what item type is that and move that photo to the destinated file. If the button "Count and End" was clicked, the program will kill the window and output the total number of document that each file contain.
