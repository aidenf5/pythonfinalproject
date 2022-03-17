import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import sys
def voteComparison(interestedState):
    """
    Takes in the parameter of whatever state the user is interested in getting data for,
    outputs the given republican and democrat candidates and who won in the state.

    Used in calling the functions flipCounter() and votedCorrectly().

    """
    year = 2000
    data = pd.read_csv("1976-2016-president.csv", index_col="state")
    #interestedState = input("What state are you interested in data from?")
    x = data.loc[interestedState]
    sumRepub = 0
    sumDem = 0
    sumTotal = 0
    repubCandidates = []
    demCandidates = []
    winningCandidate = []
    y = x["candidatevotes"]
    y2 = x["party"]
    y3 = x["year"]
    y4 = x["totalvotes"]
    y5 = x["candidate"]
    for i in range(len(x)):
        if (y3[i]) >= year:
            if (y2[i]) == "republican":
                sumRepub += y[i]
                sumTotal += y4[i]
                repubCandidates.append(y5[i])
            elif (y2[i]) == "democrat":
                sumDem += y[i]
                demCandidates.append(y5[i])
        if(sumDem>sumRepub and sumRepub!=0 and sumDem!=0):
            winningCandidate.append("Democrat")
            sumRepub = 0
            sumDem = 0
        elif(sumRepub>sumDem and sumRepub!=0 and sumDem!=0):
            winningCandidate.append("Republican")
            sumDem = 0
            sumRepub = 0
    demPercent = sumDem/sumTotal*100
    repubPercent = sumRepub/sumTotal*100
    return repubCandidates,demCandidates,winningCandidate


def voteComparison2(interestedState,year):
    """
    The same function as voteComparison(interestedState), but uses user input to find the
    state in which the user is interested in data from, as well as the year.

    Used in the topfiveStates2() function to get data from all 50 states, returns the given percentage
    of votes for the selected state that are democratic and republican.

    """
    #year = 2012
    data = pd.read_csv("1976-2016-president.csv", index_col="state")
    data["year"] = pd.to_datetime(data["year"], format="%Y")
    #interestedState = input("What state are you interested in data from?")
    x = data.loc[interestedState]
    sumRepub = 0
    sumDem = 0
    sumTotal = 0
    y = x["candidatevotes"]
    y2 = x["party"]
    y3 = x["year"]
    y4 = x["totalvotes"]
    for i in range(len(x)):
        if (y3[i]) == pd.to_datetime("%s-01-01" % year):
            if (y2[i]) == "republican":
                sumRepub += y[i]
                sumTotal += y4[i]
            elif (y2[i]) == "democrat":
                sumDem += y[i]
    demPercent = sumDem/sumTotal*100
    repubPercent = sumRepub/sumTotal*100
    #print(sumRepub)
    #print(sumDem)
    #print(sumTotal)
    #print(interestedState,"Total Republican Votes from 2000-2016:", sumRepub, "Total Democrat Votes from 2000-2016:", sumDem,
          #"Republican Vote Percentage of Total:", round(repubPercent),
          #"Democrat Vote Percentage of Total:",
          #round(demPercent))
    return round(demPercent),round(repubPercent)

def topfiveStates2():
    """
    Uses the voteComparison2() function to get data on all 50 states, returns the top 5 states with the
    highest voting percentages in either 2012 or 2016, based on user input.

    Used in the visualization of this data in function top5table().

    """
    states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","District of Columbia","Florida",
              "Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
              "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire",
              "New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
              "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington",
              "West Virginia","Wisconsin","Wyoming"]
    statesPercents = []
    year = int(input("Question 3 requires data from 2012 or 2016, which one would you like to find data for?"))
    for i in range(51):
        statesPercents.append(voteComparison2(states[i],year))
    #print(statesPercents)
    zipped = zip(states,statesPercents)
    zippedFinal = list(zipped)
    #print(zippedFinal)
    demPercents = []
    repubPercents = []
    for i in range(51):
        demPercents.append(zippedFinal[i][1][0])
    for i in range(51):
        repubPercents.append(zippedFinal[i][1][1])
    #print(repubPercents)
    #print(demPercents)
    repubPercents = list(zip(states,repubPercents))
    demPercents = list(zip(states,demPercents))
    #print(repubPercents)
    #print(demPercents)
    finalrepubPercents = sorted(repubPercents,key=lambda x: x[1],reverse=True)
    finaldemPercents = sorted(demPercents,key=lambda x: x[1],reverse=True)
    #print("Republican Percents :",finalrepubPercents)
    #print("Democrat Percents :",finaldemPercents)
    finalrepubPercents5 = []
    finaldemPercents5 = []
    for i in range(5):
        finalrepubPercents5.append(finalrepubPercents[i])
        finaldemPercents5.append(finaldemPercents[i])
    #print("Republican Top 5:",finalrepubPercents5)
    #print("Democrat Top 5:",finaldemPercents5)
    #return "Republican Top 5:"+finalrepubPercents5+". Democrat Top 5:"+finaldemPercents5+"."
    return finalrepubPercents5,finaldemPercents5
    #THIS CAN BE CLEANED UP TO LOOK BETTER, CURRENTLY PRINTED AS TUPLE

