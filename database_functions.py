import pandas as pd

def creatEmptyeDataframe():
    """ creates the empty dataframe
    """
    df = pd.DataFrame({'Username' : [], 'Friends' : [], 'Points' : []})
    return df

def createSampleDataframe(df):
    """ creates the sample dataframe
    :df: Pandas dataframe
    """
    sample = {'Username': "Johnny", 
            'Friends': ["Sarah", "Timmy", "Tobby"],
            'Points': 23}

    sample2 = {'Username': "Timmy", 
            'Friends': ["Johnny", "Sarah"],
            'Points': 12}

    sample3 = {'Username': "Sarah", 
            'Friends': ["Timmy", "Tobby"],
            'Points': 15}

    sample4 = {'Username': "Tobby", 
            'Friends': ["Johnny"],
            'Points': 41}
    
    df = df.append(sample, ignore_index=True)
    df = df.append(sample2, ignore_index=True)
    df = df.append(sample3, ignore_index=True)
    df = df.append(sample4, ignore_index=True)
    return df

def getUserFriends(username, df):
    """ gets the information for a given username within a dataframe
    :username: string of the username
    :df: Pandas dataframe
    """
    entry = list(df[df["Username"] == username]["Friends"])
    return entry

def getUserPoints(username, df):
    """ gets the information for a given username within a dataframe
    :username: string of the username
    :df: Pandas dataframe
    """
    entry = list(df[df["Username"] == username]["Points"])
    return entry