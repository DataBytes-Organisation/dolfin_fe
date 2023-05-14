from classes.api import API
from dash.dependencies import Input, Output, State
from app import app
import pandas as pd
import plotly.express as px


#Importing calculated savings and spending models. Required data will be summed Amount spent grouped by Year and Month
dfIncoming = pd.read_csv('pages/breakdown/monthly_saving_user.csv')
dfOutgoing = pd.read_csv('pages/breakdown/monthly_spending_user.csv')

#This can probably be done elsewhere as static data. Included to sort values by month and display properly on the graph
ordered_months = ["Jan", "Feb", "Mar", "Apr", "May", "June",
      "July", "Aug", "Sep", "Oct", "Nov", "Dec"]

#Both incoming models are sorted by month
dfIncoming['to_sort']=dfIncoming['month'].apply(lambda x:ordered_months.index(x))
dfIncoming = dfIncoming.sort_values('to_sort')

dfOutgoing['to_sort']=dfOutgoing['month'].apply(lambda x:ordered_months.index(x))
dfOutgoing = dfOutgoing.sort_values('to_sort')

@app.callback(
    Output('yearly_spending_graph', 'figure'),
    Input('yearly_spending_dd', 'value')
)
def update_graph(year):
    dff = dfOutgoing[dfOutgoing.iloc[:,0]==year]
    figln = px.line(dff, x='month', y='amount')
    return figln


@app.callback(
    Output('yearly_saving_graph', 'figure'),
    Input('yearly_saving_dd', 'value')
)
def update_graph(year):
    dff = dfIncoming[dfIncoming.iloc[:,0]==year]
    figln = px.line(dff, x='month', y='amount')
    return figln

def get_transaction_data():
    api = API()
    transaction_result = api.basiq_api_transaction_data
    data = json.dumps(transaction_result)
    data2 = json.loads(data)

    accounts = get_accounts()

    df = pd.json_normalize(data2)
    accounts_df = pd.json_normalize(accounts)

    processedData = df.filter(["id", "status", "amount", "direction", "account", "class", "postDate", "subClass.title"], axis=1)
    monthsForProcessing = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"]

    #Renamed 'subClass.title' as 'category'. This is not the category I was looking to use but it could do the job
    processedData.rename(columns = {'subClass.title':'category'}, inplace = True)
    return processedData
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
    transaction_result = api.basiq_api_transaction_data()
    data = json.dumps(transaction_result)
    data2 = json.loads(data)
    return data2

def get_incoming_outgoing_transactions():
    processedData = get_transaction_data()

    outgoingTransactions = processedData[processedData.amount.astype('float64') < 0]

    #transforming values to absolute value to prevent the issue mentioned above
    for index, row in outgoingTransactions.iterrows():
        row["amount"] = abs(float(row["amount"]))
        
    incomingTransactions = processedData[processedData.amount.astype('float64') > 0]

    for index, row in incomingTransactions.iterrows():
        row["amount"] = abs(float(row["amount"]))

    monthlySpending = outgoingTransactions.groupby(['year', 'month']).sum().filter(['year', 'month', 'amount'], axis=1)
    monthlySaving = incomingTransactions.groupby(['year', 'month']).sum().filter(['year', 'month', 'amount'], axis=1)

    return monthlySaving, monthlySpending

# def callback(n):
#     api = API()
#     return f"{n}"