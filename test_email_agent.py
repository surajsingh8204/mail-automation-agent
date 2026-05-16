"""Test script to run the email assistant agent"""

from email_assistant.email_assistant import email_assistant

# Test email input from the notebook
email_input = {
    "author": "Alice Smith <alice.smith@company.com>",
    "to": "John Doe <john.doe@company.com>",
    "subject": "Quick question about API documentation",
    "email_thread": "Hi John,\nI was reviewing the API documentation for the new authentication service and noticed a few endpoints seem to be missing from the specs. Could you help clarify if this was intentional or if we should update the docs?\nSpecifically, I'm looking at:\n- /auth/refresh\n- /auth/validate\nThanks!\nAlice"
}

print("=" * 80)
print("TESTING EMAIL ASSISTANT AGENT")
print("=" * 80)
print(f"\nEmail from: {email_input['author']}")
print(f"Subject: {email_input['subject']}")
print(f"\nContent:\n{email_input['email_thread']}")
print("\n" + "=" * 80)
print("RUNNING AGENT...")
print("=" * 80 + "\n")

# Run the agent
response = email_assistant.invoke({"email_input": email_input})

print("\n" + "=" * 80)
print("AGENT RESPONSE")
print("=" * 80 + "\n")

# Print the classification decision
print(f"Classification: {response.get('classification_decision', 'N/A')}")
print(f"\nMessages: {len(response.get('messages', []))} messages")

# Print the messages
for i, m in enumerate(response.get("messages", [])):
    print(f"\n--- Message {i+1} ---")
    m.pretty_print()

print("\n" + "=" * 80)
print("TEST COMPLETE")
print("=" * 80)
