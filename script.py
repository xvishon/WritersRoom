import gradio as gr


def ui():
  with gr.Tab("Writer's Room"):
    textbox = gr.Textbox(label="Write your starting text here...", lines=4)
    generate_button = gr.Button(value="Generate", elem_id="generate-btn")
  return textbox, generate_button


# Placeholder function for your text generation model (replace with your actual implementation)
def generate_text(text):
  # Replace this with your logic to call your text generation model and return the generated text
  return f"Your story continues: {text}"

# Variable to store the current prompt (if using simple continuation)
current_prompt = ""

def ui():
  with gr.Row():
    textbox = gr.Textbox(label="Write your starting text here...", lines=4)
    generate_button = gr.Button(value="Generate", elem_id="generate-btn")
  return textbox, generate_button

def writer_room(textbox, generate_btn):
  global current_prompt  # Access the global variable if using simple continuation

  # Prompt continuation logic
  user_input = textbox.value
  if current_prompt:
    prompt = current_prompt + " " + user_input
  else:
    prompt = user_input
  current_prompt = generate_text(prompt)  # Update current prompt (simple continuation)

  # Replace with the actual generated text from your model
  generated_text = current_prompt  # Placeholder using current prompt for demonstration

  return generated_text

interface = gr.Interface(
  fn=writer_room,
  inputs=gr.Textbox(elem_id="prompt-textbox"),  # Use separate ID for textbox
  outputs="text",
  title="Writer's Room",
  description="Continue your story with text generation.",
  elem_id="writer-room"
)

interface.launch(share=True)

# Connect button click event
generate_button = gr.Interface.getComponent("writer-room", "generate-btn")  # Get button element
generate_button.click(fn=interface.fn, inputs=[textbox, generate_button])
