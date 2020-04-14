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
    city = input("Please input city name:(chicago, new york city, washington) ").lower()

    while city not in ['chicago', 'new york city', 'washington']:
        city = input("invalid input! Please input another name:").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("input month name:(all, january, february, ... , june) ").lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please input day of week:(all, monday, tuesday, ... sunday) ").lower()


    print('-'*40)
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
    df = pd.read_csv(CITY_DATA[city.replace(" ","_")])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]



    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('Most common month:',df['month'].mode()[0])


    # TO DO: display the most common day of week
    print('Most common day of the week:',df['day_of_week'].mode()[0])


    # TO DO: display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    print('Most common start hour:',df['start_hour'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most common start station:',df['Start Station'].mode()[0])



    # TO DO: display most commonly used end station
    print('Most common end station:',df['End Station'].mode()[0])



    # TO DO: display most frequent combination of start station and end station trip
    df['combine'] = df['Start Station']+ " " + df['End Station']
    print("The most common start and end station combo is:",df['combine'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df['duration'] = df['End Time'] - df['Start Time']


    # TO DO: display total travel time
    print("The total travel time is:",df['duration'].sum())


    # TO DO: display mean travel time
    print("The total travel time is:",df['duration'].mean())



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("count of user types:",df['User Type'].value_counts())



    # TO DO: Display counts of gender
    if city =="washington":
        print("there is no more user data")

    if city != 'washington':
        print("gender counts",df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
        print("The earliest birth year is:",df['Birth Year'].min())
        print("The latest birth year is:",df['Birth Year'].max())
        print("The most common birth year is:",df['Birth Year'].mode()[0])






    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):

    user_req = input("Do you want to see the raw data?:(yes/no) ").lower()




    if user_req == 'yes':
        start = 0
        end = 5
        while end <= df.shape[0] - 1:

            print(df.iloc[start:end,:])
            start += 5
            end += 5

            end_display = input("Do you want to continue?:(yes/no) ").lower()
            if end_display == 'no':
                break





def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
