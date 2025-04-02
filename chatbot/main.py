import chainlit as cl 

@cl.on_message

async def main(message: cl.message):
    response = f"You said : {message.content}"

    await cl.Message(content=response).send()