def voteComparison3(interestedState):
    """
    Same function as voteComparison(), but returns only the total votes for each state, which is then
    calculated in a summation to return the total votes in the presidential elections from 2000-2016.

    Returns vote count for any given state from 2000-2016.

    """
    year = 2000
    data = pd.read_csv("1976-2016-president.csv", index_col="state")
    #interestedState = input("What state are you interested in data from?")
    x = data.loc[interestedState]
    sumRepub = 0
    sumDem = 0
    sumTotal = 0
    y = x["candidatevotes"]
    y2 = x["party"]
    y3 = x["year"]
    y4 = x["totalvotes"]
    for i in range(len(x)):
        if (y3[i]) >= year:
            if (y2[i]) == "republican":
                sumRepub += y[i]
                sumTotal += y4[i]
            elif (y2[i]) == "democrat":
                sumDem += y[i]
    demPercent = sumDem/sumTotal*100
    repubPercent = sumRepub/sumTotal*100
    #print(sumRepub)
    #print(sumDem)
    #print(sumTotal)
    #print(interestedState,"Total Republican Votes from 2000-2016:", sumRepub, "Total Democrat Votes from 2000-2016:", sumDem,
          #"Republican Vote Percentage of Total:", round(repubPercent),
          #"Democrat Vote Percentage of Total:",
          #round(demPercent))
    return sumTotal

def findtotalVotes():
    """
    Uses voteComparison3() to calculate the total votes in the presidential election from 2000-2016.

    Returns total vote count in presidential elections from 2000-2016.

    """
    states = ["Alabama","Alaska","Arkansas","California","Colorado","Connecticut","Delaware","District of Columbia","Florida",
              "Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
              "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire",
              "New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
              "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington",
              "West Virginia","Wisconsin","Wyoming"]
    totalvotesList = []
    for i in range(50):
        totalvotesList.append(voteComparison3(states[i]))
    sum = 0
    for item in totalvotesList:
        sum += item
    return "The total votes for the presidential election from 2000-2016 were: %r" % (sum)

def voteComparison4(interestedState):
    """
    Same as voteComparison(), but takes in an interested state and returns the Total Republican and Democratic
    Votes with percentages for any selected state.

    Returns a string statement including the data requested for in Question 1.

    """
    interestedState = input("What state would you like to find the data in for Question 2?")
    year = 2000
    data = pd.read_csv("1976-2016-president.csv", index_col="state")
    #interestedState = input("What state are you interested in data from?")
    x = data.loc[interestedState]
    sumRepub = 0
    sumDem = 0
    sumTotal = 0
    y = x["candidatevotes"]
    y2 = x["party"]
    y3 = x["year"]
    y4 = x["totalvotes"]
    for i in range(len(x)):
        if (y3[i]) >= year:
            if (y2[i]) == "republican":
                sumRepub += y[i]
                sumTotal += y4[i]
            elif (y2[i]) == "democrat":
                sumDem += y[i]
    demPercent = sumDem/sumTotal*100
    repubPercent = sumRepub/sumTotal*100
    #print(sumRepub)
    #print(sumDem)
    #print(sumTotal)
    return "%rs Total Republican Votes from 2000-2016: %r. Total Democrat Votes from 2000-2016: %r. Republican Vote Percentage of Total: %r. Democrat Vote Percentage of Total: %r." % (interestedState,sumRepub,sumDem,round(repubPercent),round(demPercent))


