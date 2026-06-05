import re

class IntentClassifier:
    def __init__(self):
        # Explicit conversational matching groups
        self.greeting_patterns = [
            r"\b(hi|hello|hey|greetings|good morning|good afternoon|good evening)\b",
            r"\b(how are you|how\'s it going|what\'s up)\b"
        ]
        
        self.identity_patterns = [
            r"\b(who are you|your name|what are you|who am i speaking to)\b"
        ]

    def predict(self, text: str) -> str:
        """Routes user strings to either conversation blocks or the RAG knowledge search."""
        clean_text = text.lower().strip()
        
        for pattern in self.greeting_patterns:
            if re.search(pattern, clean_text):
                return "greeting"
                
        for pattern in self.identity_patterns:
            if re.search(pattern, clean_text):
                return "identity"
                
        # Default route: Send everything else straight to the RAG database engine
        return "knowledge_query"