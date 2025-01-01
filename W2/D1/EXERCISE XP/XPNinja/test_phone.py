from Phone import Phone

# Create phone objects
phone1 = Phone("123-456-7890")
phone2 = Phone("098-765-4321")

# Test call functionality
phone1.call(phone2)
phone2.call(phone1)

# Show call history
phone1.show_call_history()
phone2.show_call_history()

# Test message functionality
phone1.send_message(phone2, "Hello!")
phone2.send_message(phone1, "Hi! How are you?")

# Show messages
phone1.show_outgoing_messages()
phone1.show_incoming_messages()
phone1.show_messages_from("098-765-4321")