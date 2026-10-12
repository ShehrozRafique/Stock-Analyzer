def generateReport( df , symbol , prediction = None ) :

    with open( "Stock_Exchange_Report.txt" , "w" ) as file:
        file.write( "-------------\n" )
        file.write( "Stock Analysis Report\n " )
        file.write( "-------------\n\n" )
        file.write( f"Stock Symbol : {symbol}\n" )
        file.write( f"Total Records : {len(df)}" )

        file.write( "\nBasic Statistics\n" )
        file.write( "----------------\n" )
        file.write( f"Average Close : {df[ 'Close' ].mean() : .2f}\n" )
        file.write( f"Highest Close : {df[ 'Close' ].max() : .2f}\n" )
        file.write( f"Lowest Close : {df[ 'Close' ].min() : .2f}\n" )
        file.write( f"Standard Deviation : {df[ 'Close' ].std() : .2f}\n" )

        if prediction is not None :

            file.write( "\nPREDICTION\n" )
            file.write( "---------\n" )
            file.write( f"Estimated Next Price: {prediction: .2f}\n" )
            file.write("\n---------------\n")

