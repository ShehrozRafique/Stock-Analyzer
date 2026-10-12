def volume_analysis(df):

    volume = df[ "Volume" ] 
    print( "---VOLUME ANALYSIS---" )
    print( "Average Volume :" , round(volume.mean(),2) )
    print( "Highest Volume : " , volume.max() )
    print( "Lowest Volume : ", volume.min() )

def highest_volume_day(df):

    index = df["Volume"].idxmax()
    print( "---Highest Volume Day---" )
    print( "Date : " , df.loc[index , "Date"])
    print( "Volume : " , df.loc[index , "Volume"])

def lowest_volume_day(df):

    index = df["Volume"].idxmin()
    print( "---Highest Volume Day---" )
    print( "Date : " , df.loc[index , "Date"] )
    print( "Volume : " , df.loc[index , "Volume"] )
