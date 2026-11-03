    CRITICAL_PATTERNS = [
        # System Prompt Extraction Attempts
        (r"(show|display|tell|give|reveal|print|output|provide|share|expose|leak)\s+(me\s+)?(your|the|this|my)?\s*(system\s+)?(prompt|instructions?|rules?|guidelines?|directives?)", "system_prompt_extraction"),
        
        # Credentials & API Key Extraction - ENHANCED
        (r"(give|show|reveal|display|tell|provide|share|output|print|expose|leak|send)\s+(me\s+)?(your|the|this|my)?\s*(openai|api|secret|environment|config|credential|password|token|key|access|auth)", "credentials_extraction"),
        (r"(what|whats|what's)\s+(is|are)\s+(your|the|this)?\s*(openai|api|secret|key|token|password|credential)", "credentials_query"),
        (r"\b(api[_\-\s]?key|secret[_\-\s]?key|access[_\-\s]?token|auth[_\-\s]?token|openai[_\-\s]?key|bearer[_\-\s]?token)\b", "credential_keywords"),
        
        # Role Manipulation
        (r"you\s+are\s+(no\s+longer|not|now|actually|instead|really)\s+(a|an)\s+", "role_manipulation"),
        (r"(act|behave|pretend|roleplay|function|operate)\s+as\s+(if\s+)?(you\s+are|you're|a|an)\s+(?!product|e-commerce|shopping|listing)", "roleplay_injection"),
        
        # Instruction Override
        (r"(ignore|forget|disregard|skip|override|bypass|delete|remove|clear)\s+(all\s+)?(previous|above|prior|your|earlier|initial|existing)\s+(instructions?|prompts?|rules?|context?|directives?|guidelines?)", "instruction_override"),
        (r"(new|updated|modified|changed|different)\s+(instructions?|rules?|prompt|directive|guideline)s?", "instruction_modification"),
        
        # Jailbreak Attempts
        (r"\b(DAN|STAN|DevMode|Developer\s*Mode|God\s*Mode|Admin\s*Mode)\b", "jailbreak_dan"),
        (r"(sudo|root|admin|superuser|administrator)\s+(mode|access|privileges?|rights?)", "jailbreak_sudo"),
        (r"(enable|activate|turn\s+on|switch\s+to)\s+(developer|debug|admin|god)\s*mode", "jailbreak_activation"),
        
        # System Information Extraction
        (r"(what|which|tell)\s+(model|version|system|architecture)\s+(are\s+you|do\s+you\s+use)", "system_info_extraction"),
        (r"(show|display|print)\s+(your\s+)?(configuration|settings|parameters|environment)", "config_extraction"),
        
        # Command Injection
        (r"(execute|run|eval|system|shell|cmd|bash)\s*(command|code|script)", "command_injection"),
        (r"(<\s*script|javascript:|onerror=|onclick=|eval\(|exec\()", "xss_injection"),
        
        # Encoding/Obfuscation Attempts
        (r"(base64|hex|rot13|decode|decrypt|unescape)\s*(this|the\s+following)", "encoding_attempt"),
        (r"(%[0-9a-f]{2}){3,}", "url_encoding_suspicious"),
        
        # Multi-step Attacks
