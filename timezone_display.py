import pytz
import datetime

countries = []
while len(countries) < 9:
    print("Choose up to 9 timezone ({} of 9 countries has been selected)".format(str(len(countries))))
    print("MENU:")
    for i,country in enumerate(pytz.country_names):
        number_list = str(i+1) + "."
        if country in pytz.country_timezones:
            print(number_list,country,pytz.country_names[country],pytz.country_timezones[country])
    user_choice = input("Input your choice:\n")
    if user_choice == "0":
        break
    elif user_choice.upper() in pytz.country_timezones:
        print(pytz.country_timezones[user_choice.upper()])
        countries.append(user_choice.upper())
        input("Press enter to continue...")
    else:
        print("Please enter the correct input!")

print("Showing times:")
for country in sorted(countries):
    for zone in sorted(pytz.country_timezones[country]):
        tz_to_display = pytz.timezone(zone)
        local_time = datetime.datetime.now(tz=tz_to_display)
        print("{}: {}".format(zone,local_time))