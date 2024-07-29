import os
from typing_extensions import override

import streamlit as st
from openai import OpenAI
from litellm import AssistantEventHandler, get_assistants, create_thread, run_thread_stream, get_messages

os.environ["OPENAI_API_KEY"] = st.secrets["openai_api_key"]

class EventHandler(AssistantEventHandler):
  @override
  def on_text_created(self, text) -> None:
    print(f"\nassistant > ", end="", flush=True)

  @override
  def on_text_delta(self, delta, snapshot):
    print(delta.value, end="", flush=True)

  def on_tool_call_created(self, tool_call):
    print(f"\nassistant > {tool_call.type}\n", flush=True)

  def on_tool_call_delta(self, delta, snapshot):
    if delta.type == 'code_interpreter':
      if delta.code_interpreter.input:
        print(delta.code_interpreter.input, end="", flush=True)
      if delta.code_interpreter.outputs:
        print(f"\n\noutput >", flush=True)
        for output in delta.code_interpreter.outputs:
          if output.type == "logs":
            print(f"\n{output.logs}", flush=True)


class Assistant:
    def __init__(self):
        self.client = OpenAI()
        self.assistant = get_assistants(custom_llm_provider="openai").data[0]
        self.thread = create_thread(custom_llm_provider="openai",
                                    messages=[{"role": "assistant","content": "Hi, I am SCRIBE, how can I help you today?"}])

    def get_history(self):
        return get_messages(custom_llm_provider="openai", thread_id=self.thread.id).data

    def ask(self, query):
        message = {
            "role": "user",
            "content": query,
        }
        data = {"custom_llm_provider": "openai", "thread_id": self.thread.id, "assistant_id": self.assistant.id, **message}
        run = run_thread_stream(**data)
        with run as run:
            assert isinstance(run, AssistantEventHandler)
            print(run.on_message_delta)
            # for chunk in run:
            #     print(f"chunk: {chunk}")
            #     run.until_done()



assistant = Assistant()
assistant.ask("What is a VCC")

