#Flask is a micro web framework written in Python
#basically builds a link from Python to a Web site "front end" (web page)

from flask import Flask, render_template, request, redirect, g, url_for
import csv

# ===================== FIX CHANGE 1 of 4 (NEW LINE) =====================
# 'os' is a built-in Python module for working with folders and file paths.
# We need it below to work out WHERE this .py file lives on the computer.
import os
# ========================================================================

# ===================== FIX CHANGE 2 of 4 (NEW LINES) ====================
# matplotlib normally tries to open a pop-up WINDOW to show a graph.
# A web server has no screen to show windows on, so that can crash Flask
# (500 error) or freeze it.
# 'Agg' tells matplotlib: "don't open a window, just draw the graph into
# an image file". This line MUST come BEFORE 'import matplotlib.pyplot'.
import matplotlib
matplotlib.use('Agg')
# ========================================================================
import matplotlib.pyplot as plt

app = Flask(__name__)
#creates an instance of flask (ie runs it) ...the "__name__" is standard syntax

# ===================== FIX CHANGE 3 of 4 (THE MAIN FIX) =================
# THE PROBLEM:
#   BEFORE it said:   Spurs_Dataset = 'Spurs_Data.csv'
#   A bare file name like that is a RELATIVE path. Python looks for the file
#   in the folder you RAN the program FROM (the "current working directory"),
#   NOT the folder this .py file is saved in.
#   Running from the LCCS-Flask folder, Python looked for
#   LCCS-Flask\Spurs_Data.csv, which doesn't exist, so open() crashed with
#   FileNotFoundError. Flask turns any crash into "500 Internal Server Error".
#
# THE FIX:
#   __file__                    = the path of THIS .py file
#   os.path.abspath(__file__)   = turn it into a full path, e.g.
#                                 C:\...\Spurs Info System\Football Data.py
#   os.path.dirname(...)        = cut off the file name to keep only the folder:
#                                 C:\...\Spurs Info System
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# os.path.join() glues the folder and file name together with the correct
# slash for your operating system (\ on Windows, / on Mac/Linux).
# Now the CSVs are ALWAYS found, wherever you run the program from.
Spurs_Dataset = os.path.join(BASE_DIR, 'Spurs_Data.csv')            # was: 'Spurs_Data.csv'
football_survey = os.path.join(BASE_DIR, 'football_form_data.csv')  # was: 'football_form_data.csv'
# ========================================================================

