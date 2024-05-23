from database import Session, User, Thread, Message


session = Session()


def get_or_create_user(username):
    user = session.query(User).filter_by(username=username).first()
    if not user:
        user = User(username=username)
        session.add(user)
        session.commit()
    return user


def get_or_create_thread(user):
    thread = session.query(Thread).filter_by(user_id=user.id).first()
    if not thread:
        thread_id = generate_thread_id()
        thread = Thread(user_id=user.id, thread_id=thread_id)
        session.add(thread)
        session.commit()
    return thread


def get_thread_messages(thread):
    messages = session.query(Message).filter_by(thread_id=thread.id).all()
    return [{"role": "user", "content": msg.content} if i % 2 == 0 else {"role": "assistant", "content": msg.content}
            for i, msg in enumerate(messages)]


def summarize_conversation(conversation):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=f"Суммаризируй следующую беседу:\n\n{conversation}\n\n",
        max_tokens=150
    )
    return response.choices[0].text.strip()


def handle_user_message(username, user_message):
    user = get_or_create_user(username)
    thread = get_or_create_thread(user)
    thread_messages = get_thread_messages(thread)

    # текущее сообщение пользователя
    thread_messages.append({"role": "user", "content": user_message})

    bot_response = generate_response(thread_messages, thread.thread_id)

    # Сохранение сообщений в базу данных
    user_msg = Message(thread_id=thread.id, content=user_message)
    bot_msg = Message(thread_id=thread.id, content=bot_response)
    session.add_all([user_msg, bot_msg])
    session.commit()

    # Суммаризация беседы после окончания
    conversation = "\n".join([f"{msg['role']}: {msg['content']}" for msg in thread_messages])
    summary = summarize_conversation(conversation)
    thread.summary = summary
    session.commit()

    return bot_response
