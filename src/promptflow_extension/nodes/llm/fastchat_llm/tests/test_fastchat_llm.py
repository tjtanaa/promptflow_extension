import pytest
import unittest

from promptflow.connections import CustomConnection
from fastchat_llm.tools.fastchat_llm import FastChatLLM


@pytest.fixture
def fastchat_custom_connection() -> CustomConnection:
    fastchat_custom_connection = CustomConnection(
        {
            "api-key" : "",
            "api-secret" : "",
            "api-base" : "http://127.0.0.1:6888/v1"
        }
    )
    return fastchat_custom_connection


@pytest.fixture
def fastchat_llm_provider(fastchat_custom_connection) -> FastChatLLM:
    fastchat_llm_provider = FastChatLLM(fastchat_custom_connection)
    return fastchat_llm_provider


class TestFastChatLLMNode:
    def test_fastchat_llm(self, fastchat_llm_provider: FastChatLLM):
        result = fastchat_llm_provider.chat( 
                            prompt_template="",
                            prompt="Microsoft", 
                            system_prompt="",
                            model="longchat-7b-v1.5-32k",
                            max_tokens=512,
                            temperature=0.01,
                            top_p=0.1,)
        print(result)
        # assert result == "Hello Microsoft"


# Run the unit tests
if __name__ == "__main__":
    unittest.main()