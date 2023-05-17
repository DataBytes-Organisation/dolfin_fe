from classes.api import API
from dash.dependencies import Input, Output, State
from app import app
import pandas as pd
import plotly.express as px
import json

@app.callback(
    Output('yearly_spending_graph', 'figure'),
    Input('yearly_spending_dd', 'value')
)
def update_graph(year):
    dfIncoming, dfOutgoing = get_incoming_outgoing_transactions()
    dff = dfOutgoing[dfOutgoing.iloc[:,0]==year]
    figln = px.line(dff, x='month', y='amount')
    return figln

@app.callback(
    Output('yearly_saving_graph', 'figure'),
    Input('yearly_saving_dd', 'value')
)
def update_graph(year):
    dfIncoming, dfOutgoing = get_incoming_outgoing_transactions()
    dff = dfIncoming[dfIncoming.iloc[:,0]==year]
    figln = px.line(dff, x='month', y='amount')
    return figln

def get_transaction_data():
    api = API()
    transaction_result = api.basiq_api_transaction_data()
    data = transaction_result["data"]

    accounts = get_accounts()

    df = pd.json_normalize(data)
    accounts_df = pd.json_normalize(accounts)

    processedData = df.filter(["id", "status", "amount", "direction", "account", "class", "postDate", "subClass.title"], axis=1)
    monthsForProcessing = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"]

    #Renamed 'subClass.title' as 'category'. This is not the category I was looking to use but it could do the job
    processedData.rename(columns = {'subClass.title':'category'}, inplace = True)

    #Processing the date value that is returned. It will be split from a string in to 3 arrays listed below
    year = []
    month = []
    day = []

    #Account name included to give something human readable to the account id number
    accountName = []
    #Here I am transforming the data in the postDate and account columns. 
    for column in df[["postDate", "account"]]:
        for val in df[column]:
            if column == "postDate":
                
                #postDate has the initial string value split, giving us a date formatted to yyy-mm-dd at the 0th index. This is then
                #split at the '-' into separate years, months and dates and added in to the appropriate array above 
                
                initialSplit = val.split('T')
                yearMonthDay = initialSplit[0].split("-")
                year.append(yearMonthDay[0])
                month.append(monthsForProcessing[int(yearMonthDay[1]) - 1])
                day.append(yearMonthDay[2])
            if column == "account":
                
                #If the account id matches the account id in the 'Accounts' dataframe (created 2 cells above) then the account name
                #is added to the accountName array, to be added in to the dataframe 
                for index, accountNumber in enumerate(accounts_df["id"]):
                    if val == accountNumber:
                        accountName.append(accounts_df["name"][index])
                        break

    #All of the new values are added to the existing dataframe
    processedData["year"] = year
    processedData["month"] = month
    processedData["day"] = day
    # processedData["accountName"] = accountName
    processedData = processedData.drop('postDate', axis=1)
    processedData["category"].fillna("Unknown", inplace = True)

    return processedData

def get_accounts():
    api = API()
    account_details = api.get_accounts_for_user()
    data = account_details["data"]

    return data

def get_incoming_outgoing_transactions():
    processedData = get_transaction_data()

    outgoingTransactions = processedData[processedData.amount.astype('float64') < 0]

    #transforming values to absolute value to prevent the issue mentioned above
    for index, row in outgoingTransactions.iterrows():
        row["amount"] = abs(float(row["amount"]))
        
    incomingTransactions = processedData[processedData.amount.astype('float64') > 0]

    for index, row in incomingTransactions.iterrows():
        row["amount"] = abs(float(row["amount"]))

    monthlySpending = outgoingTransactions.groupby(['year', 'month']).sum().reset_index().filter(['year', 'month', 'amount'], axis=1)
    monthlySaving = incomingTransactions.groupby(['year', 'month']).sum().reset_index().filter(['year', 'month', 'amount'], axis=1)

    ordered_months = ["Jan", "Feb", "Mar", "Apr", "May", "June",
      "July", "Aug", "Sep", "Oct", "Nov", "Dec"]
    
    #Both incoming models are sorted by month
    monthlySaving['to_sort']=monthlySaving['month'].apply(lambda x:ordered_months.index(x))
    monthlySaving = monthlySaving.sort_values('to_sort')

    monthlySpending['to_sort']=monthlySpending['month'].apply(lambda x:ordered_months.index(x))
    monthlySpending = monthlySpending.sort_values('to_sort')

    return monthlySaving, monthlySpending
