conversation_store = {}


def save_message(user_id, role, message):

    if user_id not in conversation_store:
        conversation_store[user_id] = []

    conversation_store[user_id].append({
        "role": role,
        "message": message
    })


def get_history(user_id):

    return conversation_store.get(
        user_id,
        []
    )