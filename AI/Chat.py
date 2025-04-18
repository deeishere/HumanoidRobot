import requests
import json

DEEPSEEK_API_KEY = "sk-ff9ba23189d54b9687b733f1a6cdedcb"
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"


class DeepSeekChat:
    def __init__(self, api_key):
        self.api_key = DEEPSEEK_API_KEY
        self.api_url = DEEPSEEK_API_URL  # Verify this is the correct endpoint
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
    
    def chat(self, messages, model="deepseek-chat", temperature=0.7, max_tokens=1000):
        """
        Send a chat request to DeepSeek API
        
        Args:
            messages: List of message objects with 'role' and 'content'
            model: DeepSeek model to use
            temperature: Sampling temperature (0.0 to 1.0)
            max_tokens: Maximum number of tokens to generate
            
        Returns:
            The API response as a Python dictionary
        """
        payload = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        
        try:
            response = requests.post(
                self.api_url,
                headers=self.headers,
                data=json.dumps(payload)
            )
            response.raise_for_status()  # Raise exception for HTTP errors
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error calling DeepSeek API: {e}")
            return None

# Example usage
if __name__ == "__main__":
    api_key = DEEPSEEK_API_KEY  # Replace with your actual API key
    deepseek = DeepSeekChat(api_key)
     
    # Example conversation
    messages = [
        {"role": "system", "content": "You are a bilingual helpful assistant for a drone and robotics club. You speak arabic and english. Always respond in short and concise manner. Reply in english when asked in english and in arabic when asked in arabic."},
        {"role": "user", "content": "ما تفعل"}
    ]
    
    response = deepseek.chat(messages)
    
    if response:
        # Extract and print the assistant's response
        assistant_message = response["choices"][0]["message"]["content"]
        print(f"DeepSeek AI: {assistant_message}")