@app.route('/')
#sends data to the index page (home page) 
def display_player_data():
    striker_data = []
    # Read CSV file
    with open(Spurs_Dataset , 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            striker_data.append(row)
    return render_template('index.html', Spurs_data_For_My_Web_Page =striker_data )
#line 27 passes a variable (containing the CSV data ) as Spurs_data_For_My_Web_Page to a web page called index.html

# function to WRITE (append=a) NEW survey data (via the HTML page) to the CSV
def write_survey_to_csv(new_survey_data):
    with open(football_survey, mode='a', newline='') as file:
        #appaends (a) the new data to the file
        writer = csv.writer(file)
        writer.writerow(new_survey_data)


@app.route('/take_survey')
# 
def display_survey_data():
    survey_results_data = []
    # Read CSV file
    with open(football_survey, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            survey_results_data.append(row)
#sends data to the form.htl (survey page)   
    return render_template('form.html', For_HTML_survey_results_data=survey_results_data)
#  
@app.route('/take_survey', methods=['GET', 'POST'])
def add_survey_Data():
    if request.method == 'POST':
  # Get form data from the HTML file - what the customer has typed into the HTML page in the FORM.html page
  #notice the "GREEN" these are the names of the IDs on the form.html page (lines 27-45)
  #if these are NOT correct it will not work
         watch_football_matches= request.form['watch_football_matches']
         last_at_football_match = request.form['last_at_football_match']
         how_often = request.form['how_often']
         how_much_spent = request.form['price']
         fav_player = request.form['favorite_player']
         # Write the form data that the customer enters to the CSV - parses the variables that has started the data the customer typed into the form
         write_survey_to_csv([watch_football_matches, last_at_football_match, how_often, how_much_spent, fav_player ])
#         # Redirect to the same page to display the updated data
         return redirect(url_for('display_survey_data'))
#         # Read the data from CSV to display
    #survey_results = display_survey_data()
    return render_template('form.html') #show_survey=survey_results


@app.route("/displayGraphs")    
def create_lists_split_players():

#opens the CSV file ready to read in the data
    filename = open(Spurs_Dataset, 'r')
    file = csv.DictReader(filename)
    # creating empty lists for the data coming in (from the CSV)
    Goals = []
    Games = []
    Player_name = []
    for col in file:
    # iterating over each row and COLUMN name (of CSV)
    #and append (adds) values to empty lists above
        Games.append(col['Apps'])
        Goals.append(col['Goals'])
        Player_name.append(col['Player'])
        
    Games = [int(value) for value in Games]
    Goals= [int(value) for value in Goals]
#converts the values to an int (from a string) in case we need it for some stats/maths later !     

    Kane_Goals = []
    Kane_Games = []
    #create a couple of empty lists [] to store data in 
    for Current_Player in range(len(Player_name)):
        #starts a loop, do the following for the length (len) of the Player_name list - ALL players have a name so it will do this
        #check for EVERY player in my dataset
            
            if Player_name[Current_Player] == 'Kane':
                              #IF the player of the CURRENT player in the list is equal to (==) Kane then do the following
                Kane_Goals.append (Goals[Current_Player])
                Kane_Games.append (Games[Current_Player])
                #Add (append) to the new lists (lines 100, 101 the Goals AND the Games kane has played for hat season
                Current_Player=+1
                #Move to the next player
                
            else:                                   
                Current_Player=+1
        #ELSE (if is DOESN'T = Kane just move to the next player
        
    Total_Kane_Goals = sum(Kane_Goals)
    Total_Kane_Games  = sum(Kane_Games)
    #add up the topals of both of these lists
    
    #Get Kane's averages goals PER season - basically for each season, the goals scored / games played
    Kane_Career_Avg  = round(Total_Kane_Goals/Total_Kane_Games,2)
    
    
    global Kane_yearly_averages
    Kane_yearly_averages = []
   
    
    #creates a NEW blank list []
    for Current_season in range(len(Kane_Goals )):
            #then steps through the Kane Goals list 
                 Kane_yearly_averages.append(round(Kane_Goals[Current_season]/Kane_Games[Current_season],2))                  
                   #and at EACH position divides (/) the Goals/ Games to get an Average for that season
    #data to be PArsed to the display_graph page from this function
    #You can see this data being "called" on the display_graphs.html Lines 21-38 
    
    ############PRODUCE LINE GRAPH ###################
    Kane_Data = Kane_yearly_averages
    #The data we will use is the Kane yearly averages list (line 131)
    Labels = ['2013', '2014' , '2015' ,'2016', '2017','2018','2019','2020', '2021', '2022','2023']
    #The labels are just text - i have here the 10 different seasons that Kane was at Spurs
    plt.plot(Labels, Kane_Data)
    #Plot order 
    plt.xlabel("Year")  # add X-axis label
    plt.ylabel("Avg Goals Per Game")  # add Y-axis label
    plt.title("Kane: Average Goals per Game per Season at Spurs")  # add title
    # ===================== FIX CHANGE 4 of 4 =============================
    # Same problem as change 3: 'static/total_kane_averages.png' is a relative
    # path, so the image could be saved into the WRONG static folder (or fail).
    # BEFORE: plt.savefig(f'static/total_kane_averages.png')
    # NOW:    build the full path from BASE_DIR -> static -> image name
    plt.savefig(os.path.join(BASE_DIR, 'static', 'total_kane_averages.png'))
    # ======================================================================
    plt.close()
    return render_template("display_graph.html", 
                           HTML_Total_Kane_Goals = Total_Kane_Goals,
                            HTML_Total_Kane_Games  = Total_Kane_Games,
                            HTML_Kane_Career_Avg = Kane_Career_Avg,
                           HTML_Kane_yearly_averages = Kane_yearly_averages )

# @app.route("/displayGraphs")
def display_graphs():
# #  this then RE creates the graphs at "real time" everytime the Display Graphs link is cllicked
#You may not NEED this BUT if new data was being added to a CSV (say like the survey/form) and you DID want this new data included in the graph 
            create_lists_split_players()
            return render_template("display_graph.html")
#     

if __name__=="__main__":
    app.run(host ="0.0.0.0", port=8080)    

    
