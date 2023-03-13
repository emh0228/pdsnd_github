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
    months = ['all', 'january', 'febraury', 'march', 'april', 'may', 'june']
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        city = input("\nPick either Chicago, New York City or Washington\n").lower()
        if city not in CITY_DATA:
            print('\nYou picked an incorrect city, please try again\n.')
            continue
        else:
            break
    while True:
        month = input("\nPick a month between January and June\n").lower()
        if month not in months:
            print('\nYou picked an incorrect month, please try again.\n')
            continue
        else:
            break
    while True:
        day = input("\nPick a day between Monday-Sunday\n").lower()
        if day not in days:
            print('\nYou picked an incorrect day, please try again.\n')
            continue
        else:
            break
    print('-' * 40)
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    if month != 'all':
        months = ['january','febraury','march','april','may','june']
        month = months.index(month) + 1
        
        df = df[df['month'] == month]
        
    if day != 'all':        
        df = df[df['day_of_week'] == day.title()]


    return df
                   
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    
    common_month = df['month'].mode()[0]
    print('\nMost Common Month to Ride Bike:', common_month)
    
    df['day_of_the_week'] = df['Start Time'].dt.day_name()
    day_of_week = df['day_of_the_week'].mode()[0]
    print('\nMost Common Day to Ride Bike:', day_of_week)
                   
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('\nThe hour of the day with the most travelers is:', most_common_hour)
                   

    # display the most common month


    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
                        
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
                        
    common_start_station = df['Start Station'].mode()[0]
    print('\nMost Common Bike Start Station:', common_start_station)
                        
    common_end_station = df['End Station'].mode()[0]
    print('\nMost Common Bike End Station:', common_end_station)
    
    combined_station = df.groupby(['Start Station', 'End Station']).size().reset_index(name='count').sort_values(by='count', ascending=False).iloc[0]
    print('\nMost Frequent Combination of Start & End Station:', combined_station)
                        
    

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
                        
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    total_time = df['Trip Duration'].sum()
    print('\nTotal Trip Duration:', total_time)
    
    mean_time = df['Trip Duration'].mean()
    print('\nAverage Trip Duration:', mean_time)
    
    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
                        
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
                        
    count_users = df['User Type'].value_counts()
    print('\nCount of Users:', count_users)
    
    if 'Gender' in df.columns:
        count_gender = df['Gender'].value_counts()
        print('\nCount of Gender:', count_gender)
        
    else:
            print('\nGender not available')
            
    if 'Birth Year' in df.columns:
        earliest_birth = df['Birth Year'].min()
        print('\nEarliest Birth Year:', int(earliest_birth))
              
        m_birth = df['Birth Year'].max()
        print('\nMost Recent Birth Year:', int(m_birth))
        
        common_birth = df['Birth Year'].mode()[0]
        print('\nMost Common Birth Year:', int(common_birth))
        
    else:
            print('\nBirth Year data not available')
    

    # Display counts of user types


    # Display counts of gender

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    start_loc = 0
    view_data = input('\nWould you like to see 5 rows of data?  Enter yes or no\n')
    
    while view_data == 'yes':
            print(df.iloc[start_loc:start_loc +5])
            start_loc += 5
            view_data = input('Do you want to Continue?: ').lower()
       
            
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
            break


if __name__ == "__main__":
	main()
