Skills Demonstrated in This Project
??? Python GUI Development using Tkinter and ttk

?? Custom GUI Layouts with grid and pack managers

?? Real-time Terminal Output embedded in GUI via Text widget and sys.stdout redirection

?? Multithreading for concurrent MQTT event handling without blocking the GUI

?? MQTT Communication Protocol (paho-mqtt) for message-based agent control

?? Object-Oriented Design (OOP) with clear class responsibilities and modular architecture

??? Image Processing with PIL to dynamically update visuals (e.g. connection status)

?? Controller Delegation Pattern to avoid circular imports and enable centralized control

?? Event-Driven Programming for GUI interaction and agent response handling

?? Clean Code Structure using multiple organized files for GUI, logic, and agents

??? Debug Logging through an auto-updating in-GUI terminal

?? Scalable UI Design with resizable frames and proper widget configuration

?? Documentation and Code Comments for maintainability and clarity


Todo - 
$ Create connect button that connects the bot (slider?)

Notes =====

2025/06/25
-----------
start in gif frame -> use gif function to to insert generic pic

main should call the window and then call grey scale in main not window.py

2025/06/28 
------------
Remember each class is its own fucntions and abilities, while coding window. App_design is the handler of the gif,msg,terminal frame classes
for example; in App_design, there is a function to toggle with gif's connection functions.

Message needs 
- an entry box with send box
- box to that toggles connection of handler/agents? (need to be clear on how you want it to be structured - needs to trigger toggle_con)
-send button triggers entry box
- coonects to controller (main) through class initalize and call

2025/06/30
-----------
Need to make the gif pic to update dynamically, right now line 60 in windows.py and line 40 in main.py needs attention to be able to 
call in main and update specific windows.py gif.

issue with text box since app_design class and class was in the same file
- had to manually pass controller to App_design(controller=self) so then message can see it because message was in the same class as 
    app_deisgn. since main was already calling app design, calling main from app design created a loop, crashed python.

2025/07/10
-----------
when ever we run, it is not publishign anything and broker log is not identifiying anything (code is somethng other then 0)
 -> treid threading the handler to loop 

 soltuion: 
  -----> info.rc error 4: App_design:(which had send button to call a funct in handler) was being called before anything
    handler was event initalized
  -----> Accidently initalized handler twice (note line 149 in windows.py for comment), had initalized handler directly
    in in app_design but that just skipped the handler from being connected which is required first

2025/07/11
-----------
add a terminal into app_design, made a text box and customized it to look like a terminal with black background and green text
Within terminal class --> made a simplified version on print() which has write and flush fucntions:
used sys to redirect all print() to the built-terminal as long as the declaration is called prior to print statment

Lets make it look a little btter, like a scrollbar or make the terminal print better