def voteComparison5(interestedState):
    """
    Same as voteComparison(), but returns only the democratic voting percentages and the republican
    voting percentages for any selected state. Used in graphingData(), needs to be different from the
    other functions based on the exact year.

    Returns republican and democrat percentages from 1976-2016.

    """
    year = 1976
    data = pd.read_csv("1976-2016-president.csv", index_col="state")
    #interestedState = input("What state are you interested in data from?")
    x = data.loc[interestedState]
    sumRepub = 0
    sumDem = 0
    sumTotal = 0
    y = x["candidatevotes"]
    y2 = x["party"]
    y3 = x["year"]
    y4 = x["totalvotes"]
    for i in range(len(x)):
        if (y3[i]) >= year:
            if (y2[i]) == "republican":
                sumRepub += y[i]
                sumTotal += y4[i]
            elif (y2[i]) == "democrat":
                sumDem += y[i]
    demPercent = sumDem/sumTotal*100
    repubPercent = sumRepub/sumTotal*100
    #print(sumRepub)
    #print(sumDem)
    #print(sumTotal)
    #print(interestedState,"Total Republican Votes from 2000-2016:", sumRepub, "Total Democrat Votes from 2000-2016:", sumDem,
          #"Republican Vote Percentage of Total:", round(repubPercent),
          #"Democrat Vote Percentage of Total:",
          #round(demPercent))
    return round(demPercent),round(repubPercent)

def graphingData(interestedState):
    """
    Takes in any selected state and returns 3 graphs (bar, line and pie) with voting statistics from
    2000-2016.

    Returns 3 graphs of types specified above.

    """
    data = pd.read_csv("1976-2016-president.csv", index_col="state")
    interestedState = input("What state would you like to visualize statistics for?")
    #data["year"] = pd.to_datetime(data["year"], format="%Y")
    x = data.loc[interestedState]
    repubVotes = []
    demVotes = []
    y = x["candidatevotes"]
    y2 = x["party"]
    y3 = x["year"]
    y4 = x["totalvotes"]
    for i in range(len(x)):
        if y2[i]=="republican":
            repubVotes.append(y[i])
        elif y2[i]=="democrat":
            demVotes.append(y[i])
    years = [1976,1980,1984,1988,1992,1996,2000,2004,2008,2012,2016]
    #print(repubVotes,demVotes)
    #Bar Graph
    N = np.arange(11)
    width = .35
    fig,ax = plt.subplots()
    rects1 = ax.bar(N - width / 2, repubVotes, width, label='Republican Votes')
    rects2 = ax.bar(N + width / 2, demVotes, width, label='Democrat Votes')
    ax.set_ylabel("Total Votes")
    ax.set_title("Republican and Democrat Votes from 1976-2016 for %s"%interestedState)
    ax.set_xticks(N)
    ax.set_xticklabels(years)
    ax.legend()
    fig.tight_layout()
    plt.show()
    #Line Graph
    df = pd.DataFrame({'xx': years, 'Democrat': demVotes, 'Republican': repubVotes})
    plt.plot('xx', 'Democrat', data=df, marker='', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4)
    plt.plot('xx', 'Republican', data=df, marker='', color='red', linewidth=2)
    plt.title("Republican and Democrat Votes from 1976-2016 for %s"%interestedState)
    plt.legend()
    plt.show()
    #Pie Chart
    labels = ["Democrat","Republican","Other"]
    percents = voteComparison5(interestedState)
    sizes = [percents[0],percents[1],100-(percents[0]+percents[1])]
    fig1,ax1 = plt.subplots()
    if(percents[0]>percents[1]):
        explode = (.1,0,0)
    else:
        explode = (0,.1,0)
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    plt.title("Republican and Democrat Votes from 1976-2016 for %s"%interestedState)
    plt.show()

