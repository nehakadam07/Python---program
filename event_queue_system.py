from collections import deque


class EventQueue:
    def __init__(self):
        self.events = deque()

    def add_event(self, event_id, description):
        # Prevent duplicate IDs among pending events
        if any(event["id"] == event_id for event in self.events):
            print(f"Event ID {event_id} is already pending.")
            return

        self.events.append({"id": event_id, "description": description})
        print(f"Added event {event_id}: {description}")

    def process_next_event(self):
        if not self.events:
            print("No events to process.")
            return

        event = self.events.popleft()
        print(f"Processed event {event['id']}: {event['description']}")

    def display_pending_events(self):
        if not self.events:
            print("No pending events.")
            return

        print("Pending events (oldest first):")
        for event in self.events:
            print(f"  {event['id']}: {event['description']}")

    def cancel_event(self, event_id):
        for event in self.events:
            if event["id"] == event_id:
                self.events.remove(event)
                print(f"Canceled event {event_id}.")
                return

        print(f"Event {event_id} is not pending and cannot be canceled.")


# Demonstration
event_queue = EventQueue()

event_queue.add_event(101, "User login")
event_queue.add_event(102, "Payment received")
event_queue.add_event(103, "Send confirmation email")

event_queue.display_pending_events()
event_queue.process_next_event()
event_queue.cancel_event(103)
event_queue.display_pending_events()