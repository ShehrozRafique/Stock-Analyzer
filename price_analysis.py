def price_change(df):

    df[ "Price Change" ] = df[ "Close" ].diff()
    return df

def daily_return(df):

    df[ "Daily return" ] = df["Close"].pct_change() * 100
    return df

def highest_price(df):

    index = df["High"].idxmax()
    print( "---Highest Price---" )
    print( "Date : " , df.loc[index , "Date"])
    print( "Highest Price : " , df.loc[index , "High"])

def lowest_price(df):

    index = df["Low"].idxmin()
    print( "---Lowest Price---" )
    print( "Date : " , df.loc[index , "Date"])
    print( "Lowest Price : " , df.loc[index , "Low"])

def best_tradeday(df):

    df["Daily return"] = df["Close"].pct_change() * 100
    index = df[ "Daily return" ].idxmax()
    print( "---Best Trading Day---" )
    print( "Date : " , df.loc[index , "Date"])
    print( "Return: " , round(df.loc[index, "Daily return"],2) , "%" )

def Bad_tradeday(df):

    df["Daily return"] = df["Close"].pct_change() * 100
    index = df[ "Daily return" ].idxmin()
    print( "---Worst Trading Day---" )
    print( "Date : " , df.loc[index , "Date"])
    print( "Return: " , round(df.loc[index, "Daily return"],2) , "%" )




