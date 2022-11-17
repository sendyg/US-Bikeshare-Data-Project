import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Choose a city from (chicago, new york city, washington): ").lower()
    while city not in CITY_DATA.keys():
        print('Please choose from the available cities')
        city = input("Choose a city from (chicago, new york city, washington): ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input("Choose month of the year: ").lower()
        if month in MONTHS:
            break
        else:
            print('Please choose from january to june or choose all')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
        day = input("choose day of the week: ").lower()
        if day in DAYS:
            break
        else:
            Print('Please write the name of the day')

    print('-'*40)
    print("Great! Let's check.")
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['start hour'] = df['Start Time'].dt.hour
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
        month = MONTHS.index(month) + 1
        df = df[df['month'] == month] # filter by month to create the new dataframe
        
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common month: {}'.format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print('The most common day of the week: {}'.format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    print('The most common start hour: {}'.format(df['start hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commonly used start station: {}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print("The most common end station: {}".format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['route']=df['Start Station']+","+df['End Station']
    print('The most frequent combination station: '.format(df['route'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The total travel time: ',(df['Trip Duration'].sum()).round())

    # TO DO: display mean travel time
    print('The average travel time: ',(df['Trip Duration'].mean()).round())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts().to_frame())

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print(df['Gender'].value_counts().to_frame())

    # TO DO: Display earliest, most recent, and most common year of birth
        print('The most earliest year of birth: ',int(df['Birth Year'].min()))
        print('The most recent year of birth: ',int(df['Birth Year'].max()))
        print('The most common year of birth: ',int(df['Birth Year'].mode()[0]))
    else:
        print('Some data is not available in your city choice')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_data(df):
    """
    To display raw data if requested upon user input.
    """
    print('There are raw data available to display.')
    
    i = 0  # i as in index
    user_requested = input('Would you like to check 5 rows of raw data?, type yes or no: ').lower()
    if user_requested not in ['yes', 'no']:
        print('That\'s not the choice, please type yes or no')
        user_requested = input('Would you like to continue?, type yes or no: ').lower()
    elif user_requested != 'yes':
        print('That\'s fine as well.')
    else:
        while i+5 < df.shape[0]:
            print(df.iloc[i:i+5])
            i += 5
            user_requested = input('Would you like to display 5 rows more of raw data? ').lower()
            if user_requested != 'yes':
                print('That\'s fine as well.')
                break
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('That\'s fine.')
            break


if __name__ == "__main__":
	main()