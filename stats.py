def show_stats(df):

    close = df["Close"]
    print( "----Basic Stats----" )

    print( "Number of Records : " , len(df) )

    print( "Mean : " , round(close.mean(),2) )
    print( "Median : " , round(close.median(),2) )
    print( "Maximum Value : " , round(close.max(),2) )
    print( "Minimum Value : " , round(close.min(),2) )
    print( "Variance : " , round(close.var(),2) )
    print( "Standard Deviation : " , round(close.std(),2) )
    
