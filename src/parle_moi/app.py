import gradio as gr


def respond(message, history):
    return "Work in progress."


demo = gr.ChatInterface(fn=respond, title="Parle-moi")

if __name__ == "__main__":
    demo.launch()
