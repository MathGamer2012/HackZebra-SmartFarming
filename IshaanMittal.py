
def plot_a():
    global plotA
    #ask for efficiencies for plotA
    plotA = list(map(int, input("Enter the efficiencies of plot A (4 values), must be less than 100 and more than 0(using spaces to indicate next number): ").split()))
    
def plot_b():
    global plotB
    #ask for efficiencies for plotB
    plotB = list(map(int, input("Enter the efficiencies of plot B (4 values), must be less than 100 and more than 0(using spaces to indicate next number): ").split()))

def plot_c():
    global plotC
    #ask for efficiencies for plotC
    plotC = list(map(int, input("Enter the efficiencies of plot C (4 values), must be less than 100 and more than 0(using spaces to indicate next number): ").split()))

def plot_d():
    global plotD
    #ask for efficiencies for plotD
    plotD = list(map(int, input("Enter the efficiencies of plot D (4 values), must be less than 100 and more than 0 (using spaces to indicate next number): ").split()))

def year():
    global year_total
    #ask for the #of years for production 
    year_total = int(input("Enter the amount of years for production: ")) 

#creats a text file to store the crop counts, once program calculates  
myFile = open("crop_counts.txt", "w")

#stores the values of each crop
car_stock = 110 * 100 
pot_stock = 40 * 100 
bean_stock = 90 * 100 
cab_stock = 10 * 100 

#variable to keep track of harvestable crops after each crop rotation 
carrots = 0
potatoes = 0
beans = 0
cabbage = 0

#index for each crop in the plots 
car_index = 0
pot_index = 1
bean_index = 2
cab_index = 3 

#stores the plot values divided by 100, to turn into decimal format 
plotA_div = []
plotB_div = []
plotC_div = []
plotD_div = []

#to keep track of which year we are on 
year_count = 0

#keeps track of crop rotation rounds 
crop_rotation = 0 

#to keep track of which plot each crop is currently in 
currentPlot_Car = plotA_div
currentPlot_Pot = plotB_div
currentPlot_Bean = plotC_div
currentPlot_Cab = plotD_div

#list for the values being writen on the .txt file
year_list = []
car_list = []
pot_list = []
bean_list = []
cab_list = [] 

#informs the user for the index of each crop 
print("These are the indices of the crops: (Carrots, Potatoes, Beans, Cabbage)")
    
#function asks for plot a inputs
plot_a()

#checks if the index of the list is greater than the given amount, for each plot 
if len(plotA) > 4:
    print("Too many values, Try again (remember to use spaces to indicate next number)")
    plot_a()

#checks if the index of the list is less than the given amount, for each plot 
if len(plotA) < 4:
    print("Not enough values, Try again (remember to use spaces to indicate next number)")
    plot_a()

#checks if any value in the list in greater than/equal to 100 or less than/equal to 0 
for i in range(len(plotA)):
    if plotA[i] >= 100 or plotA[i] <= 0:
        print("Try Again")
        plot_a()

#function asks for plot b inputs
plot_b()

#same comments as the others 
if len(plotB) > 4:
    print("Too many values, Try again (remember to use spaces to indicate next number)")
    plot_b()

if len(plotB) < 4:
    print("Not enough values, Try again (remember to use spaces to indicate next number)")
    plot_b()

for i in range(len(plotB)):
    if plotB[i] >= 100 or plotB[i] <= 0:
        print("Try Again")
        plot_b()

#function asks for plot c inputs 
plot_c()

#same comments as the others 
if len(plotC) > 4:
    print("Too many values, Try again (remember to use spaces to indicate next number)")
    plot_c()

if len(plotC) < 4:
    print("Not enough values, Try again (remember to use spaces to indicate next number)")
    plot_c()

for i in range(len(plotC)):
    if plotC[i] >= 100 or plotC[i] <= 0:
        print("Try Again")
        plot_c()

#function asks for plot d inputs
plot_d()

#same comments as the others 
if len(plotD) > 4:
    print("Too many values, Try again (remember to use spaces to indicate next number)")
    plot_d()

if len(plotD) < 4:
    print("Not enough values, Try again (remember to use spaces to indicate next number)")
    plot_d()

for i in range(len(plotD)):
    if plotD[i] >= 100 or plotD[i] <= 0:
        print("Try Again")
        plot_d()

#function asks for #of years input 
year()        

#divides all the values in the plot efficiencies by 100, to convert into decimal 
for i in plotA:
    plotA_div.append(i / 100)

for i in plotB:
    plotB_div.append(i / 100)

for i in plotC:
    plotC_div.append(i / 100)

for i in plotD:
    plotD_div.append(i / 100)

#repeats tracking of harvestable crops until year_count doesn't equal year_total (user input)
while(year_count != year_total):
    #adds 1 everytime all the values have been multiplied, representing the years 
    year_count += 1
    
    #writes the current year to the .txt file
    year_list = ['\n', 'Year ', str(year_count), '\n']
    myFile.writelines(year_list)
    
    #keeps track of all the harvestable crops per year
    carrots = currentPlot_Car[car_index] * car_stock

    #writes the # of harvestable carrots to the .txt file
    car_list = ['\n', 'Carrots: ', str(carrots), '\n']
    myFile.writelines(car_list)

    potatoes = currentPlot_Pot[pot_index] * pot_stock
    #writes the # of harvestable potatoes to the .txt file
    pot_list = ['Potatoes: ', str(potatoes), '\n'] 
    myFile.writelines(pot_list)

    beans = currentPlot_Bean[bean_index] * bean_stock
    #writes the # of harvestable beans to the .txt file
    bean_list = ['Beans: ', str(beans), '\n']
    myFile.writelines(bean_list)

    cabbage = currentPlot_Cab[cab_index] * cab_stock 
    #writes the # of harvestable cabbages to the .txt file
    cab_list = ['Cabbage: ', str(cabbage), '\n'] 
    myFile.writelines(cab_list)

    
    #adds 1 verytime all the values have been multiplied, representing crop rotation
    crop_rotation += 1 

    #based on year, starts the crop rotation 
    if crop_rotation == 1:
        currentPlot_Car = plotD_div
        currentPlot_Pot = plotA_div
        currentPlot_Bean = plotB_div
        currentPlot_Cab = plotC_div

    if crop_rotation == 2:
        currentPlot_Car = plotC_div
        currentPlot_Pot = plotD_div
        currentPlot_Bean = plotA_div
        currentPlot_Cab = plotB_div

    if crop_rotation == 3:
        currentPlot_Car = plotB_div
        currentPlot_Pot = plotC_div
        currentPlot_Bean = plotD_div
        currentPlot_Cab = plotA_div

    if crop_rotation == 4:
        #resets, as 1 round of crop rotation has finished (since there are only 4 plots)
        currentPlot_Car = plotA_div
        currentPlot_Pot = plotB_div
        currentPlot_Bean = plotC_div
        currentPlot_Cab = plotD_div
        crop_rotation = 0

myFile.close()
     


 
                                   
                                
            
            
                                
    



