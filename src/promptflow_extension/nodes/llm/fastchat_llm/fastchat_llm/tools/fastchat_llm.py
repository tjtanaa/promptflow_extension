from promptflow._core.tool import tool, ToolProvider
from promptflow.connections import CustomConnection
from promptflow.contracts.types import PromptTemplate
import openai

class FastChatLLM(ToolProvider):
    """
    Doc reference :
    """

    def __init__(self, connection: CustomConnection):
        super().__init__()
        self.connection = connection


    @tool
    def chat(self,
                    prompt_template: PromptTemplate, 
                    prompt: str,
                    system_prompt: str,
                    model: str,
                    max_tokens: int,
                    temperature: float,
                    top_p: float,
        ) -> str:
        # Replace with your tool code.
        # Usually connection contains configs to connect to an API.
        # Use CustomConnection is a dict. You can use it like: connection.api_key, connection.api_base
        # Not all tools need a connection. You can remove it if you don't need it.

        openai.api_key = "EMPTY"
        # print(connection.keys())

        # raise ValueError()
        print(dir(self.connection))
        print(dict(self.connection))
        openai.api_base = self.connection['api-base']
        print(openai.api_base )
        # raise ValueError()

        full_response = ""
        
        for response in openai.ChatCompletion.create(
            model=model,
            messages=([
                {
                    "role": "system",
                    "content": system_prompt
                }
            ] +
            [
                {"role": "user", "content": prompt}
            ]
            # [
            #     {"role": "user", "content": memory_str}
            # ]
            ),
            stream=True,
            temperature=temperature,
            presence_penalty=0.0,
            frequency_penalty=0.0,
            max_tokens=max_tokens,
        ):
            full_response += response.choices[0].delta.get("content", "")

        return full_response