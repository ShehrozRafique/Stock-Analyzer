import matplotlib.pyplot as plt
from trend_analysis import moving_average

def closing_PriceChart(df) :

    plt.figure ( figsize = (10,5) )
    plt.plot ( df[ "Date" ] , df[ "Close"] )

    plt.title ( "Stock Closing Price" )
    plt.xlabel ( "Date" )
    plt.ylabel ( "Closing price" )

    plt.xticks ( rotation = 45 )
    plt.tight_layout()
    plt.show()

def Volume_Chart(df) :

    plt.figure ( figsize = (10,5) )
    plt.plot ( df[ "Date" ] , df[ "Volume"] )

    plt.title ( "Trading Volume" )
    plt.xlabel ( "Date" )
    plt.ylabel ( "Volume" )

    plt.xticks ( rotation = 45 )
    plt.tight_layout()
    plt.show()

def moving_average_chart(df) :

    df = moving_average(df)

    plt.figure( figsize= (10,5))
    plt.plot(df[ "Date" ],df[ "Close" ] , label="Close" )
    plt.plot(df[ "Date" ],df[ "MA7" ] , label="MA7" )
    plt.plot(df[ "Date" ],df[ "MA30" ] , label="MA30" )

    plt.title ( "Price and Moving Average" )
    plt.xlabel ( "Date" )
    plt.ylabel ( "Price" )

    plt.legend()
    plt.xticks ( rotation = 45 )
    plt.tight_layout()
    plt.show()

def  daily_returnChart(df) :

    df[ "Daily return" ] = df[ "Close" ].pct_change() * 100

    plt.figure( figsize= (10,5))
    plt.plot(df[ "Date" ],df[ "Daily return" ] )

    plt.title ( "Daily Returns" )
    plt.xlabel ( "Date" )
    plt.ylabel ( "Return %" )

    
    plt.xticks ( rotation = 45 )
    plt.tight_layout()
    plt.show()

def boxplot(df) :

    plt.figure( figsize= (7,5))
    plt.boxplot(df[ "Close" ])
    plt.title( "Closing price Box Plot" )
    plt.ylabel( "Price" )
    plt.show()



