# Complete Event Scheduler Application with Advanced Features in basic Command Line Interface

from datetime import datetime

# list to store events
events = []

# Function to add a new event
def create_event(title, description, date, time):
    try:
        datetime.strptime(date, '%Y-%m-%d')
        datetime.strptime(time, '%H:%M')
        events.append({
            "title": title,
            "description": description,
            "date": date,
            "time": time
        })
        return "Event created successfully."
    except ValueError:
        return "Invalid date or time format."

# Function to list all events
def list_events():
    if not events:
        print("No events scheduled.")
        return
    sorted_events = sorted(events, key=lambda x: (x['date'], x['time']))
    for event in sorted_events:
        print(f"Title: {event['title']}, Description: {event['description']}, Date: {event['date']}, Time: {event['time']}")

# Function to delete an event
def delete_event(title):
    for i, event in enumerate(events):
        if event['title'] == title:
            del events[i]
            return "Event deleted successfully."
    return "Event not found."

# Search Functionality
def search_events(search_term):
    found_events = [event for event in events if search_term.lower() in event['title'].lower() or
                    search_term.lower() in event['description'].lower() or
                    search_term == event['date']]
    if found_events:
        for event in found_events:
            print(f"Title: {event['title']}, Description: {event['description']}, Date: {event['date']}, Time: {event['time']}")
    else:
        print("No events found matching your search criteria.")

# Editing Existing Events
def edit_event(old_title, new_title=None, new_description=None, new_date=None, new_time=None):
    for event in events:
        if event['title'] == old_title:
            if new_title: event['title'] = new_title
            if new_description: event['description'] = new_description
            if new_date: event['date'] = new_date
            if new_time: event['time'] = new_time
            print("Event updated successfully.")
            return
    print("Event not found.")

# Main interface function
def run_event_scheduler():
    while True:
        print("\n1. Create an Event\n2. List all Events\n3. Delete an Event\n4. Search Events\n5. Edit an Event\n6. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            title = input("Title: ")
            description = input("Description: ")
            date = input("Date (YYYY-MM-DD): ")
            time = input("Time (HH:MM): ")
            print(create_event(title, description, date, time))
        elif choice == "2":
            list_events()
        elif choice == "3":
            title = input("Enter the title of the event to delete: ")
            print(delete_event(title))
        elif choice == "4":
            search_term = input("Search by date (YYYY-MM-DD) or keyword: ")
            search_events(search_term)
        elif choice == "5":
            old_title = input("Enter the title of the event to edit: ")
            new_title = input("New title (leave blank to not change): ")
            new_description = input("New description (leave blank to not change): ")
            new_date = input("New date (YYYY-MM-DD, leave blank to not change): ")
            new_time = input("New time (HH:MM, leave blank to not change): ")
            edit_event(old_title, new_title or None, new_description or None, new_date or None, new_time or None)
        elif choice == "6":
            print("Exiting.")
            break
        else:
            print("Invalid option.")


run_event_scheduler()
