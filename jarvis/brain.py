from openai import APIConnectionError, APIStatusError, AuthenticationError, OpenAI
from jarvis.config import settings
from jarvis.tools import TOOL_SCHEMAS, execute_tool

class Brain:                        
    def __init__(self) -> None:
        self.client = OpenAI(          
            api_key = settings.deepseek_api_key,   
            base_url = settings.deepseek_base_url, 
        )
        self.model_name = settings.chat_model 

        self.system_promt = (
            "You are Aça, a highly capable, concise, and professional personal AI assistant. "
            "You communicate naturally in Turkish while keeping technical artifacts, code, and logs in English. "
            "You have access to operating system tools. Use proactively when requested. "
        )
        self.conversation_history: list[dict] = [
            {"role": "system", "content": self.system_promt}
        ]                                                   

    def reset_memory(self) -> None:                        
        self.conversation_history = [
            {"role": "system", "content": self.system_promt}
        ]

    def think_and_act(self, user_input: str) -> str:
        self.conversation_history.append({"role": "user", "content": user_input})

        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=self.conversation_history,
                tools=TOOL_SCHEMAS,
                tool_choice="auto"
            )
            
            response_message = response.choices[0].message
            
            if response_message.tool_calls:
                self.conversation_history.append(response_message)
                
                for tool_call in response_message.tool_calls:
                    function_name = tool_call.function.name
                    function_args = tool_call.function.arguments
                    
                    print(f"\n[ARAÇ ÇAĞRISI]: {function_name} çalıştırılıyor...")
                    tool_output = execute_tool(function_name, function_args)
                    
                    self.conversation_history.append({
                        "tool_call_id": tool_call.id,
                        "role": "tool",
                        "name": function_name,
                        "content": str(tool_output),
                    })
                
                second_response = self.client.chat.completions.create(
                    model=self.model_name,
                    messages=self.conversation_history,
                )
                final_reply = second_response.choices[0].message.content
                self.conversation_history.append({"role": "assistant", "content": final_reply})
                return final_reply

            else:
                reply = response_message.content
                self.conversation_history.append({"role": "assistant", "content": reply})
                return reply

        except (AuthenticationError, APIStatusError, APIConnectionError) as e:
            return f"API İletişim Hatası: {e}"
        except Exception as e:
            return f"Beklenmeyen Hata: {e}"

brain = Brain()