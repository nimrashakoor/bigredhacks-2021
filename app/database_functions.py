import pandas as pd


def createEmptyDataframe():
    """creates the empty dataframe"""
    df = pd.DataFrame({"Username": [], "Friends": [], "Points": []})
    return df


def createSampleDataframe():
    """creates the sample dataframe
    :df: Pandas dataframe
    """
    df = createEmptyDataframe()
    sample = {
        "Username": "Johnny",
        "Friends": ["Sarah", "Timmy", "Tobby"],
        "Points": 23,
    }

    sample2 = {"Username": "Timmy", "Friends": ["Johnny", "Sarah"], "Points": 12}

    sample3 = {"Username": "Sarah", "Friends": ["Timmy", "Tobby"], "Points": 15}

    sample4 = {"Username": "Tobby", "Friends": ["Johnny"], "Points": 41}

    df = df.append(sample, ignore_index=True)
    df = df.append(sample2, ignore_index=True)
    df = df.append(sample3, ignore_index=True)
    df = df.append(sample4, ignore_index=True)
    return df


def getUserFriends(username, df):
    """gets the information for a given username within a dataframe
    :username: string of the username
    :df: Pandas dataframe
    """
    entry = list(df[df["Username"] == username]["Friends"])
    return entry[0]


def getUserPoints(username, df):
    """gets the information for a given username within a dataframe
    :username: string of the username
    :df: Pandas dataframe
    """
    entry = list(df[df["Username"] == username]["Points"])
    return entry[0]


def addUser(username, df):
    """adds username to the given database
    :username: string of the username to be added
    :df: Pandas dataframe
    """
    # Checks if given username exists.  If they exist already, the function
    # returns none
    # if list(df[df["Username"] == username].isin([username])["Username"])[0]:
    if len(df[df["Username"] == username].isin([username])) == 1:
        return None
    else:
        df.loc[len(df.index)] = [username, [], 0]
        return df


def addPoints(username, points, df):
    """adds points to a username to the given database
    :username: string of the username to be added
    :points: int of number of points
    :df: Pandas dataframe
    """
    idx = df.index[df["Username"] == username][0]
    df.iat[idx, 2] += points
    return df


def addFriend(username, friend, df):
    """adds friends to a username to the given database
    :username: string of the username to be added
    :friend: string of friends
    :df: Pandas dataframe
    """
    idx = df.index[df["Username"] == username][0]
    df.iat[idx, 1].append(friend)
    return df


def checkUser(username, df):
    """checks if a username is in the dataframe
    :username: string of the username to be checked
    :df: Pandas dataframe
    """
    if len(df[df["Username"] == username].isin([username])) == 1:
        return True
    else:
        return False
