from get_data import send_link

def handle_response(message):
    message = message.lower()
    if message == "play":
        return send_link()

    return "Did you mean play?"