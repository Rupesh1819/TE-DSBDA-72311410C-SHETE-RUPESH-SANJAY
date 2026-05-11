# Smart Customer Chatbot System

"""
Time Complexity:
O(1)

Space Complexity:
O(1)
"""

print("===================================")
print("     CUSTOMER SUPPORT CHATBOT")
print("===================================")

print("\nChatbot: Hello! Welcome to Smart Customer Support.")
print("Chatbot: Type 'bye' to exit.\n")

while True:

    # Take input
    user = input("You: ").lower().strip()

    # ---------------- GREETINGS ---------------- #

    if user in ["hi", "hello", "hey", "hii", "helo"]:

        print("Chatbot: Hello! How can I assist you today?")

    # ---------------- PRODUCT MENU ---------------- #

    elif "product" in user or "products" in user:

        print("\nChatbot: Available Products:")
        print("1. Laptops")
        print("2. Mobiles")
        print("3. Headphones")
        print("4. Smart Watches")
        print("5. Accessories")
        print("\nType product name or number to know prices.")

    # ---------------- LAPTOP ---------------- #

    elif user == "1" or "laptop" in user:

        print("\nChatbot: Laptop Prices:")
        print("Dell Laptop      : ₹55,000")
        print("HP Laptop        : ₹50,000")
        print("Lenovo Laptop    : ₹48,000")

    # ---------------- MOBILE ---------------- #

    elif user == "2" or "mobile" in user:

        print("\nChatbot: Mobile Prices:")
        print("Samsung Galaxy   : ₹25,000")
        print("iPhone           : ₹70,000")
        print("OnePlus          : ₹32,000")

    # ---------------- HEADPHONES ---------------- #

    elif user == "3" or "headphone" in user:

        print("\nChatbot: Headphone Prices:")
        print("Boat             : ₹2,000")
        print("Sony             : ₹5,000")
        print("JBL              : ₹3,500")

    # ---------------- SMART WATCH ---------------- #

    elif user == "4" or "watch" in user:

        print("\nChatbot: Smart Watch Prices:")
        print("Noise            : ₹3,000")
        print("FireBoltt        : ₹2,500")
        print("Apple Watch      : ₹35,000")

    # ---------------- ACCESSORIES ---------------- #

    elif user == "5" or "accessories" in user:

        print("\nChatbot: Accessories Prices:")
        print("Keyboard         : ₹800")
        print("Mouse            : ₹500")
        print("USB Cable        : ₹300")

    # ---------------- DELIVERY ---------------- #

    elif "delivery" in user:

        print("Chatbot: Delivery takes 3 to 5 business days.")

    # ---------------- PAYMENT ---------------- #

    elif "payment" in user:

        print("Chatbot: We accept UPI, Debit Card, Credit Card, and Cash on Delivery.")

    # ---------------- RETURN POLICY ---------------- #

    elif "return" in user or "refund" in user:

        print("Chatbot: Products can be returned within 7 days.")

    # ---------------- CONTACT ---------------- #

    elif "contact" in user or "support" in user:

        print("Chatbot: Contact us at support@gmail.com")

    # ---------------- THANK YOU ---------------- #

    elif "thank" in user:

        print("Chatbot: You're welcome!")

    # ---------------- EXIT ---------------- #

    elif user == "bye":

        print("Chatbot: Thank you! Have a nice day.")
        break

    # ---------------- DEFAULT ---------------- #

    else:

        print("Chatbot: Sorry, I did not understand.")

print("\n===================================")
print("         CHAT ENDED")
print("===================================")