def flipCounter(interestedState):
    """
    Takes in any selected state and returns however many times it flipped, which can be defined as
    if a state was one party in one election cycle, then voted majority in favor of another party
    the next cycle.

    """
    interestedState = input("What state would you like to choose to find out how many times they flipped parties they voted for?")
    data = voteComparison(interestedState)
    interestedstateVotes = data[2]
    flips = 0
    for i in range(5):
        if(i==0):
            currentParty = interestedstateVotes[i]
        else:
            if(interestedstateVotes[i]!=currentParty):
                currentParty = interestedstateVotes[i]
                flips += 1
    return "The state of %r flipped %r times." % (interestedState,flips)


def votedCorrectly(interestedState):
    """
    Returns the amount of times a state voted for the person that got elected

    """
    interestedState = input("What state would you like to choose to find out how many times they voted for the person that got elected?")
    data = voteComparison(interestedState)
    interestedstateVotes = data[2]
    key = []
    key.append("Republican")
    key.append("Republican")
    key.append("Democrat")
    key.append("Democrat")
    key.append("Republican")
    correctCount = 0
    for i in range(5):
        if interestedstateVotes[i]==key[i]:
            correctCount += 1
    return "The state of %r voted for the president that got elected %r times between 2000-2016." % (interestedState,correctCount)

def USMap():
    """
    Returns a Choropleth graph of the United States in any input year election cycle with red and blue
    representing whether a Republican or a Democrat won the state.

    """
    states = ["Alabama", "Alaska","Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida",
              "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine",
              "Maryland",
              "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada",
              "New Hampshire",
              "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
              "Pennsylvania",
              "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia",
              "Washington",
              "West Virginia", "Wisconsin", "Wyoming"]
    abvStates = ["AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA",
                 "ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR"
                 ,"PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]
    year = int(input("What year would you like to produce a map for?"))
    redorBlue = []
    repubC = 0
    demC = 0
    for i in range(50):
        data = voteComparison2(states[i],year)
        if(data[0]>data[1]):
            redorBlue.append(0)
            #demC += 1
        else:
            redorBlue.append(1)
            #repubC += 1
    #print(redorBlue)
    #print(demC,repubC)
    #run a voteComparison without DC, doesnt exist on geo maps thing
    fig = px.choropleth(locations=abvStates, locationmode="USA-states", color=redorBlue, scope="usa")
    fig.update_layout(title_text="United States Presidential Election Map in %r" %(year),coloraxis_colorscale=[(0,"blue"), (1,"red")],coloraxis_showscale=False)
    fig.show()
def top5table():
    """
    A visualization of the answer to Question 3, which was the top 5 states that voted either Republican or
    Democratic in any given election cycle.

    Returns a dataframe table with the top 5 states data.

    """
    topdemstates_df = []
    topdempercentages_df = []
    toprepubstates_df = []
    toprepubpercentages_df = []
    data = topfiveStates2()
    for i in range(5):
        topdemstates_df.append(data[1][i][0])
    for i in range (5):
        topdempercentages_df.append(data[1][i][1])
    for i in range(5):
        toprepubstates_df.append(data[0][i][0])
    for i in range(5):
        toprepubpercentages_df.append(data[0][i][1])
    top5dem_df = {'Top Democratic States':topdemstates_df,'Percentage of Votes':topdempercentages_df}
    top5repub_df = {'Top Republican States':toprepubstates_df,'Percentage of Votes':toprepubpercentages_df}
    df = pd.DataFrame(top5dem_df, index=[1,2,3,4,5])
    df2 = pd.DataFrame(top5repub_df, index=[1,2,3,4,5])
    print(df)
    print(df2)
def main():
    if len(sys.argv) != 2:
        print('usage: ./datasetAnalysis.py {--totalVotes | --stateComparison | --top5States |'
              '--statedataVisualization | --electionMap | --votedCorrectly | --flipCounter}')
        sys.exit(1)
    option = sys.argv[1]
    if option == '--totalVotes':
        print(findtotalVotes())
    elif option == '--stateComparison':
        print(voteComparison4("State"))
    elif option == '--top5States':
        top5table()
    elif option == '--statedataVisualization':
        graphingData("State")
    elif option == '--electionMap':
        USMap()
    elif option == '--votedCorrectly':
        print(votedCorrectly("State"))
    elif option == '--flipCounter':
        print(flipCounter("State"))
    else:
        print('unknown option: ' + option)
        sys.exit(1)
if __name__ == "__main__":
    main()