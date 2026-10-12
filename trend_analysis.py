def moving_average(df):

    df[ "MA7" ] = df[ "Close" ].rolling(7).mean()
    df[ "MA30" ] = df[ "Close" ].rolling(30).mean()

    return df

def detect_trend(df):

    first_price = df[ "Close" ].iloc[0]
    last_price = df[ "Close" ].iloc[-1]
    print( "---Trend Analysis---" )

    if last_price > first_price :

        print( "Overall Market Trend : Increasing" )

    elif last_price < first_price :

        print( "Overall Market Trend :  Decreasing" )

    else :

        print( "Stable Market" )

def daily_movements(df):

    change = df[ "Close" ].diff()
    increasing = (change > 0).sum()
    decreasing = (change < 0).sum()
    stable = (change == 0).sum()

    print( "Increasing Days :" , increasing )
    print( "Decreasing Days :" , decreasing )
    print( "Stable Days : " , stable)